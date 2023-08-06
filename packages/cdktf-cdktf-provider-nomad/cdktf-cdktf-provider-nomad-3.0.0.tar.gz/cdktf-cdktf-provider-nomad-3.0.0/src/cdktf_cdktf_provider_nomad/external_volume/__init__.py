'''
# `nomad_external_volume`

Refer to the Terraform Registory for docs: [`nomad_external_volume`](https://www.terraform.io/docs/providers/nomad/r/external_volume).
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


class ExternalVolume(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.externalVolume.ExternalVolume",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/nomad/r/external_volume nomad_external_volume}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        capability: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ExternalVolumeCapability", typing.Dict[builtins.str, typing.Any]]]],
        name: builtins.str,
        plugin_id: builtins.str,
        volume_id: builtins.str,
        capacity_max: typing.Optional[builtins.str] = None,
        capacity_min: typing.Optional[builtins.str] = None,
        clone_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        mount_options: typing.Optional[typing.Union["ExternalVolumeMountOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        namespace: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        secrets: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        snapshot_id: typing.Optional[builtins.str] = None,
        topology_request: typing.Optional[typing.Union["ExternalVolumeTopologyRequest", typing.Dict[builtins.str, typing.Any]]] = None,
        type: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/nomad/r/external_volume nomad_external_volume} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param capability: capability block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#capability ExternalVolume#capability}
        :param name: The display name of the volume. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#name ExternalVolume#name}
        :param plugin_id: The ID of the CSI plugin that manages this volume. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#plugin_id ExternalVolume#plugin_id}
        :param volume_id: The unique ID of the volume, how jobs will refer to the volume. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#volume_id ExternalVolume#volume_id}
        :param capacity_max: Defines how large the volume can be. The storage provider may return a volume that is smaller than this value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#capacity_max ExternalVolume#capacity_max}
        :param capacity_min: Defines how small the volume can be. The storage provider may return a volume that is larger than this value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#capacity_min ExternalVolume#capacity_min}
        :param clone_id: The volume ID to clone when creating this volume. Storage provider must support cloning. Conflicts with 'snapshot_id'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#clone_id ExternalVolume#clone_id}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#id ExternalVolume#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param mount_options: mount_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#mount_options ExternalVolume#mount_options}
        :param namespace: The namespace in which to create the volume. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#namespace ExternalVolume#namespace}
        :param parameters: An optional key-value map of strings passed directly to the CSI plugin to configure the volume. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#parameters ExternalVolume#parameters}
        :param secrets: An optional key-value map of strings used as credentials for publishing and unpublishing volumes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#secrets ExternalVolume#secrets}
        :param snapshot_id: The snapshot ID to restore when creating this volume. Storage provider must support snapshots. Conflicts with 'clone_id'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#snapshot_id ExternalVolume#snapshot_id}
        :param topology_request: topology_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#topology_request ExternalVolume#topology_request}
        :param type: The type of the volume. Currently, only 'csi' is supported. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#type ExternalVolume#type}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d002996b5da22241684eeccafdd3e215b4fee943223ee8a4e3412f27f6e5e7f9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ExternalVolumeConfig(
            capability=capability,
            name=name,
            plugin_id=plugin_id,
            volume_id=volume_id,
            capacity_max=capacity_max,
            capacity_min=capacity_min,
            clone_id=clone_id,
            id=id,
            mount_options=mount_options,
            namespace=namespace,
            parameters=parameters,
            secrets=secrets,
            snapshot_id=snapshot_id,
            topology_request=topology_request,
            type=type,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putCapability")
    def put_capability(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ExternalVolumeCapability", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7401bf4226d343ca87c5f6ac3d4ce36260013f26fe2529fd4c5973e3506c8ca8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCapability", [value]))

    @jsii.member(jsii_name="putMountOptions")
    def put_mount_options(
        self,
        *,
        fs_type: typing.Optional[builtins.str] = None,
        mount_flags: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param fs_type: The file system type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#fs_type ExternalVolume#fs_type}
        :param mount_flags: The flags passed to mount. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#mount_flags ExternalVolume#mount_flags}
        '''
        value = ExternalVolumeMountOptions(fs_type=fs_type, mount_flags=mount_flags)

        return typing.cast(None, jsii.invoke(self, "putMountOptions", [value]))

    @jsii.member(jsii_name="putTopologyRequest")
    def put_topology_request(
        self,
        *,
        preferred: typing.Optional[typing.Union["ExternalVolumeTopologyRequestPreferred", typing.Dict[builtins.str, typing.Any]]] = None,
        required: typing.Optional[typing.Union["ExternalVolumeTopologyRequestRequired", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param preferred: preferred block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#preferred ExternalVolume#preferred}
        :param required: required block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#required ExternalVolume#required}
        '''
        value = ExternalVolumeTopologyRequest(preferred=preferred, required=required)

        return typing.cast(None, jsii.invoke(self, "putTopologyRequest", [value]))

    @jsii.member(jsii_name="resetCapacityMax")
    def reset_capacity_max(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCapacityMax", []))

    @jsii.member(jsii_name="resetCapacityMin")
    def reset_capacity_min(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCapacityMin", []))

    @jsii.member(jsii_name="resetCloneId")
    def reset_clone_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloneId", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMountOptions")
    def reset_mount_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMountOptions", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @jsii.member(jsii_name="resetParameters")
    def reset_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameters", []))

    @jsii.member(jsii_name="resetSecrets")
    def reset_secrets(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecrets", []))

    @jsii.member(jsii_name="resetSnapshotId")
    def reset_snapshot_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSnapshotId", []))

    @jsii.member(jsii_name="resetTopologyRequest")
    def reset_topology_request(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTopologyRequest", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="capability")
    def capability(self) -> "ExternalVolumeCapabilityList":
        return typing.cast("ExternalVolumeCapabilityList", jsii.get(self, "capability"))

    @builtins.property
    @jsii.member(jsii_name="controllerRequired")
    def controller_required(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "controllerRequired"))

    @builtins.property
    @jsii.member(jsii_name="controllersExpected")
    def controllers_expected(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "controllersExpected"))

    @builtins.property
    @jsii.member(jsii_name="controllersHealthy")
    def controllers_healthy(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "controllersHealthy"))

    @builtins.property
    @jsii.member(jsii_name="mountOptions")
    def mount_options(self) -> "ExternalVolumeMountOptionsOutputReference":
        return typing.cast("ExternalVolumeMountOptionsOutputReference", jsii.get(self, "mountOptions"))

    @builtins.property
    @jsii.member(jsii_name="nodesExpected")
    def nodes_expected(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "nodesExpected"))

    @builtins.property
    @jsii.member(jsii_name="nodesHealthy")
    def nodes_healthy(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "nodesHealthy"))

    @builtins.property
    @jsii.member(jsii_name="pluginProvider")
    def plugin_provider(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pluginProvider"))

    @builtins.property
    @jsii.member(jsii_name="pluginProviderVersion")
    def plugin_provider_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pluginProviderVersion"))

    @builtins.property
    @jsii.member(jsii_name="schedulable")
    def schedulable(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "schedulable"))

    @builtins.property
    @jsii.member(jsii_name="topologies")
    def topologies(self) -> "ExternalVolumeTopologiesList":
        return typing.cast("ExternalVolumeTopologiesList", jsii.get(self, "topologies"))

    @builtins.property
    @jsii.member(jsii_name="topologyRequest")
    def topology_request(self) -> "ExternalVolumeTopologyRequestOutputReference":
        return typing.cast("ExternalVolumeTopologyRequestOutputReference", jsii.get(self, "topologyRequest"))

    @builtins.property
    @jsii.member(jsii_name="capabilityInput")
    def capability_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ExternalVolumeCapability"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ExternalVolumeCapability"]]], jsii.get(self, "capabilityInput"))

    @builtins.property
    @jsii.member(jsii_name="capacityMaxInput")
    def capacity_max_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "capacityMaxInput"))

    @builtins.property
    @jsii.member(jsii_name="capacityMinInput")
    def capacity_min_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "capacityMinInput"))

    @builtins.property
    @jsii.member(jsii_name="cloneIdInput")
    def clone_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cloneIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="mountOptionsInput")
    def mount_options_input(self) -> typing.Optional["ExternalVolumeMountOptions"]:
        return typing.cast(typing.Optional["ExternalVolumeMountOptions"], jsii.get(self, "mountOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="parametersInput")
    def parameters_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "parametersInput"))

    @builtins.property
    @jsii.member(jsii_name="pluginIdInput")
    def plugin_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pluginIdInput"))

    @builtins.property
    @jsii.member(jsii_name="secretsInput")
    def secrets_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "secretsInput"))

    @builtins.property
    @jsii.member(jsii_name="snapshotIdInput")
    def snapshot_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "snapshotIdInput"))

    @builtins.property
    @jsii.member(jsii_name="topologyRequestInput")
    def topology_request_input(
        self,
    ) -> typing.Optional["ExternalVolumeTopologyRequest"]:
        return typing.cast(typing.Optional["ExternalVolumeTopologyRequest"], jsii.get(self, "topologyRequestInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeIdInput")
    def volume_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "volumeIdInput"))

    @builtins.property
    @jsii.member(jsii_name="capacityMax")
    def capacity_max(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "capacityMax"))

    @capacity_max.setter
    def capacity_max(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d8f748b046ae4c35af1305a4aa421efdb1323d509ff0ba39085b894687e0f2c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "capacityMax", value)

    @builtins.property
    @jsii.member(jsii_name="capacityMin")
    def capacity_min(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "capacityMin"))

    @capacity_min.setter
    def capacity_min(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3dcfd23532928dda2e18bfd88ac3372fddab8cea4a0ae0b8bb851d3c0c73cdd8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "capacityMin", value)

    @builtins.property
    @jsii.member(jsii_name="cloneId")
    def clone_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloneId"))

    @clone_id.setter
    def clone_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__107ab3b252539b7a6392cd66d8bdf186b3f13523bf5de35ec834b3960895ee2d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloneId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b67fa79364c3dbda91a53cb0c2e54f296403d0fa7a7e82dbf48b04064f981129)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bfbaf0c9613421ab722cb89459a2061254852de12ed48d1180ea32f140bf45a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05a6701185c89fdddf639db6858430931dad3fb3479ee0521ed503032af631f0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b5976e86bbd34b407410518368b0a97b568d014abbc9f6bc15e87d38eb72dfe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="pluginId")
    def plugin_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pluginId"))

    @plugin_id.setter
    def plugin_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3829ac6f7a004824ed269a292fd1f3293833f83bc157e17a8821423bc7c4c9b3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pluginId", value)

    @builtins.property
    @jsii.member(jsii_name="secrets")
    def secrets(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "secrets"))

    @secrets.setter
    def secrets(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__506701013d4b5beef2f2f34e041140b600f8b15f352c84053248544d1f26fc15)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secrets", value)

    @builtins.property
    @jsii.member(jsii_name="snapshotId")
    def snapshot_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "snapshotId"))

    @snapshot_id.setter
    def snapshot_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__289cad766ff83cb80de5422a63f2e886b7e1d6794bf5a95511705fcbda0c5ca0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotId", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b8a4f70e12633a55f191398badeb164069918345b0e10d2fe1c307e970f5be4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="volumeId")
    def volume_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volumeId"))

    @volume_id.setter
    def volume_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78c8bf974bd47ef5b023c32fdd3898d810f7fb759aed311e67fcbc8cee39cc69)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-nomad.externalVolume.ExternalVolumeCapability",
    jsii_struct_bases=[],
    name_mapping={"access_mode": "accessMode", "attachment_mode": "attachmentMode"},
)
class ExternalVolumeCapability:
    def __init__(
        self,
        *,
        access_mode: builtins.str,
        attachment_mode: builtins.str,
    ) -> None:
        '''
        :param access_mode: Defines whether a volume should be available concurrently. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#access_mode ExternalVolume#access_mode}
        :param attachment_mode: The storage API that will be used by the volume. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#attachment_mode ExternalVolume#attachment_mode}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eef56ee2021e0f6b876e4088399075c751c2c52807eec2b390180c9cae5303ba)
            check_type(argname="argument access_mode", value=access_mode, expected_type=type_hints["access_mode"])
            check_type(argname="argument attachment_mode", value=attachment_mode, expected_type=type_hints["attachment_mode"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "access_mode": access_mode,
            "attachment_mode": attachment_mode,
        }

    @builtins.property
    def access_mode(self) -> builtins.str:
        '''Defines whether a volume should be available concurrently.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#access_mode ExternalVolume#access_mode}
        '''
        result = self._values.get("access_mode")
        assert result is not None, "Required property 'access_mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def attachment_mode(self) -> builtins.str:
        '''The storage API that will be used by the volume.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#attachment_mode ExternalVolume#attachment_mode}
        '''
        result = self._values.get("attachment_mode")
        assert result is not None, "Required property 'attachment_mode' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalVolumeCapability(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ExternalVolumeCapabilityList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.externalVolume.ExternalVolumeCapabilityList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7b46c5df8a568d77226e55f0aef3dd69498b100385b15a12e6047c813aebda98)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ExternalVolumeCapabilityOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46c7627e214aa7b2071431dfebc8f7da2a717c5b39dab355f7774c9875bd95aa)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ExternalVolumeCapabilityOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e122ec1e61862fdd5588346fb072599fca98fa02d4920731cef99156b3aec0fa)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e8853633c68f9eb2dd226dae8aaeddb3a53feed020c159e1e87141a07a531c1a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ed82ee76c57dc955b031dc2e81b71559249d72cdfc6a14cf4dcfb1d8703e0103)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ExternalVolumeCapability]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ExternalVolumeCapability]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ExternalVolumeCapability]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a02bc4fc8af04b94e9e56fd0a804719d8e55b6f4f99db31747836377d03d0341)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ExternalVolumeCapabilityOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.externalVolume.ExternalVolumeCapabilityOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__933e32a237777ed6ad2ee9bc173f0a165171cddef5035fadde3f0eea031a6324)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="accessModeInput")
    def access_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessModeInput"))

    @builtins.property
    @jsii.member(jsii_name="attachmentModeInput")
    def attachment_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "attachmentModeInput"))

    @builtins.property
    @jsii.member(jsii_name="accessMode")
    def access_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessMode"))

    @access_mode.setter
    def access_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f680b1760b116dfea955075623d119c09dfa2885167c9d7c7dc36cacc92fa6c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessMode", value)

    @builtins.property
    @jsii.member(jsii_name="attachmentMode")
    def attachment_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "attachmentMode"))

    @attachment_mode.setter
    def attachment_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18232a4af7b6afaf35d18726935b7f259d59c88bd9a330a731450e611fc6ce80)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attachmentMode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ExternalVolumeCapability, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ExternalVolumeCapability, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ExternalVolumeCapability, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec80bebdb5db4059b0d33c455eae45949fdf85992a10535f9d7c11094c8b2adc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-nomad.externalVolume.ExternalVolumeConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "capability": "capability",
        "name": "name",
        "plugin_id": "pluginId",
        "volume_id": "volumeId",
        "capacity_max": "capacityMax",
        "capacity_min": "capacityMin",
        "clone_id": "cloneId",
        "id": "id",
        "mount_options": "mountOptions",
        "namespace": "namespace",
        "parameters": "parameters",
        "secrets": "secrets",
        "snapshot_id": "snapshotId",
        "topology_request": "topologyRequest",
        "type": "type",
    },
)
class ExternalVolumeConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        capability: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ExternalVolumeCapability, typing.Dict[builtins.str, typing.Any]]]],
        name: builtins.str,
        plugin_id: builtins.str,
        volume_id: builtins.str,
        capacity_max: typing.Optional[builtins.str] = None,
        capacity_min: typing.Optional[builtins.str] = None,
        clone_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        mount_options: typing.Optional[typing.Union["ExternalVolumeMountOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        namespace: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        secrets: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        snapshot_id: typing.Optional[builtins.str] = None,
        topology_request: typing.Optional[typing.Union["ExternalVolumeTopologyRequest", typing.Dict[builtins.str, typing.Any]]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param capability: capability block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#capability ExternalVolume#capability}
        :param name: The display name of the volume. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#name ExternalVolume#name}
        :param plugin_id: The ID of the CSI plugin that manages this volume. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#plugin_id ExternalVolume#plugin_id}
        :param volume_id: The unique ID of the volume, how jobs will refer to the volume. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#volume_id ExternalVolume#volume_id}
        :param capacity_max: Defines how large the volume can be. The storage provider may return a volume that is smaller than this value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#capacity_max ExternalVolume#capacity_max}
        :param capacity_min: Defines how small the volume can be. The storage provider may return a volume that is larger than this value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#capacity_min ExternalVolume#capacity_min}
        :param clone_id: The volume ID to clone when creating this volume. Storage provider must support cloning. Conflicts with 'snapshot_id'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#clone_id ExternalVolume#clone_id}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#id ExternalVolume#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param mount_options: mount_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#mount_options ExternalVolume#mount_options}
        :param namespace: The namespace in which to create the volume. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#namespace ExternalVolume#namespace}
        :param parameters: An optional key-value map of strings passed directly to the CSI plugin to configure the volume. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#parameters ExternalVolume#parameters}
        :param secrets: An optional key-value map of strings used as credentials for publishing and unpublishing volumes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#secrets ExternalVolume#secrets}
        :param snapshot_id: The snapshot ID to restore when creating this volume. Storage provider must support snapshots. Conflicts with 'clone_id'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#snapshot_id ExternalVolume#snapshot_id}
        :param topology_request: topology_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#topology_request ExternalVolume#topology_request}
        :param type: The type of the volume. Currently, only 'csi' is supported. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#type ExternalVolume#type}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(mount_options, dict):
            mount_options = ExternalVolumeMountOptions(**mount_options)
        if isinstance(topology_request, dict):
            topology_request = ExternalVolumeTopologyRequest(**topology_request)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b7e1ab3b5b3e528078e47a1078a3235f757c4ded1c3e28f98f2bf52b3c6ce05)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument capability", value=capability, expected_type=type_hints["capability"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument plugin_id", value=plugin_id, expected_type=type_hints["plugin_id"])
            check_type(argname="argument volume_id", value=volume_id, expected_type=type_hints["volume_id"])
            check_type(argname="argument capacity_max", value=capacity_max, expected_type=type_hints["capacity_max"])
            check_type(argname="argument capacity_min", value=capacity_min, expected_type=type_hints["capacity_min"])
            check_type(argname="argument clone_id", value=clone_id, expected_type=type_hints["clone_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument mount_options", value=mount_options, expected_type=type_hints["mount_options"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument secrets", value=secrets, expected_type=type_hints["secrets"])
            check_type(argname="argument snapshot_id", value=snapshot_id, expected_type=type_hints["snapshot_id"])
            check_type(argname="argument topology_request", value=topology_request, expected_type=type_hints["topology_request"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "capability": capability,
            "name": name,
            "plugin_id": plugin_id,
            "volume_id": volume_id,
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
        if capacity_max is not None:
            self._values["capacity_max"] = capacity_max
        if capacity_min is not None:
            self._values["capacity_min"] = capacity_min
        if clone_id is not None:
            self._values["clone_id"] = clone_id
        if id is not None:
            self._values["id"] = id
        if mount_options is not None:
            self._values["mount_options"] = mount_options
        if namespace is not None:
            self._values["namespace"] = namespace
        if parameters is not None:
            self._values["parameters"] = parameters
        if secrets is not None:
            self._values["secrets"] = secrets
        if snapshot_id is not None:
            self._values["snapshot_id"] = snapshot_id
        if topology_request is not None:
            self._values["topology_request"] = topology_request
        if type is not None:
            self._values["type"] = type

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
    def capability(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ExternalVolumeCapability]]:
        '''capability block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#capability ExternalVolume#capability}
        '''
        result = self._values.get("capability")
        assert result is not None, "Required property 'capability' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ExternalVolumeCapability]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The display name of the volume.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#name ExternalVolume#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def plugin_id(self) -> builtins.str:
        '''The ID of the CSI plugin that manages this volume.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#plugin_id ExternalVolume#plugin_id}
        '''
        result = self._values.get("plugin_id")
        assert result is not None, "Required property 'plugin_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def volume_id(self) -> builtins.str:
        '''The unique ID of the volume, how jobs will refer to the volume.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#volume_id ExternalVolume#volume_id}
        '''
        result = self._values.get("volume_id")
        assert result is not None, "Required property 'volume_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def capacity_max(self) -> typing.Optional[builtins.str]:
        '''Defines how large the volume can be.

        The storage provider may return a volume that is smaller than this value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#capacity_max ExternalVolume#capacity_max}
        '''
        result = self._values.get("capacity_max")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def capacity_min(self) -> typing.Optional[builtins.str]:
        '''Defines how small the volume can be.

        The storage provider may return a volume that is larger than this value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#capacity_min ExternalVolume#capacity_min}
        '''
        result = self._values.get("capacity_min")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def clone_id(self) -> typing.Optional[builtins.str]:
        '''The volume ID to clone when creating this volume. Storage provider must support cloning. Conflicts with 'snapshot_id'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#clone_id ExternalVolume#clone_id}
        '''
        result = self._values.get("clone_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#id ExternalVolume#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mount_options(self) -> typing.Optional["ExternalVolumeMountOptions"]:
        '''mount_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#mount_options ExternalVolume#mount_options}
        '''
        result = self._values.get("mount_options")
        return typing.cast(typing.Optional["ExternalVolumeMountOptions"], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''The namespace in which to create the volume.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#namespace ExternalVolume#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameters(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''An optional key-value map of strings passed directly to the CSI plugin to configure the volume.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#parameters ExternalVolume#parameters}
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def secrets(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''An optional key-value map of strings used as credentials for publishing and unpublishing volumes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#secrets ExternalVolume#secrets}
        '''
        result = self._values.get("secrets")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def snapshot_id(self) -> typing.Optional[builtins.str]:
        '''The snapshot ID to restore when creating this volume. Storage provider must support snapshots. Conflicts with 'clone_id'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#snapshot_id ExternalVolume#snapshot_id}
        '''
        result = self._values.get("snapshot_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def topology_request(self) -> typing.Optional["ExternalVolumeTopologyRequest"]:
        '''topology_request block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#topology_request ExternalVolume#topology_request}
        '''
        result = self._values.get("topology_request")
        return typing.cast(typing.Optional["ExternalVolumeTopologyRequest"], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''The type of the volume. Currently, only 'csi' is supported.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#type ExternalVolume#type}
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalVolumeConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-nomad.externalVolume.ExternalVolumeMountOptions",
    jsii_struct_bases=[],
    name_mapping={"fs_type": "fsType", "mount_flags": "mountFlags"},
)
class ExternalVolumeMountOptions:
    def __init__(
        self,
        *,
        fs_type: typing.Optional[builtins.str] = None,
        mount_flags: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param fs_type: The file system type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#fs_type ExternalVolume#fs_type}
        :param mount_flags: The flags passed to mount. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#mount_flags ExternalVolume#mount_flags}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cae5722437a1cfcfaa567da19c8e0e2145693d4846fd79bff0dd3deb4c599539)
            check_type(argname="argument fs_type", value=fs_type, expected_type=type_hints["fs_type"])
            check_type(argname="argument mount_flags", value=mount_flags, expected_type=type_hints["mount_flags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if fs_type is not None:
            self._values["fs_type"] = fs_type
        if mount_flags is not None:
            self._values["mount_flags"] = mount_flags

    @builtins.property
    def fs_type(self) -> typing.Optional[builtins.str]:
        '''The file system type.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#fs_type ExternalVolume#fs_type}
        '''
        result = self._values.get("fs_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mount_flags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The flags passed to mount.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#mount_flags ExternalVolume#mount_flags}
        '''
        result = self._values.get("mount_flags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalVolumeMountOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ExternalVolumeMountOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.externalVolume.ExternalVolumeMountOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__499e25812068bfab684de486095281912a4c55f58efc68b56bf82404fa8fab7f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFsType")
    def reset_fs_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFsType", []))

    @jsii.member(jsii_name="resetMountFlags")
    def reset_mount_flags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMountFlags", []))

    @builtins.property
    @jsii.member(jsii_name="fsTypeInput")
    def fs_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fsTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="mountFlagsInput")
    def mount_flags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "mountFlagsInput"))

    @builtins.property
    @jsii.member(jsii_name="fsType")
    def fs_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fsType"))

    @fs_type.setter
    def fs_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__abbe5292bf8b641022700de86e79747ae32007415305a258ab5823c390e12fe1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fsType", value)

    @builtins.property
    @jsii.member(jsii_name="mountFlags")
    def mount_flags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "mountFlags"))

    @mount_flags.setter
    def mount_flags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8cbe27958debcde8ffe43d29ad0d9c09e62ea23a3c74b5ac26e8832c7a4c262)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mountFlags", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ExternalVolumeMountOptions]:
        return typing.cast(typing.Optional[ExternalVolumeMountOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ExternalVolumeMountOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7530b69707f58c44e6b190fe7b9a41b64f62f0412ba5c52bad5ab2ea01786ba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-nomad.externalVolume.ExternalVolumeTopologies",
    jsii_struct_bases=[],
    name_mapping={},
)
class ExternalVolumeTopologies:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalVolumeTopologies(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ExternalVolumeTopologiesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.externalVolume.ExternalVolumeTopologiesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__522f9f079d58eb08826b4293524a668f43065de869c43c9d28cce06b78d501cc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ExternalVolumeTopologiesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f885fcec7517fa9eb0393a08d942b952cce1017b6c8270de847eb16e7bcee01)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ExternalVolumeTopologiesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f07482076c0305917f067d7d2ab52f0a9147da3b15791689ed3b83a6afbc946)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7df7dbfb60e7e7de278ad87a5e25f0ea2e7fda8bea948277dd4a275f3d1c417c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f13626cc5254f16d8158fd9d2d86677bf9a017a83f4e6c3ca5499045148c6dbc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class ExternalVolumeTopologiesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.externalVolume.ExternalVolumeTopologiesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6710a12536c0ba75ea27bc5d8864d494e50b9e82f32e8d67adca7c06a5201ace)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="segments")
    def segments(self) -> _cdktf_9a9027ec.StringMap:
        return typing.cast(_cdktf_9a9027ec.StringMap, jsii.get(self, "segments"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ExternalVolumeTopologies]:
        return typing.cast(typing.Optional[ExternalVolumeTopologies], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ExternalVolumeTopologies]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e643e54c6b18312fd60bda40f23ac5348704dddb75761da73d3bc2917ac50b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-nomad.externalVolume.ExternalVolumeTopologyRequest",
    jsii_struct_bases=[],
    name_mapping={"preferred": "preferred", "required": "required"},
)
class ExternalVolumeTopologyRequest:
    def __init__(
        self,
        *,
        preferred: typing.Optional[typing.Union["ExternalVolumeTopologyRequestPreferred", typing.Dict[builtins.str, typing.Any]]] = None,
        required: typing.Optional[typing.Union["ExternalVolumeTopologyRequestRequired", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param preferred: preferred block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#preferred ExternalVolume#preferred}
        :param required: required block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#required ExternalVolume#required}
        '''
        if isinstance(preferred, dict):
            preferred = ExternalVolumeTopologyRequestPreferred(**preferred)
        if isinstance(required, dict):
            required = ExternalVolumeTopologyRequestRequired(**required)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef1b6ead6360f02853486c7deb75cccaae2e27685d9367fc7e90d66274b1451e)
            check_type(argname="argument preferred", value=preferred, expected_type=type_hints["preferred"])
            check_type(argname="argument required", value=required, expected_type=type_hints["required"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if preferred is not None:
            self._values["preferred"] = preferred
        if required is not None:
            self._values["required"] = required

    @builtins.property
    def preferred(self) -> typing.Optional["ExternalVolumeTopologyRequestPreferred"]:
        '''preferred block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#preferred ExternalVolume#preferred}
        '''
        result = self._values.get("preferred")
        return typing.cast(typing.Optional["ExternalVolumeTopologyRequestPreferred"], result)

    @builtins.property
    def required(self) -> typing.Optional["ExternalVolumeTopologyRequestRequired"]:
        '''required block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#required ExternalVolume#required}
        '''
        result = self._values.get("required")
        return typing.cast(typing.Optional["ExternalVolumeTopologyRequestRequired"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalVolumeTopologyRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ExternalVolumeTopologyRequestOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.externalVolume.ExternalVolumeTopologyRequestOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5a972b13d3af4c78a8b35dbd74625cc1250d9dce67397be644f280e060f3b9f9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putPreferred")
    def put_preferred(
        self,
        *,
        topology: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ExternalVolumeTopologyRequestPreferredTopology", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param topology: topology block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#topology ExternalVolume#topology}
        '''
        value = ExternalVolumeTopologyRequestPreferred(topology=topology)

        return typing.cast(None, jsii.invoke(self, "putPreferred", [value]))

    @jsii.member(jsii_name="putRequired")
    def put_required(
        self,
        *,
        topology: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ExternalVolumeTopologyRequestRequiredTopology", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param topology: topology block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#topology ExternalVolume#topology}
        '''
        value = ExternalVolumeTopologyRequestRequired(topology=topology)

        return typing.cast(None, jsii.invoke(self, "putRequired", [value]))

    @jsii.member(jsii_name="resetPreferred")
    def reset_preferred(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreferred", []))

    @jsii.member(jsii_name="resetRequired")
    def reset_required(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequired", []))

    @builtins.property
    @jsii.member(jsii_name="preferred")
    def preferred(self) -> "ExternalVolumeTopologyRequestPreferredOutputReference":
        return typing.cast("ExternalVolumeTopologyRequestPreferredOutputReference", jsii.get(self, "preferred"))

    @builtins.property
    @jsii.member(jsii_name="required")
    def required(self) -> "ExternalVolumeTopologyRequestRequiredOutputReference":
        return typing.cast("ExternalVolumeTopologyRequestRequiredOutputReference", jsii.get(self, "required"))

    @builtins.property
    @jsii.member(jsii_name="preferredInput")
    def preferred_input(
        self,
    ) -> typing.Optional["ExternalVolumeTopologyRequestPreferred"]:
        return typing.cast(typing.Optional["ExternalVolumeTopologyRequestPreferred"], jsii.get(self, "preferredInput"))

    @builtins.property
    @jsii.member(jsii_name="requiredInput")
    def required_input(
        self,
    ) -> typing.Optional["ExternalVolumeTopologyRequestRequired"]:
        return typing.cast(typing.Optional["ExternalVolumeTopologyRequestRequired"], jsii.get(self, "requiredInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ExternalVolumeTopologyRequest]:
        return typing.cast(typing.Optional[ExternalVolumeTopologyRequest], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ExternalVolumeTopologyRequest],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98e0ce0e45b564efadbb734f9914935e4594421a7ac22eb9c9914d478ac621bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-nomad.externalVolume.ExternalVolumeTopologyRequestPreferred",
    jsii_struct_bases=[],
    name_mapping={"topology": "topology"},
)
class ExternalVolumeTopologyRequestPreferred:
    def __init__(
        self,
        *,
        topology: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ExternalVolumeTopologyRequestPreferredTopology", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param topology: topology block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#topology ExternalVolume#topology}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c616ba5dc0196f03bfd1c72737cb2901e2b87697e063c7b78149dc628622b834)
            check_type(argname="argument topology", value=topology, expected_type=type_hints["topology"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "topology": topology,
        }

    @builtins.property
    def topology(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ExternalVolumeTopologyRequestPreferredTopology"]]:
        '''topology block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#topology ExternalVolume#topology}
        '''
        result = self._values.get("topology")
        assert result is not None, "Required property 'topology' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ExternalVolumeTopologyRequestPreferredTopology"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalVolumeTopologyRequestPreferred(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ExternalVolumeTopologyRequestPreferredOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.externalVolume.ExternalVolumeTopologyRequestPreferredOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e968f3b474715872feb67345ecb1ac146f78576a89a5195cb3e09f04b566ccd5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putTopology")
    def put_topology(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ExternalVolumeTopologyRequestPreferredTopology", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__feb3f1acb7125837f2ab6ad2b49d44e52db451833a136332fd858e5a50ef46ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTopology", [value]))

    @builtins.property
    @jsii.member(jsii_name="topology")
    def topology(self) -> "ExternalVolumeTopologyRequestPreferredTopologyList":
        return typing.cast("ExternalVolumeTopologyRequestPreferredTopologyList", jsii.get(self, "topology"))

    @builtins.property
    @jsii.member(jsii_name="topologyInput")
    def topology_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ExternalVolumeTopologyRequestPreferredTopology"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ExternalVolumeTopologyRequestPreferredTopology"]]], jsii.get(self, "topologyInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ExternalVolumeTopologyRequestPreferred]:
        return typing.cast(typing.Optional[ExternalVolumeTopologyRequestPreferred], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ExternalVolumeTopologyRequestPreferred],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fbfc68c16cb9d77eb4c6045cfb0b4c8e8688be7a6121fedd8128c1006e2d7d72)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-nomad.externalVolume.ExternalVolumeTopologyRequestPreferredTopology",
    jsii_struct_bases=[],
    name_mapping={"segments": "segments"},
)
class ExternalVolumeTopologyRequestPreferredTopology:
    def __init__(self, *, segments: typing.Mapping[builtins.str, builtins.str]) -> None:
        '''
        :param segments: Define the attributes for the topology request. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#segments ExternalVolume#segments}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d674a9a46dee127dbe9c0207fe6d4794cda9b6448fcb4d1e51c9a69b10e9323)
            check_type(argname="argument segments", value=segments, expected_type=type_hints["segments"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "segments": segments,
        }

    @builtins.property
    def segments(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''Define the attributes for the topology request.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#segments ExternalVolume#segments}
        '''
        result = self._values.get("segments")
        assert result is not None, "Required property 'segments' is missing"
        return typing.cast(typing.Mapping[builtins.str, builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalVolumeTopologyRequestPreferredTopology(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ExternalVolumeTopologyRequestPreferredTopologyList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.externalVolume.ExternalVolumeTopologyRequestPreferredTopologyList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__935d7a435d62994c297df54655c88aebe2b96f53c53f37ad5124eb39184321de)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ExternalVolumeTopologyRequestPreferredTopologyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f54d82aa69a8b76d5cd5155a1518d5fd4a20922f82c3e4b140dba4b9af51675a)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ExternalVolumeTopologyRequestPreferredTopologyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78c5923355b96d7d86bce1a6cc78610a3bce5882223f4db04f0807c183cf36e2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8ee510c2003d1a7cf7e18f9e3f7311921263fa6c4319b07779c52888862b3be6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__32b8807c77634c35c813a72989f0a426e8becb6e125bad28ff9ee67e59a0722d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ExternalVolumeTopologyRequestPreferredTopology]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ExternalVolumeTopologyRequestPreferredTopology]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ExternalVolumeTopologyRequestPreferredTopology]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1cc03cb877fc8d9c1382d111a0c59557629abbff2d6dc440af844b7b2959569)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ExternalVolumeTopologyRequestPreferredTopologyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.externalVolume.ExternalVolumeTopologyRequestPreferredTopologyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d1af2368bba6aef5e030ed32a1e64ff42897aed755dfdfb9551a785627faf2cb)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="segmentsInput")
    def segments_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "segmentsInput"))

    @builtins.property
    @jsii.member(jsii_name="segments")
    def segments(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "segments"))

    @segments.setter
    def segments(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__626752f8866586a95437d4b81c100262d4d73bc5434b201b99b2e6ae37c57283)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "segments", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ExternalVolumeTopologyRequestPreferredTopology, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ExternalVolumeTopologyRequestPreferredTopology, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ExternalVolumeTopologyRequestPreferredTopology, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a80a31c338397afb23845243e2517136e369847180ac1096b11178d3b96cecc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-nomad.externalVolume.ExternalVolumeTopologyRequestRequired",
    jsii_struct_bases=[],
    name_mapping={"topology": "topology"},
)
class ExternalVolumeTopologyRequestRequired:
    def __init__(
        self,
        *,
        topology: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ExternalVolumeTopologyRequestRequiredTopology", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param topology: topology block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#topology ExternalVolume#topology}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52be38be32d7d459be054e61bd9a9b9bc78006d5d7882c83e29057eec38c296a)
            check_type(argname="argument topology", value=topology, expected_type=type_hints["topology"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "topology": topology,
        }

    @builtins.property
    def topology(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ExternalVolumeTopologyRequestRequiredTopology"]]:
        '''topology block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#topology ExternalVolume#topology}
        '''
        result = self._values.get("topology")
        assert result is not None, "Required property 'topology' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ExternalVolumeTopologyRequestRequiredTopology"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalVolumeTopologyRequestRequired(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ExternalVolumeTopologyRequestRequiredOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.externalVolume.ExternalVolumeTopologyRequestRequiredOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__42b54769912d32b119b0d4a1c0d9b473573edbbc7e463ce077143c059d661448)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putTopology")
    def put_topology(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ExternalVolumeTopologyRequestRequiredTopology", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13a8b38030f1de86a78047a0b480448b11063ee0c14cbb728323bd02fa5b23e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTopology", [value]))

    @builtins.property
    @jsii.member(jsii_name="topology")
    def topology(self) -> "ExternalVolumeTopologyRequestRequiredTopologyList":
        return typing.cast("ExternalVolumeTopologyRequestRequiredTopologyList", jsii.get(self, "topology"))

    @builtins.property
    @jsii.member(jsii_name="topologyInput")
    def topology_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ExternalVolumeTopologyRequestRequiredTopology"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ExternalVolumeTopologyRequestRequiredTopology"]]], jsii.get(self, "topologyInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ExternalVolumeTopologyRequestRequired]:
        return typing.cast(typing.Optional[ExternalVolumeTopologyRequestRequired], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ExternalVolumeTopologyRequestRequired],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9d13a853105ba3e7943f2f96214c3562bd04caae8c4c624f3a253e0298aa83e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-nomad.externalVolume.ExternalVolumeTopologyRequestRequiredTopology",
    jsii_struct_bases=[],
    name_mapping={"segments": "segments"},
)
class ExternalVolumeTopologyRequestRequiredTopology:
    def __init__(self, *, segments: typing.Mapping[builtins.str, builtins.str]) -> None:
        '''
        :param segments: Define the attributes for the topology request. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#segments ExternalVolume#segments}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72f2114a9abbe766b99886b0f86178779fc416a5e2faa2a5cc77252daf54c6f5)
            check_type(argname="argument segments", value=segments, expected_type=type_hints["segments"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "segments": segments,
        }

    @builtins.property
    def segments(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''Define the attributes for the topology request.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/external_volume#segments ExternalVolume#segments}
        '''
        result = self._values.get("segments")
        assert result is not None, "Required property 'segments' is missing"
        return typing.cast(typing.Mapping[builtins.str, builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalVolumeTopologyRequestRequiredTopology(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ExternalVolumeTopologyRequestRequiredTopologyList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.externalVolume.ExternalVolumeTopologyRequestRequiredTopologyList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fbc171301699e2afc0c679b52bd33ab645661f66a3839f848b0ea5b15348377f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ExternalVolumeTopologyRequestRequiredTopologyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__078abe554d755b49379305530e3aefbba180922aef653e39a26e3fe515b84ace)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ExternalVolumeTopologyRequestRequiredTopologyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d08943b585b46aa868ec154178f95f06e7fab71bab026facda5cfb776b5ce300)
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
            type_hints = typing.get_type_hints(_typecheckingstub__fc988f80938130f54e6ea1cbda74c8c2d3006b0ac90d104d2d0ca838a0c2454f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__64956e19606d0ef7612e43423d54119bce24c8daa8138179f28120429894b416)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ExternalVolumeTopologyRequestRequiredTopology]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ExternalVolumeTopologyRequestRequiredTopology]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ExternalVolumeTopologyRequestRequiredTopology]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__173c06d32932284ea70e0cc44bd2742bf5cc2966b75d263f4750ee4f5362ef28)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ExternalVolumeTopologyRequestRequiredTopologyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.externalVolume.ExternalVolumeTopologyRequestRequiredTopologyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0529e1d34adeb404ab9ecef57260d31cf1431ddafbf54bb4455eb356bd4f0b88)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="segmentsInput")
    def segments_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "segmentsInput"))

    @builtins.property
    @jsii.member(jsii_name="segments")
    def segments(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "segments"))

    @segments.setter
    def segments(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b891c39f4dc1dea80aa2da1e2f4098f8c91b0b9c1f2dfaa415139b91340512df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "segments", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ExternalVolumeTopologyRequestRequiredTopology, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ExternalVolumeTopologyRequestRequiredTopology, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ExternalVolumeTopologyRequestRequiredTopology, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e260d35c5a047ce4f4b6be68a5dc79f67543c53d1381b0f802c407b9c9fa956e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ExternalVolume",
    "ExternalVolumeCapability",
    "ExternalVolumeCapabilityList",
    "ExternalVolumeCapabilityOutputReference",
    "ExternalVolumeConfig",
    "ExternalVolumeMountOptions",
    "ExternalVolumeMountOptionsOutputReference",
    "ExternalVolumeTopologies",
    "ExternalVolumeTopologiesList",
    "ExternalVolumeTopologiesOutputReference",
    "ExternalVolumeTopologyRequest",
    "ExternalVolumeTopologyRequestOutputReference",
    "ExternalVolumeTopologyRequestPreferred",
    "ExternalVolumeTopologyRequestPreferredOutputReference",
    "ExternalVolumeTopologyRequestPreferredTopology",
    "ExternalVolumeTopologyRequestPreferredTopologyList",
    "ExternalVolumeTopologyRequestPreferredTopologyOutputReference",
    "ExternalVolumeTopologyRequestRequired",
    "ExternalVolumeTopologyRequestRequiredOutputReference",
    "ExternalVolumeTopologyRequestRequiredTopology",
    "ExternalVolumeTopologyRequestRequiredTopologyList",
    "ExternalVolumeTopologyRequestRequiredTopologyOutputReference",
]

publication.publish()

def _typecheckingstub__d002996b5da22241684eeccafdd3e215b4fee943223ee8a4e3412f27f6e5e7f9(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    capability: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ExternalVolumeCapability, typing.Dict[builtins.str, typing.Any]]]],
    name: builtins.str,
    plugin_id: builtins.str,
    volume_id: builtins.str,
    capacity_max: typing.Optional[builtins.str] = None,
    capacity_min: typing.Optional[builtins.str] = None,
    clone_id: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    mount_options: typing.Optional[typing.Union[ExternalVolumeMountOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    namespace: typing.Optional[builtins.str] = None,
    parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    secrets: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    snapshot_id: typing.Optional[builtins.str] = None,
    topology_request: typing.Optional[typing.Union[ExternalVolumeTopologyRequest, typing.Dict[builtins.str, typing.Any]]] = None,
    type: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__7401bf4226d343ca87c5f6ac3d4ce36260013f26fe2529fd4c5973e3506c8ca8(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ExternalVolumeCapability, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d8f748b046ae4c35af1305a4aa421efdb1323d509ff0ba39085b894687e0f2c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3dcfd23532928dda2e18bfd88ac3372fddab8cea4a0ae0b8bb851d3c0c73cdd8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__107ab3b252539b7a6392cd66d8bdf186b3f13523bf5de35ec834b3960895ee2d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b67fa79364c3dbda91a53cb0c2e54f296403d0fa7a7e82dbf48b04064f981129(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfbaf0c9613421ab722cb89459a2061254852de12ed48d1180ea32f140bf45a8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05a6701185c89fdddf639db6858430931dad3fb3479ee0521ed503032af631f0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b5976e86bbd34b407410518368b0a97b568d014abbc9f6bc15e87d38eb72dfe(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3829ac6f7a004824ed269a292fd1f3293833f83bc157e17a8821423bc7c4c9b3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__506701013d4b5beef2f2f34e041140b600f8b15f352c84053248544d1f26fc15(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__289cad766ff83cb80de5422a63f2e886b7e1d6794bf5a95511705fcbda0c5ca0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b8a4f70e12633a55f191398badeb164069918345b0e10d2fe1c307e970f5be4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78c8bf974bd47ef5b023c32fdd3898d810f7fb759aed311e67fcbc8cee39cc69(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eef56ee2021e0f6b876e4088399075c751c2c52807eec2b390180c9cae5303ba(
    *,
    access_mode: builtins.str,
    attachment_mode: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b46c5df8a568d77226e55f0aef3dd69498b100385b15a12e6047c813aebda98(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46c7627e214aa7b2071431dfebc8f7da2a717c5b39dab355f7774c9875bd95aa(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e122ec1e61862fdd5588346fb072599fca98fa02d4920731cef99156b3aec0fa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8853633c68f9eb2dd226dae8aaeddb3a53feed020c159e1e87141a07a531c1a(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed82ee76c57dc955b031dc2e81b71559249d72cdfc6a14cf4dcfb1d8703e0103(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a02bc4fc8af04b94e9e56fd0a804719d8e55b6f4f99db31747836377d03d0341(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ExternalVolumeCapability]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__933e32a237777ed6ad2ee9bc173f0a165171cddef5035fadde3f0eea031a6324(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f680b1760b116dfea955075623d119c09dfa2885167c9d7c7dc36cacc92fa6c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18232a4af7b6afaf35d18726935b7f259d59c88bd9a330a731450e611fc6ce80(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec80bebdb5db4059b0d33c455eae45949fdf85992a10535f9d7c11094c8b2adc(
    value: typing.Optional[typing.Union[ExternalVolumeCapability, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b7e1ab3b5b3e528078e47a1078a3235f757c4ded1c3e28f98f2bf52b3c6ce05(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    capability: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ExternalVolumeCapability, typing.Dict[builtins.str, typing.Any]]]],
    name: builtins.str,
    plugin_id: builtins.str,
    volume_id: builtins.str,
    capacity_max: typing.Optional[builtins.str] = None,
    capacity_min: typing.Optional[builtins.str] = None,
    clone_id: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    mount_options: typing.Optional[typing.Union[ExternalVolumeMountOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    namespace: typing.Optional[builtins.str] = None,
    parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    secrets: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    snapshot_id: typing.Optional[builtins.str] = None,
    topology_request: typing.Optional[typing.Union[ExternalVolumeTopologyRequest, typing.Dict[builtins.str, typing.Any]]] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cae5722437a1cfcfaa567da19c8e0e2145693d4846fd79bff0dd3deb4c599539(
    *,
    fs_type: typing.Optional[builtins.str] = None,
    mount_flags: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__499e25812068bfab684de486095281912a4c55f58efc68b56bf82404fa8fab7f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__abbe5292bf8b641022700de86e79747ae32007415305a258ab5823c390e12fe1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8cbe27958debcde8ffe43d29ad0d9c09e62ea23a3c74b5ac26e8832c7a4c262(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7530b69707f58c44e6b190fe7b9a41b64f62f0412ba5c52bad5ab2ea01786ba(
    value: typing.Optional[ExternalVolumeMountOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__522f9f079d58eb08826b4293524a668f43065de869c43c9d28cce06b78d501cc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f885fcec7517fa9eb0393a08d942b952cce1017b6c8270de847eb16e7bcee01(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f07482076c0305917f067d7d2ab52f0a9147da3b15791689ed3b83a6afbc946(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7df7dbfb60e7e7de278ad87a5e25f0ea2e7fda8bea948277dd4a275f3d1c417c(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f13626cc5254f16d8158fd9d2d86677bf9a017a83f4e6c3ca5499045148c6dbc(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6710a12536c0ba75ea27bc5d8864d494e50b9e82f32e8d67adca7c06a5201ace(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e643e54c6b18312fd60bda40f23ac5348704dddb75761da73d3bc2917ac50b9(
    value: typing.Optional[ExternalVolumeTopologies],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef1b6ead6360f02853486c7deb75cccaae2e27685d9367fc7e90d66274b1451e(
    *,
    preferred: typing.Optional[typing.Union[ExternalVolumeTopologyRequestPreferred, typing.Dict[builtins.str, typing.Any]]] = None,
    required: typing.Optional[typing.Union[ExternalVolumeTopologyRequestRequired, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a972b13d3af4c78a8b35dbd74625cc1250d9dce67397be644f280e060f3b9f9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98e0ce0e45b564efadbb734f9914935e4594421a7ac22eb9c9914d478ac621bc(
    value: typing.Optional[ExternalVolumeTopologyRequest],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c616ba5dc0196f03bfd1c72737cb2901e2b87697e063c7b78149dc628622b834(
    *,
    topology: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ExternalVolumeTopologyRequestPreferredTopology, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e968f3b474715872feb67345ecb1ac146f78576a89a5195cb3e09f04b566ccd5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__feb3f1acb7125837f2ab6ad2b49d44e52db451833a136332fd858e5a50ef46ec(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ExternalVolumeTopologyRequestPreferredTopology, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fbfc68c16cb9d77eb4c6045cfb0b4c8e8688be7a6121fedd8128c1006e2d7d72(
    value: typing.Optional[ExternalVolumeTopologyRequestPreferred],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d674a9a46dee127dbe9c0207fe6d4794cda9b6448fcb4d1e51c9a69b10e9323(
    *,
    segments: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__935d7a435d62994c297df54655c88aebe2b96f53c53f37ad5124eb39184321de(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f54d82aa69a8b76d5cd5155a1518d5fd4a20922f82c3e4b140dba4b9af51675a(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78c5923355b96d7d86bce1a6cc78610a3bce5882223f4db04f0807c183cf36e2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ee510c2003d1a7cf7e18f9e3f7311921263fa6c4319b07779c52888862b3be6(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32b8807c77634c35c813a72989f0a426e8becb6e125bad28ff9ee67e59a0722d(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1cc03cb877fc8d9c1382d111a0c59557629abbff2d6dc440af844b7b2959569(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ExternalVolumeTopologyRequestPreferredTopology]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1af2368bba6aef5e030ed32a1e64ff42897aed755dfdfb9551a785627faf2cb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__626752f8866586a95437d4b81c100262d4d73bc5434b201b99b2e6ae37c57283(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a80a31c338397afb23845243e2517136e369847180ac1096b11178d3b96cecc(
    value: typing.Optional[typing.Union[ExternalVolumeTopologyRequestPreferredTopology, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52be38be32d7d459be054e61bd9a9b9bc78006d5d7882c83e29057eec38c296a(
    *,
    topology: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ExternalVolumeTopologyRequestRequiredTopology, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42b54769912d32b119b0d4a1c0d9b473573edbbc7e463ce077143c059d661448(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13a8b38030f1de86a78047a0b480448b11063ee0c14cbb728323bd02fa5b23e0(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ExternalVolumeTopologyRequestRequiredTopology, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9d13a853105ba3e7943f2f96214c3562bd04caae8c4c624f3a253e0298aa83e(
    value: typing.Optional[ExternalVolumeTopologyRequestRequired],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72f2114a9abbe766b99886b0f86178779fc416a5e2faa2a5cc77252daf54c6f5(
    *,
    segments: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fbc171301699e2afc0c679b52bd33ab645661f66a3839f848b0ea5b15348377f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__078abe554d755b49379305530e3aefbba180922aef653e39a26e3fe515b84ace(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d08943b585b46aa868ec154178f95f06e7fab71bab026facda5cfb776b5ce300(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc988f80938130f54e6ea1cbda74c8c2d3006b0ac90d104d2d0ca838a0c2454f(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64956e19606d0ef7612e43423d54119bce24c8daa8138179f28120429894b416(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__173c06d32932284ea70e0cc44bd2742bf5cc2966b75d263f4750ee4f5362ef28(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ExternalVolumeTopologyRequestRequiredTopology]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0529e1d34adeb404ab9ecef57260d31cf1431ddafbf54bb4455eb356bd4f0b88(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b891c39f4dc1dea80aa2da1e2f4098f8c91b0b9c1f2dfaa415139b91340512df(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e260d35c5a047ce4f4b6be68a5dc79f67543c53d1381b0f802c407b9c9fa956e(
    value: typing.Optional[typing.Union[ExternalVolumeTopologyRequestRequiredTopology, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
