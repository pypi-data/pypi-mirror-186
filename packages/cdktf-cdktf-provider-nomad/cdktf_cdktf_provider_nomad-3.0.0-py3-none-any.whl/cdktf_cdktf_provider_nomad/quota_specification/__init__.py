'''
# `nomad_quota_specification`

Refer to the Terraform Registory for docs: [`nomad_quota_specification`](https://www.terraform.io/docs/providers/nomad/r/quota_specification).
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


class QuotaSpecification(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.quotaSpecification.QuotaSpecification",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/nomad/r/quota_specification nomad_quota_specification}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        limits: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["QuotaSpecificationLimits", typing.Dict[builtins.str, typing.Any]]]],
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/nomad/r/quota_specification nomad_quota_specification} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param limits: limits block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/quota_specification#limits QuotaSpecification#limits}
        :param name: Unique name for this quota specification. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/quota_specification#name QuotaSpecification#name}
        :param description: Description for this quota specification. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/quota_specification#description QuotaSpecification#description}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/quota_specification#id QuotaSpecification#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94f7f898ee7e9543c060b7c80ce5e18554dc44a4a4e6180aa607c19a8f128d5d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = QuotaSpecificationConfig(
            limits=limits,
            name=name,
            description=description,
            id=id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putLimits")
    def put_limits(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["QuotaSpecificationLimits", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68c8a5b25c8e960c0ec0576016f25e172527673a39a2105f0ad868b013efad9a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLimits", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="limits")
    def limits(self) -> "QuotaSpecificationLimitsList":
        return typing.cast("QuotaSpecificationLimitsList", jsii.get(self, "limits"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="limitsInput")
    def limits_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["QuotaSpecificationLimits"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["QuotaSpecificationLimits"]]], jsii.get(self, "limitsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df6bcfce0fccd60dcd16673d3a4129092946c097ac55a94a7db9741ca7605f8d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2be5ed39974d0bed05a4928cf34117746e64cf8bb5e96f0a2439991ad2945ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c363c42648bc2ec743a9f5e73cd3f0a1dfc5e1827dc15c80a3164ba474b84266)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-nomad.quotaSpecification.QuotaSpecificationConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "limits": "limits",
        "name": "name",
        "description": "description",
        "id": "id",
    },
)
class QuotaSpecificationConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        limits: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["QuotaSpecificationLimits", typing.Dict[builtins.str, typing.Any]]]],
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param limits: limits block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/quota_specification#limits QuotaSpecification#limits}
        :param name: Unique name for this quota specification. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/quota_specification#name QuotaSpecification#name}
        :param description: Description for this quota specification. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/quota_specification#description QuotaSpecification#description}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/quota_specification#id QuotaSpecification#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9bbacac1608669777de5aa925508b8baa491a0beaf6e872b0375040fbf806252)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument limits", value=limits, expected_type=type_hints["limits"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "limits": limits,
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
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id

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
    def limits(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["QuotaSpecificationLimits"]]:
        '''limits block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/quota_specification#limits QuotaSpecification#limits}
        '''
        result = self._values.get("limits")
        assert result is not None, "Required property 'limits' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["QuotaSpecificationLimits"]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Unique name for this quota specification.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/quota_specification#name QuotaSpecification#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Description for this quota specification.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/quota_specification#description QuotaSpecification#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/quota_specification#id QuotaSpecification#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "QuotaSpecificationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-nomad.quotaSpecification.QuotaSpecificationLimits",
    jsii_struct_bases=[],
    name_mapping={"region": "region", "region_limit": "regionLimit"},
)
class QuotaSpecificationLimits:
    def __init__(
        self,
        *,
        region: builtins.str,
        region_limit: typing.Union["QuotaSpecificationLimitsRegionLimit", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param region: Region in which this limit has affect. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/quota_specification#region QuotaSpecification#region}
        :param region_limit: region_limit block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/quota_specification#region_limit QuotaSpecification#region_limit}
        '''
        if isinstance(region_limit, dict):
            region_limit = QuotaSpecificationLimitsRegionLimit(**region_limit)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__046cab3db18bfd2e688094ffdf93d01951feb11939f6d207109d226b05318751)
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument region_limit", value=region_limit, expected_type=type_hints["region_limit"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "region": region,
            "region_limit": region_limit,
        }

    @builtins.property
    def region(self) -> builtins.str:
        '''Region in which this limit has affect.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/quota_specification#region QuotaSpecification#region}
        '''
        result = self._values.get("region")
        assert result is not None, "Required property 'region' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def region_limit(self) -> "QuotaSpecificationLimitsRegionLimit":
        '''region_limit block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/quota_specification#region_limit QuotaSpecification#region_limit}
        '''
        result = self._values.get("region_limit")
        assert result is not None, "Required property 'region_limit' is missing"
        return typing.cast("QuotaSpecificationLimitsRegionLimit", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "QuotaSpecificationLimits(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class QuotaSpecificationLimitsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.quotaSpecification.QuotaSpecificationLimitsList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d5ca69984a61765150d74df541f2b7b9645879ddc51be550cbcd42c36f7ab0c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "QuotaSpecificationLimitsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce4d53ecb9d49be82f7d69c87dfea2184c144f08230b54ee533cade0d5d6999f)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("QuotaSpecificationLimitsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cdf2be715386f8dd50c7cb345a9579114e97f0260ea2a94845691a15c2d12699)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71b7eadf7730d58e6dc8183cb4a3c9220d142a48b575e09063a57b8f2428c13b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fef26bf2be2a8a73879a8b13dba8aecf45c9155e4a35f191649b3cb492640f2b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[QuotaSpecificationLimits]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[QuotaSpecificationLimits]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[QuotaSpecificationLimits]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b384d70ce706f24e006838739b5f880566cec858fa548f62b26c15b111ce735)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class QuotaSpecificationLimitsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.quotaSpecification.QuotaSpecificationLimitsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86acaf5a7605d28994bbab5d6aeaa050339d009c9d61ed89eb1d12d617f293f0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putRegionLimit")
    def put_region_limit(
        self,
        *,
        cpu: typing.Optional[jsii.Number] = None,
        memory_mb: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param cpu: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/quota_specification#cpu QuotaSpecification#cpu}.
        :param memory_mb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/quota_specification#memory_mb QuotaSpecification#memory_mb}.
        '''
        value = QuotaSpecificationLimitsRegionLimit(cpu=cpu, memory_mb=memory_mb)

        return typing.cast(None, jsii.invoke(self, "putRegionLimit", [value]))

    @builtins.property
    @jsii.member(jsii_name="regionLimit")
    def region_limit(self) -> "QuotaSpecificationLimitsRegionLimitOutputReference":
        return typing.cast("QuotaSpecificationLimitsRegionLimitOutputReference", jsii.get(self, "regionLimit"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="regionLimitInput")
    def region_limit_input(
        self,
    ) -> typing.Optional["QuotaSpecificationLimitsRegionLimit"]:
        return typing.cast(typing.Optional["QuotaSpecificationLimitsRegionLimit"], jsii.get(self, "regionLimitInput"))

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf931ffeea636623bc8f641858f746338dcbcda98295a8e6f59db614eac360f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[QuotaSpecificationLimits, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[QuotaSpecificationLimits, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[QuotaSpecificationLimits, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a702d8acebd3ad79137218c609a197a461758c9d14e0efaa2c3f25e36a960515)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-nomad.quotaSpecification.QuotaSpecificationLimitsRegionLimit",
    jsii_struct_bases=[],
    name_mapping={"cpu": "cpu", "memory_mb": "memoryMb"},
)
class QuotaSpecificationLimitsRegionLimit:
    def __init__(
        self,
        *,
        cpu: typing.Optional[jsii.Number] = None,
        memory_mb: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param cpu: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/quota_specification#cpu QuotaSpecification#cpu}.
        :param memory_mb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/quota_specification#memory_mb QuotaSpecification#memory_mb}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb2c774fec44fdef15550af04c0defda44df7373af4c89bbbe5ca8ecc225a88f)
            check_type(argname="argument cpu", value=cpu, expected_type=type_hints["cpu"])
            check_type(argname="argument memory_mb", value=memory_mb, expected_type=type_hints["memory_mb"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cpu is not None:
            self._values["cpu"] = cpu
        if memory_mb is not None:
            self._values["memory_mb"] = memory_mb

    @builtins.property
    def cpu(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/quota_specification#cpu QuotaSpecification#cpu}.'''
        result = self._values.get("cpu")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def memory_mb(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/quota_specification#memory_mb QuotaSpecification#memory_mb}.'''
        result = self._values.get("memory_mb")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "QuotaSpecificationLimitsRegionLimit(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class QuotaSpecificationLimitsRegionLimitOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.quotaSpecification.QuotaSpecificationLimitsRegionLimitOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__beb562575e966ab003a3af30589fd6370d1ec3590f54d4fc2997161ec6ae98a4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCpu")
    def reset_cpu(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCpu", []))

    @jsii.member(jsii_name="resetMemoryMb")
    def reset_memory_mb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMemoryMb", []))

    @builtins.property
    @jsii.member(jsii_name="cpuInput")
    def cpu_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "cpuInput"))

    @builtins.property
    @jsii.member(jsii_name="memoryMbInput")
    def memory_mb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "memoryMbInput"))

    @builtins.property
    @jsii.member(jsii_name="cpu")
    def cpu(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cpu"))

    @cpu.setter
    def cpu(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7243a6fd503dd60908ac33c63e0b25f5fbb1d47fb3d7ebface911500aad5591b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpu", value)

    @builtins.property
    @jsii.member(jsii_name="memoryMb")
    def memory_mb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "memoryMb"))

    @memory_mb.setter
    def memory_mb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__166d4bff1ea522a735244acd113a1900f20efb2b4cff4e258b49901910f44a5f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memoryMb", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[QuotaSpecificationLimitsRegionLimit]:
        return typing.cast(typing.Optional[QuotaSpecificationLimitsRegionLimit], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[QuotaSpecificationLimitsRegionLimit],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__169f09eea8db9a6cad4915c0a1f2e9fd406020b47aabd76150847d9962dac2ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "QuotaSpecification",
    "QuotaSpecificationConfig",
    "QuotaSpecificationLimits",
    "QuotaSpecificationLimitsList",
    "QuotaSpecificationLimitsOutputReference",
    "QuotaSpecificationLimitsRegionLimit",
    "QuotaSpecificationLimitsRegionLimitOutputReference",
]

publication.publish()

def _typecheckingstub__94f7f898ee7e9543c060b7c80ce5e18554dc44a4a4e6180aa607c19a8f128d5d(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    limits: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[QuotaSpecificationLimits, typing.Dict[builtins.str, typing.Any]]]],
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__68c8a5b25c8e960c0ec0576016f25e172527673a39a2105f0ad868b013efad9a(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[QuotaSpecificationLimits, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df6bcfce0fccd60dcd16673d3a4129092946c097ac55a94a7db9741ca7605f8d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2be5ed39974d0bed05a4928cf34117746e64cf8bb5e96f0a2439991ad2945ce(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c363c42648bc2ec743a9f5e73cd3f0a1dfc5e1827dc15c80a3164ba474b84266(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bbacac1608669777de5aa925508b8baa491a0beaf6e872b0375040fbf806252(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    limits: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[QuotaSpecificationLimits, typing.Dict[builtins.str, typing.Any]]]],
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__046cab3db18bfd2e688094ffdf93d01951feb11939f6d207109d226b05318751(
    *,
    region: builtins.str,
    region_limit: typing.Union[QuotaSpecificationLimitsRegionLimit, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d5ca69984a61765150d74df541f2b7b9645879ddc51be550cbcd42c36f7ab0c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce4d53ecb9d49be82f7d69c87dfea2184c144f08230b54ee533cade0d5d6999f(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdf2be715386f8dd50c7cb345a9579114e97f0260ea2a94845691a15c2d12699(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71b7eadf7730d58e6dc8183cb4a3c9220d142a48b575e09063a57b8f2428c13b(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fef26bf2be2a8a73879a8b13dba8aecf45c9155e4a35f191649b3cb492640f2b(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b384d70ce706f24e006838739b5f880566cec858fa548f62b26c15b111ce735(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[QuotaSpecificationLimits]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86acaf5a7605d28994bbab5d6aeaa050339d009c9d61ed89eb1d12d617f293f0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf931ffeea636623bc8f641858f746338dcbcda98295a8e6f59db614eac360f7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a702d8acebd3ad79137218c609a197a461758c9d14e0efaa2c3f25e36a960515(
    value: typing.Optional[typing.Union[QuotaSpecificationLimits, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb2c774fec44fdef15550af04c0defda44df7373af4c89bbbe5ca8ecc225a88f(
    *,
    cpu: typing.Optional[jsii.Number] = None,
    memory_mb: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__beb562575e966ab003a3af30589fd6370d1ec3590f54d4fc2997161ec6ae98a4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7243a6fd503dd60908ac33c63e0b25f5fbb1d47fb3d7ebface911500aad5591b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__166d4bff1ea522a735244acd113a1900f20efb2b4cff4e258b49901910f44a5f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__169f09eea8db9a6cad4915c0a1f2e9fd406020b47aabd76150847d9962dac2ab(
    value: typing.Optional[QuotaSpecificationLimitsRegionLimit],
) -> None:
    """Type checking stubs"""
    pass
