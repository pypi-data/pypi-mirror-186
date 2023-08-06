#!/usr/bin/env python

import logging
import os
import subprocess
from abc import ABCMeta, abstractmethod

from soyuz.utils import UploaderException, NotValidFolderException


class Storage(object):
    __metaclass__ = ABCMeta

    def __init__(self, api, context):
        self._api = api
        self._context = context

    @abstractmethod
    def validate_target_dir(self, folder):
        raise NotImplementedError()

    @abstractmethod
    def upload_file(self, data_file, remote_folder, types, properties):
        raise NotImplementedError()

    @abstractmethod
    def remove_file(self, data_file, remote_folder):
        raise NotImplementedError()

    @abstractmethod
    def remove_target_dir(self, folder):
        raise NotImplementedError()


class DNAnexusStorage(Storage):
    NAME = "dnanexus"

    def __init__(self, api, context):
        # type: (DxApi, Context) -> None
        super(DNAnexusStorage, self).__init__(api, context)

        self.basedir = self._context.get_base_dir()
        self.token = self._context.get_token()
        self.ua_path = self._context.get_ua_path()
        self.ua_parameters = self._context.get_ua_parameters()
        self.__project = self._context.get_project_id()

    def get_project_id(self):
        return self.__project

    def get_project(self):
        return self._api.get_project(self.get_project_id())

    def get_file_by_id(self, file_id):
        return self._api.get_file(file_id)

    def validate_target_dir(self, folder):
        if not folder.is_valid:
            raise NotValidFolderException(
                "{} is not valid".format(folder.get_name()))

    def upload_file(self, data_file, remote_folder, types, properties):
        logging.info("Uploading {} to {}".format(data_file.get_full_path(), remote_folder))
        dx_file = self._api.upload_local_file(data_file.get_full_path(),
                                              folder=remote_folder,
                                              keep_open=True,
                                              parents=True)
        if dx_file:
            dx_file.add_types(types)
            dx_file.set_properties(properties)
            dx_file.close()
        else:
            raise UploaderException("Failed to upload {}".format(data_file.get_full_path()))
        return dx_file.get_id()

    def remove_target_dir(self, folder):
        logging.debug("{} folder will be removed from DNANexus".format(folder.get_name()))

        project = self._api.get_project(self.get_project_id())
        project.remove_folder(os.path.join(self.basedir, folder.get_name()), recurse=True, force=True)

    def remove_file(self, data_file, remote_folder):
        files = self._api.find_data_objects(classname="file", name=data_file.get_name(), folder=remote_folder,
                                            return_handler=True)
        for remote_file in files:
            describe = remote_file.describe(fields={'state', 'name'})
            if describe['state'] != 'closed':
                logging.warning("{}{} file will be removed from DNANexus".format(remote_folder, describe['name']))
                remote_file.remove()


class DNAnexusStorageUA(DNAnexusStorage):
    def upload_file(self, data_file, remote_folder, types, properties):
        logging.info("Uploading {} to {}".format(data_file.get_full_path(), remote_folder))
        args = [r'"{}"'.format(self.ua_path), data_file.get_full_path().replace("(", "\(").replace(")", "\)")]
        args.extend(["--auth-token", self.token])
        args.extend(["-p", self.get_project_id()])
        args.extend(["-f", remote_folder])
        args.extend([self.ua_parameters])
        args.extend(["--type {}".format(_type) for _type in types])
        args.extend(["--property {}={}".format(key, val) for key, val in properties.items()])
        args.extend(["-g"])
        args.extend(["--do-not-compress"])
        file_id = subprocess.check_output(" ".join(args), shell=True).strip().decode('utf8').replace("'", '"')
        return file_id


class ExodusStorage(Storage):
    NAME = "stella"

    def __init__(self, api, context):
        super(ExodusStorage, self).__init__(api, context)

        if not context.get_exodus_url():
            raise UploaderException("Exodus URL was not specified")

    def validate_target_dir(self, folder):
        if not folder.is_valid:
            raise NotValidFolderException(
                "{} is not valid".format(folder.get_name()))

    def upload_file(self, data_file, remote_folder, types, properties):
        logging.info("Uploading {} to {}".format(data_file.get_full_path(), remote_folder))
        result = self._api.upload_local_file(file_full_path=data_file.get_full_path(),
                                             name=data_file.get_name(),
                                             folder=remote_folder,
                                             types=types,
                                             properties=properties,
                                             tags=[])

        logging.info("Successfully uploaded: {} to {}".format(data_file.get_full_path(), remote_folder))

        return result['link']

    def remove_target_dir(self, folder):
        raise NotImplementedError()

    def remove_file(self, data_file, remote_folder):
        logging.warning("Remove file not supported for exodus storage")


class StorageType(object):
    DNANEXUS = DNAnexusStorage.NAME
    EXODUS = ExodusStorage.NAME
    DEFAULT = DNANEXUS
    ALL = [DNANEXUS, EXODUS]


class StorageFactory(object):
    @staticmethod
    def create(api, context):
        # type: (DxApi|ExodusApi, Context) -> Storage

        if context.get_storage() == DNAnexusStorage.NAME:
            return DNAnexusStorageUA(api, context) if context.get_ua_path() else DNAnexusStorage(api, context)
        elif context.get_storage() == ExodusStorage.NAME:
            return ExodusStorage(api, context)
        raise UploaderException("Storage with name {} was not found".format(context.get_storage()))
