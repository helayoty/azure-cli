# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "sql mi dtc update",
)
class Update(AAZCommand):
    """Update managed instance DTC settings.

    This command updates the managed instance DTC settings. All parameters are optional.

    :example: Enable DTC on a managed instance
        az sql mi dtc update -g resourceGroup1 --mi managedInstance1 --dtc-enabled true
        az sql mi dtc update --ids /subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/ResourceGroup1/providers/Microsoft.Sql/managedInstances/ManagedInstance1/dtc/current --dtc-enabled true

    :example: Allow XA transactions for managed instance DTC
        az sql mi dtc update -g resourceGroup1 --mi managedInstance1 --xa-transactions-enabled true
    """

    _aaz_info = {
        "version": "2022-05-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.sql/managedinstances/{}/dtc/{}", "2022-05-01-preview"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    AZ_SUPPORT_GENERIC_UPDATE = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.managed_instance_name = AAZStrArg(
            options=["--mi", "--managed-instance-name"],
            help="The name of the managed instance.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            help="Name of the resource group",
            required=True,
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.dtc_enabled = AAZBoolArg(
            options=["--dtc-enabled"],
            arg_group="Properties",
            help="Active status of managed instance DTC.",
            nullable=True,
        )
        _args_schema.external_dns_suffix_search_list = AAZListArg(
            options=["--external-dns-suffixes", "--external-dns-suffix-search-list"],
            arg_group="Properties",
            help="External dns suffix search list of managed instance DTC.",
            nullable=True,
        )

        external_dns_suffix_search_list = cls._args_schema.external_dns_suffix_search_list
        external_dns_suffix_search_list.Element = AAZStrArg(
            nullable=True,
        )

        # define Arg Group "SecuritySettings"

        _args_schema = cls._args_schema
        _args_schema.sna_lu6point2_transactions_enabled = AAZBoolArg(
            options=["--sna-lu-transactions", "--sna-lu6point2-transactions-enabled"],
            arg_group="SecuritySettings",
            help="Allow SNA LU 6.2 Transactions to managed instance DTC.",
            nullable=True,
        )
        _args_schema.xa_transactions_default_timeout = AAZIntArg(
            options=["--xa-default-timeout", "--xa-transactions-default-timeout"],
            arg_group="SecuritySettings",
            help="Default timeout for XA Transactions (in seconds).",
            nullable=True,
        )
        _args_schema.xa_transactions_enabled = AAZBoolArg(
            options=["--xa-transactions", "--xa-transactions-enabled"],
            arg_group="SecuritySettings",
            help="Allow XA Transactions to managed instance DTC.",
            nullable=True,
        )
        _args_schema.xa_transactions_maximum_timeout = AAZIntArg(
            options=["--xa-max-timeout", "--xa-transactions-maximum-timeout"],
            arg_group="SecuritySettings",
            help="Maximum timeout for XA Transactions (in seconds).",
            nullable=True,
        )

        # define Arg Group "TransactionManagerCommunicationSettings"

        _args_schema = cls._args_schema
        _args_schema.allow_inbound_enabled = AAZBoolArg(
            options=["--allow-inbound-enabled"],
            arg_group="TransactionManagerCommunicationSettings",
            help="Allow Inbound traffic to managed instance DTC.",
            nullable=True,
        )
        _args_schema.allow_outbound_enabled = AAZBoolArg(
            options=["--allow-outbound-enabled"],
            arg_group="TransactionManagerCommunicationSettings",
            help="Allow Outbound traffic of managed instance DTC.",
            nullable=True,
        )
        _args_schema.authentication = AAZStrArg(
            options=["--authentication"],
            arg_group="TransactionManagerCommunicationSettings",
            help="Authentication type of managed instance DTC.",
            nullable=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.ManagedInstanceDtcsGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        yield self.ManagedInstanceDtcsCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_update(self, instance):
        pass

    @register_callback
    def post_instance_update(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class ManagedInstanceDtcsGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/managedInstances/{managedInstanceName}/dtc/{dtcName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "dtcName", "current",
                    required=True,
                ),
                **self.serialize_url_param(
                    "managedInstanceName", self.ctx.args.managed_instance_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-05-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()
            _UpdateHelper._build_schema_managed_instance_dtc_read(cls._schema_on_200)

            return cls._schema_on_200

    class ManagedInstanceDtcsCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/managedInstances/{managedInstanceName}/dtc/{dtcName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "dtcName", "current",
                    required=True,
                ),
                **self.serialize_url_param(
                    "managedInstanceName", self.ctx.args.managed_instance_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-05-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

        def on_200(self, session):
            data = self.deserialize_http_content(session)

            # Due to a bug in the API, the dtcHostName is returned as the dtcHostNameDnsSuffix property. Also the dtcHostName doesn't exist as a property currently.
            # The new API versions (with a fix) should return dtcHostName property and the correct value for dtcHostNameDnsSuffix.
            # Currently, as a workaround we check if the dtcHostName property exist.
            # If it doesn't exist, we create an additional field "dtcHostName" and display the "dtcHostNameDnsSuffix"
            # from the API response as the host name. Also, the dtcHostNameDnsSuffix is corrected to display the proper value.
            if 'dtcHostName' not in data['properties']:
                data['properties']['dtcHostName'] = data['properties']['dtcHostNameDnsSuffix']

                # Also, we extract the DNS suffix and display it properly.
                data['properties']['dtcHostNameDnsSuffix'] = data['properties']['dtcHostNameDnsSuffix'].split('.', 1)[1]
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()
            _UpdateHelper._build_schema_managed_instance_dtc_read(cls._schema_on_200)

            return cls._schema_on_200

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("dtcEnabled", AAZBoolType, ".dtc_enabled")
                properties.set_prop("externalDnsSuffixSearchList", AAZListType, ".external_dns_suffix_search_list")
                properties.set_prop("securitySettings", AAZObjectType)

            external_dns_suffix_search_list = _builder.get(".properties.externalDnsSuffixSearchList")
            if external_dns_suffix_search_list is not None:
                external_dns_suffix_search_list.set_elements(AAZStrType, ".")

            security_settings = _builder.get(".properties.securitySettings")
            if security_settings is not None:
                security_settings.set_prop("snaLu6point2TransactionsEnabled", AAZBoolType, ".sna_lu6point2_transactions_enabled")
                security_settings.set_prop("transactionManagerCommunicationSettings", AAZObjectType)
                security_settings.set_prop("xaTransactionsDefaultTimeout", AAZIntType, ".xa_transactions_default_timeout")
                security_settings.set_prop("xaTransactionsEnabled", AAZBoolType, ".xa_transactions_enabled")
                security_settings.set_prop("xaTransactionsMaximumTimeout", AAZIntType, ".xa_transactions_maximum_timeout")

            transaction_manager_communication_settings = _builder.get(".properties.securitySettings.transactionManagerCommunicationSettings")
            if transaction_manager_communication_settings is not None:
                transaction_manager_communication_settings.set_prop("allowInboundEnabled", AAZBoolType, ".allow_inbound_enabled")
                transaction_manager_communication_settings.set_prop("allowOutboundEnabled", AAZBoolType, ".allow_outbound_enabled")
                transaction_manager_communication_settings.set_prop("authentication", AAZStrType, ".authentication")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

    _schema_managed_instance_dtc_read = None

    @classmethod
    def _build_schema_managed_instance_dtc_read(cls, _schema):
        if cls._schema_managed_instance_dtc_read is not None:
            _schema.id = cls._schema_managed_instance_dtc_read.id
            _schema.name = cls._schema_managed_instance_dtc_read.name
            _schema.properties = cls._schema_managed_instance_dtc_read.properties
            _schema.type = cls._schema_managed_instance_dtc_read.type
            return

        cls._schema_managed_instance_dtc_read = _schema_managed_instance_dtc_read = AAZObjectType()

        managed_instance_dtc_read = _schema_managed_instance_dtc_read
        managed_instance_dtc_read.id = AAZStrType(
            flags={"read_only": True},
        )
        managed_instance_dtc_read.name = AAZStrType(
            flags={"read_only": True},
        )
        managed_instance_dtc_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        managed_instance_dtc_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_managed_instance_dtc_read.properties
        properties.dtc_enabled = AAZBoolType(
            serialized_name="dtcEnabled",
        )
        properties.dtc_host_name_dns_suffix = AAZStrType(
            serialized_name="dtcHostNameDnsSuffix",
            flags={"read_only": True},
        )
        properties.dtc_host_name = AAZStrType(
            serialized_name="dtcHostName",
            flags={"read_only": True},
        )
        properties.external_dns_suffix_search_list = AAZListType(
            serialized_name="externalDnsSuffixSearchList",
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.security_settings = AAZObjectType(
            serialized_name="securitySettings",
        )

        external_dns_suffix_search_list = _schema_managed_instance_dtc_read.properties.external_dns_suffix_search_list
        external_dns_suffix_search_list.Element = AAZStrType()

        security_settings = _schema_managed_instance_dtc_read.properties.security_settings
        security_settings.sna_lu6point2_transactions_enabled = AAZBoolType(
            serialized_name="snaLu6point2TransactionsEnabled",
        )
        security_settings.transaction_manager_communication_settings = AAZObjectType(
            serialized_name="transactionManagerCommunicationSettings",
        )
        security_settings.xa_transactions_default_timeout = AAZIntType(
            serialized_name="xaTransactionsDefaultTimeout",
        )
        security_settings.xa_transactions_enabled = AAZBoolType(
            serialized_name="xaTransactionsEnabled",
        )
        security_settings.xa_transactions_maximum_timeout = AAZIntType(
            serialized_name="xaTransactionsMaximumTimeout",
        )

        transaction_manager_communication_settings = _schema_managed_instance_dtc_read.properties.security_settings.transaction_manager_communication_settings
        transaction_manager_communication_settings.allow_inbound_enabled = AAZBoolType(
            serialized_name="allowInboundEnabled",
        )
        transaction_manager_communication_settings.allow_outbound_enabled = AAZBoolType(
            serialized_name="allowOutboundEnabled",
        )
        transaction_manager_communication_settings.authentication = AAZStrType()

        _schema.id = cls._schema_managed_instance_dtc_read.id
        _schema.name = cls._schema_managed_instance_dtc_read.name
        _schema.properties = cls._schema_managed_instance_dtc_read.properties
        _schema.type = cls._schema_managed_instance_dtc_read.type


__all__ = ["Update"]