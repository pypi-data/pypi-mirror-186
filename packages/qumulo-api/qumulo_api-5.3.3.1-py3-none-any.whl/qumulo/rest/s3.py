# Copyright (c) 2022 Qumulo, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.

from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from dataclasses_json import DataClassJsonMixin

import qumulo.lib.request as request

from qumulo.lib.identity_util import ApiIdentity, Identity
from qumulo.lib.rest_util import dataclass_to_dict_omit_none_fields
from qumulo.lib.uri import UriBuilder

S3_ACCESS_KEYS_URI = '/v1/s3/access-keys/'
S3_SETTINGS_URI = '/v1/s3/settings'
S3_BUCKETS_URI = '/v1/s3/buckets/'
S3_BUCKETS_DELETE_URI = S3_BUCKETS_URI + '{}?delete-root-dir={}'
S3_BUCKETS_MODIFY_URI = S3_BUCKETS_URI + '{}'


@dataclass
class Config(DataClassJsonMixin):
    enabled: bool
    base_path: str


@dataclass
class ConfigPatch:
    enabled: Optional[bool] = None
    base_path: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return dataclass_to_dict_omit_none_fields(self)


@dataclass
class AccessKeyDescription:
    access_key_id: str
    owner: ApiIdentity
    creation_time: str

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'AccessKeyDescription':
        return AccessKeyDescription(
            access_key_id=data['access_key_id'],
            owner=data['owner'],
            creation_time=data['creation_time'],
        )


@dataclass
class AccessKeyDescriptionListPaginationToken(DataClassJsonMixin):
    next: Optional[str]


@dataclass
class AccessKeyDescriptionList:
    entries: List[AccessKeyDescription]
    paging: AccessKeyDescriptionListPaginationToken

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'AccessKeyDescriptionList':
        return AccessKeyDescriptionList(
            entries=[AccessKeyDescription.from_dict(entry) for entry in data['entries']],
            paging=AccessKeyDescriptionListPaginationToken.from_dict(data['paging']),
        )


@dataclass
class CreatedAccessKey:
    access_key_id: str
    owner: ApiIdentity
    secret_access_key: str
    creation_time: str

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'CreatedAccessKey':
        return CreatedAccessKey(
            access_key_id=data['access_key_id'],
            owner=data['owner'],
            secret_access_key=data['secret_access_key'],
            creation_time=data['creation_time'],
        )


@dataclass
class BucketDescription:
    name: str
    creation_time: str
    path: str
    anonymous_access_enabled: bool

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'BucketDescription':
        return BucketDescription(
            name=data['name'],
            creation_time=data['creation_time'],
            path=data['path'],
            anonymous_access_enabled=data['anonymous_access_enabled'],
        )

    def __hash__(self) -> int:
        return hash(repr(self))


@dataclass
class BucketDescriptionList:
    buckets: List[BucketDescription]

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'BucketDescriptionList':
        return BucketDescriptionList(
            buckets=[BucketDescription.from_dict(bucket) for bucket in data['buckets']]
        )


@dataclass
class BucketPatch:
    anonymous_access_enabled: Optional[bool] = None

    def to_dict(self) -> Dict[str, Any]:
        return dataclass_to_dict_omit_none_fields(self)


class S3:
    def __init__(self, client: request.SendRequestObject):
        self.client = client

    def get_settings(self) -> Config:
        response = self.client.send_request('GET', S3_SETTINGS_URI)
        return Config.schema().load(response.data, unknown='EXCLUDE')

    def modify_settings(self, config: ConfigPatch) -> Config:
        response = self.client.send_request('PATCH', S3_SETTINGS_URI, body=config.to_dict())
        assert response.etag is None
        return Config.schema().load(response.data, unknown='EXCLUDE')

    def list_access_keys(
        self, limit: Optional[int] = None, start_at: Optional[str] = None
    ) -> AccessKeyDescriptionList:
        uri = UriBuilder(path=S3_ACCESS_KEYS_URI, rstrip_slash=False)

        if limit is not None:
            uri.add_query_param('limit', limit)

        if start_at is not None:
            uri.add_query_param('after', start_at)

        response = self.client.send_request('GET', str(uri))
        assert response.etag is None

        access_key_list = AccessKeyDescriptionList.from_dict(response.data)
        if access_key_list.paging.next is not None:
            # Extract the continuation token from the next URI. This way callers don't have to know
            # about the actual format.
            next_uri = access_key_list.paging.next
            start = next_uri.find('after=') + len('after=')
            end = next_uri.find('&', start)
            if end == -1:
                access_key_list.paging.next = next_uri[start:]
            else:
                access_key_list.paging.next = next_uri[start:end]

        return access_key_list

    def create_access_key(self, user: Identity) -> CreatedAccessKey:
        req = {'user': user.dictionary()}
        response = self.client.send_request('POST', S3_ACCESS_KEYS_URI, body=req)
        assert response.etag is None
        return CreatedAccessKey.from_dict(response.data)

    def delete_access_key(self, access_key_id: str) -> None:
        response = self.client.send_request('DELETE', S3_ACCESS_KEYS_URI + access_key_id)
        assert response.etag is None

    # The path used as the bucket root, if specified in the path parameter, must be an absolute
    # path.
    def create_bucket(self, name: str, path: Optional[str] = None) -> BucketDescription:
        req = {'name': name, 'path': path}
        response = self.client.send_request('POST', S3_BUCKETS_URI, body=req)
        assert response.etag is None
        return BucketDescription.from_dict(response.data)

    def list_buckets(self) -> BucketDescriptionList:
        response = self.client.send_request('GET', S3_BUCKETS_URI)
        assert response.etag is None
        return BucketDescriptionList.from_dict(response.data)

    def delete_bucket(self, name: str, delete_root_dir: bool) -> None:
        response = self.client.send_request(
            'DELETE', S3_BUCKETS_DELETE_URI.format(name, str(delete_root_dir).lower())
        )
        assert response.etag is None
        assert response.data is None

    def modify_bucket(self, name: str, patch: BucketPatch) -> BucketDescription:
        response = self.client.send_request(
            'PATCH', S3_BUCKETS_MODIFY_URI.format(name), body=patch.to_dict()
        )
        assert response.etag is None
        return BucketDescription.from_dict(response.data)
