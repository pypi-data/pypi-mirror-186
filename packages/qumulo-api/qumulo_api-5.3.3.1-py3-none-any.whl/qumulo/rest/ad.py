# Copyright (c) 2013 Qumulo, Inc.
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


from typing import Optional

import qumulo.lib.request as request

from qumulo.lib.auth import Credentials
from qumulo.lib.uri import UriBuilder


@request.request
def list_ad(
    conninfo: request.Connection, _credentials: Optional[Credentials]
) -> request.RestResponse:
    method = 'GET'
    uri = '/v1/ad/status'

    return conninfo.send_request(method, uri)


@request.request
def poll_ad(
    conninfo: request.Connection, _credentials: Optional[Credentials]
) -> request.RestResponse:
    method = 'GET'
    uri = '/v1/ad/monitor'

    return conninfo.send_request(method, uri)


@request.request
def join_ad(
    conninfo: request.Connection,
    _credentials: Optional[Credentials],
    domain: object,
    username: object,
    password: object,
    ou: Optional[object] = None,
    domain_netbios: Optional[object] = None,
    enable_ldap: bool = False,
    base_dn: Optional[object] = None,
) -> request.RestResponse:
    method = 'POST'
    uri = '/v1/ad/join'

    if ou is None:
        ou = ''
    if domain_netbios is None:
        domain_netbios = ''
    if base_dn is None:
        base_dn = ''

    config = {
        'domain': str(domain),
        'domain_netbios': str(domain_netbios),
        'user': str(username),
        'password': str(password),
        'ou': str(ou),
        'use_ad_posix_attributes': enable_ldap,
        'base_dn': str(base_dn),
    }

    return conninfo.send_request(method, uri, body=config)


@request.request
def reconfigure_ad(
    conninfo: request.Connection,
    _credentials: Optional[Credentials],
    enable_ldap: bool,
    base_dn: str,
) -> request.RestResponse:
    method = 'POST'
    uri = '/v1/ad/reconfigure'

    config = {'use_ad_posix_attributes': enable_ldap, 'base_dn': base_dn}

    return conninfo.send_request(method, uri, body=config)


@request.request
def leave_ad(
    conninfo: request.Connection,
    _credentials: Optional[Credentials],
    domain: object,
    username: object,
    password: object,
) -> request.RestResponse:
    method = 'POST'
    uri = '/v1/ad/leave'

    # XXX scott: support none for these in the api, also, don't call domain
    # assistant script in that case
    if username is None:
        username = ''
    if password is None:
        password = ''

    config = {'domain': str(domain), 'user': str(username), 'password': str(password)}

    return conninfo.send_request(method, uri, body=config)


@request.request
def cancel_ad(
    conninfo: request.Connection, _credentials: Optional[Credentials]
) -> request.RestResponse:
    method = 'POST'
    uri = '/v1/ad/cancel'

    return conninfo.send_request(method, uri)


@request.request
def uid_to_sid_get(
    conninfo: request.Connection, _credentials: Optional[Credentials], uid: object
) -> request.RestResponse:
    method = 'GET'
    uri = '/v1/ad/uids/' + str(uid) + '/sids/'

    return conninfo.send_request(method, uri)


@request.request
def username_to_sid_get(
    conninfo: request.Connection, _credentials: Optional[Credentials], name: object
) -> request.RestResponse:
    return conninfo.send_request('GET', f'/v1/ad/usernames/{name}/sids/')


@request.request
def name_to_ad_accounts(
    conninfo: request.Connection, _credentials: Optional[Credentials], name: object
) -> request.RestResponse:
    uri = UriBuilder(path='/v1/ad/usernames')
    uri.add_path_component(str(name))
    uri.add_path_component('objects')
    uri.append_slash()
    return conninfo.send_request('GET', str(uri))


@request.request
def sid_to_uid_get(
    conninfo: request.Connection, _credentials: Optional[Credentials], sid: str
) -> request.RestResponse:
    method = 'GET'
    uri = '/v1/ad/sids/' + sid + '/uid'

    return conninfo.send_request(method, uri)


@request.request
def sid_to_username_get(
    conninfo: request.Connection, _credentials: Optional[Credentials], sid: object
) -> request.RestResponse:
    return conninfo.send_request('GET', f'/v1/ad/sids/{sid}/username')


@request.request
def sid_to_gid_get(
    conninfo: request.Connection, _credentials: Optional[Credentials], sid: str
) -> request.RestResponse:
    method = 'GET'
    uri = '/v1/ad/sids/' + sid + '/gid'

    return conninfo.send_request(method, uri)


@request.request
def sid_to_ad_account(
    conninfo: request.Connection, _credentials: Optional[Credentials], sid: str
) -> request.RestResponse:
    return conninfo.send_request('GET', '/v1/ad/sids/' + sid + '/object')


@request.request
def gid_to_sid_get(
    conninfo: request.Connection, _credentials: Optional[Credentials], gid: object
) -> request.RestResponse:
    method = 'GET'
    uri = '/v1/ad/gids/' + str(gid) + '/sids/'

    return conninfo.send_request(method, uri)


@request.request
def sid_to_expanded_group_sids_get(
    conninfo: request.Connection, _credentials: Optional[Credentials], sid: str
) -> request.RestResponse:
    method = 'GET'
    uri = '/v1/ad/sids/' + sid + '/expanded-groups/'

    return conninfo.send_request(method, uri)


@request.request
def clear_cache_post(
    conninfo: request.Connection, _credentials: Optional[Credentials]
) -> request.RestResponse:
    method = 'POST'
    uri = '/v1/ad/clear-cache'

    return conninfo.send_request(method, uri)


@request.request
def distinguished_name_to_ad_account(
    conninfo: request.Connection, _credentials: Optional[Credentials], distinguished_name: object
) -> request.RestResponse:
    uri = UriBuilder(path='/v1/ad/distinguished-names/')
    uri.add_path_component(str(distinguished_name))
    uri.add_path_component('object')
    return conninfo.send_request('GET', str(uri))


@request.request
def get_advanced_settings(
    conninfo: request.Connection, _credentials: Optional[Credentials]
) -> request.RestResponse:
    method = 'GET'
    uri = '/v1/ad/settings'
    return conninfo.send_request(method, uri)


# Values for the advanced AD setting controlling DCERPC signing.
VALID_SIGNING_CHOICES = ('NO_SIGNING', 'WANT_SIGNING', 'REQUIRE_SIGNING')

# Values for the advanced AD setting controlling DCERPC sealing.
VALID_SEALING_CHOICES = ('NO_SEALING', 'WANT_SEALING', 'REQUIRE_SEALING')

# Values for the advanced AD setting controlling DCERPC encryption.
VALID_ENCRYPTION_CHOICES = ('NO_AES', 'WANT_AES', 'REQUIRE_AES')


@request.request
def set_advanced_settings(
    conninfo: request.Connection,
    _credentials: Optional[Credentials],
    signing: object,
    sealing: object,
    crypto: object,
    if_match: Optional[str] = None,
) -> request.RestResponse:
    """
    This method controls advanced Active Directory settings.

    @param signing  Configure DCERPC signing to be off, prefer signing, or require
                    signing. Must be one of NO_SIGNING, WANT_SIGNING, or REQUIRE_SIGNING

    @param sealing  Configure DCERPC sealing to be off, prefer sealing, or require
                    sealing. Must be one of NO_SEALING, WANT_SEALING, or REQUIRE_SEALING

    @param crypto   Configure DCERPC to not use encryption, prefer AES encryption,
                    or require AES encryption. Must be one of NO_AES, WANT_AES, or
                    REQUIRE_AES
    """
    method = 'PUT'
    uri = '/v1/ad/settings'
    body = {'signing': str(signing), 'sealing': str(sealing), 'crypto': str(crypto)}

    return conninfo.send_request(method, uri, body=body, if_match=if_match)
