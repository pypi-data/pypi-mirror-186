'''
# `nomad_volume`

Refer to the Terraform Registory for docs: [`nomad_volume`](https://www.terraform.io/docs/providers/nomad/r/volume).
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


class Volume(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.volume.Volume",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/nomad/r/volume nomad_volume}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        external_id: builtins.str,
        name: builtins.str,
        plugin_id: builtins.str,
        volume_id: builtins.str,
        access_mode: typing.Optional[builtins.str] = None,
        attachment_mode: typing.Optional[builtins.str] = None,
        capability: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["VolumeCapability", typing.Dict[builtins.str, typing.Any]]]]] = None,
        context: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        deregister_on_destroy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        mount_options: typing.Optional[typing.Union["VolumeMountOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        namespace: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        secrets: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        topology_request: typing.Optional[typing.Union["VolumeTopologyRequest", typing.Dict[builtins.str, typing.Any]]] = None,
        type: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/nomad/r/volume nomad_volume} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param external_id: The ID of the physical volume from the storage provider. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#external_id Volume#external_id}
        :param name: The display name of the volume. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#name Volume#name}
        :param plugin_id: The ID of the CSI plugin that manages this volume. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#plugin_id Volume#plugin_id}
        :param volume_id: The unique ID of the volume, how jobs will refer to the volume. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#volume_id Volume#volume_id}
        :param access_mode: Defines whether a volume should be available concurrently. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#access_mode Volume#access_mode}
        :param attachment_mode: The storage API that will be used by the volume. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#attachment_mode Volume#attachment_mode}
        :param capability: capability block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#capability Volume#capability}
        :param context: An optional key-value map of strings passed directly to the CSI plugin to validate the volume. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#context Volume#context}
        :param deregister_on_destroy: If true, the volume will be deregistered on destroy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#deregister_on_destroy Volume#deregister_on_destroy}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#id Volume#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param mount_options: mount_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#mount_options Volume#mount_options}
        :param namespace: The namespace in which to create the volume. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#namespace Volume#namespace}
        :param parameters: An optional key-value map of strings passed directly to the CSI plugin to configure the volume. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#parameters Volume#parameters}
        :param secrets: An optional key-value map of strings used as credentials for publishing and unpublishing volumes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#secrets Volume#secrets}
        :param topology_request: topology_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#topology_request Volume#topology_request}
        :param type: The type of the volume. Currently, only 'csi' is supported. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#type Volume#type}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce1738d87feac8e9e1545157cbd8c58279d22797d7adeda10c42e585f9bd4a7a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = VolumeConfig(
            external_id=external_id,
            name=name,
            plugin_id=plugin_id,
            volume_id=volume_id,
            access_mode=access_mode,
            attachment_mode=attachment_mode,
            capability=capability,
            context=context,
            deregister_on_destroy=deregister_on_destroy,
            id=id,
            mount_options=mount_options,
            namespace=namespace,
            parameters=parameters,
            secrets=secrets,
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
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["VolumeCapability", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a94b9cdf9b34a5704453223f4e466698ffc12852b97d21219469d79e32ca9eb2)
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
        :param fs_type: The file system type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#fs_type Volume#fs_type}
        :param mount_flags: The flags passed to mount. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#mount_flags Volume#mount_flags}
        '''
        value = VolumeMountOptions(fs_type=fs_type, mount_flags=mount_flags)

        return typing.cast(None, jsii.invoke(self, "putMountOptions", [value]))

    @jsii.member(jsii_name="putTopologyRequest")
    def put_topology_request(
        self,
        *,
        required: typing.Optional[typing.Union["VolumeTopologyRequestRequired", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param required: required block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#required Volume#required}
        '''
        value = VolumeTopologyRequest(required=required)

        return typing.cast(None, jsii.invoke(self, "putTopologyRequest", [value]))

    @jsii.member(jsii_name="resetAccessMode")
    def reset_access_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessMode", []))

    @jsii.member(jsii_name="resetAttachmentMode")
    def reset_attachment_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAttachmentMode", []))

    @jsii.member(jsii_name="resetCapability")
    def reset_capability(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCapability", []))

    @jsii.member(jsii_name="resetContext")
    def reset_context(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContext", []))

    @jsii.member(jsii_name="resetDeregisterOnDestroy")
    def reset_deregister_on_destroy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeregisterOnDestroy", []))

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
    def capability(self) -> "VolumeCapabilityList":
        return typing.cast("VolumeCapabilityList", jsii.get(self, "capability"))

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
    def mount_options(self) -> "VolumeMountOptionsOutputReference":
        return typing.cast("VolumeMountOptionsOutputReference", jsii.get(self, "mountOptions"))

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
    def topologies(self) -> "VolumeTopologiesList":
        return typing.cast("VolumeTopologiesList", jsii.get(self, "topologies"))

    @builtins.property
    @jsii.member(jsii_name="topologyRequest")
    def topology_request(self) -> "VolumeTopologyRequestOutputReference":
        return typing.cast("VolumeTopologyRequestOutputReference", jsii.get(self, "topologyRequest"))

    @builtins.property
    @jsii.member(jsii_name="accessModeInput")
    def access_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessModeInput"))

    @builtins.property
    @jsii.member(jsii_name="attachmentModeInput")
    def attachment_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "attachmentModeInput"))

    @builtins.property
    @jsii.member(jsii_name="capabilityInput")
    def capability_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["VolumeCapability"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["VolumeCapability"]]], jsii.get(self, "capabilityInput"))

    @builtins.property
    @jsii.member(jsii_name="contextInput")
    def context_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "contextInput"))

    @builtins.property
    @jsii.member(jsii_name="deregisterOnDestroyInput")
    def deregister_on_destroy_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "deregisterOnDestroyInput"))

    @builtins.property
    @jsii.member(jsii_name="externalIdInput")
    def external_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "externalIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="mountOptionsInput")
    def mount_options_input(self) -> typing.Optional["VolumeMountOptions"]:
        return typing.cast(typing.Optional["VolumeMountOptions"], jsii.get(self, "mountOptionsInput"))

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
    @jsii.member(jsii_name="topologyRequestInput")
    def topology_request_input(self) -> typing.Optional["VolumeTopologyRequest"]:
        return typing.cast(typing.Optional["VolumeTopologyRequest"], jsii.get(self, "topologyRequestInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeIdInput")
    def volume_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "volumeIdInput"))

    @builtins.property
    @jsii.member(jsii_name="accessMode")
    def access_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessMode"))

    @access_mode.setter
    def access_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e41c9c6e5cb5a4399f2546b5ae9696e431b4897ba1421f92da75531a87c1d792)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessMode", value)

    @builtins.property
    @jsii.member(jsii_name="attachmentMode")
    def attachment_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "attachmentMode"))

    @attachment_mode.setter
    def attachment_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__391dc8cef3ffd660a0221ac955a38fe317c59aa1049d58caac2caeb3f020c076)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attachmentMode", value)

    @builtins.property
    @jsii.member(jsii_name="context")
    def context(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "context"))

    @context.setter
    def context(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__597834f01ce828a73903e771575c144704fe5aa9c9b0de3c007a2c964945be71)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "context", value)

    @builtins.property
    @jsii.member(jsii_name="deregisterOnDestroy")
    def deregister_on_destroy(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "deregisterOnDestroy"))

    @deregister_on_destroy.setter
    def deregister_on_destroy(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__801b1447c48baf455cb46be475eaaa541628a34115cc6f1124c546cdeab601c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deregisterOnDestroy", value)

    @builtins.property
    @jsii.member(jsii_name="externalId")
    def external_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "externalId"))

    @external_id.setter
    def external_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__981eb4c9cb35dca99c423316b04b1555aa9cfd30fc55627349428c0cff0c6955)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "externalId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc694244171e62a3187221c5d42a301c0c2e72f78aab3aefc2c3a4082b06ee9d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19d6d2f34c09068788b1e6ccceeec6e26a6218291667bcbc63ca094f77e5c6ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be782c6336f7ecdb8d6158e16bab1775e9b5418788a1970e5c99d219f6932d5a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4f63c35e021d145560456dc295cb6800596a704b29091118ad96ca55912620a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="pluginId")
    def plugin_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pluginId"))

    @plugin_id.setter
    def plugin_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5c192456436ccfd5b5bb31650fc5e0638a684fb89dfb4ed610a27c516e73b52)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pluginId", value)

    @builtins.property
    @jsii.member(jsii_name="secrets")
    def secrets(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "secrets"))

    @secrets.setter
    def secrets(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__256106c554e294e4f598a94452d28e2bbfd833343751b347c438b41f51e50f6f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secrets", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85877411bfbb5082c4548a09b9e0694e43a010e3d1a19eaaaec462de22b671eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="volumeId")
    def volume_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volumeId"))

    @volume_id.setter
    def volume_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db6f8cbc03c044f50cccb7b0223392378d44895ae801499f9ac49bd23e847949)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-nomad.volume.VolumeCapability",
    jsii_struct_bases=[],
    name_mapping={"access_mode": "accessMode", "attachment_mode": "attachmentMode"},
)
class VolumeCapability:
    def __init__(
        self,
        *,
        access_mode: builtins.str,
        attachment_mode: builtins.str,
    ) -> None:
        '''
        :param access_mode: Defines whether a volume should be available concurrently. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#access_mode Volume#access_mode}
        :param attachment_mode: The storage API that will be used by the volume. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#attachment_mode Volume#attachment_mode}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82ff8d33b081ea2e1dd4c0781d9b593bc38991532a7cb78bfea7b13ccf673154)
            check_type(argname="argument access_mode", value=access_mode, expected_type=type_hints["access_mode"])
            check_type(argname="argument attachment_mode", value=attachment_mode, expected_type=type_hints["attachment_mode"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "access_mode": access_mode,
            "attachment_mode": attachment_mode,
        }

    @builtins.property
    def access_mode(self) -> builtins.str:
        '''Defines whether a volume should be available concurrently.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#access_mode Volume#access_mode}
        '''
        result = self._values.get("access_mode")
        assert result is not None, "Required property 'access_mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def attachment_mode(self) -> builtins.str:
        '''The storage API that will be used by the volume.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#attachment_mode Volume#attachment_mode}
        '''
        result = self._values.get("attachment_mode")
        assert result is not None, "Required property 'attachment_mode' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VolumeCapability(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VolumeCapabilityList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.volume.VolumeCapabilityList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__55b2956eec774b4639796178d26e85690dcf4f300ddb5a69055eb7b2c89d3c9a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "VolumeCapabilityOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e234d4428e3c677efa3f14cd7d034cdeb39f31450d2170cf53ea799659dbef8)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("VolumeCapabilityOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba253a32eb52e1c0c10c1a4a33ea8bcd374886dc62b0c17e09be3ca21ee2b303)
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
            type_hints = typing.get_type_hints(_typecheckingstub__559068321fca9aff9b11a2c20ff4cd5479b8c3b498525bd9ac49f6c8072ec149)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e1941194e639a0a2c4bc43f9c967698655f010f4c1247fb1b8ec86f8fa759db2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[VolumeCapability]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[VolumeCapability]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[VolumeCapability]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fda169b2fca96b9a0b53c1c7b798bd88101180b733c542306b0002db63536089)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class VolumeCapabilityOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.volume.VolumeCapabilityOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f154eab2423fa39c1aebf8bf5e114b1649d3b0bb4bead6dbb8db2e5c01fe25e1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__41129720fd0e45aba5bc678ed033cee0bed4d0bcc554480b3f7eeff10ab74a85)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessMode", value)

    @builtins.property
    @jsii.member(jsii_name="attachmentMode")
    def attachment_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "attachmentMode"))

    @attachment_mode.setter
    def attachment_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79e4ef59dc7bed2ea0daa1e549d0802e715be96fab4558ad5a7f27c900ec1cfd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attachmentMode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[VolumeCapability, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[VolumeCapability, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[VolumeCapability, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9cfb8b73d64963e9d4bc628154c8d441bf542e377d22e94fd1352b119772fd83)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-nomad.volume.VolumeConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "external_id": "externalId",
        "name": "name",
        "plugin_id": "pluginId",
        "volume_id": "volumeId",
        "access_mode": "accessMode",
        "attachment_mode": "attachmentMode",
        "capability": "capability",
        "context": "context",
        "deregister_on_destroy": "deregisterOnDestroy",
        "id": "id",
        "mount_options": "mountOptions",
        "namespace": "namespace",
        "parameters": "parameters",
        "secrets": "secrets",
        "topology_request": "topologyRequest",
        "type": "type",
    },
)
class VolumeConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        external_id: builtins.str,
        name: builtins.str,
        plugin_id: builtins.str,
        volume_id: builtins.str,
        access_mode: typing.Optional[builtins.str] = None,
        attachment_mode: typing.Optional[builtins.str] = None,
        capability: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[VolumeCapability, typing.Dict[builtins.str, typing.Any]]]]] = None,
        context: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        deregister_on_destroy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        mount_options: typing.Optional[typing.Union["VolumeMountOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        namespace: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        secrets: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        topology_request: typing.Optional[typing.Union["VolumeTopologyRequest", typing.Dict[builtins.str, typing.Any]]] = None,
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
        :param external_id: The ID of the physical volume from the storage provider. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#external_id Volume#external_id}
        :param name: The display name of the volume. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#name Volume#name}
        :param plugin_id: The ID of the CSI plugin that manages this volume. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#plugin_id Volume#plugin_id}
        :param volume_id: The unique ID of the volume, how jobs will refer to the volume. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#volume_id Volume#volume_id}
        :param access_mode: Defines whether a volume should be available concurrently. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#access_mode Volume#access_mode}
        :param attachment_mode: The storage API that will be used by the volume. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#attachment_mode Volume#attachment_mode}
        :param capability: capability block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#capability Volume#capability}
        :param context: An optional key-value map of strings passed directly to the CSI plugin to validate the volume. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#context Volume#context}
        :param deregister_on_destroy: If true, the volume will be deregistered on destroy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#deregister_on_destroy Volume#deregister_on_destroy}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#id Volume#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param mount_options: mount_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#mount_options Volume#mount_options}
        :param namespace: The namespace in which to create the volume. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#namespace Volume#namespace}
        :param parameters: An optional key-value map of strings passed directly to the CSI plugin to configure the volume. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#parameters Volume#parameters}
        :param secrets: An optional key-value map of strings used as credentials for publishing and unpublishing volumes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#secrets Volume#secrets}
        :param topology_request: topology_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#topology_request Volume#topology_request}
        :param type: The type of the volume. Currently, only 'csi' is supported. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#type Volume#type}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(mount_options, dict):
            mount_options = VolumeMountOptions(**mount_options)
        if isinstance(topology_request, dict):
            topology_request = VolumeTopologyRequest(**topology_request)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52babf881cfea79050bb811ab5834626eb980a40882a415da94157a451771d85)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument external_id", value=external_id, expected_type=type_hints["external_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument plugin_id", value=plugin_id, expected_type=type_hints["plugin_id"])
            check_type(argname="argument volume_id", value=volume_id, expected_type=type_hints["volume_id"])
            check_type(argname="argument access_mode", value=access_mode, expected_type=type_hints["access_mode"])
            check_type(argname="argument attachment_mode", value=attachment_mode, expected_type=type_hints["attachment_mode"])
            check_type(argname="argument capability", value=capability, expected_type=type_hints["capability"])
            check_type(argname="argument context", value=context, expected_type=type_hints["context"])
            check_type(argname="argument deregister_on_destroy", value=deregister_on_destroy, expected_type=type_hints["deregister_on_destroy"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument mount_options", value=mount_options, expected_type=type_hints["mount_options"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument secrets", value=secrets, expected_type=type_hints["secrets"])
            check_type(argname="argument topology_request", value=topology_request, expected_type=type_hints["topology_request"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "external_id": external_id,
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
        if access_mode is not None:
            self._values["access_mode"] = access_mode
        if attachment_mode is not None:
            self._values["attachment_mode"] = attachment_mode
        if capability is not None:
            self._values["capability"] = capability
        if context is not None:
            self._values["context"] = context
        if deregister_on_destroy is not None:
            self._values["deregister_on_destroy"] = deregister_on_destroy
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
    def external_id(self) -> builtins.str:
        '''The ID of the physical volume from the storage provider.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#external_id Volume#external_id}
        '''
        result = self._values.get("external_id")
        assert result is not None, "Required property 'external_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The display name of the volume.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#name Volume#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def plugin_id(self) -> builtins.str:
        '''The ID of the CSI plugin that manages this volume.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#plugin_id Volume#plugin_id}
        '''
        result = self._values.get("plugin_id")
        assert result is not None, "Required property 'plugin_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def volume_id(self) -> builtins.str:
        '''The unique ID of the volume, how jobs will refer to the volume.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#volume_id Volume#volume_id}
        '''
        result = self._values.get("volume_id")
        assert result is not None, "Required property 'volume_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_mode(self) -> typing.Optional[builtins.str]:
        '''Defines whether a volume should be available concurrently.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#access_mode Volume#access_mode}
        '''
        result = self._values.get("access_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def attachment_mode(self) -> typing.Optional[builtins.str]:
        '''The storage API that will be used by the volume.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#attachment_mode Volume#attachment_mode}
        '''
        result = self._values.get("attachment_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def capability(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[VolumeCapability]]]:
        '''capability block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#capability Volume#capability}
        '''
        result = self._values.get("capability")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[VolumeCapability]]], result)

    @builtins.property
    def context(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''An optional key-value map of strings passed directly to the CSI plugin to validate the volume.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#context Volume#context}
        '''
        result = self._values.get("context")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def deregister_on_destroy(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''If true, the volume will be deregistered on destroy.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#deregister_on_destroy Volume#deregister_on_destroy}
        '''
        result = self._values.get("deregister_on_destroy")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#id Volume#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mount_options(self) -> typing.Optional["VolumeMountOptions"]:
        '''mount_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#mount_options Volume#mount_options}
        '''
        result = self._values.get("mount_options")
        return typing.cast(typing.Optional["VolumeMountOptions"], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''The namespace in which to create the volume.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#namespace Volume#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameters(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''An optional key-value map of strings passed directly to the CSI plugin to configure the volume.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#parameters Volume#parameters}
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def secrets(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''An optional key-value map of strings used as credentials for publishing and unpublishing volumes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#secrets Volume#secrets}
        '''
        result = self._values.get("secrets")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def topology_request(self) -> typing.Optional["VolumeTopologyRequest"]:
        '''topology_request block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#topology_request Volume#topology_request}
        '''
        result = self._values.get("topology_request")
        return typing.cast(typing.Optional["VolumeTopologyRequest"], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''The type of the volume. Currently, only 'csi' is supported.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#type Volume#type}
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VolumeConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-nomad.volume.VolumeMountOptions",
    jsii_struct_bases=[],
    name_mapping={"fs_type": "fsType", "mount_flags": "mountFlags"},
)
class VolumeMountOptions:
    def __init__(
        self,
        *,
        fs_type: typing.Optional[builtins.str] = None,
        mount_flags: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param fs_type: The file system type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#fs_type Volume#fs_type}
        :param mount_flags: The flags passed to mount. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#mount_flags Volume#mount_flags}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d7feb5a469c8fcd95c95dd231c420df4eedfcc8ed690da67dc74a1596d722cf)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#fs_type Volume#fs_type}
        '''
        result = self._values.get("fs_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mount_flags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The flags passed to mount.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#mount_flags Volume#mount_flags}
        '''
        result = self._values.get("mount_flags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VolumeMountOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VolumeMountOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.volume.VolumeMountOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b1ac7def179d163fc058b3b0433b35f55157507a057e992c7774f026ff7b7d7e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__fd6e663c46dafb7bb85a7725c5d9a4a8eae3a1bcfddf17091b50cfc370e6451a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fsType", value)

    @builtins.property
    @jsii.member(jsii_name="mountFlags")
    def mount_flags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "mountFlags"))

    @mount_flags.setter
    def mount_flags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef43accdd635cbb8038083270a71e62cc302fee469d1dd582b068d7fa28aa9c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mountFlags", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[VolumeMountOptions]:
        return typing.cast(typing.Optional[VolumeMountOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[VolumeMountOptions]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db3143fe646ccfc77e8e58f84dee7d7990734cda4dec86bb2cf7826c557f4716)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-nomad.volume.VolumeTopologies",
    jsii_struct_bases=[],
    name_mapping={},
)
class VolumeTopologies:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VolumeTopologies(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VolumeTopologiesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.volume.VolumeTopologiesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e3adce475736417806c5399f9c97ec6dd83a15824963519877763bdac2dbdb5a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "VolumeTopologiesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3759769ccd60c103d6c91e88959de1895e9935837a4b152886e50085020f840a)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("VolumeTopologiesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b519fb73f56b997f829f7dae4020e3ea17ae4c2f7700f7eb1d9c7a0c122c5f1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0dd14d3ecb6980f996aabdbb1a89b88bcc8901059e5d9a1470a9637231c00fc6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c3ce94264df454e0d18b6754aec7d17ee85fb045eb355c64f28f15d03f14a9f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class VolumeTopologiesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.volume.VolumeTopologiesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__006417d6bfcf925856072e9c93a0325d420b345ae949b4dbc07866e44b5f515e)
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
    def internal_value(self) -> typing.Optional[VolumeTopologies]:
        return typing.cast(typing.Optional[VolumeTopologies], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[VolumeTopologies]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__740c59715316e2ef90a1f1bc40d8f2b1ebdd5684517080cd7badcd9d1bace4d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-nomad.volume.VolumeTopologyRequest",
    jsii_struct_bases=[],
    name_mapping={"required": "required"},
)
class VolumeTopologyRequest:
    def __init__(
        self,
        *,
        required: typing.Optional[typing.Union["VolumeTopologyRequestRequired", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param required: required block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#required Volume#required}
        '''
        if isinstance(required, dict):
            required = VolumeTopologyRequestRequired(**required)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d3276426c5991d2601f38dcf5b1a34b9623cb79308256f951807d43a9e3dd55)
            check_type(argname="argument required", value=required, expected_type=type_hints["required"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if required is not None:
            self._values["required"] = required

    @builtins.property
    def required(self) -> typing.Optional["VolumeTopologyRequestRequired"]:
        '''required block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#required Volume#required}
        '''
        result = self._values.get("required")
        return typing.cast(typing.Optional["VolumeTopologyRequestRequired"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VolumeTopologyRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VolumeTopologyRequestOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.volume.VolumeTopologyRequestOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__43121536e7d0664b0f6a6f8208131918193c3efbffe29187aa29e19d6a661407)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRequired")
    def put_required(
        self,
        *,
        topology: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["VolumeTopologyRequestRequiredTopology", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param topology: topology block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#topology Volume#topology}
        '''
        value = VolumeTopologyRequestRequired(topology=topology)

        return typing.cast(None, jsii.invoke(self, "putRequired", [value]))

    @jsii.member(jsii_name="resetRequired")
    def reset_required(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequired", []))

    @builtins.property
    @jsii.member(jsii_name="required")
    def required(self) -> "VolumeTopologyRequestRequiredOutputReference":
        return typing.cast("VolumeTopologyRequestRequiredOutputReference", jsii.get(self, "required"))

    @builtins.property
    @jsii.member(jsii_name="requiredInput")
    def required_input(self) -> typing.Optional["VolumeTopologyRequestRequired"]:
        return typing.cast(typing.Optional["VolumeTopologyRequestRequired"], jsii.get(self, "requiredInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[VolumeTopologyRequest]:
        return typing.cast(typing.Optional[VolumeTopologyRequest], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[VolumeTopologyRequest]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9677028bae617fe0a522d4aa7dc0ff728832c92930b659d8cf885708ae8d1c4c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-nomad.volume.VolumeTopologyRequestRequired",
    jsii_struct_bases=[],
    name_mapping={"topology": "topology"},
)
class VolumeTopologyRequestRequired:
    def __init__(
        self,
        *,
        topology: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["VolumeTopologyRequestRequiredTopology", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param topology: topology block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#topology Volume#topology}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d615fe70e0d6d70420c0b22f988cf927fdb46da96f73255b57b88c4510cf61a0)
            check_type(argname="argument topology", value=topology, expected_type=type_hints["topology"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "topology": topology,
        }

    @builtins.property
    def topology(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["VolumeTopologyRequestRequiredTopology"]]:
        '''topology block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#topology Volume#topology}
        '''
        result = self._values.get("topology")
        assert result is not None, "Required property 'topology' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["VolumeTopologyRequestRequiredTopology"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VolumeTopologyRequestRequired(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VolumeTopologyRequestRequiredOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.volume.VolumeTopologyRequestRequiredOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__766ccbd7f65e1e8bcf593786676efb4010e3b7bbdc78ea9861281dce58f94a06)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putTopology")
    def put_topology(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["VolumeTopologyRequestRequiredTopology", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5fac1e6861abd344d5d9c163620bd8bbe447c3cd067e0bbb3c68141e2ecafe90)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTopology", [value]))

    @builtins.property
    @jsii.member(jsii_name="topology")
    def topology(self) -> "VolumeTopologyRequestRequiredTopologyList":
        return typing.cast("VolumeTopologyRequestRequiredTopologyList", jsii.get(self, "topology"))

    @builtins.property
    @jsii.member(jsii_name="topologyInput")
    def topology_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["VolumeTopologyRequestRequiredTopology"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["VolumeTopologyRequestRequiredTopology"]]], jsii.get(self, "topologyInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[VolumeTopologyRequestRequired]:
        return typing.cast(typing.Optional[VolumeTopologyRequestRequired], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[VolumeTopologyRequestRequired],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12f7c3b00ffa70fd1f7260ffd5adddbad3750f9ad061790068731e176adb8120)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-nomad.volume.VolumeTopologyRequestRequiredTopology",
    jsii_struct_bases=[],
    name_mapping={"segments": "segments"},
)
class VolumeTopologyRequestRequiredTopology:
    def __init__(self, *, segments: typing.Mapping[builtins.str, builtins.str]) -> None:
        '''
        :param segments: Define attributes for the topology request. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#segments Volume#segments}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4562a0ac1b734aed0d2e5fa885ebfe69f6b4249b485c956c66468125c09a9f1d)
            check_type(argname="argument segments", value=segments, expected_type=type_hints["segments"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "segments": segments,
        }

    @builtins.property
    def segments(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''Define attributes for the topology request.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/volume#segments Volume#segments}
        '''
        result = self._values.get("segments")
        assert result is not None, "Required property 'segments' is missing"
        return typing.cast(typing.Mapping[builtins.str, builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VolumeTopologyRequestRequiredTopology(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VolumeTopologyRequestRequiredTopologyList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.volume.VolumeTopologyRequestRequiredTopologyList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a338128e795a82dc75abab709a2ecca1e67108b0c7d6ac243ddfd8d137f178c5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "VolumeTopologyRequestRequiredTopologyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__850e830e7372d761fb745791a073081b62897c9fb1cf0ffeec9cc4a164e9209a)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("VolumeTopologyRequestRequiredTopologyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9537ac3f7fcfda5cdc33f5067ae009b3051848ab3a69ebdba96a256ceb9b8d69)
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
            type_hints = typing.get_type_hints(_typecheckingstub__abb4814e228890e67bb40313e783b6b7da558cf4308af70755cae8fac52827f1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__563cfa4c11f5397b8a220f13e46504bc489bd6cba33d76031b19334e9af1e994)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[VolumeTopologyRequestRequiredTopology]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[VolumeTopologyRequestRequiredTopology]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[VolumeTopologyRequestRequiredTopology]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62f15929164c8a36b2a80ec0714fb3451c60b91db9073f24e5c0fc42df722ee2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class VolumeTopologyRequestRequiredTopologyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.volume.VolumeTopologyRequestRequiredTopologyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__468f3dec8583b5bae905e57239b14bf126bbf4f9b761b47d5546acc56f9e3353)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9683bbb1fa88ed1e8653de2ef0ce703dd3fe57f1a752f6c90bfd487d1d9a367a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "segments", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[VolumeTopologyRequestRequiredTopology, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[VolumeTopologyRequestRequiredTopology, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[VolumeTopologyRequestRequiredTopology, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51a92def6e2ff376411dd959960ccf75f9ea3d095d4f50a81416f89ce1ff5a66)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Volume",
    "VolumeCapability",
    "VolumeCapabilityList",
    "VolumeCapabilityOutputReference",
    "VolumeConfig",
    "VolumeMountOptions",
    "VolumeMountOptionsOutputReference",
    "VolumeTopologies",
    "VolumeTopologiesList",
    "VolumeTopologiesOutputReference",
    "VolumeTopologyRequest",
    "VolumeTopologyRequestOutputReference",
    "VolumeTopologyRequestRequired",
    "VolumeTopologyRequestRequiredOutputReference",
    "VolumeTopologyRequestRequiredTopology",
    "VolumeTopologyRequestRequiredTopologyList",
    "VolumeTopologyRequestRequiredTopologyOutputReference",
]

publication.publish()

def _typecheckingstub__ce1738d87feac8e9e1545157cbd8c58279d22797d7adeda10c42e585f9bd4a7a(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    external_id: builtins.str,
    name: builtins.str,
    plugin_id: builtins.str,
    volume_id: builtins.str,
    access_mode: typing.Optional[builtins.str] = None,
    attachment_mode: typing.Optional[builtins.str] = None,
    capability: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[VolumeCapability, typing.Dict[builtins.str, typing.Any]]]]] = None,
    context: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    deregister_on_destroy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    mount_options: typing.Optional[typing.Union[VolumeMountOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    namespace: typing.Optional[builtins.str] = None,
    parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    secrets: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    topology_request: typing.Optional[typing.Union[VolumeTopologyRequest, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__a94b9cdf9b34a5704453223f4e466698ffc12852b97d21219469d79e32ca9eb2(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[VolumeCapability, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e41c9c6e5cb5a4399f2546b5ae9696e431b4897ba1421f92da75531a87c1d792(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__391dc8cef3ffd660a0221ac955a38fe317c59aa1049d58caac2caeb3f020c076(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__597834f01ce828a73903e771575c144704fe5aa9c9b0de3c007a2c964945be71(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__801b1447c48baf455cb46be475eaaa541628a34115cc6f1124c546cdeab601c4(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__981eb4c9cb35dca99c423316b04b1555aa9cfd30fc55627349428c0cff0c6955(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc694244171e62a3187221c5d42a301c0c2e72f78aab3aefc2c3a4082b06ee9d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19d6d2f34c09068788b1e6ccceeec6e26a6218291667bcbc63ca094f77e5c6ea(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be782c6336f7ecdb8d6158e16bab1775e9b5418788a1970e5c99d219f6932d5a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4f63c35e021d145560456dc295cb6800596a704b29091118ad96ca55912620a(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5c192456436ccfd5b5bb31650fc5e0638a684fb89dfb4ed610a27c516e73b52(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__256106c554e294e4f598a94452d28e2bbfd833343751b347c438b41f51e50f6f(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85877411bfbb5082c4548a09b9e0694e43a010e3d1a19eaaaec462de22b671eb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db6f8cbc03c044f50cccb7b0223392378d44895ae801499f9ac49bd23e847949(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82ff8d33b081ea2e1dd4c0781d9b593bc38991532a7cb78bfea7b13ccf673154(
    *,
    access_mode: builtins.str,
    attachment_mode: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55b2956eec774b4639796178d26e85690dcf4f300ddb5a69055eb7b2c89d3c9a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e234d4428e3c677efa3f14cd7d034cdeb39f31450d2170cf53ea799659dbef8(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba253a32eb52e1c0c10c1a4a33ea8bcd374886dc62b0c17e09be3ca21ee2b303(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__559068321fca9aff9b11a2c20ff4cd5479b8c3b498525bd9ac49f6c8072ec149(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1941194e639a0a2c4bc43f9c967698655f010f4c1247fb1b8ec86f8fa759db2(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fda169b2fca96b9a0b53c1c7b798bd88101180b733c542306b0002db63536089(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[VolumeCapability]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f154eab2423fa39c1aebf8bf5e114b1649d3b0bb4bead6dbb8db2e5c01fe25e1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41129720fd0e45aba5bc678ed033cee0bed4d0bcc554480b3f7eeff10ab74a85(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79e4ef59dc7bed2ea0daa1e549d0802e715be96fab4558ad5a7f27c900ec1cfd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9cfb8b73d64963e9d4bc628154c8d441bf542e377d22e94fd1352b119772fd83(
    value: typing.Optional[typing.Union[VolumeCapability, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52babf881cfea79050bb811ab5834626eb980a40882a415da94157a451771d85(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    external_id: builtins.str,
    name: builtins.str,
    plugin_id: builtins.str,
    volume_id: builtins.str,
    access_mode: typing.Optional[builtins.str] = None,
    attachment_mode: typing.Optional[builtins.str] = None,
    capability: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[VolumeCapability, typing.Dict[builtins.str, typing.Any]]]]] = None,
    context: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    deregister_on_destroy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    mount_options: typing.Optional[typing.Union[VolumeMountOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    namespace: typing.Optional[builtins.str] = None,
    parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    secrets: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    topology_request: typing.Optional[typing.Union[VolumeTopologyRequest, typing.Dict[builtins.str, typing.Any]]] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d7feb5a469c8fcd95c95dd231c420df4eedfcc8ed690da67dc74a1596d722cf(
    *,
    fs_type: typing.Optional[builtins.str] = None,
    mount_flags: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1ac7def179d163fc058b3b0433b35f55157507a057e992c7774f026ff7b7d7e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd6e663c46dafb7bb85a7725c5d9a4a8eae3a1bcfddf17091b50cfc370e6451a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef43accdd635cbb8038083270a71e62cc302fee469d1dd582b068d7fa28aa9c9(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db3143fe646ccfc77e8e58f84dee7d7990734cda4dec86bb2cf7826c557f4716(
    value: typing.Optional[VolumeMountOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3adce475736417806c5399f9c97ec6dd83a15824963519877763bdac2dbdb5a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3759769ccd60c103d6c91e88959de1895e9935837a4b152886e50085020f840a(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b519fb73f56b997f829f7dae4020e3ea17ae4c2f7700f7eb1d9c7a0c122c5f1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0dd14d3ecb6980f996aabdbb1a89b88bcc8901059e5d9a1470a9637231c00fc6(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3ce94264df454e0d18b6754aec7d17ee85fb045eb355c64f28f15d03f14a9f4(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__006417d6bfcf925856072e9c93a0325d420b345ae949b4dbc07866e44b5f515e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__740c59715316e2ef90a1f1bc40d8f2b1ebdd5684517080cd7badcd9d1bace4d7(
    value: typing.Optional[VolumeTopologies],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d3276426c5991d2601f38dcf5b1a34b9623cb79308256f951807d43a9e3dd55(
    *,
    required: typing.Optional[typing.Union[VolumeTopologyRequestRequired, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43121536e7d0664b0f6a6f8208131918193c3efbffe29187aa29e19d6a661407(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9677028bae617fe0a522d4aa7dc0ff728832c92930b659d8cf885708ae8d1c4c(
    value: typing.Optional[VolumeTopologyRequest],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d615fe70e0d6d70420c0b22f988cf927fdb46da96f73255b57b88c4510cf61a0(
    *,
    topology: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[VolumeTopologyRequestRequiredTopology, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__766ccbd7f65e1e8bcf593786676efb4010e3b7bbdc78ea9861281dce58f94a06(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5fac1e6861abd344d5d9c163620bd8bbe447c3cd067e0bbb3c68141e2ecafe90(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[VolumeTopologyRequestRequiredTopology, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12f7c3b00ffa70fd1f7260ffd5adddbad3750f9ad061790068731e176adb8120(
    value: typing.Optional[VolumeTopologyRequestRequired],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4562a0ac1b734aed0d2e5fa885ebfe69f6b4249b485c956c66468125c09a9f1d(
    *,
    segments: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a338128e795a82dc75abab709a2ecca1e67108b0c7d6ac243ddfd8d137f178c5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__850e830e7372d761fb745791a073081b62897c9fb1cf0ffeec9cc4a164e9209a(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9537ac3f7fcfda5cdc33f5067ae009b3051848ab3a69ebdba96a256ceb9b8d69(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__abb4814e228890e67bb40313e783b6b7da558cf4308af70755cae8fac52827f1(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__563cfa4c11f5397b8a220f13e46504bc489bd6cba33d76031b19334e9af1e994(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62f15929164c8a36b2a80ec0714fb3451c60b91db9073f24e5c0fc42df722ee2(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[VolumeTopologyRequestRequiredTopology]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__468f3dec8583b5bae905e57239b14bf126bbf4f9b761b47d5546acc56f9e3353(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9683bbb1fa88ed1e8653de2ef0ce703dd3fe57f1a752f6c90bfd487d1d9a367a(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51a92def6e2ff376411dd959960ccf75f9ea3d095d4f50a81416f89ce1ff5a66(
    value: typing.Optional[typing.Union[VolumeTopologyRequestRequiredTopology, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
