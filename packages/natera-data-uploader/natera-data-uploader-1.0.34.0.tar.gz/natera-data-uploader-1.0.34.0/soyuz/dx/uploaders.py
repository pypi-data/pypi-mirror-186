#!/usr/bin/env python
import errno
import logging
import os
import tarfile
import threading
import time
from abc import ABCMeta, abstractmethod
from contextlib import contextmanager
from multiprocessing.pool import ThreadPool

import zope.event
import zope.event.classhandler

from soyuz.api.dx import DxApi
from soyuz.api.exodus import ExodusApi
from soyuz.data.files import DataFile
from soyuz.data.folders import WesSignateraSeqFolder, PersonalisSeqFolder, RawSeqFolder, BgiSeqFolder, SeqFolderBase, \
    SangerSeqFolder, NgsSeqFolder
from soyuz.data.storages import StorageFactory
from soyuz.dx.context import Context
from soyuz.dx.sentinels import WesSignateraSentinel, RawSentinel, PersonalisSentinel, SangerSentinel, NgsSentinel
from soyuz.dx.variables import Type, Property
from soyuz.event.upload import SeqFolderUploadStart, SeqFolderUploadComplete, UploadJobTerminated, \
    SeqFolderUploadTerminated, NewUploadJob, DataFileUploadStart, DataFileUploadFinish
from soyuz.utils import UploaderException, timeit, get_expected_time, NotValidFolderException, \
    LOGGER_FORMAT


@contextmanager
def poolcontext(*args, **kwargs):
    pool = ThreadPool(*args, **kwargs)
    yield pool
    pool.terminate()


class WatchUploader(object):
    __metaclass__ = ABCMeta

    def __init__(self, context, api):
        # type: (Context, DxApi|ExodusApi) -> None

        self.__context = context
        self.__api = api

    def watch(self, watch_dir):
        if self.__context.is_force_upload():
            watch_dir.remove_uploaded_file()
            watch_dir.remove_uploading_file()

        while True:
            for seq_folder in watch_dir.get_seq_folders():
                if watch_dir.is_uploaded(seq_folder.get_name()):
                    logging.info("{} already uploaded. Skipping".format(seq_folder.get_name()))
                    continue

                if watch_dir.is_uploading(seq_folder.get_name()):
                    logging.info("{} is uploading. Skipping".format(seq_folder.get_name()))
                    continue

                threading.Thread(target=self.__upload, args=(seq_folder,), daemon=True).start()

            time.sleep(self.__context.get_interval())

    def __upload(self, seq_folder):
        try:
            uploader = DxUploaderFactory.create(self.__context, self.__api, seq_folder)
            uploader.upload(seq_folder)
        except Exception as e:
            logging.error("{}. Skipping".format(e))


class DxUploaderBase(object):
    __metaclass__ = ABCMeta

    def __init__(self, context, api):
        # type: (Context, DxApi|ExodusApi) -> None

        self._context = context
        self._api = api
        self._storage = StorageFactory.create(self._api, context)
        self.__terminated_seq_folder_names = set()
        self.__upload_conditions = {}
        self.__seq_folder_name_to_upload_job_id = {}

        self.__init_listeners()

    def __call__(self, data_file):
        return self.upload_file(data_file)

    @timeit
    def upload(self, seq_folder):
        seq_folder_name = seq_folder.get_name()

        with SeqFolderLogUploader(logging.root, seq_folder_name, self._storage, self._context.get_base_dir()):
            try:
                if self._context.is_force_upload():
                    logging.info("Force upload is enabled, removing folder {} before upload".format(seq_folder_name))
                    self.remove_target_dir(seq_folder)
                    seq_folder.remove_upload_info_file()

                self._validate_target_dir(seq_folder)

                logging.info("Starting upload for {}".format(seq_folder_name))
                sentinel = self._create_sentinel(seq_folder_name)

                if sentinel.is_closed():
                    logging.info("The {} folder is already uploaded".format(seq_folder_name))
                    return

                zope.event.notify(SeqFolderUploadStart(seq_folder, sentinel))

                if self._context.is_constellation_portal_mode():
                    event = threading.Event()
                    self.__upload_conditions[seq_folder_name] = event
                    logging.info(
                        "Constellation mode is enabled, waiting for the job to be started from Constellation Portal")
                    event.wait()

                    sentinel.add_property(Property.JOB_ID, self.__seq_folder_name_to_upload_job_id[seq_folder_name])

                if self._context.get_process_count() > 1:
                    with poolcontext(processes=self._context.get_process_count()) as pool:
                        results = pool.map(self, seq_folder.list_files())
                else:
                    results = [self.upload_file(data_file) for data_file in seq_folder.list_files()]

                if seq_folder_name not in self.__terminated_seq_folder_names:
                    for data_file, file_id in results:
                        sentinel.add_file(data_file, file_id)

                    sentinel.close()
                    logging.info("{} folder has been successfully uploaded".format(seq_folder_name))
                    zope.event.notify(SeqFolderUploadComplete(seq_folder))
                else:
                    zope.event.notify(SeqFolderUploadTerminated(seq_folder))
                    logging.info("Upload {} folder has been terminated".format(seq_folder_name))
                    self.__terminated_seq_folder_names.remove(seq_folder_name)
            except NotValidFolderException as e:
                logging.error("Upload {} folder has been failed due to validation error: {}".format(seq_folder_name, e))
                self.remove_target_dir(seq_folder)
                raise e
            except BaseException as e:
                logging.error(e, exc_info=True)
                raise e

    def upload_file(self, data_file):
        if data_file.get_seq_folder_name() not in self.__terminated_seq_folder_names:
            zope.event.notify(DataFileUploadStart(data_file))

            remote_folder = os.path.join(self._context.get_base_dir(),
                                         data_file.get_seq_folder_name(),
                                         data_file.get_relative_path()).replace("\\", "/")
            types = self._get_additional_types(data_file)
            types.append(Type.UPLOAD_DATA)
            properties = self._get_additional_properties(data_file, data_file.get_seq_folder_name())
            properties[Property.RUN_FOLDER] = data_file.get_seq_folder_name()
            try:
                file_id = self._storage.upload_file(data_file, remote_folder, types, properties)
            except BaseException as ex:
                self._storage.remove_file(data_file, remote_folder)
                raise ex

            zope.event.notify(DataFileUploadFinish(data_file, file_id))

            return data_file, file_id
        else:
            return data_file, None

    def remove_target_dir(self, seq_folder):
        self._storage.remove_target_dir(seq_folder)

    def _validate_target_dir(self, folder):
        self._storage.validate_target_dir(folder)

    @abstractmethod
    def _create_sentinel(self, seq_folder_name):
        raise NotImplementedError()

    @abstractmethod
    def _get_additional_types(self, data_file):
        raise NotImplementedError()

    @abstractmethod
    def _get_additional_properties(self, data_file, seq_folder_name):
        raise NotImplementedError()

    def __init_listeners(self):
        @zope.event.classhandler.handler(UploadJobTerminated)
        def on_upload_job_terminated(event):
            # type: (UploadJobTerminated) -> None
            self.__terminated_seq_folder_names.add(event.seq_folder_name)

        @zope.event.classhandler.handler(NewUploadJob)
        def on_new_upload_job(event):
            # type: (NewUploadJob) -> None
            if event.seq_folder_name in self.__upload_conditions:
                logging.info('Upload job was found: {}, resuming upload'.format(event.job_id))
                self.__seq_folder_name_to_upload_job_id[event.seq_folder_name] = event.job_id
                self.__upload_conditions[event.seq_folder_name].set()


class WesSignateraDxUploader(DxUploaderBase):
    SEQ_FOLDER_TYPE = WesSignateraSeqFolder

    def _create_sentinel(self, seq_folder_name):
        return WesSignateraSentinel(self._api, self._context.get_base_dir(), seq_folder_name)

    def _get_additional_types(self, data_file):
        types = []
        data_type = data_file.get_type()
        if data_type:
            types.append(data_type)
            if data_type == Type.CSV and data_file.get_name().startswith("WES-QCMetrics"):
                types.append(Type.WESQCREPORT)
        return types

    def _get_additional_properties(self, data_file, seq_folder_name):
        properties = {}
        if data_file.get_sample_id():
            properties[Property.SAMPLE_REFERENCE] = "{}/{}".format(seq_folder_name, data_file.get_sample_id())
        return properties


class PersonalisDxUploader(DxUploaderBase):
    SEQ_FOLDER_TYPE = PersonalisSeqFolder

    def _create_sentinel(self, seq_folder_name):
        return PersonalisSentinel(self._api, self._context.get_base_dir(), seq_folder_name)

    def _get_additional_types(self, data_file):
        types = []
        data_type = data_file.get_type()
        if data_type:
            types.append(data_type)
            if data_type == Type.CSV and data_file.get_name().startswith("QCMetrics"):
                types.append(Type.WESQCREPORT)
        return types

    def _get_additional_properties(self, data_file, seq_folder_name):
        properties = {}
        if data_file.get_sample_id():
            properties[Property.SAMPLE_REFERENCE] = "{}/{}".format(seq_folder_name, data_file.get_sample_id())
        return properties


class RawDxUploader(DxUploaderBase):
    SEQ_FOLDER_TYPE = RawSeqFolder

    def _create_sentinel(self, seq_folder_name):
        return RawSentinel(self._api, self._context.get_base_dir(), seq_folder_name)

    def _get_additional_types(self, data_file):
        return []

    def _get_additional_properties(self, data_file, seq_folder_name):
        return {}


class BgiDxUploader(DxUploaderBase):
    SEQ_FOLDER_TYPE = BgiSeqFolder

    def _create_sentinel(self, seq_folder_name):
        return RawSentinel(self._api, self._context.get_base_dir(), seq_folder_name)

    def _get_additional_types(self, data_file):
        return []

    def _get_additional_properties(self, data_file, seq_folder_name):
        return {}


class SangerDxUploader(DxUploaderBase):
    SEQ_FOLDER_TYPE = SangerSeqFolder

    def _create_sentinel(self, seq_folder_name):
        return SangerSentinel(self._api, self._context.get_base_dir(), seq_folder_name)

    def _get_additional_types(self, data_file):
        return []

    def _get_additional_properties(self, data_file, seq_folder_name):
        return {}


class NgsDxUploader(DxUploaderBase):
    SEQ_FOLDER_TYPE = NgsSeqFolder

    def upload_file(self, data_file):
        data_file, file_id = super(NgsDxUploader, self).upload_file(data_file)

        logging.info("Removing uploaded tar file {}".format(data_file.get_full_path()))
        os.remove(data_file.get_full_path())

        return data_file, file_id

    def _create_sentinel(self, seq_folder_name):
        return NgsSentinel(self._api,
                           self._context.get_base_dir(),
                           seq_folder_name,
                           self._context.get_site_id(),
                           get_expected_time('NgsDxUploader', 'upload'))

    def _get_additional_types(self, data_file):
        return []

    def _get_additional_properties(self, data_file, seq_folder_name):
        return {}


class DxUploaderFactory(object):
    @staticmethod
    def create(context, api, seq_folder):
        # type: (Context, DxApi|ExodusApi, SeqFolderBase) -> DxUploaderBase

        if isinstance(seq_folder, BgiDxUploader.SEQ_FOLDER_TYPE):
            return BgiDxUploader(context, api)
        elif isinstance(seq_folder, RawDxUploader.SEQ_FOLDER_TYPE):
            return RawDxUploader(context, api)
        elif isinstance(seq_folder, WesSignateraDxUploader.SEQ_FOLDER_TYPE):
            return WesSignateraDxUploader(context, api)
        elif isinstance(seq_folder, PersonalisDxUploader.SEQ_FOLDER_TYPE):
            return PersonalisDxUploader(context, api)
        elif isinstance(seq_folder, SangerDxUploader.SEQ_FOLDER_TYPE):
            return SangerDxUploader(context, api)
        elif isinstance(seq_folder, NgsDxUploader.SEQ_FOLDER_TYPE):
            return NgsDxUploader(context, api)
        raise UploaderException(
            "Uploader for the folder {} was not found".format(seq_folder.get_name()))


class SeqFolderLogUploader:
    def __init__(self, logger, seq_folder_name, remote_storage, remote_base_dir):
        self._logger = logger
        self._remote_storage = remote_storage
        self._remote_base_dir = remote_base_dir
        self._seq_folder_name = seq_folder_name
        self._log_file_path = self._resolve_log_file_path(self._seq_folder_name)

        self._handler = logging.FileHandler(self._log_file_path)
        self._handler.setFormatter(logging.Formatter(LOGGER_FORMAT))

    def __enter__(self):
        self._logger.addHandler(self._handler)

    def __exit__(self, et, ev, tb):
        self._logger.removeHandler(self._handler)
        self._handler.close()

        self._upload_log_file()

    def _upload_log_file(self):
        if os.path.exists(self._log_file_path):
            remote_folder = os.path.join(self._remote_base_dir, self._seq_folder_name)
            tar_full_path = os.path.join(os.path.dirname(self._log_file_path), 'service.tar.gz')

            with tarfile.open(tar_full_path, 'w:gz') as t:
                t.add(self._log_file_path, arcname=os.path.basename(self._log_file_path))

            types = [Type.SERVICE]
            properties = {Property.RUN_FOLDER: self._seq_folder_name}
            tar_data_file = DataFile(os.path.dirname(tar_full_path), os.path.basename(tar_full_path), None)
            self._remote_storage.upload_file(tar_data_file, remote_folder, types, properties)

            if os.path.exists(tar_full_path):
                os.remove(tar_full_path)

            if os.path.exists(self._log_file_path):
                os.remove(self._log_file_path)

    def _resolve_log_file_path(self, seq_folder_name):
        log_file_path = '/tmp/{}/folder_upload.log'.format(seq_folder_name)
        path = os.path.dirname(log_file_path)

        try:
            os.makedirs(path)
        except OSError as exc:  # Python ≥ 2.5
            if exc.errno == errno.EEXIST and os.path.isdir(path):
                pass
            else:
                raise exc

        return log_file_path
