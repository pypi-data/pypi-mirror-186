'''
# `nomad_namespace`

Refer to the Terraform Registory for docs: [`nomad_namespace`](https://www.terraform.io/docs/providers/nomad/r/namespace).
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from .._jsii import *

import cdktf as _cdktf_9a9027ec
import constructs as _constructs_77d1e7e8


class Namespace(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.namespace.Namespace",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/nomad/r/namespace nomad_namespace}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        capabilities: typing.Optional[typing.Union["NamespaceCapabilities", typing.Dict[builtins.str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        meta: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        quota: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/nomad/r/namespace nomad_namespace} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Unique name for this namespace. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/namespace#name Namespace#name}
        :param capabilities: capabilities block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/namespace#capabilities Namespace#capabilities}
        :param description: Description for this namespace. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/namespace#description Namespace#description}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/namespace#id Namespace#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param meta: Metadata associated with the namespace. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/namespace#meta Namespace#meta}
        :param quota: Quota to set for this namespace. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/namespace#quota Namespace#quota}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6664f886989d474b0b63d9927c7b349975f0ca6ee369f1c9be4689de8174263f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = NamespaceConfig(
            name=name,
            capabilities=capabilities,
            description=description,
            id=id,
            meta=meta,
            quota=quota,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putCapabilities")
    def put_capabilities(
        self,
        *,
        disabled_task_drivers: typing.Optional[typing.Sequence[builtins.str]] = None,
        enabled_task_drivers: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param disabled_task_drivers: Disabled task drivers for the namespace. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/namespace#disabled_task_drivers Namespace#disabled_task_drivers}
        :param enabled_task_drivers: Enabled task drivers for the namespace. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/namespace#enabled_task_drivers Namespace#enabled_task_drivers}
        '''
        value = NamespaceCapabilities(
            disabled_task_drivers=disabled_task_drivers,
            enabled_task_drivers=enabled_task_drivers,
        )

        return typing.cast(None, jsii.invoke(self, "putCapabilities", [value]))

    @jsii.member(jsii_name="resetCapabilities")
    def reset_capabilities(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCapabilities", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMeta")
    def reset_meta(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMeta", []))

    @jsii.member(jsii_name="resetQuota")
    def reset_quota(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQuota", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="capabilities")
    def capabilities(self) -> "NamespaceCapabilitiesOutputReference":
        return typing.cast("NamespaceCapabilitiesOutputReference", jsii.get(self, "capabilities"))

    @builtins.property
    @jsii.member(jsii_name="capabilitiesInput")
    def capabilities_input(self) -> typing.Optional["NamespaceCapabilities"]:
        return typing.cast(typing.Optional["NamespaceCapabilities"], jsii.get(self, "capabilitiesInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="metaInput")
    def meta_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "metaInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="quotaInput")
    def quota_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "quotaInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d621b8317acd077e4337f0991daddc76582ec1edfd564d350a7d90b25714bec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2c8981294e43cce7f3b631f6855ccc23bd21303f16502051f944fc3bfc09615)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="meta")
    def meta(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "meta"))

    @meta.setter
    def meta(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dea37a9f1ee55d1c820907ee0566975a8f57c2f2a65b9f46c74928550c965b68)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "meta", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15aa23ccad32d1b1ddcdcca600a2b026e96a1124795a804d74c6f7c5553b3aa6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="quota")
    def quota(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "quota"))

    @quota.setter
    def quota(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a73ebd700626428885ff8be7c1c56e39bb9efdf623b0e072ee324d8115ae1895)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "quota", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-nomad.namespace.NamespaceCapabilities",
    jsii_struct_bases=[],
    name_mapping={
        "disabled_task_drivers": "disabledTaskDrivers",
        "enabled_task_drivers": "enabledTaskDrivers",
    },
)
class NamespaceCapabilities:
    def __init__(
        self,
        *,
        disabled_task_drivers: typing.Optional[typing.Sequence[builtins.str]] = None,
        enabled_task_drivers: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param disabled_task_drivers: Disabled task drivers for the namespace. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/namespace#disabled_task_drivers Namespace#disabled_task_drivers}
        :param enabled_task_drivers: Enabled task drivers for the namespace. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/namespace#enabled_task_drivers Namespace#enabled_task_drivers}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3379bc61ce22be5e8f5f099b1c0b081234e86c61100cda567dba8e72745663b)
            check_type(argname="argument disabled_task_drivers", value=disabled_task_drivers, expected_type=type_hints["disabled_task_drivers"])
            check_type(argname="argument enabled_task_drivers", value=enabled_task_drivers, expected_type=type_hints["enabled_task_drivers"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if disabled_task_drivers is not None:
            self._values["disabled_task_drivers"] = disabled_task_drivers
        if enabled_task_drivers is not None:
            self._values["enabled_task_drivers"] = enabled_task_drivers

    @builtins.property
    def disabled_task_drivers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Disabled task drivers for the namespace.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/namespace#disabled_task_drivers Namespace#disabled_task_drivers}
        '''
        result = self._values.get("disabled_task_drivers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def enabled_task_drivers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Enabled task drivers for the namespace.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/namespace#enabled_task_drivers Namespace#enabled_task_drivers}
        '''
        result = self._values.get("enabled_task_drivers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NamespaceCapabilities(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NamespaceCapabilitiesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.namespace.NamespaceCapabilitiesOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83a32012fcaeea628d7e7d1b179a97a03193124d36002385ba8db74eb39a512e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDisabledTaskDrivers")
    def reset_disabled_task_drivers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisabledTaskDrivers", []))

    @jsii.member(jsii_name="resetEnabledTaskDrivers")
    def reset_enabled_task_drivers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabledTaskDrivers", []))

    @builtins.property
    @jsii.member(jsii_name="disabledTaskDriversInput")
    def disabled_task_drivers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "disabledTaskDriversInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledTaskDriversInput")
    def enabled_task_drivers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "enabledTaskDriversInput"))

    @builtins.property
    @jsii.member(jsii_name="disabledTaskDrivers")
    def disabled_task_drivers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "disabledTaskDrivers"))

    @disabled_task_drivers.setter
    def disabled_task_drivers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__662e6da8ef8c64378e941e496e56d5c65cc94c782acd498df960512ebb01ce63)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disabledTaskDrivers", value)

    @builtins.property
    @jsii.member(jsii_name="enabledTaskDrivers")
    def enabled_task_drivers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "enabledTaskDrivers"))

    @enabled_task_drivers.setter
    def enabled_task_drivers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53d45d4effdc237deb09d70385ffeca360e9eb19a8ac2d747dcf1f9cb8f552b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabledTaskDrivers", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[NamespaceCapabilities]:
        return typing.cast(typing.Optional[NamespaceCapabilities], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[NamespaceCapabilities]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed44cc642b680de4437e740e7ef692963250a4ec8d6a2f02e5cf844d93aec4db)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-nomad.namespace.NamespaceConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "name": "name",
        "capabilities": "capabilities",
        "description": "description",
        "id": "id",
        "meta": "meta",
        "quota": "quota",
    },
)
class NamespaceConfig(_cdktf_9a9027ec.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
        name: builtins.str,
        capabilities: typing.Optional[typing.Union[NamespaceCapabilities, typing.Dict[builtins.str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        meta: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        quota: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Unique name for this namespace. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/namespace#name Namespace#name}
        :param capabilities: capabilities block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/namespace#capabilities Namespace#capabilities}
        :param description: Description for this namespace. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/namespace#description Namespace#description}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/namespace#id Namespace#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param meta: Metadata associated with the namespace. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/namespace#meta Namespace#meta}
        :param quota: Quota to set for this namespace. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/namespace#quota Namespace#quota}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(capabilities, dict):
            capabilities = NamespaceCapabilities(**capabilities)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a81352aa4fd2f5d9a2d30390572fa3baecc6fbd2f02319884c8eccc39bcb5e2e)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument capabilities", value=capabilities, expected_type=type_hints["capabilities"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument meta", value=meta, expected_type=type_hints["meta"])
            check_type(argname="argument quota", value=quota, expected_type=type_hints["quota"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if capabilities is not None:
            self._values["capabilities"] = capabilities
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if meta is not None:
            self._values["meta"] = meta
        if quota is not None:
            self._values["quota"] = quota

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(
        self,
    ) -> typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[_cdktf_9a9027ec.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[_cdktf_9a9027ec.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Unique name for this namespace.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/namespace#name Namespace#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def capabilities(self) -> typing.Optional[NamespaceCapabilities]:
        '''capabilities block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/namespace#capabilities Namespace#capabilities}
        '''
        result = self._values.get("capabilities")
        return typing.cast(typing.Optional[NamespaceCapabilities], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Description for this namespace.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/namespace#description Namespace#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/namespace#id Namespace#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def meta(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Metadata associated with the namespace.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/namespace#meta Namespace#meta}
        '''
        result = self._values.get("meta")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def quota(self) -> typing.Optional[builtins.str]:
        '''Quota to set for this namespace.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/namespace#quota Namespace#quota}
        '''
        result = self._values.get("quota")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NamespaceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "Namespace",
    "NamespaceCapabilities",
    "NamespaceCapabilitiesOutputReference",
    "NamespaceConfig",
]

publication.publish()

def _typecheckingstub__6664f886989d474b0b63d9927c7b349975f0ca6ee369f1c9be4689de8174263f(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    capabilities: typing.Optional[typing.Union[NamespaceCapabilities, typing.Dict[builtins.str, typing.Any]]] = None,
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    meta: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    quota: typing.Optional[builtins.str] = None,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d621b8317acd077e4337f0991daddc76582ec1edfd564d350a7d90b25714bec(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2c8981294e43cce7f3b631f6855ccc23bd21303f16502051f944fc3bfc09615(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dea37a9f1ee55d1c820907ee0566975a8f57c2f2a65b9f46c74928550c965b68(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15aa23ccad32d1b1ddcdcca600a2b026e96a1124795a804d74c6f7c5553b3aa6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a73ebd700626428885ff8be7c1c56e39bb9efdf623b0e072ee324d8115ae1895(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3379bc61ce22be5e8f5f099b1c0b081234e86c61100cda567dba8e72745663b(
    *,
    disabled_task_drivers: typing.Optional[typing.Sequence[builtins.str]] = None,
    enabled_task_drivers: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83a32012fcaeea628d7e7d1b179a97a03193124d36002385ba8db74eb39a512e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__662e6da8ef8c64378e941e496e56d5c65cc94c782acd498df960512ebb01ce63(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53d45d4effdc237deb09d70385ffeca360e9eb19a8ac2d747dcf1f9cb8f552b1(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed44cc642b680de4437e740e7ef692963250a4ec8d6a2f02e5cf844d93aec4db(
    value: typing.Optional[NamespaceCapabilities],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a81352aa4fd2f5d9a2d30390572fa3baecc6fbd2f02319884c8eccc39bcb5e2e(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    capabilities: typing.Optional[typing.Union[NamespaceCapabilities, typing.Dict[builtins.str, typing.Any]]] = None,
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    meta: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    quota: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
