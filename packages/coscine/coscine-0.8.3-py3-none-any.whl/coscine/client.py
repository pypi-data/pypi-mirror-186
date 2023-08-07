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
This file contains the backbone of the Coscine Python SDK - the client class.
The client class acts as the manager of the SDK and is mainly
responsible for the communication and exchange of information
with Coscine servers.
"""

###############################################################################
# Dependencies
###############################################################################

from __future__ import annotations
from typing import List, Optional, Union
import urllib.parse
import logging
import platform
import requests
import colorama
from coscine.__about__ import __version__
from coscine.cache import Cache
from coscine.defaults import BASE_URL, LANGUAGES
from coscine.project import Project, ProjectForm
from coscine.resource import ResourceForm
from coscine.utils import in_cli_mode
from coscine.vocabulary import VocabularyManager

###############################################################################
# Module globals / Constants
###############################################################################

# Coscine REST API Endpoints
API_ENDPOINTS = ("Blob", "Metadata", "Organization",
			"Project", "Resources", "Tree",
			"User", "Search", "ActivatedFeatures")

# Get a logger handle.
logger = logging.getLogger(__name__)

# A colorful pretty banner to show on startup when run in a cli.
# Note: The noqa comment disables flake8 linter rule E101 for this variable.
BANNER: str = rf"""{colorama.Fore.BLUE}
                     _
                    (_)
   ___ ___  ___  ___ _ _ __   ___
  / __/ _ \/ __|/ __| | '_ \ / _ \
 | (_| (_) \__ \ (__| | | | |  __/
  \___\___/|___/\___|_|_| |_|\___|{colorama.Fore.WHITE}
____________________________________

    Coscine Python SDK {colorama.Fore.YELLOW}{__version__}{colorama.Fore.WHITE}
____________________________________
"""  # noqa: E101

###############################################################################
# Classes / Functions / Scripts
###############################################################################


class Settings:
	"""
	Contains settings for configuring the Coscine Client class.
	"""

	_language: str
	read_only: bool
	concurrent: bool
	persistent_cache: bool
	verbose: bool

###############################################################################

	@property
	def language(self) -> str:
		"""Returns the language setting"""
		return self._language

###############################################################################

	@language.setter
	def language(self, lang: str) -> None:
		lang = lang.lower()
		if lang in LANGUAGES:
			self._language = lang
		else:
			errormessage: str = (
				f"Invalid value for argument 'lang' -> [{lang}]!\n"
				f"Possible values are {str(LANGUAGES)}."
			)
			raise ValueError(errormessage)

###############################################################################

	def __init__(
		self,
		language: str = "en",
		persistent_cache: bool = True,
		concurrent: bool = True,
		read_only: bool = False,
		verbose: bool = True
	) -> None:
		"""
		Parameters
		----------
		language : str, "en" or "de", default: "en"
			Language preset for input form fields and vocabularies.
		persistent_cache : bool, default: True
			Enable to store the cache in a file on deinitialization of
			the client object. Will attempt to load the cache file
			on initialization if enabled. Leads to a significant speed
			boost when making static requests right after init, but may
			also lead to invalid data when using outdated cache data, in case
			the Coscine API changed recently. However this is mostly avoided
			by performing frequent updates. Useful for applications with
			a short runtime that get run often.
		concurrent : bool, default: True
			If enabled, a ThreadPool is used for bulk requests, speeding up
			up- and downloads of multiple files tremendously.
		read_only : bool, default: False
			Do not perform PUT, POST, DELETE requests
		verbose : bool, default: True
			Print stuff to stdout if running from a command line
		"""
		self.concurrent = concurrent
		self.read_only = read_only
		self.persistent_cache = persistent_cache
		self.language = language
		self.verbose = verbose

###############################################################################
###############################################################################
###############################################################################


class Client:
	"""
	The client class handles the connection with the Coscine server.
	It performs requests to the API and returns the response data.
	All objects of the Python SDK use a handle to the client to
	communicate with Coscine.
	"""

	cache: Cache
	session: requests.Session
	settings: Settings
	vocabularies: VocabularyManager
	_id: int = 0  # unique identifier for each client instance

###############################################################################

	@property
	def version(self) -> str:
		"""Returns the current Coscine Python SDK version"""
		return __version__

###############################################################################

	def __init__(self, token: str, settings: Settings = Settings()) -> None:
		"""
		Initializes an instance of the base class of the Coscine Python SDK.

		Parameters
		----------
		token : str
			A Coscine API access token.
		settings : Settings
			Coscine Python SDK client settings.
		"""

		if not isinstance(token, str):
			raise TypeError("Invalid token type: Expected string!")

		self.settings = settings
		self.cache = Cache(self.settings.persistent_cache)
		self.vocabularies = VocabularyManager(self)
		self.session = requests.Session()
		self.session.headers.update({
			"Authorization": f"Bearer {token}",
			"User-Agent": f"Coscine Python SDK {self.version}"
		})
		if in_cli_mode():
			colorama.init(autoreset=True)
			print(BANNER)
		self._id += 1
		logger.info(f"Initialized Coscine Python SDK version {__version__} "
										f"Client instance (id={self._id})")
		logger.debug(self.sysinfo())

###############################################################################

	@staticmethod
	def sysinfo() -> str:
		"""
		Constructs system information for better bug reports.

		Returns
		-------
		str
			Multiline string containing system and python information.
		"""

		return f"""
			Platform: {platform.platform()}
			Machine: {platform.machine()}
			Processor: {platform.processor()}
			Python compiler: {platform.python_compiler()}
			Python branch: {platform.python_branch()}
			Python implementation: {platform.python_implementation()}
			Python revision: {platform.python_revision()}
			Python version: {platform.python_version()}
		""".replace("\t", " ")

###############################################################################

	@staticmethod
	def uri(api: str, endpoint: str, *args) -> str:
		"""
		Constructs a URL for performing a request to the Coscine API.

		Parameters
		----------
		api : str
			The target Coscine API endpoint, e.g. Blob, Metadata, Tree, ...
		endpoint : str
			The subendpoint of `api`.
		*args
			Variable number of arguments of type string to append to the URL.
			Arguments are automatically seperated by a slash '/' and
			special characters are encoded.

		Raises
		------
		ValueError
			If the api / endpoint is invalid.

		Returns
		-------
		str
			Encoded URL for communicating with the Coscine servers.
		"""

		if api not in API_ENDPOINTS:
			raise ValueError("Invalid value for argument 'api'!\n"
					f"Possible values are {str(API_ENDPOINTS)}.")

		uri = BASE_URL % (api, endpoint)
		for arg in args:
			if arg is None:
				continue
			uri += "/" + urllib.parse.quote(arg, safe="")
		return uri

###############################################################################

	def _request(self, method: str, uri: str, **kwargs) -> requests.Response:
		"""
		Performs a HTTP request to the Coscine Servers.

		Parameters
		----------
		method : str
			HTTP request method (GET, PUT, POST, DELETE).
		uri : str
			Coscine URL generated with Client.uri(...).
		**kwargs
			Additional keyword arguments forwarded to the requests library.

		Raises
		------
		ConnectionError
			If the Coscine servers could not be reached.
		PermissionError
			If the Coscine API token is invalid.
		RuntimeError
			If the request resulted in an error.

		Returns
		-------
		requests.Response
			The response of the Coscine server as a requests.Response object.
		"""

		# Debugging URL
		params = kwargs["params"] if "params" in kwargs else None
		full_url = requests.Request(method, uri, params=params).prepare().url
		if full_url:
			logger.debug(f"HTTP {method}: {full_url}")
		else:
			logger.debug(f"HTTP {method}: {uri}")

		# Handling read_only setting
		if self.settings.read_only and method != "GET":
			logger.warning(f"READ_ONLY mode in effect for {method} : {uri}")
			return requests.Response()

		try:  # performing the request and handle any resulting errors
			response = self.session.request(method, uri, **kwargs)
			response.raise_for_status()
			logger.debug(f"response: {str(response.content)}")
			return response
		except requests.exceptions.ConnectionError as exc:
			raise ConnectionError("Failed to connect to Coscine!") from exc
		except requests.exceptions.RequestException as exc:
			if exc.response.status_code == 401:
				raise PermissionError("Invalid Coscine API token!") from exc
			raise RuntimeError("Unspecified error occurred when communicating "
										"with the Coscine servers") from exc

###############################################################################

	def get(self, uri: str, **kwargs) -> requests.Response:
		"""
		Performs a GET request to the Coscine API.

		Parameters
		----------
		uri : str
			Coscine URL generated with Client.uri(...).
		**kwargs
			Additional keyword arguments forwarded to the requests library.

		Examples
		--------
		>>> uri = Client.uri("Project", "Project")
		>>> projects = Client.get(uri).json()

		Raises
		------
		ConnectionError
			If the Coscine servers could not be reached.
		PermissionError
			If the Coscine API token is invalid.
		RuntimeError
			If the request resulted in an error.

		Returns
		-------
		requests.Response
			The response of the Coscine server as a requests.Response object.
		"""

		return self._request("GET", uri, **kwargs)

###############################################################################

	def put(self, uri: str, **kwargs) -> requests.Response:
		"""
		Performs a PUT request to the Coscine API.

		Parameters
		----------
		uri : str
			Coscine URL generated with Client.uri(...).
		**kwargs
			Additional keyword arguments forwarded to the requests library.

		Examples
		--------
		>>> uri = Client.uri("Tree", "Tree", resource.id, filename)
		>>> Client.put(uri, data = metadata)

		Raises
		------
		ConnectionError
			If the Coscine servers could not be reached.
		PermissionError
			If the Coscine API token is invalid.
		RuntimeError
			If the request resulted in an error.

		Returns
		-------
		requests.Response
			The response of the Coscine server as a requests.Response object.
		"""

		return self._request("PUT", uri, **kwargs)

###############################################################################

	def post(self, uri: str, **kwargs) -> requests.Response:
		"""
		Performs a POST request to the Coscine API.

		Parameters
		----------
		uri : str
			Coscine URL generated with Client.uri(...).
		**kwargs
			Additional arguments forwarded to the requests library.

		Examples
		--------
		>>> data = member.data
		>>> data["projectId"] = Client.id
		>>> data["role"]["displayName"] = "Member"
		>>> data["role"]["id"] = ProjectMember.ROLES["Member"]
		>>> uri = Client.uri("Project", "ProjectRole")
		>>> Client.post(uri, data=data)

		Raises
		------
		ConnectionError
			If the Coscine servers could not be reached.
		PermissionError
			If the Coscine API token is invalid.
		RuntimeError
			If the request resulted in an error.

		Returns
		-------
		requests.Response
			The response of the Coscine server as a requests.Response object.
		"""

		return self._request("POST", uri, **kwargs)

###############################################################################

	def delete(self, uri: str, **kwargs) -> requests.Response:
		"""
		Performs a DELETE request to the Coscine API.

		Parameters
		----------
		uri : str
			Coscine URL generated with Client.uri(...).
		**kwargs
			Additional keyword arguments forwarded to the requests library.

		Examples
		--------
		>>> uri = Client.uri("Project", "Project", Client.id)
		>>> Client.delete(uri)

		Raises
		------
		ConnectionError
			If the Coscine servers could not be reached.
		PermissionError
			If the Coscine API token is invalid.
		RuntimeError
			If the request resulted in an error.

		Returns
		-------
		requests.Response
			The response of the Coscine server as a requests.Response object.
		"""

		return self._request("DELETE", uri, **kwargs)

###############################################################################

	def static_request(self, uri: str) -> dict:
		"""
		Performs a GET request for the given uri. If such a request
		has been performed previously during the current session, the previous
		response is returned. Otherwise a new request is made to Coscine
		and that response is then stored inside the session cache.

		Parameters
		-----------
		uri : str
			Request URI

		Returns
		-------
		dict
		"""

		logger.debug(f"static_request({uri})")
		data = self.cache.get(uri)
		if data is None:
			data = self.get(uri).json()
			self.cache.set(uri, data)
		return data

###############################################################################

	def project_form(self, data: Optional[dict] = None) -> ProjectForm:
		"""
		Returns an empty project form.

		Parameters
		----------
		data : dict, default: None
			If data is specified, the form is initialized with that data
			using the InputForm.fill() method.
		"""
		form = ProjectForm(self)
		if data:
			form.fill(data)
		return form

###############################################################################

	def resource_form(self, data: Optional[dict] = None) -> ResourceForm:
		"""
		Returns an empty resource form.

		Parameters
		----------
		data : dict, default: None
			If data is specified, the form is initialized with that data
			using the InputForm.fill() method.
		"""
		form = ResourceForm(self)
		if data:
			form.fill(data)
		return form

###############################################################################

	def projects(self, toplevel: bool = True) -> List[Project]:
		"""
		Retrieves a list of a all projects the creator of
		the Coscine API token is currently a member of.

		Parameters
		----------
		toplevel : bool, default: True
			Retrieve only toplevel projects (no subprojects).
			Set to False if you want to retrieve all projects, regardless
			of hierarchy.

		Returns
		-------
		List[Project]
			List of coscine.Project objects
		"""

		endpoint = ("Project", "Project/-/topLevel")
		uri = self.uri("Project", endpoint[toplevel])
		projects = []
		for project_data in self.get(uri).json():
			projects.append(Project(self, project_data))
		return projects

###############################################################################

	def project(
		self,
		display_name: str,
		toplevel: bool = True
	) -> Union[Project, None]:
		"""
		Returns a single project via its displayName

		Parameters
		----------
		display_name : str
			Look for a project with the specified displayName
		toplevel : bool, default: True
			Retrieve only toplevel projects (no subprojects).
			Set to False if you want to retrieve all projects, regardless
			of hierarchy.

		Returns
		-------
		Project or None
			A single coscine project handle or None if no match found

		Raises
		------
		IndexError
			In case more than 1 project matches the specified criteria.
		"""
		filtered_project_list = list(filter(
			lambda project: project.display_name == display_name,
			self.projects(toplevel)
		))
		if len(filtered_project_list) == 1:
			return filtered_project_list[0]
		if len(filtered_project_list) == 0:
			return None
		raise IndexError("Received more than 1 project matching the "
				f"specified criteria (display_name = '{display_name}')!")

###############################################################################

	def create_project(self, form: Union[ProjectForm, dict]) -> Project:
		"""
		Creates a project using the given ProjectForm.

		Parameters
		----------
		form : ProjectForm or dict
			ProjectForm filled with project metadata or a dict with the
			data generated from a form.

		Returns
		-------
		Project
			Project object for the new project.
		"""

		if isinstance(form, ProjectForm):
			form = form.generate()
		uri = self.uri("Project", "Project")
		return Project(self, self.post(uri, json=form).json())

###############################################################################

	def search(self, query: str) -> dict:
		"""
		Performs a Coscine search query.

		Returns
		--------
		dict
			The search results as a dict
		"""

		uri = self.uri("Search", f"Search?query={query}")
		results = self.get(uri).json()
		return results

###############################################################################
