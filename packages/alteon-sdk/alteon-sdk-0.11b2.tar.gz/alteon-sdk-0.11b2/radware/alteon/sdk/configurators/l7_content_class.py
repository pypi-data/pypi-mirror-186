#!/usr/bin/env python
# Copyright (c) 2019 Radware LTD.
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
from radware.alteon.sdk.alteon_configurator import MSG_UPDATE, AlteonConfigurator
from radware.alteon.beans.Layer7NewCfgContentClassTable import *
from typing import List, Optional, ClassVar, Dict
from radware.alteon.exceptions import AlteonRequestError
from radware.alteon.sdk.alteon_managment import AlteonMngInfo
from radware.sdk.exceptions import DeviceConfiguratorError


class L7ContentClassParameters(RadwareParametersStruct):
    content_class_id: str
    name: Optional[str]
    logical_expression: Optional[str]
    host_name: Optional[EnumLayer7ContentClassHostName]
    path: Optional[EnumLayer7ContentClassPath]
    file_name: Optional[EnumLayer7ContentClassFileName]
    file_type: Optional[EnumLayer7ContentClassFileType]
    header: Optional[EnumLayer7ContentClassHeader]
    cookie: Optional[EnumLayer7ContentClassCookie]
    text: Optional[EnumLayer7ContentClassText]
    xml_tag: Optional[EnumLayer7ContentClassXMLTag]
    #copy: Optional[str]
    content_class_type: Optional[EnumLayer7ContentClassType]


    def __init__(self, id: str = None):
        self.content_class_id = id
        self.name = None
        self.logical_expression = None
        self.host_name = None
        self.path = None
        self.file_name = None
        self.file_type = None
        self.header = None
        self.cookie = None
        self.text = None
        self.xml_tag = None
    #    self.copy = None
        self.content_class_type = None

bean_map = {
    Layer7NewCfgContentClassTable: dict(
        struct=L7ContentClassParameters,
        direct=True,
        attrs=dict(
            ID='content_class_id',
            Name='name',
            LogicalExpression='logical_expression',
            HostName='host_name',
            Path='path',
            FileName='file_name',
            FileType='file_type',
            Header='header',
            Cookie='cookie',
            Text='text',
            XMLTag='xml_tag',
#            Copy='copy',
            Type='content_class_type'
        )
    )
}


class L7ContentClassConfigurator(AlteonConfigurator):
    parameters_class: ClassVar[L7ContentClassParameters]

    def __init__(self, alteon_connection):
        super(L7ContentClassConfigurator, self).__init__(bean_map, alteon_connection)        
        self._mng_info = AlteonMngInfo(alteon_connection)

    def _read(self, parameters: L7ContentClassParameters) -> L7ContentClassParameters:
        self._read_device_beans(parameters)
        if self._beans:
            return parameters

    def _update(self, parameters: L7ContentClassParameters, dry_run: bool) -> str:
        if parameters.host_name is not None:
            raise DeviceConfiguratorError(self.__class__, 'host_name is a read only field')
        if parameters.path is not None:
            raise DeviceConfiguratorError(self.__class__, 'path is a read only field')
        if parameters.file_name is not None:
            raise DeviceConfiguratorError(self.__class__, 'file_name is a read only field')
        if parameters.file_type is not None:
            raise DeviceConfiguratorError(self.__class__, 'file_type is a read only field')
        if parameters.header is not None:
            raise DeviceConfiguratorError(self.__class__, 'header is a read only field')
        if parameters.cookie is not None:
            raise DeviceConfiguratorError(self.__class__, 'cookie is a read only field')
        if parameters.text is not None:
            raise DeviceConfiguratorError(self.__class__, 'text is a read only field')
        if parameters.xml_tag is not None:
            raise DeviceConfiguratorError(self.__class__, 'xml_tag is a read only field')

        #content_class_type nust be set when creating new entry and cannot be update for existing entry.
        #therefore if user didn't set the type use the defualt value for new entry.
        # if entry exist take the type from this entry.
        configured_content_class = self._device_api.read_all(Layer7NewCfgContentClassTable())
        result = self._lookup_current_entry(parameters, configured_content_class)
        if result:
            #entry exist
            new_entry = False
            if parameters.content_class_type is None:
                parameters.content_class_type = result.Type
        else:
            #this is new entry
            new_entry = True
            if parameters.content_class_type is None:
                parameters.content_class_type = EnumLayer7ContentClassType.http

        #don't allow copy for new entry, since the type is set last.
        #which means that if we copy the new entry we don't have the type yet.
        #we don't support the copy field - therefor the next code is not relevant anymore
        #if new_entry == True and parameters.copy is not None:
        #    raise DeviceConfiguratorError(self.__class__, 'copy is not allowed for new configured entry.')


        self._write_device_beans(parameters, dry_run=dry_run)
        return self._get_object_id(parameters) + MSG_UPDATE

    @staticmethod
    def _lookup_current_entry(parameters, configured_content_class):
        for entry in configured_content_class:
            if parameters.content_class_id == entry.ID:
                return entry

    def _entry_bean_instance(self, parameters):
        return self._get_bean_instance(Layer7NewCfgContentClassTable, parameters)


