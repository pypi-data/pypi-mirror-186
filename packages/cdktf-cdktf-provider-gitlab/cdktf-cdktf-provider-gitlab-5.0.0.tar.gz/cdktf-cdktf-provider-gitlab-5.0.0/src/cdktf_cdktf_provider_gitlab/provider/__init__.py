'''
# `provider`

Refer to the Terraform Registory for docs: [`gitlab`](https://www.terraform.io/docs/providers/gitlab).
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


class GitlabProvider(
    _cdktf_9a9027ec.TerraformProvider,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-gitlab.provider.GitlabProvider",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/gitlab gitlab}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        token: builtins.str,
        alias: typing.Optional[builtins.str] = None,
        base_url: typing.Optional[builtins.str] = None,
        cacert_file: typing.Optional[builtins.str] = None,
        client_cert: typing.Optional[builtins.str] = None,
        client_key: typing.Optional[builtins.str] = None,
        early_auth_check: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        insecure: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/gitlab gitlab} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param token: The OAuth2 Token, Project, Group, Personal Access Token or CI Job Token used to connect to GitLab. The OAuth method is used in this provider for authentication (using Bearer authorization token). See https://docs.gitlab.com/ee/api/#authentication for details. It may be sourced from the ``GITLAB_TOKEN`` environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab#token GitlabProvider#token}
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab#alias GitlabProvider#alias}
        :param base_url: This is the target GitLab base API endpoint. Providing a value is a requirement when working with GitLab CE or GitLab Enterprise e.g. ``https://my.gitlab.server/api/v4/``. It is optional to provide this value and it can also be sourced from the ``GITLAB_BASE_URL`` environment variable. The value must end with a slash. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab#base_url GitlabProvider#base_url}
        :param cacert_file: This is a file containing the ca cert to verify the gitlab instance. This is available for use when working with GitLab CE or Gitlab Enterprise with a locally-issued or self-signed certificate chain. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab#cacert_file GitlabProvider#cacert_file}
        :param client_cert: File path to client certificate when GitLab instance is behind company proxy. File must contain PEM encoded data. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab#client_cert GitlabProvider#client_cert}
        :param client_key: File path to client key when GitLab instance is behind company proxy. File must contain PEM encoded data. Required when ``client_cert`` is set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab#client_key GitlabProvider#client_key}
        :param early_auth_check: (Experimental) By default the provider does a dummy request to get the current user in order to verify that the provider configuration is correct and the GitLab API is reachable. Turn it off, to skip this check. This may be useful if the GitLab instance does not yet exist and is created within the same terraform module. This is an experimental feature and may change in the future. Please make sure to always keep backups of your state. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab#early_auth_check GitlabProvider#early_auth_check}
        :param insecure: When set to true this disables SSL verification of the connection to the GitLab instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab#insecure GitlabProvider#insecure}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d356a8a4a7f18b890dbe59582765c88e0cacb8aa26068a378295802d72717509)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = GitlabProviderConfig(
            token=token,
            alias=alias,
            base_url=base_url,
            cacert_file=cacert_file,
            client_cert=client_cert,
            client_key=client_key,
            early_auth_check=early_auth_check,
            insecure=insecure,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="resetAlias")
    def reset_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlias", []))

    @jsii.member(jsii_name="resetBaseUrl")
    def reset_base_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBaseUrl", []))

    @jsii.member(jsii_name="resetCacertFile")
    def reset_cacert_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCacertFile", []))

    @jsii.member(jsii_name="resetClientCert")
    def reset_client_cert(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientCert", []))

    @jsii.member(jsii_name="resetClientKey")
    def reset_client_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientKey", []))

    @jsii.member(jsii_name="resetEarlyAuthCheck")
    def reset_early_auth_check(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEarlyAuthCheck", []))

    @jsii.member(jsii_name="resetInsecure")
    def reset_insecure(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInsecure", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="aliasInput")
    def alias_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aliasInput"))

    @builtins.property
    @jsii.member(jsii_name="baseUrlInput")
    def base_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "baseUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="cacertFileInput")
    def cacert_file_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cacertFileInput"))

    @builtins.property
    @jsii.member(jsii_name="clientCertInput")
    def client_cert_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientCertInput"))

    @builtins.property
    @jsii.member(jsii_name="clientKeyInput")
    def client_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="earlyAuthCheckInput")
    def early_auth_check_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "earlyAuthCheckInput"))

    @builtins.property
    @jsii.member(jsii_name="insecureInput")
    def insecure_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "insecureInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenInput")
    def token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenInput"))

    @builtins.property
    @jsii.member(jsii_name="alias")
    def alias(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alias"))

    @alias.setter
    def alias(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80bf881f2529219cf047ec39c744d03a8d2af60d02e7decd7ce3eec83b10e075)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alias", value)

    @builtins.property
    @jsii.member(jsii_name="baseUrl")
    def base_url(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "baseUrl"))

    @base_url.setter
    def base_url(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9d994df983a9f1dcd3ba52213715df406343e24ad0adc8c23dbda88d989aec8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "baseUrl", value)

    @builtins.property
    @jsii.member(jsii_name="cacertFile")
    def cacert_file(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cacertFile"))

    @cacert_file.setter
    def cacert_file(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2c2d3cf9242f0a83a33c85a314ed1b52427a2feb430a3f3b2406a9b64e9939f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cacertFile", value)

    @builtins.property
    @jsii.member(jsii_name="clientCert")
    def client_cert(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientCert"))

    @client_cert.setter
    def client_cert(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__607852ccbcb31e35a4e222cdb548458312e4cfac7ddbf3d5b38402ede5048b05)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientCert", value)

    @builtins.property
    @jsii.member(jsii_name="clientKey")
    def client_key(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientKey"))

    @client_key.setter
    def client_key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18614c7c24e7fa3b433d290a1182b14c7677e04d5d66d98e590f5a60805b0dad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientKey", value)

    @builtins.property
    @jsii.member(jsii_name="earlyAuthCheck")
    def early_auth_check(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "earlyAuthCheck"))

    @early_auth_check.setter
    def early_auth_check(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4e98bb05510b21a8ebc2388544d111deb1e2fa6dd8ccb5b2a6c5cc588b4e54b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "earlyAuthCheck", value)

    @builtins.property
    @jsii.member(jsii_name="insecure")
    def insecure(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "insecure"))

    @insecure.setter
    def insecure(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed57f47541ee68f36118261a8419b1fd87b8a76ade8b9d75a82d2daae004ad78)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "insecure", value)

    @builtins.property
    @jsii.member(jsii_name="token")
    def token(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "token"))

    @token.setter
    def token(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f18ba9dfb8cd7c594e2c8fd9a4767e9061728e975d7d5876fe4ebfdc348de43)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "token", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-gitlab.provider.GitlabProviderConfig",
    jsii_struct_bases=[],
    name_mapping={
        "token": "token",
        "alias": "alias",
        "base_url": "baseUrl",
        "cacert_file": "cacertFile",
        "client_cert": "clientCert",
        "client_key": "clientKey",
        "early_auth_check": "earlyAuthCheck",
        "insecure": "insecure",
    },
)
class GitlabProviderConfig:
    def __init__(
        self,
        *,
        token: builtins.str,
        alias: typing.Optional[builtins.str] = None,
        base_url: typing.Optional[builtins.str] = None,
        cacert_file: typing.Optional[builtins.str] = None,
        client_cert: typing.Optional[builtins.str] = None,
        client_key: typing.Optional[builtins.str] = None,
        early_auth_check: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        insecure: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param token: The OAuth2 Token, Project, Group, Personal Access Token or CI Job Token used to connect to GitLab. The OAuth method is used in this provider for authentication (using Bearer authorization token). See https://docs.gitlab.com/ee/api/#authentication for details. It may be sourced from the ``GITLAB_TOKEN`` environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab#token GitlabProvider#token}
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab#alias GitlabProvider#alias}
        :param base_url: This is the target GitLab base API endpoint. Providing a value is a requirement when working with GitLab CE or GitLab Enterprise e.g. ``https://my.gitlab.server/api/v4/``. It is optional to provide this value and it can also be sourced from the ``GITLAB_BASE_URL`` environment variable. The value must end with a slash. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab#base_url GitlabProvider#base_url}
        :param cacert_file: This is a file containing the ca cert to verify the gitlab instance. This is available for use when working with GitLab CE or Gitlab Enterprise with a locally-issued or self-signed certificate chain. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab#cacert_file GitlabProvider#cacert_file}
        :param client_cert: File path to client certificate when GitLab instance is behind company proxy. File must contain PEM encoded data. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab#client_cert GitlabProvider#client_cert}
        :param client_key: File path to client key when GitLab instance is behind company proxy. File must contain PEM encoded data. Required when ``client_cert`` is set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab#client_key GitlabProvider#client_key}
        :param early_auth_check: (Experimental) By default the provider does a dummy request to get the current user in order to verify that the provider configuration is correct and the GitLab API is reachable. Turn it off, to skip this check. This may be useful if the GitLab instance does not yet exist and is created within the same terraform module. This is an experimental feature and may change in the future. Please make sure to always keep backups of your state. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab#early_auth_check GitlabProvider#early_auth_check}
        :param insecure: When set to true this disables SSL verification of the connection to the GitLab instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab#insecure GitlabProvider#insecure}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e118e43ef31e36351e1b19d38c03f02cfcc9765f8903670245d7e7156c186383)
            check_type(argname="argument token", value=token, expected_type=type_hints["token"])
            check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
            check_type(argname="argument base_url", value=base_url, expected_type=type_hints["base_url"])
            check_type(argname="argument cacert_file", value=cacert_file, expected_type=type_hints["cacert_file"])
            check_type(argname="argument client_cert", value=client_cert, expected_type=type_hints["client_cert"])
            check_type(argname="argument client_key", value=client_key, expected_type=type_hints["client_key"])
            check_type(argname="argument early_auth_check", value=early_auth_check, expected_type=type_hints["early_auth_check"])
            check_type(argname="argument insecure", value=insecure, expected_type=type_hints["insecure"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "token": token,
        }
        if alias is not None:
            self._values["alias"] = alias
        if base_url is not None:
            self._values["base_url"] = base_url
        if cacert_file is not None:
            self._values["cacert_file"] = cacert_file
        if client_cert is not None:
            self._values["client_cert"] = client_cert
        if client_key is not None:
            self._values["client_key"] = client_key
        if early_auth_check is not None:
            self._values["early_auth_check"] = early_auth_check
        if insecure is not None:
            self._values["insecure"] = insecure

    @builtins.property
    def token(self) -> builtins.str:
        '''The OAuth2 Token, Project, Group, Personal Access Token or CI Job Token used to connect to GitLab.

        The OAuth method is used in this provider for authentication (using Bearer authorization token). See https://docs.gitlab.com/ee/api/#authentication for details. It may be sourced from the ``GITLAB_TOKEN`` environment variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab#token GitlabProvider#token}
        '''
        result = self._values.get("token")
        assert result is not None, "Required property 'token' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def alias(self) -> typing.Optional[builtins.str]:
        '''Alias name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab#alias GitlabProvider#alias}
        '''
        result = self._values.get("alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def base_url(self) -> typing.Optional[builtins.str]:
        '''This is the target GitLab base API endpoint.

        Providing a value is a requirement when working with GitLab CE or GitLab Enterprise e.g. ``https://my.gitlab.server/api/v4/``. It is optional to provide this value and it can also be sourced from the ``GITLAB_BASE_URL`` environment variable. The value must end with a slash.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab#base_url GitlabProvider#base_url}
        '''
        result = self._values.get("base_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cacert_file(self) -> typing.Optional[builtins.str]:
        '''This is a file containing the ca cert to verify the gitlab instance.

        This is available for use when working with GitLab CE or Gitlab Enterprise with a locally-issued or self-signed certificate chain.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab#cacert_file GitlabProvider#cacert_file}
        '''
        result = self._values.get("cacert_file")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_cert(self) -> typing.Optional[builtins.str]:
        '''File path to client certificate when GitLab instance is behind company proxy. File must contain PEM encoded data.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab#client_cert GitlabProvider#client_cert}
        '''
        result = self._values.get("client_cert")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_key(self) -> typing.Optional[builtins.str]:
        '''File path to client key when GitLab instance is behind company proxy.

        File must contain PEM encoded data. Required when ``client_cert`` is set.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab#client_key GitlabProvider#client_key}
        '''
        result = self._values.get("client_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def early_auth_check(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''(Experimental) By default the provider does a dummy request to get the current user in order to verify that the provider configuration is correct and the GitLab API is reachable.

        Turn it off, to skip this check. This may be useful if the GitLab instance does not yet exist and is created within the same terraform module. This is an experimental feature and may change in the future. Please make sure to always keep backups of your state.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab#early_auth_check GitlabProvider#early_auth_check}
        '''
        result = self._values.get("early_auth_check")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def insecure(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''When set to true this disables SSL verification of the connection to the GitLab instance.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab#insecure GitlabProvider#insecure}
        '''
        result = self._values.get("insecure")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GitlabProviderConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "GitlabProvider",
    "GitlabProviderConfig",
]

publication.publish()

def _typecheckingstub__d356a8a4a7f18b890dbe59582765c88e0cacb8aa26068a378295802d72717509(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    token: builtins.str,
    alias: typing.Optional[builtins.str] = None,
    base_url: typing.Optional[builtins.str] = None,
    cacert_file: typing.Optional[builtins.str] = None,
    client_cert: typing.Optional[builtins.str] = None,
    client_key: typing.Optional[builtins.str] = None,
    early_auth_check: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    insecure: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80bf881f2529219cf047ec39c744d03a8d2af60d02e7decd7ce3eec83b10e075(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9d994df983a9f1dcd3ba52213715df406343e24ad0adc8c23dbda88d989aec8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2c2d3cf9242f0a83a33c85a314ed1b52427a2feb430a3f3b2406a9b64e9939f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__607852ccbcb31e35a4e222cdb548458312e4cfac7ddbf3d5b38402ede5048b05(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18614c7c24e7fa3b433d290a1182b14c7677e04d5d66d98e590f5a60805b0dad(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4e98bb05510b21a8ebc2388544d111deb1e2fa6dd8ccb5b2a6c5cc588b4e54b(
    value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed57f47541ee68f36118261a8419b1fd87b8a76ade8b9d75a82d2daae004ad78(
    value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f18ba9dfb8cd7c594e2c8fd9a4767e9061728e975d7d5876fe4ebfdc348de43(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e118e43ef31e36351e1b19d38c03f02cfcc9765f8903670245d7e7156c186383(
    *,
    token: builtins.str,
    alias: typing.Optional[builtins.str] = None,
    base_url: typing.Optional[builtins.str] = None,
    cacert_file: typing.Optional[builtins.str] = None,
    client_cert: typing.Optional[builtins.str] = None,
    client_key: typing.Optional[builtins.str] = None,
    early_auth_check: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    insecure: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass
