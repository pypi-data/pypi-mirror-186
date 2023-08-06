'''
# `ad_gpo_security`

Refer to the Terraform Registory for docs: [`ad_gpo_security`](https://www.terraform.io/docs/providers/ad/r/gpo_security).
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


class GpoSecurity(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-ad.gpoSecurity.GpoSecurity",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/ad/r/gpo_security ad_gpo_security}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        gpo_container: builtins.str,
        account_lockout: typing.Optional[typing.Union["GpoSecurityAccountLockout", typing.Dict[builtins.str, typing.Any]]] = None,
        application_log: typing.Optional[typing.Union["GpoSecurityApplicationLog", typing.Dict[builtins.str, typing.Any]]] = None,
        audit_log: typing.Optional[typing.Union["GpoSecurityAuditLog", typing.Dict[builtins.str, typing.Any]]] = None,
        event_audit: typing.Optional[typing.Union["GpoSecurityEventAudit", typing.Dict[builtins.str, typing.Any]]] = None,
        filesystem: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GpoSecurityFilesystem", typing.Dict[builtins.str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        kerberos_policy: typing.Optional[typing.Union["GpoSecurityKerberosPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        password_policies: typing.Optional[typing.Union["GpoSecurityPasswordPolicies", typing.Dict[builtins.str, typing.Any]]] = None,
        registry_keys: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GpoSecurityRegistryKeys", typing.Dict[builtins.str, typing.Any]]]]] = None,
        registry_values: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GpoSecurityRegistryValues", typing.Dict[builtins.str, typing.Any]]]]] = None,
        restricted_groups: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GpoSecurityRestrictedGroups", typing.Dict[builtins.str, typing.Any]]]]] = None,
        system_log: typing.Optional[typing.Union["GpoSecuritySystemLog", typing.Dict[builtins.str, typing.Any]]] = None,
        system_services: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GpoSecuritySystemServices", typing.Dict[builtins.str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/ad/r/gpo_security ad_gpo_security} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param gpo_container: The GUID of the container the security settings belong to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#gpo_container GpoSecurity#gpo_container}
        :param account_lockout: account_lockout block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#account_lockout GpoSecurity#account_lockout}
        :param application_log: application_log block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#application_log GpoSecurity#application_log}
        :param audit_log: audit_log block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#audit_log GpoSecurity#audit_log}
        :param event_audit: event_audit block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#event_audit GpoSecurity#event_audit}
        :param filesystem: filesystem block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#filesystem GpoSecurity#filesystem}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#id GpoSecurity#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kerberos_policy: kerberos_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#kerberos_policy GpoSecurity#kerberos_policy}
        :param password_policies: password_policies block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#password_policies GpoSecurity#password_policies}
        :param registry_keys: registry_keys block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#registry_keys GpoSecurity#registry_keys}
        :param registry_values: registry_values block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#registry_values GpoSecurity#registry_values}
        :param restricted_groups: restricted_groups block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#restricted_groups GpoSecurity#restricted_groups}
        :param system_log: system_log block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#system_log GpoSecurity#system_log}
        :param system_services: system_services block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#system_services GpoSecurity#system_services}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cdb1107fda99a69a663814450f726e0075566c2fbd1e3fef8eef763c7bfe69bd)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GpoSecurityConfig(
            gpo_container=gpo_container,
            account_lockout=account_lockout,
            application_log=application_log,
            audit_log=audit_log,
            event_audit=event_audit,
            filesystem=filesystem,
            id=id,
            kerberos_policy=kerberos_policy,
            password_policies=password_policies,
            registry_keys=registry_keys,
            registry_values=registry_values,
            restricted_groups=restricted_groups,
            system_log=system_log,
            system_services=system_services,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAccountLockout")
    def put_account_lockout(
        self,
        *,
        force_logoff_when_hour_expire: typing.Optional[builtins.str] = None,
        lockout_bad_count: typing.Optional[builtins.str] = None,
        lockout_duration: typing.Optional[builtins.str] = None,
        reset_lockout_count: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param force_logoff_when_hour_expire: Disconnect SMB sessions when logon hours expire. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#force_logoff_when_hour_expire GpoSecurity#force_logoff_when_hour_expire}
        :param lockout_bad_count: Number of failed logon attempts until a account is locked. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#lockout_bad_count GpoSecurity#lockout_bad_count}
        :param lockout_duration: Number of minutes a locked out account must remain locked out. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#lockout_duration GpoSecurity#lockout_duration}
        :param reset_lockout_count: Number of minutes a account will remain locked after a failed logon attempt. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#reset_lockout_count GpoSecurity#reset_lockout_count}
        '''
        value = GpoSecurityAccountLockout(
            force_logoff_when_hour_expire=force_logoff_when_hour_expire,
            lockout_bad_count=lockout_bad_count,
            lockout_duration=lockout_duration,
            reset_lockout_count=reset_lockout_count,
        )

        return typing.cast(None, jsii.invoke(self, "putAccountLockout", [value]))

    @jsii.member(jsii_name="putApplicationLog")
    def put_application_log(
        self,
        *,
        audit_log_retention_period: typing.Optional[builtins.str] = None,
        maximum_log_size: typing.Optional[builtins.str] = None,
        restrict_guest_access: typing.Optional[builtins.str] = None,
        retention_days: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param audit_log_retention_period: Control log retention. Values: 0: overwrite events as needed, 1: overwrite events as specified specified by ``retention_days``, 2: never overwrite events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#audit_log_retention_period GpoSecurity#audit_log_retention_period}
        :param maximum_log_size: Maximum size of log in KiloBytes. (64-4194240). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#maximum_log_size GpoSecurity#maximum_log_size}
        :param restrict_guest_access: Restrict access to logs for guest users. A non-zero value restricts access to guest users. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#restrict_guest_access GpoSecurity#restrict_guest_access}
        :param retention_days: Number of days before new events overwrite old events. (1-365). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#retention_days GpoSecurity#retention_days}
        '''
        value = GpoSecurityApplicationLog(
            audit_log_retention_period=audit_log_retention_period,
            maximum_log_size=maximum_log_size,
            restrict_guest_access=restrict_guest_access,
            retention_days=retention_days,
        )

        return typing.cast(None, jsii.invoke(self, "putApplicationLog", [value]))

    @jsii.member(jsii_name="putAuditLog")
    def put_audit_log(
        self,
        *,
        audit_log_retention_period: typing.Optional[builtins.str] = None,
        maximum_log_size: typing.Optional[builtins.str] = None,
        restrict_guest_access: typing.Optional[builtins.str] = None,
        retention_days: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param audit_log_retention_period: Control log retention. Values: 0: overwrite events as needed, 1: overwrite events as specified specified by ``retention_days``, 2: never overwrite events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#audit_log_retention_period GpoSecurity#audit_log_retention_period}
        :param maximum_log_size: Maximum size of log in KiloBytes. (64-4194240). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#maximum_log_size GpoSecurity#maximum_log_size}
        :param restrict_guest_access: Restrict access to logs for guest users. A non-zero value restricts access to guest users. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#restrict_guest_access GpoSecurity#restrict_guest_access}
        :param retention_days: Number of days before new events overwrite old events. (1-365). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#retention_days GpoSecurity#retention_days}
        '''
        value = GpoSecurityAuditLog(
            audit_log_retention_period=audit_log_retention_period,
            maximum_log_size=maximum_log_size,
            restrict_guest_access=restrict_guest_access,
            retention_days=retention_days,
        )

        return typing.cast(None, jsii.invoke(self, "putAuditLog", [value]))

    @jsii.member(jsii_name="putEventAudit")
    def put_event_audit(
        self,
        *,
        audit_account_logon: typing.Optional[builtins.str] = None,
        audit_account_manage: typing.Optional[builtins.str] = None,
        audit_ds_access: typing.Optional[builtins.str] = None,
        audit_logon_events: typing.Optional[builtins.str] = None,
        audit_object_access: typing.Optional[builtins.str] = None,
        audit_policy_change: typing.Optional[builtins.str] = None,
        audit_privilege_use: typing.Optional[builtins.str] = None,
        audit_process_tracking: typing.Optional[builtins.str] = None,
        audit_system_events: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param audit_account_logon: Audit credential validation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#audit_account_logon GpoSecurity#audit_account_logon}
        :param audit_account_manage: Audit account management events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#audit_account_manage GpoSecurity#audit_account_manage}
        :param audit_ds_access: Audit access attempts to AD objects. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#audit_ds_access GpoSecurity#audit_ds_access}
        :param audit_logon_events: Audit logon events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#audit_logon_events GpoSecurity#audit_logon_events}
        :param audit_object_access: Audit access attempts to non-AD objects. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#audit_object_access GpoSecurity#audit_object_access}
        :param audit_policy_change: Audit attempts to change a policy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#audit_policy_change GpoSecurity#audit_policy_change}
        :param audit_privilege_use: Audit user attempts of exercising user rights. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#audit_privilege_use GpoSecurity#audit_privilege_use}
        :param audit_process_tracking: Audit process related events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#audit_process_tracking GpoSecurity#audit_process_tracking}
        :param audit_system_events: Audit system events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#audit_system_events GpoSecurity#audit_system_events}
        '''
        value = GpoSecurityEventAudit(
            audit_account_logon=audit_account_logon,
            audit_account_manage=audit_account_manage,
            audit_ds_access=audit_ds_access,
            audit_logon_events=audit_logon_events,
            audit_object_access=audit_object_access,
            audit_policy_change=audit_policy_change,
            audit_privilege_use=audit_privilege_use,
            audit_process_tracking=audit_process_tracking,
            audit_system_events=audit_system_events,
        )

        return typing.cast(None, jsii.invoke(self, "putEventAudit", [value]))

    @jsii.member(jsii_name="putFilesystem")
    def put_filesystem(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GpoSecurityFilesystem", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a95d4be4b10541ca0b6a13f4568a834665f4039492895b15e0b50371922a1be9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putFilesystem", [value]))

    @jsii.member(jsii_name="putKerberosPolicy")
    def put_kerberos_policy(
        self,
        *,
        max_clock_skew: typing.Optional[builtins.str] = None,
        max_renew_age: typing.Optional[builtins.str] = None,
        max_service_age: typing.Optional[builtins.str] = None,
        max_ticket_age: typing.Optional[builtins.str] = None,
        ticket_validate_client: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param max_clock_skew: Maximum time difference, in minutes, between the client clock and the server clock. (0-99999). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#max_clock_skew GpoSecurity#max_clock_skew}
        :param max_renew_age: Number of days during which a ticket-granting ticket can be renewed (0-99999). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#max_renew_age GpoSecurity#max_renew_age}
        :param max_service_age: Maximum amount of minutes a ticket must be valid to access a service or resource. Minimum should be 10 and maximum should be equal to ``max_ticket_age``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#max_service_age GpoSecurity#max_service_age}
        :param max_ticket_age: Maximum amount of hours a ticket-granting ticket is valid (0-99999). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#max_ticket_age GpoSecurity#max_ticket_age}
        :param ticket_validate_client: Control if the session ticket is validated for every request. A non-zero value disables the policy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#ticket_validate_client GpoSecurity#ticket_validate_client}
        '''
        value = GpoSecurityKerberosPolicy(
            max_clock_skew=max_clock_skew,
            max_renew_age=max_renew_age,
            max_service_age=max_service_age,
            max_ticket_age=max_ticket_age,
            ticket_validate_client=ticket_validate_client,
        )

        return typing.cast(None, jsii.invoke(self, "putKerberosPolicy", [value]))

    @jsii.member(jsii_name="putPasswordPolicies")
    def put_password_policies(
        self,
        *,
        clear_text_password: typing.Optional[builtins.str] = None,
        maximum_password_age: typing.Optional[builtins.str] = None,
        minimum_password_age: typing.Optional[builtins.str] = None,
        minimum_password_length: typing.Optional[builtins.str] = None,
        password_complexity: typing.Optional[builtins.str] = None,
        password_history_size: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param clear_text_password: Store password with reversible encryption (0-2^16). The password will not be stored with reversible encryption if the value is set to 0. Reversible encryption will be used in any other case. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#clear_text_password GpoSecurity#clear_text_password}
        :param maximum_password_age: Number of days before password expires (-1-999). If set to -1, it means the password never expires. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#maximum_password_age GpoSecurity#maximum_password_age}
        :param minimum_password_age: Number of days a password must be used before changing it (0-999). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#minimum_password_age GpoSecurity#minimum_password_age}
        :param minimum_password_length: Minimum number of characters used in a password (0-2^16). If set to 0, it means no password is required. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#minimum_password_length GpoSecurity#minimum_password_length}
        :param password_complexity: Password must meet complexity requirements (0-2^16). If set to 0, then requirements do not apply, any other value means requirements are applied Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#password_complexity GpoSecurity#password_complexity}
        :param password_history_size: The number of unique new passwords that are required before an old password can be reused in association with a user account (0-2^16). A value of 0 indicates that the password history is disabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#password_history_size GpoSecurity#password_history_size}
        '''
        value = GpoSecurityPasswordPolicies(
            clear_text_password=clear_text_password,
            maximum_password_age=maximum_password_age,
            minimum_password_age=minimum_password_age,
            minimum_password_length=minimum_password_length,
            password_complexity=password_complexity,
            password_history_size=password_history_size,
        )

        return typing.cast(None, jsii.invoke(self, "putPasswordPolicies", [value]))

    @jsii.member(jsii_name="putRegistryKeys")
    def put_registry_keys(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GpoSecurityRegistryKeys", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5f9d5edf01079abe58071bc93847a52f6e2c734042f0e841f5ff9ddcefb4bab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRegistryKeys", [value]))

    @jsii.member(jsii_name="putRegistryValues")
    def put_registry_values(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GpoSecurityRegistryValues", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6e1f717f7af974b9c9bea2b82c3510507583504a0b1a6e5514f1565a6134603)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRegistryValues", [value]))

    @jsii.member(jsii_name="putRestrictedGroups")
    def put_restricted_groups(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GpoSecurityRestrictedGroups", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__534ae54df2a3d3efcae6aa677e8ce1adbc2f0032eb9cebf38d22412c8d24cb4c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRestrictedGroups", [value]))

    @jsii.member(jsii_name="putSystemLog")
    def put_system_log(
        self,
        *,
        audit_log_retention_period: typing.Optional[builtins.str] = None,
        maximum_log_size: typing.Optional[builtins.str] = None,
        restrict_guest_access: typing.Optional[builtins.str] = None,
        retention_days: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param audit_log_retention_period: Control log retention. Values: 0: overwrite events as needed, 1: overwrite events as specified specified by ``retention_days``, 2: never overwrite events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#audit_log_retention_period GpoSecurity#audit_log_retention_period}
        :param maximum_log_size: Maximum size of log in KiloBytes. (64-4194240). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#maximum_log_size GpoSecurity#maximum_log_size}
        :param restrict_guest_access: Restrict access to logs for guest users. A non-zero value restricts access to guest users. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#restrict_guest_access GpoSecurity#restrict_guest_access}
        :param retention_days: Number of days before new events overwrite old events. (1-365). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#retention_days GpoSecurity#retention_days}
        '''
        value = GpoSecuritySystemLog(
            audit_log_retention_period=audit_log_retention_period,
            maximum_log_size=maximum_log_size,
            restrict_guest_access=restrict_guest_access,
            retention_days=retention_days,
        )

        return typing.cast(None, jsii.invoke(self, "putSystemLog", [value]))

    @jsii.member(jsii_name="putSystemServices")
    def put_system_services(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GpoSecuritySystemServices", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d66305e3fd97727c8064171ea3ef2be46739d5c37d1813863fe702bac3bb850)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSystemServices", [value]))

    @jsii.member(jsii_name="resetAccountLockout")
    def reset_account_lockout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountLockout", []))

    @jsii.member(jsii_name="resetApplicationLog")
    def reset_application_log(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApplicationLog", []))

    @jsii.member(jsii_name="resetAuditLog")
    def reset_audit_log(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuditLog", []))

    @jsii.member(jsii_name="resetEventAudit")
    def reset_event_audit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEventAudit", []))

    @jsii.member(jsii_name="resetFilesystem")
    def reset_filesystem(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilesystem", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetKerberosPolicy")
    def reset_kerberos_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKerberosPolicy", []))

    @jsii.member(jsii_name="resetPasswordPolicies")
    def reset_password_policies(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPasswordPolicies", []))

    @jsii.member(jsii_name="resetRegistryKeys")
    def reset_registry_keys(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegistryKeys", []))

    @jsii.member(jsii_name="resetRegistryValues")
    def reset_registry_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegistryValues", []))

    @jsii.member(jsii_name="resetRestrictedGroups")
    def reset_restricted_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRestrictedGroups", []))

    @jsii.member(jsii_name="resetSystemLog")
    def reset_system_log(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSystemLog", []))

    @jsii.member(jsii_name="resetSystemServices")
    def reset_system_services(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSystemServices", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="accountLockout")
    def account_lockout(self) -> "GpoSecurityAccountLockoutOutputReference":
        return typing.cast("GpoSecurityAccountLockoutOutputReference", jsii.get(self, "accountLockout"))

    @builtins.property
    @jsii.member(jsii_name="applicationLog")
    def application_log(self) -> "GpoSecurityApplicationLogOutputReference":
        return typing.cast("GpoSecurityApplicationLogOutputReference", jsii.get(self, "applicationLog"))

    @builtins.property
    @jsii.member(jsii_name="auditLog")
    def audit_log(self) -> "GpoSecurityAuditLogOutputReference":
        return typing.cast("GpoSecurityAuditLogOutputReference", jsii.get(self, "auditLog"))

    @builtins.property
    @jsii.member(jsii_name="eventAudit")
    def event_audit(self) -> "GpoSecurityEventAuditOutputReference":
        return typing.cast("GpoSecurityEventAuditOutputReference", jsii.get(self, "eventAudit"))

    @builtins.property
    @jsii.member(jsii_name="filesystem")
    def filesystem(self) -> "GpoSecurityFilesystemList":
        return typing.cast("GpoSecurityFilesystemList", jsii.get(self, "filesystem"))

    @builtins.property
    @jsii.member(jsii_name="kerberosPolicy")
    def kerberos_policy(self) -> "GpoSecurityKerberosPolicyOutputReference":
        return typing.cast("GpoSecurityKerberosPolicyOutputReference", jsii.get(self, "kerberosPolicy"))

    @builtins.property
    @jsii.member(jsii_name="passwordPolicies")
    def password_policies(self) -> "GpoSecurityPasswordPoliciesOutputReference":
        return typing.cast("GpoSecurityPasswordPoliciesOutputReference", jsii.get(self, "passwordPolicies"))

    @builtins.property
    @jsii.member(jsii_name="registryKeys")
    def registry_keys(self) -> "GpoSecurityRegistryKeysList":
        return typing.cast("GpoSecurityRegistryKeysList", jsii.get(self, "registryKeys"))

    @builtins.property
    @jsii.member(jsii_name="registryValues")
    def registry_values(self) -> "GpoSecurityRegistryValuesList":
        return typing.cast("GpoSecurityRegistryValuesList", jsii.get(self, "registryValues"))

    @builtins.property
    @jsii.member(jsii_name="restrictedGroups")
    def restricted_groups(self) -> "GpoSecurityRestrictedGroupsList":
        return typing.cast("GpoSecurityRestrictedGroupsList", jsii.get(self, "restrictedGroups"))

    @builtins.property
    @jsii.member(jsii_name="systemLog")
    def system_log(self) -> "GpoSecuritySystemLogOutputReference":
        return typing.cast("GpoSecuritySystemLogOutputReference", jsii.get(self, "systemLog"))

    @builtins.property
    @jsii.member(jsii_name="systemServices")
    def system_services(self) -> "GpoSecuritySystemServicesList":
        return typing.cast("GpoSecuritySystemServicesList", jsii.get(self, "systemServices"))

    @builtins.property
    @jsii.member(jsii_name="accountLockoutInput")
    def account_lockout_input(self) -> typing.Optional["GpoSecurityAccountLockout"]:
        return typing.cast(typing.Optional["GpoSecurityAccountLockout"], jsii.get(self, "accountLockoutInput"))

    @builtins.property
    @jsii.member(jsii_name="applicationLogInput")
    def application_log_input(self) -> typing.Optional["GpoSecurityApplicationLog"]:
        return typing.cast(typing.Optional["GpoSecurityApplicationLog"], jsii.get(self, "applicationLogInput"))

    @builtins.property
    @jsii.member(jsii_name="auditLogInput")
    def audit_log_input(self) -> typing.Optional["GpoSecurityAuditLog"]:
        return typing.cast(typing.Optional["GpoSecurityAuditLog"], jsii.get(self, "auditLogInput"))

    @builtins.property
    @jsii.member(jsii_name="eventAuditInput")
    def event_audit_input(self) -> typing.Optional["GpoSecurityEventAudit"]:
        return typing.cast(typing.Optional["GpoSecurityEventAudit"], jsii.get(self, "eventAuditInput"))

    @builtins.property
    @jsii.member(jsii_name="filesystemInput")
    def filesystem_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GpoSecurityFilesystem"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GpoSecurityFilesystem"]]], jsii.get(self, "filesystemInput"))

    @builtins.property
    @jsii.member(jsii_name="gpoContainerInput")
    def gpo_container_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gpoContainerInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="kerberosPolicyInput")
    def kerberos_policy_input(self) -> typing.Optional["GpoSecurityKerberosPolicy"]:
        return typing.cast(typing.Optional["GpoSecurityKerberosPolicy"], jsii.get(self, "kerberosPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordPoliciesInput")
    def password_policies_input(self) -> typing.Optional["GpoSecurityPasswordPolicies"]:
        return typing.cast(typing.Optional["GpoSecurityPasswordPolicies"], jsii.get(self, "passwordPoliciesInput"))

    @builtins.property
    @jsii.member(jsii_name="registryKeysInput")
    def registry_keys_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GpoSecurityRegistryKeys"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GpoSecurityRegistryKeys"]]], jsii.get(self, "registryKeysInput"))

    @builtins.property
    @jsii.member(jsii_name="registryValuesInput")
    def registry_values_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GpoSecurityRegistryValues"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GpoSecurityRegistryValues"]]], jsii.get(self, "registryValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="restrictedGroupsInput")
    def restricted_groups_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GpoSecurityRestrictedGroups"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GpoSecurityRestrictedGroups"]]], jsii.get(self, "restrictedGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="systemLogInput")
    def system_log_input(self) -> typing.Optional["GpoSecuritySystemLog"]:
        return typing.cast(typing.Optional["GpoSecuritySystemLog"], jsii.get(self, "systemLogInput"))

    @builtins.property
    @jsii.member(jsii_name="systemServicesInput")
    def system_services_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GpoSecuritySystemServices"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GpoSecuritySystemServices"]]], jsii.get(self, "systemServicesInput"))

    @builtins.property
    @jsii.member(jsii_name="gpoContainer")
    def gpo_container(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gpoContainer"))

    @gpo_container.setter
    def gpo_container(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2281cd61760e5c2da2a86a226aa36540c0358fb361e387ad61ba4210ac651fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gpoContainer", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1fc44d8f755fd069e480a4574cf496e6cd9c42d3f294583862277c8b8587eff7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-ad.gpoSecurity.GpoSecurityAccountLockout",
    jsii_struct_bases=[],
    name_mapping={
        "force_logoff_when_hour_expire": "forceLogoffWhenHourExpire",
        "lockout_bad_count": "lockoutBadCount",
        "lockout_duration": "lockoutDuration",
        "reset_lockout_count": "resetLockoutCount",
    },
)
class GpoSecurityAccountLockout:
    def __init__(
        self,
        *,
        force_logoff_when_hour_expire: typing.Optional[builtins.str] = None,
        lockout_bad_count: typing.Optional[builtins.str] = None,
        lockout_duration: typing.Optional[builtins.str] = None,
        reset_lockout_count: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param force_logoff_when_hour_expire: Disconnect SMB sessions when logon hours expire. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#force_logoff_when_hour_expire GpoSecurity#force_logoff_when_hour_expire}
        :param lockout_bad_count: Number of failed logon attempts until a account is locked. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#lockout_bad_count GpoSecurity#lockout_bad_count}
        :param lockout_duration: Number of minutes a locked out account must remain locked out. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#lockout_duration GpoSecurity#lockout_duration}
        :param reset_lockout_count: Number of minutes a account will remain locked after a failed logon attempt. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#reset_lockout_count GpoSecurity#reset_lockout_count}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cacf0f22d18e2b8532d32516e2fd1a537c0c00aaee04dca03763d69b225ff8c1)
            check_type(argname="argument force_logoff_when_hour_expire", value=force_logoff_when_hour_expire, expected_type=type_hints["force_logoff_when_hour_expire"])
            check_type(argname="argument lockout_bad_count", value=lockout_bad_count, expected_type=type_hints["lockout_bad_count"])
            check_type(argname="argument lockout_duration", value=lockout_duration, expected_type=type_hints["lockout_duration"])
            check_type(argname="argument reset_lockout_count", value=reset_lockout_count, expected_type=type_hints["reset_lockout_count"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if force_logoff_when_hour_expire is not None:
            self._values["force_logoff_when_hour_expire"] = force_logoff_when_hour_expire
        if lockout_bad_count is not None:
            self._values["lockout_bad_count"] = lockout_bad_count
        if lockout_duration is not None:
            self._values["lockout_duration"] = lockout_duration
        if reset_lockout_count is not None:
            self._values["reset_lockout_count"] = reset_lockout_count

    @builtins.property
    def force_logoff_when_hour_expire(self) -> typing.Optional[builtins.str]:
        '''Disconnect SMB sessions when logon hours expire.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#force_logoff_when_hour_expire GpoSecurity#force_logoff_when_hour_expire}
        '''
        result = self._values.get("force_logoff_when_hour_expire")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lockout_bad_count(self) -> typing.Optional[builtins.str]:
        '''Number of failed logon attempts until a account is locked.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#lockout_bad_count GpoSecurity#lockout_bad_count}
        '''
        result = self._values.get("lockout_bad_count")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lockout_duration(self) -> typing.Optional[builtins.str]:
        '''Number of minutes a locked out account must remain locked out.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#lockout_duration GpoSecurity#lockout_duration}
        '''
        result = self._values.get("lockout_duration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def reset_lockout_count(self) -> typing.Optional[builtins.str]:
        '''Number of minutes a account will remain locked after a failed logon attempt.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#reset_lockout_count GpoSecurity#reset_lockout_count}
        '''
        result = self._values.get("reset_lockout_count")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GpoSecurityAccountLockout(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GpoSecurityAccountLockoutOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-ad.gpoSecurity.GpoSecurityAccountLockoutOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__00fcbffdf6aa8425791393df721ea48b413906ee62c43eaca7430ea046441e98)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetForceLogoffWhenHourExpire")
    def reset_force_logoff_when_hour_expire(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForceLogoffWhenHourExpire", []))

    @jsii.member(jsii_name="resetLockoutBadCount")
    def reset_lockout_bad_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLockoutBadCount", []))

    @jsii.member(jsii_name="resetLockoutDuration")
    def reset_lockout_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLockoutDuration", []))

    @jsii.member(jsii_name="resetResetLockoutCount")
    def reset_reset_lockout_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResetLockoutCount", []))

    @builtins.property
    @jsii.member(jsii_name="forceLogoffWhenHourExpireInput")
    def force_logoff_when_hour_expire_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "forceLogoffWhenHourExpireInput"))

    @builtins.property
    @jsii.member(jsii_name="lockoutBadCountInput")
    def lockout_bad_count_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lockoutBadCountInput"))

    @builtins.property
    @jsii.member(jsii_name="lockoutDurationInput")
    def lockout_duration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lockoutDurationInput"))

    @builtins.property
    @jsii.member(jsii_name="resetLockoutCountInput")
    def reset_lockout_count_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resetLockoutCountInput"))

    @builtins.property
    @jsii.member(jsii_name="forceLogoffWhenHourExpire")
    def force_logoff_when_hour_expire(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "forceLogoffWhenHourExpire"))

    @force_logoff_when_hour_expire.setter
    def force_logoff_when_hour_expire(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__237edace8a3f23958a9d5b246ebc5132a7de1bea831693b3a0251e0048a22aaf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forceLogoffWhenHourExpire", value)

    @builtins.property
    @jsii.member(jsii_name="lockoutBadCount")
    def lockout_bad_count(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lockoutBadCount"))

    @lockout_bad_count.setter
    def lockout_bad_count(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bcc309013d4a30036c9126c89ee2f2601664af6e1e31c07305f53d03530aed1e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lockoutBadCount", value)

    @builtins.property
    @jsii.member(jsii_name="lockoutDuration")
    def lockout_duration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lockoutDuration"))

    @lockout_duration.setter
    def lockout_duration(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2d5cdc4e02b08537c8cf3e4cbc40e2011acef50327ac885b76dd34db74384a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lockoutDuration", value)

    @builtins.property
    @jsii.member(jsii_name="resetLockoutCount")
    def reset_lockout_count(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resetLockoutCount"))

    @reset_lockout_count.setter
    def reset_lockout_count(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6283fcb6510c72cf2a67ac32cb7567d34385205ab8ba9652350b430975b195d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resetLockoutCount", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GpoSecurityAccountLockout]:
        return typing.cast(typing.Optional[GpoSecurityAccountLockout], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[GpoSecurityAccountLockout]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3c12e763b02ec987d7b3cb3d79579848dbfb8b04da917b778109edc9d2e316f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-ad.gpoSecurity.GpoSecurityApplicationLog",
    jsii_struct_bases=[],
    name_mapping={
        "audit_log_retention_period": "auditLogRetentionPeriod",
        "maximum_log_size": "maximumLogSize",
        "restrict_guest_access": "restrictGuestAccess",
        "retention_days": "retentionDays",
    },
)
class GpoSecurityApplicationLog:
    def __init__(
        self,
        *,
        audit_log_retention_period: typing.Optional[builtins.str] = None,
        maximum_log_size: typing.Optional[builtins.str] = None,
        restrict_guest_access: typing.Optional[builtins.str] = None,
        retention_days: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param audit_log_retention_period: Control log retention. Values: 0: overwrite events as needed, 1: overwrite events as specified specified by ``retention_days``, 2: never overwrite events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#audit_log_retention_period GpoSecurity#audit_log_retention_period}
        :param maximum_log_size: Maximum size of log in KiloBytes. (64-4194240). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#maximum_log_size GpoSecurity#maximum_log_size}
        :param restrict_guest_access: Restrict access to logs for guest users. A non-zero value restricts access to guest users. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#restrict_guest_access GpoSecurity#restrict_guest_access}
        :param retention_days: Number of days before new events overwrite old events. (1-365). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#retention_days GpoSecurity#retention_days}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0d73debdd5e6d72575b43ce6044d3ea0513f21b83c4340353a0baa55419e7ca)
            check_type(argname="argument audit_log_retention_period", value=audit_log_retention_period, expected_type=type_hints["audit_log_retention_period"])
            check_type(argname="argument maximum_log_size", value=maximum_log_size, expected_type=type_hints["maximum_log_size"])
            check_type(argname="argument restrict_guest_access", value=restrict_guest_access, expected_type=type_hints["restrict_guest_access"])
            check_type(argname="argument retention_days", value=retention_days, expected_type=type_hints["retention_days"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if audit_log_retention_period is not None:
            self._values["audit_log_retention_period"] = audit_log_retention_period
        if maximum_log_size is not None:
            self._values["maximum_log_size"] = maximum_log_size
        if restrict_guest_access is not None:
            self._values["restrict_guest_access"] = restrict_guest_access
        if retention_days is not None:
            self._values["retention_days"] = retention_days

    @builtins.property
    def audit_log_retention_period(self) -> typing.Optional[builtins.str]:
        '''Control log retention.

        Values: 0: overwrite events as needed, 1: overwrite events as specified specified by ``retention_days``, 2: never overwrite events.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#audit_log_retention_period GpoSecurity#audit_log_retention_period}
        '''
        result = self._values.get("audit_log_retention_period")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def maximum_log_size(self) -> typing.Optional[builtins.str]:
        '''Maximum size of log in KiloBytes. (64-4194240).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#maximum_log_size GpoSecurity#maximum_log_size}
        '''
        result = self._values.get("maximum_log_size")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def restrict_guest_access(self) -> typing.Optional[builtins.str]:
        '''Restrict access to logs for guest users. A non-zero value restricts access to guest users.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#restrict_guest_access GpoSecurity#restrict_guest_access}
        '''
        result = self._values.get("restrict_guest_access")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def retention_days(self) -> typing.Optional[builtins.str]:
        '''Number of days before new events overwrite old events. (1-365).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#retention_days GpoSecurity#retention_days}
        '''
        result = self._values.get("retention_days")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GpoSecurityApplicationLog(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GpoSecurityApplicationLogOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-ad.gpoSecurity.GpoSecurityApplicationLogOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ac14ebd89771ca0aac99195f79c50cd73a2c1b9c4feacdb411d8c6f665a946a8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAuditLogRetentionPeriod")
    def reset_audit_log_retention_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuditLogRetentionPeriod", []))

    @jsii.member(jsii_name="resetMaximumLogSize")
    def reset_maximum_log_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaximumLogSize", []))

    @jsii.member(jsii_name="resetRestrictGuestAccess")
    def reset_restrict_guest_access(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRestrictGuestAccess", []))

    @jsii.member(jsii_name="resetRetentionDays")
    def reset_retention_days(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetentionDays", []))

    @builtins.property
    @jsii.member(jsii_name="auditLogRetentionPeriodInput")
    def audit_log_retention_period_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "auditLogRetentionPeriodInput"))

    @builtins.property
    @jsii.member(jsii_name="maximumLogSizeInput")
    def maximum_log_size_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maximumLogSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="restrictGuestAccessInput")
    def restrict_guest_access_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "restrictGuestAccessInput"))

    @builtins.property
    @jsii.member(jsii_name="retentionDaysInput")
    def retention_days_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "retentionDaysInput"))

    @builtins.property
    @jsii.member(jsii_name="auditLogRetentionPeriod")
    def audit_log_retention_period(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "auditLogRetentionPeriod"))

    @audit_log_retention_period.setter
    def audit_log_retention_period(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb6c5039bf9f921f8eb803e24b031cafe0ca4c43b9c8b88baaad697399f10571)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "auditLogRetentionPeriod", value)

    @builtins.property
    @jsii.member(jsii_name="maximumLogSize")
    def maximum_log_size(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maximumLogSize"))

    @maximum_log_size.setter
    def maximum_log_size(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56f629f8ae48e32d9476248637033fd3186a12824b6ce8e36a6c8e2df95fc28a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maximumLogSize", value)

    @builtins.property
    @jsii.member(jsii_name="restrictGuestAccess")
    def restrict_guest_access(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "restrictGuestAccess"))

    @restrict_guest_access.setter
    def restrict_guest_access(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f6c9613bb11364a7f9a816b34702ffd66f5f800a5072672dba9e3619f2260b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "restrictGuestAccess", value)

    @builtins.property
    @jsii.member(jsii_name="retentionDays")
    def retention_days(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "retentionDays"))

    @retention_days.setter
    def retention_days(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bfeac08926005551e9babc0e38f03f59d0c70995f8f552233deac5da821518a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retentionDays", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GpoSecurityApplicationLog]:
        return typing.cast(typing.Optional[GpoSecurityApplicationLog], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[GpoSecurityApplicationLog]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2ef25f346061db36ce8137c7913085d654c78d356f0eb5f547cf7a22b799e7b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-ad.gpoSecurity.GpoSecurityAuditLog",
    jsii_struct_bases=[],
    name_mapping={
        "audit_log_retention_period": "auditLogRetentionPeriod",
        "maximum_log_size": "maximumLogSize",
        "restrict_guest_access": "restrictGuestAccess",
        "retention_days": "retentionDays",
    },
)
class GpoSecurityAuditLog:
    def __init__(
        self,
        *,
        audit_log_retention_period: typing.Optional[builtins.str] = None,
        maximum_log_size: typing.Optional[builtins.str] = None,
        restrict_guest_access: typing.Optional[builtins.str] = None,
        retention_days: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param audit_log_retention_period: Control log retention. Values: 0: overwrite events as needed, 1: overwrite events as specified specified by ``retention_days``, 2: never overwrite events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#audit_log_retention_period GpoSecurity#audit_log_retention_period}
        :param maximum_log_size: Maximum size of log in KiloBytes. (64-4194240). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#maximum_log_size GpoSecurity#maximum_log_size}
        :param restrict_guest_access: Restrict access to logs for guest users. A non-zero value restricts access to guest users. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#restrict_guest_access GpoSecurity#restrict_guest_access}
        :param retention_days: Number of days before new events overwrite old events. (1-365). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#retention_days GpoSecurity#retention_days}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85435532b75fbdc4dc1b2e8e371b20c3191694415025fee1e3e76c4cae5b9108)
            check_type(argname="argument audit_log_retention_period", value=audit_log_retention_period, expected_type=type_hints["audit_log_retention_period"])
            check_type(argname="argument maximum_log_size", value=maximum_log_size, expected_type=type_hints["maximum_log_size"])
            check_type(argname="argument restrict_guest_access", value=restrict_guest_access, expected_type=type_hints["restrict_guest_access"])
            check_type(argname="argument retention_days", value=retention_days, expected_type=type_hints["retention_days"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if audit_log_retention_period is not None:
            self._values["audit_log_retention_period"] = audit_log_retention_period
        if maximum_log_size is not None:
            self._values["maximum_log_size"] = maximum_log_size
        if restrict_guest_access is not None:
            self._values["restrict_guest_access"] = restrict_guest_access
        if retention_days is not None:
            self._values["retention_days"] = retention_days

    @builtins.property
    def audit_log_retention_period(self) -> typing.Optional[builtins.str]:
        '''Control log retention.

        Values: 0: overwrite events as needed, 1: overwrite events as specified specified by ``retention_days``, 2: never overwrite events.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#audit_log_retention_period GpoSecurity#audit_log_retention_period}
        '''
        result = self._values.get("audit_log_retention_period")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def maximum_log_size(self) -> typing.Optional[builtins.str]:
        '''Maximum size of log in KiloBytes. (64-4194240).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#maximum_log_size GpoSecurity#maximum_log_size}
        '''
        result = self._values.get("maximum_log_size")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def restrict_guest_access(self) -> typing.Optional[builtins.str]:
        '''Restrict access to logs for guest users. A non-zero value restricts access to guest users.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#restrict_guest_access GpoSecurity#restrict_guest_access}
        '''
        result = self._values.get("restrict_guest_access")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def retention_days(self) -> typing.Optional[builtins.str]:
        '''Number of days before new events overwrite old events. (1-365).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#retention_days GpoSecurity#retention_days}
        '''
        result = self._values.get("retention_days")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GpoSecurityAuditLog(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GpoSecurityAuditLogOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-ad.gpoSecurity.GpoSecurityAuditLogOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1a8f18e557ceb6f1ce26ec997861249fd892e3181328be3714732b1614eac5e3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAuditLogRetentionPeriod")
    def reset_audit_log_retention_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuditLogRetentionPeriod", []))

    @jsii.member(jsii_name="resetMaximumLogSize")
    def reset_maximum_log_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaximumLogSize", []))

    @jsii.member(jsii_name="resetRestrictGuestAccess")
    def reset_restrict_guest_access(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRestrictGuestAccess", []))

    @jsii.member(jsii_name="resetRetentionDays")
    def reset_retention_days(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetentionDays", []))

    @builtins.property
    @jsii.member(jsii_name="auditLogRetentionPeriodInput")
    def audit_log_retention_period_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "auditLogRetentionPeriodInput"))

    @builtins.property
    @jsii.member(jsii_name="maximumLogSizeInput")
    def maximum_log_size_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maximumLogSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="restrictGuestAccessInput")
    def restrict_guest_access_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "restrictGuestAccessInput"))

    @builtins.property
    @jsii.member(jsii_name="retentionDaysInput")
    def retention_days_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "retentionDaysInput"))

    @builtins.property
    @jsii.member(jsii_name="auditLogRetentionPeriod")
    def audit_log_retention_period(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "auditLogRetentionPeriod"))

    @audit_log_retention_period.setter
    def audit_log_retention_period(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4200b7b700fac011f82d0a1371b640c43a6d437575b33aef41957d90ba333ab0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "auditLogRetentionPeriod", value)

    @builtins.property
    @jsii.member(jsii_name="maximumLogSize")
    def maximum_log_size(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maximumLogSize"))

    @maximum_log_size.setter
    def maximum_log_size(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9439c34a383f5f0ca371a5d6762c478d03afe4b42a76e3edcebf7b82e0f505d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maximumLogSize", value)

    @builtins.property
    @jsii.member(jsii_name="restrictGuestAccess")
    def restrict_guest_access(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "restrictGuestAccess"))

    @restrict_guest_access.setter
    def restrict_guest_access(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4b8ea273308141124153bba9cb02983d952967f5d2b7332061ca7776a3655c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "restrictGuestAccess", value)

    @builtins.property
    @jsii.member(jsii_name="retentionDays")
    def retention_days(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "retentionDays"))

    @retention_days.setter
    def retention_days(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f31648752ad56bfc1cee76deba694e6c63f43942d46183a13607f4b693d37f13)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retentionDays", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GpoSecurityAuditLog]:
        return typing.cast(typing.Optional[GpoSecurityAuditLog], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[GpoSecurityAuditLog]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c76bafe3233af81a3096329685077641e7853dbe87ec8c52a65ff2f3b77d9d58)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-ad.gpoSecurity.GpoSecurityConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "gpo_container": "gpoContainer",
        "account_lockout": "accountLockout",
        "application_log": "applicationLog",
        "audit_log": "auditLog",
        "event_audit": "eventAudit",
        "filesystem": "filesystem",
        "id": "id",
        "kerberos_policy": "kerberosPolicy",
        "password_policies": "passwordPolicies",
        "registry_keys": "registryKeys",
        "registry_values": "registryValues",
        "restricted_groups": "restrictedGroups",
        "system_log": "systemLog",
        "system_services": "systemServices",
    },
)
class GpoSecurityConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        gpo_container: builtins.str,
        account_lockout: typing.Optional[typing.Union[GpoSecurityAccountLockout, typing.Dict[builtins.str, typing.Any]]] = None,
        application_log: typing.Optional[typing.Union[GpoSecurityApplicationLog, typing.Dict[builtins.str, typing.Any]]] = None,
        audit_log: typing.Optional[typing.Union[GpoSecurityAuditLog, typing.Dict[builtins.str, typing.Any]]] = None,
        event_audit: typing.Optional[typing.Union["GpoSecurityEventAudit", typing.Dict[builtins.str, typing.Any]]] = None,
        filesystem: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GpoSecurityFilesystem", typing.Dict[builtins.str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        kerberos_policy: typing.Optional[typing.Union["GpoSecurityKerberosPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        password_policies: typing.Optional[typing.Union["GpoSecurityPasswordPolicies", typing.Dict[builtins.str, typing.Any]]] = None,
        registry_keys: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GpoSecurityRegistryKeys", typing.Dict[builtins.str, typing.Any]]]]] = None,
        registry_values: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GpoSecurityRegistryValues", typing.Dict[builtins.str, typing.Any]]]]] = None,
        restricted_groups: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GpoSecurityRestrictedGroups", typing.Dict[builtins.str, typing.Any]]]]] = None,
        system_log: typing.Optional[typing.Union["GpoSecuritySystemLog", typing.Dict[builtins.str, typing.Any]]] = None,
        system_services: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GpoSecuritySystemServices", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param gpo_container: The GUID of the container the security settings belong to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#gpo_container GpoSecurity#gpo_container}
        :param account_lockout: account_lockout block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#account_lockout GpoSecurity#account_lockout}
        :param application_log: application_log block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#application_log GpoSecurity#application_log}
        :param audit_log: audit_log block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#audit_log GpoSecurity#audit_log}
        :param event_audit: event_audit block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#event_audit GpoSecurity#event_audit}
        :param filesystem: filesystem block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#filesystem GpoSecurity#filesystem}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#id GpoSecurity#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kerberos_policy: kerberos_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#kerberos_policy GpoSecurity#kerberos_policy}
        :param password_policies: password_policies block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#password_policies GpoSecurity#password_policies}
        :param registry_keys: registry_keys block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#registry_keys GpoSecurity#registry_keys}
        :param registry_values: registry_values block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#registry_values GpoSecurity#registry_values}
        :param restricted_groups: restricted_groups block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#restricted_groups GpoSecurity#restricted_groups}
        :param system_log: system_log block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#system_log GpoSecurity#system_log}
        :param system_services: system_services block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#system_services GpoSecurity#system_services}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(account_lockout, dict):
            account_lockout = GpoSecurityAccountLockout(**account_lockout)
        if isinstance(application_log, dict):
            application_log = GpoSecurityApplicationLog(**application_log)
        if isinstance(audit_log, dict):
            audit_log = GpoSecurityAuditLog(**audit_log)
        if isinstance(event_audit, dict):
            event_audit = GpoSecurityEventAudit(**event_audit)
        if isinstance(kerberos_policy, dict):
            kerberos_policy = GpoSecurityKerberosPolicy(**kerberos_policy)
        if isinstance(password_policies, dict):
            password_policies = GpoSecurityPasswordPolicies(**password_policies)
        if isinstance(system_log, dict):
            system_log = GpoSecuritySystemLog(**system_log)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__813fbf075deae0a8dfc08469b9da1745f51d18e18bfeb83aa92f4d8ad9e55094)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument gpo_container", value=gpo_container, expected_type=type_hints["gpo_container"])
            check_type(argname="argument account_lockout", value=account_lockout, expected_type=type_hints["account_lockout"])
            check_type(argname="argument application_log", value=application_log, expected_type=type_hints["application_log"])
            check_type(argname="argument audit_log", value=audit_log, expected_type=type_hints["audit_log"])
            check_type(argname="argument event_audit", value=event_audit, expected_type=type_hints["event_audit"])
            check_type(argname="argument filesystem", value=filesystem, expected_type=type_hints["filesystem"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument kerberos_policy", value=kerberos_policy, expected_type=type_hints["kerberos_policy"])
            check_type(argname="argument password_policies", value=password_policies, expected_type=type_hints["password_policies"])
            check_type(argname="argument registry_keys", value=registry_keys, expected_type=type_hints["registry_keys"])
            check_type(argname="argument registry_values", value=registry_values, expected_type=type_hints["registry_values"])
            check_type(argname="argument restricted_groups", value=restricted_groups, expected_type=type_hints["restricted_groups"])
            check_type(argname="argument system_log", value=system_log, expected_type=type_hints["system_log"])
            check_type(argname="argument system_services", value=system_services, expected_type=type_hints["system_services"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "gpo_container": gpo_container,
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
        if account_lockout is not None:
            self._values["account_lockout"] = account_lockout
        if application_log is not None:
            self._values["application_log"] = application_log
        if audit_log is not None:
            self._values["audit_log"] = audit_log
        if event_audit is not None:
            self._values["event_audit"] = event_audit
        if filesystem is not None:
            self._values["filesystem"] = filesystem
        if id is not None:
            self._values["id"] = id
        if kerberos_policy is not None:
            self._values["kerberos_policy"] = kerberos_policy
        if password_policies is not None:
            self._values["password_policies"] = password_policies
        if registry_keys is not None:
            self._values["registry_keys"] = registry_keys
        if registry_values is not None:
            self._values["registry_values"] = registry_values
        if restricted_groups is not None:
            self._values["restricted_groups"] = restricted_groups
        if system_log is not None:
            self._values["system_log"] = system_log
        if system_services is not None:
            self._values["system_services"] = system_services

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
    def gpo_container(self) -> builtins.str:
        '''The GUID of the container the security settings belong to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#gpo_container GpoSecurity#gpo_container}
        '''
        result = self._values.get("gpo_container")
        assert result is not None, "Required property 'gpo_container' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def account_lockout(self) -> typing.Optional[GpoSecurityAccountLockout]:
        '''account_lockout block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#account_lockout GpoSecurity#account_lockout}
        '''
        result = self._values.get("account_lockout")
        return typing.cast(typing.Optional[GpoSecurityAccountLockout], result)

    @builtins.property
    def application_log(self) -> typing.Optional[GpoSecurityApplicationLog]:
        '''application_log block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#application_log GpoSecurity#application_log}
        '''
        result = self._values.get("application_log")
        return typing.cast(typing.Optional[GpoSecurityApplicationLog], result)

    @builtins.property
    def audit_log(self) -> typing.Optional[GpoSecurityAuditLog]:
        '''audit_log block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#audit_log GpoSecurity#audit_log}
        '''
        result = self._values.get("audit_log")
        return typing.cast(typing.Optional[GpoSecurityAuditLog], result)

    @builtins.property
    def event_audit(self) -> typing.Optional["GpoSecurityEventAudit"]:
        '''event_audit block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#event_audit GpoSecurity#event_audit}
        '''
        result = self._values.get("event_audit")
        return typing.cast(typing.Optional["GpoSecurityEventAudit"], result)

    @builtins.property
    def filesystem(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GpoSecurityFilesystem"]]]:
        '''filesystem block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#filesystem GpoSecurity#filesystem}
        '''
        result = self._values.get("filesystem")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GpoSecurityFilesystem"]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#id GpoSecurity#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kerberos_policy(self) -> typing.Optional["GpoSecurityKerberosPolicy"]:
        '''kerberos_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#kerberos_policy GpoSecurity#kerberos_policy}
        '''
        result = self._values.get("kerberos_policy")
        return typing.cast(typing.Optional["GpoSecurityKerberosPolicy"], result)

    @builtins.property
    def password_policies(self) -> typing.Optional["GpoSecurityPasswordPolicies"]:
        '''password_policies block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#password_policies GpoSecurity#password_policies}
        '''
        result = self._values.get("password_policies")
        return typing.cast(typing.Optional["GpoSecurityPasswordPolicies"], result)

    @builtins.property
    def registry_keys(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GpoSecurityRegistryKeys"]]]:
        '''registry_keys block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#registry_keys GpoSecurity#registry_keys}
        '''
        result = self._values.get("registry_keys")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GpoSecurityRegistryKeys"]]], result)

    @builtins.property
    def registry_values(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GpoSecurityRegistryValues"]]]:
        '''registry_values block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#registry_values GpoSecurity#registry_values}
        '''
        result = self._values.get("registry_values")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GpoSecurityRegistryValues"]]], result)

    @builtins.property
    def restricted_groups(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GpoSecurityRestrictedGroups"]]]:
        '''restricted_groups block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#restricted_groups GpoSecurity#restricted_groups}
        '''
        result = self._values.get("restricted_groups")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GpoSecurityRestrictedGroups"]]], result)

    @builtins.property
    def system_log(self) -> typing.Optional["GpoSecuritySystemLog"]:
        '''system_log block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#system_log GpoSecurity#system_log}
        '''
        result = self._values.get("system_log")
        return typing.cast(typing.Optional["GpoSecuritySystemLog"], result)

    @builtins.property
    def system_services(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GpoSecuritySystemServices"]]]:
        '''system_services block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#system_services GpoSecurity#system_services}
        '''
        result = self._values.get("system_services")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GpoSecuritySystemServices"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GpoSecurityConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-ad.gpoSecurity.GpoSecurityEventAudit",
    jsii_struct_bases=[],
    name_mapping={
        "audit_account_logon": "auditAccountLogon",
        "audit_account_manage": "auditAccountManage",
        "audit_ds_access": "auditDsAccess",
        "audit_logon_events": "auditLogonEvents",
        "audit_object_access": "auditObjectAccess",
        "audit_policy_change": "auditPolicyChange",
        "audit_privilege_use": "auditPrivilegeUse",
        "audit_process_tracking": "auditProcessTracking",
        "audit_system_events": "auditSystemEvents",
    },
)
class GpoSecurityEventAudit:
    def __init__(
        self,
        *,
        audit_account_logon: typing.Optional[builtins.str] = None,
        audit_account_manage: typing.Optional[builtins.str] = None,
        audit_ds_access: typing.Optional[builtins.str] = None,
        audit_logon_events: typing.Optional[builtins.str] = None,
        audit_object_access: typing.Optional[builtins.str] = None,
        audit_policy_change: typing.Optional[builtins.str] = None,
        audit_privilege_use: typing.Optional[builtins.str] = None,
        audit_process_tracking: typing.Optional[builtins.str] = None,
        audit_system_events: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param audit_account_logon: Audit credential validation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#audit_account_logon GpoSecurity#audit_account_logon}
        :param audit_account_manage: Audit account management events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#audit_account_manage GpoSecurity#audit_account_manage}
        :param audit_ds_access: Audit access attempts to AD objects. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#audit_ds_access GpoSecurity#audit_ds_access}
        :param audit_logon_events: Audit logon events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#audit_logon_events GpoSecurity#audit_logon_events}
        :param audit_object_access: Audit access attempts to non-AD objects. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#audit_object_access GpoSecurity#audit_object_access}
        :param audit_policy_change: Audit attempts to change a policy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#audit_policy_change GpoSecurity#audit_policy_change}
        :param audit_privilege_use: Audit user attempts of exercising user rights. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#audit_privilege_use GpoSecurity#audit_privilege_use}
        :param audit_process_tracking: Audit process related events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#audit_process_tracking GpoSecurity#audit_process_tracking}
        :param audit_system_events: Audit system events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#audit_system_events GpoSecurity#audit_system_events}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04f36083c93644f3b8249fda0271cc7369ecb371f6324297bdf28af4eb49ed93)
            check_type(argname="argument audit_account_logon", value=audit_account_logon, expected_type=type_hints["audit_account_logon"])
            check_type(argname="argument audit_account_manage", value=audit_account_manage, expected_type=type_hints["audit_account_manage"])
            check_type(argname="argument audit_ds_access", value=audit_ds_access, expected_type=type_hints["audit_ds_access"])
            check_type(argname="argument audit_logon_events", value=audit_logon_events, expected_type=type_hints["audit_logon_events"])
            check_type(argname="argument audit_object_access", value=audit_object_access, expected_type=type_hints["audit_object_access"])
            check_type(argname="argument audit_policy_change", value=audit_policy_change, expected_type=type_hints["audit_policy_change"])
            check_type(argname="argument audit_privilege_use", value=audit_privilege_use, expected_type=type_hints["audit_privilege_use"])
            check_type(argname="argument audit_process_tracking", value=audit_process_tracking, expected_type=type_hints["audit_process_tracking"])
            check_type(argname="argument audit_system_events", value=audit_system_events, expected_type=type_hints["audit_system_events"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if audit_account_logon is not None:
            self._values["audit_account_logon"] = audit_account_logon
        if audit_account_manage is not None:
            self._values["audit_account_manage"] = audit_account_manage
        if audit_ds_access is not None:
            self._values["audit_ds_access"] = audit_ds_access
        if audit_logon_events is not None:
            self._values["audit_logon_events"] = audit_logon_events
        if audit_object_access is not None:
            self._values["audit_object_access"] = audit_object_access
        if audit_policy_change is not None:
            self._values["audit_policy_change"] = audit_policy_change
        if audit_privilege_use is not None:
            self._values["audit_privilege_use"] = audit_privilege_use
        if audit_process_tracking is not None:
            self._values["audit_process_tracking"] = audit_process_tracking
        if audit_system_events is not None:
            self._values["audit_system_events"] = audit_system_events

    @builtins.property
    def audit_account_logon(self) -> typing.Optional[builtins.str]:
        '''Audit credential validation.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#audit_account_logon GpoSecurity#audit_account_logon}
        '''
        result = self._values.get("audit_account_logon")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def audit_account_manage(self) -> typing.Optional[builtins.str]:
        '''Audit account management events.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#audit_account_manage GpoSecurity#audit_account_manage}
        '''
        result = self._values.get("audit_account_manage")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def audit_ds_access(self) -> typing.Optional[builtins.str]:
        '''Audit access attempts to AD objects.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#audit_ds_access GpoSecurity#audit_ds_access}
        '''
        result = self._values.get("audit_ds_access")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def audit_logon_events(self) -> typing.Optional[builtins.str]:
        '''Audit logon events.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#audit_logon_events GpoSecurity#audit_logon_events}
        '''
        result = self._values.get("audit_logon_events")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def audit_object_access(self) -> typing.Optional[builtins.str]:
        '''Audit access attempts to non-AD objects.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#audit_object_access GpoSecurity#audit_object_access}
        '''
        result = self._values.get("audit_object_access")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def audit_policy_change(self) -> typing.Optional[builtins.str]:
        '''Audit attempts to change a policy.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#audit_policy_change GpoSecurity#audit_policy_change}
        '''
        result = self._values.get("audit_policy_change")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def audit_privilege_use(self) -> typing.Optional[builtins.str]:
        '''Audit user attempts of exercising user rights.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#audit_privilege_use GpoSecurity#audit_privilege_use}
        '''
        result = self._values.get("audit_privilege_use")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def audit_process_tracking(self) -> typing.Optional[builtins.str]:
        '''Audit process related events.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#audit_process_tracking GpoSecurity#audit_process_tracking}
        '''
        result = self._values.get("audit_process_tracking")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def audit_system_events(self) -> typing.Optional[builtins.str]:
        '''Audit system events.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#audit_system_events GpoSecurity#audit_system_events}
        '''
        result = self._values.get("audit_system_events")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GpoSecurityEventAudit(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GpoSecurityEventAuditOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-ad.gpoSecurity.GpoSecurityEventAuditOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d7aced749cdd9f0af83009aa8cd7daefde8cf57b3ae23c0023cf6ba818050c3c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAuditAccountLogon")
    def reset_audit_account_logon(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuditAccountLogon", []))

    @jsii.member(jsii_name="resetAuditAccountManage")
    def reset_audit_account_manage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuditAccountManage", []))

    @jsii.member(jsii_name="resetAuditDsAccess")
    def reset_audit_ds_access(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuditDsAccess", []))

    @jsii.member(jsii_name="resetAuditLogonEvents")
    def reset_audit_logon_events(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuditLogonEvents", []))

    @jsii.member(jsii_name="resetAuditObjectAccess")
    def reset_audit_object_access(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuditObjectAccess", []))

    @jsii.member(jsii_name="resetAuditPolicyChange")
    def reset_audit_policy_change(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuditPolicyChange", []))

    @jsii.member(jsii_name="resetAuditPrivilegeUse")
    def reset_audit_privilege_use(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuditPrivilegeUse", []))

    @jsii.member(jsii_name="resetAuditProcessTracking")
    def reset_audit_process_tracking(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuditProcessTracking", []))

    @jsii.member(jsii_name="resetAuditSystemEvents")
    def reset_audit_system_events(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuditSystemEvents", []))

    @builtins.property
    @jsii.member(jsii_name="auditAccountLogonInput")
    def audit_account_logon_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "auditAccountLogonInput"))

    @builtins.property
    @jsii.member(jsii_name="auditAccountManageInput")
    def audit_account_manage_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "auditAccountManageInput"))

    @builtins.property
    @jsii.member(jsii_name="auditDsAccessInput")
    def audit_ds_access_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "auditDsAccessInput"))

    @builtins.property
    @jsii.member(jsii_name="auditLogonEventsInput")
    def audit_logon_events_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "auditLogonEventsInput"))

    @builtins.property
    @jsii.member(jsii_name="auditObjectAccessInput")
    def audit_object_access_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "auditObjectAccessInput"))

    @builtins.property
    @jsii.member(jsii_name="auditPolicyChangeInput")
    def audit_policy_change_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "auditPolicyChangeInput"))

    @builtins.property
    @jsii.member(jsii_name="auditPrivilegeUseInput")
    def audit_privilege_use_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "auditPrivilegeUseInput"))

    @builtins.property
    @jsii.member(jsii_name="auditProcessTrackingInput")
    def audit_process_tracking_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "auditProcessTrackingInput"))

    @builtins.property
    @jsii.member(jsii_name="auditSystemEventsInput")
    def audit_system_events_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "auditSystemEventsInput"))

    @builtins.property
    @jsii.member(jsii_name="auditAccountLogon")
    def audit_account_logon(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "auditAccountLogon"))

    @audit_account_logon.setter
    def audit_account_logon(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72dc27d5eb10f2a1e98093f033958de03c6ca1d9b5181dc08dd55e5ee93b2cb2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "auditAccountLogon", value)

    @builtins.property
    @jsii.member(jsii_name="auditAccountManage")
    def audit_account_manage(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "auditAccountManage"))

    @audit_account_manage.setter
    def audit_account_manage(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab4fb512367fb02388379891951051a5aecb04273e97ad46d61125e712668758)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "auditAccountManage", value)

    @builtins.property
    @jsii.member(jsii_name="auditDsAccess")
    def audit_ds_access(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "auditDsAccess"))

    @audit_ds_access.setter
    def audit_ds_access(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44d1b67d546b251edaabd6d5cb3f263a11793e89714c232df983b93da3d70f69)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "auditDsAccess", value)

    @builtins.property
    @jsii.member(jsii_name="auditLogonEvents")
    def audit_logon_events(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "auditLogonEvents"))

    @audit_logon_events.setter
    def audit_logon_events(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38f7374ad9a96aa02f8fc27e00ed1c02d2536dfce2b83a75503e6a02a692d1b5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "auditLogonEvents", value)

    @builtins.property
    @jsii.member(jsii_name="auditObjectAccess")
    def audit_object_access(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "auditObjectAccess"))

    @audit_object_access.setter
    def audit_object_access(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb3b3a8a30449eca40ab5367378948333c3c9064720d88e863de1e64ab99a965)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "auditObjectAccess", value)

    @builtins.property
    @jsii.member(jsii_name="auditPolicyChange")
    def audit_policy_change(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "auditPolicyChange"))

    @audit_policy_change.setter
    def audit_policy_change(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51cc1a53da4374db98eaac5789dd654bb44c20acf052fea696ae3f024a42f012)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "auditPolicyChange", value)

    @builtins.property
    @jsii.member(jsii_name="auditPrivilegeUse")
    def audit_privilege_use(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "auditPrivilegeUse"))

    @audit_privilege_use.setter
    def audit_privilege_use(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__068eb046ab6b694b4a9fabe1fbdf45b1f13457eaf7cbeda35e5b3cd417847678)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "auditPrivilegeUse", value)

    @builtins.property
    @jsii.member(jsii_name="auditProcessTracking")
    def audit_process_tracking(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "auditProcessTracking"))

    @audit_process_tracking.setter
    def audit_process_tracking(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a00fdb2c84f00ea6ea46bceaa18264e129f30fb3bd193510709847d1d515fa03)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "auditProcessTracking", value)

    @builtins.property
    @jsii.member(jsii_name="auditSystemEvents")
    def audit_system_events(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "auditSystemEvents"))

    @audit_system_events.setter
    def audit_system_events(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d85c3c63cf0735082c964ab7bc517a67f6c2dde16a5432dc1e546500c64c487)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "auditSystemEvents", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GpoSecurityEventAudit]:
        return typing.cast(typing.Optional[GpoSecurityEventAudit], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[GpoSecurityEventAudit]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a0da96c093de149b615d2df34c10bd5e4a01dbfe7908f63c5074a21a2d8f957)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-ad.gpoSecurity.GpoSecurityFilesystem",
    jsii_struct_bases=[],
    name_mapping={"acl": "acl", "path": "path", "propagation_mode": "propagationMode"},
)
class GpoSecurityFilesystem:
    def __init__(
        self,
        *,
        acl: builtins.str,
        path: builtins.str,
        propagation_mode: builtins.str,
    ) -> None:
        '''
        :param acl: Security descriptor to apply. (https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-dtyp/f4296d69-1c0f-491f-9587-a960b292d070). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#acl GpoSecurity#acl}
        :param path: Path of the file or directory. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#path GpoSecurity#path}
        :param propagation_mode: Control permission propagation. 0: Propagate permissions to all subfolders and files, 1: Replace existing permissions on all subfolders and files, 2: Do not allow permissions to be replaced. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#propagation_mode GpoSecurity#propagation_mode}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1e47ad0df9ce1f0d0dca5122a3c2d58890a35639017d7ef682e0539a203733f)
            check_type(argname="argument acl", value=acl, expected_type=type_hints["acl"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument propagation_mode", value=propagation_mode, expected_type=type_hints["propagation_mode"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "acl": acl,
            "path": path,
            "propagation_mode": propagation_mode,
        }

    @builtins.property
    def acl(self) -> builtins.str:
        '''Security descriptor to apply. (https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-dtyp/f4296d69-1c0f-491f-9587-a960b292d070).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#acl GpoSecurity#acl}
        '''
        result = self._values.get("acl")
        assert result is not None, "Required property 'acl' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> builtins.str:
        '''Path of the file or directory.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#path GpoSecurity#path}
        '''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def propagation_mode(self) -> builtins.str:
        '''Control permission propagation.

        0: Propagate permissions to all subfolders and files, 1: Replace existing permissions on all subfolders and files, 2: Do not allow permissions to be replaced.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#propagation_mode GpoSecurity#propagation_mode}
        '''
        result = self._values.get("propagation_mode")
        assert result is not None, "Required property 'propagation_mode' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GpoSecurityFilesystem(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GpoSecurityFilesystemList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-ad.gpoSecurity.GpoSecurityFilesystemList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__58685115e48fa2d8f9c180523df2e90ee2743fcad970eef0b2d181c5864f8463)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "GpoSecurityFilesystemOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9c89d89a19132886d7c043fd6c5eece40ac642f35aca124e50042b51859bcf7)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GpoSecurityFilesystemOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a5fa93edd75fd44574e9a3b89ee9e0c412f971ec70770cac7dc642ea9dc7bb4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6dc1fd2681d7adb3769fd40a7472b86fc3f9adafb7cd50cba4d914dbed04e947)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9d550ab727be3a427a9dbb8906d9c533edee1acb2945a718daa0a0bf580dcab5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GpoSecurityFilesystem]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GpoSecurityFilesystem]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GpoSecurityFilesystem]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82f4766df6f19b922c0e09840c07b68c8b4af310c9ba834774f7727a35c86094)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GpoSecurityFilesystemOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-ad.gpoSecurity.GpoSecurityFilesystemOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ec11fd6cb4d6878c3c9508fee627188cc515ee30e97bca7b62fc675f21e09f35)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="aclInput")
    def acl_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aclInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="propagationModeInput")
    def propagation_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "propagationModeInput"))

    @builtins.property
    @jsii.member(jsii_name="acl")
    def acl(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "acl"))

    @acl.setter
    def acl(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8082f6f1ffa98954e4858d4cb4f26149053bcd801f288b4b0ea4ad8d4cd19dd8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "acl", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72034034ab63474ced193d307b64f5807c622f14386cacc3673485cfd53b2c90)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="propagationMode")
    def propagation_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "propagationMode"))

    @propagation_mode.setter
    def propagation_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__feb72591ba803d01834d0a0f85bf393488de88ebbc014b63d61a26daf3b50528)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "propagationMode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GpoSecurityFilesystem, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GpoSecurityFilesystem, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GpoSecurityFilesystem, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26f9e1640d50a64c6151582b2cae33a8ac491d90b00b01d6390e1b4dd3902172)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-ad.gpoSecurity.GpoSecurityKerberosPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "max_clock_skew": "maxClockSkew",
        "max_renew_age": "maxRenewAge",
        "max_service_age": "maxServiceAge",
        "max_ticket_age": "maxTicketAge",
        "ticket_validate_client": "ticketValidateClient",
    },
)
class GpoSecurityKerberosPolicy:
    def __init__(
        self,
        *,
        max_clock_skew: typing.Optional[builtins.str] = None,
        max_renew_age: typing.Optional[builtins.str] = None,
        max_service_age: typing.Optional[builtins.str] = None,
        max_ticket_age: typing.Optional[builtins.str] = None,
        ticket_validate_client: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param max_clock_skew: Maximum time difference, in minutes, between the client clock and the server clock. (0-99999). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#max_clock_skew GpoSecurity#max_clock_skew}
        :param max_renew_age: Number of days during which a ticket-granting ticket can be renewed (0-99999). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#max_renew_age GpoSecurity#max_renew_age}
        :param max_service_age: Maximum amount of minutes a ticket must be valid to access a service or resource. Minimum should be 10 and maximum should be equal to ``max_ticket_age``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#max_service_age GpoSecurity#max_service_age}
        :param max_ticket_age: Maximum amount of hours a ticket-granting ticket is valid (0-99999). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#max_ticket_age GpoSecurity#max_ticket_age}
        :param ticket_validate_client: Control if the session ticket is validated for every request. A non-zero value disables the policy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#ticket_validate_client GpoSecurity#ticket_validate_client}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02abc20895ee902d3e4eeb6d435b574318c54664742937967fdb55e9c67d803b)
            check_type(argname="argument max_clock_skew", value=max_clock_skew, expected_type=type_hints["max_clock_skew"])
            check_type(argname="argument max_renew_age", value=max_renew_age, expected_type=type_hints["max_renew_age"])
            check_type(argname="argument max_service_age", value=max_service_age, expected_type=type_hints["max_service_age"])
            check_type(argname="argument max_ticket_age", value=max_ticket_age, expected_type=type_hints["max_ticket_age"])
            check_type(argname="argument ticket_validate_client", value=ticket_validate_client, expected_type=type_hints["ticket_validate_client"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if max_clock_skew is not None:
            self._values["max_clock_skew"] = max_clock_skew
        if max_renew_age is not None:
            self._values["max_renew_age"] = max_renew_age
        if max_service_age is not None:
            self._values["max_service_age"] = max_service_age
        if max_ticket_age is not None:
            self._values["max_ticket_age"] = max_ticket_age
        if ticket_validate_client is not None:
            self._values["ticket_validate_client"] = ticket_validate_client

    @builtins.property
    def max_clock_skew(self) -> typing.Optional[builtins.str]:
        '''Maximum time difference, in minutes, between the client clock and the server clock. (0-99999).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#max_clock_skew GpoSecurity#max_clock_skew}
        '''
        result = self._values.get("max_clock_skew")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_renew_age(self) -> typing.Optional[builtins.str]:
        '''Number of days during which a ticket-granting ticket can be renewed (0-99999).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#max_renew_age GpoSecurity#max_renew_age}
        '''
        result = self._values.get("max_renew_age")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_service_age(self) -> typing.Optional[builtins.str]:
        '''Maximum amount of minutes a ticket must be valid to access a service or resource.

        Minimum should be 10 and maximum should be equal to ``max_ticket_age``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#max_service_age GpoSecurity#max_service_age}
        '''
        result = self._values.get("max_service_age")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_ticket_age(self) -> typing.Optional[builtins.str]:
        '''Maximum amount of hours a ticket-granting ticket is valid (0-99999).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#max_ticket_age GpoSecurity#max_ticket_age}
        '''
        result = self._values.get("max_ticket_age")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ticket_validate_client(self) -> typing.Optional[builtins.str]:
        '''Control if the session ticket is validated for every request. A non-zero value disables the policy.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#ticket_validate_client GpoSecurity#ticket_validate_client}
        '''
        result = self._values.get("ticket_validate_client")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GpoSecurityKerberosPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GpoSecurityKerberosPolicyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-ad.gpoSecurity.GpoSecurityKerberosPolicyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3f57613fda8f901a1d90c37fea97d32f00a7238029bfb3d26fd4738e1e759235)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMaxClockSkew")
    def reset_max_clock_skew(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxClockSkew", []))

    @jsii.member(jsii_name="resetMaxRenewAge")
    def reset_max_renew_age(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxRenewAge", []))

    @jsii.member(jsii_name="resetMaxServiceAge")
    def reset_max_service_age(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxServiceAge", []))

    @jsii.member(jsii_name="resetMaxTicketAge")
    def reset_max_ticket_age(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxTicketAge", []))

    @jsii.member(jsii_name="resetTicketValidateClient")
    def reset_ticket_validate_client(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTicketValidateClient", []))

    @builtins.property
    @jsii.member(jsii_name="maxClockSkewInput")
    def max_clock_skew_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxClockSkewInput"))

    @builtins.property
    @jsii.member(jsii_name="maxRenewAgeInput")
    def max_renew_age_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxRenewAgeInput"))

    @builtins.property
    @jsii.member(jsii_name="maxServiceAgeInput")
    def max_service_age_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxServiceAgeInput"))

    @builtins.property
    @jsii.member(jsii_name="maxTicketAgeInput")
    def max_ticket_age_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxTicketAgeInput"))

    @builtins.property
    @jsii.member(jsii_name="ticketValidateClientInput")
    def ticket_validate_client_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ticketValidateClientInput"))

    @builtins.property
    @jsii.member(jsii_name="maxClockSkew")
    def max_clock_skew(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxClockSkew"))

    @max_clock_skew.setter
    def max_clock_skew(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__070d1751c905b718abd561d24aa7fd9ef71594aca979ae389cd8eef45992acad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxClockSkew", value)

    @builtins.property
    @jsii.member(jsii_name="maxRenewAge")
    def max_renew_age(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxRenewAge"))

    @max_renew_age.setter
    def max_renew_age(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__475c396392478331dae4bbd7ef020fde2367ee07c6a9f24a793fb7df11edd4b2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxRenewAge", value)

    @builtins.property
    @jsii.member(jsii_name="maxServiceAge")
    def max_service_age(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxServiceAge"))

    @max_service_age.setter
    def max_service_age(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b52ad9a19a9e9e4189cb832f6dff9253595a96bd7cab6a27e0016a77291f6771)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxServiceAge", value)

    @builtins.property
    @jsii.member(jsii_name="maxTicketAge")
    def max_ticket_age(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxTicketAge"))

    @max_ticket_age.setter
    def max_ticket_age(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd57b5b5434a2f247aa5d8cb997a9fa28d669fc36f3ea5a3ef34d5e8b4b78059)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxTicketAge", value)

    @builtins.property
    @jsii.member(jsii_name="ticketValidateClient")
    def ticket_validate_client(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ticketValidateClient"))

    @ticket_validate_client.setter
    def ticket_validate_client(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0806aa8e6dadb307c62248cb51c893bd767eab2cfc04cb67d0488185149a1a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ticketValidateClient", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GpoSecurityKerberosPolicy]:
        return typing.cast(typing.Optional[GpoSecurityKerberosPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[GpoSecurityKerberosPolicy]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ac312c1d24b7480d6d5e6ef565387d401a59b600910b6ca8f9e68e5a7d1db84)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-ad.gpoSecurity.GpoSecurityPasswordPolicies",
    jsii_struct_bases=[],
    name_mapping={
        "clear_text_password": "clearTextPassword",
        "maximum_password_age": "maximumPasswordAge",
        "minimum_password_age": "minimumPasswordAge",
        "minimum_password_length": "minimumPasswordLength",
        "password_complexity": "passwordComplexity",
        "password_history_size": "passwordHistorySize",
    },
)
class GpoSecurityPasswordPolicies:
    def __init__(
        self,
        *,
        clear_text_password: typing.Optional[builtins.str] = None,
        maximum_password_age: typing.Optional[builtins.str] = None,
        minimum_password_age: typing.Optional[builtins.str] = None,
        minimum_password_length: typing.Optional[builtins.str] = None,
        password_complexity: typing.Optional[builtins.str] = None,
        password_history_size: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param clear_text_password: Store password with reversible encryption (0-2^16). The password will not be stored with reversible encryption if the value is set to 0. Reversible encryption will be used in any other case. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#clear_text_password GpoSecurity#clear_text_password}
        :param maximum_password_age: Number of days before password expires (-1-999). If set to -1, it means the password never expires. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#maximum_password_age GpoSecurity#maximum_password_age}
        :param minimum_password_age: Number of days a password must be used before changing it (0-999). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#minimum_password_age GpoSecurity#minimum_password_age}
        :param minimum_password_length: Minimum number of characters used in a password (0-2^16). If set to 0, it means no password is required. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#minimum_password_length GpoSecurity#minimum_password_length}
        :param password_complexity: Password must meet complexity requirements (0-2^16). If set to 0, then requirements do not apply, any other value means requirements are applied Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#password_complexity GpoSecurity#password_complexity}
        :param password_history_size: The number of unique new passwords that are required before an old password can be reused in association with a user account (0-2^16). A value of 0 indicates that the password history is disabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#password_history_size GpoSecurity#password_history_size}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e772677afd93a9ada091ed35eef2d3076c0e7452d28b59f4cadf651231179e0)
            check_type(argname="argument clear_text_password", value=clear_text_password, expected_type=type_hints["clear_text_password"])
            check_type(argname="argument maximum_password_age", value=maximum_password_age, expected_type=type_hints["maximum_password_age"])
            check_type(argname="argument minimum_password_age", value=minimum_password_age, expected_type=type_hints["minimum_password_age"])
            check_type(argname="argument minimum_password_length", value=minimum_password_length, expected_type=type_hints["minimum_password_length"])
            check_type(argname="argument password_complexity", value=password_complexity, expected_type=type_hints["password_complexity"])
            check_type(argname="argument password_history_size", value=password_history_size, expected_type=type_hints["password_history_size"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if clear_text_password is not None:
            self._values["clear_text_password"] = clear_text_password
        if maximum_password_age is not None:
            self._values["maximum_password_age"] = maximum_password_age
        if minimum_password_age is not None:
            self._values["minimum_password_age"] = minimum_password_age
        if minimum_password_length is not None:
            self._values["minimum_password_length"] = minimum_password_length
        if password_complexity is not None:
            self._values["password_complexity"] = password_complexity
        if password_history_size is not None:
            self._values["password_history_size"] = password_history_size

    @builtins.property
    def clear_text_password(self) -> typing.Optional[builtins.str]:
        '''Store password with reversible encryption (0-2^16).

        The password will not be stored with reversible encryption if the value is set to 0. Reversible encryption will be used in any other case.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#clear_text_password GpoSecurity#clear_text_password}
        '''
        result = self._values.get("clear_text_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def maximum_password_age(self) -> typing.Optional[builtins.str]:
        '''Number of days before password expires (-1-999). If set to -1, it means the password never expires.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#maximum_password_age GpoSecurity#maximum_password_age}
        '''
        result = self._values.get("maximum_password_age")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def minimum_password_age(self) -> typing.Optional[builtins.str]:
        '''Number of days a password must be used before changing it (0-999).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#minimum_password_age GpoSecurity#minimum_password_age}
        '''
        result = self._values.get("minimum_password_age")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def minimum_password_length(self) -> typing.Optional[builtins.str]:
        '''Minimum number of characters used in a password (0-2^16). If set to 0, it means no password is required.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#minimum_password_length GpoSecurity#minimum_password_length}
        '''
        result = self._values.get("minimum_password_length")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def password_complexity(self) -> typing.Optional[builtins.str]:
        '''Password must meet complexity requirements (0-2^16).

        If set to 0, then requirements do not apply, any other value means requirements are applied

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#password_complexity GpoSecurity#password_complexity}
        '''
        result = self._values.get("password_complexity")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def password_history_size(self) -> typing.Optional[builtins.str]:
        '''The number of unique new passwords that are required before an old password can be reused in association with a user account (0-2^16).

        A value of 0 indicates that the password history is disabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#password_history_size GpoSecurity#password_history_size}
        '''
        result = self._values.get("password_history_size")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GpoSecurityPasswordPolicies(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GpoSecurityPasswordPoliciesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-ad.gpoSecurity.GpoSecurityPasswordPoliciesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__48fe57bb1529711996c86f5e89a70427c7bc6363b3496828324724c869053e5e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetClearTextPassword")
    def reset_clear_text_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClearTextPassword", []))

    @jsii.member(jsii_name="resetMaximumPasswordAge")
    def reset_maximum_password_age(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaximumPasswordAge", []))

    @jsii.member(jsii_name="resetMinimumPasswordAge")
    def reset_minimum_password_age(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinimumPasswordAge", []))

    @jsii.member(jsii_name="resetMinimumPasswordLength")
    def reset_minimum_password_length(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinimumPasswordLength", []))

    @jsii.member(jsii_name="resetPasswordComplexity")
    def reset_password_complexity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPasswordComplexity", []))

    @jsii.member(jsii_name="resetPasswordHistorySize")
    def reset_password_history_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPasswordHistorySize", []))

    @builtins.property
    @jsii.member(jsii_name="clearTextPasswordInput")
    def clear_text_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clearTextPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="maximumPasswordAgeInput")
    def maximum_password_age_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maximumPasswordAgeInput"))

    @builtins.property
    @jsii.member(jsii_name="minimumPasswordAgeInput")
    def minimum_password_age_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "minimumPasswordAgeInput"))

    @builtins.property
    @jsii.member(jsii_name="minimumPasswordLengthInput")
    def minimum_password_length_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "minimumPasswordLengthInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordComplexityInput")
    def password_complexity_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordComplexityInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordHistorySizeInput")
    def password_history_size_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordHistorySizeInput"))

    @builtins.property
    @jsii.member(jsii_name="clearTextPassword")
    def clear_text_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clearTextPassword"))

    @clear_text_password.setter
    def clear_text_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3bf584b32f7a2cedd4b4184d567d4f579f49ce2820845c08ae8b0bf663522b3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clearTextPassword", value)

    @builtins.property
    @jsii.member(jsii_name="maximumPasswordAge")
    def maximum_password_age(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maximumPasswordAge"))

    @maximum_password_age.setter
    def maximum_password_age(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfb8974cb22dc97eaad54df563bd4340985652873e5998166ca7c17234aa8013)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maximumPasswordAge", value)

    @builtins.property
    @jsii.member(jsii_name="minimumPasswordAge")
    def minimum_password_age(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "minimumPasswordAge"))

    @minimum_password_age.setter
    def minimum_password_age(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9c23fa3c883849fcba47a5a0ea75ae7f145b4fefaa58c458f59843a4b7f464f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minimumPasswordAge", value)

    @builtins.property
    @jsii.member(jsii_name="minimumPasswordLength")
    def minimum_password_length(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "minimumPasswordLength"))

    @minimum_password_length.setter
    def minimum_password_length(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab422fe7e75fcc05f3ec7cd5f8b71c539971cfaada8dbb48dfb52e37f0cb3bd2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minimumPasswordLength", value)

    @builtins.property
    @jsii.member(jsii_name="passwordComplexity")
    def password_complexity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "passwordComplexity"))

    @password_complexity.setter
    def password_complexity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49f61ff737c8b9e4a32310576d9b9284e43dccff1f4969d5241a41ace139d381)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "passwordComplexity", value)

    @builtins.property
    @jsii.member(jsii_name="passwordHistorySize")
    def password_history_size(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "passwordHistorySize"))

    @password_history_size.setter
    def password_history_size(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ea398589ee089eedbde2dd934db72c7743756355c25d18a6ee7dcaa1c6090f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "passwordHistorySize", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GpoSecurityPasswordPolicies]:
        return typing.cast(typing.Optional[GpoSecurityPasswordPolicies], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GpoSecurityPasswordPolicies],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6df8e29fe4f86b349444f7fb37dc0ec26fec263fa0e3859187521530a1b2ecf4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-ad.gpoSecurity.GpoSecurityRegistryKeys",
    jsii_struct_bases=[],
    name_mapping={
        "acl": "acl",
        "key_name": "keyName",
        "propagation_mode": "propagationMode",
    },
)
class GpoSecurityRegistryKeys:
    def __init__(
        self,
        *,
        acl: builtins.str,
        key_name: builtins.str,
        propagation_mode: builtins.str,
    ) -> None:
        '''
        :param acl: Security descriptor to apply. (https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-dtyp/f4296d69-1c0f-491f-9587-a960b292d070). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#acl GpoSecurity#acl}
        :param key_name: Fully qualified name of the key (https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-rrp/97587de7-3524-4291-8527-3951711 0c0eb). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#key_name GpoSecurity#key_name}
        :param propagation_mode: Control permission propagation. 0: Propagate permissions to all subkeys, 1: Replace existing permissions on all subkeys, 2: Do not allow permissions to be replaced on the key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#propagation_mode GpoSecurity#propagation_mode}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe2524f50e031da606c37d83319cf14a6e3f93f6fe4121cdb0bd21b257287ecf)
            check_type(argname="argument acl", value=acl, expected_type=type_hints["acl"])
            check_type(argname="argument key_name", value=key_name, expected_type=type_hints["key_name"])
            check_type(argname="argument propagation_mode", value=propagation_mode, expected_type=type_hints["propagation_mode"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "acl": acl,
            "key_name": key_name,
            "propagation_mode": propagation_mode,
        }

    @builtins.property
    def acl(self) -> builtins.str:
        '''Security descriptor to apply. (https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-dtyp/f4296d69-1c0f-491f-9587-a960b292d070).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#acl GpoSecurity#acl}
        '''
        result = self._values.get("acl")
        assert result is not None, "Required property 'acl' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key_name(self) -> builtins.str:
        '''Fully qualified name of the key (https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-rrp/97587de7-3524-4291-8527-3951711      0c0eb).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#key_name GpoSecurity#key_name}
        '''
        result = self._values.get("key_name")
        assert result is not None, "Required property 'key_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def propagation_mode(self) -> builtins.str:
        '''Control permission propagation.

        0: Propagate permissions to all subkeys, 1: Replace existing permissions on all subkeys, 2: Do not allow permissions to be replaced on the key.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#propagation_mode GpoSecurity#propagation_mode}
        '''
        result = self._values.get("propagation_mode")
        assert result is not None, "Required property 'propagation_mode' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GpoSecurityRegistryKeys(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GpoSecurityRegistryKeysList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-ad.gpoSecurity.GpoSecurityRegistryKeysList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__37e53ef0fe67b567ecb739b9cb4175b9016946c20706a9124f2c6930def1eeda)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "GpoSecurityRegistryKeysOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__180647ca0d470eb23e60ed3f7bc0ecfc068451a1c433b321c7cfffaec91f18e6)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GpoSecurityRegistryKeysOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b573e09539743887a145561fea6c0eecc3564f3450e72f87986c5d6ef16338e6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a8ad4ac3b88ffafd65dccb52585cf13c2092838edaab145c7437d868298f7ac3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__90af2de019ef2a1392216179e978572bd568a4369eead89a138b5b3b3f15e2fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GpoSecurityRegistryKeys]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GpoSecurityRegistryKeys]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GpoSecurityRegistryKeys]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2695d3967b8ab16e1ff4996ad237a8b3f3d0c1500e5e147ef808a7c6b129d23)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GpoSecurityRegistryKeysOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-ad.gpoSecurity.GpoSecurityRegistryKeysOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ce60821884678b6ace5e5413d0a09efa740d76cc6eb79cc793f74562f915dba1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="aclInput")
    def acl_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aclInput"))

    @builtins.property
    @jsii.member(jsii_name="keyNameInput")
    def key_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyNameInput"))

    @builtins.property
    @jsii.member(jsii_name="propagationModeInput")
    def propagation_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "propagationModeInput"))

    @builtins.property
    @jsii.member(jsii_name="acl")
    def acl(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "acl"))

    @acl.setter
    def acl(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b81bdf36405456012b9adf0a72c03fac4730b87833054a23d28c8b66a179dc83)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "acl", value)

    @builtins.property
    @jsii.member(jsii_name="keyName")
    def key_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyName"))

    @key_name.setter
    def key_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5064f13a7c106adfa33a44547adf2d52270952ef344162d8328972383c6b1d24)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyName", value)

    @builtins.property
    @jsii.member(jsii_name="propagationMode")
    def propagation_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "propagationMode"))

    @propagation_mode.setter
    def propagation_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__076764f6ccb7504d489b87a1486436f77915954d1cef112a6159b5ea1e134cb3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "propagationMode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GpoSecurityRegistryKeys, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GpoSecurityRegistryKeys, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GpoSecurityRegistryKeys, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5843af2273e9795269fbe86c9f2f320950fe7225e85b13035e0176ba17a1d56)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-ad.gpoSecurity.GpoSecurityRegistryValues",
    jsii_struct_bases=[],
    name_mapping={"key_name": "keyName", "value": "value", "value_type": "valueType"},
)
class GpoSecurityRegistryValues:
    def __init__(
        self,
        *,
        key_name: builtins.str,
        value: builtins.str,
        value_type: builtins.str,
    ) -> None:
        '''
        :param key_name: Fully qualified name of the key (https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-rrp/97587de7-3524-4291-8527-39517110c0eb). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#key_name GpoSecurity#key_name}
        :param value: The value of the key, matching the type set in ``value_type``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#value GpoSecurity#value}
        :param value_type: Data type of the key's value. 1: String, 2: Expand String, 3: Binary, 4: DWORD, 5: MULTI_SZ. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#value_type GpoSecurity#value_type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75bfb8fdde1f9e13205db062cd76b5fa0b133f6b623a99890f9f5cbbd069d3c6)
            check_type(argname="argument key_name", value=key_name, expected_type=type_hints["key_name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument value_type", value=value_type, expected_type=type_hints["value_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key_name": key_name,
            "value": value,
            "value_type": value_type,
        }

    @builtins.property
    def key_name(self) -> builtins.str:
        '''Fully qualified name of the key (https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-rrp/97587de7-3524-4291-8527-39517110c0eb).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#key_name GpoSecurity#key_name}
        '''
        result = self._values.get("key_name")
        assert result is not None, "Required property 'key_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''The value of the key, matching the type set in ``value_type``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#value GpoSecurity#value}
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value_type(self) -> builtins.str:
        '''Data type of the key's value. 1: String, 2: Expand String, 3: Binary, 4: DWORD, 5: MULTI_SZ.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#value_type GpoSecurity#value_type}
        '''
        result = self._values.get("value_type")
        assert result is not None, "Required property 'value_type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GpoSecurityRegistryValues(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GpoSecurityRegistryValuesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-ad.gpoSecurity.GpoSecurityRegistryValuesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__bcbb094c5c4a8a669a0a7c938f512ac23cce7bd3b49427430bb47166810e0a44)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "GpoSecurityRegistryValuesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ecbfbf75c53edaf6ef63ec83b26b1cf791a3c48a0b9622d8c6f925461ff0d19)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GpoSecurityRegistryValuesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__766abf9eb398c3b083a03901c9da22dbf1af939d3cfd83f35b969f325badf144)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9fc19054bc8965437eb5e13e5dc3c4ba38ac1400c76a30b34281f9e3e0b66c27)
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
            type_hints = typing.get_type_hints(_typecheckingstub__afa1042fb54db4a002f1f58d1bdbb2e97d9dc8e140f4f8417ec390273c9aeff4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GpoSecurityRegistryValues]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GpoSecurityRegistryValues]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GpoSecurityRegistryValues]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63220a5cc33804f8f4f773c146e53caf180d6fbd0cb24f67283edfbf5220a0d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GpoSecurityRegistryValuesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-ad.gpoSecurity.GpoSecurityRegistryValuesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b00e4b625b6350ce646e0a462164f2b27e624aa2fb9815d7a4abf709cc895f98)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="keyNameInput")
    def key_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyNameInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="valueTypeInput")
    def value_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="keyName")
    def key_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyName"))

    @key_name.setter
    def key_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7dd5d24214f3b53da38d98d81b483111f85057946d3dec7113e7fa5571b4450c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyName", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e507e5abe1642335fc358a3a0f9b0ac23a0d03f8fb542e23529523828bc6d3a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="valueType")
    def value_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "valueType"))

    @value_type.setter
    def value_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aaa0306e211019a88d80d5edc9c7b29fdb50597b1e0567bdefef2325ba495f49)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "valueType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GpoSecurityRegistryValues, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GpoSecurityRegistryValues, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GpoSecurityRegistryValues, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c636f273e19105d47f3c0b8a118ee441c4ef0517284d7b1aea03c7c2994738f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-ad.gpoSecurity.GpoSecurityRestrictedGroups",
    jsii_struct_bases=[],
    name_mapping={
        "group_memberof": "groupMemberof",
        "group_members": "groupMembers",
        "group_name": "groupName",
    },
)
class GpoSecurityRestrictedGroups:
    def __init__(
        self,
        *,
        group_memberof: builtins.str,
        group_members: builtins.str,
        group_name: builtins.str,
    ) -> None:
        '''
        :param group_memberof: Comma separated list of group names or SIDs that this group belongs to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#group_memberof GpoSecurity#group_memberof}
        :param group_members: Comma separated list of group names or SIDs that are members of the group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#group_members GpoSecurity#group_members}
        :param group_name: Name of the group we are managing. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#group_name GpoSecurity#group_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ce42a35443ab69779568df4c7a89ae66e130c3bcc77f1818bff49ca65bf24c6)
            check_type(argname="argument group_memberof", value=group_memberof, expected_type=type_hints["group_memberof"])
            check_type(argname="argument group_members", value=group_members, expected_type=type_hints["group_members"])
            check_type(argname="argument group_name", value=group_name, expected_type=type_hints["group_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "group_memberof": group_memberof,
            "group_members": group_members,
            "group_name": group_name,
        }

    @builtins.property
    def group_memberof(self) -> builtins.str:
        '''Comma separated list of group names or SIDs that this group belongs to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#group_memberof GpoSecurity#group_memberof}
        '''
        result = self._values.get("group_memberof")
        assert result is not None, "Required property 'group_memberof' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group_members(self) -> builtins.str:
        '''Comma separated list of group names or SIDs that are members of the group.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#group_members GpoSecurity#group_members}
        '''
        result = self._values.get("group_members")
        assert result is not None, "Required property 'group_members' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group_name(self) -> builtins.str:
        '''Name of the group we are managing.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#group_name GpoSecurity#group_name}
        '''
        result = self._values.get("group_name")
        assert result is not None, "Required property 'group_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GpoSecurityRestrictedGroups(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GpoSecurityRestrictedGroupsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-ad.gpoSecurity.GpoSecurityRestrictedGroupsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7d8f2a21b9250b949d87dcf0675bb9dbeb0aefc965c785dc97aeac4a9d41b606)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "GpoSecurityRestrictedGroupsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec7d639cd36117eff25a8545d5f5f263eebbaa4976ed32385973d67e549842a2)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GpoSecurityRestrictedGroupsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0ed4408d60cab98dd7f540675872dca9ab70d8add470f4b423658e7d58042fd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7f1571828f74b4cd6c7d0a28655181374928f2ea180c23508a85707c81f88de0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e39d85ec3cfc4fcd92eb5d102edb15cbec9b116b0a57381e11d5f8835527dc3c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GpoSecurityRestrictedGroups]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GpoSecurityRestrictedGroups]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GpoSecurityRestrictedGroups]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7ab5d1dfaf42c84cc54cda4317914d78b3a9fd3a4878266ed145171542c35b3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GpoSecurityRestrictedGroupsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-ad.gpoSecurity.GpoSecurityRestrictedGroupsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9d4f4ead6260d6ecc6895875dfe5b8b3fa1aba450c79c8b791388e081042067d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="groupMemberofInput")
    def group_memberof_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupMemberofInput"))

    @builtins.property
    @jsii.member(jsii_name="groupMembersInput")
    def group_members_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupMembersInput"))

    @builtins.property
    @jsii.member(jsii_name="groupNameInput")
    def group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="groupMemberof")
    def group_memberof(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "groupMemberof"))

    @group_memberof.setter
    def group_memberof(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e9e27e9d7431f6fb2af394ec7dffcb2a078703033a0f1614de2c34e4ea50e58)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupMemberof", value)

    @builtins.property
    @jsii.member(jsii_name="groupMembers")
    def group_members(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "groupMembers"))

    @group_members.setter
    def group_members(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c519a1973dc7812aa9985d8920b5614e7419aff7b49a3c62df06f97bb7c99ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupMembers", value)

    @builtins.property
    @jsii.member(jsii_name="groupName")
    def group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "groupName"))

    @group_name.setter
    def group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a16ef776022275c18e0168bd78d222baf9c86459ac814b47d13c05eaedeff474)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GpoSecurityRestrictedGroups, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GpoSecurityRestrictedGroups, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GpoSecurityRestrictedGroups, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52d8847ab65dcf220f589c919a5db0172b63b99867073474e2db94336ae13b7a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-ad.gpoSecurity.GpoSecuritySystemLog",
    jsii_struct_bases=[],
    name_mapping={
        "audit_log_retention_period": "auditLogRetentionPeriod",
        "maximum_log_size": "maximumLogSize",
        "restrict_guest_access": "restrictGuestAccess",
        "retention_days": "retentionDays",
    },
)
class GpoSecuritySystemLog:
    def __init__(
        self,
        *,
        audit_log_retention_period: typing.Optional[builtins.str] = None,
        maximum_log_size: typing.Optional[builtins.str] = None,
        restrict_guest_access: typing.Optional[builtins.str] = None,
        retention_days: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param audit_log_retention_period: Control log retention. Values: 0: overwrite events as needed, 1: overwrite events as specified specified by ``retention_days``, 2: never overwrite events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#audit_log_retention_period GpoSecurity#audit_log_retention_period}
        :param maximum_log_size: Maximum size of log in KiloBytes. (64-4194240). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#maximum_log_size GpoSecurity#maximum_log_size}
        :param restrict_guest_access: Restrict access to logs for guest users. A non-zero value restricts access to guest users. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#restrict_guest_access GpoSecurity#restrict_guest_access}
        :param retention_days: Number of days before new events overwrite old events. (1-365). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#retention_days GpoSecurity#retention_days}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e76d4551a024fb277187dfd83ead93a052d42a6ad199ce2ded65afa58e6ce6d)
            check_type(argname="argument audit_log_retention_period", value=audit_log_retention_period, expected_type=type_hints["audit_log_retention_period"])
            check_type(argname="argument maximum_log_size", value=maximum_log_size, expected_type=type_hints["maximum_log_size"])
            check_type(argname="argument restrict_guest_access", value=restrict_guest_access, expected_type=type_hints["restrict_guest_access"])
            check_type(argname="argument retention_days", value=retention_days, expected_type=type_hints["retention_days"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if audit_log_retention_period is not None:
            self._values["audit_log_retention_period"] = audit_log_retention_period
        if maximum_log_size is not None:
            self._values["maximum_log_size"] = maximum_log_size
        if restrict_guest_access is not None:
            self._values["restrict_guest_access"] = restrict_guest_access
        if retention_days is not None:
            self._values["retention_days"] = retention_days

    @builtins.property
    def audit_log_retention_period(self) -> typing.Optional[builtins.str]:
        '''Control log retention.

        Values: 0: overwrite events as needed, 1: overwrite events as specified specified by ``retention_days``, 2: never overwrite events.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#audit_log_retention_period GpoSecurity#audit_log_retention_period}
        '''
        result = self._values.get("audit_log_retention_period")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def maximum_log_size(self) -> typing.Optional[builtins.str]:
        '''Maximum size of log in KiloBytes. (64-4194240).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#maximum_log_size GpoSecurity#maximum_log_size}
        '''
        result = self._values.get("maximum_log_size")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def restrict_guest_access(self) -> typing.Optional[builtins.str]:
        '''Restrict access to logs for guest users. A non-zero value restricts access to guest users.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#restrict_guest_access GpoSecurity#restrict_guest_access}
        '''
        result = self._values.get("restrict_guest_access")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def retention_days(self) -> typing.Optional[builtins.str]:
        '''Number of days before new events overwrite old events. (1-365).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#retention_days GpoSecurity#retention_days}
        '''
        result = self._values.get("retention_days")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GpoSecuritySystemLog(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GpoSecuritySystemLogOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-ad.gpoSecurity.GpoSecuritySystemLogOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9047aa71e60b1376330a4c11a148c575817c48c370543b332bd60f90ab440118)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAuditLogRetentionPeriod")
    def reset_audit_log_retention_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuditLogRetentionPeriod", []))

    @jsii.member(jsii_name="resetMaximumLogSize")
    def reset_maximum_log_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaximumLogSize", []))

    @jsii.member(jsii_name="resetRestrictGuestAccess")
    def reset_restrict_guest_access(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRestrictGuestAccess", []))

    @jsii.member(jsii_name="resetRetentionDays")
    def reset_retention_days(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetentionDays", []))

    @builtins.property
    @jsii.member(jsii_name="auditLogRetentionPeriodInput")
    def audit_log_retention_period_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "auditLogRetentionPeriodInput"))

    @builtins.property
    @jsii.member(jsii_name="maximumLogSizeInput")
    def maximum_log_size_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maximumLogSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="restrictGuestAccessInput")
    def restrict_guest_access_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "restrictGuestAccessInput"))

    @builtins.property
    @jsii.member(jsii_name="retentionDaysInput")
    def retention_days_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "retentionDaysInput"))

    @builtins.property
    @jsii.member(jsii_name="auditLogRetentionPeriod")
    def audit_log_retention_period(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "auditLogRetentionPeriod"))

    @audit_log_retention_period.setter
    def audit_log_retention_period(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6cdbc5748066abd45bc9ff18cb40e2466615357ce32b97b9ce2c67a01949179)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "auditLogRetentionPeriod", value)

    @builtins.property
    @jsii.member(jsii_name="maximumLogSize")
    def maximum_log_size(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maximumLogSize"))

    @maximum_log_size.setter
    def maximum_log_size(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6e1fe429d4c83a91b231c20adeb705f0ceb9b2bb606fb6cccb23080b5d8fb55)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maximumLogSize", value)

    @builtins.property
    @jsii.member(jsii_name="restrictGuestAccess")
    def restrict_guest_access(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "restrictGuestAccess"))

    @restrict_guest_access.setter
    def restrict_guest_access(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a4e1e12a8d7b3ff6007d35508e4ae1ae7bf083769827ff7c1e7bd1518fcc11f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "restrictGuestAccess", value)

    @builtins.property
    @jsii.member(jsii_name="retentionDays")
    def retention_days(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "retentionDays"))

    @retention_days.setter
    def retention_days(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b6e2de1e689a60435cfc47d5df3fc44c777915dc45dc19e36b88e8acecc1dd8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retentionDays", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GpoSecuritySystemLog]:
        return typing.cast(typing.Optional[GpoSecuritySystemLog], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[GpoSecuritySystemLog]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2e92fe95548761b1f23accc2932468b03068a41427005c71cb237b97c9e44a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-ad.gpoSecurity.GpoSecuritySystemServices",
    jsii_struct_bases=[],
    name_mapping={
        "acl": "acl",
        "service_name": "serviceName",
        "startup_mode": "startupMode",
    },
)
class GpoSecuritySystemServices:
    def __init__(
        self,
        *,
        acl: builtins.str,
        service_name: builtins.str,
        startup_mode: builtins.str,
    ) -> None:
        '''
        :param acl: Security descriptor to apply. (https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-dtyp/f4296d69-1c0f-491f-9587-a960b292d070). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#acl GpoSecurity#acl}
        :param service_name: Name of the service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#service_name GpoSecurity#service_name}
        :param startup_mode: Startup mode of the service. Possible values are 2: Automatic, 3: Manual, 4: Disabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#startup_mode GpoSecurity#startup_mode}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2188d074c1f3c10a2818a60856846a4340c28f6588dcf5329ee38be44e09433a)
            check_type(argname="argument acl", value=acl, expected_type=type_hints["acl"])
            check_type(argname="argument service_name", value=service_name, expected_type=type_hints["service_name"])
            check_type(argname="argument startup_mode", value=startup_mode, expected_type=type_hints["startup_mode"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "acl": acl,
            "service_name": service_name,
            "startup_mode": startup_mode,
        }

    @builtins.property
    def acl(self) -> builtins.str:
        '''Security descriptor to apply. (https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-dtyp/f4296d69-1c0f-491f-9587-a960b292d070).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#acl GpoSecurity#acl}
        '''
        result = self._values.get("acl")
        assert result is not None, "Required property 'acl' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_name(self) -> builtins.str:
        '''Name of the service.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#service_name GpoSecurity#service_name}
        '''
        result = self._values.get("service_name")
        assert result is not None, "Required property 'service_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def startup_mode(self) -> builtins.str:
        '''Startup mode of the service. Possible values are 2: Automatic, 3: Manual, 4: Disabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/gpo_security#startup_mode GpoSecurity#startup_mode}
        '''
        result = self._values.get("startup_mode")
        assert result is not None, "Required property 'startup_mode' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GpoSecuritySystemServices(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GpoSecuritySystemServicesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-ad.gpoSecurity.GpoSecuritySystemServicesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7509ee1c62144afac8154d9faddd45f0bd704298ea8c66bc4765ce868af2ffae)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "GpoSecuritySystemServicesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec3c5bf33bb2975566c5169d194b4af1bfa7eb5c3b7945a5ca9ce61f1f2184f2)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GpoSecuritySystemServicesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d091ecc4e091150b1d6f4b7b68967b1ec82f35ccfddd34ec49b408fff57a28b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d068218450a97e37d295e183b1f47cbc9c5a2b1cf322f6667591b6e3dd760a5a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9a9aec6570f16647a49858248e7b750413ee12982f35e566dfb36df5a07a4d9c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GpoSecuritySystemServices]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GpoSecuritySystemServices]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GpoSecuritySystemServices]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d29e27b10e5fc8b483aab06e231783e559fece8060af2ebeb8f5b51fd326f84)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GpoSecuritySystemServicesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-ad.gpoSecurity.GpoSecuritySystemServicesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f0a63d6fdfcbba74dc80cdeb049a77b037e306134574e02f1df3a752d4ab0060)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="aclInput")
    def acl_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aclInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceNameInput")
    def service_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="startupModeInput")
    def startup_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startupModeInput"))

    @builtins.property
    @jsii.member(jsii_name="acl")
    def acl(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "acl"))

    @acl.setter
    def acl(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a8679cefa26e81a6e1b8cb417a162d546c097c87bd7c07528262bd7cfd34638)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "acl", value)

    @builtins.property
    @jsii.member(jsii_name="serviceName")
    def service_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceName"))

    @service_name.setter
    def service_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a23e58d37ce496a2e6191e8e61863bc5b8ced5ae4a8cf99cee27669d559d3a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceName", value)

    @builtins.property
    @jsii.member(jsii_name="startupMode")
    def startup_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startupMode"))

    @startup_mode.setter
    def startup_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6cf81c79e5a641f68b9f8794e0fc6c1b50c066da0acd5ffd4be69c226281739a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startupMode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GpoSecuritySystemServices, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GpoSecuritySystemServices, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GpoSecuritySystemServices, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__341eba7af3ad81a1633955901d60d5874642bb5dfab10c5f9a7c8b882a116e1c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GpoSecurity",
    "GpoSecurityAccountLockout",
    "GpoSecurityAccountLockoutOutputReference",
    "GpoSecurityApplicationLog",
    "GpoSecurityApplicationLogOutputReference",
    "GpoSecurityAuditLog",
    "GpoSecurityAuditLogOutputReference",
    "GpoSecurityConfig",
    "GpoSecurityEventAudit",
    "GpoSecurityEventAuditOutputReference",
    "GpoSecurityFilesystem",
    "GpoSecurityFilesystemList",
    "GpoSecurityFilesystemOutputReference",
    "GpoSecurityKerberosPolicy",
    "GpoSecurityKerberosPolicyOutputReference",
    "GpoSecurityPasswordPolicies",
    "GpoSecurityPasswordPoliciesOutputReference",
    "GpoSecurityRegistryKeys",
    "GpoSecurityRegistryKeysList",
    "GpoSecurityRegistryKeysOutputReference",
    "GpoSecurityRegistryValues",
    "GpoSecurityRegistryValuesList",
    "GpoSecurityRegistryValuesOutputReference",
    "GpoSecurityRestrictedGroups",
    "GpoSecurityRestrictedGroupsList",
    "GpoSecurityRestrictedGroupsOutputReference",
    "GpoSecuritySystemLog",
    "GpoSecuritySystemLogOutputReference",
    "GpoSecuritySystemServices",
    "GpoSecuritySystemServicesList",
    "GpoSecuritySystemServicesOutputReference",
]

publication.publish()

def _typecheckingstub__cdb1107fda99a69a663814450f726e0075566c2fbd1e3fef8eef763c7bfe69bd(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    gpo_container: builtins.str,
    account_lockout: typing.Optional[typing.Union[GpoSecurityAccountLockout, typing.Dict[builtins.str, typing.Any]]] = None,
    application_log: typing.Optional[typing.Union[GpoSecurityApplicationLog, typing.Dict[builtins.str, typing.Any]]] = None,
    audit_log: typing.Optional[typing.Union[GpoSecurityAuditLog, typing.Dict[builtins.str, typing.Any]]] = None,
    event_audit: typing.Optional[typing.Union[GpoSecurityEventAudit, typing.Dict[builtins.str, typing.Any]]] = None,
    filesystem: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GpoSecurityFilesystem, typing.Dict[builtins.str, typing.Any]]]]] = None,
    id: typing.Optional[builtins.str] = None,
    kerberos_policy: typing.Optional[typing.Union[GpoSecurityKerberosPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    password_policies: typing.Optional[typing.Union[GpoSecurityPasswordPolicies, typing.Dict[builtins.str, typing.Any]]] = None,
    registry_keys: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GpoSecurityRegistryKeys, typing.Dict[builtins.str, typing.Any]]]]] = None,
    registry_values: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GpoSecurityRegistryValues, typing.Dict[builtins.str, typing.Any]]]]] = None,
    restricted_groups: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GpoSecurityRestrictedGroups, typing.Dict[builtins.str, typing.Any]]]]] = None,
    system_log: typing.Optional[typing.Union[GpoSecuritySystemLog, typing.Dict[builtins.str, typing.Any]]] = None,
    system_services: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GpoSecuritySystemServices, typing.Dict[builtins.str, typing.Any]]]]] = None,
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

def _typecheckingstub__a95d4be4b10541ca0b6a13f4568a834665f4039492895b15e0b50371922a1be9(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GpoSecurityFilesystem, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5f9d5edf01079abe58071bc93847a52f6e2c734042f0e841f5ff9ddcefb4bab(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GpoSecurityRegistryKeys, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6e1f717f7af974b9c9bea2b82c3510507583504a0b1a6e5514f1565a6134603(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GpoSecurityRegistryValues, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__534ae54df2a3d3efcae6aa677e8ce1adbc2f0032eb9cebf38d22412c8d24cb4c(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GpoSecurityRestrictedGroups, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d66305e3fd97727c8064171ea3ef2be46739d5c37d1813863fe702bac3bb850(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GpoSecuritySystemServices, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2281cd61760e5c2da2a86a226aa36540c0358fb361e387ad61ba4210ac651fa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fc44d8f755fd069e480a4574cf496e6cd9c42d3f294583862277c8b8587eff7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cacf0f22d18e2b8532d32516e2fd1a537c0c00aaee04dca03763d69b225ff8c1(
    *,
    force_logoff_when_hour_expire: typing.Optional[builtins.str] = None,
    lockout_bad_count: typing.Optional[builtins.str] = None,
    lockout_duration: typing.Optional[builtins.str] = None,
    reset_lockout_count: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00fcbffdf6aa8425791393df721ea48b413906ee62c43eaca7430ea046441e98(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__237edace8a3f23958a9d5b246ebc5132a7de1bea831693b3a0251e0048a22aaf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bcc309013d4a30036c9126c89ee2f2601664af6e1e31c07305f53d03530aed1e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2d5cdc4e02b08537c8cf3e4cbc40e2011acef50327ac885b76dd34db74384a4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6283fcb6510c72cf2a67ac32cb7567d34385205ab8ba9652350b430975b195d0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3c12e763b02ec987d7b3cb3d79579848dbfb8b04da917b778109edc9d2e316f(
    value: typing.Optional[GpoSecurityAccountLockout],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0d73debdd5e6d72575b43ce6044d3ea0513f21b83c4340353a0baa55419e7ca(
    *,
    audit_log_retention_period: typing.Optional[builtins.str] = None,
    maximum_log_size: typing.Optional[builtins.str] = None,
    restrict_guest_access: typing.Optional[builtins.str] = None,
    retention_days: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac14ebd89771ca0aac99195f79c50cd73a2c1b9c4feacdb411d8c6f665a946a8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb6c5039bf9f921f8eb803e24b031cafe0ca4c43b9c8b88baaad697399f10571(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56f629f8ae48e32d9476248637033fd3186a12824b6ce8e36a6c8e2df95fc28a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f6c9613bb11364a7f9a816b34702ffd66f5f800a5072672dba9e3619f2260b1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfeac08926005551e9babc0e38f03f59d0c70995f8f552233deac5da821518a9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2ef25f346061db36ce8137c7913085d654c78d356f0eb5f547cf7a22b799e7b(
    value: typing.Optional[GpoSecurityApplicationLog],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85435532b75fbdc4dc1b2e8e371b20c3191694415025fee1e3e76c4cae5b9108(
    *,
    audit_log_retention_period: typing.Optional[builtins.str] = None,
    maximum_log_size: typing.Optional[builtins.str] = None,
    restrict_guest_access: typing.Optional[builtins.str] = None,
    retention_days: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a8f18e557ceb6f1ce26ec997861249fd892e3181328be3714732b1614eac5e3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4200b7b700fac011f82d0a1371b640c43a6d437575b33aef41957d90ba333ab0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9439c34a383f5f0ca371a5d6762c478d03afe4b42a76e3edcebf7b82e0f505d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4b8ea273308141124153bba9cb02983d952967f5d2b7332061ca7776a3655c6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f31648752ad56bfc1cee76deba694e6c63f43942d46183a13607f4b693d37f13(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c76bafe3233af81a3096329685077641e7853dbe87ec8c52a65ff2f3b77d9d58(
    value: typing.Optional[GpoSecurityAuditLog],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__813fbf075deae0a8dfc08469b9da1745f51d18e18bfeb83aa92f4d8ad9e55094(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    gpo_container: builtins.str,
    account_lockout: typing.Optional[typing.Union[GpoSecurityAccountLockout, typing.Dict[builtins.str, typing.Any]]] = None,
    application_log: typing.Optional[typing.Union[GpoSecurityApplicationLog, typing.Dict[builtins.str, typing.Any]]] = None,
    audit_log: typing.Optional[typing.Union[GpoSecurityAuditLog, typing.Dict[builtins.str, typing.Any]]] = None,
    event_audit: typing.Optional[typing.Union[GpoSecurityEventAudit, typing.Dict[builtins.str, typing.Any]]] = None,
    filesystem: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GpoSecurityFilesystem, typing.Dict[builtins.str, typing.Any]]]]] = None,
    id: typing.Optional[builtins.str] = None,
    kerberos_policy: typing.Optional[typing.Union[GpoSecurityKerberosPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    password_policies: typing.Optional[typing.Union[GpoSecurityPasswordPolicies, typing.Dict[builtins.str, typing.Any]]] = None,
    registry_keys: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GpoSecurityRegistryKeys, typing.Dict[builtins.str, typing.Any]]]]] = None,
    registry_values: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GpoSecurityRegistryValues, typing.Dict[builtins.str, typing.Any]]]]] = None,
    restricted_groups: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GpoSecurityRestrictedGroups, typing.Dict[builtins.str, typing.Any]]]]] = None,
    system_log: typing.Optional[typing.Union[GpoSecuritySystemLog, typing.Dict[builtins.str, typing.Any]]] = None,
    system_services: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GpoSecuritySystemServices, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04f36083c93644f3b8249fda0271cc7369ecb371f6324297bdf28af4eb49ed93(
    *,
    audit_account_logon: typing.Optional[builtins.str] = None,
    audit_account_manage: typing.Optional[builtins.str] = None,
    audit_ds_access: typing.Optional[builtins.str] = None,
    audit_logon_events: typing.Optional[builtins.str] = None,
    audit_object_access: typing.Optional[builtins.str] = None,
    audit_policy_change: typing.Optional[builtins.str] = None,
    audit_privilege_use: typing.Optional[builtins.str] = None,
    audit_process_tracking: typing.Optional[builtins.str] = None,
    audit_system_events: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7aced749cdd9f0af83009aa8cd7daefde8cf57b3ae23c0023cf6ba818050c3c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72dc27d5eb10f2a1e98093f033958de03c6ca1d9b5181dc08dd55e5ee93b2cb2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab4fb512367fb02388379891951051a5aecb04273e97ad46d61125e712668758(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44d1b67d546b251edaabd6d5cb3f263a11793e89714c232df983b93da3d70f69(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38f7374ad9a96aa02f8fc27e00ed1c02d2536dfce2b83a75503e6a02a692d1b5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb3b3a8a30449eca40ab5367378948333c3c9064720d88e863de1e64ab99a965(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51cc1a53da4374db98eaac5789dd654bb44c20acf052fea696ae3f024a42f012(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__068eb046ab6b694b4a9fabe1fbdf45b1f13457eaf7cbeda35e5b3cd417847678(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a00fdb2c84f00ea6ea46bceaa18264e129f30fb3bd193510709847d1d515fa03(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d85c3c63cf0735082c964ab7bc517a67f6c2dde16a5432dc1e546500c64c487(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a0da96c093de149b615d2df34c10bd5e4a01dbfe7908f63c5074a21a2d8f957(
    value: typing.Optional[GpoSecurityEventAudit],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1e47ad0df9ce1f0d0dca5122a3c2d58890a35639017d7ef682e0539a203733f(
    *,
    acl: builtins.str,
    path: builtins.str,
    propagation_mode: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58685115e48fa2d8f9c180523df2e90ee2743fcad970eef0b2d181c5864f8463(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9c89d89a19132886d7c043fd6c5eece40ac642f35aca124e50042b51859bcf7(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a5fa93edd75fd44574e9a3b89ee9e0c412f971ec70770cac7dc642ea9dc7bb4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6dc1fd2681d7adb3769fd40a7472b86fc3f9adafb7cd50cba4d914dbed04e947(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d550ab727be3a427a9dbb8906d9c533edee1acb2945a718daa0a0bf580dcab5(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82f4766df6f19b922c0e09840c07b68c8b4af310c9ba834774f7727a35c86094(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GpoSecurityFilesystem]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec11fd6cb4d6878c3c9508fee627188cc515ee30e97bca7b62fc675f21e09f35(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8082f6f1ffa98954e4858d4cb4f26149053bcd801f288b4b0ea4ad8d4cd19dd8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72034034ab63474ced193d307b64f5807c622f14386cacc3673485cfd53b2c90(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__feb72591ba803d01834d0a0f85bf393488de88ebbc014b63d61a26daf3b50528(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26f9e1640d50a64c6151582b2cae33a8ac491d90b00b01d6390e1b4dd3902172(
    value: typing.Optional[typing.Union[GpoSecurityFilesystem, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02abc20895ee902d3e4eeb6d435b574318c54664742937967fdb55e9c67d803b(
    *,
    max_clock_skew: typing.Optional[builtins.str] = None,
    max_renew_age: typing.Optional[builtins.str] = None,
    max_service_age: typing.Optional[builtins.str] = None,
    max_ticket_age: typing.Optional[builtins.str] = None,
    ticket_validate_client: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f57613fda8f901a1d90c37fea97d32f00a7238029bfb3d26fd4738e1e759235(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__070d1751c905b718abd561d24aa7fd9ef71594aca979ae389cd8eef45992acad(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__475c396392478331dae4bbd7ef020fde2367ee07c6a9f24a793fb7df11edd4b2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b52ad9a19a9e9e4189cb832f6dff9253595a96bd7cab6a27e0016a77291f6771(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd57b5b5434a2f247aa5d8cb997a9fa28d669fc36f3ea5a3ef34d5e8b4b78059(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0806aa8e6dadb307c62248cb51c893bd767eab2cfc04cb67d0488185149a1a9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ac312c1d24b7480d6d5e6ef565387d401a59b600910b6ca8f9e68e5a7d1db84(
    value: typing.Optional[GpoSecurityKerberosPolicy],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e772677afd93a9ada091ed35eef2d3076c0e7452d28b59f4cadf651231179e0(
    *,
    clear_text_password: typing.Optional[builtins.str] = None,
    maximum_password_age: typing.Optional[builtins.str] = None,
    minimum_password_age: typing.Optional[builtins.str] = None,
    minimum_password_length: typing.Optional[builtins.str] = None,
    password_complexity: typing.Optional[builtins.str] = None,
    password_history_size: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48fe57bb1529711996c86f5e89a70427c7bc6363b3496828324724c869053e5e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3bf584b32f7a2cedd4b4184d567d4f579f49ce2820845c08ae8b0bf663522b3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfb8974cb22dc97eaad54df563bd4340985652873e5998166ca7c17234aa8013(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9c23fa3c883849fcba47a5a0ea75ae7f145b4fefaa58c458f59843a4b7f464f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab422fe7e75fcc05f3ec7cd5f8b71c539971cfaada8dbb48dfb52e37f0cb3bd2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49f61ff737c8b9e4a32310576d9b9284e43dccff1f4969d5241a41ace139d381(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ea398589ee089eedbde2dd934db72c7743756355c25d18a6ee7dcaa1c6090f8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6df8e29fe4f86b349444f7fb37dc0ec26fec263fa0e3859187521530a1b2ecf4(
    value: typing.Optional[GpoSecurityPasswordPolicies],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe2524f50e031da606c37d83319cf14a6e3f93f6fe4121cdb0bd21b257287ecf(
    *,
    acl: builtins.str,
    key_name: builtins.str,
    propagation_mode: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37e53ef0fe67b567ecb739b9cb4175b9016946c20706a9124f2c6930def1eeda(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__180647ca0d470eb23e60ed3f7bc0ecfc068451a1c433b321c7cfffaec91f18e6(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b573e09539743887a145561fea6c0eecc3564f3450e72f87986c5d6ef16338e6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8ad4ac3b88ffafd65dccb52585cf13c2092838edaab145c7437d868298f7ac3(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90af2de019ef2a1392216179e978572bd568a4369eead89a138b5b3b3f15e2fa(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2695d3967b8ab16e1ff4996ad237a8b3f3d0c1500e5e147ef808a7c6b129d23(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GpoSecurityRegistryKeys]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce60821884678b6ace5e5413d0a09efa740d76cc6eb79cc793f74562f915dba1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b81bdf36405456012b9adf0a72c03fac4730b87833054a23d28c8b66a179dc83(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5064f13a7c106adfa33a44547adf2d52270952ef344162d8328972383c6b1d24(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__076764f6ccb7504d489b87a1486436f77915954d1cef112a6159b5ea1e134cb3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5843af2273e9795269fbe86c9f2f320950fe7225e85b13035e0176ba17a1d56(
    value: typing.Optional[typing.Union[GpoSecurityRegistryKeys, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75bfb8fdde1f9e13205db062cd76b5fa0b133f6b623a99890f9f5cbbd069d3c6(
    *,
    key_name: builtins.str,
    value: builtins.str,
    value_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bcbb094c5c4a8a669a0a7c938f512ac23cce7bd3b49427430bb47166810e0a44(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ecbfbf75c53edaf6ef63ec83b26b1cf791a3c48a0b9622d8c6f925461ff0d19(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__766abf9eb398c3b083a03901c9da22dbf1af939d3cfd83f35b969f325badf144(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fc19054bc8965437eb5e13e5dc3c4ba38ac1400c76a30b34281f9e3e0b66c27(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afa1042fb54db4a002f1f58d1bdbb2e97d9dc8e140f4f8417ec390273c9aeff4(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63220a5cc33804f8f4f773c146e53caf180d6fbd0cb24f67283edfbf5220a0d7(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GpoSecurityRegistryValues]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b00e4b625b6350ce646e0a462164f2b27e624aa2fb9815d7a4abf709cc895f98(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7dd5d24214f3b53da38d98d81b483111f85057946d3dec7113e7fa5571b4450c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e507e5abe1642335fc358a3a0f9b0ac23a0d03f8fb542e23529523828bc6d3a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aaa0306e211019a88d80d5edc9c7b29fdb50597b1e0567bdefef2325ba495f49(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c636f273e19105d47f3c0b8a118ee441c4ef0517284d7b1aea03c7c2994738f3(
    value: typing.Optional[typing.Union[GpoSecurityRegistryValues, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ce42a35443ab69779568df4c7a89ae66e130c3bcc77f1818bff49ca65bf24c6(
    *,
    group_memberof: builtins.str,
    group_members: builtins.str,
    group_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d8f2a21b9250b949d87dcf0675bb9dbeb0aefc965c785dc97aeac4a9d41b606(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec7d639cd36117eff25a8545d5f5f263eebbaa4976ed32385973d67e549842a2(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0ed4408d60cab98dd7f540675872dca9ab70d8add470f4b423658e7d58042fd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f1571828f74b4cd6c7d0a28655181374928f2ea180c23508a85707c81f88de0(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e39d85ec3cfc4fcd92eb5d102edb15cbec9b116b0a57381e11d5f8835527dc3c(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7ab5d1dfaf42c84cc54cda4317914d78b3a9fd3a4878266ed145171542c35b3(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GpoSecurityRestrictedGroups]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d4f4ead6260d6ecc6895875dfe5b8b3fa1aba450c79c8b791388e081042067d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e9e27e9d7431f6fb2af394ec7dffcb2a078703033a0f1614de2c34e4ea50e58(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c519a1973dc7812aa9985d8920b5614e7419aff7b49a3c62df06f97bb7c99ed(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a16ef776022275c18e0168bd78d222baf9c86459ac814b47d13c05eaedeff474(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52d8847ab65dcf220f589c919a5db0172b63b99867073474e2db94336ae13b7a(
    value: typing.Optional[typing.Union[GpoSecurityRestrictedGroups, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e76d4551a024fb277187dfd83ead93a052d42a6ad199ce2ded65afa58e6ce6d(
    *,
    audit_log_retention_period: typing.Optional[builtins.str] = None,
    maximum_log_size: typing.Optional[builtins.str] = None,
    restrict_guest_access: typing.Optional[builtins.str] = None,
    retention_days: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9047aa71e60b1376330a4c11a148c575817c48c370543b332bd60f90ab440118(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6cdbc5748066abd45bc9ff18cb40e2466615357ce32b97b9ce2c67a01949179(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6e1fe429d4c83a91b231c20adeb705f0ceb9b2bb606fb6cccb23080b5d8fb55(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a4e1e12a8d7b3ff6007d35508e4ae1ae7bf083769827ff7c1e7bd1518fcc11f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b6e2de1e689a60435cfc47d5df3fc44c777915dc45dc19e36b88e8acecc1dd8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2e92fe95548761b1f23accc2932468b03068a41427005c71cb237b97c9e44a8(
    value: typing.Optional[GpoSecuritySystemLog],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2188d074c1f3c10a2818a60856846a4340c28f6588dcf5329ee38be44e09433a(
    *,
    acl: builtins.str,
    service_name: builtins.str,
    startup_mode: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7509ee1c62144afac8154d9faddd45f0bd704298ea8c66bc4765ce868af2ffae(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec3c5bf33bb2975566c5169d194b4af1bfa7eb5c3b7945a5ca9ce61f1f2184f2(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d091ecc4e091150b1d6f4b7b68967b1ec82f35ccfddd34ec49b408fff57a28b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d068218450a97e37d295e183b1f47cbc9c5a2b1cf322f6667591b6e3dd760a5a(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a9aec6570f16647a49858248e7b750413ee12982f35e566dfb36df5a07a4d9c(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d29e27b10e5fc8b483aab06e231783e559fece8060af2ebeb8f5b51fd326f84(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GpoSecuritySystemServices]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0a63d6fdfcbba74dc80cdeb049a77b037e306134574e02f1df3a752d4ab0060(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a8679cefa26e81a6e1b8cb417a162d546c097c87bd7c07528262bd7cfd34638(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a23e58d37ce496a2e6191e8e61863bc5b8ced5ae4a8cf99cee27669d559d3a4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6cf81c79e5a641f68b9f8794e0fc6c1b50c066da0acd5ffd4be69c226281739a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__341eba7af3ad81a1633955901d60d5874642bb5dfab10c5f9a7c8b882a116e1c(
    value: typing.Optional[typing.Union[GpoSecuritySystemServices, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
