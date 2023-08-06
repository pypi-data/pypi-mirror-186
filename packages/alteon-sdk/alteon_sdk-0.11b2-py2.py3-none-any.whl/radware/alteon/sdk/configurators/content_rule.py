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
from radware.alteon.beans.SlbNewCfgEnhContRuleTable import *
from typing import Optional, ClassVar, Dict
from radware.alteon.exceptions import AlteonRequestError
from radware.alteon.sdk.alteon_managment import AlteonMngInfo
from radware.sdk.exceptions import DeviceConfiguratorError


class ContentRuleParameters(RadwareParametersStruct):
    virtual_server_id: str
    virtual_service_index: int
    content_rule_index: int
    rule_name: Optional[str]
    content_class: Optional[str]
    action: Optional[EnumSlbContRuleAction]
    group_id: Optional[str]
    redirection_url: Optional[str]
    state: Optional[EnumSlbContRuleState]
    bot_manager_processing: Optional[EnumSlbContRuleBotMProcessing]
    bot_manager_policy: Optional[str]
    secure_web_application_processing: Optional[EnumSlbContRuleSecwaProcessing]
    secure_path_policy: Optional[str]
    sideband_processing: Optional[EnumSlbContRuleSidebandProccessing]
    sideband_policy: Optional[str]

    def __init__(self, srvrid: str = None, serviceidx: int = None, ruleidx: int = None):
        self.virtual_server_id = srvrid
        self.virtual_service_index = serviceidx
        self.content_rule_index = ruleidx
        self.rule_name = None
        self.content_class = None
        self.action = None
        self.group_id = None
        self.redirection_url = None
        self.state = None
        self.bot_manager_processing = None
        self.bot_manager_policy = None
        self.secure_web_application_processing = None
        self.secure_path_policy = None
        self.sideband_processing = None
        self.sideband_policy = None
    
bean_map = {
    SlbNewCfgEnhContRuleTable: dict(
        struct=ContentRuleParameters,
        direct=True,
        attrs=dict(
            VirtServIndex='virtual_server_id',
            VirtServiceIndex='virtual_service_index',
            Index='content_rule_index',
            Name='rule_name',
            ContClass='content_class',
            Action='action',
            RealGrpNum='group_id',
            Redirection='redirection_url',
            State='state',
            BotMProcessing='bot_manager_processing',
            BotMPolicy='bot_manager_policy',
            SecwaProcessing='secure_web_application_processing',
            SecurePathPolicy='secure_path_policy',
            SidebandProccessing='sideband_processing',
            SidebandID='sideband_policy'
        )
    )
}


class ContentRuleConfigurator(AlteonConfigurator):
    parameters_class: ClassVar[ContentRuleParameters]

    def __init__(self, alteon_connection):
        super(ContentRuleConfigurator, self).__init__(bean_map, alteon_connection)

    def _read(self, parameters: ContentRuleParameters) -> ContentRuleParameters:
        self._read_device_beans(parameters)
        if self._beans:
            return parameters

    def _update(self, parameters: ContentRuleParameters, dry_run: bool) -> str:
        self._write_device_beans(parameters, dry_run=dry_run)
        return self._get_object_id(parameters) + MSG_UPDATE


    def _entry_bean_instance(self, parameters):
        return self._get_bean_instance(SlbNewCfgEnhContRuleTable, parameters)


