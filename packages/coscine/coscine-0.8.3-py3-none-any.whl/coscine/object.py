###############################################################################
# Coscine Python SDK
# Copyright (c) 2018-2022 RWTH Aachen University
# Licensed under the terms of the MIT License
###############################################################################
# Coscine, short for Collaborative Scientific Integration Environment is
# a platform for research data management (RDM).
# For more information on Coscine visit https://www.coscine.de/.
#
# Please note that this python module is open source software primarily
# developed and maintained by the scientific community. It is not
# an official service that RWTH Aachen provides support for.
###############################################################################

###############################################################################
# File description
###############################################################################

"""
Implements classes and routines for manipulating Metadata and interacting
with files and file-like data in Coscine.
"""

###############################################################################
# Dependencies
###############################################################################

from __future__ import annotations
from datetime import datetime
from typing import List, Optional, TYPE_CHECKING, Callable, Union
import os
import posixpath
import logging
import dateutil.parser
from prettytable.prettytable import PrettyTable
from coscine.graph import ApplicationProfile
from coscine.form import InputForm, FormField
from coscine.utils import HumanBytes, ProgressBar
if TYPE_CHECKING:
	from coscine.client import Client
	from coscine.resource import Resource

###############################################################################
# Module globals / Constants
###############################################################################

logger = logging.getLogger(__name__)

###############################################################################
# Classes / Functions / Scripts
###############################################################################

class MetadataForm(InputForm):
	"""
	The MetadataForm supports parsing coscine.Object metadata, generating
	metadata and manipulating it in the same way one would manipulate
	a python dict.
	"""

	profile: ApplicationProfile

###############################################################################

	def __init__(self, client: Client, graph: ApplicationProfile) -> None:
		"""
		Initializes an instance of type MetadataForm.

		Parameters
		----------
		client : Client
			Coscine Python SDK client handle
		graph : ApplicationProfile
			Coscine application profile rdf graph
		"""

		super().__init__(client)
		self.profile = graph
		self._fields = [
			FormField(client, item) for item in self.profile.items()
		]
		# Query vocabularies for controlled fields
		for field in self._fields:
			if field.vocabulary:
				instance = client.vocabularies.instance(field.vocabulary)
				self._vocabularies[field.path] = instance

###############################################################################

	def generate(self) -> dict:
		"""
		Generates and validates metadata for sending to Coscine.
		"""

		metadata = {}
		metadata[ApplicationProfile.RDFTYPE] = [{
			"type": "uri",
			"value": self.profile.target()
		}]

		# Collect missing required fields
		missing = []

		# Set metadata
		for key, values in self.items():
			if not values:
				if self.is_required(key):
					missing.append(key)
				continue

			properties = self.properties(key)
			metadata[properties.path] = []
			raw_value = values.raw()
			if not isinstance(raw_value, list):
				raw_value = [raw_value]
			for value in raw_value:
				entry = {
					"value": value,
					"datatype": (properties.datatype if properties.datatype
												else properties.vocabulary),
					"type": "uri" if properties.vocabulary else "literal"
				}
				if not entry["datatype"]:
					del entry["datatype"]
				metadata[properties.path].append(entry)

		# Check for missing required fields
		if len(missing) > 0:
			raise ValueError(missing)

		return metadata

###############################################################################

	def parse(self, data: Union[dict, None]) -> None:
		if data is None:
			return
		for path, values in data.items():
			if path == ApplicationProfile.RDFTYPE:
				continue
			try:
				key = self.name_of(path)
				self.set_value(key, [v["value"] for v in values], True)
			except KeyError:
				continue

###############################################################################
###############################################################################
###############################################################################

class FileObject:
	"""
	Objects in Coscine represent file-like data. We could have called it
	'File', but in case of linked data we are not actually dealing with files
	themselves, but with links to files.Thus we require a more general
	datatype.
	"""

	client: Client
	resource: Resource
	data: dict
	_cached_metadata: Optional[dict]  # None in case of no metadata
	_metadata_cache_is_invalid: bool

	@property
	def has_metadata(self) -> bool:
		"""
		Evaluates whether the FileObject has metadata attached to it
		"""
		return bool(self._cached_metadata)

	@property
	def name(self) -> str:
		"""
		FileObject name
		"""
		return self.data["Name"]

	@property
	def size(self) -> int:
		"""
		FileObject size in bytes
		"""
		return int(self.data["Size"])

	@property
	def type(self) -> str:
		"""
		FileObject type, e.g. 'file' or 'folder'
		"""
		return self.data["Kind"]

	@property
	def modified(self) -> datetime:
		"""
		Last time the FileObject was modified
		"""
		if not self.data["Modified"]:
			return datetime(1900, 1, 1)
		return dateutil.parser.parse(self.data["Modified"])

	@property
	def created(self) -> datetime:
		"""
		Time the FileObject was created
		"""
		if not self.data["Created"]:
			return datetime(1900, 1, 1)
		return dateutil.parser.parse(self.data["Created"])

	@property
	def provider(self) -> str:
		"""
		Resource type
		"""
		return self.data["Provider"]

	@property
	def filetype(self) -> str:
		"""
		FileObject file type, e.g. '.png'
		"""
		return os.path.splitext(self.data["Name"])[1]

	@property
	def path(self) -> str:
		"""
		FileObject path including folders (in case of S3 resources)
		"""
		return self.data["Path"]

	@property
	def is_folder(self) -> bool:
		"""
		Evaluates to true if the FileObject resembles a folder (only S3)
		"""
		return bool(self.data["IsFolder"])

	CHUNK_SIZE: int = 4096

###############################################################################

	def __init__(self, resource: Resource, data: dict,
				metadata: Optional[dict] = None) -> None:
		"""
		Initializes the Coscine FileObject.

		Parameters
		----------
		resource : Resource
			Coscine resource handle.
		data : dict
			data of the file-like object.
		"""

		# Configuration
		self.client = resource.client
		self.resource = resource
		self.data = data
		self._cached_metadata = metadata
		self._metadata_cache_is_invalid = False

###############################################################################

	def __str__(self) -> str:
		table = PrettyTable(("Property", "Value"))
		rows = [
			("Name", self.name),
			("Size", HumanBytes.format(self.size)),
			("Type", self.type),
			("Path", self.path),
			("Folder", self.is_folder)
		]
		table.max_width["Value"] = 50
		table.add_rows(rows)
		return table.get_string(title=f"Object {self.name}")

###############################################################################

	def metadata(self, force_update: bool = False) -> Union[dict, None]:
		"""
		Retrieves the metadata of the file-like object.

		Parameters
		----------
		force_update : bool, default: False
			Normally, metadata is cached and that cache is only updated
			when an action is performed via the Coscine Python SDK, that
			would invalidate that cache (e.g. update()).
			By setting force_update to True, metadata is always fetched
			from Coscine, ignoring the cache. Keep in mind that fetching
			the metadata from every file in a resource will result in a
			seperate request for each file, while with caching it only
			fetches all metadata once.

		Returns
		-------
		dict
			Metadata as a python dictionary.
		None
			If no metadata has been set for the file-like object.
		"""

		if not (force_update or self._metadata_cache_is_invalid):
			if self._cached_metadata:
				for key in self._cached_metadata:
					return self._cached_metadata[key]
			return None
		uri = self.client.uri("Tree", "Tree", self.resource.id)
		args = {"path": self.path}
		data = self.client.get(uri, params=args).json()
		metadata = data["data"]["metadataStorage"]
		if not metadata:
			return None
		metadata = metadata[0]
		for key in metadata:
			self._cached_metadata = metadata
			self._metadata_cache_is_invalid = False
			return metadata[key]
		return None

###############################################################################

	def update(self, metadata: Union[MetadataForm, dict]) -> None:
		"""
		Updates the metadata of the file-like object.

		Parameters
		----------
		metadata : MetadataForm or dict
			MetadataForm or JSON-LD formatted metadata dict

		Raises
		------
		TypeError
			If argument `metadata` has an unexpected type.
		"""

		if isinstance(metadata, MetadataForm):
			metadata = metadata.generate()
		elif not isinstance(metadata, dict):
			raise TypeError("Expected MetadataForm or dict.")
		logger.info(f"Updating metadata of FileObject '{self.path}'...")
		uri = self.client.uri("Tree", "Tree", self.resource.id)
		self.client.put(uri, params={"path": self.path}, json=metadata)
		self._metadata_cache_is_invalid = True  # Invalidate cached metadata

###############################################################################

	def content(self) -> bytes:
		"""
		Retrieves the content/data of the object. In case of linked data
		this would be the link, not the actual file itself. It is impossible
		to get the file contents of linked data objects with this python module.
		In case of rds or rds-s3 data this would return the file contents.
		Be aware that for very large files this will consume a considerable
		amount of RAM!

		Returns
		-------
		bytes
			A raw byte-array containing the Coscine file-object's data.
		"""

		uri = self.client.uri("Blob", "Blob", self.resource.id)
		return self.client.get(uri, params={"path": self.path}).content

###############################################################################

	def download(
		self,
		path: str = "./",
		callback: Optional[Callable[[int], None]] = None,
		preserve_path: Optional[bool] = False
	) -> None:
		"""
		Downloads the file-like object to the local harddrive.

		Parameters
		----------
		path : str, default: "./"
			The path to the download location on the harddrive.
		callback : function(chunksize: int)
			A callback function to be called during downloading chunks.
		preserve_path : bool, default: False
			Preserve the folder structure, i.e. if the file object is located
			in a subfolder, create said subfolder if it does not exist yet
			on the local harddrive and put the file in there.
		"""

		logger.info(f"Downloading FileObject '{self.path}'...")
		if self.is_folder:
			if preserve_path:
				path = posixpath.join(path, self.path)
				os.makedirs(path, exist_ok=True)
			else:
				raise TypeError("FileObject is a folder! "
					"Set 'preserve_path=True' to download folders.")
		else:
			uri = self.client.uri("Blob", "Blob", self.resource.id)
			args = {"path": self.path}
			response = self.client.get(uri, params=args, stream=True)
			if preserve_path:
				path = posixpath.join(path, self.path)
			else:
				path = os.path.join(path, self.name)
			with open(path, 'wb') as fd:
				progress_bar = ProgressBar(self.client.settings.verbose,
										self.size, self.name, callback)
				for chunk in response.iter_content(chunk_size=self.CHUNK_SIZE):
					fd.write(chunk)
					progress_bar.update(len(chunk))

###############################################################################

	def delete(self) -> None:
		"""
		Deletes the file-like object on the Coscine server.
		"""

		logger.info(f"Deleting FileObject '{self.path}'...")
		uri = self.client.uri("Blob", "Blob", self.resource.id)
		self.client.delete(uri, params={"path": self.path})

###############################################################################

	def objects(self, path: str = "") -> List[FileObject]:
		"""
		Returns a list of FileObjects resembling the contents of
		the current object in case the current object is a folder.
		Irrelevant for anything other than S3 resources.

		Parameters
		-----------
		path : str, default: None
			Path to a directory. Irrelevant for anything other than S3.

		Returns
		-------
		List[FileObject]
			A list of file objects.

		Raises
		-------
		TypeError
			In case the current FileObject is not a folder or not part of an
			S3 resource.
		"""
		if self.is_folder:
			fullpath = posixpath.join(self.path, path)
			return self.resource.objects(fullpath)
		raise TypeError(f"FileObject '{self.path}' is not a directory!")

###############################################################################

	def object(self, path: str) -> Optional[FileObject]:
		"""
		Returns a FileObject resembling a file inside of
		the current object in case the current object is a folder.
		Irrelevant for anything other than S3 resources.

		Parameters
		-----------
		path : str
			Path to the file or folder.

		Raises
		-------
		TypeError
			In case the current FileObject is not a folder or not part of an
			S3 resource.
		"""
		if self.is_folder:
			fullpath = posixpath.join(self.path, path)
			return self.resource.object(fullpath)
		raise TypeError(f"FileObject '{self.path}' is not a directory!")

###############################################################################

	def form(self) -> MetadataForm:
		"""
		Returns a MetadataForm to interact with the metadata of the FileObject.
		"""

		graph = self.resource.application_profile()
		form = MetadataForm(self.client, graph)
		form.parse(self.metadata())
		return form

###############################################################################
