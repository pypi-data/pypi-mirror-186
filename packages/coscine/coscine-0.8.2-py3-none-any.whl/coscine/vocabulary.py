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
This file implements various classes for querying, parsing and interacting
with data inside Coscine vocabularies.
"""

###############################################################################
# Dependencies
###############################################################################

from __future__ import annotations
from typing import TYPE_CHECKING, Tuple, Union, List
import os
import json
import difflib
import pkgutil
import urllib.parse
from coscine.defaults import LANGUAGES
from coscine.form import FormField
from coscine.graph import ApplicationProfile
from coscine.utils import is_subset
if TYPE_CHECKING:
	from coscine.client import Client

###############################################################################
# Classes / Functions / Scripts
###############################################################################

class Vocabulary:
	"""
	A wrapper around Coscine vocabularies. Vocabularies from Coscine
	do not necessarily all follow the same format, so this class takes
	care of abstracting the Vocabulary interface.
	The internal language of the Vocabulary changes automatically based
	on the Client setting `language`.

	Attributes
	-----------
	raw : dict
		Contains the raw dictionary data that is served by Coscine. Parsing
		for language is not taken into account.
	content : dict
		Contains the raw dictionary data that is served by Coscine
		for the language preset set in coscine.Client .
	"""

	client: Client
	_data: dict

	@property
	def raw(self) -> dict:
		return self._data

	@property
	def content(self) -> dict:
		data = self.raw
		languages = self.languages()
		# Select appropriate language branch
		if self.client.settings.language in languages:
			data = data[self.client.settings.language]
		elif len(languages) > 0:
			data = data[languages[0]]
		return data

###############################################################################

	def __init__(self, client: Client, data: dict) -> None:
		self.client = client
		self._data = data

###############################################################################

	def __str__(self) -> str:
		return json.dumps(self.raw, indent=4)

###############################################################################

	def keys(self) -> List[str]:
		return [entry["name"] for entry in self.content]

###############################################################################

	def values(self) -> List[object]:
		return [entry["value"] for entry in self.content]

###############################################################################

	def items(self) -> List[Tuple[str, object]]:
		return list(zip(self.keys(), self.values()))

###############################################################################

	def languages(self) -> List[str]:
		"""
		Returns the languages supported by the dictionary.
		Some dictionaries may not contain a language setting and thus
		are valid for all languages. In that case an empty list is returned.
		"""

		languages = []
		for lang in LANGUAGES:
			if lang in self.raw:
				languages.append(lang)
		return languages

###############################################################################

	def contains(self, key: str) -> bool:
		"""
		Determines whether the vocabulary contains the given key.

		Parameters
		----------
		key : object (str, list or dict)
			The key to look for in the vocabulary.
		reverse : bool
			If set to true, key is assumed to be a value inside of the
			vocabulary and thus all values are searched for key.
		"""

		return self.lookup_key(key) is not None

###############################################################################

	def suggest(self, key: str) -> str:
		"""
		Returns the closest matches for a given key based on
		the Levenshtein distance
		"""
		keys: List[str] = [entry["name"] for entry in self.content]
		close_matches = difflib.get_close_matches(key, keys, n=3, cutoff=0.6)
		suggestions = [f"'{match}'" for match in close_matches]
		return " or ".join(suggestions)

###############################################################################

	def lookup_key(self, key: str) -> object:
		"""
		Looks up the counterpart of $key.

		Parameters
		----------
		key : object (str, list or dict)
			The key to look for in the vocabulary.
		reverse : bool
			If set to true, key is assumed to be a value inside of the
			vocabulary and thus all values are searched for key.
		"""

		for entry in self.content:
			if entry["name"] == key:
				return entry["value"]
		return None

###############################################################################

	def lookup_value(self, value: object) -> Union[str, None]:
		"""
		Returns the key referenced by value
		"""

		if isinstance(value, list) and len(value) == 1:
			value = value[0]
		for entry in self.content:
			if isinstance(value, str):
				if entry["value"] == value:
					return entry["name"]
			elif isinstance(value, dict):
				if is_subset(value, entry["value"]):
					return entry["name"]
		return None

###############################################################################
# Class
###############################################################################

class VocabularyManager:
	"""
	The VocabularyManager takes care of loading local InputForms and
	querying vocabularies from the Coscine servers. Local InputForms
	are stored in src/data in json format.
	It makes use of the Cache class thus making it more efficient at
	querying vocabularies.
	"""

	client: Client
	_builtins: dict

###############################################################################

	def __init__(self, client: Client) -> None:
		"""
		Initializes the VocabularyManager with a client instance for
		talking to the Coscine servers.
		"""
		self.client = client
		project_template = pkgutil.get_data(__name__, "data/project.json")
		resource_template = pkgutil.get_data(__name__, "data/resource.json")
		if project_template is None or resource_template is None:
			raise FileNotFoundError()
		self._builtins = {
			"project": json.loads(project_template.decode("utf-8")),
			"resource": json.loads(resource_template.decode("utf-8"))
		}
		for graph in self._builtins:
			container = []
			for element in self._builtins[graph]:
				container.append(FormField(client, element))
			self._builtins[graph] = container

###############################################################################

	def builtin(self, name: str) -> List[FormField]:
		"""
		Returns a builtin InputForm as a list of FormFields.

		Parameters
		-----------
		name : str
			Name of the builtin vocabulary (filename in src/data
			without filetype).
		"""
		if name not in self._builtins:
			raise ValueError("Invalid builtin InputForm name!")
		return self._builtins[name]

###############################################################################

	def licenses(self, normalize: bool = True) -> Vocabulary:
		"""
		Returns a dictionary containing a list of licenses
		available in Coscine.
		"""

		uri = self.client.uri("Project", "License")
		data = self.client.static_request(uri)
		if normalize:
			normalized: dict = {"en": []}
			for entry in data:
				normalized["en"].append({
					"name": entry["displayName"],
					"value": entry
				})
			data = normalized
		return Vocabulary(self.client, data)

###############################################################################

	def resource_types(self, normalize: bool = True) -> Vocabulary:
		"""
		Retrieves a list of the available resource types in Coscine.
		Only enabled (currently usable) resource types are returned.
		"""

		uri = self.client.uri("Resources", "ResourceType", "types")
		data = self.client.static_request(uri)
		if normalize:
			normalized: dict = {"en": []}
			for entry in data:
				if entry["isEnabled"]:
					normalized["en"].append({
						"name": entry["displayName"],
						"value": entry
					})
			data = normalized
		return Vocabulary(self.client, data)

###############################################################################

	def application_profiles(self, normalize: bool = True) -> Vocabulary:
		"""
		Returns a list of all available Coscine application profiles.
		"""

		uri = self.client.uri("Metadata", "Metadata", "profiles")
		data = self.client.static_request(uri)
		if normalize:
			normalized: dict = {"en": []}
			for entry in data:
				name = urllib.parse.urlparse(entry)[2]
				name = os.path.relpath(name, "/coscine/ap/")
				normalized["en"].append({
					"name": name,
					"value": entry
				})
			data = normalized
		return Vocabulary(self.client, data)

###############################################################################

	def application_profile(self, path: str) -> ApplicationProfile:
		"""
		Retrieves a specific Coscine application profile.

		Parameters
		-----------
		path : str
			Path/Url to the application profile.
			(e.g. Resource.data["applicationProfile"]))
		id : str, default: None
			Coscine resource ID.

		Returns
		-------
		ApplicationProfile
			A parsed application profile.
		"""

		uri = self.client.uri("Metadata", "Metadata", "profiles", path)
		data = self.client.static_request(uri)
		graph = json.dumps(data[0]["@graph"])
		return ApplicationProfile(graph)

###############################################################################

	def instance(self, link: str) -> Vocabulary:
		"""
		Retrieves a data instance. Instances are always normalized.

		Parameters
		-----------
		link : str
			link to the instance
		"""

		uri = self.client.uri("Metadata", "Metadata", "instances", link)
		instance = self.client.static_request(uri)
		return Vocabulary(self.client, instance)

###############################################################################

	def organizations(self, normalize: bool = True,
					filter: str = "") -> Vocabulary:
		"""
		Queries the organizations (e.g. 'RWTH Aachen University') available
		for selection in Coscine.
		"""

		if filter:
			raise NotImplementedError("Handling of filter "
								"argument not implemented!")
		uri = self.client.uri("Organization", "Organization", "-", "ror")
		data = self.client.static_request(uri)
		if normalize:
			normalized: dict = {"en": []}
			for entry in data["data"]:
				normalized["en"].append({
					"name": entry["displayName"],
					"value": entry
				})
			data = normalized
		return Vocabulary(self.client, data)

###############################################################################

	def visibility(self, normalize: bool = True) -> Vocabulary:
		"""
		Returns the key-value mapping of the Coscine project visibility field.

		Returns
		-------
		dict
			Key-value mapped Coscine project visibility field.
		"""

		uri = self.client.uri("Project", "Visibility")
		data = self.client.static_request(uri)
		if normalize:
			normalized: dict = {"en": []}
			for entry in data:
				normalized["en"].append({
					"name": entry["displayName"],
					"value": entry
				})
			data = normalized
		return Vocabulary(self.client, data)

###############################################################################

	def disciplines(self, normalize: bool = True) -> Vocabulary:
		"""
		Queries the scientific disciplines available for selection in Coscine.

		Returns
		-------
		dict
			Dictionary containing the disciplines.
		"""

		uri = self.client.uri("Project", "Discipline")
		data = self.client.static_request(uri)
		if normalize:
			normalized: dict = {"en": [], "de": []}
			for entry in data:
				normalized["en"].append({
					"name": entry["displayNameEn"],
					"value": entry
				})
				normalized["de"].append({
					"name": entry["displayNameDe"],
					"value": entry
				})
			data = normalized
		return Vocabulary(self.client, data)

###############################################################################
