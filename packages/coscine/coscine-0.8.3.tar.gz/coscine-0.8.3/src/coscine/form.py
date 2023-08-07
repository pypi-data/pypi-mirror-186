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
This file provides base class for all input forms defined by
the Coscine Python SDK.
"""

###############################################################################
# Dependencies
###############################################################################

from __future__ import annotations
from typing import Any, TYPE_CHECKING, Union, Tuple, Iterator, List, Dict
from datetime import datetime
import urllib.parse
from prettytable import PrettyTable
from coscine.defaults import LANGUAGES
if TYPE_CHECKING:
	from coscine.client import Client
	from coscine.vocabulary import Vocabulary

###############################################################################
# Classes / Functions / Scripts
###############################################################################

class FormField:
	"""
	The FormField class defines a field such as "Display Name"
	inside an InputForm with all of its properties.
	"""

	client: Client
	_data: Dict

	def __init__(self, client: Client, data: Dict) -> None:
		self.client = client
		self._data = data

	@property
	def name(self) -> str:
		"""
		The name of the field e.g. "Project Name"
		"""
		index = LANGUAGES.index(self.client.settings.language)
		return self._data["name"][index]

	@property
	def path(self) -> str:
		"""
		The unique Coscine internal name of the field e.g. "projectName"
		"""
		return self._data["path"]

	@property
	def order(self) -> int:
		"""
		The order of appearance of the field inside of the form
		"""
		return int(self._data["order"])

	@property
	def vocabulary(self) -> str:
		"""
		Name of the vocabulary instance for the field, may be None
		"""
		return self._data["class"]

	@property
	def min_count(self) -> int:
		"""
		Minimum amount of values required for a successful generate()
		"""
		return int(self._data["minCount"])

	@property
	def max_count(self) -> int:
		"""
		Maximum allowed amount of values
		"""
		return int(self._data["maxCount"])

	@property
	def datatype(self) -> str:
		"""
		Expected datatype of the field as a string identifier, e.g. "xsd:int"
		"""
		return self._data["datatype"]

	@property
	def selection(self) -> List[str]:
		"""
		Preset selection of values - no other value except for these values
		can be specified. Think of it as a class defined in the profile.
		"""
		if "in" in self._data:
			return self._data["in"]
		return None

###############################################################################
###############################################################################
###############################################################################

class FormValue:
	"""
	An InputForm specific representation of a value
	"""

	_form: InputForm
	_key: str
	properties: FormField
	# In case of form.properties(key).maxValues > 1 it is a list,
	# otherwise a scalar object
	_container: Union[List[Any], Any]

###############################################################################

	def __init__(self, form: InputForm, key: str, obj: Any = None,
										raw: bool = False) -> None:
		"""
		Specifying the associated InputForm and key may seem redundant from
		the point of view of the InputForm, but ultimately it allows the form
		value to access the vocabulary and the field properties.
		"""
		self._form = form
		self._key = key
		self.properties = form.properties(key)
		self.set_value(obj, raw)

###############################################################################

	def __bool__(self) -> bool:
		if isinstance(self._container, list):
			return self._container[0] is not None
		return self._container is not None

###############################################################################

	def _set_list_value(self, values: List[Any], raw: bool = False) -> None:
		if isinstance(values, (list, tuple)):
			self._container = []
			for entry in values:
				self.append(entry, raw)
		else:
			# Let's be generous and do the conversion if scalar type to list
			# of size 1 for the users ourselves
			self._container = []
			self.append(values, raw)

###############################################################################

	def _set_scalar_value(self, value: Any, raw: bool = False) -> None:
		if isinstance(value, (list, tuple)):
			# Be very generous and automatically convert lists
			# of size 1 to an atomic value.
			if len(value) > 1:
				raise TypeError("Did not expect list type exceeding "
							f"MaxValues property for key '{self._key}'.")
			value = value[0]
		self._container = value if raw else self._objectify(value)

###############################################################################

	def set_value(self, value: Any, raw: bool = False) -> None:
		"""
		Sets the FormValue equal to the specified value.

		Parameters
		----------
		value : Any
			The value to set the FormField equal to. Could be
			a list of values.
		raw : bool
			If set to True, the value is not interpreted for controlled
			fields and its type is not checked. Use raw when dealing with
			values in Coscines internal format.
		"""
		if self.properties.max_count > 1:
			self._set_list_value(value, raw)
		else:
			self._set_scalar_value(value, raw)

###############################################################################

	def append(self, value: Any, raw: bool = False) -> None:
		"""
		Appends a value to a FormValue allowing multiple values.

		Parameters
		----------
		value : Any
			The value to append to the FormField.
		raw : bool
			If set to True, the value is not interpreted for controlled
			fields and its type is not checked. Use raw when dealing with
			values in Coscines internal format.

		Raises
		------
		TypeError
			In case of appending a value to a scalar FormField.
		IndexError
			When exceeding the maxValues setting for the FormField.
		"""
		if not isinstance(self._container, list):
			raise TypeError("Attempting to append a value to scalar "
										f"FormField '{self._key}'. "
							"See 'MaxCount' property in application profile.")
		if len(self._container) < self.properties.max_count:
			if not raw:
				value = self._objectify(value)
			self._container.append(value)
		else:
			raise IndexError(f"Exceeding maxValues for field {self._key}.")

###############################################################################

	def type_format(self) -> str:
		"""
		Returns the type format of the internal type.
		See InputForm.type_format() as this is internally called.

		Returns
		-------
		str
			The type format as a string, e.g. "%s" for string types
			or "%d" for integers. This function is handy when dealing with
			datetime objects, as it returns the expected date format.
		"""
		return self._form.type_format(self._key)

###############################################################################

	def _is_valid_type(self, key: str, value: Any) -> bool:
		if self._form.is_controlled(self._key) and not isinstance(value, str):
			raise TypeError("Values specified for controlled fields "
					"must be of type string to make it possible to "
					"look up their raw representation in the vocabulary: "
					f"Expected 'str', got '{str(type(value))}'")
		if self._form.datatype(key) is None:
			return True
		datatype = self._form.datatype(key)
		return datatype is not None and isinstance(value, datatype)

###############################################################################

	def _objectify(self, value: Any) -> Any:
		"""
		Checks if the type of the value matches the expecte type and
		in case of controlled fields, converts the human-readable value to
		the unique internal Coscine representation via
		the associated vocabulary.
		"""
		if value is None:
			return None

		if not self._is_valid_type(self._key, value):
			raise TypeError(f"Value of type {str(type(value))} specified "
					f"for key {self._key} does not match expected "
						f"type {self._form.datatype(self._key)}!")

		if self._form.has_vocabulary(self._key):
			if not self._form.vocabulary(self._key).contains(value):
				suggestions = self._form.vocabulary(self._key).suggest(value)
				raise ValueError(f"Invalid value '{value}' for vocabulary "
										f"controlled key '{self._key}'! "
										f"Perhaps you meant {suggestions}?")
			return self._form.vocabulary(self._key).lookup_key(value)
		elif self._form.has_selection(self._key):
			if value not in self._form.selection(self._key):
				raise ValueError(f"Invalid value '{value}' for selection "
										f"controlled key '{self._key}'!")
		return value

###############################################################################

	def _serialize_value(self, obj: Any, raw: bool = False) -> str:
		"""
		Serializes a single value according to its type / format
		-> This function converts a pythonic value to a string.
		"""
		serialized_value: str = ""
		if obj and self._form.has_vocabulary(self._key):
			if raw:
				serialized_value = obj
			else:
				serialized_value = str(
					self._form.vocabulary(self._key).lookup_value(obj)
				)
		elif isinstance(obj, datetime):
			try:
				serialized_value = obj.strftime(self.type_format())
			except ValueError:
				serialized_value = str(obj)  # Omit format if error
		elif isinstance(obj, dict):
			serialized_value = str(obj)
		elif isinstance(obj, bool):
			serialized_value = str(obj).lower()
		elif obj is None:
			serialized_value = ""
		else:
			serialized_value = str(obj)
		return serialized_value

###############################################################################

	def _serialize_list_raw(self) -> List:
		serialized_values = []
		for value in self._container:
			serialized_values.append(self._serialize_value(value, True))
		return serialized_values

###############################################################################

	def _serialize_list(self) -> str:
		serialized_values = []
		for value in self._container:
			serialized_values.append(self._serialize_value(value))
		return "\n".join(serialized_values)

###############################################################################

	def __str__(self) -> str:
		if self.properties.max_count > 1:
			return self._serialize_list()
		return self._serialize_value(self._container)

###############################################################################

	def raw(self) -> Any:
		"""
		Returns the raw value of the FormValue.
		"""
		if self.properties.max_count > 1:
			return self._serialize_list_raw()
		return self._serialize_value(self._container, True)

###############################################################################
###############################################################################
###############################################################################

class InputForm:
	"""
	Coscine InputForm base class
	"""

	client: Client
	_fields: List[FormField]
	_values: Dict[str, FormValue]
	_vocabularies: Dict[str, Vocabulary]

###############################################################################

	def __init__(self, client: Client) -> None:
		"""
		Parameters
		----------
		client : Client
			Coscine Python SDK Client handle
		"""
		super().__init__()
		self.client = client
		self._fields = []
		self._values = {}
		self._vocabularies = {}

###############################################################################

	def __setitem__(self, key: str, value: Any) -> None:
		self.set_value(key, value)

###############################################################################

	def __getitem__(self, key: str) -> FormValue:
		return self.get_value(key)

###############################################################################

	def __delitem__(self, key: str) -> None:
		del self._values[self.path(key)]

###############################################################################

	def __iter__(self) -> Iterator[str]:
		return iter(self.keys())

###############################################################################

	def __len__(self) -> int:
		return len(self._fields)

###############################################################################

	def __str__(self) -> str:
		return self.as_str()

###############################################################################

	def clear(self) -> None:
		"""Removes all values of the InputForm"""
		self._values.clear()

###############################################################################

	def path(self, key: str) -> str:
		"""
		Returns the unique identifier for a multilanguage key.
		Logical example:
		path("Display Name") == path("Anzeigename") == "__XXX__"
		->> True
		where "__XXX__" is of some fixed internal value.

		Parameters
		-----------
		key : str
			Multilanguage form key. Language depends on the
			coscine.Client language setting.

		Returns
		-------
		str
			Unique identifier of a form field.
		"""
		return self.properties(key).path

###############################################################################

	def properties(self, key: str) -> FormField:
		"""
		Returns the form field properties corresponding to the given key.

		Parameters
		----------
		key : str
			Form key

		Returns
		-------
		FormField
			Object containing the field properties for the given key
		"""
		return self._fields[self.index_of(key)]

###############################################################################

	def index_of(self, key: str) -> int:
		"""
		Returns the order/index of the given key.
		"""
		for index, item in enumerate(self.keys()):
			if item == key:
				return index
		raise KeyError(f"Key '{key}' not in InputForm!")

###############################################################################

	def name_of(self, path: str) -> str:
		"""
		Returns the key name for the unique path depending on the client
		language setting.
		"""
		for field in self._fields:
			if field.path == path:
				return field.name
		raise KeyError(f"Path '{path}' not in InputForm!")

###############################################################################

	def keys(self) -> List[str]:
		"""
		Returns a list of keys in their respective order based on the
		language setting of the client class instance used to initialize
		the InputForm.
		"""
		return [field.name for field in self._fields]

###############################################################################

	def values(self) -> List[FormValue]:
		"""
		Returns a list of values in their respective order based on the
		language setting of the client class instance used to initialize
		the InputForm.
		"""
		return [self.get_value(key) for key in self.keys()]

###############################################################################

	def items(self) -> List[Tuple[str, FormValue]]:
		"""
		Returns a list of key, value pairs in their respective order based
		on the 	language setting of the client class instance
		used to initialize the InputForm.
		"""
		return list(zip(self.keys(), self.values()))

###############################################################################

	def datatype(self, key: str) -> Union[type, None]:
		"""
		Returns the datatype for a given field (which may be None).
		"""
		datatype = self.properties(key).datatype
		if datatype and datatype.startswith("http:"):
			datatype = f"xsd:{urllib.parse.urlparse(datatype)[-1]}"
		type_info: Union[type, None] = None
		if datatype == "xsd:string":
			type_info = str
		elif datatype == "xsd:boolean":
			type_info = bool
		elif datatype == "xsd:decimal":
			type_info = float
		elif datatype in ["xsd:int", "xsd:integer"]:
			type_info = int
		elif datatype in ["xsd:date", "xsd:dateTime"]:
			type_info = datetime
		return type_info

###############################################################################

	def type_format(self, key: str) -> str:
		"""
		Returns the format for a datatype of a field.
		This is especially useful for instances of type datetype.
		"""
		datatype = self.properties(key).datatype
		if datatype and datatype.startswith("http:"):
			datatype = f"xsd:{urllib.parse.urlparse(datatype)[-1]}"
		format_string: str = "Invalid"
		if datatype == "xsd:string":
			format_string = "%s"
		elif datatype == "xsd:boolean":
			format_string = "%d"
		elif datatype == "xsd:decimal":
			format_string = "%f"
		elif datatype in ["xsd:int", "xsd:integer"]:
			format_string = "%d"
		elif datatype == "xsd:date":
			format_string = "%Y-%m-%d"
		elif datatype == "xsd:dateTime":
			format_string = "%Y-%m-%dT%H:%M:%S"
		return format_string

###############################################################################

	def is_typed(self, key: str) -> bool:
		"""
		Returns whether a value is expecting a certain datatype.
		"""
		return self.datatype(key) is not None

###############################################################################

	def is_required(self, key: str) -> bool:
		"""
		Determines whether a key is a required one.
		"""
		return self.properties(key).min_count > 0

###############################################################################

	def has_vocabulary(self, key: str) -> bool:
		"""
		Determines whether a key is controlled by a vocabulary.
		"""
		return self.properties(key).vocabulary is not None

###############################################################################

	def has_selection(self, key: str) -> bool:
		"""
		Determines whether a key is controlled by a selection.
		"""
		return self.properties(key).selection is not None

###############################################################################

	def is_controlled(self, key: str) -> bool:
		"""
		Determines whether a key is controlled by a vocabulary or selection.
		"""
		return self.has_vocabulary(key) or self.has_selection(key)

###############################################################################

	def vocabulary(self, key: str) -> Vocabulary:
		"""
		Returns the vocabulary for the given controlled key. Make sure
		the key is actually controlled to avoid an exception.

		Raises
		-------
		KeyError
			In case the specified key is not controlled by a vocabulary.
		"""
		if self.has_vocabulary(key):
			return self._vocabularies[self.path(key)]
		raise KeyError(f"Key '{key}' is not controlled by a vocabulary!")

###############################################################################

	def selection(self, key: str) -> List[str]:
		"""
		Returns the selection for the given controlled key. Make sure
		the key is actually controlled to avoid an exception.

		Raises
		-------
		KeyError
			In case the specified key is not controlled by a selection.
		"""

		if self.has_selection(key):
			return self.properties(key).selection
		raise KeyError(f"Key '{key}' is not controlled by a selection!")

###############################################################################

	def set_value(self, key: str, value: Any, raw: bool = False) -> None:
		"""
		Sets the value for a given key.

		Parameters
		----------
		key : str
			The key to associate the value with
		value : Any
			The typed value, either in raw format or human readable
		raw : bool, default: False
			Treat the value as a raw value (from Coscine) and do not apply
			vocabulary search or type checking on it
		"""
		self._values[self.path(key)] = FormValue(self, key, value, raw)

###############################################################################

	def get_value(self, key: str) -> FormValue:
		"""
		Returns the FormValue for the specified key

		Parameters
		----------
		key : str
			The key to get the value from.
		"""
		if key not in self.keys():
			raise KeyError(f"Key '{key}' not in InputForm!")
		if self.path(key) in self._values:
			return self._values[self.path(key)]
		return FormValue(self, key)  # Yields an empty FormValue

###############################################################################

	def fill(self, data: Dict) -> None:
		"""
		Fill in an InputForm from a dictionary

		Parameters
		----------
		data : dict
			Python dictionary containing key value pairs in human-readable
			form (not data from Coscine!).
		"""
		for key, value in data.items():
			self[key] = value

###############################################################################

	def parse(self, data: Dict) -> None:
		"""
		Parses data from Coscine into an InputForm.

		Parameters
		----------
		data : dict
			Python dictionary (output of json.loads) containing
			the data from Coscine.
		"""

###############################################################################

	def generate(self) -> dict:
		"""
		Generates Coscine formatted json-ld from an InputForm.
		"""
		return {}

###############################################################################

	def as_str(self, format: str = "str") -> str:
		"""
		Returns a string in the specified format

		Parameters
		-----------
		format : str, default "str"
			Format of the string, possible options are: str, csv, json, html

		Returns
		--------
		str
			A string with the form values in the specified format.
		"""

		supported_formats = ["str", "csv", "json", "html"]
		if format not in supported_formats:
			raise ValueError(f"Unsupported format '{format}'!")
		table = PrettyTable(("C", "Property", "Value"), align="l")
		rows = []
		for key in self.keys():
			value = str(self.get_value(key))
			name: str = key
			name = name + "*" if self.is_required(key) else name
			controlled: str = "X" if self.is_controlled(key) else ""
			rows.append((controlled, name, value))
		table.max_width["Value"] = 50
		table.add_rows(rows)
		if format == "csv":
			return table.get_csv_string()
		if format == "json":
			return table.get_json_string()
		if format == "html":
			return table.get_html_string()
		return table.get_string()

###############################################################################
