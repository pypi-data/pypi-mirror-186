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
This file defines the project object for the representation of
Coscine projects. It provides a simple interface to interact with Coscine
projects from python.
"""

###############################################################################
# Dependencies
###############################################################################

from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union, List
import json
import os
from datetime import datetime
import logging
import dateutil.parser
from prettytable.prettytable import PrettyTable
from coscine.resource import Resource, ResourceForm
from coscine.form import InputForm
if TYPE_CHECKING:
	from coscine.client import Client

###############################################################################
# Module globals / Constants
###############################################################################

logger = logging.getLogger(__name__)

###############################################################################
# Classes / Functions / Scripts
###############################################################################

class ProjectForm(InputForm):
	"""
	An InputForm for Coscine project metadata. Use this form
	to generate or edit project metadata such as the project name
	and start date.
	"""

###############################################################################

	def __init__(self, client: Client) -> None:
		"""
		Generates a new instance of type ProjectForm.

		Parameters
		----------
		client : Client
			Coscine Python SDK Client handle
		"""
		super().__init__(client)
		self._fields = client.vocabularies.builtin("project")
		vocabularies = {
			"disciplines": client.vocabularies.disciplines(True),
			"visibility": client.vocabularies.visibility(True)
		}
		for item in self._fields:
			if item.vocabulary:
				self._vocabularies[item.path] = vocabularies[item.path]

###############################################################################

	@staticmethod
	def _parse_organizations(data: List):
		return [value["url"] for value in data]

###############################################################################

	def parse(self, data: dict) -> None:
		for path, value in data.items():
			if path in ["id", "slug", "parentId"]:  # ignored paths
				continue
			if path == "organizations":
				value = self._parse_organizations(value)
			try:
				key = self.name_of(path)
				self.set_value(key, value, True)
			except KeyError:
				continue

###############################################################################

	def generate(self) -> dict:
		metadata = {}
		missing = []

		for key, value in self.items():
			if not value:
				if self.is_required(key):
					missing.append(key)
				continue
			properties = self.properties(key)
			metadata[properties.path] = value.raw()

			# The organizations field is normally controlled, but we omit
			# actively controlling it, because doing so is too complicated.
			# Because we handle things differently here, some special care
			# is needed when preparing it for Coscine:
			if properties.path == "organizations":
				metadata[properties.path] = [{
					"displayName": url, "url": url
				} for url in value.raw()]
		if missing:
			raise ValueError(missing)
		return metadata

###############################################################################
# Class definition
###############################################################################

class Project:
	"""
	Python representation of a Coscine Project
	"""

	client: Client
	data: dict
	parent: Optional[Project]

###############################################################################

	def __init__(self, client: Client, data: dict,
			parent: Optional[Project] = None) -> None:
		"""
		Initializes a Coscine project object.

		Parameters
		----------
		client : Client
			Coscine client handle
		data : dict
			Project data received from Coscine.
		parent : Project, default: None
			Optional parent project.
		"""

		self.client = client
		self.data = data
		self.parent = parent

###############################################################################

	@property
	def id(self) -> str:
		"""
		Project ID
		"""
		return self.data["id"]

	@property
	def name(self) -> str:
		"""
		Project Name
		"""
		return self.data["projectName"]

	@property
	def display_name(self) -> str:
		"""
		Project Display Name
		"""
		return self.data["displayName"]

	@property
	def description(self) -> str:
		"""
		Project Description
		"""
		return self.data["description"]

	@property
	def principle_investigators(self) -> str:
		"""
		Project PIs
		"""
		return self.data["principleInvestigators"]

	@property
	def start_date(self) -> datetime:
		"""
		Project Start Date as datetime object
		"""
		return dateutil.parser.parse(self.data["startDate"])

	@property
	def end_date(self) -> datetime:
		"""
		Project End Date as datetime object
		"""
		return dateutil.parser.parse(self.data["endDate"])

	@property
	def disciplines(self) -> List[str]:
		"""
		Project Disciplines
		"""
		lang = {
			"en": "displayNameEn",
			"de": "displayNameDe"
		}[self.client.settings.language]
		return [k[lang] for k in self.data["disciplines"]]

	@property
	def organizations(self) -> List[str]:
		"""
		Project Associated Organizations
		"""
		return [k["displayName"] for k in self.data["organizations"]]

	@property
	def visibility(self) -> str:
		"""
		Project Visibility in Coscine
		"""
		return self.data["visibility"]["displayName"]

###############################################################################

	def __str__(self) -> str:
		table = PrettyTable(("Property", "Value"))
		rows = [
			("ID", self.id),
			("Name", self.name),
			("Display Name", self.display_name),
			("Description", self.description),
			("Principle Investigators", self.principle_investigators),
			("Disciplines", "\n".join(self.disciplines)),
			("Organizations", "\n".join(self.organizations)),
			("Start Date", self.start_date),
			("End Date", self.end_date),
			("Visibility", self.visibility)
		]
		table.max_width["Value"] = 50
		table.add_rows(rows)
		return table.get_string(title=f"Project {self.display_name}")

###############################################################################

	def subprojects(self) -> List[Project]:
		"""
		Retrieves a list of a all projects the creator of the Coscine API token
		is currently a member of.

		Returns
		-------
		list
			List of coscine.Project objects
		"""

		uri = self.client.uri("Project", "SubProject", self.id)
		projects = []
		for data in self.client.get(uri).json():
			projects.append(Project(self.client, data, self))
		return projects

###############################################################################

	def subproject(self, display_name: str) -> Optional[Project]:
		"""
		Returns a single subproject via its displayName

		Parameters
		----------
		display_name : str
			Look for a project with the specified displayName

		Returns
		-------
		Project
			A single coscine project handle or None if no match found

		Raises
		------
		IndexError
		"""

		filtered_project_list = list(filter(
			lambda project: project.display_name == display_name,
			self.subprojects()
		))
		if len(filtered_project_list) == 1:
			return filtered_project_list[0]
		if len(filtered_project_list) == 0:
			return None
		raise IndexError("More than 1 project matching "
								"the specified criteria!")

###############################################################################

	def create_subproject(self, form: ProjectForm) -> Project:
		"""
		Creates a subproject inside of the current project
		"""
		metadata = form.generate()
		metadata["ParentId"] = self.id
		return self.client.create_project(metadata)

###############################################################################

	def delete(self) -> None:
		"""
		Deletes the project on the Coscine servers.
		"""

		uri = self.client.uri("Project", "Project", self.id)
		self.client.delete(uri)

###############################################################################

	def resources(self) -> List[Resource]:
		"""
		Retrieves a list of Resources of the current project.

		Returns
		-------
		list[Resource]
			list of resources matching the supplied filter.
		"""

		uri = self.client.uri("Project", "Project", self.id, "resources")
		resources = []
		for data in self.client.get(uri).json():
			resources.append(Resource(self, data))
		return resources

###############################################################################

	def resource(self, display_name: str) -> Optional[Resource]:
		"""
		Retrieves a certain resource of the current project
		identified by its displayName.

		Parameters
		----------
		display_name : str
			The display name of the resource.

		Returns
		--------
		Resource or None

		Raises
		-------
		IndexError
		"""

		resources = list(filter(
			lambda resource: resource.display_name == display_name,
			self.resources()
		))
		if len(resources) == 1:
			return resources[0]
		if len(resources) == 0:
			return None
		raise IndexError("Found more than 1 resource matching "
									"the specified criteria!")

###############################################################################

	def download(self, path: str = "./", metadata: bool = False) -> None:
		"""
		Downloads the project to the location referenced by 'path'.

		Parameters
		----------
		path : str
			Download location on the harddrive
			Default: current directory './'
		metadata : bool, default: False
			If enabled, project metadata is downloaded and put in
			a hidden file '.metadata.json'.
		"""

		logger.info(f"Downloading project '{self.name}' ({self.id})...")
		path = os.path.join(path, self.display_name)
		if not os.path.isdir(path):
			os.mkdir(path)
		for resource in self.resources():
			resource.download(path=path, metadata=metadata)
		if metadata:
			data = json.dumps(self.data, indent=4)
			metadata_path: str = os.path.join(path, ".metadata.json")
			with open(metadata_path, "w", encoding="utf-8") as file:
				file.write(data)

###############################################################################

	def members(self) -> List[ProjectMember]:
		"""
		Retrieves a list of all members of the current project

		Returns
		--------
		list[ProjectMember]
			List of project members as ProjectMember objects.
		"""

		uri = self.client.uri("Project", "ProjectRole", self.id)
		data = self.client.get(uri).json()
		members = [ProjectMember(self, m) for m in data]
		return members

###############################################################################

	def invite(self, email: str, role: str = "Member") -> None:
		"""
		Invites a person to a project via their email address

		Parameters
		----------
		email : str
			The email address to send the invite to
		role : str, "Member" or "Owner", default: "Member"
			The role for the new project member
		"""

		if role not in ProjectMember.ROLES:
			raise ValueError(f"Invalid role {role}.")

		uri = self.client.uri("Project", "Project", "invitation")
		data = {
			"projectId": self.data["id"],
			"role": ProjectMember.ROLES[role],
			"email": email
		}

		try:
			logger.info(f"Inviting {email} as {role} to project {self.name}.")
			self.client.post(uri, json=data)
		except RuntimeError:
			logger.warning(f"User {email} has invite pending.")

###############################################################################

	def add_member(self, member: ProjectMember, role: str = "Member"):
		"""
		Adds a project member of another project to the current project.

		Parameters
		----------
		member : ProjectMember
			Member of another Coscine project
		role : str, "Member" or "Owner", default: "Member"

		Raises
		------
		ValueError
			In case the specified role is unsupported
		"""

		if role not in ProjectMember.ROLES:
			raise ValueError(f"Invalid role for member '{member.name}'!")
		data = member.data
		data["projectId"] = self.id
		data["role"]["displayName"] = role
		data["role"]["id"] = ProjectMember.ROLES[role]
		uri = self.client.uri("Project", "ProjectRole")
		self.client.post(uri, json=data)
		logger.info(f"Added '{member.name}' as a project member with "
							f"role '{role}' to project '{self.name}'.")

###############################################################################

	def form(self) -> ProjectForm:
		"""
		Returns the project metadata form of the project. That form can
		then be used to edit the project metadata.

		Examples
		---------
		>>> metadata = Project.form()
		>>> metadata["Display Name"] = "Different display name"
		>>> Project.update(metadata)
		"""

		form = ProjectForm(self.client)
		form.parse(self.data)
		return form

###############################################################################

	def update(self, form: Union[ProjectForm, dict]) -> Project:
		"""
		Updates a project using the given ProjectForm

		Parameters
		----------
		form : ProjectForm or dict
			ProjectForm containing updated data or dict generated from a form.
		"""

		if isinstance(form, ProjectForm):
			form = form.generate()
		uri = self.client.uri("Project", "Project", self.id)
		response = self.client.post(uri, json=form)
		logger.info(f"Updated project metadata for '{self.name}' ({self.id}).")
		updated_project_handle = self
		if response.ok:
			# Update project properties
			# The response unfortunately does not return
			# the new project data - bummer!
			updated_project_handle = list(filter(
				lambda p: p.id == self.id,
				self.client.projects(False)
			))[0]
		return updated_project_handle

###############################################################################

	def create_resource(self, form: Union[ResourceForm, dict]) -> Resource:
		"""
		Creates a resource within the current project using the supplied
		resource form.

		Parameters
		----------
		resourceForm : ResourceForm
			Form to generate the resource with.
		metadataPreset : MetadataPresetForm
			optional application profile configuration.
			Currently not supported.
		"""
		if isinstance(form, ResourceForm):
			form = form.generate()
		uri = self.client.uri("Resources", "Resource", "project", self.id)
		logger.info(f"Creating resource in project '{self.name}'.")
		return Resource(self, self.client.post(uri, json=form).json())

###############################################################################
###############################################################################

class ProjectMember:
	"""
	Python representation of a Coscine project member.
	"""

	ROLES = {
		"Owner": "be294c5e-4e42-49b3-bec4-4b15f49df9a5",
		"Member": "508b6d4e-c6ac-4aa5-8a8d-caa31dd39527"
	}

	data: dict
	client: Client
	project: Project

###############################################################################

	@property
	def name(self) -> str:
		"""Name of the Project Member"""
		return self.data["user"]["displayName"]

	@property
	def email(self) -> str:
		"""E-Mail address of the Project Member"""
		return self.data["user"]["emailAddress"]

	@property
	def id(self) -> str:
		"""Project Member ID"""
		return self.data["user"]["id"]

	@property
	def role(self) -> str:
		"""Role of the Project Member within the Project"""
		return self.data["role"]["displayName"]

###############################################################################

	def __init__(self, project: Project, data: dict) -> None:
		"""
		Initializes a project member for a given project.

		Parameters
		----------
		project : Project
			Coscine Python SDK project handle.
		data: dict
			User data as dict, retrieved via
			client.uri("Project", "ProjectRole", self.id).
		"""

		self.project = project
		self.client = self.project.client
		self.data = data

###############################################################################

	def set_role(self, role: str) -> None:
		"""
		Sets the role of a project member

		Parameters
		----------
		role : str
			The new role of the member ('Owner' or 'Member').
		"""

		if role not in ProjectMember.ROLES:
			raise ValueError(f"Invalid role {role}.")

		uri = self.client.uri("Project", "ProjectRole")
		self.data["role"]["id"] = ProjectMember.ROLES[role]
		self.data["role"]["displayName"] = role
		logger.info(f"Setting role of '{self.name}' to {role}...")
		self.client.post(uri, json=self.data)

###############################################################################

	def remove(self) -> None:
		"""
		Removes a project member from their associated project.
		"""

		uri = self.client.uri("Project", "ProjectRole", "project",
						self.project.id, "user", self.id, "role",
						self.data["role"]["id"])
		logger.info(f"Removing member '{self.name}' "
					f"from project '{self.project.name}'...")
		self.client.delete(uri)

###############################################################################
