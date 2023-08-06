import os

import requests

from soyuz.utils import read_in_chunks


class ExodusApi(object):
    def __init__(self, exodus_url, exodus_username, exodus_password, chunk_size, exodus_aws_access_key_id,
                 exodus_aws_secret_access_key, exodus_s3_bucket_name, exodus_aws_region, exodus_sample_source):
        self._base_headers = {}
        self._exodus_url = exodus_url
        self._exodus_username = exodus_username
        self._exodus_password = exodus_password
        self._chunk_size = chunk_size

        if exodus_aws_access_key_id:
            self._base_headers['X-AWS_ACCESS_KEY_ID'] = exodus_aws_access_key_id

        if exodus_aws_secret_access_key:
            self._base_headers['X-AWS_SECRET_ACCESS_KEY'] = exodus_aws_secret_access_key

        if exodus_s3_bucket_name:
            self._base_headers['X-AWS_S3_BUCKET_NAME'] = exodus_s3_bucket_name

        if exodus_aws_region:
            self._base_headers['X-AWS_DEFAULT_REGION'] = exodus_aws_region

        if exodus_sample_source:
            self._base_headers['X-SAMPLE_SOURCE'] = exodus_sample_source

    def create_record(self, name, folder, types, properties, tags, details):
        data = {'name': name,
                'folder': folder,
                'types': types,
                'properties': properties,
                'tags': tags,
                'details': details
                }

        response = requests.post(os.path.join(self._exodus_url, "2.0/data/records/new"),
                                 json=data,
                                 auth=(self._exodus_username, self._exodus_password),
                                 headers=self._base_headers)

        response.raise_for_status()

        return response.json()

    def upload_local_file(self, file_full_path, name, folder, types, properties, tags):
        new_file_data = {'name': name, 'folder': folder, 'types': types, 'properties': properties, 'tags': tags}
        new_file_response = requests.post(os.path.join(self._exodus_url, "2.0/data/files/new"),
                                          json=new_file_data,
                                          auth=(self._exodus_username, self._exodus_password),
                                          headers=self._base_headers)
        new_file_response.raise_for_status()
        new_file_response = new_file_response.json()
        file_id = new_file_response['file']['link']
        upload_id = new_file_response['uploadId']

        with open(file_full_path, 'rb') as file_object:
            parts = []
            for i, chunk in enumerate(read_in_chunks(file_object, self._chunk_size)):
                part_upload_response = requests.post(os.path.join(self._exodus_url, "2.0/data/files/part-upload"),
                                                     json={'file': {'link': file_id}, 'uploadId': upload_id,
                                                           'part': i + 1},
                                                     auth=(self._exodus_username, self._exodus_password),
                                                     headers=self._base_headers)
                part_upload_response.raise_for_status()

                upload_url = part_upload_response.json()['uploadUrl']
                upload_response = requests.put(upload_url, data=chunk, headers=self._base_headers)
                upload_response.raise_for_status()

                parts.append({'eTag': upload_response.headers['ETag'], 'part': i + 1})

        finish_upload_response = requests.post(os.path.join(self._exodus_url, "2.0/data/files/finish-upload"),
                                               json={'file': {'link': file_id},
                                                     'uploadId': upload_id,
                                                     'contentLength': os.path.getsize(file_full_path),
                                                     'parts': parts},
                                               auth=(self._exodus_username, self._exodus_password),
                                               headers=self._base_headers)
        finish_upload_response.raise_for_status()

        return finish_upload_response.json()
