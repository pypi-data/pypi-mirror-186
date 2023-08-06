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
from radware.alteon.beans.Layer7NewCfgContentClassHeaderTable import *
from typing import Optional, ClassVar, Dict
from radware.alteon.exceptions import AlteonRequestError
from radware.alteon.sdk.alteon_managment import AlteonMngInfo
from radware.sdk.exceptions import DeviceConfiguratorError


class L7ContentClassHeaderParameters(RadwareParametersStruct):
    content_class_id: str
    header_id: str
    header_name: Optional[str]
    header_value: Optional[str]
    header_name_match_type: Optional[EnumLayer7ContentClassHeaderMatchTypeName]
    header_value_match_type: Optional[EnumLayer7ContentClassHeaderMatchTypeVal]
    case_sensitive: Optional[EnumLayer7ContentClassHeaderCase]
#    copy: Optional[str]

    def __init__(self, cntclasid: str = None, headerid: str = None):
        self.content_class_id = cntclasid
        self.header_id = headerid
        self.header_name = None
        self.header_value = None
        self.header_name_match_type = None
        self.header_value_match_type = None
        self.case_sensitive = None
#        self.copy = None

bean_map = {
    Layer7NewCfgContentClassHeaderTable: dict(
        struct=L7ContentClassHeaderParameters,
        direct=True,
        attrs=dict(
            ContentClassID='content_class_id',
            ID='header_id',
            Name='header_name',
            Val='header_value',
            MatchTypeName='header_name_match_type',
            MatchTypeVal='header_value_match_type',
            Case='case_sensitive',
#            Copy='copy'
        )
    )
}


class L7ContentClassHeaderConfigurator(AlteonConfigurator):
    parameters_class: ClassVar[L7ContentClassHeaderParameters]

    def __init__(self, alteon_connection):
        super(L7ContentClassHeaderConfigurator, self).__init__(bean_map, alteon_connection)

    def _read(self, parameters: L7ContentClassHeaderParameters) -> L7ContentClassHeaderParameters:
        self._read_device_beans(parameters)
        if self._beans:
            return parameters

    def _update(self, parameters: L7ContentClassHeaderParameters, dry_run: bool) -> str:
        self._write_device_beans(parameters, dry_run=dry_run)
        return self._get_object_id(parameters) + MSG_UPDATE


    def _entry_bean_instance(self, parameters):
        return self._get_bean_instance(Layer7NewCfgContentClassHeaderTable, parameters)


