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
This file provides a simple wrapper around Coscine application profiles.
It abstracts the interaction with rdf graphs using rdflib and
provides a more intuitive, Coscine-specific interface to these graphs.
"""

###############################################################################
# Dependencies
###############################################################################

from __future__ import annotations
from typing import List
import rdflib

###############################################################################
# Classes / Functions / Scripts
###############################################################################

class ApplicationProfile:
	"""
	The ApplicationProfile class serves as a wrapper around Coscine
	application profiles. Coscine application profiles are served
	as rdf graphs which are difficult to interact with, without 3rd
	party libraries.
	The ApplicationProfile class abstracts this interaction.

	Attributes
	----------
	graph : rdflib.Graph
		An rdf graph parsed with the help of rdflib
	RDFTYPE : str
		A variable frequently used by methods of this class.
	"""

	graph: rdflib.Graph
	RDFTYPE: str = "http://www.w3.org/1999/02/22-rdf-syntax-ns#type"

###############################################################################

	def __init__(self, graph: str, format: str = "json-ld") -> None:
		"""
		Initializes an instance of the ApplicationProfile wrapper class.

		Parameters
		----------
		graph : str
			A Coscine application profile rdf graph in json-ld text format.
		format : str (optional), default: "json-ld"
			The format of the graph
		"""

		self.graph = rdflib.Graph()
		self.graph.bind("sh", "http://www.w3.org/ns/shacl#")
		self.graph.bind("dcterms", "http://purl.org/dc/terms/")
		self.graph.parse(data=graph, format=format)

###############################################################################

	def __str__(self) -> str:
		"""
		Serializes the application profile rdf graph used internally
		for easy output to stdout.
		"""
		# Explicitly return as str because pylint does not understand
		# rdflib's ambiguous return type for this method.
		return str(self.graph.serialize(format="ttl"))

###############################################################################

	def target(self) -> str:
		"""
		Returns a str indicating the target class of the application profile.
		This may for example be "engmeta" in case of an engmeta profile.
		"""

		query = \
			"""
			SELECT ?target WHERE {
				?_ sh:targetClass ?target .
			}
			"""
		result = self.query(query)
		return str(result[0][0])  # Force string

###############################################################################

	def query(self, query: str, **kwargs) -> List[List[object]]:
		"""
		Performs a SPARQL query against the application profile and
		returns the result as a list of rows.
		"""

		items = []
		results = self.graph.query(query, **kwargs)
		for row in results:
			item = []
			for val in row:
				value = val.toPython() if val is not None else None
				item.append(value)
			items.append(item)
		return items

###############################################################################

	def items(self) -> List[dict]:
		"""
		Returns all items contained within the application profile as a list
		of key value pairs in their order of appearance.
		"""

		query = \
			"""
			SELECT ?path ?name ?order ?class ?minCount ?maxCount
						?datatype (lang(?name) as ?lang) WHERE {
				?_ sh:path ?path ;
					sh:name ?name ;
					sh:order ?order .
				OPTIONAL { ?_ sh:class ?class . } .
				OPTIONAL { ?_ sh:minCount ?minCount . } .
				OPTIONAL { ?_ sh:maxCount ?maxCount . } .
				OPTIONAL { ?_ sh:datatype ?datatype . } .
			}
			ORDER BY ASC(?order)
			"""
		items_de = []
		items_en = []
		items = []
		results = self.query(query)
		for result in results:
			lang = result[7]
			properties = {
				"path": result[0],
				"name": result[1],
				"order": result[2],
				"class": result[3],
				"minCount": result[4] if result[4] else 0,
				"maxCount": result[5] if result[5] else 42,
				"datatype": result[6]
			}
			if lang == "de":
				items_de.append(properties)
			else:
				items_en.append(properties)

		# Fuse language lists into one
		# An application profile may only contain a single language!
		# in that case, primary == secondary language
		primary_language = items_de if len(items_de) > 0 else items_en
		secondary_language = items_en if len(items_en) > 0 else items_de
		for index, item in enumerate(primary_language):
			item["name"] = [item["name"], secondary_language[index]["name"]]
			items.append(item)
		return items

###############################################################################

	def length(self) -> int:
		"""
		Returns the number of fields contained within the application profile.
		"""

		query = \
			"""
			SELECT ?path WHERE {
				?_ sh:path ?path ;
					sh:order ?order .
			}
			"""
		results = self.query(query)
		return len(results)

###############################################################################
