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
This file defines the S3 object for interacting with Coscine S3
resources (natively).
"""

###############################################################################
# Dependencies
###############################################################################

from __future__ import annotations
import logging
import os
from typing import Optional, Callable, Any
from prettytable import PrettyTable
from coscine.utils import ProgressBar
try:
	import boto3
except ImportError:
	boto3 = None

###############################################################################
# Module globals / Constants
###############################################################################

logger = logging.getLogger(__name__)

###############################################################################
# Classes / Functions / Scripts
###############################################################################

class S3:
	"""
	Provides a simple pythonic interface to the underlying S3 storage
	of a resource. The attributes may all be null in case the resource
	is not of type S3.
	"""

	_read_access_key: Optional[str]
	_read_secret_key: Optional[str]
	_write_access_key: Optional[str]
	_write_secret_key: Optional[str]
	_endpoint: Optional[str]
	_bucket: Optional[str]
	_data: dict
	_s3_client: Optional[Any]
	verbose: bool

	@property
	def read_access_key(self) -> Optional[str]:
		"""The S3 resource read_access_key for read only access"""
		return self._read_access_key

	@property
	def read_secret_key(self) -> Optional[str]:
		"""The S3 resource read_secret_key for read only access"""
		return self._read_secret_key

	@property
	def write_access_key(self) -> Optional[str]:
		"""The S3 resource write_access_key for read/write access"""
		return self._write_access_key

	@property
	def write_secret_key(self) -> Optional[str]:
		"""The S3 resource write_secret_key for read/write access"""
		return self._write_secret_key

	@property
	def bucket(self) -> Optional[str]:
		"""The S3 bucket name of the resource"""
		return self._bucket

	@property
	def endpoint(self) -> Optional[str]:
		"""The S3 endpoint"""
		return self._endpoint

###############################################################################

	def __init__(self, data: dict, verbose: bool = False) -> None:
		self._data = data
		self.verbose = verbose
		if "resourceTypeOption" in data and data["resourceTypeOption"]:
			opt: dict = data["resourceTypeOption"]
			self._read_access_key = opt.get("ReadAccessKey")
			self._read_secret_key = opt.get("ReadSecretKey")
			self._write_access_key = opt.get("WriteAccessKey")
			self._write_secret_key = opt.get("WriteSecretKey")
			self._endpoint = opt.get("Endpoint")
			self._bucket = opt.get("BucketName")
			if boto3 and self.write_secret_key:
				self._s3_client = boto3.client(
					"s3",
					aws_access_key_id=self.write_access_key,
					aws_secret_access_key=self.write_secret_key,
					endpoint_url=self.endpoint
				)
			else:
				self._s3_client = None

###############################################################################

	def __str__(self) -> str:
		table = PrettyTable(["Property", "Value"])
		rows = [
			("read_access_key", self.read_access_key),
			("read_secret_key", self.read_secret_key),
			("write_access_key", self.write_access_key),
			("write_secret_key", self.write_secret_key),
			("endpoint", self.endpoint),
			("bucket", self.bucket)
		]
		table.max_width["Value"] = 50
		table.add_rows(rows)
		return table.get_string(title="S3")

###############################################################################

	def mkdir(self, path: str) -> None:
		"""
		Creates a directory
		"""
		if not self._s3_client:
			raise ModuleNotFoundError("S3.mkdir() requires package 'boto3'!")
		logger.info(f"Creating directory '{path}' in "
					f"S3 resource '{self.bucket}'...")
		self._s3_client.put_object(Bucket=self.bucket, Key=path)

###############################################################################

	def upload(
		self,
		key: str,
		file,
		callback: Optional[Callable[[int], None]] = None
	) -> None:
		"""
		Uploads a file-like object to an S3 resource on the Coscine server

		Parameters
		----------
		key : str
			filename of the file-like object.
		file : object with read() attribute
			Either open file handle or local file location path.
		callback : Callable[[int], None], default: None
			Optional callback called during chunk uploads
			indicating the progress.

		Raises
		------
		TypeError
			In case the file object specified cannot be used.
		"""
		if not self._s3_client:
			raise ModuleNotFoundError("S3.upload() requires package 'boto3'!")
		logger.info(f"Uploading FileObject '{key}' to "
					f"S3 resource '{self.bucket}'...")

		#######################################################################
		def s3upload(
			s3_client,
			key: str,
			file,
			filesize: int,
			callback: Optional[Callable[[int], None]] = None
		) -> None:
			progress_bar = ProgressBar(self.verbose, filesize, key, callback)
			s3_client.upload_file(file, self.bucket, key,
							Callback=progress_bar.update)
		#######################################################################

		if hasattr(file, "read"):  # FIXME: How to get the size?
			s3upload(self._s3_client, key, file, 10**6, callback)
		elif isinstance(file, str):
			s3upload(self._s3_client, key, file,
				os.stat(file).st_size, callback)
		else:
			raise TypeError("Argument `file` has unexpected type!")

###############################################################################
