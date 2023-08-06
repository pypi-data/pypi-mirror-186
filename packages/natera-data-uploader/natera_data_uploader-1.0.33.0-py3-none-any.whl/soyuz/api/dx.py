import logging

import dxpy

from soyuz.configuration import Settings
from soyuz.utils import UploaderException


class DxApi(object):
    def __init__(self, token):
        # type: (str) -> None
        dxpy.set_security_context({'auth_token_type': 'Bearer', 'auth_token': token})

        self.__project_id = self.__resolve_project_id()
        dxpy.set_project_context(self.__project_id)
        dxpy.set_workspace_id(self.__project_id)

    def get_current_project_id(self):
        return self.__project_id

    def get_project(self, project_id):
        return dxpy.DXProject(project_id)

    def get_record(self, record_id):
        return dxpy.DXRecord(record_id)

    def get_job(self, job_id):
        return dxpy.DXJob(job_id)

    def get_file(self, file_id):
        return dxpy.DXFile(file_id)

    def upload_local_file(self, filename=None, file=None, media_type=None, keep_open=False,
                          wait_on_close=False, use_existing_dxfile=None, show_progress=False,
                          write_buffer_size=None, multithread=True, **kwargs):
        return dxpy.upload_local_file(filename=filename, file=file, media_type=media_type, keep_open=keep_open,
                                      wait_on_close=wait_on_close, use_existing_dxfile=use_existing_dxfile,
                                      show_progress=show_progress, write_buffer_size=write_buffer_size,
                                      multithread=multithread, **kwargs)

    def find_projects(self, name=None, name_mode='exact', properties=None, tags=None,
                      level=None, describe=False, explicit_perms=None, region=None,
                      public=None, created_after=None, created_before=None, billed_to=None,
                      limit=None, return_handler=False, first_page_size=100, containsPHI=None, **kwargs):
        return list(dxpy.bindings.search.find_projects(
            name=name, name_mode=name_mode, properties=properties, tags=tags,
            level=level, describe=describe, explicit_perms=explicit_perms, region=region,
            public=public, created_after=created_after, created_before=created_before, billed_to=billed_to,
            limit=limit, return_handler=return_handler, first_page_size=first_page_size, containsPHI=containsPHI,
            **kwargs
        ))

    def find_executions(self, classname=None, launched_by=None, executable=None, project=None,
                        state=None, origin_job=None, parent_job=None, no_parent_job=False,
                        parent_analysis=None, no_parent_analysis=False, root_execution=None,
                        created_after=None, created_before=None, describe=False,
                        name=None, name_mode="exact", tags=None, properties=None, limit=None,
                        first_page_size=100, return_handler=False, include_subjobs=True,
                        **kwargs):
        return list(dxpy.find_executions(
            classname=classname, launched_by=launched_by, executable=executable, project=project,
            state=state, origin_job=origin_job, parent_job=parent_job, no_parent_job=no_parent_job,
            parent_analysis=parent_analysis, no_parent_analysis=no_parent_analysis,
            root_execution=root_execution, created_after=created_after, created_before=created_before,
            describe=describe, name=name, name_mode=name_mode, tags=tags, properties=properties, limit=limit,
            first_page_size=first_page_size, return_handler=return_handler, include_subjobs=include_subjobs,
            **kwargs))

    def find_data_objects(self, classname=None, state=None, visibility=None,
                          name=None, name_mode='exact', properties=None,
                          typename=None, tag=None, tags=None,
                          link=None, project=None, folder=None, recurse=None,
                          modified_after=None, modified_before=None,
                          created_after=None, created_before=None,
                          describe=False, limit=None, level=None, region=None,
                          return_handler=False, first_page_size=100,
                          **kwargs):
        return list(dxpy.bindings.find_data_objects(
            classname=classname, state=state, visibility=visibility, name=name, name_mode=name_mode,
            properties=properties, typename=typename, tag=tag, tags=tags, link=link, project=project, folder=folder,
            recurse=recurse, modified_after=modified_after, modified_before=modified_before,
            created_after=created_after, created_before=created_before, describe=describe, limit=limit, level=level,
            region=region, return_handler=return_handler, first_page_size=first_page_size, **kwargs))

    def create_record(self, details=None, **kwargs):
        return dxpy.new_dxrecord(details=details, **kwargs)

    def load_settings_from_dnanexus_profile(self):
        # type: () -> Settings
        external_profiles = self.find_data_objects(classname="record",
                                                   project=self.__project_id,
                                                   folder='/profile/sequencingUpload/',
                                                   name='config', recurse=False, return_handler=True)

        if len(external_profiles) > 1:
            logging.warning("More than 1 settings profile exists in /profile/sequencingUpload/ folder, skipping...")
        elif len(external_profiles) == 0:
            return Settings(settings_dict={})

        if len(external_profiles) == 1:
            logging.info("Found a settings profile in /profile/sequencingUpload/ folder, loading...")

            return Settings(settings_dict=external_profiles[0].describe(incl_details=True)['details'])

    def __resolve_project_id(self):
        # type: () -> str

        try:
            projects = list(self.find_projects(level='UPLOAD'))

            if len(projects) == 0 or len(projects) > 1:
                raise UploaderException("Auth Token must have access to exactly 1 project with UPLOAD permission.")

            return projects[0]['id']
        except dxpy.exceptions.InvalidAuthentication:
            raise UploaderException("Authorization token is invalid or expired")
