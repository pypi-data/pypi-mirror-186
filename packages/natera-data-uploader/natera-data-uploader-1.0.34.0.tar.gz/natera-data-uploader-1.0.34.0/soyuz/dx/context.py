import dxpy

from soyuz.configuration import Parameters
from soyuz.configuration import Settings
from soyuz.data.storages import StorageType
from soyuz.utils import UploaderException, parse_and_validate_jwt_token


class Context(object):
    def __init__(self, params, settings):
        # type: (Parameters, Settings) -> None

        self.__params = params
        self.__settings = settings
        self.__settings_from_dnanexus_profile = settings

        self.__project_id = None
        self.__dnanexus_token = None

        if self.__settings.get_storage() == StorageType.DNANEXUS:
            self.__dnanexus_token = self.__resolve_dnanexus_token()
            if not self.__dnanexus_token:
                raise UploaderException("Token was not specified")

    def set_settings_from_dnanexus_profile(self, settings):
        # type: (Settings) -> None

        self.__settings_from_dnanexus_profile = settings

    def set_project_id(self, project_id):
        # type: (str) -> None
        self.__project_id = project_id

    def get_project_id(self):
        # type: () -> str
        return self.__project_id

    def get_token(self):
        # type: () -> str

        return self.__dnanexus_token

    def get_interval(self):
        # type: () -> float

        return self.__params.get_interval() or self.__settings_from_dnanexus_profile.get_interval() or self.__settings.get_interval()

    def is_force_upload(self):
        # type: () -> bool

        return self.__params.is_force_upload()

    def is_constellation_portal_mode(self):
        # type: () -> bool

        return self.__params.is_constellation_portal_mode()

    def get_upload_jobs_check_interval(self):
        # type: () -> float

        return self.__params.get_upload_jobs_check_interval()

    def get_site_id(self):
        # type: () -> str

        return self.__params.get_site_id()

    def get_ngs_completion_marker(self):
        # type: () -> str

        return self.__params.get_ngs_completion_marker()

    def get_ngs_check_interval(self):
        # type: () -> float

        return self.__params.get_ngs_check_interval()

    def get_ngs_file_age_time(self):
        # type: () -> float

        return self.__params.get_ngs_file_age_time()

    def get_ngs_archive_temp_folder(self):
        # type: () -> str

        return self.__params.get_ngs_archive_temp_folder()

    def get_sanger_check_interval(self):
        # type: () -> float

        return self.__params.get_sanger_check_interval()

    def get_base_dir(self):
        # type: () -> str

        return self.__settings_from_dnanexus_profile.get_base_dir() or self.__settings.get_base_dir() or '/data/seq'

    def get_storage(self):
        # type: () -> str

        return self.__settings.get_storage()

    def get_exodus_url(self):
        # type: () -> str

        return self.__settings_from_dnanexus_profile.get_exodus_url() or self.__settings.get_exodus_url()

    def get_exodus_username(self):
        # type: () -> str

        return self.__settings_from_dnanexus_profile.get_exodus_username() or self.__settings.get_exodus_username()

    def get_exodus_password(self):
        # type: () -> str

        return self.__settings_from_dnanexus_profile.get_exodus_password() or self.__settings.get_exodus_password()

    def get_exodus_aws_access_key_id(self):
        # type: () -> str

        return self.__settings_from_dnanexus_profile.get_exodus_aws_access_key_id() or self.__settings.get_exodus_aws_access_key_id()

    def get_exodus_aws_secret_access_key(self):
        # type: () -> str

        return self.__settings_from_dnanexus_profile.get_exodus_aws_secret_access_key() or self.__settings.get_exodus_aws_secret_access_key()

    def get_exodus_s3_bucket_name(self):
        # type: () -> str

        return self.__settings_from_dnanexus_profile.get_exodus_s3_bucket_name() or self.__settings.get_exodus_s3_bucket_name()

    def get_exodus_aws_region(self):
        # type: () -> str

        return self.__settings_from_dnanexus_profile.get_exodus_aws_region() or self.__settings.get_exodus_aws_region()

    def get_exodus_sample_source(self):
        # type: () -> str

        return self.__settings_from_dnanexus_profile.get_exodus_sample_source() or self.__settings.get_exodus_sample_source()

    def get_constellation_url(self):
        # type: () -> str

        return self.__settings_from_dnanexus_profile.get_constellation_url() or self.__settings.get_constellation_url()

    def get_ua_path(self):
        # type: () -> str

        return self.__settings_from_dnanexus_profile.get_ua_path() or self.__settings.get_ua_path()

    def get_ua_parameters(self):
        # type: () -> str

        return self.__settings_from_dnanexus_profile.get_ua_parameters() or self.__settings.get_ua_parameters()

    def get_chunk_size(self):
        # type: () -> int

        return self.__settings_from_dnanexus_profile.get_chunk_size() or self.__settings.get_chunk_size()

    def get_process_count(self):
        # type: () -> int

        return self.__settings_from_dnanexus_profile.get_process_count() or self.__settings.get_process_count()

    def get_soyuz_id(self):
        # type: () -> str

        return self.__settings_from_dnanexus_profile.get_soyuz_id() or self.__settings.get_soyuz_id() \
               or self.__params.get_soyuz_id()

    def get_heartbeat_record_update_interval(self):
        # type: () -> str

        return self.__settings_from_dnanexus_profile.get_heartbeat_record_update_interval() \
               or self.__settings.get_heartbeat_record_update_interval() \
               or self.__params.get_heartbeat_record_update_interval()

    def __resolve_dnanexus_token(self):
        # type: () -> str

        if self.__params.get_jwt_token() or self.__settings.get_jwt_token():
            jwt_token = self.__params.get_jwt_token() or self.__settings.get_jwt_token()
            public_key_path = self.__params.get_jwt_token_public_key_path() or self.__settings.get_jwt_token_public_key_path()

            if not public_key_path:
                raise UploaderException('Please provide correct path to JWT token public key')

            return parse_and_validate_jwt_token(jwt_token, public_key_path)['soyuzUploadToken']
        else:
            return self.__params.get_token() or self.__settings.get_token()

