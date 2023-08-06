#!/usr/bin/env python
# Copyright (c) 2022 Radware LTD.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# @author: Leon Meguira, Radware


from radware.sdk.common import RadwareParametersStruct, PasswordArgument
from radware.alteon.sdk.alteon_configurator import MSG_UPDATE, MSG_DELETE, AlteonConfigurator
from radware.alteon.beans.Layer7NewCfgContentClassCookieTable import *
from typing import Optional, ClassVar, Dict
from radware.alteon.exceptions import AlteonRequestError
from radware.alteon.sdk.alteon_managment import AlteonMngInfo
from radware.sdk.exceptions import DeviceConfiguratorError


class L7ContentClassCookieParameters(RadwareParametersStruct):
    content_class_id: str
    cookie_id: str
    cookie_key: Optional[str]
    cookie_value: Optional[str]
    cookie_key_match_type: Optional[EnumLayer7ContentClassCookieMatchTypeKey]
    cookie_value_match_type: Optional[EnumLayer7ContentClassCookieMatchTypeVal]
    case_sensitive: Optional[EnumLayer7ContentClassCookieCase]
#    copy: Optional[str]

    def __init__(self, cntclasid: str = None, cookieid: str = None):
        self.content_class_id = cntclasid
        self.cookie_id = cookieid
        self.cookie_key = None
        self.cookie_value = None
        self.cookie_key_match_type = None
        self.cookie_value_match_type = None
        self.case_sensitive = None
#        self.copy = None

bean_map = {
    Layer7NewCfgContentClassCookieTable: dict(
        struct=L7ContentClassCookieParameters,
        direct=True,
        attrs=dict(
            ContentClassID='content_class_id',
            ID='cookie_id',
            Key='cookie_key',
            Val='cookie_value',
            MatchTypeKey='cookie_key_match_type',
            MatchTypeVal='cookie_value_match_type',
            Case='case_sensitive',
#            Copy='copy'
        )
    )
}


class L7ContentClassCookieConfigurator(AlteonConfigurator):
    parameters_class: ClassVar[L7ContentClassCookieParameters]

    def __init__(self, alteon_connection):
        super(L7ContentClassCookieConfigurator, self).__init__(bean_map, alteon_connection)

    def _read(self, parameters: L7ContentClassCookieParameters) -> L7ContentClassCookieParameters:
        self._read_device_beans(parameters)
        if self._beans:
            return parameters

    def _update(self, parameters: L7ContentClassCookieParameters, dry_run: bool) -> str:
        self._write_device_beans(parameters, dry_run=dry_run)
        return self._get_object_id(parameters) + MSG_UPDATE


    def _entry_bean_instance(self, parameters):
        return self._get_bean_instance(Layer7NewCfgContentClassCookieTable, parameters)


