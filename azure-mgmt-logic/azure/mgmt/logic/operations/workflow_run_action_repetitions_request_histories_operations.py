# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import uuid
from msrest.pipeline import ClientRawResponse
from msrestazure.azure_exceptions import CloudError

from .. import models


class WorkflowRunActionRepetitionsRequestHistoriesOperations(object):
    """WorkflowRunActionRepetitionsRequestHistoriesOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: The API version. Constant value: "2018-07-01-preview".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2018-07-01-preview"

        self.config = config

    def list(
            self, resource_group_name, workflow_name, run_name, action_name, repetition_name, custom_headers=None, raw=False, **operation_config):
        """List a workflow run repetition request history.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param workflow_name: The workflow name.
        :type workflow_name: str
        :param run_name: The workflow run name.
        :type run_name: str
        :param action_name: The workflow action name.
        :type action_name: str
        :param repetition_name: The workflow repetition.
        :type repetition_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of RequestHistory
        :rtype:
         ~azure.mgmt.logic.models.RequestHistoryPaged[~azure.mgmt.logic.models.RequestHistory]
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = self.list.metadata['url']
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
                    'workflowName': self._serialize.url("workflow_name", workflow_name, 'str'),
                    'runName': self._serialize.url("run_name", run_name, 'str'),
                    'actionName': self._serialize.url("action_name", action_name, 'str'),
                    'repetitionName': self._serialize.url("repetition_name", repetition_name, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            response = self._client.send(request, stream=False, **operation_config)

            if response.status_code not in [200]:
                exp = CloudError(response)
                exp.request_id = response.headers.get('x-ms-request-id')
                raise exp

            return response

        # Deserialize response
        deserialized = models.RequestHistoryPaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.RequestHistoryPaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized
    list.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/runs/{runName}/actions/{actionName}/repetitions/{repetitionName}/requestHistories'}

    def get(
            self, resource_group_name, workflow_name, run_name, action_name, repetition_name, request_history_name, custom_headers=None, raw=False, **operation_config):
        """Gets a workflow run repetition request history.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param workflow_name: The workflow name.
        :type workflow_name: str
        :param run_name: The workflow run name.
        :type run_name: str
        :param action_name: The workflow action name.
        :type action_name: str
        :param repetition_name: The workflow repetition.
        :type repetition_name: str
        :param request_history_name: The request history name.
        :type request_history_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: RequestHistory or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.logic.models.RequestHistory or
         ~msrest.pipeline.ClientRawResponse
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'workflowName': self._serialize.url("workflow_name", workflow_name, 'str'),
            'runName': self._serialize.url("run_name", run_name, 'str'),
            'actionName': self._serialize.url("action_name", action_name, 'str'),
            'repetitionName': self._serialize.url("repetition_name", repetition_name, 'str'),
            'requestHistoryName': self._serialize.url("request_history_name", request_history_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('RequestHistory', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/runs/{runName}/actions/{actionName}/repetitions/{repetitionName}/requestHistories/{requestHistoryName}'}
