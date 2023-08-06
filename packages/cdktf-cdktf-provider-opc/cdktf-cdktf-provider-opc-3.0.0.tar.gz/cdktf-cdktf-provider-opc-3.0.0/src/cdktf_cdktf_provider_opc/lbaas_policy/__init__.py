'''
# `opc_lbaas_policy`

Refer to the Terraform Registory for docs: [`opc_lbaas_policy`](https://www.terraform.io/docs/providers/opc/r/lbaas_policy).
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


class LbaasPolicy(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-opc.lbaasPolicy.LbaasPolicy",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy opc_lbaas_policy}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        load_balancer: builtins.str,
        name: builtins.str,
        application_cookie_stickiness_policy: typing.Optional[typing.Union["LbaasPolicyApplicationCookieStickinessPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        cloudgate_policy: typing.Optional[typing.Union["LbaasPolicyCloudgatePolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        load_balancer_cookie_stickiness_policy: typing.Optional[typing.Union["LbaasPolicyLoadBalancerCookieStickinessPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        load_balancing_mechanism_policy: typing.Optional[typing.Union["LbaasPolicyLoadBalancingMechanismPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        rate_limiting_request_policy: typing.Optional[typing.Union["LbaasPolicyRateLimitingRequestPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        redirect_policy: typing.Optional[typing.Union["LbaasPolicyRedirectPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        resource_access_control_policy: typing.Optional[typing.Union["LbaasPolicyResourceAccessControlPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        set_request_header_policy: typing.Optional[typing.Union["LbaasPolicySetRequestHeaderPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        ssl_negotiation_policy: typing.Optional[typing.Union["LbaasPolicySslNegotiationPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        trusted_certificate_policy: typing.Optional[typing.Union["LbaasPolicyTrustedCertificatePolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy opc_lbaas_policy} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param load_balancer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#load_balancer LbaasPolicy#load_balancer}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#name LbaasPolicy#name}.
        :param application_cookie_stickiness_policy: application_cookie_stickiness_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#application_cookie_stickiness_policy LbaasPolicy#application_cookie_stickiness_policy}
        :param cloudgate_policy: cloudgate_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#cloudgate_policy LbaasPolicy#cloudgate_policy}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#id LbaasPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param load_balancer_cookie_stickiness_policy: load_balancer_cookie_stickiness_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#load_balancer_cookie_stickiness_policy LbaasPolicy#load_balancer_cookie_stickiness_policy}
        :param load_balancing_mechanism_policy: load_balancing_mechanism_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#load_balancing_mechanism_policy LbaasPolicy#load_balancing_mechanism_policy}
        :param rate_limiting_request_policy: rate_limiting_request_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#rate_limiting_request_policy LbaasPolicy#rate_limiting_request_policy}
        :param redirect_policy: redirect_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#redirect_policy LbaasPolicy#redirect_policy}
        :param resource_access_control_policy: resource_access_control_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#resource_access_control_policy LbaasPolicy#resource_access_control_policy}
        :param set_request_header_policy: set_request_header_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#set_request_header_policy LbaasPolicy#set_request_header_policy}
        :param ssl_negotiation_policy: ssl_negotiation_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#ssl_negotiation_policy LbaasPolicy#ssl_negotiation_policy}
        :param trusted_certificate_policy: trusted_certificate_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#trusted_certificate_policy LbaasPolicy#trusted_certificate_policy}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3279d9c3fecbd56b29535b57f2fe62bcc8f6d88c837af2b2fc7c80cb01a3c3d4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = LbaasPolicyConfig(
            load_balancer=load_balancer,
            name=name,
            application_cookie_stickiness_policy=application_cookie_stickiness_policy,
            cloudgate_policy=cloudgate_policy,
            id=id,
            load_balancer_cookie_stickiness_policy=load_balancer_cookie_stickiness_policy,
            load_balancing_mechanism_policy=load_balancing_mechanism_policy,
            rate_limiting_request_policy=rate_limiting_request_policy,
            redirect_policy=redirect_policy,
            resource_access_control_policy=resource_access_control_policy,
            set_request_header_policy=set_request_header_policy,
            ssl_negotiation_policy=ssl_negotiation_policy,
            trusted_certificate_policy=trusted_certificate_policy,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putApplicationCookieStickinessPolicy")
    def put_application_cookie_stickiness_policy(
        self,
        *,
        cookie_name: builtins.str,
    ) -> None:
        '''
        :param cookie_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#cookie_name LbaasPolicy#cookie_name}.
        '''
        value = LbaasPolicyApplicationCookieStickinessPolicy(cookie_name=cookie_name)

        return typing.cast(None, jsii.invoke(self, "putApplicationCookieStickinessPolicy", [value]))

    @jsii.member(jsii_name="putCloudgatePolicy")
    def put_cloudgate_policy(
        self,
        *,
        virtual_hostname_for_policy_attribution: builtins.str,
        cloudgate_application: typing.Optional[builtins.str] = None,
        cloudgate_policy_name: typing.Optional[builtins.str] = None,
        identity_service_instance_guid: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param virtual_hostname_for_policy_attribution: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#virtual_hostname_for_policy_attribution LbaasPolicy#virtual_hostname_for_policy_attribution}.
        :param cloudgate_application: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#cloudgate_application LbaasPolicy#cloudgate_application}.
        :param cloudgate_policy_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#cloudgate_policy_name LbaasPolicy#cloudgate_policy_name}.
        :param identity_service_instance_guid: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#identity_service_instance_guid LbaasPolicy#identity_service_instance_guid}.
        '''
        value = LbaasPolicyCloudgatePolicy(
            virtual_hostname_for_policy_attribution=virtual_hostname_for_policy_attribution,
            cloudgate_application=cloudgate_application,
            cloudgate_policy_name=cloudgate_policy_name,
            identity_service_instance_guid=identity_service_instance_guid,
        )

        return typing.cast(None, jsii.invoke(self, "putCloudgatePolicy", [value]))

    @jsii.member(jsii_name="putLoadBalancerCookieStickinessPolicy")
    def put_load_balancer_cookie_stickiness_policy(
        self,
        *,
        cookie_expiration_period: jsii.Number,
    ) -> None:
        '''
        :param cookie_expiration_period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#cookie_expiration_period LbaasPolicy#cookie_expiration_period}.
        '''
        value = LbaasPolicyLoadBalancerCookieStickinessPolicy(
            cookie_expiration_period=cookie_expiration_period
        )

        return typing.cast(None, jsii.invoke(self, "putLoadBalancerCookieStickinessPolicy", [value]))

    @jsii.member(jsii_name="putLoadBalancingMechanismPolicy")
    def put_load_balancing_mechanism_policy(
        self,
        *,
        load_balancing_mechanism: builtins.str,
    ) -> None:
        '''
        :param load_balancing_mechanism: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#load_balancing_mechanism LbaasPolicy#load_balancing_mechanism}.
        '''
        value = LbaasPolicyLoadBalancingMechanismPolicy(
            load_balancing_mechanism=load_balancing_mechanism
        )

        return typing.cast(None, jsii.invoke(self, "putLoadBalancingMechanismPolicy", [value]))

    @jsii.member(jsii_name="putRateLimitingRequestPolicy")
    def put_rate_limiting_request_policy(
        self,
        *,
        burst_size: jsii.Number,
        delay_excessive_requests: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        requests_per_second: jsii.Number,
        zone: builtins.str,
        http_error_code: typing.Optional[jsii.Number] = None,
        logging_level: typing.Optional[builtins.str] = None,
        rate_limiting_criteria: typing.Optional[builtins.str] = None,
        zone_memory_size: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param burst_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#burst_size LbaasPolicy#burst_size}.
        :param delay_excessive_requests: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#delay_excessive_requests LbaasPolicy#delay_excessive_requests}.
        :param requests_per_second: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#requests_per_second LbaasPolicy#requests_per_second}.
        :param zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#zone LbaasPolicy#zone}.
        :param http_error_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#http_error_code LbaasPolicy#http_error_code}.
        :param logging_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#logging_level LbaasPolicy#logging_level}.
        :param rate_limiting_criteria: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#rate_limiting_criteria LbaasPolicy#rate_limiting_criteria}.
        :param zone_memory_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#zone_memory_size LbaasPolicy#zone_memory_size}.
        '''
        value = LbaasPolicyRateLimitingRequestPolicy(
            burst_size=burst_size,
            delay_excessive_requests=delay_excessive_requests,
            requests_per_second=requests_per_second,
            zone=zone,
            http_error_code=http_error_code,
            logging_level=logging_level,
            rate_limiting_criteria=rate_limiting_criteria,
            zone_memory_size=zone_memory_size,
        )

        return typing.cast(None, jsii.invoke(self, "putRateLimitingRequestPolicy", [value]))

    @jsii.member(jsii_name="putRedirectPolicy")
    def put_redirect_policy(
        self,
        *,
        redirect_uri: builtins.str,
        response_code: jsii.Number,
    ) -> None:
        '''
        :param redirect_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#redirect_uri LbaasPolicy#redirect_uri}.
        :param response_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#response_code LbaasPolicy#response_code}.
        '''
        value = LbaasPolicyRedirectPolicy(
            redirect_uri=redirect_uri, response_code=response_code
        )

        return typing.cast(None, jsii.invoke(self, "putRedirectPolicy", [value]))

    @jsii.member(jsii_name="putResourceAccessControlPolicy")
    def put_resource_access_control_policy(
        self,
        *,
        disposition: builtins.str,
        denied_clients: typing.Optional[typing.Sequence[builtins.str]] = None,
        permitted_clients: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param disposition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#disposition LbaasPolicy#disposition}.
        :param denied_clients: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#denied_clients LbaasPolicy#denied_clients}.
        :param permitted_clients: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#permitted_clients LbaasPolicy#permitted_clients}.
        '''
        value = LbaasPolicyResourceAccessControlPolicy(
            disposition=disposition,
            denied_clients=denied_clients,
            permitted_clients=permitted_clients,
        )

        return typing.cast(None, jsii.invoke(self, "putResourceAccessControlPolicy", [value]))

    @jsii.member(jsii_name="putSetRequestHeaderPolicy")
    def put_set_request_header_policy(
        self,
        *,
        header_name: builtins.str,
        action_when_header_exists: typing.Optional[builtins.str] = None,
        action_when_header_value_is: typing.Optional[typing.Sequence[builtins.str]] = None,
        action_when_header_value_is_not: typing.Optional[typing.Sequence[builtins.str]] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param header_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#header_name LbaasPolicy#header_name}.
        :param action_when_header_exists: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#action_when_header_exists LbaasPolicy#action_when_header_exists}.
        :param action_when_header_value_is: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#action_when_header_value_is LbaasPolicy#action_when_header_value_is}.
        :param action_when_header_value_is_not: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#action_when_header_value_is_not LbaasPolicy#action_when_header_value_is_not}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#value LbaasPolicy#value}.
        '''
        value_ = LbaasPolicySetRequestHeaderPolicy(
            header_name=header_name,
            action_when_header_exists=action_when_header_exists,
            action_when_header_value_is=action_when_header_value_is,
            action_when_header_value_is_not=action_when_header_value_is_not,
            value=value,
        )

        return typing.cast(None, jsii.invoke(self, "putSetRequestHeaderPolicy", [value_]))

    @jsii.member(jsii_name="putSslNegotiationPolicy")
    def put_ssl_negotiation_policy(
        self,
        *,
        port: jsii.Number,
        ssl_protocol: typing.Sequence[builtins.str],
        server_order_preference: typing.Optional[builtins.str] = None,
        ssl_ciphers: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#port LbaasPolicy#port}.
        :param ssl_protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#ssl_protocol LbaasPolicy#ssl_protocol}.
        :param server_order_preference: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#server_order_preference LbaasPolicy#server_order_preference}.
        :param ssl_ciphers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#ssl_ciphers LbaasPolicy#ssl_ciphers}.
        '''
        value = LbaasPolicySslNegotiationPolicy(
            port=port,
            ssl_protocol=ssl_protocol,
            server_order_preference=server_order_preference,
            ssl_ciphers=ssl_ciphers,
        )

        return typing.cast(None, jsii.invoke(self, "putSslNegotiationPolicy", [value]))

    @jsii.member(jsii_name="putTrustedCertificatePolicy")
    def put_trusted_certificate_policy(
        self,
        *,
        trusted_certificate: builtins.str,
    ) -> None:
        '''
        :param trusted_certificate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#trusted_certificate LbaasPolicy#trusted_certificate}.
        '''
        value = LbaasPolicyTrustedCertificatePolicy(
            trusted_certificate=trusted_certificate
        )

        return typing.cast(None, jsii.invoke(self, "putTrustedCertificatePolicy", [value]))

    @jsii.member(jsii_name="resetApplicationCookieStickinessPolicy")
    def reset_application_cookie_stickiness_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApplicationCookieStickinessPolicy", []))

    @jsii.member(jsii_name="resetCloudgatePolicy")
    def reset_cloudgate_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudgatePolicy", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLoadBalancerCookieStickinessPolicy")
    def reset_load_balancer_cookie_stickiness_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoadBalancerCookieStickinessPolicy", []))

    @jsii.member(jsii_name="resetLoadBalancingMechanismPolicy")
    def reset_load_balancing_mechanism_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoadBalancingMechanismPolicy", []))

    @jsii.member(jsii_name="resetRateLimitingRequestPolicy")
    def reset_rate_limiting_request_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRateLimitingRequestPolicy", []))

    @jsii.member(jsii_name="resetRedirectPolicy")
    def reset_redirect_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedirectPolicy", []))

    @jsii.member(jsii_name="resetResourceAccessControlPolicy")
    def reset_resource_access_control_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceAccessControlPolicy", []))

    @jsii.member(jsii_name="resetSetRequestHeaderPolicy")
    def reset_set_request_header_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSetRequestHeaderPolicy", []))

    @jsii.member(jsii_name="resetSslNegotiationPolicy")
    def reset_ssl_negotiation_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSslNegotiationPolicy", []))

    @jsii.member(jsii_name="resetTrustedCertificatePolicy")
    def reset_trusted_certificate_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTrustedCertificatePolicy", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="applicationCookieStickinessPolicy")
    def application_cookie_stickiness_policy(
        self,
    ) -> "LbaasPolicyApplicationCookieStickinessPolicyOutputReference":
        return typing.cast("LbaasPolicyApplicationCookieStickinessPolicyOutputReference", jsii.get(self, "applicationCookieStickinessPolicy"))

    @builtins.property
    @jsii.member(jsii_name="cloudgatePolicy")
    def cloudgate_policy(self) -> "LbaasPolicyCloudgatePolicyOutputReference":
        return typing.cast("LbaasPolicyCloudgatePolicyOutputReference", jsii.get(self, "cloudgatePolicy"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancerCookieStickinessPolicy")
    def load_balancer_cookie_stickiness_policy(
        self,
    ) -> "LbaasPolicyLoadBalancerCookieStickinessPolicyOutputReference":
        return typing.cast("LbaasPolicyLoadBalancerCookieStickinessPolicyOutputReference", jsii.get(self, "loadBalancerCookieStickinessPolicy"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancingMechanismPolicy")
    def load_balancing_mechanism_policy(
        self,
    ) -> "LbaasPolicyLoadBalancingMechanismPolicyOutputReference":
        return typing.cast("LbaasPolicyLoadBalancingMechanismPolicyOutputReference", jsii.get(self, "loadBalancingMechanismPolicy"))

    @builtins.property
    @jsii.member(jsii_name="rateLimitingRequestPolicy")
    def rate_limiting_request_policy(
        self,
    ) -> "LbaasPolicyRateLimitingRequestPolicyOutputReference":
        return typing.cast("LbaasPolicyRateLimitingRequestPolicyOutputReference", jsii.get(self, "rateLimitingRequestPolicy"))

    @builtins.property
    @jsii.member(jsii_name="redirectPolicy")
    def redirect_policy(self) -> "LbaasPolicyRedirectPolicyOutputReference":
        return typing.cast("LbaasPolicyRedirectPolicyOutputReference", jsii.get(self, "redirectPolicy"))

    @builtins.property
    @jsii.member(jsii_name="resourceAccessControlPolicy")
    def resource_access_control_policy(
        self,
    ) -> "LbaasPolicyResourceAccessControlPolicyOutputReference":
        return typing.cast("LbaasPolicyResourceAccessControlPolicyOutputReference", jsii.get(self, "resourceAccessControlPolicy"))

    @builtins.property
    @jsii.member(jsii_name="setRequestHeaderPolicy")
    def set_request_header_policy(
        self,
    ) -> "LbaasPolicySetRequestHeaderPolicyOutputReference":
        return typing.cast("LbaasPolicySetRequestHeaderPolicyOutputReference", jsii.get(self, "setRequestHeaderPolicy"))

    @builtins.property
    @jsii.member(jsii_name="sslNegotiationPolicy")
    def ssl_negotiation_policy(
        self,
    ) -> "LbaasPolicySslNegotiationPolicyOutputReference":
        return typing.cast("LbaasPolicySslNegotiationPolicyOutputReference", jsii.get(self, "sslNegotiationPolicy"))

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "state"))

    @builtins.property
    @jsii.member(jsii_name="trustedCertificatePolicy")
    def trusted_certificate_policy(
        self,
    ) -> "LbaasPolicyTrustedCertificatePolicyOutputReference":
        return typing.cast("LbaasPolicyTrustedCertificatePolicyOutputReference", jsii.get(self, "trustedCertificatePolicy"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @builtins.property
    @jsii.member(jsii_name="uri")
    def uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uri"))

    @builtins.property
    @jsii.member(jsii_name="applicationCookieStickinessPolicyInput")
    def application_cookie_stickiness_policy_input(
        self,
    ) -> typing.Optional["LbaasPolicyApplicationCookieStickinessPolicy"]:
        return typing.cast(typing.Optional["LbaasPolicyApplicationCookieStickinessPolicy"], jsii.get(self, "applicationCookieStickinessPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudgatePolicyInput")
    def cloudgate_policy_input(self) -> typing.Optional["LbaasPolicyCloudgatePolicy"]:
        return typing.cast(typing.Optional["LbaasPolicyCloudgatePolicy"], jsii.get(self, "cloudgatePolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancerCookieStickinessPolicyInput")
    def load_balancer_cookie_stickiness_policy_input(
        self,
    ) -> typing.Optional["LbaasPolicyLoadBalancerCookieStickinessPolicy"]:
        return typing.cast(typing.Optional["LbaasPolicyLoadBalancerCookieStickinessPolicy"], jsii.get(self, "loadBalancerCookieStickinessPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancerInput")
    def load_balancer_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "loadBalancerInput"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancingMechanismPolicyInput")
    def load_balancing_mechanism_policy_input(
        self,
    ) -> typing.Optional["LbaasPolicyLoadBalancingMechanismPolicy"]:
        return typing.cast(typing.Optional["LbaasPolicyLoadBalancingMechanismPolicy"], jsii.get(self, "loadBalancingMechanismPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="rateLimitingRequestPolicyInput")
    def rate_limiting_request_policy_input(
        self,
    ) -> typing.Optional["LbaasPolicyRateLimitingRequestPolicy"]:
        return typing.cast(typing.Optional["LbaasPolicyRateLimitingRequestPolicy"], jsii.get(self, "rateLimitingRequestPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="redirectPolicyInput")
    def redirect_policy_input(self) -> typing.Optional["LbaasPolicyRedirectPolicy"]:
        return typing.cast(typing.Optional["LbaasPolicyRedirectPolicy"], jsii.get(self, "redirectPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceAccessControlPolicyInput")
    def resource_access_control_policy_input(
        self,
    ) -> typing.Optional["LbaasPolicyResourceAccessControlPolicy"]:
        return typing.cast(typing.Optional["LbaasPolicyResourceAccessControlPolicy"], jsii.get(self, "resourceAccessControlPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="setRequestHeaderPolicyInput")
    def set_request_header_policy_input(
        self,
    ) -> typing.Optional["LbaasPolicySetRequestHeaderPolicy"]:
        return typing.cast(typing.Optional["LbaasPolicySetRequestHeaderPolicy"], jsii.get(self, "setRequestHeaderPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="sslNegotiationPolicyInput")
    def ssl_negotiation_policy_input(
        self,
    ) -> typing.Optional["LbaasPolicySslNegotiationPolicy"]:
        return typing.cast(typing.Optional["LbaasPolicySslNegotiationPolicy"], jsii.get(self, "sslNegotiationPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="trustedCertificatePolicyInput")
    def trusted_certificate_policy_input(
        self,
    ) -> typing.Optional["LbaasPolicyTrustedCertificatePolicy"]:
        return typing.cast(typing.Optional["LbaasPolicyTrustedCertificatePolicy"], jsii.get(self, "trustedCertificatePolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f60c179d1855388fca5845ed43fe6c5b9240666db5f78b4eb271bf0f37c5cd7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="loadBalancer")
    def load_balancer(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "loadBalancer"))

    @load_balancer.setter
    def load_balancer(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0e76d75d4c62fbfc8092abaa53b0a94c4b7631f0d78a89ae29c99cccf9715fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loadBalancer", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74316676f002b47e4b0adf5e2e4a05ecc82605287ba30df74b309c0dfb7ea297)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-opc.lbaasPolicy.LbaasPolicyApplicationCookieStickinessPolicy",
    jsii_struct_bases=[],
    name_mapping={"cookie_name": "cookieName"},
)
class LbaasPolicyApplicationCookieStickinessPolicy:
    def __init__(self, *, cookie_name: builtins.str) -> None:
        '''
        :param cookie_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#cookie_name LbaasPolicy#cookie_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b05c133e36f99ab703ddabe70fdb4021aa65a103f639864e3a7016bd9e842267)
            check_type(argname="argument cookie_name", value=cookie_name, expected_type=type_hints["cookie_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cookie_name": cookie_name,
        }

    @builtins.property
    def cookie_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#cookie_name LbaasPolicy#cookie_name}.'''
        result = self._values.get("cookie_name")
        assert result is not None, "Required property 'cookie_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LbaasPolicyApplicationCookieStickinessPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LbaasPolicyApplicationCookieStickinessPolicyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-opc.lbaasPolicy.LbaasPolicyApplicationCookieStickinessPolicyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ade0d22fe32a0c7a397eca74113d523d22eb3d58b4593766e2233f09de608f61)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="cookieNameInput")
    def cookie_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cookieNameInput"))

    @builtins.property
    @jsii.member(jsii_name="cookieName")
    def cookie_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cookieName"))

    @cookie_name.setter
    def cookie_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1147827db676648811436064c5acb410992b46884ed5377fe4a0463bb7386fdb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cookieName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LbaasPolicyApplicationCookieStickinessPolicy]:
        return typing.cast(typing.Optional[LbaasPolicyApplicationCookieStickinessPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LbaasPolicyApplicationCookieStickinessPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bfdd7e144befe2e0238a210bfeb7051468fdc2199efc24f42394add331b44344)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-opc.lbaasPolicy.LbaasPolicyCloudgatePolicy",
    jsii_struct_bases=[],
    name_mapping={
        "virtual_hostname_for_policy_attribution": "virtualHostnameForPolicyAttribution",
        "cloudgate_application": "cloudgateApplication",
        "cloudgate_policy_name": "cloudgatePolicyName",
        "identity_service_instance_guid": "identityServiceInstanceGuid",
    },
)
class LbaasPolicyCloudgatePolicy:
    def __init__(
        self,
        *,
        virtual_hostname_for_policy_attribution: builtins.str,
        cloudgate_application: typing.Optional[builtins.str] = None,
        cloudgate_policy_name: typing.Optional[builtins.str] = None,
        identity_service_instance_guid: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param virtual_hostname_for_policy_attribution: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#virtual_hostname_for_policy_attribution LbaasPolicy#virtual_hostname_for_policy_attribution}.
        :param cloudgate_application: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#cloudgate_application LbaasPolicy#cloudgate_application}.
        :param cloudgate_policy_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#cloudgate_policy_name LbaasPolicy#cloudgate_policy_name}.
        :param identity_service_instance_guid: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#identity_service_instance_guid LbaasPolicy#identity_service_instance_guid}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af7a622f455d4701699a6d66b28a6a3e1270cebc2a5c4b0a369c517ba48efcf6)
            check_type(argname="argument virtual_hostname_for_policy_attribution", value=virtual_hostname_for_policy_attribution, expected_type=type_hints["virtual_hostname_for_policy_attribution"])
            check_type(argname="argument cloudgate_application", value=cloudgate_application, expected_type=type_hints["cloudgate_application"])
            check_type(argname="argument cloudgate_policy_name", value=cloudgate_policy_name, expected_type=type_hints["cloudgate_policy_name"])
            check_type(argname="argument identity_service_instance_guid", value=identity_service_instance_guid, expected_type=type_hints["identity_service_instance_guid"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "virtual_hostname_for_policy_attribution": virtual_hostname_for_policy_attribution,
        }
        if cloudgate_application is not None:
            self._values["cloudgate_application"] = cloudgate_application
        if cloudgate_policy_name is not None:
            self._values["cloudgate_policy_name"] = cloudgate_policy_name
        if identity_service_instance_guid is not None:
            self._values["identity_service_instance_guid"] = identity_service_instance_guid

    @builtins.property
    def virtual_hostname_for_policy_attribution(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#virtual_hostname_for_policy_attribution LbaasPolicy#virtual_hostname_for_policy_attribution}.'''
        result = self._values.get("virtual_hostname_for_policy_attribution")
        assert result is not None, "Required property 'virtual_hostname_for_policy_attribution' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cloudgate_application(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#cloudgate_application LbaasPolicy#cloudgate_application}.'''
        result = self._values.get("cloudgate_application")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cloudgate_policy_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#cloudgate_policy_name LbaasPolicy#cloudgate_policy_name}.'''
        result = self._values.get("cloudgate_policy_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identity_service_instance_guid(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#identity_service_instance_guid LbaasPolicy#identity_service_instance_guid}.'''
        result = self._values.get("identity_service_instance_guid")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LbaasPolicyCloudgatePolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LbaasPolicyCloudgatePolicyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-opc.lbaasPolicy.LbaasPolicyCloudgatePolicyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__45fde25f007faaecbef4aa3c23123ae46e90de101a655dc0502432a1530b1eb2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCloudgateApplication")
    def reset_cloudgate_application(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudgateApplication", []))

    @jsii.member(jsii_name="resetCloudgatePolicyName")
    def reset_cloudgate_policy_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudgatePolicyName", []))

    @jsii.member(jsii_name="resetIdentityServiceInstanceGuid")
    def reset_identity_service_instance_guid(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentityServiceInstanceGuid", []))

    @builtins.property
    @jsii.member(jsii_name="cloudgateApplicationInput")
    def cloudgate_application_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cloudgateApplicationInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudgatePolicyNameInput")
    def cloudgate_policy_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cloudgatePolicyNameInput"))

    @builtins.property
    @jsii.member(jsii_name="identityServiceInstanceGuidInput")
    def identity_service_instance_guid_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identityServiceInstanceGuidInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualHostnameForPolicyAttributionInput")
    def virtual_hostname_for_policy_attribution_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "virtualHostnameForPolicyAttributionInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudgateApplication")
    def cloudgate_application(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudgateApplication"))

    @cloudgate_application.setter
    def cloudgate_application(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7869522c91257550c207b5e63cd483e88475822ac5b16eec05a494c0a3f8b159)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudgateApplication", value)

    @builtins.property
    @jsii.member(jsii_name="cloudgatePolicyName")
    def cloudgate_policy_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudgatePolicyName"))

    @cloudgate_policy_name.setter
    def cloudgate_policy_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9fa3db2c49c9c72ad82b8f4fdf0486f4d13dadbb0d16c428b625b58586f79743)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudgatePolicyName", value)

    @builtins.property
    @jsii.member(jsii_name="identityServiceInstanceGuid")
    def identity_service_instance_guid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identityServiceInstanceGuid"))

    @identity_service_instance_guid.setter
    def identity_service_instance_guid(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b1adaa3ebcf0ca174f1ddc59d57cbe53c0d5a42f0d72a89055209ccdffd2018)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityServiceInstanceGuid", value)

    @builtins.property
    @jsii.member(jsii_name="virtualHostnameForPolicyAttribution")
    def virtual_hostname_for_policy_attribution(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualHostnameForPolicyAttribution"))

    @virtual_hostname_for_policy_attribution.setter
    def virtual_hostname_for_policy_attribution(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6c1dce9ddf35eddc32fc6251068697677ce61986b1f095aab5f8af77b247359)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualHostnameForPolicyAttribution", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LbaasPolicyCloudgatePolicy]:
        return typing.cast(typing.Optional[LbaasPolicyCloudgatePolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LbaasPolicyCloudgatePolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e728720be377f3cc5d7cfaed2f4ea853d1c909ff00b52deb58491051a89a228)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-opc.lbaasPolicy.LbaasPolicyConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "load_balancer": "loadBalancer",
        "name": "name",
        "application_cookie_stickiness_policy": "applicationCookieStickinessPolicy",
        "cloudgate_policy": "cloudgatePolicy",
        "id": "id",
        "load_balancer_cookie_stickiness_policy": "loadBalancerCookieStickinessPolicy",
        "load_balancing_mechanism_policy": "loadBalancingMechanismPolicy",
        "rate_limiting_request_policy": "rateLimitingRequestPolicy",
        "redirect_policy": "redirectPolicy",
        "resource_access_control_policy": "resourceAccessControlPolicy",
        "set_request_header_policy": "setRequestHeaderPolicy",
        "ssl_negotiation_policy": "sslNegotiationPolicy",
        "trusted_certificate_policy": "trustedCertificatePolicy",
    },
)
class LbaasPolicyConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        load_balancer: builtins.str,
        name: builtins.str,
        application_cookie_stickiness_policy: typing.Optional[typing.Union[LbaasPolicyApplicationCookieStickinessPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
        cloudgate_policy: typing.Optional[typing.Union[LbaasPolicyCloudgatePolicy, typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        load_balancer_cookie_stickiness_policy: typing.Optional[typing.Union["LbaasPolicyLoadBalancerCookieStickinessPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        load_balancing_mechanism_policy: typing.Optional[typing.Union["LbaasPolicyLoadBalancingMechanismPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        rate_limiting_request_policy: typing.Optional[typing.Union["LbaasPolicyRateLimitingRequestPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        redirect_policy: typing.Optional[typing.Union["LbaasPolicyRedirectPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        resource_access_control_policy: typing.Optional[typing.Union["LbaasPolicyResourceAccessControlPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        set_request_header_policy: typing.Optional[typing.Union["LbaasPolicySetRequestHeaderPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        ssl_negotiation_policy: typing.Optional[typing.Union["LbaasPolicySslNegotiationPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        trusted_certificate_policy: typing.Optional[typing.Union["LbaasPolicyTrustedCertificatePolicy", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param load_balancer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#load_balancer LbaasPolicy#load_balancer}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#name LbaasPolicy#name}.
        :param application_cookie_stickiness_policy: application_cookie_stickiness_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#application_cookie_stickiness_policy LbaasPolicy#application_cookie_stickiness_policy}
        :param cloudgate_policy: cloudgate_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#cloudgate_policy LbaasPolicy#cloudgate_policy}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#id LbaasPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param load_balancer_cookie_stickiness_policy: load_balancer_cookie_stickiness_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#load_balancer_cookie_stickiness_policy LbaasPolicy#load_balancer_cookie_stickiness_policy}
        :param load_balancing_mechanism_policy: load_balancing_mechanism_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#load_balancing_mechanism_policy LbaasPolicy#load_balancing_mechanism_policy}
        :param rate_limiting_request_policy: rate_limiting_request_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#rate_limiting_request_policy LbaasPolicy#rate_limiting_request_policy}
        :param redirect_policy: redirect_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#redirect_policy LbaasPolicy#redirect_policy}
        :param resource_access_control_policy: resource_access_control_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#resource_access_control_policy LbaasPolicy#resource_access_control_policy}
        :param set_request_header_policy: set_request_header_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#set_request_header_policy LbaasPolicy#set_request_header_policy}
        :param ssl_negotiation_policy: ssl_negotiation_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#ssl_negotiation_policy LbaasPolicy#ssl_negotiation_policy}
        :param trusted_certificate_policy: trusted_certificate_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#trusted_certificate_policy LbaasPolicy#trusted_certificate_policy}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(application_cookie_stickiness_policy, dict):
            application_cookie_stickiness_policy = LbaasPolicyApplicationCookieStickinessPolicy(**application_cookie_stickiness_policy)
        if isinstance(cloudgate_policy, dict):
            cloudgate_policy = LbaasPolicyCloudgatePolicy(**cloudgate_policy)
        if isinstance(load_balancer_cookie_stickiness_policy, dict):
            load_balancer_cookie_stickiness_policy = LbaasPolicyLoadBalancerCookieStickinessPolicy(**load_balancer_cookie_stickiness_policy)
        if isinstance(load_balancing_mechanism_policy, dict):
            load_balancing_mechanism_policy = LbaasPolicyLoadBalancingMechanismPolicy(**load_balancing_mechanism_policy)
        if isinstance(rate_limiting_request_policy, dict):
            rate_limiting_request_policy = LbaasPolicyRateLimitingRequestPolicy(**rate_limiting_request_policy)
        if isinstance(redirect_policy, dict):
            redirect_policy = LbaasPolicyRedirectPolicy(**redirect_policy)
        if isinstance(resource_access_control_policy, dict):
            resource_access_control_policy = LbaasPolicyResourceAccessControlPolicy(**resource_access_control_policy)
        if isinstance(set_request_header_policy, dict):
            set_request_header_policy = LbaasPolicySetRequestHeaderPolicy(**set_request_header_policy)
        if isinstance(ssl_negotiation_policy, dict):
            ssl_negotiation_policy = LbaasPolicySslNegotiationPolicy(**ssl_negotiation_policy)
        if isinstance(trusted_certificate_policy, dict):
            trusted_certificate_policy = LbaasPolicyTrustedCertificatePolicy(**trusted_certificate_policy)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13d9c7b0886043f8985bab37aaf68a25ec9d7b514b62fbdfee5ff7479b42c49b)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument load_balancer", value=load_balancer, expected_type=type_hints["load_balancer"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument application_cookie_stickiness_policy", value=application_cookie_stickiness_policy, expected_type=type_hints["application_cookie_stickiness_policy"])
            check_type(argname="argument cloudgate_policy", value=cloudgate_policy, expected_type=type_hints["cloudgate_policy"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument load_balancer_cookie_stickiness_policy", value=load_balancer_cookie_stickiness_policy, expected_type=type_hints["load_balancer_cookie_stickiness_policy"])
            check_type(argname="argument load_balancing_mechanism_policy", value=load_balancing_mechanism_policy, expected_type=type_hints["load_balancing_mechanism_policy"])
            check_type(argname="argument rate_limiting_request_policy", value=rate_limiting_request_policy, expected_type=type_hints["rate_limiting_request_policy"])
            check_type(argname="argument redirect_policy", value=redirect_policy, expected_type=type_hints["redirect_policy"])
            check_type(argname="argument resource_access_control_policy", value=resource_access_control_policy, expected_type=type_hints["resource_access_control_policy"])
            check_type(argname="argument set_request_header_policy", value=set_request_header_policy, expected_type=type_hints["set_request_header_policy"])
            check_type(argname="argument ssl_negotiation_policy", value=ssl_negotiation_policy, expected_type=type_hints["ssl_negotiation_policy"])
            check_type(argname="argument trusted_certificate_policy", value=trusted_certificate_policy, expected_type=type_hints["trusted_certificate_policy"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "load_balancer": load_balancer,
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
        if application_cookie_stickiness_policy is not None:
            self._values["application_cookie_stickiness_policy"] = application_cookie_stickiness_policy
        if cloudgate_policy is not None:
            self._values["cloudgate_policy"] = cloudgate_policy
        if id is not None:
            self._values["id"] = id
        if load_balancer_cookie_stickiness_policy is not None:
            self._values["load_balancer_cookie_stickiness_policy"] = load_balancer_cookie_stickiness_policy
        if load_balancing_mechanism_policy is not None:
            self._values["load_balancing_mechanism_policy"] = load_balancing_mechanism_policy
        if rate_limiting_request_policy is not None:
            self._values["rate_limiting_request_policy"] = rate_limiting_request_policy
        if redirect_policy is not None:
            self._values["redirect_policy"] = redirect_policy
        if resource_access_control_policy is not None:
            self._values["resource_access_control_policy"] = resource_access_control_policy
        if set_request_header_policy is not None:
            self._values["set_request_header_policy"] = set_request_header_policy
        if ssl_negotiation_policy is not None:
            self._values["ssl_negotiation_policy"] = ssl_negotiation_policy
        if trusted_certificate_policy is not None:
            self._values["trusted_certificate_policy"] = trusted_certificate_policy

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
    def load_balancer(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#load_balancer LbaasPolicy#load_balancer}.'''
        result = self._values.get("load_balancer")
        assert result is not None, "Required property 'load_balancer' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#name LbaasPolicy#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def application_cookie_stickiness_policy(
        self,
    ) -> typing.Optional[LbaasPolicyApplicationCookieStickinessPolicy]:
        '''application_cookie_stickiness_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#application_cookie_stickiness_policy LbaasPolicy#application_cookie_stickiness_policy}
        '''
        result = self._values.get("application_cookie_stickiness_policy")
        return typing.cast(typing.Optional[LbaasPolicyApplicationCookieStickinessPolicy], result)

    @builtins.property
    def cloudgate_policy(self) -> typing.Optional[LbaasPolicyCloudgatePolicy]:
        '''cloudgate_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#cloudgate_policy LbaasPolicy#cloudgate_policy}
        '''
        result = self._values.get("cloudgate_policy")
        return typing.cast(typing.Optional[LbaasPolicyCloudgatePolicy], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#id LbaasPolicy#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def load_balancer_cookie_stickiness_policy(
        self,
    ) -> typing.Optional["LbaasPolicyLoadBalancerCookieStickinessPolicy"]:
        '''load_balancer_cookie_stickiness_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#load_balancer_cookie_stickiness_policy LbaasPolicy#load_balancer_cookie_stickiness_policy}
        '''
        result = self._values.get("load_balancer_cookie_stickiness_policy")
        return typing.cast(typing.Optional["LbaasPolicyLoadBalancerCookieStickinessPolicy"], result)

    @builtins.property
    def load_balancing_mechanism_policy(
        self,
    ) -> typing.Optional["LbaasPolicyLoadBalancingMechanismPolicy"]:
        '''load_balancing_mechanism_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#load_balancing_mechanism_policy LbaasPolicy#load_balancing_mechanism_policy}
        '''
        result = self._values.get("load_balancing_mechanism_policy")
        return typing.cast(typing.Optional["LbaasPolicyLoadBalancingMechanismPolicy"], result)

    @builtins.property
    def rate_limiting_request_policy(
        self,
    ) -> typing.Optional["LbaasPolicyRateLimitingRequestPolicy"]:
        '''rate_limiting_request_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#rate_limiting_request_policy LbaasPolicy#rate_limiting_request_policy}
        '''
        result = self._values.get("rate_limiting_request_policy")
        return typing.cast(typing.Optional["LbaasPolicyRateLimitingRequestPolicy"], result)

    @builtins.property
    def redirect_policy(self) -> typing.Optional["LbaasPolicyRedirectPolicy"]:
        '''redirect_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#redirect_policy LbaasPolicy#redirect_policy}
        '''
        result = self._values.get("redirect_policy")
        return typing.cast(typing.Optional["LbaasPolicyRedirectPolicy"], result)

    @builtins.property
    def resource_access_control_policy(
        self,
    ) -> typing.Optional["LbaasPolicyResourceAccessControlPolicy"]:
        '''resource_access_control_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#resource_access_control_policy LbaasPolicy#resource_access_control_policy}
        '''
        result = self._values.get("resource_access_control_policy")
        return typing.cast(typing.Optional["LbaasPolicyResourceAccessControlPolicy"], result)

    @builtins.property
    def set_request_header_policy(
        self,
    ) -> typing.Optional["LbaasPolicySetRequestHeaderPolicy"]:
        '''set_request_header_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#set_request_header_policy LbaasPolicy#set_request_header_policy}
        '''
        result = self._values.get("set_request_header_policy")
        return typing.cast(typing.Optional["LbaasPolicySetRequestHeaderPolicy"], result)

    @builtins.property
    def ssl_negotiation_policy(
        self,
    ) -> typing.Optional["LbaasPolicySslNegotiationPolicy"]:
        '''ssl_negotiation_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#ssl_negotiation_policy LbaasPolicy#ssl_negotiation_policy}
        '''
        result = self._values.get("ssl_negotiation_policy")
        return typing.cast(typing.Optional["LbaasPolicySslNegotiationPolicy"], result)

    @builtins.property
    def trusted_certificate_policy(
        self,
    ) -> typing.Optional["LbaasPolicyTrustedCertificatePolicy"]:
        '''trusted_certificate_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#trusted_certificate_policy LbaasPolicy#trusted_certificate_policy}
        '''
        result = self._values.get("trusted_certificate_policy")
        return typing.cast(typing.Optional["LbaasPolicyTrustedCertificatePolicy"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LbaasPolicyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-opc.lbaasPolicy.LbaasPolicyLoadBalancerCookieStickinessPolicy",
    jsii_struct_bases=[],
    name_mapping={"cookie_expiration_period": "cookieExpirationPeriod"},
)
class LbaasPolicyLoadBalancerCookieStickinessPolicy:
    def __init__(self, *, cookie_expiration_period: jsii.Number) -> None:
        '''
        :param cookie_expiration_period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#cookie_expiration_period LbaasPolicy#cookie_expiration_period}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54a2cf37ad6db4eec7cb1f22836903bdc729846dc80e7a7ad3687f537e56434b)
            check_type(argname="argument cookie_expiration_period", value=cookie_expiration_period, expected_type=type_hints["cookie_expiration_period"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cookie_expiration_period": cookie_expiration_period,
        }

    @builtins.property
    def cookie_expiration_period(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#cookie_expiration_period LbaasPolicy#cookie_expiration_period}.'''
        result = self._values.get("cookie_expiration_period")
        assert result is not None, "Required property 'cookie_expiration_period' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LbaasPolicyLoadBalancerCookieStickinessPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LbaasPolicyLoadBalancerCookieStickinessPolicyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-opc.lbaasPolicy.LbaasPolicyLoadBalancerCookieStickinessPolicyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__763e52ac2c161eaeb29d3904fcc0890c422652ba21829d8ead6fd9476d43adba)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="cookieExpirationPeriodInput")
    def cookie_expiration_period_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "cookieExpirationPeriodInput"))

    @builtins.property
    @jsii.member(jsii_name="cookieExpirationPeriod")
    def cookie_expiration_period(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cookieExpirationPeriod"))

    @cookie_expiration_period.setter
    def cookie_expiration_period(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4dd52500cbeec3870762f92a21ac36eb5e57d3f9bbfe6ca81cb036ea27922612)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cookieExpirationPeriod", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LbaasPolicyLoadBalancerCookieStickinessPolicy]:
        return typing.cast(typing.Optional[LbaasPolicyLoadBalancerCookieStickinessPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LbaasPolicyLoadBalancerCookieStickinessPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5df5e84411aa89463126cd401b72f11d9910b68e8bbc151225ef005f5f4aa764)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-opc.lbaasPolicy.LbaasPolicyLoadBalancingMechanismPolicy",
    jsii_struct_bases=[],
    name_mapping={"load_balancing_mechanism": "loadBalancingMechanism"},
)
class LbaasPolicyLoadBalancingMechanismPolicy:
    def __init__(self, *, load_balancing_mechanism: builtins.str) -> None:
        '''
        :param load_balancing_mechanism: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#load_balancing_mechanism LbaasPolicy#load_balancing_mechanism}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5f8184114950c5bb3357deb10ddd1d1a64498f2ba4f9bfb90887aa6741cd7d3)
            check_type(argname="argument load_balancing_mechanism", value=load_balancing_mechanism, expected_type=type_hints["load_balancing_mechanism"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "load_balancing_mechanism": load_balancing_mechanism,
        }

    @builtins.property
    def load_balancing_mechanism(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#load_balancing_mechanism LbaasPolicy#load_balancing_mechanism}.'''
        result = self._values.get("load_balancing_mechanism")
        assert result is not None, "Required property 'load_balancing_mechanism' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LbaasPolicyLoadBalancingMechanismPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LbaasPolicyLoadBalancingMechanismPolicyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-opc.lbaasPolicy.LbaasPolicyLoadBalancingMechanismPolicyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__57fde6c3fef83db3d7963201d12c628483be67d74530c002ff1f828aacf2d18a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="loadBalancingMechanismInput")
    def load_balancing_mechanism_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "loadBalancingMechanismInput"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancingMechanism")
    def load_balancing_mechanism(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "loadBalancingMechanism"))

    @load_balancing_mechanism.setter
    def load_balancing_mechanism(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__faf83ab5804be9f71795477f6becf6e8a33825fa2b71e84988a397980cbe1f92)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loadBalancingMechanism", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LbaasPolicyLoadBalancingMechanismPolicy]:
        return typing.cast(typing.Optional[LbaasPolicyLoadBalancingMechanismPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LbaasPolicyLoadBalancingMechanismPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8976e6612042798d3f4ff45cc38845d8bfee446d62ae684b41c0e3d5d06bd2ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-opc.lbaasPolicy.LbaasPolicyRateLimitingRequestPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "burst_size": "burstSize",
        "delay_excessive_requests": "delayExcessiveRequests",
        "requests_per_second": "requestsPerSecond",
        "zone": "zone",
        "http_error_code": "httpErrorCode",
        "logging_level": "loggingLevel",
        "rate_limiting_criteria": "rateLimitingCriteria",
        "zone_memory_size": "zoneMemorySize",
    },
)
class LbaasPolicyRateLimitingRequestPolicy:
    def __init__(
        self,
        *,
        burst_size: jsii.Number,
        delay_excessive_requests: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        requests_per_second: jsii.Number,
        zone: builtins.str,
        http_error_code: typing.Optional[jsii.Number] = None,
        logging_level: typing.Optional[builtins.str] = None,
        rate_limiting_criteria: typing.Optional[builtins.str] = None,
        zone_memory_size: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param burst_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#burst_size LbaasPolicy#burst_size}.
        :param delay_excessive_requests: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#delay_excessive_requests LbaasPolicy#delay_excessive_requests}.
        :param requests_per_second: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#requests_per_second LbaasPolicy#requests_per_second}.
        :param zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#zone LbaasPolicy#zone}.
        :param http_error_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#http_error_code LbaasPolicy#http_error_code}.
        :param logging_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#logging_level LbaasPolicy#logging_level}.
        :param rate_limiting_criteria: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#rate_limiting_criteria LbaasPolicy#rate_limiting_criteria}.
        :param zone_memory_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#zone_memory_size LbaasPolicy#zone_memory_size}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ba1c133abb3787f408fb3dcd3c5ce117992efeb3fea4b39fabe75a7afe68c75)
            check_type(argname="argument burst_size", value=burst_size, expected_type=type_hints["burst_size"])
            check_type(argname="argument delay_excessive_requests", value=delay_excessive_requests, expected_type=type_hints["delay_excessive_requests"])
            check_type(argname="argument requests_per_second", value=requests_per_second, expected_type=type_hints["requests_per_second"])
            check_type(argname="argument zone", value=zone, expected_type=type_hints["zone"])
            check_type(argname="argument http_error_code", value=http_error_code, expected_type=type_hints["http_error_code"])
            check_type(argname="argument logging_level", value=logging_level, expected_type=type_hints["logging_level"])
            check_type(argname="argument rate_limiting_criteria", value=rate_limiting_criteria, expected_type=type_hints["rate_limiting_criteria"])
            check_type(argname="argument zone_memory_size", value=zone_memory_size, expected_type=type_hints["zone_memory_size"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "burst_size": burst_size,
            "delay_excessive_requests": delay_excessive_requests,
            "requests_per_second": requests_per_second,
            "zone": zone,
        }
        if http_error_code is not None:
            self._values["http_error_code"] = http_error_code
        if logging_level is not None:
            self._values["logging_level"] = logging_level
        if rate_limiting_criteria is not None:
            self._values["rate_limiting_criteria"] = rate_limiting_criteria
        if zone_memory_size is not None:
            self._values["zone_memory_size"] = zone_memory_size

    @builtins.property
    def burst_size(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#burst_size LbaasPolicy#burst_size}.'''
        result = self._values.get("burst_size")
        assert result is not None, "Required property 'burst_size' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def delay_excessive_requests(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#delay_excessive_requests LbaasPolicy#delay_excessive_requests}.'''
        result = self._values.get("delay_excessive_requests")
        assert result is not None, "Required property 'delay_excessive_requests' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def requests_per_second(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#requests_per_second LbaasPolicy#requests_per_second}.'''
        result = self._values.get("requests_per_second")
        assert result is not None, "Required property 'requests_per_second' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def zone(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#zone LbaasPolicy#zone}.'''
        result = self._values.get("zone")
        assert result is not None, "Required property 'zone' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def http_error_code(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#http_error_code LbaasPolicy#http_error_code}.'''
        result = self._values.get("http_error_code")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def logging_level(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#logging_level LbaasPolicy#logging_level}.'''
        result = self._values.get("logging_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rate_limiting_criteria(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#rate_limiting_criteria LbaasPolicy#rate_limiting_criteria}.'''
        result = self._values.get("rate_limiting_criteria")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def zone_memory_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#zone_memory_size LbaasPolicy#zone_memory_size}.'''
        result = self._values.get("zone_memory_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LbaasPolicyRateLimitingRequestPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LbaasPolicyRateLimitingRequestPolicyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-opc.lbaasPolicy.LbaasPolicyRateLimitingRequestPolicyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__69cf698d68f9caa43a8c2e74cb7d7171fcbd47ab249f26aefc46df2bb8237920)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetHttpErrorCode")
    def reset_http_error_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpErrorCode", []))

    @jsii.member(jsii_name="resetLoggingLevel")
    def reset_logging_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoggingLevel", []))

    @jsii.member(jsii_name="resetRateLimitingCriteria")
    def reset_rate_limiting_criteria(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRateLimitingCriteria", []))

    @jsii.member(jsii_name="resetZoneMemorySize")
    def reset_zone_memory_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZoneMemorySize", []))

    @builtins.property
    @jsii.member(jsii_name="burstSizeInput")
    def burst_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "burstSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="delayExcessiveRequestsInput")
    def delay_excessive_requests_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "delayExcessiveRequestsInput"))

    @builtins.property
    @jsii.member(jsii_name="httpErrorCodeInput")
    def http_error_code_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "httpErrorCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="loggingLevelInput")
    def logging_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "loggingLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="rateLimitingCriteriaInput")
    def rate_limiting_criteria_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rateLimitingCriteriaInput"))

    @builtins.property
    @jsii.member(jsii_name="requestsPerSecondInput")
    def requests_per_second_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "requestsPerSecondInput"))

    @builtins.property
    @jsii.member(jsii_name="zoneInput")
    def zone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "zoneInput"))

    @builtins.property
    @jsii.member(jsii_name="zoneMemorySizeInput")
    def zone_memory_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "zoneMemorySizeInput"))

    @builtins.property
    @jsii.member(jsii_name="burstSize")
    def burst_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "burstSize"))

    @burst_size.setter
    def burst_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1ba4eb25042e9b69d9af443459593294058d375790c5abe17b36b8eb3518011)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "burstSize", value)

    @builtins.property
    @jsii.member(jsii_name="delayExcessiveRequests")
    def delay_excessive_requests(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "delayExcessiveRequests"))

    @delay_excessive_requests.setter
    def delay_excessive_requests(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dfcda59324900426c980d0a4e492bfef9b0641f2ee47edecd8b85c9860bb397d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delayExcessiveRequests", value)

    @builtins.property
    @jsii.member(jsii_name="httpErrorCode")
    def http_error_code(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "httpErrorCode"))

    @http_error_code.setter
    def http_error_code(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d13723387ae87d4fd627882b07dfb0df75c36273d19a92ce662515234ec6e323)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpErrorCode", value)

    @builtins.property
    @jsii.member(jsii_name="loggingLevel")
    def logging_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "loggingLevel"))

    @logging_level.setter
    def logging_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62ae98ecba2dd6530132f0643b9fdc005b76959a32ae62a797d3db121f79add5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loggingLevel", value)

    @builtins.property
    @jsii.member(jsii_name="rateLimitingCriteria")
    def rate_limiting_criteria(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rateLimitingCriteria"))

    @rate_limiting_criteria.setter
    def rate_limiting_criteria(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f54ec5531fa3699635629940b8729be8e4327474af2ed39d4844a9b6fd99a51b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rateLimitingCriteria", value)

    @builtins.property
    @jsii.member(jsii_name="requestsPerSecond")
    def requests_per_second(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "requestsPerSecond"))

    @requests_per_second.setter
    def requests_per_second(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__363bac1b9f01665677970388fd5acd8170c4f238047140bbc9080c5d792f5bfc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestsPerSecond", value)

    @builtins.property
    @jsii.member(jsii_name="zone")
    def zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zone"))

    @zone.setter
    def zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef1efc08371ce234a515f75f041fe0ded3361e27a2c448f75aab3120aad3dea7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zone", value)

    @builtins.property
    @jsii.member(jsii_name="zoneMemorySize")
    def zone_memory_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "zoneMemorySize"))

    @zone_memory_size.setter
    def zone_memory_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cdc1116bb8b3a61d5f4c9ed91c73384a8e23c2163dd779070378b763d3c526c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zoneMemorySize", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LbaasPolicyRateLimitingRequestPolicy]:
        return typing.cast(typing.Optional[LbaasPolicyRateLimitingRequestPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LbaasPolicyRateLimitingRequestPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d11d9bf7218925b4459093bd35d2f6df881f639e2b9a40ea4731898f78bc7c5b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-opc.lbaasPolicy.LbaasPolicyRedirectPolicy",
    jsii_struct_bases=[],
    name_mapping={"redirect_uri": "redirectUri", "response_code": "responseCode"},
)
class LbaasPolicyRedirectPolicy:
    def __init__(
        self,
        *,
        redirect_uri: builtins.str,
        response_code: jsii.Number,
    ) -> None:
        '''
        :param redirect_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#redirect_uri LbaasPolicy#redirect_uri}.
        :param response_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#response_code LbaasPolicy#response_code}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__efd52c34df53abbe570f1e9dcc461d03afe008a97095ac0b13ec7596a677d0d0)
            check_type(argname="argument redirect_uri", value=redirect_uri, expected_type=type_hints["redirect_uri"])
            check_type(argname="argument response_code", value=response_code, expected_type=type_hints["response_code"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "redirect_uri": redirect_uri,
            "response_code": response_code,
        }

    @builtins.property
    def redirect_uri(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#redirect_uri LbaasPolicy#redirect_uri}.'''
        result = self._values.get("redirect_uri")
        assert result is not None, "Required property 'redirect_uri' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def response_code(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#response_code LbaasPolicy#response_code}.'''
        result = self._values.get("response_code")
        assert result is not None, "Required property 'response_code' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LbaasPolicyRedirectPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LbaasPolicyRedirectPolicyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-opc.lbaasPolicy.LbaasPolicyRedirectPolicyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5083222f2b2e7ff0ee2ae10d4097eeb25a27d298e407d38a90c7fb14d8dcc8db)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="redirectUriInput")
    def redirect_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "redirectUriInput"))

    @builtins.property
    @jsii.member(jsii_name="responseCodeInput")
    def response_code_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "responseCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="redirectUri")
    def redirect_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "redirectUri"))

    @redirect_uri.setter
    def redirect_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59cbc3f33faefde414c65d5092291c3fe0e28d48c8600258e7c853cf09fc63a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redirectUri", value)

    @builtins.property
    @jsii.member(jsii_name="responseCode")
    def response_code(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "responseCode"))

    @response_code.setter
    def response_code(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ca1193a5f1567244cca7b0c3579b8e0644cee457bf2e8b5e8ff0e2f333cd6b3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseCode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LbaasPolicyRedirectPolicy]:
        return typing.cast(typing.Optional[LbaasPolicyRedirectPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[LbaasPolicyRedirectPolicy]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01a155521b8673d583c6923975a702dd1c0085b5879cb00e5e515eebbf443693)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-opc.lbaasPolicy.LbaasPolicyResourceAccessControlPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "disposition": "disposition",
        "denied_clients": "deniedClients",
        "permitted_clients": "permittedClients",
    },
)
class LbaasPolicyResourceAccessControlPolicy:
    def __init__(
        self,
        *,
        disposition: builtins.str,
        denied_clients: typing.Optional[typing.Sequence[builtins.str]] = None,
        permitted_clients: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param disposition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#disposition LbaasPolicy#disposition}.
        :param denied_clients: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#denied_clients LbaasPolicy#denied_clients}.
        :param permitted_clients: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#permitted_clients LbaasPolicy#permitted_clients}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__782516a2c2b663a97fc2f8e8dbba3f4a618adb00ef40cb7a7acf3eb22d8b503f)
            check_type(argname="argument disposition", value=disposition, expected_type=type_hints["disposition"])
            check_type(argname="argument denied_clients", value=denied_clients, expected_type=type_hints["denied_clients"])
            check_type(argname="argument permitted_clients", value=permitted_clients, expected_type=type_hints["permitted_clients"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "disposition": disposition,
        }
        if denied_clients is not None:
            self._values["denied_clients"] = denied_clients
        if permitted_clients is not None:
            self._values["permitted_clients"] = permitted_clients

    @builtins.property
    def disposition(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#disposition LbaasPolicy#disposition}.'''
        result = self._values.get("disposition")
        assert result is not None, "Required property 'disposition' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def denied_clients(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#denied_clients LbaasPolicy#denied_clients}.'''
        result = self._values.get("denied_clients")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def permitted_clients(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#permitted_clients LbaasPolicy#permitted_clients}.'''
        result = self._values.get("permitted_clients")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LbaasPolicyResourceAccessControlPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LbaasPolicyResourceAccessControlPolicyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-opc.lbaasPolicy.LbaasPolicyResourceAccessControlPolicyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__73d5efba1ce0a45b4e0126dbb34a32591d818b040fb950029f51161db3a84f90)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDeniedClients")
    def reset_denied_clients(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeniedClients", []))

    @jsii.member(jsii_name="resetPermittedClients")
    def reset_permitted_clients(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPermittedClients", []))

    @builtins.property
    @jsii.member(jsii_name="deniedClientsInput")
    def denied_clients_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "deniedClientsInput"))

    @builtins.property
    @jsii.member(jsii_name="dispositionInput")
    def disposition_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dispositionInput"))

    @builtins.property
    @jsii.member(jsii_name="permittedClientsInput")
    def permitted_clients_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "permittedClientsInput"))

    @builtins.property
    @jsii.member(jsii_name="deniedClients")
    def denied_clients(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "deniedClients"))

    @denied_clients.setter
    def denied_clients(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6a29f09ad7d66393461c6f4589a26ca6704c0d614d9fa6f11f4567ef71dd8e4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deniedClients", value)

    @builtins.property
    @jsii.member(jsii_name="disposition")
    def disposition(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "disposition"))

    @disposition.setter
    def disposition(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc73d7b728c621771aff4ba957d6602e7f852d8ad95735237734ffe273f4e035)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disposition", value)

    @builtins.property
    @jsii.member(jsii_name="permittedClients")
    def permitted_clients(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "permittedClients"))

    @permitted_clients.setter
    def permitted_clients(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c94d830818434b9cf22409f145f419f8bf891f842e556a649ebde556fd7183af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permittedClients", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LbaasPolicyResourceAccessControlPolicy]:
        return typing.cast(typing.Optional[LbaasPolicyResourceAccessControlPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LbaasPolicyResourceAccessControlPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34c0bbf68fa67dbf9fa7e736908326ea0b92008ff946415b8b756b6a67d1e866)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-opc.lbaasPolicy.LbaasPolicySetRequestHeaderPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "header_name": "headerName",
        "action_when_header_exists": "actionWhenHeaderExists",
        "action_when_header_value_is": "actionWhenHeaderValueIs",
        "action_when_header_value_is_not": "actionWhenHeaderValueIsNot",
        "value": "value",
    },
)
class LbaasPolicySetRequestHeaderPolicy:
    def __init__(
        self,
        *,
        header_name: builtins.str,
        action_when_header_exists: typing.Optional[builtins.str] = None,
        action_when_header_value_is: typing.Optional[typing.Sequence[builtins.str]] = None,
        action_when_header_value_is_not: typing.Optional[typing.Sequence[builtins.str]] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param header_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#header_name LbaasPolicy#header_name}.
        :param action_when_header_exists: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#action_when_header_exists LbaasPolicy#action_when_header_exists}.
        :param action_when_header_value_is: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#action_when_header_value_is LbaasPolicy#action_when_header_value_is}.
        :param action_when_header_value_is_not: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#action_when_header_value_is_not LbaasPolicy#action_when_header_value_is_not}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#value LbaasPolicy#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f81f3e0203e2548edcbb3fd26bdee2eadc0b464783e7fad08950c9acfd598db3)
            check_type(argname="argument header_name", value=header_name, expected_type=type_hints["header_name"])
            check_type(argname="argument action_when_header_exists", value=action_when_header_exists, expected_type=type_hints["action_when_header_exists"])
            check_type(argname="argument action_when_header_value_is", value=action_when_header_value_is, expected_type=type_hints["action_when_header_value_is"])
            check_type(argname="argument action_when_header_value_is_not", value=action_when_header_value_is_not, expected_type=type_hints["action_when_header_value_is_not"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "header_name": header_name,
        }
        if action_when_header_exists is not None:
            self._values["action_when_header_exists"] = action_when_header_exists
        if action_when_header_value_is is not None:
            self._values["action_when_header_value_is"] = action_when_header_value_is
        if action_when_header_value_is_not is not None:
            self._values["action_when_header_value_is_not"] = action_when_header_value_is_not
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def header_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#header_name LbaasPolicy#header_name}.'''
        result = self._values.get("header_name")
        assert result is not None, "Required property 'header_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def action_when_header_exists(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#action_when_header_exists LbaasPolicy#action_when_header_exists}.'''
        result = self._values.get("action_when_header_exists")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def action_when_header_value_is(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#action_when_header_value_is LbaasPolicy#action_when_header_value_is}.'''
        result = self._values.get("action_when_header_value_is")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def action_when_header_value_is_not(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#action_when_header_value_is_not LbaasPolicy#action_when_header_value_is_not}.'''
        result = self._values.get("action_when_header_value_is_not")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#value LbaasPolicy#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LbaasPolicySetRequestHeaderPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LbaasPolicySetRequestHeaderPolicyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-opc.lbaasPolicy.LbaasPolicySetRequestHeaderPolicyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7aca196e3d104d1ecad91520555dc9d1ce1638ef17d0a5c9edc52a2001d715a9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetActionWhenHeaderExists")
    def reset_action_when_header_exists(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActionWhenHeaderExists", []))

    @jsii.member(jsii_name="resetActionWhenHeaderValueIs")
    def reset_action_when_header_value_is(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActionWhenHeaderValueIs", []))

    @jsii.member(jsii_name="resetActionWhenHeaderValueIsNot")
    def reset_action_when_header_value_is_not(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActionWhenHeaderValueIsNot", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="actionWhenHeaderExistsInput")
    def action_when_header_exists_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionWhenHeaderExistsInput"))

    @builtins.property
    @jsii.member(jsii_name="actionWhenHeaderValueIsInput")
    def action_when_header_value_is_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "actionWhenHeaderValueIsInput"))

    @builtins.property
    @jsii.member(jsii_name="actionWhenHeaderValueIsNotInput")
    def action_when_header_value_is_not_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "actionWhenHeaderValueIsNotInput"))

    @builtins.property
    @jsii.member(jsii_name="headerNameInput")
    def header_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "headerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="actionWhenHeaderExists")
    def action_when_header_exists(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "actionWhenHeaderExists"))

    @action_when_header_exists.setter
    def action_when_header_exists(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f09c257a3ada0f9337328731c74043fb66dd288da1c188cdf02e7d1d4b52d23d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "actionWhenHeaderExists", value)

    @builtins.property
    @jsii.member(jsii_name="actionWhenHeaderValueIs")
    def action_when_header_value_is(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "actionWhenHeaderValueIs"))

    @action_when_header_value_is.setter
    def action_when_header_value_is(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__978f0e0d628dd1665391d46b0da31c6da602477380fb950c4930c628c4080d52)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "actionWhenHeaderValueIs", value)

    @builtins.property
    @jsii.member(jsii_name="actionWhenHeaderValueIsNot")
    def action_when_header_value_is_not(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "actionWhenHeaderValueIsNot"))

    @action_when_header_value_is_not.setter
    def action_when_header_value_is_not(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e5370e85d08ca995e7096718a6988d82e901b927739b999ad5e9f96c089e538)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "actionWhenHeaderValueIsNot", value)

    @builtins.property
    @jsii.member(jsii_name="headerName")
    def header_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "headerName"))

    @header_name.setter
    def header_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79d2677ad8fe25b71a35c5444c0a5693a9b84c7ac118c908e10c929b5098dd4a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headerName", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a72889b94a6efee9eec82865f9508f28a3ee60f9184ffcba45323a4ae172cc7a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LbaasPolicySetRequestHeaderPolicy]:
        return typing.cast(typing.Optional[LbaasPolicySetRequestHeaderPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LbaasPolicySetRequestHeaderPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f37b13d57f7128a02e4f687e3b3ec93f52983966d318808094386864019e3009)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-opc.lbaasPolicy.LbaasPolicySslNegotiationPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "port": "port",
        "ssl_protocol": "sslProtocol",
        "server_order_preference": "serverOrderPreference",
        "ssl_ciphers": "sslCiphers",
    },
)
class LbaasPolicySslNegotiationPolicy:
    def __init__(
        self,
        *,
        port: jsii.Number,
        ssl_protocol: typing.Sequence[builtins.str],
        server_order_preference: typing.Optional[builtins.str] = None,
        ssl_ciphers: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#port LbaasPolicy#port}.
        :param ssl_protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#ssl_protocol LbaasPolicy#ssl_protocol}.
        :param server_order_preference: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#server_order_preference LbaasPolicy#server_order_preference}.
        :param ssl_ciphers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#ssl_ciphers LbaasPolicy#ssl_ciphers}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81b1ba0df07a893c2860d6bbefea62e8f07e1f4ddea9df617f99b235f4957d8f)
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument ssl_protocol", value=ssl_protocol, expected_type=type_hints["ssl_protocol"])
            check_type(argname="argument server_order_preference", value=server_order_preference, expected_type=type_hints["server_order_preference"])
            check_type(argname="argument ssl_ciphers", value=ssl_ciphers, expected_type=type_hints["ssl_ciphers"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "port": port,
            "ssl_protocol": ssl_protocol,
        }
        if server_order_preference is not None:
            self._values["server_order_preference"] = server_order_preference
        if ssl_ciphers is not None:
            self._values["ssl_ciphers"] = ssl_ciphers

    @builtins.property
    def port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#port LbaasPolicy#port}.'''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def ssl_protocol(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#ssl_protocol LbaasPolicy#ssl_protocol}.'''
        result = self._values.get("ssl_protocol")
        assert result is not None, "Required property 'ssl_protocol' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def server_order_preference(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#server_order_preference LbaasPolicy#server_order_preference}.'''
        result = self._values.get("server_order_preference")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ssl_ciphers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#ssl_ciphers LbaasPolicy#ssl_ciphers}.'''
        result = self._values.get("ssl_ciphers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LbaasPolicySslNegotiationPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LbaasPolicySslNegotiationPolicyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-opc.lbaasPolicy.LbaasPolicySslNegotiationPolicyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__159619460f4b219dde01aebf0d04afbcbb2f7de209038e9d3bdd21ced92c4832)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetServerOrderPreference")
    def reset_server_order_preference(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServerOrderPreference", []))

    @jsii.member(jsii_name="resetSslCiphers")
    def reset_ssl_ciphers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSslCiphers", []))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="serverOrderPreferenceInput")
    def server_order_preference_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverOrderPreferenceInput"))

    @builtins.property
    @jsii.member(jsii_name="sslCiphersInput")
    def ssl_ciphers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sslCiphersInput"))

    @builtins.property
    @jsii.member(jsii_name="sslProtocolInput")
    def ssl_protocol_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sslProtocolInput"))

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5adcc79559f1d6f6343d0bc4879a85426bf9cfed47564a5509af69d527e87e5f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="serverOrderPreference")
    def server_order_preference(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serverOrderPreference"))

    @server_order_preference.setter
    def server_order_preference(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8cb9e37907b605ba7554a61e7486e13a3ea2cffdcf843ec3d1070af0cf7c47d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverOrderPreference", value)

    @builtins.property
    @jsii.member(jsii_name="sslCiphers")
    def ssl_ciphers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sslCiphers"))

    @ssl_ciphers.setter
    def ssl_ciphers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ae570e499db051ada8db97840614feae66a3cc8f1c29e360a1dbb9035e4ba60)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sslCiphers", value)

    @builtins.property
    @jsii.member(jsii_name="sslProtocol")
    def ssl_protocol(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sslProtocol"))

    @ssl_protocol.setter
    def ssl_protocol(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__740abd0e76f8e4f16783cc5b9d21a345b6c2b59ae3f732ff66ed5ddf574439a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sslProtocol", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LbaasPolicySslNegotiationPolicy]:
        return typing.cast(typing.Optional[LbaasPolicySslNegotiationPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LbaasPolicySslNegotiationPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60f4d24704edf714e44bb078e96b923a116ca51e496011d27e8bad8ebc0445d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-opc.lbaasPolicy.LbaasPolicyTrustedCertificatePolicy",
    jsii_struct_bases=[],
    name_mapping={"trusted_certificate": "trustedCertificate"},
)
class LbaasPolicyTrustedCertificatePolicy:
    def __init__(self, *, trusted_certificate: builtins.str) -> None:
        '''
        :param trusted_certificate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#trusted_certificate LbaasPolicy#trusted_certificate}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94cf4b4e951ff42bc694209b97e1cde6bb6c893a86ef38a968c60b8fc248f4f6)
            check_type(argname="argument trusted_certificate", value=trusted_certificate, expected_type=type_hints["trusted_certificate"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "trusted_certificate": trusted_certificate,
        }

    @builtins.property
    def trusted_certificate(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_policy#trusted_certificate LbaasPolicy#trusted_certificate}.'''
        result = self._values.get("trusted_certificate")
        assert result is not None, "Required property 'trusted_certificate' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LbaasPolicyTrustedCertificatePolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LbaasPolicyTrustedCertificatePolicyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-opc.lbaasPolicy.LbaasPolicyTrustedCertificatePolicyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__dc2578e0677e8038e112a1b6d888c700dcce4346fc1e6467d35f2ec760904b99)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="trustedCertificateInput")
    def trusted_certificate_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "trustedCertificateInput"))

    @builtins.property
    @jsii.member(jsii_name="trustedCertificate")
    def trusted_certificate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "trustedCertificate"))

    @trusted_certificate.setter
    def trusted_certificate(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c805ed193c8e6124d1e69d1557a2169f8e2fb8ba79f6c53d3ac15a820ea0224c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "trustedCertificate", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LbaasPolicyTrustedCertificatePolicy]:
        return typing.cast(typing.Optional[LbaasPolicyTrustedCertificatePolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LbaasPolicyTrustedCertificatePolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2035e05c53d0de0bb96eeba011a1276738daea4208c72fd49bad95029d3ab43)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "LbaasPolicy",
    "LbaasPolicyApplicationCookieStickinessPolicy",
    "LbaasPolicyApplicationCookieStickinessPolicyOutputReference",
    "LbaasPolicyCloudgatePolicy",
    "LbaasPolicyCloudgatePolicyOutputReference",
    "LbaasPolicyConfig",
    "LbaasPolicyLoadBalancerCookieStickinessPolicy",
    "LbaasPolicyLoadBalancerCookieStickinessPolicyOutputReference",
    "LbaasPolicyLoadBalancingMechanismPolicy",
    "LbaasPolicyLoadBalancingMechanismPolicyOutputReference",
    "LbaasPolicyRateLimitingRequestPolicy",
    "LbaasPolicyRateLimitingRequestPolicyOutputReference",
    "LbaasPolicyRedirectPolicy",
    "LbaasPolicyRedirectPolicyOutputReference",
    "LbaasPolicyResourceAccessControlPolicy",
    "LbaasPolicyResourceAccessControlPolicyOutputReference",
    "LbaasPolicySetRequestHeaderPolicy",
    "LbaasPolicySetRequestHeaderPolicyOutputReference",
    "LbaasPolicySslNegotiationPolicy",
    "LbaasPolicySslNegotiationPolicyOutputReference",
    "LbaasPolicyTrustedCertificatePolicy",
    "LbaasPolicyTrustedCertificatePolicyOutputReference",
]

publication.publish()

def _typecheckingstub__3279d9c3fecbd56b29535b57f2fe62bcc8f6d88c837af2b2fc7c80cb01a3c3d4(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    load_balancer: builtins.str,
    name: builtins.str,
    application_cookie_stickiness_policy: typing.Optional[typing.Union[LbaasPolicyApplicationCookieStickinessPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    cloudgate_policy: typing.Optional[typing.Union[LbaasPolicyCloudgatePolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    load_balancer_cookie_stickiness_policy: typing.Optional[typing.Union[LbaasPolicyLoadBalancerCookieStickinessPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    load_balancing_mechanism_policy: typing.Optional[typing.Union[LbaasPolicyLoadBalancingMechanismPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    rate_limiting_request_policy: typing.Optional[typing.Union[LbaasPolicyRateLimitingRequestPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    redirect_policy: typing.Optional[typing.Union[LbaasPolicyRedirectPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    resource_access_control_policy: typing.Optional[typing.Union[LbaasPolicyResourceAccessControlPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    set_request_header_policy: typing.Optional[typing.Union[LbaasPolicySetRequestHeaderPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    ssl_negotiation_policy: typing.Optional[typing.Union[LbaasPolicySslNegotiationPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    trusted_certificate_policy: typing.Optional[typing.Union[LbaasPolicyTrustedCertificatePolicy, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__4f60c179d1855388fca5845ed43fe6c5b9240666db5f78b4eb271bf0f37c5cd7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0e76d75d4c62fbfc8092abaa53b0a94c4b7631f0d78a89ae29c99cccf9715fb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74316676f002b47e4b0adf5e2e4a05ecc82605287ba30df74b309c0dfb7ea297(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b05c133e36f99ab703ddabe70fdb4021aa65a103f639864e3a7016bd9e842267(
    *,
    cookie_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ade0d22fe32a0c7a397eca74113d523d22eb3d58b4593766e2233f09de608f61(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1147827db676648811436064c5acb410992b46884ed5377fe4a0463bb7386fdb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfdd7e144befe2e0238a210bfeb7051468fdc2199efc24f42394add331b44344(
    value: typing.Optional[LbaasPolicyApplicationCookieStickinessPolicy],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af7a622f455d4701699a6d66b28a6a3e1270cebc2a5c4b0a369c517ba48efcf6(
    *,
    virtual_hostname_for_policy_attribution: builtins.str,
    cloudgate_application: typing.Optional[builtins.str] = None,
    cloudgate_policy_name: typing.Optional[builtins.str] = None,
    identity_service_instance_guid: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45fde25f007faaecbef4aa3c23123ae46e90de101a655dc0502432a1530b1eb2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7869522c91257550c207b5e63cd483e88475822ac5b16eec05a494c0a3f8b159(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fa3db2c49c9c72ad82b8f4fdf0486f4d13dadbb0d16c428b625b58586f79743(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b1adaa3ebcf0ca174f1ddc59d57cbe53c0d5a42f0d72a89055209ccdffd2018(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6c1dce9ddf35eddc32fc6251068697677ce61986b1f095aab5f8af77b247359(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e728720be377f3cc5d7cfaed2f4ea853d1c909ff00b52deb58491051a89a228(
    value: typing.Optional[LbaasPolicyCloudgatePolicy],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13d9c7b0886043f8985bab37aaf68a25ec9d7b514b62fbdfee5ff7479b42c49b(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    load_balancer: builtins.str,
    name: builtins.str,
    application_cookie_stickiness_policy: typing.Optional[typing.Union[LbaasPolicyApplicationCookieStickinessPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    cloudgate_policy: typing.Optional[typing.Union[LbaasPolicyCloudgatePolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    load_balancer_cookie_stickiness_policy: typing.Optional[typing.Union[LbaasPolicyLoadBalancerCookieStickinessPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    load_balancing_mechanism_policy: typing.Optional[typing.Union[LbaasPolicyLoadBalancingMechanismPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    rate_limiting_request_policy: typing.Optional[typing.Union[LbaasPolicyRateLimitingRequestPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    redirect_policy: typing.Optional[typing.Union[LbaasPolicyRedirectPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    resource_access_control_policy: typing.Optional[typing.Union[LbaasPolicyResourceAccessControlPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    set_request_header_policy: typing.Optional[typing.Union[LbaasPolicySetRequestHeaderPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    ssl_negotiation_policy: typing.Optional[typing.Union[LbaasPolicySslNegotiationPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    trusted_certificate_policy: typing.Optional[typing.Union[LbaasPolicyTrustedCertificatePolicy, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54a2cf37ad6db4eec7cb1f22836903bdc729846dc80e7a7ad3687f537e56434b(
    *,
    cookie_expiration_period: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__763e52ac2c161eaeb29d3904fcc0890c422652ba21829d8ead6fd9476d43adba(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4dd52500cbeec3870762f92a21ac36eb5e57d3f9bbfe6ca81cb036ea27922612(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5df5e84411aa89463126cd401b72f11d9910b68e8bbc151225ef005f5f4aa764(
    value: typing.Optional[LbaasPolicyLoadBalancerCookieStickinessPolicy],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5f8184114950c5bb3357deb10ddd1d1a64498f2ba4f9bfb90887aa6741cd7d3(
    *,
    load_balancing_mechanism: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57fde6c3fef83db3d7963201d12c628483be67d74530c002ff1f828aacf2d18a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__faf83ab5804be9f71795477f6becf6e8a33825fa2b71e84988a397980cbe1f92(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8976e6612042798d3f4ff45cc38845d8bfee446d62ae684b41c0e3d5d06bd2ac(
    value: typing.Optional[LbaasPolicyLoadBalancingMechanismPolicy],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ba1c133abb3787f408fb3dcd3c5ce117992efeb3fea4b39fabe75a7afe68c75(
    *,
    burst_size: jsii.Number,
    delay_excessive_requests: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    requests_per_second: jsii.Number,
    zone: builtins.str,
    http_error_code: typing.Optional[jsii.Number] = None,
    logging_level: typing.Optional[builtins.str] = None,
    rate_limiting_criteria: typing.Optional[builtins.str] = None,
    zone_memory_size: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69cf698d68f9caa43a8c2e74cb7d7171fcbd47ab249f26aefc46df2bb8237920(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1ba4eb25042e9b69d9af443459593294058d375790c5abe17b36b8eb3518011(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dfcda59324900426c980d0a4e492bfef9b0641f2ee47edecd8b85c9860bb397d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d13723387ae87d4fd627882b07dfb0df75c36273d19a92ce662515234ec6e323(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62ae98ecba2dd6530132f0643b9fdc005b76959a32ae62a797d3db121f79add5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f54ec5531fa3699635629940b8729be8e4327474af2ed39d4844a9b6fd99a51b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__363bac1b9f01665677970388fd5acd8170c4f238047140bbc9080c5d792f5bfc(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef1efc08371ce234a515f75f041fe0ded3361e27a2c448f75aab3120aad3dea7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdc1116bb8b3a61d5f4c9ed91c73384a8e23c2163dd779070378b763d3c526c2(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d11d9bf7218925b4459093bd35d2f6df881f639e2b9a40ea4731898f78bc7c5b(
    value: typing.Optional[LbaasPolicyRateLimitingRequestPolicy],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efd52c34df53abbe570f1e9dcc461d03afe008a97095ac0b13ec7596a677d0d0(
    *,
    redirect_uri: builtins.str,
    response_code: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5083222f2b2e7ff0ee2ae10d4097eeb25a27d298e407d38a90c7fb14d8dcc8db(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59cbc3f33faefde414c65d5092291c3fe0e28d48c8600258e7c853cf09fc63a4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ca1193a5f1567244cca7b0c3579b8e0644cee457bf2e8b5e8ff0e2f333cd6b3(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01a155521b8673d583c6923975a702dd1c0085b5879cb00e5e515eebbf443693(
    value: typing.Optional[LbaasPolicyRedirectPolicy],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__782516a2c2b663a97fc2f8e8dbba3f4a618adb00ef40cb7a7acf3eb22d8b503f(
    *,
    disposition: builtins.str,
    denied_clients: typing.Optional[typing.Sequence[builtins.str]] = None,
    permitted_clients: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73d5efba1ce0a45b4e0126dbb34a32591d818b040fb950029f51161db3a84f90(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6a29f09ad7d66393461c6f4589a26ca6704c0d614d9fa6f11f4567ef71dd8e4(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc73d7b728c621771aff4ba957d6602e7f852d8ad95735237734ffe273f4e035(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c94d830818434b9cf22409f145f419f8bf891f842e556a649ebde556fd7183af(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34c0bbf68fa67dbf9fa7e736908326ea0b92008ff946415b8b756b6a67d1e866(
    value: typing.Optional[LbaasPolicyResourceAccessControlPolicy],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f81f3e0203e2548edcbb3fd26bdee2eadc0b464783e7fad08950c9acfd598db3(
    *,
    header_name: builtins.str,
    action_when_header_exists: typing.Optional[builtins.str] = None,
    action_when_header_value_is: typing.Optional[typing.Sequence[builtins.str]] = None,
    action_when_header_value_is_not: typing.Optional[typing.Sequence[builtins.str]] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7aca196e3d104d1ecad91520555dc9d1ce1638ef17d0a5c9edc52a2001d715a9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f09c257a3ada0f9337328731c74043fb66dd288da1c188cdf02e7d1d4b52d23d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__978f0e0d628dd1665391d46b0da31c6da602477380fb950c4930c628c4080d52(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e5370e85d08ca995e7096718a6988d82e901b927739b999ad5e9f96c089e538(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79d2677ad8fe25b71a35c5444c0a5693a9b84c7ac118c908e10c929b5098dd4a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a72889b94a6efee9eec82865f9508f28a3ee60f9184ffcba45323a4ae172cc7a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f37b13d57f7128a02e4f687e3b3ec93f52983966d318808094386864019e3009(
    value: typing.Optional[LbaasPolicySetRequestHeaderPolicy],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81b1ba0df07a893c2860d6bbefea62e8f07e1f4ddea9df617f99b235f4957d8f(
    *,
    port: jsii.Number,
    ssl_protocol: typing.Sequence[builtins.str],
    server_order_preference: typing.Optional[builtins.str] = None,
    ssl_ciphers: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__159619460f4b219dde01aebf0d04afbcbb2f7de209038e9d3bdd21ced92c4832(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5adcc79559f1d6f6343d0bc4879a85426bf9cfed47564a5509af69d527e87e5f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8cb9e37907b605ba7554a61e7486e13a3ea2cffdcf843ec3d1070af0cf7c47d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ae570e499db051ada8db97840614feae66a3cc8f1c29e360a1dbb9035e4ba60(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__740abd0e76f8e4f16783cc5b9d21a345b6c2b59ae3f732ff66ed5ddf574439a0(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60f4d24704edf714e44bb078e96b923a116ca51e496011d27e8bad8ebc0445d0(
    value: typing.Optional[LbaasPolicySslNegotiationPolicy],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94cf4b4e951ff42bc694209b97e1cde6bb6c893a86ef38a968c60b8fc248f4f6(
    *,
    trusted_certificate: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc2578e0677e8038e112a1b6d888c700dcce4346fc1e6467d35f2ec760904b99(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c805ed193c8e6124d1e69d1557a2169f8e2fb8ba79f6c53d3ac15a820ea0224c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2035e05c53d0de0bb96eeba011a1276738daea4208c72fd49bad95029d3ab43(
    value: typing.Optional[LbaasPolicyTrustedCertificatePolicy],
) -> None:
    """Type checking stubs"""
    pass
