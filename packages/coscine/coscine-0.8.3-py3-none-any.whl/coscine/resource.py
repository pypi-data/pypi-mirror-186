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
This file defines the resource object for the representation of
Coscine resources. It provides an easy interface to interact with Coscine
resources from python.
"""

###############################################################################
# Dependencies
###############################################################################

from __future__ import annotations
import json
import os
import posixpath
import logging
from concurrent.futures import ThreadPoolExecutor, wait
from typing import Callable, TYPE_CHECKING, Union, List, Optional
import urllib.parse
import csv
from requests_toolbelt import MultipartEncoder, MultipartEncoderMonitor
from prettytable.prettytable import PrettyTable
import rdflib
from coscine.object import FileObject, MetadataForm
from coscine.form import InputForm
from coscine.graph import ApplicationProfile
from coscine.utils import ProgressBar
from coscine.s3 import S3
if TYPE_CHECKING:
	from coscine.client import Client
	from coscine.project import Project

###############################################################################
# Module globals / Constants
###############################################################################

logger = logging.getLogger(__name__)

###############################################################################
# Classes / Functions / Scripts
###############################################################################

class ResourceForm(InputForm):
	"""
	An InputForm for Coscine Resource metadata.
	"""

###############################################################################

	def __init__(self, client: Client) -> None:
		"""
		Parameters
		-----------
		client : Client
			Coscine Python SDK Client instance
		"""
		super().__init__(client)
		self._fields = client.vocabularies.builtin("resource")
		vocabularies = {
			"type": client.vocabularies.resource_types(True),
			"applicationProfile": client.vocabularies.application_profiles(True),
			"license": client.vocabularies.licenses(True),
			"visibility": client.vocabularies.visibility(True),
			"disciplines": client.vocabularies.disciplines(True)
		}
		for item in self._fields:
			if item.vocabulary:
				self._vocabularies[item.path] = vocabularies[item.path]

###############################################################################

	def parse(self, data: dict) -> None:
		ignore = ["id", "pid", "fixedValues", "creator", "archived"]
		for path, value in data.items():
			if path not in ignore:
				try:
					key = self.name_of(path)
					self.set_value(key, value, True)
				except KeyError:
					continue

###############################################################################

	def generate(self) -> dict:
		metadata = {}

		# Collect missing required fields
		missing: List[str] = []

		# Set metadata
		for key, value in self.items():
			if value is None:
				if self.is_required(key):
					missing.append(key)
				continue

			properties = self.properties(key)
			metadata[properties.path] = value.raw()
			# The resourceTypeOption requires a dict with additional
			# 'Size' field in it.
			if properties.path == "resourceTypeOption":
				metadata[properties.path] = {
					"Size": value.raw()
				}

		# Check for missing required fields
		if len(missing) > 0:
			if not (
				len(missing) == 1
				and missing[0] == "resourceTypeOption"
				and metadata["type"] == "linked"
			):
				raise ValueError(missing)

		return metadata

###############################################################################
###############################################################################
###############################################################################

class Resource:
	"""
	Python representation of a Coscine Resource type.
	"""

	client: Client
	project: Project
	data: dict
	s3: Optional[S3]

###############################################################################

	def __init__(self, project: Project, data: dict) -> None:
		"""
		Initializes a Coscine resource object.

		Parameters
		----------
		project : Project
			Coscine project handle
		data : dict
			Resource data received from Coscine.
		"""

		self.project = project
		self.client = self.project.client
		self.data = data
		self.s3 = S3(data, self.client.settings.verbose)

###############################################################################

	@property
	def id(self) -> str:
		"""Resource ID"""
		return self.data["id"]

	@property
	def pid(self) -> str:
		"""Resource Persistent Identifier"""
		return self.data["pid"]

	@property
	def name(self) -> str:
		"""Resource Name"""
		return self.data["resourceName"]

	@property
	def display_name(self) -> str:
		"""Resource Display Name"""
		return self.data["displayName"]

	@property
	def description(self) -> str:
		"""Resource Description"""
		return self.data["description"]

	@property
	def license(self) -> str:
		"""Resource License Name"""
		return (self.data["license"]["displayName"]
			if self.data["license"] else "")

	@property
	def type(self) -> str:
		"""Resource Type e.g. rdss3rwth"""
		return self.data["type"]["displayName"]

	@property
	def disciplines(self) -> List[str]:
		"""Associated Disciplines"""
		lang = {
			"en": "displayNameEn",
			"de": "displayNameDe"
		}[self.client.settings.language]
		return [k[lang] for k in self.data["disciplines"]]

	@property
	def profile(self) -> str:
		"""Name of the Application Profile used in the Resource"""
		return self.data["applicationProfile"]

	@property
	def archived(self) -> bool:
		"""Status indicator, indicating whether the resource is archived"""
		return bool(self.data["archived"])

	@property
	def creator(self) -> str:
		"""Resource Creator"""
		return self.data["creator"]

###############################################################################

	def __str__(self) -> str:
		table = PrettyTable(["Property", "Value"])
		rows = [
			("ID", self.id),
			("Resource Name", self.name),
			("Display Name", self.display_name),
			("Description", self.description),
			("PID", self.pid),
			("Type", self.type),
			("Disciplines", "\n".join(self.disciplines)),
			("License", self.license),
			("Application Profile", self.profile),
			("Archived", self.archived),
			("Creator", self.creator),
			("Project", self.project.display_name),
			("Project ID", self.project.id)
		]
		table.max_width["Value"] = 50
		table.add_rows(rows)
		return table.get_string(title=f"Resource {self.display_name}")

###############################################################################

	def delete(self) -> None:
		"""
		Deletes the Coscine resource and all objects contained within it on
		the Coscine servers.
		"""

		logger.info(f"Deleting resource '{self.name}' ({self.id})...")
		uri = self.client.uri("Resources", "Resource", self.id)
		self.client.delete(uri)

###############################################################################

	def application_profile(self) -> ApplicationProfile:
		"""
		Returns the application profile of the resource.
		"""

		return self.client.vocabularies.application_profile(self.profile)

###############################################################################

	def download_metadata(self, path: str = "./", format: str = "csv") -> None:
		"""
		Downloads the metadata of the file objects stored within the resource
		in the specified format.

		Parameters
		----------
		format : str, default: "csv"
			The file format to store the data in. Available formats are:
			"json", "csv"

		Raises
		-------
		ValueError
			In case of an unexpected format.
		"""

		if format == "csv":
			with open(
				os.path.join(path, ".file-metadata.csv"),
				"w", encoding="utf-8", newline=""
			) as fd:
				csvwriter = csv.writer(fd)
				csvwriter.writerow(["File"] + self.metadata_form().keys())
				for obj in self.contents():
					values = [obj.path] + [
						str(value) for value in obj.form().values()
					]
					csvwriter.writerow(values)
		elif format == "json":
			metadata = []
			keys = ["File"] + self.metadata_form().keys()
			for obj in self.contents():
				values = [obj.path] + [
					str(value) for value in obj.form().values()
				]
				entry = {
					keys[i]: values[i] for i in range(len(keys))
				}
				metadata.append(entry)
			with open(
				os.path.join(path, ".file-metadata.json"),
				"w", encoding="utf-8"
			) as fp:
				json.dump(metadata, fp)
		else:
			raise ValueError("Unexpected metadata format!")

###############################################################################

	def _download_concurrently(self, path: str = "./") -> None:
		with ThreadPoolExecutor(max_workers=4) as executor:
			files = self.contents()
			futures = [
				executor.submit(file.download, path, None, True)
				for file in files
			]
			wait(futures)  # Exciting, I went long with leveraged calls
			for future in futures:
				future.result()

###############################################################################

	def download(self, path: str = "./", metadata: bool = False) -> None:
		"""
		Downloads the resource and all of its contents to the local harddrive.

		Parameters
		----------
		path : str, default: "./"
			Path to the local storage location.
		metadata : bool, default: False
			If enabled, resource metadata is downloaded and put in
			the file '.resource-metadata.json'.
		"""

		logger.info(f"Downloading resource '{self.name} ({self.id})...")
		path = os.path.join(path, self.name)
		if not os.path.isdir(path):
			os.mkdir(path)
		if self.client.settings.concurrent:
			self._download_concurrently(path)
		else:
			for obj in self.contents():
				obj.download(path, preserve_path=True)
		if metadata:
			self.download_metadata(path)
			data = json.dumps(self.data, indent=4)
			metadata_path: str = os.path.join(path, ".resource-metadata.json")
			with open(metadata_path, "w", encoding="utf-8") as file:
				file.write(data)

###############################################################################

	def exists(self, path: str) -> bool:
		"""
		Returns whether the file referenced by key is contained
		in the resource.

		Parameters
		-----------
		path : str
			The key/path to the file object

		Returns
		-------
		bool
			True if file object exists, False if not
		"""
		return self.object(path) is not None

###############################################################################

	def contents(self) -> List[FileObject]:
		"""
		Returns a list of ALL Objects stored within the resource
		by recursively traversing directories

		Returns
		-------
		List[FileObject]
			List of Coscine file-like objects.
		"""

		more_folders: bool = True
		contents = []
		directories = []
		files = self.objects()
		while more_folders:
			more_folders = False
			for obj in files:
				if obj.is_folder:
					files.remove(obj)
					directories.append(obj)
					files.extend(obj.objects())
					more_folders = True
		contents.extend(directories)
		contents.extend(files)
		return contents

###############################################################################

	def objects(self, path: Optional[str] = None) -> List[FileObject]:
		"""
		Returns a list of Objects stored within the resource.

		Parameters
		------------
		path : str, default: None
			Path to a directory. Irrelevant for anything other than S3.

		Examples
		---------
		>>> Resource.objects(path="Folder/Subfolder")
		Returns all objects inside 'Folder/Subfolder' (s3 resources only)

		Returns
		-------
		List[FileObject]
			List of Coscine file-like objects.
		"""

		objects = []
		uri = self.client.uri("Tree", "Tree", self.id)
		dirpath = posixpath.dirname(path) if path else None
		args = {"path": path} if dirpath and dirpath != "/" else None
		data = self.client.get(uri, params=args).json()
		file_storage: List[dict] = data["data"]["fileStorage"]
		metadata_storage: List[dict] = data["data"]["metadataStorage"]
		for data in file_storage:
			path = urllib.parse.quote("/" + data["Path"], safe="")
			metadata: dict = {}
			for meta in metadata_storage:
				if list(meta.keys())[0].endswith(f"@path={path}"):
					metadata = meta
					break
			objects.append(FileObject(self, data, metadata))
		return objects

###############################################################################

	def object(self, path: str) -> Union[FileObject, None]:
		"""
		Returns an Object stored within the resource

		Parameters
		------------
		path : str, default: None
			Path to a directory. Irrelevant for anything other than S3.

		Examples
		---------
		>>> Resource.object(path="Folder/Subfolder/Filename.jpg")
		Returns the file inside 'Folder/Subfolder' (s3 resources only)

		Returns
		-------
		FileObject
			Python representation of the file-object as an Object instance
		None
			In case nothing was found.

		Raises
		------
		IndexError
			In case more than 1 FileObject was found at the path.
		"""

		dirpath = posixpath.join(posixpath.dirname(path), "")
		dirpath = dirpath if dirpath != "/" else ""
		filename = posixpath.basename(path)
		if not filename:
			filename = posixpath.dirname(dirpath)
			dirpath = ""
		filtered_list = list(filter(lambda fo: fo.name == filename,
									self.objects(path=dirpath)))
		if len(filtered_list) == 1:
			return filtered_list[0]
		if len(filtered_list) == 0:
			return None
		raise IndexError("Found more than 1 FileObject matching "
									"the specified criteria!")

###############################################################################

	def upload(
		self,
		key: str,
		file,
		metadata: Union[MetadataForm, dict],
		callback: Optional[Callable[[int], None]] = None
	) -> None:
		"""
		Uploads a file-like object to a resource on the Coscine server

		Parameters
		----------
		key : str
			filename of the file-like object.
		file : object with read() attribute
			Either open file handle or local file location path.
		metadata : MetadataForm or dict
			File metadata matching the resource application profile.
		callback : Callable[[int], None], default: None
			Optional callback called during chunk uploads
			indicating the progress.

		Raises
		------
		TypeError
			In case the file object specified cannot be used.
		"""

		logger.info(f"Uploading FileObject '{key}' to "
					f"resource '{self.name}' ({self.id})...")
		if hasattr(file, "read"):
			self._upload_file_metadata(key, metadata)
			self._upload_file_data(key, file, callback)
		elif isinstance(file, str):
			with open(file, "rb") as fp:
				self._upload_file_metadata(key, metadata)
				self._upload_file_data(key, fp, callback)
		else:
			raise TypeError("Argument `file` has unexpected type!")

###############################################################################

	def _upload_file_metadata(self, key: str, metadata) -> None:
		if isinstance(metadata, MetadataForm):
			metadata = metadata.generate()
		uri = self.client.uri("Tree", "Tree", self.id)
		params = {"path": key}
		self.client.put(uri, json=metadata, params=params)

###############################################################################

	def _upload_file_data(
		self,
		key: str,
		file_handle,
		callback: Optional[Callable[[int], None]] = None
	) -> None:
		uri = self.client.uri("Blob", "Blob", self.id)
		fields = {"files": (key, file_handle, "application/octect-stream")}
		encoder = MultipartEncoder(fields=fields)
		progress_bar = ProgressBar(self.client.settings.verbose,
								encoder.len, key, callback)
		monitor = MultipartEncoderMonitor(encoder, callback=lambda monitor:
				progress_bar.update(monitor.bytes_read - progress_bar.count))
		headers = {"Content-Type": monitor.content_type}
		params = {"path": key}
		self.client.put(uri, data=monitor, headers=headers, params=params)

###############################################################################

	def set_archived(self, flag: bool) -> None:
		"""
		Set the archived flag of the resource to put it in read-only mode.
		Only the resource creator or project owner can do this.

		Parameters
		----------
		flag : bool
			Enable with True, Disable with False.
		"""

		uri = self.client.uri("Resources", "Resource", self.id,
					f"setReadonly?status={str(flag).lower()}")
		logger.info(f"Setting resource '{self.name}' read only flag = {flag}")
		self.client.post(uri)
		self.data["archived"] = flag

###############################################################################

	def form(self) -> ResourceForm:
		"""
		Returns a ResourceForm filled with the metadata of
		the current resource.

		Returns
		-------
		ResourceForm
		"""

		form = self.client.resource_form()
		form.parse(self.data)
		return form

###############################################################################

	def update(self, form: Union[ResourceForm, dict]) -> Resource:
		"""
		Updates the metadata of the resource using the supplied ResourceForm.

		Parameters
		----------
		form : ResourceForm or dict
			ResourceForm filled with updated values
			or generated form data dict.

		Returns
		-------
		Resource
			A new resource object with updated resource metadata
		"""

		if isinstance(form, ResourceForm):
			form = form.generate()
		elif not isinstance(form, dict):
			raise TypeError("Resource metadata form has unexpected type.")

		logger.info(f"Updating resource metadata of resource '{self.name}'...")
		uri = self.client.uri("Resources", "Resource", self.id)
		response = self.client.post(uri, json=form)
		updated_resource_handle = self
		if response.ok:
			# Update resource properties
			# Hint - the response unfortunately does not return
			# the new resource data - bummer!
			updated_resource_handle = list(filter(lambda r: r.id == self.id,
												self.project.resources()))[0]
		return updated_resource_handle

###############################################################################

	def metadata_form(self, data: Optional[dict] = None) -> MetadataForm:
		"""
		Creates a MetadataForm for this resource

		Parameters
		----------
		data : dict, default: None
			If data is specified, the form is initialized with that data
			using the InputForm.fill() method.
		"""

		form = MetadataForm(self.client, self.application_profile())
		if data:
			form.fill(data)
		return form

###############################################################################

	def graph(self, literal: bool = False) -> Optional[rdflib.Graph]:
		"""
		Create an rdflib graph from the resource contents.
		The rdflib graph can be queried with SPARQL, merged with the graphs
		from other resources and serialized into various formats such
		as xml or dot (for rendering it as a graph).

		Parameters
		----------
		literal : bool, default: False
			If enabled, the literal values as seen in the MetadataForm
			are used for the triples in the graph (the human
			readable values instead of the URIs).

		Returns
		--------
		rdflib.Graph
		"""

		#######################################################################

		def add_to_graph(graph: rdflib.Graph, file: FileObject):
			"""Adds the FileObject to the rdflib graph"""
			metadata = file.metadata()
			if metadata:
				file_reference = rdflib.URIRef(
					file.name,
					"https://purl.org/coscine/file/"
				)
				for key, values in metadata.items():
					for v in values:
						graph.add((
							file_reference,
							rdflib.URIRef(key),
							rdflib.Literal(v["value"])
						))

		#######################################################################

		# TODO: Implement literal option, add project and resource as triple
		# to graph; enhance method in various other ways...
		file_objects = self.objects()
		logger.info(f"Constructing graph for resource {self.display_name}...")
		pbar = ProgressBar(
			self.client.settings.verbose,
			len(file_objects),
			f"Creating rdf graph for '{self.display_name}'"
		)
		graph = rdflib.Graph()
		for file in file_objects:
			pbar.update(1)
			if file.has_metadata:
				add_to_graph(graph, file)
		return graph

###############################################################################
