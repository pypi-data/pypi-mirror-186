'''
# `provider`

Refer to the Terraform Registory for docs: [`nomad`](https://www.terraform.io/docs/providers/nomad).
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


class NomadProvider(
    _cdktf_9a9027ec.TerraformProvider,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-nomad.provider.NomadProvider",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/nomad nomad}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        address: builtins.str,
        alias: typing.Optional[builtins.str] = None,
        ca_file: typing.Optional[builtins.str] = None,
        ca_pem: typing.Optional[builtins.str] = None,
        cert_file: typing.Optional[builtins.str] = None,
        cert_pem: typing.Optional[builtins.str] = None,
        consul_token: typing.Optional[builtins.str] = None,
        headers: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["NomadProviderHeaders", typing.Dict[builtins.str, typing.Any]]]]] = None,
        http_auth: typing.Optional[builtins.str] = None,
        ignore_env_vars: typing.Optional[typing.Mapping[builtins.str, typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]] = None,
        key_file: typing.Optional[builtins.str] = None,
        key_pem: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        secret_id: typing.Optional[builtins.str] = None,
        vault_token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/nomad nomad} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param address: URL of the root of the target Nomad agent. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad#address NomadProvider#address}
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad#alias NomadProvider#alias}
        :param ca_file: A path to a PEM-encoded certificate authority used to verify the remote agent's certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad#ca_file NomadProvider#ca_file}
        :param ca_pem: PEM-encoded certificate authority used to verify the remote agent's certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad#ca_pem NomadProvider#ca_pem}
        :param cert_file: A path to a PEM-encoded certificate provided to the remote agent; requires use of key_file or key_pem. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad#cert_file NomadProvider#cert_file}
        :param cert_pem: PEM-encoded certificate provided to the remote agent; requires use of key_file or key_pem. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad#cert_pem NomadProvider#cert_pem}
        :param consul_token: Consul token to validate Consul Connect Service Identity policies specified in the job file. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad#consul_token NomadProvider#consul_token}
        :param headers: headers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad#headers NomadProvider#headers}
        :param http_auth: HTTP basic auth configuration. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad#http_auth NomadProvider#http_auth}
        :param ignore_env_vars: A set of environment variables that are ignored by the provider when configuring the Nomad API client. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad#ignore_env_vars NomadProvider#ignore_env_vars}
        :param key_file: A path to a PEM-encoded private key, required if cert_file or cert_pem is specified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad#key_file NomadProvider#key_file}
        :param key_pem: PEM-encoded private key, required if cert_file or cert_pem is specified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad#key_pem NomadProvider#key_pem}
        :param region: Region of the target Nomad agent. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad#region NomadProvider#region}
        :param secret_id: ACL token secret for API requests. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad#secret_id NomadProvider#secret_id}
        :param vault_token: Vault token if policies are specified in the job file. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad#vault_token NomadProvider#vault_token}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa1135b3e0a6e5d3f7edfef684226a9a3ae7c144ae366e8b37d5ae425d916fff)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = NomadProviderConfig(
            address=address,
            alias=alias,
            ca_file=ca_file,
            ca_pem=ca_pem,
            cert_file=cert_file,
            cert_pem=cert_pem,
            consul_token=consul_token,
            headers=headers,
            http_auth=http_auth,
            ignore_env_vars=ignore_env_vars,
            key_file=key_file,
            key_pem=key_pem,
            region=region,
            secret_id=secret_id,
            vault_token=vault_token,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="resetAlias")
    def reset_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlias", []))

    @jsii.member(jsii_name="resetCaFile")
    def reset_ca_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCaFile", []))

    @jsii.member(jsii_name="resetCaPem")
    def reset_ca_pem(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCaPem", []))

    @jsii.member(jsii_name="resetCertFile")
    def reset_cert_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertFile", []))

    @jsii.member(jsii_name="resetCertPem")
    def reset_cert_pem(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertPem", []))

    @jsii.member(jsii_name="resetConsulToken")
    def reset_consul_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConsulToken", []))

    @jsii.member(jsii_name="resetHeaders")
    def reset_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeaders", []))

    @jsii.member(jsii_name="resetHttpAuth")
    def reset_http_auth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpAuth", []))

    @jsii.member(jsii_name="resetIgnoreEnvVars")
    def reset_ignore_env_vars(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIgnoreEnvVars", []))

    @jsii.member(jsii_name="resetKeyFile")
    def reset_key_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyFile", []))

    @jsii.member(jsii_name="resetKeyPem")
    def reset_key_pem(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyPem", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @jsii.member(jsii_name="resetSecretId")
    def reset_secret_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecretId", []))

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
    @jsii.member(jsii_name="addressInput")
    def address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "addressInput"))

    @builtins.property
    @jsii.member(jsii_name="aliasInput")
    def alias_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aliasInput"))

    @builtins.property
    @jsii.member(jsii_name="caFileInput")
    def ca_file_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "caFileInput"))

    @builtins.property
    @jsii.member(jsii_name="caPemInput")
    def ca_pem_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "caPemInput"))

    @builtins.property
    @jsii.member(jsii_name="certFileInput")
    def cert_file_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certFileInput"))

    @builtins.property
    @jsii.member(jsii_name="certPemInput")
    def cert_pem_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certPemInput"))

    @builtins.property
    @jsii.member(jsii_name="consulTokenInput")
    def consul_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "consulTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="headersInput")
    def headers_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NomadProviderHeaders"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NomadProviderHeaders"]]], jsii.get(self, "headersInput"))

    @builtins.property
    @jsii.member(jsii_name="httpAuthInput")
    def http_auth_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "httpAuthInput"))

    @builtins.property
    @jsii.member(jsii_name="ignoreEnvVarsInput")
    def ignore_env_vars_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]], jsii.get(self, "ignoreEnvVarsInput"))

    @builtins.property
    @jsii.member(jsii_name="keyFileInput")
    def key_file_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyFileInput"))

    @builtins.property
    @jsii.member(jsii_name="keyPemInput")
    def key_pem_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyPemInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="secretIdInput")
    def secret_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretIdInput"))

    @builtins.property
    @jsii.member(jsii_name="vaultTokenInput")
    def vault_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vaultTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="address")
    def address(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "address"))

    @address.setter
    def address(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0beabfec8d7dd5d694d2cef5d7bc866119587940ba297f965ed9e5822f413b7a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "address", value)

    @builtins.property
    @jsii.member(jsii_name="alias")
    def alias(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alias"))

    @alias.setter
    def alias(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e5de19b3060e54bb9c7fdcfe267e89508ed0eb9eb0184bd9cd17c3d40a7169d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alias", value)

    @builtins.property
    @jsii.member(jsii_name="caFile")
    def ca_file(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "caFile"))

    @ca_file.setter
    def ca_file(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9aff273426dc241a2eb068c671e754330aaf4caecdbac2821e45b146e780d272)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "caFile", value)

    @builtins.property
    @jsii.member(jsii_name="caPem")
    def ca_pem(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "caPem"))

    @ca_pem.setter
    def ca_pem(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65ff0fb31e2b5251e5cdbef8c962770de40031fdafb80d09b48167b6a056bded)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "caPem", value)

    @builtins.property
    @jsii.member(jsii_name="certFile")
    def cert_file(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certFile"))

    @cert_file.setter
    def cert_file(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf67e2c037b05499cfe0245de807dc78ac7dfd606e54bef3181c717ce8f027d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certFile", value)

    @builtins.property
    @jsii.member(jsii_name="certPem")
    def cert_pem(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certPem"))

    @cert_pem.setter
    def cert_pem(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a34464dbc144eb2214380e5db8e2a958ee7a2b5c2f109aa24fbbf20d538fd2e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certPem", value)

    @builtins.property
    @jsii.member(jsii_name="consulToken")
    def consul_token(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "consulToken"))

    @consul_token.setter
    def consul_token(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30489e475fdf34de0e156c791593eaf7fd8fde64fd18bbb6289f36d1cdb9098c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "consulToken", value)

    @builtins.property
    @jsii.member(jsii_name="headers")
    def headers(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NomadProviderHeaders"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NomadProviderHeaders"]]], jsii.get(self, "headers"))

    @headers.setter
    def headers(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NomadProviderHeaders"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a3f592752af918242782f6ea70217202671f5edcc341fcf80f1cbb08d18bac6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headers", value)

    @builtins.property
    @jsii.member(jsii_name="httpAuth")
    def http_auth(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "httpAuth"))

    @http_auth.setter
    def http_auth(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c66bf4bc162a7eec972510b0510f85519cabd45b262100f9a2076b2c9e8a8c13)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpAuth", value)

    @builtins.property
    @jsii.member(jsii_name="ignoreEnvVars")
    def ignore_env_vars(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]], jsii.get(self, "ignoreEnvVars"))

    @ignore_env_vars.setter
    def ignore_env_vars(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49719b0f0dbe22ef93291f5e0a62835d823f044ce61032f370f1ba1cba2868f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoreEnvVars", value)

    @builtins.property
    @jsii.member(jsii_name="keyFile")
    def key_file(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyFile"))

    @key_file.setter
    def key_file(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__468babcbbdb16e5670b21e9f8eba58d5bcd8045ca7ed476d317c655d74c133dd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyFile", value)

    @builtins.property
    @jsii.member(jsii_name="keyPem")
    def key_pem(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyPem"))

    @key_pem.setter
    def key_pem(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85cd3c41f2552a4146e96aabcb245bb4299fffa94adf0880356e26445462328d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyPem", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "region"))

    @region.setter
    def region(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b04a884d329f7dcafe6ca5f0f57fbab564e8d3bb90b7b3efb1f5d2b2ec4d60a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="secretId")
    def secret_id(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretId"))

    @secret_id.setter
    def secret_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a02d46d72fb1046bdbb99d51171a00c00913f2085971c13e6a975aa870e3694b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretId", value)

    @builtins.property
    @jsii.member(jsii_name="vaultToken")
    def vault_token(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vaultToken"))

    @vault_token.setter
    def vault_token(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c35027298099735fca65479f06bd9ef7c18a82b71e2e6c73f48e0b6327262c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vaultToken", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-nomad.provider.NomadProviderConfig",
    jsii_struct_bases=[],
    name_mapping={
        "address": "address",
        "alias": "alias",
        "ca_file": "caFile",
        "ca_pem": "caPem",
        "cert_file": "certFile",
        "cert_pem": "certPem",
        "consul_token": "consulToken",
        "headers": "headers",
        "http_auth": "httpAuth",
        "ignore_env_vars": "ignoreEnvVars",
        "key_file": "keyFile",
        "key_pem": "keyPem",
        "region": "region",
        "secret_id": "secretId",
        "vault_token": "vaultToken",
    },
)
class NomadProviderConfig:
    def __init__(
        self,
        *,
        address: builtins.str,
        alias: typing.Optional[builtins.str] = None,
        ca_file: typing.Optional[builtins.str] = None,
        ca_pem: typing.Optional[builtins.str] = None,
        cert_file: typing.Optional[builtins.str] = None,
        cert_pem: typing.Optional[builtins.str] = None,
        consul_token: typing.Optional[builtins.str] = None,
        headers: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["NomadProviderHeaders", typing.Dict[builtins.str, typing.Any]]]]] = None,
        http_auth: typing.Optional[builtins.str] = None,
        ignore_env_vars: typing.Optional[typing.Mapping[builtins.str, typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]] = None,
        key_file: typing.Optional[builtins.str] = None,
        key_pem: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        secret_id: typing.Optional[builtins.str] = None,
        vault_token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param address: URL of the root of the target Nomad agent. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad#address NomadProvider#address}
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad#alias NomadProvider#alias}
        :param ca_file: A path to a PEM-encoded certificate authority used to verify the remote agent's certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad#ca_file NomadProvider#ca_file}
        :param ca_pem: PEM-encoded certificate authority used to verify the remote agent's certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad#ca_pem NomadProvider#ca_pem}
        :param cert_file: A path to a PEM-encoded certificate provided to the remote agent; requires use of key_file or key_pem. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad#cert_file NomadProvider#cert_file}
        :param cert_pem: PEM-encoded certificate provided to the remote agent; requires use of key_file or key_pem. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad#cert_pem NomadProvider#cert_pem}
        :param consul_token: Consul token to validate Consul Connect Service Identity policies specified in the job file. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad#consul_token NomadProvider#consul_token}
        :param headers: headers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad#headers NomadProvider#headers}
        :param http_auth: HTTP basic auth configuration. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad#http_auth NomadProvider#http_auth}
        :param ignore_env_vars: A set of environment variables that are ignored by the provider when configuring the Nomad API client. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad#ignore_env_vars NomadProvider#ignore_env_vars}
        :param key_file: A path to a PEM-encoded private key, required if cert_file or cert_pem is specified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad#key_file NomadProvider#key_file}
        :param key_pem: PEM-encoded private key, required if cert_file or cert_pem is specified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad#key_pem NomadProvider#key_pem}
        :param region: Region of the target Nomad agent. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad#region NomadProvider#region}
        :param secret_id: ACL token secret for API requests. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad#secret_id NomadProvider#secret_id}
        :param vault_token: Vault token if policies are specified in the job file. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad#vault_token NomadProvider#vault_token}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e759273490438086fe5dd3d88c084b63217b1cc6e133fcd010a5f3e4c7a37ada)
            check_type(argname="argument address", value=address, expected_type=type_hints["address"])
            check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
            check_type(argname="argument ca_file", value=ca_file, expected_type=type_hints["ca_file"])
            check_type(argname="argument ca_pem", value=ca_pem, expected_type=type_hints["ca_pem"])
            check_type(argname="argument cert_file", value=cert_file, expected_type=type_hints["cert_file"])
            check_type(argname="argument cert_pem", value=cert_pem, expected_type=type_hints["cert_pem"])
            check_type(argname="argument consul_token", value=consul_token, expected_type=type_hints["consul_token"])
            check_type(argname="argument headers", value=headers, expected_type=type_hints["headers"])
            check_type(argname="argument http_auth", value=http_auth, expected_type=type_hints["http_auth"])
            check_type(argname="argument ignore_env_vars", value=ignore_env_vars, expected_type=type_hints["ignore_env_vars"])
            check_type(argname="argument key_file", value=key_file, expected_type=type_hints["key_file"])
            check_type(argname="argument key_pem", value=key_pem, expected_type=type_hints["key_pem"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument secret_id", value=secret_id, expected_type=type_hints["secret_id"])
            check_type(argname="argument vault_token", value=vault_token, expected_type=type_hints["vault_token"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "address": address,
        }
        if alias is not None:
            self._values["alias"] = alias
        if ca_file is not None:
            self._values["ca_file"] = ca_file
        if ca_pem is not None:
            self._values["ca_pem"] = ca_pem
        if cert_file is not None:
            self._values["cert_file"] = cert_file
        if cert_pem is not None:
            self._values["cert_pem"] = cert_pem
        if consul_token is not None:
            self._values["consul_token"] = consul_token
        if headers is not None:
            self._values["headers"] = headers
        if http_auth is not None:
            self._values["http_auth"] = http_auth
        if ignore_env_vars is not None:
            self._values["ignore_env_vars"] = ignore_env_vars
        if key_file is not None:
            self._values["key_file"] = key_file
        if key_pem is not None:
            self._values["key_pem"] = key_pem
        if region is not None:
            self._values["region"] = region
        if secret_id is not None:
            self._values["secret_id"] = secret_id
        if vault_token is not None:
            self._values["vault_token"] = vault_token

    @builtins.property
    def address(self) -> builtins.str:
        '''URL of the root of the target Nomad agent.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad#address NomadProvider#address}
        '''
        result = self._values.get("address")
        assert result is not None, "Required property 'address' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def alias(self) -> typing.Optional[builtins.str]:
        '''Alias name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad#alias NomadProvider#alias}
        '''
        result = self._values.get("alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ca_file(self) -> typing.Optional[builtins.str]:
        '''A path to a PEM-encoded certificate authority used to verify the remote agent's certificate.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad#ca_file NomadProvider#ca_file}
        '''
        result = self._values.get("ca_file")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ca_pem(self) -> typing.Optional[builtins.str]:
        '''PEM-encoded certificate authority used to verify the remote agent's certificate.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad#ca_pem NomadProvider#ca_pem}
        '''
        result = self._values.get("ca_pem")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cert_file(self) -> typing.Optional[builtins.str]:
        '''A path to a PEM-encoded certificate provided to the remote agent; requires use of key_file or key_pem.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad#cert_file NomadProvider#cert_file}
        '''
        result = self._values.get("cert_file")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cert_pem(self) -> typing.Optional[builtins.str]:
        '''PEM-encoded certificate provided to the remote agent; requires use of key_file or key_pem.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad#cert_pem NomadProvider#cert_pem}
        '''
        result = self._values.get("cert_pem")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def consul_token(self) -> typing.Optional[builtins.str]:
        '''Consul token to validate Consul Connect Service Identity policies specified in the job file.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad#consul_token NomadProvider#consul_token}
        '''
        result = self._values.get("consul_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def headers(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NomadProviderHeaders"]]]:
        '''headers block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad#headers NomadProvider#headers}
        '''
        result = self._values.get("headers")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NomadProviderHeaders"]]], result)

    @builtins.property
    def http_auth(self) -> typing.Optional[builtins.str]:
        '''HTTP basic auth configuration.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad#http_auth NomadProvider#http_auth}
        '''
        result = self._values.get("http_auth")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ignore_env_vars(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]]:
        '''A set of environment variables that are ignored by the provider when configuring the Nomad API client.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad#ignore_env_vars NomadProvider#ignore_env_vars}
        '''
        result = self._values.get("ignore_env_vars")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]], result)

    @builtins.property
    def key_file(self) -> typing.Optional[builtins.str]:
        '''A path to a PEM-encoded private key, required if cert_file or cert_pem is specified.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad#key_file NomadProvider#key_file}
        '''
        result = self._values.get("key_file")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key_pem(self) -> typing.Optional[builtins.str]:
        '''PEM-encoded private key, required if cert_file or cert_pem is specified.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad#key_pem NomadProvider#key_pem}
        '''
        result = self._values.get("key_pem")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''Region of the target Nomad agent.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad#region NomadProvider#region}
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secret_id(self) -> typing.Optional[builtins.str]:
        '''ACL token secret for API requests.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad#secret_id NomadProvider#secret_id}
        '''
        result = self._values.get("secret_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vault_token(self) -> typing.Optional[builtins.str]:
        '''Vault token if policies are specified in the job file.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad#vault_token NomadProvider#vault_token}
        '''
        result = self._values.get("vault_token")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NomadProviderConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-nomad.provider.NomadProviderHeaders",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value": "value"},
)
class NomadProviderHeaders:
    def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
        '''
        :param name: The header name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad#name NomadProvider#name}
        :param value: The header value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad#value NomadProvider#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55e77394e5bf2f9bd34a37f003dbe588118fddb6f74338ed48dcede78167deb3)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "value": value,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''The header name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad#name NomadProvider#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''The header value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/nomad#value NomadProvider#value}
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NomadProviderHeaders(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "NomadProvider",
    "NomadProviderConfig",
    "NomadProviderHeaders",
]

publication.publish()

def _typecheckingstub__fa1135b3e0a6e5d3f7edfef684226a9a3ae7c144ae366e8b37d5ae425d916fff(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    address: builtins.str,
    alias: typing.Optional[builtins.str] = None,
    ca_file: typing.Optional[builtins.str] = None,
    ca_pem: typing.Optional[builtins.str] = None,
    cert_file: typing.Optional[builtins.str] = None,
    cert_pem: typing.Optional[builtins.str] = None,
    consul_token: typing.Optional[builtins.str] = None,
    headers: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NomadProviderHeaders, typing.Dict[builtins.str, typing.Any]]]]] = None,
    http_auth: typing.Optional[builtins.str] = None,
    ignore_env_vars: typing.Optional[typing.Mapping[builtins.str, typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]] = None,
    key_file: typing.Optional[builtins.str] = None,
    key_pem: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    secret_id: typing.Optional[builtins.str] = None,
    vault_token: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0beabfec8d7dd5d694d2cef5d7bc866119587940ba297f965ed9e5822f413b7a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e5de19b3060e54bb9c7fdcfe267e89508ed0eb9eb0184bd9cd17c3d40a7169d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9aff273426dc241a2eb068c671e754330aaf4caecdbac2821e45b146e780d272(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65ff0fb31e2b5251e5cdbef8c962770de40031fdafb80d09b48167b6a056bded(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf67e2c037b05499cfe0245de807dc78ac7dfd606e54bef3181c717ce8f027d2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a34464dbc144eb2214380e5db8e2a958ee7a2b5c2f109aa24fbbf20d538fd2e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30489e475fdf34de0e156c791593eaf7fd8fde64fd18bbb6289f36d1cdb9098c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a3f592752af918242782f6ea70217202671f5edcc341fcf80f1cbb08d18bac6(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NomadProviderHeaders]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c66bf4bc162a7eec972510b0510f85519cabd45b262100f9a2076b2c9e8a8c13(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49719b0f0dbe22ef93291f5e0a62835d823f044ce61032f370f1ba1cba2868f2(
    value: typing.Optional[typing.Mapping[builtins.str, typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__468babcbbdb16e5670b21e9f8eba58d5bcd8045ca7ed476d317c655d74c133dd(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85cd3c41f2552a4146e96aabcb245bb4299fffa94adf0880356e26445462328d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b04a884d329f7dcafe6ca5f0f57fbab564e8d3bb90b7b3efb1f5d2b2ec4d60a7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a02d46d72fb1046bdbb99d51171a00c00913f2085971c13e6a975aa870e3694b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c35027298099735fca65479f06bd9ef7c18a82b71e2e6c73f48e0b6327262c6(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e759273490438086fe5dd3d88c084b63217b1cc6e133fcd010a5f3e4c7a37ada(
    *,
    address: builtins.str,
    alias: typing.Optional[builtins.str] = None,
    ca_file: typing.Optional[builtins.str] = None,
    ca_pem: typing.Optional[builtins.str] = None,
    cert_file: typing.Optional[builtins.str] = None,
    cert_pem: typing.Optional[builtins.str] = None,
    consul_token: typing.Optional[builtins.str] = None,
    headers: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NomadProviderHeaders, typing.Dict[builtins.str, typing.Any]]]]] = None,
    http_auth: typing.Optional[builtins.str] = None,
    ignore_env_vars: typing.Optional[typing.Mapping[builtins.str, typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]] = None,
    key_file: typing.Optional[builtins.str] = None,
    key_pem: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    secret_id: typing.Optional[builtins.str] = None,
    vault_token: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55e77394e5bf2f9bd34a37f003dbe588118fddb6f74338ed48dcede78167deb3(
    *,
    name: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass
