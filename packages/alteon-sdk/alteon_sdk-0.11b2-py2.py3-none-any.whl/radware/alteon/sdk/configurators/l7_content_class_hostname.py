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
from radware.alteon.beans.Layer7NewCfgContentClassHostNameTable import *
from typing import Optional, ClassVar, Dict
from radware.alteon.exceptions import AlteonRequestError
from radware.alteon.sdk.alteon_managment import AlteonMngInfo
from radware.sdk.exceptions import DeviceConfiguratorError


class L7ContentClassHostNameParameters(RadwareParametersStruct):
    content_class_id: str
    host_name_id: str
    host_name: Optional[str]
    match_type: Optional[EnumLayer7ContentClassHostNameMatchType]
    data_class_id: Optional[str]
#    copy: Optional[str]

    def __init__(self, cntclasid: str = None, hostnameid: str = None):
        self.content_class_id = cntclasid
        self.host_name_id = hostnameid
        self.host_name = None
        self.match_type = None
        self.data_class_id = None
#        self.copy = None

bean_map = {
    Layer7NewCfgContentClassHostNameTable: dict(
        struct=L7ContentClassHostNameParameters,
        direct=True,
        attrs=dict(
            ContentClassID='content_class_id',
            ID='host_name_id',
            HostName='host_name',
            MatchType='match_type',
            DataclassID='data_class_id',
#            Copy='copy'
        )
    )
}


class L7ContentClassHostNameConfigurator(AlteonConfigurator):
    parameters_class: ClassVar[L7ContentClassHostNameParameters]

    def __init__(self, alteon_connection):
        super(L7ContentClassHostNameConfigurator, self).__init__(bean_map, alteon_connection)

    def _read(self, parameters: L7ContentClassHostNameParameters) -> L7ContentClassHostNameParameters:
        self._read_device_beans(parameters)
        if self._beans:
            return parameters

    def _update(self, parameters: L7ContentClassHostNameParameters, dry_run: bool) -> str:
        self._write_device_beans(parameters, dry_run=dry_run)
        return self._get_object_id(parameters) + MSG_UPDATE


    def _entry_bean_instance(self, parameters):
        return self._get_bean_instance(Layer7NewCfgContentClassHostNameTable, parameters)


