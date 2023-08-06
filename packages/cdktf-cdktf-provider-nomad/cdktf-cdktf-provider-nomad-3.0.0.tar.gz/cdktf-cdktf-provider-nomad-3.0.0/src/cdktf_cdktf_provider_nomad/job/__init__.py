'''
# `nomad_job`

Refer to the Terraform Registory for docs: [`nomad_job`](https://www.terraform.io/docs/providers/nomad/r/job).
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


class Job(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.job.Job",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/nomad/r/job nomad_job}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        jobspec: builtins.str,
        consul_token: typing.Optional[builtins.str] = None,
        deregister_on_destroy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        deregister_on_id_change: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        detach: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        hcl2: typing.Optional[typing.Union["JobHcl2", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        json: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        policy_override: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        purge_on_destroy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        timeouts: typing.Optional[typing.Union["JobTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        vault_token: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/nomad/r/job nomad_job} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param jobspec: Job specification. If you want to point to a file use the file() function. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#jobspec Job#jobspec}
        :param consul_token: The Consul token used to submit this job. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#consul_token Job#consul_token}
        :param deregister_on_destroy: If true, the job will be deregistered on destroy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#deregister_on_destroy Job#deregister_on_destroy}
        :param deregister_on_id_change: If true, the job will be deregistered when the job ID changes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#deregister_on_id_change Job#deregister_on_id_change}
        :param detach: If true, the provider will return immediately after creating or updating, instead of monitoring. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#detach Job#detach}
        :param hcl2: hcl2 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#hcl2 Job#hcl2}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#id Job#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param json: If true, the ``jobspec`` will be parsed as json instead of HCL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#json Job#json}
        :param policy_override: Override any soft-mandatory Sentinel policies that fail. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#policy_override Job#policy_override}
        :param purge_on_destroy: Whether to purge the job when the resource is destroyed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#purge_on_destroy Job#purge_on_destroy}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#timeouts Job#timeouts}
        :param vault_token: The Vault token used to submit this job. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#vault_token Job#vault_token}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e9e8f55e8cd582973ea2af0596c3f464a65eeff93736c25a32d8418f95816e6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = JobConfig(
            jobspec=jobspec,
            consul_token=consul_token,
            deregister_on_destroy=deregister_on_destroy,
            deregister_on_id_change=deregister_on_id_change,
            detach=detach,
            hcl2=hcl2,
            id=id,
            json=json,
            policy_override=policy_override,
            purge_on_destroy=purge_on_destroy,
            timeouts=timeouts,
            vault_token=vault_token,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putHcl2")
    def put_hcl2(
        self,
        *,
        allow_fs: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        vars: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param allow_fs: If true, HCL2 file system functions will be enabled when parsing the ``jobspec``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#allow_fs Job#allow_fs}
        :param enabled: If true, the ``jobspec`` will be parsed as HCL2 instead of HCL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#enabled Job#enabled}
        :param vars: Additional variables to use when templating the job with HCL2. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#vars Job#vars}
        '''
        value = JobHcl2(allow_fs=allow_fs, enabled=enabled, vars=vars)

        return typing.cast(None, jsii.invoke(self, "putHcl2", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#create Job#create}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#update Job#update}.
        '''
        value = JobTimeouts(create=create, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetConsulToken")
    def reset_consul_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConsulToken", []))

    @jsii.member(jsii_name="resetDeregisterOnDestroy")
    def reset_deregister_on_destroy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeregisterOnDestroy", []))

    @jsii.member(jsii_name="resetDeregisterOnIdChange")
    def reset_deregister_on_id_change(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeregisterOnIdChange", []))

    @jsii.member(jsii_name="resetDetach")
    def reset_detach(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDetach", []))

    @jsii.member(jsii_name="resetHcl2")
    def reset_hcl2(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHcl2", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetJson")
    def reset_json(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJson", []))

    @jsii.member(jsii_name="resetPolicyOverride")
    def reset_policy_override(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPolicyOverride", []))

    @jsii.member(jsii_name="resetPurgeOnDestroy")
    def reset_purge_on_destroy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPurgeOnDestroy", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetVaultToken")
    def reset_vault_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVaultToken", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="allocationIds")
    def allocation_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allocationIds"))

    @builtins.property
    @jsii.member(jsii_name="datacenters")
    def datacenters(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "datacenters"))

    @builtins.property
    @jsii.member(jsii_name="deploymentId")
    def deployment_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deploymentId"))

    @builtins.property
    @jsii.member(jsii_name="deploymentStatus")
    def deployment_status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deploymentStatus"))

    @builtins.property
    @jsii.member(jsii_name="hcl2")
    def hcl2(self) -> "JobHcl2OutputReference":
        return typing.cast("JobHcl2OutputReference", jsii.get(self, "hcl2"))

    @builtins.property
    @jsii.member(jsii_name="modifyIndex")
    def modify_index(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "modifyIndex"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @builtins.property
    @jsii.member(jsii_name="taskGroups")
    def task_groups(self) -> "JobTaskGroupsList":
        return typing.cast("JobTaskGroupsList", jsii.get(self, "taskGroups"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "JobTimeoutsOutputReference":
        return typing.cast("JobTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @builtins.property
    @jsii.member(jsii_name="consulTokenInput")
    def consul_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "consulTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="deregisterOnDestroyInput")
    def deregister_on_destroy_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "deregisterOnDestroyInput"))

    @builtins.property
    @jsii.member(jsii_name="deregisterOnIdChangeInput")
    def deregister_on_id_change_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "deregisterOnIdChangeInput"))

    @builtins.property
    @jsii.member(jsii_name="detachInput")
    def detach_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "detachInput"))

    @builtins.property
    @jsii.member(jsii_name="hcl2Input")
    def hcl2_input(self) -> typing.Optional["JobHcl2"]:
        return typing.cast(typing.Optional["JobHcl2"], jsii.get(self, "hcl2Input"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="jobspecInput")
    def jobspec_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jobspecInput"))

    @builtins.property
    @jsii.member(jsii_name="jsonInput")
    def json_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "jsonInput"))

    @builtins.property
    @jsii.member(jsii_name="policyOverrideInput")
    def policy_override_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "policyOverrideInput"))

    @builtins.property
    @jsii.member(jsii_name="purgeOnDestroyInput")
    def purge_on_destroy_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "purgeOnDestroyInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["JobTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["JobTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="vaultTokenInput")
    def vault_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vaultTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="consulToken")
    def consul_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "consulToken"))

    @consul_token.setter
    def consul_token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8fb8ec063891f66a3277e2ad6b43cc0e717387a90bb815bd7ddc07631a2dac22)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "consulToken", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__078359c3f89ed0777e18e7c61ec478f7f56176e4ba4263dffb1baf0957820cc5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deregisterOnDestroy", value)

    @builtins.property
    @jsii.member(jsii_name="deregisterOnIdChange")
    def deregister_on_id_change(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "deregisterOnIdChange"))

    @deregister_on_id_change.setter
    def deregister_on_id_change(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7595b919d310b786dc2cab77000fbbd8cbe4e901c9fa62ff858c4f361902f78a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deregisterOnIdChange", value)

    @builtins.property
    @jsii.member(jsii_name="detach")
    def detach(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "detach"))

    @detach.setter
    def detach(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f687cae31fe60e332072b7d7f3bd7ecc219b10e171b759faf68a43b089ebf1d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "detach", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25b21eee6956e6b7e3081e53c224b6ff325d6c6322b0ac1bc736a8c612392e8b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="jobspec")
    def jobspec(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "jobspec"))

    @jobspec.setter
    def jobspec(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e8785aeb00fde63f7f2fd381d51d074a7fad6cc4b18529a79ede07b800806b3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jobspec", value)

    @builtins.property
    @jsii.member(jsii_name="json")
    def json(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "json"))

    @json.setter
    def json(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06d42d2dbbbb7807360a092e71f5d5ced2c46fd3b3d17ff1dc9ab394cbf6089d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "json", value)

    @builtins.property
    @jsii.member(jsii_name="policyOverride")
    def policy_override(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "policyOverride"))

    @policy_override.setter
    def policy_override(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d70c54f9c259b625b45b1ac18a2f116cc5b86e061cceac2a829d3df809bca10)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyOverride", value)

    @builtins.property
    @jsii.member(jsii_name="purgeOnDestroy")
    def purge_on_destroy(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "purgeOnDestroy"))

    @purge_on_destroy.setter
    def purge_on_destroy(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab1535cba628eb65cb272df7d4485b56a5fcd08dcfe0b5e33964bf11fc8d706a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "purgeOnDestroy", value)

    @builtins.property
    @jsii.member(jsii_name="vaultToken")
    def vault_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vaultToken"))

    @vault_token.setter
    def vault_token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b746a5a0c0e4fb728ade7483a54a2654d6d6058f91cd1254a5aaf73135ee485)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vaultToken", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-nomad.job.JobConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "jobspec": "jobspec",
        "consul_token": "consulToken",
        "deregister_on_destroy": "deregisterOnDestroy",
        "deregister_on_id_change": "deregisterOnIdChange",
        "detach": "detach",
        "hcl2": "hcl2",
        "id": "id",
        "json": "json",
        "policy_override": "policyOverride",
        "purge_on_destroy": "purgeOnDestroy",
        "timeouts": "timeouts",
        "vault_token": "vaultToken",
    },
)
class JobConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        jobspec: builtins.str,
        consul_token: typing.Optional[builtins.str] = None,
        deregister_on_destroy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        deregister_on_id_change: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        detach: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        hcl2: typing.Optional[typing.Union["JobHcl2", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        json: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        policy_override: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        purge_on_destroy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        timeouts: typing.Optional[typing.Union["JobTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        vault_token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param jobspec: Job specification. If you want to point to a file use the file() function. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#jobspec Job#jobspec}
        :param consul_token: The Consul token used to submit this job. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#consul_token Job#consul_token}
        :param deregister_on_destroy: If true, the job will be deregistered on destroy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#deregister_on_destroy Job#deregister_on_destroy}
        :param deregister_on_id_change: If true, the job will be deregistered when the job ID changes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#deregister_on_id_change Job#deregister_on_id_change}
        :param detach: If true, the provider will return immediately after creating or updating, instead of monitoring. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#detach Job#detach}
        :param hcl2: hcl2 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#hcl2 Job#hcl2}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#id Job#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param json: If true, the ``jobspec`` will be parsed as json instead of HCL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#json Job#json}
        :param policy_override: Override any soft-mandatory Sentinel policies that fail. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#policy_override Job#policy_override}
        :param purge_on_destroy: Whether to purge the job when the resource is destroyed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#purge_on_destroy Job#purge_on_destroy}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#timeouts Job#timeouts}
        :param vault_token: The Vault token used to submit this job. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#vault_token Job#vault_token}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(hcl2, dict):
            hcl2 = JobHcl2(**hcl2)
        if isinstance(timeouts, dict):
            timeouts = JobTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37af447459ed11d3aaa370e639e90e5dbccbaa7ec090fc274ebbf6a048d1f698)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument jobspec", value=jobspec, expected_type=type_hints["jobspec"])
            check_type(argname="argument consul_token", value=consul_token, expected_type=type_hints["consul_token"])
            check_type(argname="argument deregister_on_destroy", value=deregister_on_destroy, expected_type=type_hints["deregister_on_destroy"])
            check_type(argname="argument deregister_on_id_change", value=deregister_on_id_change, expected_type=type_hints["deregister_on_id_change"])
            check_type(argname="argument detach", value=detach, expected_type=type_hints["detach"])
            check_type(argname="argument hcl2", value=hcl2, expected_type=type_hints["hcl2"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument json", value=json, expected_type=type_hints["json"])
            check_type(argname="argument policy_override", value=policy_override, expected_type=type_hints["policy_override"])
            check_type(argname="argument purge_on_destroy", value=purge_on_destroy, expected_type=type_hints["purge_on_destroy"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument vault_token", value=vault_token, expected_type=type_hints["vault_token"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "jobspec": jobspec,
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
        if consul_token is not None:
            self._values["consul_token"] = consul_token
        if deregister_on_destroy is not None:
            self._values["deregister_on_destroy"] = deregister_on_destroy
        if deregister_on_id_change is not None:
            self._values["deregister_on_id_change"] = deregister_on_id_change
        if detach is not None:
            self._values["detach"] = detach
        if hcl2 is not None:
            self._values["hcl2"] = hcl2
        if id is not None:
            self._values["id"] = id
        if json is not None:
            self._values["json"] = json
        if policy_override is not None:
            self._values["policy_override"] = policy_override
        if purge_on_destroy is not None:
            self._values["purge_on_destroy"] = purge_on_destroy
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if vault_token is not None:
            self._values["vault_token"] = vault_token

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
    def jobspec(self) -> builtins.str:
        '''Job specification. If you want to point to a file use the file() function.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#jobspec Job#jobspec}
        '''
        result = self._values.get("jobspec")
        assert result is not None, "Required property 'jobspec' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def consul_token(self) -> typing.Optional[builtins.str]:
        '''The Consul token used to submit this job.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#consul_token Job#consul_token}
        '''
        result = self._values.get("consul_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def deregister_on_destroy(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''If true, the job will be deregistered on destroy.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#deregister_on_destroy Job#deregister_on_destroy}
        '''
        result = self._values.get("deregister_on_destroy")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def deregister_on_id_change(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''If true, the job will be deregistered when the job ID changes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#deregister_on_id_change Job#deregister_on_id_change}
        '''
        result = self._values.get("deregister_on_id_change")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def detach(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''If true, the provider will return immediately after creating or updating, instead of monitoring.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#detach Job#detach}
        '''
        result = self._values.get("detach")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def hcl2(self) -> typing.Optional["JobHcl2"]:
        '''hcl2 block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#hcl2 Job#hcl2}
        '''
        result = self._values.get("hcl2")
        return typing.cast(typing.Optional["JobHcl2"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#id Job#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def json(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''If true, the ``jobspec`` will be parsed as json instead of HCL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#json Job#json}
        '''
        result = self._values.get("json")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def policy_override(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Override any soft-mandatory Sentinel policies that fail.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#policy_override Job#policy_override}
        '''
        result = self._values.get("policy_override")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def purge_on_destroy(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to purge the job when the resource is destroyed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#purge_on_destroy Job#purge_on_destroy}
        '''
        result = self._values.get("purge_on_destroy")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["JobTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#timeouts Job#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["JobTimeouts"], result)

    @builtins.property
    def vault_token(self) -> typing.Optional[builtins.str]:
        '''The Vault token used to submit this job.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#vault_token Job#vault_token}
        '''
        result = self._values.get("vault_token")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "JobConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-nomad.job.JobHcl2",
    jsii_struct_bases=[],
    name_mapping={"allow_fs": "allowFs", "enabled": "enabled", "vars": "vars"},
)
class JobHcl2:
    def __init__(
        self,
        *,
        allow_fs: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        vars: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param allow_fs: If true, HCL2 file system functions will be enabled when parsing the ``jobspec``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#allow_fs Job#allow_fs}
        :param enabled: If true, the ``jobspec`` will be parsed as HCL2 instead of HCL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#enabled Job#enabled}
        :param vars: Additional variables to use when templating the job with HCL2. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#vars Job#vars}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00bd4c654c786dcc73121f9f1442771d83e52e3edaefba4adf383affd6577100)
            check_type(argname="argument allow_fs", value=allow_fs, expected_type=type_hints["allow_fs"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument vars", value=vars, expected_type=type_hints["vars"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if allow_fs is not None:
            self._values["allow_fs"] = allow_fs
        if enabled is not None:
            self._values["enabled"] = enabled
        if vars is not None:
            self._values["vars"] = vars

    @builtins.property
    def allow_fs(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''If true, HCL2 file system functions will be enabled when parsing the ``jobspec``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#allow_fs Job#allow_fs}
        '''
        result = self._values.get("allow_fs")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''If true, the ``jobspec`` will be parsed as HCL2 instead of HCL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#enabled Job#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def vars(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional variables to use when templating the job with HCL2.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#vars Job#vars}
        '''
        result = self._values.get("vars")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "JobHcl2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class JobHcl2OutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.job.JobHcl2OutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0dfe4c4c84d9591ec06b200ecabc44c8d87bf2a9eedd1c79ee76d124b6899f60)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAllowFs")
    def reset_allow_fs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowFs", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetVars")
    def reset_vars(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVars", []))

    @builtins.property
    @jsii.member(jsii_name="allowFsInput")
    def allow_fs_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "allowFsInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="varsInput")
    def vars_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "varsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowFs")
    def allow_fs(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "allowFs"))

    @allow_fs.setter
    def allow_fs(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e747dcc7b75cb9fe41793cc2dfa3640570f57fa5a807cd6990b8a8330177b010)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowFs", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a8d7796aef5a81e4a73976993a96831fe4cbe2ff7cbed0fdb5b3aa42a49e9e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="vars")
    def vars(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "vars"))

    @vars.setter
    def vars(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ade6e1ea51e55cdfe2dc15d47feea917884909cd2cc0cd809fb0811c08826096)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vars", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[JobHcl2]:
        return typing.cast(typing.Optional[JobHcl2], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[JobHcl2]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f98ecabe16ab8ae0f1afdf0266ea369f170e716c585af7faaf8d14dad9ba559)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-nomad.job.JobTaskGroups",
    jsii_struct_bases=[],
    name_mapping={},
)
class JobTaskGroups:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "JobTaskGroups(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class JobTaskGroupsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.job.JobTaskGroupsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f2e57815fe27336e718941d9f838dd79f04f4f85662754ea2b047e2160dafd50)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "JobTaskGroupsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4174be7e6ea47bfaa7492c476ff8ef114920798a22a5db27b3f1cba9c8f35494)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("JobTaskGroupsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1e7af1e993f30420fecd5a9087af46f18872c5c349ad25a9c79bd27d707e2a2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8e9507703514595225e2ee194be5456ed95a57bd8c545239212295add3c02931)
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
            type_hints = typing.get_type_hints(_typecheckingstub__eb7aebdde63eac4b6fd41cc706c59a2bc4bef01bc2f47e53e4c61bf1cce284e4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class JobTaskGroupsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.job.JobTaskGroupsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3fa71dec6bc4c7ac624fd6f8783f0f2547c57522cebfea216af629af7cfda4a0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="count")
    def count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "count"))

    @builtins.property
    @jsii.member(jsii_name="meta")
    def meta(self) -> _cdktf_9a9027ec.StringMap:
        return typing.cast(_cdktf_9a9027ec.StringMap, jsii.get(self, "meta"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="task")
    def task(self) -> "JobTaskGroupsTaskList":
        return typing.cast("JobTaskGroupsTaskList", jsii.get(self, "task"))

    @builtins.property
    @jsii.member(jsii_name="volumes")
    def volumes(self) -> "JobTaskGroupsVolumesList":
        return typing.cast("JobTaskGroupsVolumesList", jsii.get(self, "volumes"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[JobTaskGroups]:
        return typing.cast(typing.Optional[JobTaskGroups], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[JobTaskGroups]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e17551086a7bb12812477d0b0ff001ff22c9242763f04bec266cb2e819042525)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-nomad.job.JobTaskGroupsTask",
    jsii_struct_bases=[],
    name_mapping={},
)
class JobTaskGroupsTask:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "JobTaskGroupsTask(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class JobTaskGroupsTaskList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.job.JobTaskGroupsTaskList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2ca0466ccefe816b2704bb015e6d6a659756d0ec160064db8f68166339e670e0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "JobTaskGroupsTaskOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9c2e2f2371576f1ac125e8cb29a2a49350ba92d91126a02d0cf81bd11c2c6ce)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("JobTaskGroupsTaskOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e764971cec5a5c4008de0642b0a36b751b80e9d0b2177420c498290f2db00197)
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
            type_hints = typing.get_type_hints(_typecheckingstub__89e5796cbf6f6e46fdb25f920397c913245e572c7dd5f1cf36dd75192240eedf)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d751a874ba3bb47d9eb0acafadf08acd017021302e5509c3135ffc65701157de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class JobTaskGroupsTaskOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.job.JobTaskGroupsTaskOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3e0e8dcacaae8735214cd3cff3dc114cec2c8a9e9e7f3e87d28903d1b7f187dd)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="driver")
    def driver(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "driver"))

    @builtins.property
    @jsii.member(jsii_name="meta")
    def meta(self) -> _cdktf_9a9027ec.StringMap:
        return typing.cast(_cdktf_9a9027ec.StringMap, jsii.get(self, "meta"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="volumeMounts")
    def volume_mounts(self) -> "JobTaskGroupsTaskVolumeMountsList":
        return typing.cast("JobTaskGroupsTaskVolumeMountsList", jsii.get(self, "volumeMounts"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[JobTaskGroupsTask]:
        return typing.cast(typing.Optional[JobTaskGroupsTask], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[JobTaskGroupsTask]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__318977ed34242246cee7b0f84bd0dc3f041840453cc4b504770ff25339e240ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-nomad.job.JobTaskGroupsTaskVolumeMounts",
    jsii_struct_bases=[],
    name_mapping={},
)
class JobTaskGroupsTaskVolumeMounts:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "JobTaskGroupsTaskVolumeMounts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class JobTaskGroupsTaskVolumeMountsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.job.JobTaskGroupsTaskVolumeMountsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b21b55c2f78e6bf30fb4f8ff19808a7181bf744b363951d63a3100e62efa58ee)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "JobTaskGroupsTaskVolumeMountsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__952d8b0c95eca08373c7aa01376d9285a06bff2921ff6d668874e18cdc17ba6d)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("JobTaskGroupsTaskVolumeMountsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec468949fda748deb2ae15dfab82a947d6c460b8b40867928d2e055048af89e6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0e07ee6c035f7cf5d248de0f0a506d88153e3291941d2aafa2707fe5448682ec)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5bb951027814627355287c18e31987b816b75bda91e867c20b99aa2d505594c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class JobTaskGroupsTaskVolumeMountsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.job.JobTaskGroupsTaskVolumeMountsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__547a5ce46cbe6261dd2de82d155899388b6b0b4ebf0657665094fe8665dd9b75)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="destination")
    def destination(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destination"))

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "readOnly"))

    @builtins.property
    @jsii.member(jsii_name="volume")
    def volume(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volume"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[JobTaskGroupsTaskVolumeMounts]:
        return typing.cast(typing.Optional[JobTaskGroupsTaskVolumeMounts], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[JobTaskGroupsTaskVolumeMounts],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__217affc7f269d2bd160eaec9f8650f12f29fc6af0a2140b4860c9bb2894f04ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-nomad.job.JobTaskGroupsVolumes",
    jsii_struct_bases=[],
    name_mapping={},
)
class JobTaskGroupsVolumes:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "JobTaskGroupsVolumes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class JobTaskGroupsVolumesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.job.JobTaskGroupsVolumesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__21ea92071a65208fbed15eb445aac5838f7d4480afd124458399f8b5b7ee732c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "JobTaskGroupsVolumesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__801e308ec720f432311ca57ac95793922d9be43a7b1e5be087711a6cea3aa933)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("JobTaskGroupsVolumesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3fccc29d21c765b49cb6bb29e1389125870c11a302f1bfe4fddc2abef871e2c3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__567c84619cace21d5f0538101e3aeb9fad1d1dc7e15db2de299079ea11f056a9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__07175be20ab7df195e80a2cb720af1e1efa29978d3c372ad53576b6950381cbf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class JobTaskGroupsVolumesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.job.JobTaskGroupsVolumesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1d83afa70a650eff54e9239bd3e4f7a5c19a76f22dfa4775df5443d8076137cb)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "readOnly"))

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "source"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[JobTaskGroupsVolumes]:
        return typing.cast(typing.Optional[JobTaskGroupsVolumes], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[JobTaskGroupsVolumes]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05d5722fc250dec35a83d0b95a2324003a93f2cb935913ae027c6a5583456618)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-nomad.job.JobTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "update": "update"},
)
class JobTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#create Job#create}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#update Job#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80fdd78a4b76365a4ff7e85aea94e40ea25256faa32e8e589a49bb86705cfab2)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#create Job#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad/r/job#update Job#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "JobTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class JobTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.job.JobTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4ecadc8c40d68216392353ac6f807266e34d537e6ee33066dfdbcc4296c8d86b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="updateInput")
    def update_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updateInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a08f2a1086a5602e823c0147598ab085d747d4ac97451e035f25d00e39dae4e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__146f862010fade9e711971df3f5a08f3eb3ae92a892dbe22ea5d1be76a134d94)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[JobTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[JobTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[JobTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__253172634baf3c8a4c88f8a9c41e62ee6aea7096da4aaaeb1cfcb4777ec0d983)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Job",
    "JobConfig",
    "JobHcl2",
    "JobHcl2OutputReference",
    "JobTaskGroups",
    "JobTaskGroupsList",
    "JobTaskGroupsOutputReference",
    "JobTaskGroupsTask",
    "JobTaskGroupsTaskList",
    "JobTaskGroupsTaskOutputReference",
    "JobTaskGroupsTaskVolumeMounts",
    "JobTaskGroupsTaskVolumeMountsList",
    "JobTaskGroupsTaskVolumeMountsOutputReference",
    "JobTaskGroupsVolumes",
    "JobTaskGroupsVolumesList",
    "JobTaskGroupsVolumesOutputReference",
    "JobTimeouts",
    "JobTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__2e9e8f55e8cd582973ea2af0596c3f464a65eeff93736c25a32d8418f95816e6(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    jobspec: builtins.str,
    consul_token: typing.Optional[builtins.str] = None,
    deregister_on_destroy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    deregister_on_id_change: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    detach: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    hcl2: typing.Optional[typing.Union[JobHcl2, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    json: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    policy_override: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    purge_on_destroy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    timeouts: typing.Optional[typing.Union[JobTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    vault_token: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__8fb8ec063891f66a3277e2ad6b43cc0e717387a90bb815bd7ddc07631a2dac22(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__078359c3f89ed0777e18e7c61ec478f7f56176e4ba4263dffb1baf0957820cc5(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7595b919d310b786dc2cab77000fbbd8cbe4e901c9fa62ff858c4f361902f78a(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f687cae31fe60e332072b7d7f3bd7ecc219b10e171b759faf68a43b089ebf1d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25b21eee6956e6b7e3081e53c224b6ff325d6c6322b0ac1bc736a8c612392e8b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e8785aeb00fde63f7f2fd381d51d074a7fad6cc4b18529a79ede07b800806b3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06d42d2dbbbb7807360a092e71f5d5ced2c46fd3b3d17ff1dc9ab394cbf6089d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d70c54f9c259b625b45b1ac18a2f116cc5b86e061cceac2a829d3df809bca10(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab1535cba628eb65cb272df7d4485b56a5fcd08dcfe0b5e33964bf11fc8d706a(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b746a5a0c0e4fb728ade7483a54a2654d6d6058f91cd1254a5aaf73135ee485(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37af447459ed11d3aaa370e639e90e5dbccbaa7ec090fc274ebbf6a048d1f698(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    jobspec: builtins.str,
    consul_token: typing.Optional[builtins.str] = None,
    deregister_on_destroy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    deregister_on_id_change: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    detach: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    hcl2: typing.Optional[typing.Union[JobHcl2, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    json: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    policy_override: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    purge_on_destroy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    timeouts: typing.Optional[typing.Union[JobTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    vault_token: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00bd4c654c786dcc73121f9f1442771d83e52e3edaefba4adf383affd6577100(
    *,
    allow_fs: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    vars: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0dfe4c4c84d9591ec06b200ecabc44c8d87bf2a9eedd1c79ee76d124b6899f60(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e747dcc7b75cb9fe41793cc2dfa3640570f57fa5a807cd6990b8a8330177b010(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a8d7796aef5a81e4a73976993a96831fe4cbe2ff7cbed0fdb5b3aa42a49e9e3(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ade6e1ea51e55cdfe2dc15d47feea917884909cd2cc0cd809fb0811c08826096(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f98ecabe16ab8ae0f1afdf0266ea369f170e716c585af7faaf8d14dad9ba559(
    value: typing.Optional[JobHcl2],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2e57815fe27336e718941d9f838dd79f04f4f85662754ea2b047e2160dafd50(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4174be7e6ea47bfaa7492c476ff8ef114920798a22a5db27b3f1cba9c8f35494(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1e7af1e993f30420fecd5a9087af46f18872c5c349ad25a9c79bd27d707e2a2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e9507703514595225e2ee194be5456ed95a57bd8c545239212295add3c02931(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb7aebdde63eac4b6fd41cc706c59a2bc4bef01bc2f47e53e4c61bf1cce284e4(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3fa71dec6bc4c7ac624fd6f8783f0f2547c57522cebfea216af629af7cfda4a0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e17551086a7bb12812477d0b0ff001ff22c9242763f04bec266cb2e819042525(
    value: typing.Optional[JobTaskGroups],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ca0466ccefe816b2704bb015e6d6a659756d0ec160064db8f68166339e670e0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9c2e2f2371576f1ac125e8cb29a2a49350ba92d91126a02d0cf81bd11c2c6ce(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e764971cec5a5c4008de0642b0a36b751b80e9d0b2177420c498290f2db00197(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89e5796cbf6f6e46fdb25f920397c913245e572c7dd5f1cf36dd75192240eedf(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d751a874ba3bb47d9eb0acafadf08acd017021302e5509c3135ffc65701157de(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e0e8dcacaae8735214cd3cff3dc114cec2c8a9e9e7f3e87d28903d1b7f187dd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__318977ed34242246cee7b0f84bd0dc3f041840453cc4b504770ff25339e240ae(
    value: typing.Optional[JobTaskGroupsTask],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b21b55c2f78e6bf30fb4f8ff19808a7181bf744b363951d63a3100e62efa58ee(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__952d8b0c95eca08373c7aa01376d9285a06bff2921ff6d668874e18cdc17ba6d(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec468949fda748deb2ae15dfab82a947d6c460b8b40867928d2e055048af89e6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e07ee6c035f7cf5d248de0f0a506d88153e3291941d2aafa2707fe5448682ec(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bb951027814627355287c18e31987b816b75bda91e867c20b99aa2d505594c8(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__547a5ce46cbe6261dd2de82d155899388b6b0b4ebf0657665094fe8665dd9b75(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__217affc7f269d2bd160eaec9f8650f12f29fc6af0a2140b4860c9bb2894f04ec(
    value: typing.Optional[JobTaskGroupsTaskVolumeMounts],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21ea92071a65208fbed15eb445aac5838f7d4480afd124458399f8b5b7ee732c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__801e308ec720f432311ca57ac95793922d9be43a7b1e5be087711a6cea3aa933(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3fccc29d21c765b49cb6bb29e1389125870c11a302f1bfe4fddc2abef871e2c3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__567c84619cace21d5f0538101e3aeb9fad1d1dc7e15db2de299079ea11f056a9(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07175be20ab7df195e80a2cb720af1e1efa29978d3c372ad53576b6950381cbf(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d83afa70a650eff54e9239bd3e4f7a5c19a76f22dfa4775df5443d8076137cb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05d5722fc250dec35a83d0b95a2324003a93f2cb935913ae027c6a5583456618(
    value: typing.Optional[JobTaskGroupsVolumes],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80fdd78a4b76365a4ff7e85aea94e40ea25256faa32e8e589a49bb86705cfab2(
    *,
    create: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ecadc8c40d68216392353ac6f807266e34d537e6ee33066dfdbcc4296c8d86b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a08f2a1086a5602e823c0147598ab085d747d4ac97451e035f25d00e39dae4e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__146f862010fade9e711971df3f5a08f3eb3ae92a892dbe22ea5d1be76a134d94(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__253172634baf3c8a4c88f8a9c41e62ee6aea7096da4aaaeb1cfcb4777ec0d983(
    value: typing.Optional[typing.Union[JobTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
