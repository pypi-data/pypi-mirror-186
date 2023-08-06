#!/usr/bin/env python

import logging

from soyuz.api.dx import DxApi
from soyuz.api.exodus import ExodusApi
from soyuz.configuration import Parameters
from soyuz.configuration import Settings
from soyuz.constellation.api import ConstellationApi
from soyuz.constellation.job_manager import UploadJobManager, UploadJobWatcher
from soyuz.data.daemons import Daemon
from soyuz.data.folders import WesSignateraSeqFolder, BgiSeqFolder, RawSeqFolder, PersonalisSeqFolder, WatchDirectory, \
    SangerSeqFolder, NgsSeqFolder
from soyuz.data.storages import StorageType
from soyuz.dx.context import Context
from soyuz.dx.uploaders import WesSignateraDxUploader, BgiDxUploader, RawDxUploader, PersonalisDxUploader, \
    WatchUploader, SangerDxUploader, NgsDxUploader
from soyuz.heartbeat import Heartbeat
from soyuz.utils import UploaderException, Logging
from soyuz.watchdog import SequenceFolderWatchDog


def execute(params, settings, context=None, api=None, constellation_api=None):
    if params.get_action() in [Parameters.UPLOAD_ACTION, Parameters.WATCH_ACTION]:
        folder = None
        uploader = None

        if params.is_with_upload_job() or params.is_constellation_portal_mode():
            if not context.get_constellation_url():
                raise UploaderException('Constellation API URL was not specified')

            UploadJobManager(constellation_api,
                             UploadJobWatcher(context, api, constellation_api,
                                              context.get_upload_jobs_check_interval()),
                             params.is_constellation_portal_mode()).start_watcher()

        SequenceFolderWatchDog(params.get_folder(),
                               params.get_watch_dog_check_interval(),
                               params.get_watch_dog_timeout()).start()

        if params.is_with_heartbeat():
            if not context.get_soyuz_id():
                raise UploaderException("--with-heartbeat requires Soyuz ID")
            elif context.get_storage() != StorageType.DNANEXUS:
                raise UploaderException("--with-heartbeat works only with DNANexus storage")
            else:
                Heartbeat(api, context.get_soyuz_id(), context.get_heartbeat_record_update_interval()).start()

        if params.get_action() == Parameters.UPLOAD_ACTION:
            if params.get_upload_type() == Parameters.WES_SIGNATERA_UPLOAD:
                uploader = WesSignateraDxUploader(context, api)
                folder = WesSignateraSeqFolder(params.get_folder())
            elif params.get_upload_type() == Parameters.BGI_UPLOAD:
                uploader = BgiDxUploader(context, api)
                folder = BgiSeqFolder(params.get_folder())
            elif params.get_upload_type() == Parameters.RAW_UPLOAD:
                uploader = RawDxUploader(context, api)
                folder = RawSeqFolder(params.get_folder())
            elif params.get_upload_type() == Parameters.PERSONALIS_UPLOAD:
                uploader = PersonalisDxUploader(context, api)
                folder = PersonalisSeqFolder(params.get_folder())
            elif params.get_upload_type() == Parameters.SANGER_UPLOAD:
                uploader = SangerDxUploader(context, api)
                folder = SangerSeqFolder(params.get_folder(), context.get_sanger_check_interval())
            elif params.get_upload_type() == Parameters.NGS_UPLOAD:
                uploader = NgsDxUploader(context, api)
                folder = NgsSeqFolder(params.get_folder(),
                                      context.get_ngs_completion_marker(),
                                      context.get_ngs_check_interval(),
                                      context.get_ngs_file_age_time(),
                                      context.get_ngs_archive_temp_folder())

            if not folder or not uploader:
                raise UploaderException("Incorrect upload type")

            if not folder.is_valid:
                raise UploaderException("Data folder is not in a valid state")

            uploader.upload(folder)

        elif params.get_action() == Parameters.WATCH_ACTION:
            uploader = WatchUploader(context, api)

            if params.get_watch_type() == Parameters.START_WATCH:
                if params.foreground():
                    uploader.watch(WatchDirectory(context, params.get_folder()))
                else:
                    Daemon(uploader.watch, WatchDirectory(context, params.get_folder())).start()
            elif params.get_watch_type() == Parameters.STOP_WATCH:
                Daemon().stop()
            elif params.get_watch_type() == Parameters.STATUS_WATCH:
                Daemon().status()

    elif params.get_action() == Parameters.CONFIG_ACTION:
        if params.get_config_action() == Parameters.GET_CONFIG:
            if params.get_config_parameter_key() == "storage":
                logging.info(settings.get_storage())
            elif params.get_config_parameter_key() == "token":
                logging.info(settings.get_token())
            elif params.get_config_parameter_key() == "stella_url":
                logging.info(settings.get_exodus_url())
            elif params.get_config_parameter_key() == "constellation_url":
                logging.info(settings.get_constellation_url())
            elif params.get_config_parameter_key() == "basedir":
                logging.info(settings.get_base_dir())
            elif params.get_config_parameter_key() == "interval":
                logging.info(settings.get_interval())
            elif params.get_config_parameter_key() == "ua_path":
                logging.info(settings.get_ua_path())
            elif params.get_config_parameter_key() == "ua_parameters":
                logging.info(settings.get_ua_parameters())
            elif params.get_config_parameter_key() == "process_count":
                logging.info(settings.get_process_count())
            elif params.get_config_parameter_key() == "chunk_size":
                logging.info(settings.get_chunk_size())
            elif params.get_config_parameter_key() == "jwt_token":
                logging.info(settings.get_jwt_token())
            elif params.get_config_parameter_key() == "jwt_token_public_key_path":
                logging.info(settings.get_jwt_token_public_key_path())
            elif params.get_config_parameter_key() == "constellation_url":
                logging.info(settings.get_constellation_url())

        elif params.get_config_action() == Parameters.SET_CONFIG:
            if params.get_config_parameter_key() == "storage":
                settings.set_storage(params.get_config_parameter_value())
            elif params.get_config_parameter_key() == "token":
                settings.set_token(params.get_config_parameter_value())
            elif params.get_config_parameter_key() == "stella_url":
                settings.set_exodus_url(params.get_config_parameter_value())
            elif params.get_config_parameter_key() == "stella_username":
                settings.set_exodus_username(params.get_config_parameter_value())
            elif params.get_config_parameter_key() == "stella_password":
                settings.set_exodus_password(params.get_config_parameter_value())
            elif params.get_config_parameter_key() == "stella_aws_access_key_id":
                settings.set_exodus_aws_access_key_id(params.get_config_parameter_value())
            elif params.get_config_parameter_key() == "stella_aws_secret_access_key":
                settings.set_exodus_aws_secret_access_key(params.get_config_parameter_value())
            elif params.get_config_parameter_key() == "stella_s3_bucket_name":
                settings.set_exodus_s3_bucket_name(params.get_config_parameter_value())
            elif params.get_config_parameter_key() == "stella_aws_region":
                settings.set_exodus_aws_region(params.get_config_parameter_value())
            elif params.get_config_parameter_key() == "stella_sample_source":
                settings.set_exodus_sample_source(params.get_config_parameter_value())
            elif params.get_config_parameter_key() == "constellation_url":
                settings.set_constellation_url(params.get_config_parameter_value())
            elif params.get_config_parameter_key() == "basedir":
                settings.set_basedir(params.get_config_parameter_value())
            elif params.get_config_parameter_key() == "interval":
                settings.set_interval(params.get_config_parameter_value())
            elif params.get_config_parameter_key() == "ua_path":
                settings.set_ua_path(params.get_config_parameter_value())
            elif params.get_config_parameter_key() == "ua_parameters":
                settings.set_ua_parameters(params.get_config_parameter_value())
            elif params.get_config_parameter_key() == "process_count":
                settings.set_process_count(params.get_config_parameter_value())
            elif params.get_config_parameter_key() == "chunk_size":
                settings.set_chunk_size(params.get_config_parameter_value())
            elif params.get_config_parameter_key() == "jwt_token":
                settings.set_jwt_token(params.get_config_parameter_value())
            elif params.get_config_parameter_key() == "jwt_token_public_key_path":
                settings.set_jwt_token_public_key_path(params.get_config_parameter_value())
            elif params.get_config_parameter_key() == "constellation_url":
                settings.set_constellation_url(params.get_config_parameter_value())
            elif params.get_config_parameter_key() == "soyuz_id":
                settings.set_soyuz_id(params.get_config_parameter_value())
            elif params.get_config_parameter_key() == "heartbeat_record_update_interval":
                settings.set_heartbeat_record_update_interval(params.get_config_parameter_value())
            else:
                raise UploaderException("There is no parameter '{}'".format(params.get_config_parameter_key()))
            settings.dump()
            logging.info("Set {} to {}".format(params.get_config_parameter_key(), params.get_config_parameter_value()))


def main(_params=None, _settings=None):
    try:
        params = _params if _params else Parameters()
        settings = _settings if _settings else Settings(full_path_to_settings_file=params.get_setting_file_path())
        Logging().initialize()

        if params.get_action() == Parameters.CONFIG_ACTION:
            execute(params, settings)
        else:
            api = None
            constellation_api = None
            context = Context(params, settings)

            if context.get_storage() == StorageType.DNANEXUS:
                api = DxApi(context.get_token())
                context.set_settings_from_dnanexus_profile(api.load_settings_from_dnanexus_profile())
                constellation_api = ConstellationApi(context.get_token(), context.get_constellation_url())
                context.set_project_id(api.get_current_project_id())
            elif context.get_storage() == StorageType.EXODUS:
                api = ExodusApi(exodus_url=context.get_exodus_url(),
                                exodus_username=context.get_exodus_username(),
                                exodus_password=context.get_exodus_password(),
                                chunk_size=context.get_chunk_size(),
                                exodus_aws_access_key_id=context.get_exodus_aws_access_key_id(),
                                exodus_aws_secret_access_key=context.get_exodus_aws_secret_access_key(),
                                exodus_s3_bucket_name=context.get_exodus_s3_bucket_name(),
                                exodus_aws_region=context.get_exodus_aws_region(),
                                exodus_sample_source=context.get_exodus_sample_source())

            execute(params, settings, context, api, constellation_api)
    except Exception as e:
        logging.error(e, exc_info=True)
        quit(1)


if __name__ == "__main__":
    main()
