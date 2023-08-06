'''
# `snowflake_saml_integration`

Refer to the Terraform Registory for docs: [`snowflake_saml_integration`](https://www.terraform.io/docs/providers/snowflake/r/saml_integration).
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


class SamlIntegration(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-snowflake.samlIntegration.SamlIntegration",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/snowflake/r/saml_integration snowflake_saml_integration}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        saml2_issuer: builtins.str,
        saml2_provider: builtins.str,
        saml2_sso_url: builtins.str,
        saml2_x509_cert: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        saml2_enable_sp_initiated: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        saml2_force_authn: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        saml2_post_logout_redirect_url: typing.Optional[builtins.str] = None,
        saml2_requested_nameid_format: typing.Optional[builtins.str] = None,
        saml2_sign_request: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        saml2_snowflake_acs_url: typing.Optional[builtins.str] = None,
        saml2_snowflake_issuer_url: typing.Optional[builtins.str] = None,
        saml2_snowflake_x509_cert: typing.Optional[builtins.str] = None,
        saml2_sp_initiated_login_page_label: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/snowflake/r/saml_integration snowflake_saml_integration} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Specifies the name of the SAML2 integration. This name follows the rules for Object Identifiers. The name should be unique among security integrations in your account. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/saml_integration#name SamlIntegration#name}
        :param saml2_issuer: The string containing the IdP EntityID / Issuer. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/saml_integration#saml2_issuer SamlIntegration#saml2_issuer}
        :param saml2_provider: The string describing the IdP. One of the following: OKTA, ADFS, Custom. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/saml_integration#saml2_provider SamlIntegration#saml2_provider}
        :param saml2_sso_url: The string containing the IdP SSO URL, where the user should be redirected by Snowflake (the Service Provider) with a SAML AuthnRequest message. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/saml_integration#saml2_sso_url SamlIntegration#saml2_sso_url}
        :param saml2_x509_cert: The Base64 encoded IdP signing certificate on a single line without the leading -----BEGIN CERTIFICATE----- and ending -----END CERTIFICATE----- markers. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/saml_integration#saml2_x509_cert SamlIntegration#saml2_x509_cert}
        :param enabled: Specifies whether this security integration is enabled or disabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/saml_integration#enabled SamlIntegration#enabled}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/saml_integration#id SamlIntegration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param saml2_enable_sp_initiated: The Boolean indicating if the Log In With button will be shown on the login page. TRUE: displays the Log in WIth button on the login page. FALSE: does not display the Log in With button on the login page. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/saml_integration#saml2_enable_sp_initiated SamlIntegration#saml2_enable_sp_initiated}
        :param saml2_force_authn: The Boolean indicating whether users, during the initial authentication flow, are forced to authenticate again to access Snowflake. When set to TRUE, Snowflake sets the ForceAuthn SAML parameter to TRUE in the outgoing request from Snowflake to the identity provider. TRUE: forces users to authenticate again to access Snowflake, even if a valid session with the identity provider exists. FALSE: does not force users to authenticate again to access Snowflake. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/saml_integration#saml2_force_authn SamlIntegration#saml2_force_authn}
        :param saml2_post_logout_redirect_url: The endpoint to which Snowflake redirects users after clicking the Log Out button in the classic Snowflake web interface. Snowflake terminates the Snowflake session upon redirecting to the specified endpoint. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/saml_integration#saml2_post_logout_redirect_url SamlIntegration#saml2_post_logout_redirect_url}
        :param saml2_requested_nameid_format: The SAML NameID format allows Snowflake to set an expectation of the identifying attribute of the user (i.e. SAML Subject) in the SAML assertion from the IdP to ensure a valid authentication to Snowflake. If a value is not specified, Snowflake sends the urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress value in the authentication request to the IdP. NameID must be one of the following values: urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified, urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress, urn:oasis:names:tc:SAML:1.1:nameid-format:X509SubjectName, urn:oasis:names:tc:SAML:1.1:nameid-format:WindowsDomainQualifiedName, urn:oasis:names:tc:SAML:2.0:nameid-format:kerberos, urn:oasis:names:tc:SAML:2.0:nameid-format:persistent, urn:oasis:names:tc:SAML:2.0:nameid-format:transient . Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/saml_integration#saml2_requested_nameid_format SamlIntegration#saml2_requested_nameid_format}
        :param saml2_sign_request: The Boolean indicating whether SAML requests are signed. TRUE: allows SAML requests to be signed. FALSE: does not allow SAML requests to be signed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/saml_integration#saml2_sign_request SamlIntegration#saml2_sign_request}
        :param saml2_snowflake_acs_url: The string containing the Snowflake Assertion Consumer Service URL to which the IdP will send its SAML authentication response back to Snowflake. This property will be set in the SAML authentication request generated by Snowflake when initiating a SAML SSO operation with the IdP. If an incorrect value is specified, Snowflake returns an error message indicating the acceptable values to use. Default: https://<account_locator>..snowflakecomputing.com/fed/login Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/saml_integration#saml2_snowflake_acs_url SamlIntegration#saml2_snowflake_acs_url}
        :param saml2_snowflake_issuer_url: The string containing the EntityID / Issuer for the Snowflake service provider. If an incorrect value is specified, Snowflake returns an error message indicating the acceptable values to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/saml_integration#saml2_snowflake_issuer_url SamlIntegration#saml2_snowflake_issuer_url}
        :param saml2_snowflake_x509_cert: The Base64 encoded self-signed certificate generated by Snowflake for use with Encrypting SAML Assertions and Signed SAML Requests. You must have at least one of these features (encrypted SAML assertions or signed SAML responses) enabled in your Snowflake account to access the certificate value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/saml_integration#saml2_snowflake_x509_cert SamlIntegration#saml2_snowflake_x509_cert}
        :param saml2_sp_initiated_login_page_label: The string containing the label to display after the Log In With button on the login page. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/saml_integration#saml2_sp_initiated_login_page_label SamlIntegration#saml2_sp_initiated_login_page_label}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ef5e3f888980d88f02fb4ff5bfb8d32760c447671c365faddd78a3c1971a9d5)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SamlIntegrationConfig(
            name=name,
            saml2_issuer=saml2_issuer,
            saml2_provider=saml2_provider,
            saml2_sso_url=saml2_sso_url,
            saml2_x509_cert=saml2_x509_cert,
            enabled=enabled,
            id=id,
            saml2_enable_sp_initiated=saml2_enable_sp_initiated,
            saml2_force_authn=saml2_force_authn,
            saml2_post_logout_redirect_url=saml2_post_logout_redirect_url,
            saml2_requested_nameid_format=saml2_requested_nameid_format,
            saml2_sign_request=saml2_sign_request,
            saml2_snowflake_acs_url=saml2_snowflake_acs_url,
            saml2_snowflake_issuer_url=saml2_snowflake_issuer_url,
            saml2_snowflake_x509_cert=saml2_snowflake_x509_cert,
            saml2_sp_initiated_login_page_label=saml2_sp_initiated_login_page_label,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetSaml2EnableSpInitiated")
    def reset_saml2_enable_sp_initiated(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSaml2EnableSpInitiated", []))

    @jsii.member(jsii_name="resetSaml2ForceAuthn")
    def reset_saml2_force_authn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSaml2ForceAuthn", []))

    @jsii.member(jsii_name="resetSaml2PostLogoutRedirectUrl")
    def reset_saml2_post_logout_redirect_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSaml2PostLogoutRedirectUrl", []))

    @jsii.member(jsii_name="resetSaml2RequestedNameidFormat")
    def reset_saml2_requested_nameid_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSaml2RequestedNameidFormat", []))

    @jsii.member(jsii_name="resetSaml2SignRequest")
    def reset_saml2_sign_request(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSaml2SignRequest", []))

    @jsii.member(jsii_name="resetSaml2SnowflakeAcsUrl")
    def reset_saml2_snowflake_acs_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSaml2SnowflakeAcsUrl", []))

    @jsii.member(jsii_name="resetSaml2SnowflakeIssuerUrl")
    def reset_saml2_snowflake_issuer_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSaml2SnowflakeIssuerUrl", []))

    @jsii.member(jsii_name="resetSaml2SnowflakeX509Cert")
    def reset_saml2_snowflake_x509_cert(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSaml2SnowflakeX509Cert", []))

    @jsii.member(jsii_name="resetSaml2SpInitiatedLoginPageLabel")
    def reset_saml2_sp_initiated_login_page_label(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSaml2SpInitiatedLoginPageLabel", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="createdOn")
    def created_on(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdOn"))

    @builtins.property
    @jsii.member(jsii_name="saml2DigestMethodsUsed")
    def saml2_digest_methods_used(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "saml2DigestMethodsUsed"))

    @builtins.property
    @jsii.member(jsii_name="saml2SignatureMethodsUsed")
    def saml2_signature_methods_used(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "saml2SignatureMethodsUsed"))

    @builtins.property
    @jsii.member(jsii_name="saml2SnowflakeMetadata")
    def saml2_snowflake_metadata(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "saml2SnowflakeMetadata"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="saml2EnableSpInitiatedInput")
    def saml2_enable_sp_initiated_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "saml2EnableSpInitiatedInput"))

    @builtins.property
    @jsii.member(jsii_name="saml2ForceAuthnInput")
    def saml2_force_authn_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "saml2ForceAuthnInput"))

    @builtins.property
    @jsii.member(jsii_name="saml2IssuerInput")
    def saml2_issuer_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "saml2IssuerInput"))

    @builtins.property
    @jsii.member(jsii_name="saml2PostLogoutRedirectUrlInput")
    def saml2_post_logout_redirect_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "saml2PostLogoutRedirectUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="saml2ProviderInput")
    def saml2_provider_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "saml2ProviderInput"))

    @builtins.property
    @jsii.member(jsii_name="saml2RequestedNameidFormatInput")
    def saml2_requested_nameid_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "saml2RequestedNameidFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="saml2SignRequestInput")
    def saml2_sign_request_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "saml2SignRequestInput"))

    @builtins.property
    @jsii.member(jsii_name="saml2SnowflakeAcsUrlInput")
    def saml2_snowflake_acs_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "saml2SnowflakeAcsUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="saml2SnowflakeIssuerUrlInput")
    def saml2_snowflake_issuer_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "saml2SnowflakeIssuerUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="saml2SnowflakeX509CertInput")
    def saml2_snowflake_x509_cert_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "saml2SnowflakeX509CertInput"))

    @builtins.property
    @jsii.member(jsii_name="saml2SpInitiatedLoginPageLabelInput")
    def saml2_sp_initiated_login_page_label_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "saml2SpInitiatedLoginPageLabelInput"))

    @builtins.property
    @jsii.member(jsii_name="saml2SsoUrlInput")
    def saml2_sso_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "saml2SsoUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="saml2X509CertInput")
    def saml2_x509_cert_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "saml2X509CertInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__0abf2b8885a5e0ac0dfe6ddb58b2485c18b54a82496183a09549d1f0afe76746)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__847e672722c5a90eea58c73fb092b5232df15dead2f7cbf40b58975f6df1a5c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57052e84d447cdecfc67b3b197b7ae287ede531ff3e4188e4d96c646c1d55841)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="saml2EnableSpInitiated")
    def saml2_enable_sp_initiated(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "saml2EnableSpInitiated"))

    @saml2_enable_sp_initiated.setter
    def saml2_enable_sp_initiated(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df3fa14cc7b2e23c9fe5bf0afa4c9839e86e76de249f1080b6051f087fdb1235)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "saml2EnableSpInitiated", value)

    @builtins.property
    @jsii.member(jsii_name="saml2ForceAuthn")
    def saml2_force_authn(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "saml2ForceAuthn"))

    @saml2_force_authn.setter
    def saml2_force_authn(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3605d0361def17141e911f30cfcf2d9856d494aebcfa874e2ce71a585381d371)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "saml2ForceAuthn", value)

    @builtins.property
    @jsii.member(jsii_name="saml2Issuer")
    def saml2_issuer(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "saml2Issuer"))

    @saml2_issuer.setter
    def saml2_issuer(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3598d3b2f548d9ec47dcd7fb63130e59382377965c928375f7c0f20e9a06d1a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "saml2Issuer", value)

    @builtins.property
    @jsii.member(jsii_name="saml2PostLogoutRedirectUrl")
    def saml2_post_logout_redirect_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "saml2PostLogoutRedirectUrl"))

    @saml2_post_logout_redirect_url.setter
    def saml2_post_logout_redirect_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49254a90202aea56f3c62d686e35c10bf9a367f6e6cf0c7452c3c7bcb6b60f88)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "saml2PostLogoutRedirectUrl", value)

    @builtins.property
    @jsii.member(jsii_name="saml2Provider")
    def saml2_provider(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "saml2Provider"))

    @saml2_provider.setter
    def saml2_provider(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4c89dc4d6ad82d1a0afa6c6aa9e19dfa7d688d1d19bdc597ebec765cfc38cd8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "saml2Provider", value)

    @builtins.property
    @jsii.member(jsii_name="saml2RequestedNameidFormat")
    def saml2_requested_nameid_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "saml2RequestedNameidFormat"))

    @saml2_requested_nameid_format.setter
    def saml2_requested_nameid_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d7b883044c0df6cff0be7f498c81f3ae8d38ee486c815f06f43ce2fb0b9b926)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "saml2RequestedNameidFormat", value)

    @builtins.property
    @jsii.member(jsii_name="saml2SignRequest")
    def saml2_sign_request(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "saml2SignRequest"))

    @saml2_sign_request.setter
    def saml2_sign_request(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8095b8c5a94f6ea403b7d0cd8ec5c2104b47faffa4f040e242e2094782cdd61d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "saml2SignRequest", value)

    @builtins.property
    @jsii.member(jsii_name="saml2SnowflakeAcsUrl")
    def saml2_snowflake_acs_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "saml2SnowflakeAcsUrl"))

    @saml2_snowflake_acs_url.setter
    def saml2_snowflake_acs_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__298ea233832bb5de59365acab62fd8b2a32d42f3d60de7e4136ffba0ab63e678)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "saml2SnowflakeAcsUrl", value)

    @builtins.property
    @jsii.member(jsii_name="saml2SnowflakeIssuerUrl")
    def saml2_snowflake_issuer_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "saml2SnowflakeIssuerUrl"))

    @saml2_snowflake_issuer_url.setter
    def saml2_snowflake_issuer_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef26706b2840ab761d9a82b57e3da5d92962aeccbb88cd085d70e1460083c71c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "saml2SnowflakeIssuerUrl", value)

    @builtins.property
    @jsii.member(jsii_name="saml2SnowflakeX509Cert")
    def saml2_snowflake_x509_cert(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "saml2SnowflakeX509Cert"))

    @saml2_snowflake_x509_cert.setter
    def saml2_snowflake_x509_cert(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd312913b8d955c3624d3a76d6994a94866bcefb3ba6fb11974a0b711baf4ce7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "saml2SnowflakeX509Cert", value)

    @builtins.property
    @jsii.member(jsii_name="saml2SpInitiatedLoginPageLabel")
    def saml2_sp_initiated_login_page_label(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "saml2SpInitiatedLoginPageLabel"))

    @saml2_sp_initiated_login_page_label.setter
    def saml2_sp_initiated_login_page_label(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c777713cc7050f7b05dea80185758ce878d57cb05d3629ad523bcbb574073cc0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "saml2SpInitiatedLoginPageLabel", value)

    @builtins.property
    @jsii.member(jsii_name="saml2SsoUrl")
    def saml2_sso_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "saml2SsoUrl"))

    @saml2_sso_url.setter
    def saml2_sso_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9c4a8350f5ee1720838800752b8c3774ba4ad60944f11b7a4e9c216552f0b72)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "saml2SsoUrl", value)

    @builtins.property
    @jsii.member(jsii_name="saml2X509Cert")
    def saml2_x509_cert(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "saml2X509Cert"))

    @saml2_x509_cert.setter
    def saml2_x509_cert(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a5efc171aaca8f537cf53ce7eeea39361d21478edb7335f27944d262ceaa116)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "saml2X509Cert", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-snowflake.samlIntegration.SamlIntegrationConfig",
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
        "saml2_issuer": "saml2Issuer",
        "saml2_provider": "saml2Provider",
        "saml2_sso_url": "saml2SsoUrl",
        "saml2_x509_cert": "saml2X509Cert",
        "enabled": "enabled",
        "id": "id",
        "saml2_enable_sp_initiated": "saml2EnableSpInitiated",
        "saml2_force_authn": "saml2ForceAuthn",
        "saml2_post_logout_redirect_url": "saml2PostLogoutRedirectUrl",
        "saml2_requested_nameid_format": "saml2RequestedNameidFormat",
        "saml2_sign_request": "saml2SignRequest",
        "saml2_snowflake_acs_url": "saml2SnowflakeAcsUrl",
        "saml2_snowflake_issuer_url": "saml2SnowflakeIssuerUrl",
        "saml2_snowflake_x509_cert": "saml2SnowflakeX509Cert",
        "saml2_sp_initiated_login_page_label": "saml2SpInitiatedLoginPageLabel",
    },
)
class SamlIntegrationConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        saml2_issuer: builtins.str,
        saml2_provider: builtins.str,
        saml2_sso_url: builtins.str,
        saml2_x509_cert: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        saml2_enable_sp_initiated: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        saml2_force_authn: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        saml2_post_logout_redirect_url: typing.Optional[builtins.str] = None,
        saml2_requested_nameid_format: typing.Optional[builtins.str] = None,
        saml2_sign_request: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        saml2_snowflake_acs_url: typing.Optional[builtins.str] = None,
        saml2_snowflake_issuer_url: typing.Optional[builtins.str] = None,
        saml2_snowflake_x509_cert: typing.Optional[builtins.str] = None,
        saml2_sp_initiated_login_page_label: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Specifies the name of the SAML2 integration. This name follows the rules for Object Identifiers. The name should be unique among security integrations in your account. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/saml_integration#name SamlIntegration#name}
        :param saml2_issuer: The string containing the IdP EntityID / Issuer. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/saml_integration#saml2_issuer SamlIntegration#saml2_issuer}
        :param saml2_provider: The string describing the IdP. One of the following: OKTA, ADFS, Custom. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/saml_integration#saml2_provider SamlIntegration#saml2_provider}
        :param saml2_sso_url: The string containing the IdP SSO URL, where the user should be redirected by Snowflake (the Service Provider) with a SAML AuthnRequest message. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/saml_integration#saml2_sso_url SamlIntegration#saml2_sso_url}
        :param saml2_x509_cert: The Base64 encoded IdP signing certificate on a single line without the leading -----BEGIN CERTIFICATE----- and ending -----END CERTIFICATE----- markers. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/saml_integration#saml2_x509_cert SamlIntegration#saml2_x509_cert}
        :param enabled: Specifies whether this security integration is enabled or disabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/saml_integration#enabled SamlIntegration#enabled}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/saml_integration#id SamlIntegration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param saml2_enable_sp_initiated: The Boolean indicating if the Log In With button will be shown on the login page. TRUE: displays the Log in WIth button on the login page. FALSE: does not display the Log in With button on the login page. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/saml_integration#saml2_enable_sp_initiated SamlIntegration#saml2_enable_sp_initiated}
        :param saml2_force_authn: The Boolean indicating whether users, during the initial authentication flow, are forced to authenticate again to access Snowflake. When set to TRUE, Snowflake sets the ForceAuthn SAML parameter to TRUE in the outgoing request from Snowflake to the identity provider. TRUE: forces users to authenticate again to access Snowflake, even if a valid session with the identity provider exists. FALSE: does not force users to authenticate again to access Snowflake. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/saml_integration#saml2_force_authn SamlIntegration#saml2_force_authn}
        :param saml2_post_logout_redirect_url: The endpoint to which Snowflake redirects users after clicking the Log Out button in the classic Snowflake web interface. Snowflake terminates the Snowflake session upon redirecting to the specified endpoint. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/saml_integration#saml2_post_logout_redirect_url SamlIntegration#saml2_post_logout_redirect_url}
        :param saml2_requested_nameid_format: The SAML NameID format allows Snowflake to set an expectation of the identifying attribute of the user (i.e. SAML Subject) in the SAML assertion from the IdP to ensure a valid authentication to Snowflake. If a value is not specified, Snowflake sends the urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress value in the authentication request to the IdP. NameID must be one of the following values: urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified, urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress, urn:oasis:names:tc:SAML:1.1:nameid-format:X509SubjectName, urn:oasis:names:tc:SAML:1.1:nameid-format:WindowsDomainQualifiedName, urn:oasis:names:tc:SAML:2.0:nameid-format:kerberos, urn:oasis:names:tc:SAML:2.0:nameid-format:persistent, urn:oasis:names:tc:SAML:2.0:nameid-format:transient . Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/saml_integration#saml2_requested_nameid_format SamlIntegration#saml2_requested_nameid_format}
        :param saml2_sign_request: The Boolean indicating whether SAML requests are signed. TRUE: allows SAML requests to be signed. FALSE: does not allow SAML requests to be signed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/saml_integration#saml2_sign_request SamlIntegration#saml2_sign_request}
        :param saml2_snowflake_acs_url: The string containing the Snowflake Assertion Consumer Service URL to which the IdP will send its SAML authentication response back to Snowflake. This property will be set in the SAML authentication request generated by Snowflake when initiating a SAML SSO operation with the IdP. If an incorrect value is specified, Snowflake returns an error message indicating the acceptable values to use. Default: https://<account_locator>..snowflakecomputing.com/fed/login Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/saml_integration#saml2_snowflake_acs_url SamlIntegration#saml2_snowflake_acs_url}
        :param saml2_snowflake_issuer_url: The string containing the EntityID / Issuer for the Snowflake service provider. If an incorrect value is specified, Snowflake returns an error message indicating the acceptable values to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/saml_integration#saml2_snowflake_issuer_url SamlIntegration#saml2_snowflake_issuer_url}
        :param saml2_snowflake_x509_cert: The Base64 encoded self-signed certificate generated by Snowflake for use with Encrypting SAML Assertions and Signed SAML Requests. You must have at least one of these features (encrypted SAML assertions or signed SAML responses) enabled in your Snowflake account to access the certificate value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/saml_integration#saml2_snowflake_x509_cert SamlIntegration#saml2_snowflake_x509_cert}
        :param saml2_sp_initiated_login_page_label: The string containing the label to display after the Log In With button on the login page. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/saml_integration#saml2_sp_initiated_login_page_label SamlIntegration#saml2_sp_initiated_login_page_label}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__600e649beb9f4dc049828bcdd023c7c88711d5c267cc36585219359965e63fcd)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument saml2_issuer", value=saml2_issuer, expected_type=type_hints["saml2_issuer"])
            check_type(argname="argument saml2_provider", value=saml2_provider, expected_type=type_hints["saml2_provider"])
            check_type(argname="argument saml2_sso_url", value=saml2_sso_url, expected_type=type_hints["saml2_sso_url"])
            check_type(argname="argument saml2_x509_cert", value=saml2_x509_cert, expected_type=type_hints["saml2_x509_cert"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument saml2_enable_sp_initiated", value=saml2_enable_sp_initiated, expected_type=type_hints["saml2_enable_sp_initiated"])
            check_type(argname="argument saml2_force_authn", value=saml2_force_authn, expected_type=type_hints["saml2_force_authn"])
            check_type(argname="argument saml2_post_logout_redirect_url", value=saml2_post_logout_redirect_url, expected_type=type_hints["saml2_post_logout_redirect_url"])
            check_type(argname="argument saml2_requested_nameid_format", value=saml2_requested_nameid_format, expected_type=type_hints["saml2_requested_nameid_format"])
            check_type(argname="argument saml2_sign_request", value=saml2_sign_request, expected_type=type_hints["saml2_sign_request"])
            check_type(argname="argument saml2_snowflake_acs_url", value=saml2_snowflake_acs_url, expected_type=type_hints["saml2_snowflake_acs_url"])
            check_type(argname="argument saml2_snowflake_issuer_url", value=saml2_snowflake_issuer_url, expected_type=type_hints["saml2_snowflake_issuer_url"])
            check_type(argname="argument saml2_snowflake_x509_cert", value=saml2_snowflake_x509_cert, expected_type=type_hints["saml2_snowflake_x509_cert"])
            check_type(argname="argument saml2_sp_initiated_login_page_label", value=saml2_sp_initiated_login_page_label, expected_type=type_hints["saml2_sp_initiated_login_page_label"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "saml2_issuer": saml2_issuer,
            "saml2_provider": saml2_provider,
            "saml2_sso_url": saml2_sso_url,
            "saml2_x509_cert": saml2_x509_cert,
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
        if enabled is not None:
            self._values["enabled"] = enabled
        if id is not None:
            self._values["id"] = id
        if saml2_enable_sp_initiated is not None:
            self._values["saml2_enable_sp_initiated"] = saml2_enable_sp_initiated
        if saml2_force_authn is not None:
            self._values["saml2_force_authn"] = saml2_force_authn
        if saml2_post_logout_redirect_url is not None:
            self._values["saml2_post_logout_redirect_url"] = saml2_post_logout_redirect_url
        if saml2_requested_nameid_format is not None:
            self._values["saml2_requested_nameid_format"] = saml2_requested_nameid_format
        if saml2_sign_request is not None:
            self._values["saml2_sign_request"] = saml2_sign_request
        if saml2_snowflake_acs_url is not None:
            self._values["saml2_snowflake_acs_url"] = saml2_snowflake_acs_url
        if saml2_snowflake_issuer_url is not None:
            self._values["saml2_snowflake_issuer_url"] = saml2_snowflake_issuer_url
        if saml2_snowflake_x509_cert is not None:
            self._values["saml2_snowflake_x509_cert"] = saml2_snowflake_x509_cert
        if saml2_sp_initiated_login_page_label is not None:
            self._values["saml2_sp_initiated_login_page_label"] = saml2_sp_initiated_login_page_label

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
        '''Specifies the name of the SAML2 integration.

        This name follows the rules for Object Identifiers. The name should be unique among security integrations in your account.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/saml_integration#name SamlIntegration#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def saml2_issuer(self) -> builtins.str:
        '''The string containing the IdP EntityID / Issuer.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/saml_integration#saml2_issuer SamlIntegration#saml2_issuer}
        '''
        result = self._values.get("saml2_issuer")
        assert result is not None, "Required property 'saml2_issuer' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def saml2_provider(self) -> builtins.str:
        '''The string describing the IdP. One of the following: OKTA, ADFS, Custom.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/saml_integration#saml2_provider SamlIntegration#saml2_provider}
        '''
        result = self._values.get("saml2_provider")
        assert result is not None, "Required property 'saml2_provider' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def saml2_sso_url(self) -> builtins.str:
        '''The string containing the IdP SSO URL, where the user should be redirected by Snowflake (the Service Provider) with a SAML AuthnRequest message.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/saml_integration#saml2_sso_url SamlIntegration#saml2_sso_url}
        '''
        result = self._values.get("saml2_sso_url")
        assert result is not None, "Required property 'saml2_sso_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def saml2_x509_cert(self) -> builtins.str:
        '''The Base64 encoded IdP signing certificate on a single line without the leading -----BEGIN CERTIFICATE----- and ending -----END CERTIFICATE----- markers.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/saml_integration#saml2_x509_cert SamlIntegration#saml2_x509_cert}
        '''
        result = self._values.get("saml2_x509_cert")
        assert result is not None, "Required property 'saml2_x509_cert' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Specifies whether this security integration is enabled or disabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/saml_integration#enabled SamlIntegration#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/saml_integration#id SamlIntegration#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def saml2_enable_sp_initiated(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''The Boolean indicating if the Log In With button will be shown on the login page.

        TRUE: displays the Log in WIth button on the login page.  FALSE: does not display the Log in With button on the login page.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/saml_integration#saml2_enable_sp_initiated SamlIntegration#saml2_enable_sp_initiated}
        '''
        result = self._values.get("saml2_enable_sp_initiated")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def saml2_force_authn(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''The Boolean indicating whether users, during the initial authentication flow, are forced to authenticate again to access Snowflake.

        When set to TRUE, Snowflake sets the ForceAuthn SAML parameter to TRUE in the outgoing request from Snowflake to the identity provider. TRUE: forces users to authenticate again to access Snowflake, even if a valid session with the identity provider exists. FALSE: does not force users to authenticate again to access Snowflake.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/saml_integration#saml2_force_authn SamlIntegration#saml2_force_authn}
        '''
        result = self._values.get("saml2_force_authn")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def saml2_post_logout_redirect_url(self) -> typing.Optional[builtins.str]:
        '''The endpoint to which Snowflake redirects users after clicking the Log Out button in the classic Snowflake web interface.

        Snowflake terminates the Snowflake session upon redirecting to the specified endpoint.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/saml_integration#saml2_post_logout_redirect_url SamlIntegration#saml2_post_logout_redirect_url}
        '''
        result = self._values.get("saml2_post_logout_redirect_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def saml2_requested_nameid_format(self) -> typing.Optional[builtins.str]:
        '''The SAML NameID format allows Snowflake to set an expectation of the identifying attribute of the user (i.e. SAML Subject) in the SAML assertion from the IdP to ensure a valid authentication to Snowflake. If a value is not specified, Snowflake sends the urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress value in the authentication request to the IdP. NameID must be one of the following values: urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified, urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress, urn:oasis:names:tc:SAML:1.1:nameid-format:X509SubjectName, urn:oasis:names:tc:SAML:1.1:nameid-format:WindowsDomainQualifiedName, urn:oasis:names:tc:SAML:2.0:nameid-format:kerberos, urn:oasis:names:tc:SAML:2.0:nameid-format:persistent, urn:oasis:names:tc:SAML:2.0:nameid-format:transient .

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/saml_integration#saml2_requested_nameid_format SamlIntegration#saml2_requested_nameid_format}
        '''
        result = self._values.get("saml2_requested_nameid_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def saml2_sign_request(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''The Boolean indicating whether SAML requests are signed.

        TRUE: allows SAML requests to be signed. FALSE: does not allow SAML requests to be signed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/saml_integration#saml2_sign_request SamlIntegration#saml2_sign_request}
        '''
        result = self._values.get("saml2_sign_request")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def saml2_snowflake_acs_url(self) -> typing.Optional[builtins.str]:
        '''The string containing the Snowflake Assertion Consumer Service URL to which the IdP will send its SAML authentication response back to Snowflake.

        This property will be set in the SAML authentication request generated by Snowflake when initiating a SAML SSO operation with the IdP. If an incorrect value is specified, Snowflake returns an error message indicating the acceptable values to use. Default: https://<account_locator>..snowflakecomputing.com/fed/login

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/saml_integration#saml2_snowflake_acs_url SamlIntegration#saml2_snowflake_acs_url}
        '''
        result = self._values.get("saml2_snowflake_acs_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def saml2_snowflake_issuer_url(self) -> typing.Optional[builtins.str]:
        '''The string containing the EntityID / Issuer for the Snowflake service provider.

        If an incorrect value is specified, Snowflake returns an error message indicating the acceptable values to use.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/saml_integration#saml2_snowflake_issuer_url SamlIntegration#saml2_snowflake_issuer_url}
        '''
        result = self._values.get("saml2_snowflake_issuer_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def saml2_snowflake_x509_cert(self) -> typing.Optional[builtins.str]:
        '''The Base64 encoded self-signed certificate generated by Snowflake for use with Encrypting SAML Assertions and Signed SAML Requests.

        You must have at least one of these features (encrypted SAML assertions or signed SAML responses) enabled in your Snowflake account to access the certificate value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/saml_integration#saml2_snowflake_x509_cert SamlIntegration#saml2_snowflake_x509_cert}
        '''
        result = self._values.get("saml2_snowflake_x509_cert")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def saml2_sp_initiated_login_page_label(self) -> typing.Optional[builtins.str]:
        '''The string containing the label to display after the Log In With button on the login page.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/saml_integration#saml2_sp_initiated_login_page_label SamlIntegration#saml2_sp_initiated_login_page_label}
        '''
        result = self._values.get("saml2_sp_initiated_login_page_label")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SamlIntegrationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "SamlIntegration",
    "SamlIntegrationConfig",
]

publication.publish()

def _typecheckingstub__6ef5e3f888980d88f02fb4ff5bfb8d32760c447671c365faddd78a3c1971a9d5(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    saml2_issuer: builtins.str,
    saml2_provider: builtins.str,
    saml2_sso_url: builtins.str,
    saml2_x509_cert: builtins.str,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    saml2_enable_sp_initiated: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    saml2_force_authn: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    saml2_post_logout_redirect_url: typing.Optional[builtins.str] = None,
    saml2_requested_nameid_format: typing.Optional[builtins.str] = None,
    saml2_sign_request: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    saml2_snowflake_acs_url: typing.Optional[builtins.str] = None,
    saml2_snowflake_issuer_url: typing.Optional[builtins.str] = None,
    saml2_snowflake_x509_cert: typing.Optional[builtins.str] = None,
    saml2_sp_initiated_login_page_label: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__0abf2b8885a5e0ac0dfe6ddb58b2485c18b54a82496183a09549d1f0afe76746(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__847e672722c5a90eea58c73fb092b5232df15dead2f7cbf40b58975f6df1a5c5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57052e84d447cdecfc67b3b197b7ae287ede531ff3e4188e4d96c646c1d55841(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df3fa14cc7b2e23c9fe5bf0afa4c9839e86e76de249f1080b6051f087fdb1235(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3605d0361def17141e911f30cfcf2d9856d494aebcfa874e2ce71a585381d371(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3598d3b2f548d9ec47dcd7fb63130e59382377965c928375f7c0f20e9a06d1a2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49254a90202aea56f3c62d686e35c10bf9a367f6e6cf0c7452c3c7bcb6b60f88(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4c89dc4d6ad82d1a0afa6c6aa9e19dfa7d688d1d19bdc597ebec765cfc38cd8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d7b883044c0df6cff0be7f498c81f3ae8d38ee486c815f06f43ce2fb0b9b926(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8095b8c5a94f6ea403b7d0cd8ec5c2104b47faffa4f040e242e2094782cdd61d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__298ea233832bb5de59365acab62fd8b2a32d42f3d60de7e4136ffba0ab63e678(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef26706b2840ab761d9a82b57e3da5d92962aeccbb88cd085d70e1460083c71c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd312913b8d955c3624d3a76d6994a94866bcefb3ba6fb11974a0b711baf4ce7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c777713cc7050f7b05dea80185758ce878d57cb05d3629ad523bcbb574073cc0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9c4a8350f5ee1720838800752b8c3774ba4ad60944f11b7a4e9c216552f0b72(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a5efc171aaca8f537cf53ce7eeea39361d21478edb7335f27944d262ceaa116(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__600e649beb9f4dc049828bcdd023c7c88711d5c267cc36585219359965e63fcd(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    saml2_issuer: builtins.str,
    saml2_provider: builtins.str,
    saml2_sso_url: builtins.str,
    saml2_x509_cert: builtins.str,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    saml2_enable_sp_initiated: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    saml2_force_authn: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    saml2_post_logout_redirect_url: typing.Optional[builtins.str] = None,
    saml2_requested_nameid_format: typing.Optional[builtins.str] = None,
    saml2_sign_request: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    saml2_snowflake_acs_url: typing.Optional[builtins.str] = None,
    saml2_snowflake_issuer_url: typing.Optional[builtins.str] = None,
    saml2_snowflake_x509_cert: typing.Optional[builtins.str] = None,
    saml2_sp_initiated_login_page_label: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
