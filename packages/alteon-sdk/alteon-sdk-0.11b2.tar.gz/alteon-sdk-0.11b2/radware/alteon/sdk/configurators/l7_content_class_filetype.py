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
from radware.alteon.beans.Layer7NewCfgContentClassFileTypeTable import *
from typing import Optional, ClassVar, Dict
from radware.alteon.exceptions import AlteonRequestError
from radware.alteon.sdk.alteon_managment import AlteonMngInfo
from radware.sdk.exceptions import DeviceConfiguratorError


class L7ContentClassFileTypeParameters(RadwareParametersStruct):
    content_class_id: str
    file_type_id: str
    file_type_to_match: Optional[str]
    match_type: Optional[EnumLayer7ContentClassFileTypeMatchType]
    case_sensitive: Optional[EnumLayer7ContentClassFileTypeCase]
#    copy: Optional[str]

    def __init__(self, cntclasid: str = None, filetypeid: str = None):
        self.content_class_id = cntclasid
        self.file_type_id = filetypeid
        self.file_type_to_match = None
        self.match_type = None
        self.case_sensitive = None
#        self.copy = None

bean_map = {
    Layer7NewCfgContentClassFileTypeTable: dict(
        struct=L7ContentClassFileTypeParameters,
        direct=True,
        attrs=dict(
            ContentClassID='content_class_id',
            ID='file_type_id',
            FileType='file_type_to_match',
            MatchType='match_type',
            Case='case_sensitive',
#            Copy='copy'
        )
    )
}


class L7ContentClassFileTypeConfigurator(AlteonConfigurator):
    parameters_class: ClassVar[L7ContentClassFileTypeParameters]

    def __init__(self, alteon_connection):
        super(L7ContentClassFileTypeConfigurator, self).__init__(bean_map, alteon_connection)

    def _read(self, parameters: L7ContentClassFileTypeParameters) -> L7ContentClassFileTypeParameters:
        self._read_device_beans(parameters)
        if self._beans:
            return parameters

    def _update(self, parameters: L7ContentClassFileTypeParameters, dry_run: bool) -> str:
        self._write_device_beans(parameters, dry_run=dry_run)
        return self._get_object_id(parameters) + MSG_UPDATE


    def _entry_bean_instance(self, parameters):
        return self._get_bean_instance(Layer7NewCfgContentClassFileTypeTable, parameters)


