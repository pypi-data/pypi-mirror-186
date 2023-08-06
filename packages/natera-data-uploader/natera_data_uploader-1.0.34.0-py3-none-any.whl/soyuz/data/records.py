#!/usr/bin/env python

import logging
import os
from abc import ABCMeta, abstractmethod

from soyuz import __version__ as version
from soyuz.api.dx import DxApi
from soyuz.api.exodus import ExodusApi
from soyuz.dx.variables import Type, Property
from soyuz.utils import UploaderException


class Record(object):
    __metaclass__ = ABCMeta

    def __init__(self, api, basedir, name):
        self._api = api
        self._id = None
        self._details = None
        self._tags = None
        self._types = None
        self._properties = None
        self._record = None
        self._basedir = basedir
        self._name = name

    @abstractmethod
    def get_id(self):
        raise NotImplementedError()

    @abstractmethod
    def close(self):
        raise NotImplementedError()

    @abstractmethod
    def get_details(self):
        raise NotImplementedError()

    @abstractmethod
    def add_tags(self, tags):
        raise NotImplementedError()

    @abstractmethod
    def set_details(self, details):
        raise NotImplementedError()

    @abstractmethod
    def get_properties(self):
        raise NotImplementedError()

    @abstractmethod
    def set_properties(self, properties):
        raise NotImplementedError()

    @abstractmethod
    def add_property(self, key, value):
        raise NotImplementedError()

    @abstractmethod
    def is_closed(self):
        raise NotImplementedError()


class DNAnexusRecord(Record):
    def __init__(self, api, basedir, name):
        super(DNAnexusRecord, self).__init__(api, basedir, name)

        existing_records = self._api.find_data_objects(classname="record",
                                                       folder=os.path.join(basedir, name).replace("\\", "/"),
                                                       typename=Type.UPLOAD_SENTINEL,
                                                       properties={Property.RUN_FOLDER: name},
                                                       return_handler=True)
        if not existing_records:
            self.__record = self._api.create_record(types=[Type.UPLOAD_SENTINEL],
                                                    folder=os.path.join(basedir, name).replace("\\", "/"),
                                                    name="{}_upload_sentinel".format(name),
                                                    properties={Property.RUN_FOLDER: name,
                                                                Property.VERSION: version},
                                                    parents=True)
        else:
            self.__record = existing_records[0]

    def get_id(self):
        return self.__record.get_id()

    def close(self):
        return self.__record.close()

    def is_closed(self):
        return self.__record.describe(fields={'state'})['state'] == 'closed'

    def get_details(self):
        return self.__record.get_details()

    def set_details(self, details):
        return self.__record.set_details(details)

    def get_properties(self):
        return self.__record.get_properties()

    def set_properties(self, properties):
        return self.__record.set_properties(properties)

    def add_property(self, key, value):
        properties = self.__record.get_properties()
        properties[key] = value
        self.set_properties(properties)

    def add_tags(self, tags):
        return self.__record.add_tags(tags)


class ExodusRecord(Record):
    def __init__(self, api, basedir, name):
        super(ExodusRecord, self).__init__(api, basedir, name)
        self.__id = None
        self.__record = None
        self.__name = name
        self.__basedir = basedir
        self.__details = {}
        self.__properties = {Property.RUN_FOLDER: self.__name, Property.VERSION: version}
        self.__tags = []
        self.__types = []

    def close(self):
        data = self._api.create_record(
            name=self.__name,
            folder=os.path.join(self.__basedir, self.__name).replace("\\", "/"),
            types=[Type.UPLOAD_SENTINEL],
            properties=self.__properties,
            tags=self.__tags,
            details=self.__details
        )

        self.__id = data['link']
        logging.info("Successfully created: {}".format(os.path.join(self.__basedir, self.__name)))

        return self.__id

    def is_closed(self):
        return False

    def get_id(self):
        return self.__id

    def get_details(self):
        return self.__details

    def set_details(self, details):
        self.__details = details

    def add_tags(self, tags):
        self.__tags.extend(tags)
        self.__tags = list(set(self.__tags))

    def get_properties(self):
        return self.__properties

    def set_properties(self, properties):
        self.__properties = dict(properties)

    def add_property(self, key, value):
        self.__properties[key] = value


class RecordFactory(object):
    @staticmethod
    def create(api, basedir, name):
        if isinstance(api, DxApi):
            return DNAnexusRecord(api, basedir, name)
        if isinstance(api, ExodusApi):
            return ExodusRecord(api, basedir, name)
        raise UploaderException("API which can work with {} was not found".format(name))
