'''
# `ad_user`

Refer to the Terraform Registory for docs: [`ad_user`](https://www.terraform.io/docs/providers/ad/r/user).
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


class User(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-ad.user.User",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/ad/r/user ad_user}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        display_name: builtins.str,
        principal_name: builtins.str,
        sam_account_name: builtins.str,
        cannot_change_password: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        city: typing.Optional[builtins.str] = None,
        company: typing.Optional[builtins.str] = None,
        container: typing.Optional[builtins.str] = None,
        country: typing.Optional[builtins.str] = None,
        custom_attributes: typing.Optional[builtins.str] = None,
        department: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        division: typing.Optional[builtins.str] = None,
        email_address: typing.Optional[builtins.str] = None,
        employee_id: typing.Optional[builtins.str] = None,
        employee_number: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        fax: typing.Optional[builtins.str] = None,
        given_name: typing.Optional[builtins.str] = None,
        home_directory: typing.Optional[builtins.str] = None,
        home_drive: typing.Optional[builtins.str] = None,
        home_page: typing.Optional[builtins.str] = None,
        home_phone: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        initial_password: typing.Optional[builtins.str] = None,
        initials: typing.Optional[builtins.str] = None,
        mobile_phone: typing.Optional[builtins.str] = None,
        office: typing.Optional[builtins.str] = None,
        office_phone: typing.Optional[builtins.str] = None,
        organization: typing.Optional[builtins.str] = None,
        other_name: typing.Optional[builtins.str] = None,
        password_never_expires: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        po_box: typing.Optional[builtins.str] = None,
        postal_code: typing.Optional[builtins.str] = None,
        smart_card_logon_required: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        state: typing.Optional[builtins.str] = None,
        street_address: typing.Optional[builtins.str] = None,
        surname: typing.Optional[builtins.str] = None,
        title: typing.Optional[builtins.str] = None,
        trusted_for_delegation: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/ad/r/user ad_user} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param display_name: The Display Name of an Active Directory user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#display_name User#display_name}
        :param principal_name: The Principal Name of an Active Directory user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#principal_name User#principal_name}
        :param sam_account_name: The pre-win2k user logon name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#sam_account_name User#sam_account_name}
        :param cannot_change_password: If set to true, the user will not be allowed to change their password. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#cannot_change_password User#cannot_change_password}
        :param city: Specifies the user's town or city. This parameter sets the City property of a user object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#city User#city}
        :param company: Specifies the user's company. This parameter sets the Company property of a user object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#company User#company}
        :param container: A DN of the container object that will be holding the user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#container User#container}
        :param country: Specifies the country by setting the country code (refer to ISO 3166). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#country User#country}
        :param custom_attributes: JSON encoded map that represents key/value pairs for custom attributes. Please note that ``terraform import`` will not import these attributes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#custom_attributes User#custom_attributes}
        :param department: Specifies the user's department. This parameter sets the Department property of a user object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#department User#department}
        :param description: Specifies a description of the object. This parameter sets the value of the Description property for the user object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#description User#description}
        :param division: Specifies the user's division. This parameter sets the Division property of a user object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#division User#division}
        :param email_address: Specifies the user's e-mail address. This parameter sets the EmailAddress property of a user object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#email_address User#email_address}
        :param employee_id: Specifies the user's employee ID. This parameter sets the EmployeeID property of a user object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#employee_id User#employee_id}
        :param employee_number: Specifies the user's employee number. This parameter sets the EmployeeNumber property of a user object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#employee_number User#employee_number}
        :param enabled: If set to false, the user will be disabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#enabled User#enabled}
        :param fax: Specifies the user's fax phone number. This parameter sets the Fax property of a user object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#fax User#fax}
        :param given_name: Specifies the user's given name. This parameter sets the GivenName property of a user object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#given_name User#given_name}
        :param home_directory: Specifies a user's home directory. This parameter sets the HomeDirectory property of a user object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#home_directory User#home_directory}
        :param home_drive: Specifies a drive that is associated with the UNC path defined by the HomeDirectory property. The drive letter is specified as : where indicates the letter of the drive to associate. The must be a single, uppercase letter and the colon is required. This parameter sets the HomeDrive property of the user object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#home_drive User#home_drive}
        :param home_page: Specifies the URL of the home page of the object. This parameter sets the homePage property of a user object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#home_page User#home_page}
        :param home_phone: Specifies the user's home telephone number. This parameter sets the HomePhone property of a user object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#home_phone User#home_phone}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#id User#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param initial_password: The user's initial password. This will be set on creation but will *not* be enforced in subsequent plans. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#initial_password User#initial_password}
        :param initials: Specifies the initials that represent part of a user's name. Maximum 6 char. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#initials User#initials}
        :param mobile_phone: Specifies the user's mobile phone number. This parameter sets the MobilePhone property of a user object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#mobile_phone User#mobile_phone}
        :param office: Specifies the location of the user's office or place of business. This parameter sets the Office property of a user object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#office User#office}
        :param office_phone: Specifies the user's office telephone number. This parameter sets the OfficePhone property of a user object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#office_phone User#office_phone}
        :param organization: Specifies the user's organization. This parameter sets the Organization property of a user object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#organization User#organization}
        :param other_name: Specifies a name in addition to a user's given name and surname, such as the user's middle name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#other_name User#other_name}
        :param password_never_expires: If set to true, the password for this user will not expire. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#password_never_expires User#password_never_expires}
        :param po_box: Specifies the user's post office box number. This parameter sets the POBox property of a user object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#po_box User#po_box}
        :param postal_code: Specifies the user's postal code or zip code. This parameter sets the PostalCode property of a user object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#postal_code User#postal_code}
        :param smart_card_logon_required: If set to true, a smart card is required to logon. This parameter sets the SmartCardLoginRequired property for a user object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#smart_card_logon_required User#smart_card_logon_required}
        :param state: Specifies the user's or Organizational Unit's state or province. This parameter sets the State property of a user object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#state User#state}
        :param street_address: Specifies the user's street address. This parameter sets the StreetAddress property of a user object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#street_address User#street_address}
        :param surname: Specifies the user's last name or surname. This parameter sets the Surname property of a user object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#surname User#surname}
        :param title: Specifies the user's title. This parameter sets the Title property of a user object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#title User#title}
        :param trusted_for_delegation: If set to true, the user account is trusted for Kerberos delegation. A service that runs under an account that is trusted for Kerberos delegation can assume the identity of a client requesting the service. This parameter sets the TrustedForDelegation property of an account object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#trusted_for_delegation User#trusted_for_delegation}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__473ffba57bb63c2caebe785ba245a7b160473d25ed724f7c039cf15799d7751e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = UserConfig(
            display_name=display_name,
            principal_name=principal_name,
            sam_account_name=sam_account_name,
            cannot_change_password=cannot_change_password,
            city=city,
            company=company,
            container=container,
            country=country,
            custom_attributes=custom_attributes,
            department=department,
            description=description,
            division=division,
            email_address=email_address,
            employee_id=employee_id,
            employee_number=employee_number,
            enabled=enabled,
            fax=fax,
            given_name=given_name,
            home_directory=home_directory,
            home_drive=home_drive,
            home_page=home_page,
            home_phone=home_phone,
            id=id,
            initial_password=initial_password,
            initials=initials,
            mobile_phone=mobile_phone,
            office=office,
            office_phone=office_phone,
            organization=organization,
            other_name=other_name,
            password_never_expires=password_never_expires,
            po_box=po_box,
            postal_code=postal_code,
            smart_card_logon_required=smart_card_logon_required,
            state=state,
            street_address=street_address,
            surname=surname,
            title=title,
            trusted_for_delegation=trusted_for_delegation,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetCannotChangePassword")
    def reset_cannot_change_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCannotChangePassword", []))

    @jsii.member(jsii_name="resetCity")
    def reset_city(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCity", []))

    @jsii.member(jsii_name="resetCompany")
    def reset_company(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCompany", []))

    @jsii.member(jsii_name="resetContainer")
    def reset_container(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContainer", []))

    @jsii.member(jsii_name="resetCountry")
    def reset_country(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCountry", []))

    @jsii.member(jsii_name="resetCustomAttributes")
    def reset_custom_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomAttributes", []))

    @jsii.member(jsii_name="resetDepartment")
    def reset_department(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDepartment", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDivision")
    def reset_division(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDivision", []))

    @jsii.member(jsii_name="resetEmailAddress")
    def reset_email_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmailAddress", []))

    @jsii.member(jsii_name="resetEmployeeId")
    def reset_employee_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmployeeId", []))

    @jsii.member(jsii_name="resetEmployeeNumber")
    def reset_employee_number(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmployeeNumber", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetFax")
    def reset_fax(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFax", []))

    @jsii.member(jsii_name="resetGivenName")
    def reset_given_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGivenName", []))

    @jsii.member(jsii_name="resetHomeDirectory")
    def reset_home_directory(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHomeDirectory", []))

    @jsii.member(jsii_name="resetHomeDrive")
    def reset_home_drive(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHomeDrive", []))

    @jsii.member(jsii_name="resetHomePage")
    def reset_home_page(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHomePage", []))

    @jsii.member(jsii_name="resetHomePhone")
    def reset_home_phone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHomePhone", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInitialPassword")
    def reset_initial_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInitialPassword", []))

    @jsii.member(jsii_name="resetInitials")
    def reset_initials(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInitials", []))

    @jsii.member(jsii_name="resetMobilePhone")
    def reset_mobile_phone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMobilePhone", []))

    @jsii.member(jsii_name="resetOffice")
    def reset_office(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOffice", []))

    @jsii.member(jsii_name="resetOfficePhone")
    def reset_office_phone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOfficePhone", []))

    @jsii.member(jsii_name="resetOrganization")
    def reset_organization(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrganization", []))

    @jsii.member(jsii_name="resetOtherName")
    def reset_other_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOtherName", []))

    @jsii.member(jsii_name="resetPasswordNeverExpires")
    def reset_password_never_expires(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPasswordNeverExpires", []))

    @jsii.member(jsii_name="resetPoBox")
    def reset_po_box(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPoBox", []))

    @jsii.member(jsii_name="resetPostalCode")
    def reset_postal_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPostalCode", []))

    @jsii.member(jsii_name="resetSmartCardLogonRequired")
    def reset_smart_card_logon_required(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSmartCardLogonRequired", []))

    @jsii.member(jsii_name="resetState")
    def reset_state(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetState", []))

    @jsii.member(jsii_name="resetStreetAddress")
    def reset_street_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStreetAddress", []))

    @jsii.member(jsii_name="resetSurname")
    def reset_surname(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSurname", []))

    @jsii.member(jsii_name="resetTitle")
    def reset_title(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTitle", []))

    @jsii.member(jsii_name="resetTrustedForDelegation")
    def reset_trusted_for_delegation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTrustedForDelegation", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="dn")
    def dn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dn"))

    @builtins.property
    @jsii.member(jsii_name="sid")
    def sid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sid"))

    @builtins.property
    @jsii.member(jsii_name="cannotChangePasswordInput")
    def cannot_change_password_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "cannotChangePasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="cityInput")
    def city_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cityInput"))

    @builtins.property
    @jsii.member(jsii_name="companyInput")
    def company_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "companyInput"))

    @builtins.property
    @jsii.member(jsii_name="containerInput")
    def container_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "containerInput"))

    @builtins.property
    @jsii.member(jsii_name="countryInput")
    def country_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "countryInput"))

    @builtins.property
    @jsii.member(jsii_name="customAttributesInput")
    def custom_attributes_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customAttributesInput"))

    @builtins.property
    @jsii.member(jsii_name="departmentInput")
    def department_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "departmentInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="divisionInput")
    def division_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "divisionInput"))

    @builtins.property
    @jsii.member(jsii_name="emailAddressInput")
    def email_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emailAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="employeeIdInput")
    def employee_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "employeeIdInput"))

    @builtins.property
    @jsii.member(jsii_name="employeeNumberInput")
    def employee_number_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "employeeNumberInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="faxInput")
    def fax_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "faxInput"))

    @builtins.property
    @jsii.member(jsii_name="givenNameInput")
    def given_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "givenNameInput"))

    @builtins.property
    @jsii.member(jsii_name="homeDirectoryInput")
    def home_directory_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "homeDirectoryInput"))

    @builtins.property
    @jsii.member(jsii_name="homeDriveInput")
    def home_drive_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "homeDriveInput"))

    @builtins.property
    @jsii.member(jsii_name="homePageInput")
    def home_page_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "homePageInput"))

    @builtins.property
    @jsii.member(jsii_name="homePhoneInput")
    def home_phone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "homePhoneInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="initialPasswordInput")
    def initial_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "initialPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="initialsInput")
    def initials_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "initialsInput"))

    @builtins.property
    @jsii.member(jsii_name="mobilePhoneInput")
    def mobile_phone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mobilePhoneInput"))

    @builtins.property
    @jsii.member(jsii_name="officeInput")
    def office_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "officeInput"))

    @builtins.property
    @jsii.member(jsii_name="officePhoneInput")
    def office_phone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "officePhoneInput"))

    @builtins.property
    @jsii.member(jsii_name="organizationInput")
    def organization_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "organizationInput"))

    @builtins.property
    @jsii.member(jsii_name="otherNameInput")
    def other_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "otherNameInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordNeverExpiresInput")
    def password_never_expires_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "passwordNeverExpiresInput"))

    @builtins.property
    @jsii.member(jsii_name="poBoxInput")
    def po_box_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "poBoxInput"))

    @builtins.property
    @jsii.member(jsii_name="postalCodeInput")
    def postal_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "postalCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="principalNameInput")
    def principal_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "principalNameInput"))

    @builtins.property
    @jsii.member(jsii_name="samAccountNameInput")
    def sam_account_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "samAccountNameInput"))

    @builtins.property
    @jsii.member(jsii_name="smartCardLogonRequiredInput")
    def smart_card_logon_required_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "smartCardLogonRequiredInput"))

    @builtins.property
    @jsii.member(jsii_name="stateInput")
    def state_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stateInput"))

    @builtins.property
    @jsii.member(jsii_name="streetAddressInput")
    def street_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "streetAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="surnameInput")
    def surname_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "surnameInput"))

    @builtins.property
    @jsii.member(jsii_name="titleInput")
    def title_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "titleInput"))

    @builtins.property
    @jsii.member(jsii_name="trustedForDelegationInput")
    def trusted_for_delegation_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "trustedForDelegationInput"))

    @builtins.property
    @jsii.member(jsii_name="cannotChangePassword")
    def cannot_change_password(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "cannotChangePassword"))

    @cannot_change_password.setter
    def cannot_change_password(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a80b0f6ce5b581a874e9c3d470e5f07fe7dfc65ed7cfe8daf7c13716b0acff33)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cannotChangePassword", value)

    @builtins.property
    @jsii.member(jsii_name="city")
    def city(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "city"))

    @city.setter
    def city(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6044f40a462f4b68a212d0503ed3a55e9c3c10caffbb9e7541f9468d2064c9ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "city", value)

    @builtins.property
    @jsii.member(jsii_name="company")
    def company(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "company"))

    @company.setter
    def company(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e57a6332148c139e7a6a308f9455fc6e461210f72d9f3da19b27ca46c2ade93a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "company", value)

    @builtins.property
    @jsii.member(jsii_name="container")
    def container(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "container"))

    @container.setter
    def container(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52f9fdbb05d63b3b67b65f0c6b6d109386da396cdb28cdcb92f85bab3ec835a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "container", value)

    @builtins.property
    @jsii.member(jsii_name="country")
    def country(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "country"))

    @country.setter
    def country(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9996abdf62cc55be34d734c3fa862b415aa7eb39d626715072f49bff5bd32007)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "country", value)

    @builtins.property
    @jsii.member(jsii_name="customAttributes")
    def custom_attributes(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customAttributes"))

    @custom_attributes.setter
    def custom_attributes(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__387fad2df257a20a5f2d28314203a64ed4531acd5bee7c774a2df26ab5c8e2f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customAttributes", value)

    @builtins.property
    @jsii.member(jsii_name="department")
    def department(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "department"))

    @department.setter
    def department(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b420b50163dc2e0784b562e10e99875aaa5179401a9c9a67c9c1c3b3750e78d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "department", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf8979c91a377b03f3e3fc2ac774a8023f7c245d121e3b8e7475ba3983549415)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0fb77e8cb8085999ac46c0d4d94de48ffb6df389a8bab7379335db6aba62f0bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="division")
    def division(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "division"))

    @division.setter
    def division(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea8eeb50135a607041a251f1783727d551020fbb241814afe1e9496de1cae9c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "division", value)

    @builtins.property
    @jsii.member(jsii_name="emailAddress")
    def email_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "emailAddress"))

    @email_address.setter
    def email_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73ac71d5d43dfe36b997b331a2d5425ea897346a5166f3a73471bea028ca013b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emailAddress", value)

    @builtins.property
    @jsii.member(jsii_name="employeeId")
    def employee_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "employeeId"))

    @employee_id.setter
    def employee_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cda9a723319432c8ca30859fc5eeb1edabdf136b6853ec4dba974392b00de2db)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "employeeId", value)

    @builtins.property
    @jsii.member(jsii_name="employeeNumber")
    def employee_number(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "employeeNumber"))

    @employee_number.setter
    def employee_number(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd32431072e5d029c6176b7af933e736e0d885b0f3c891a9cf6a1369ca542e4c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "employeeNumber", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__422e5e197ad6b8ea3582b4ecae549442a2b58144b8ee69365a65c50b4289b1e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="fax")
    def fax(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fax"))

    @fax.setter
    def fax(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5e06ef152c6ce42f8ad1b4f3af915717a8b4b8b3843bee80b5f358d1ae3a9ba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fax", value)

    @builtins.property
    @jsii.member(jsii_name="givenName")
    def given_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "givenName"))

    @given_name.setter
    def given_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fea66ff8e04bd87ae9900ee2c1c6ddd8393114150e85dd954291998c7a77034b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "givenName", value)

    @builtins.property
    @jsii.member(jsii_name="homeDirectory")
    def home_directory(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "homeDirectory"))

    @home_directory.setter
    def home_directory(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fdd828bbaf59cad241171d832b96dc4003b28343ec13577c41816ff7cb15f1f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "homeDirectory", value)

    @builtins.property
    @jsii.member(jsii_name="homeDrive")
    def home_drive(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "homeDrive"))

    @home_drive.setter
    def home_drive(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f0e631244b778feb80aaa48870422339fc550591683f7ea1ef04da41c397df5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "homeDrive", value)

    @builtins.property
    @jsii.member(jsii_name="homePage")
    def home_page(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "homePage"))

    @home_page.setter
    def home_page(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2f420f046d1064eca3ac697ee5ddded8df754e4c82fea7cf2f000338a965836)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "homePage", value)

    @builtins.property
    @jsii.member(jsii_name="homePhone")
    def home_phone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "homePhone"))

    @home_phone.setter
    def home_phone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d8e494bae8a6c74947cc18a389eda999fbdd2cdf14c447c793fae1651a445c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "homePhone", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28be6157285c1c2f7a65c2dc0dd2f53c28a7308fb51a09a20517abb850787b13)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="initialPassword")
    def initial_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "initialPassword"))

    @initial_password.setter
    def initial_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c2e4e612570fc30ff46f9f1c8cc5e6602ec3b79534d2b06d3e370fdf59c4837)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "initialPassword", value)

    @builtins.property
    @jsii.member(jsii_name="initials")
    def initials(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "initials"))

    @initials.setter
    def initials(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53e79608985ecfebc1e3e4f6b2f137501ad0f29e5547fe73d19441347c42d6c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "initials", value)

    @builtins.property
    @jsii.member(jsii_name="mobilePhone")
    def mobile_phone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mobilePhone"))

    @mobile_phone.setter
    def mobile_phone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3991856d796530ab90dbacdfb50ef1f511f084e5ad62a11a6f6641a238d1c2d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mobilePhone", value)

    @builtins.property
    @jsii.member(jsii_name="office")
    def office(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "office"))

    @office.setter
    def office(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49227137da503425623b40255a56329f4918c71be9f639edaabc8770321d3030)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "office", value)

    @builtins.property
    @jsii.member(jsii_name="officePhone")
    def office_phone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "officePhone"))

    @office_phone.setter
    def office_phone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07643c31c44cb70e9234c0bf8d668ac540b140e3baba4eea67809eac550c1b7f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "officePhone", value)

    @builtins.property
    @jsii.member(jsii_name="organization")
    def organization(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "organization"))

    @organization.setter
    def organization(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b73761e28217234ae21d304ba5e8027f732de5c9d7ae7413111b96b294ad838c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "organization", value)

    @builtins.property
    @jsii.member(jsii_name="otherName")
    def other_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "otherName"))

    @other_name.setter
    def other_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eeedd0215f17fb33c9a520672783f3af45d49a3553f5129306ec3cb53c41253d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "otherName", value)

    @builtins.property
    @jsii.member(jsii_name="passwordNeverExpires")
    def password_never_expires(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "passwordNeverExpires"))

    @password_never_expires.setter
    def password_never_expires(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5689c19c0b10b06dc569de623a45445d790f758441d486450f52bca63fdee8c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "passwordNeverExpires", value)

    @builtins.property
    @jsii.member(jsii_name="poBox")
    def po_box(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "poBox"))

    @po_box.setter
    def po_box(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8b46d9276ab8c343bb4880a6a9fd9643725e140eb2c167b48bc07663e493e5b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "poBox", value)

    @builtins.property
    @jsii.member(jsii_name="postalCode")
    def postal_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "postalCode"))

    @postal_code.setter
    def postal_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc5f98ee2364e632c1e3ed707c157640cef93ea8dd2d55f503fe19364fbc6543)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "postalCode", value)

    @builtins.property
    @jsii.member(jsii_name="principalName")
    def principal_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "principalName"))

    @principal_name.setter
    def principal_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32f038979a6337f9b38df3d1a3d5438b2dc7280b0d5369a6201cb4339f38143f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "principalName", value)

    @builtins.property
    @jsii.member(jsii_name="samAccountName")
    def sam_account_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "samAccountName"))

    @sam_account_name.setter
    def sam_account_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3d638df0a873e3095758d5ad4ffa01b3edcb5f44ae27fc513003085d3e2b2ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "samAccountName", value)

    @builtins.property
    @jsii.member(jsii_name="smartCardLogonRequired")
    def smart_card_logon_required(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "smartCardLogonRequired"))

    @smart_card_logon_required.setter
    def smart_card_logon_required(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__740b36ae422cd72356e8d6eb808fe52a498db27f69735b74efc473a420518bc0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "smartCardLogonRequired", value)

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @state.setter
    def state(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3bb264b1fc0e0e719c27479ffbacc04e31194ccb2fb1a47c47d0e7c96b436d3a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "state", value)

    @builtins.property
    @jsii.member(jsii_name="streetAddress")
    def street_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "streetAddress"))

    @street_address.setter
    def street_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c8306678b0977af6eff22f4c3444e82512015f8ee341c7e309043b67afe1cd5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "streetAddress", value)

    @builtins.property
    @jsii.member(jsii_name="surname")
    def surname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "surname"))

    @surname.setter
    def surname(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07901f2d9e28b9cf97ba1de0fd551cd7470bb340d3e3381ecae125ce6332ca5a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "surname", value)

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @title.setter
    def title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d365578f9b936f5c57d5e0d215e726f88962a91d6bd4768e1f23973848577b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value)

    @builtins.property
    @jsii.member(jsii_name="trustedForDelegation")
    def trusted_for_delegation(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "trustedForDelegation"))

    @trusted_for_delegation.setter
    def trusted_for_delegation(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a5e2234f49b93d8cb4e4170c92146697fdd231bd8fb74c8fd566ad5e3a5aa54)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "trustedForDelegation", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-ad.user.UserConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "display_name": "displayName",
        "principal_name": "principalName",
        "sam_account_name": "samAccountName",
        "cannot_change_password": "cannotChangePassword",
        "city": "city",
        "company": "company",
        "container": "container",
        "country": "country",
        "custom_attributes": "customAttributes",
        "department": "department",
        "description": "description",
        "division": "division",
        "email_address": "emailAddress",
        "employee_id": "employeeId",
        "employee_number": "employeeNumber",
        "enabled": "enabled",
        "fax": "fax",
        "given_name": "givenName",
        "home_directory": "homeDirectory",
        "home_drive": "homeDrive",
        "home_page": "homePage",
        "home_phone": "homePhone",
        "id": "id",
        "initial_password": "initialPassword",
        "initials": "initials",
        "mobile_phone": "mobilePhone",
        "office": "office",
        "office_phone": "officePhone",
        "organization": "organization",
        "other_name": "otherName",
        "password_never_expires": "passwordNeverExpires",
        "po_box": "poBox",
        "postal_code": "postalCode",
        "smart_card_logon_required": "smartCardLogonRequired",
        "state": "state",
        "street_address": "streetAddress",
        "surname": "surname",
        "title": "title",
        "trusted_for_delegation": "trustedForDelegation",
    },
)
class UserConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        display_name: builtins.str,
        principal_name: builtins.str,
        sam_account_name: builtins.str,
        cannot_change_password: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        city: typing.Optional[builtins.str] = None,
        company: typing.Optional[builtins.str] = None,
        container: typing.Optional[builtins.str] = None,
        country: typing.Optional[builtins.str] = None,
        custom_attributes: typing.Optional[builtins.str] = None,
        department: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        division: typing.Optional[builtins.str] = None,
        email_address: typing.Optional[builtins.str] = None,
        employee_id: typing.Optional[builtins.str] = None,
        employee_number: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        fax: typing.Optional[builtins.str] = None,
        given_name: typing.Optional[builtins.str] = None,
        home_directory: typing.Optional[builtins.str] = None,
        home_drive: typing.Optional[builtins.str] = None,
        home_page: typing.Optional[builtins.str] = None,
        home_phone: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        initial_password: typing.Optional[builtins.str] = None,
        initials: typing.Optional[builtins.str] = None,
        mobile_phone: typing.Optional[builtins.str] = None,
        office: typing.Optional[builtins.str] = None,
        office_phone: typing.Optional[builtins.str] = None,
        organization: typing.Optional[builtins.str] = None,
        other_name: typing.Optional[builtins.str] = None,
        password_never_expires: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        po_box: typing.Optional[builtins.str] = None,
        postal_code: typing.Optional[builtins.str] = None,
        smart_card_logon_required: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        state: typing.Optional[builtins.str] = None,
        street_address: typing.Optional[builtins.str] = None,
        surname: typing.Optional[builtins.str] = None,
        title: typing.Optional[builtins.str] = None,
        trusted_for_delegation: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param display_name: The Display Name of an Active Directory user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#display_name User#display_name}
        :param principal_name: The Principal Name of an Active Directory user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#principal_name User#principal_name}
        :param sam_account_name: The pre-win2k user logon name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#sam_account_name User#sam_account_name}
        :param cannot_change_password: If set to true, the user will not be allowed to change their password. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#cannot_change_password User#cannot_change_password}
        :param city: Specifies the user's town or city. This parameter sets the City property of a user object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#city User#city}
        :param company: Specifies the user's company. This parameter sets the Company property of a user object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#company User#company}
        :param container: A DN of the container object that will be holding the user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#container User#container}
        :param country: Specifies the country by setting the country code (refer to ISO 3166). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#country User#country}
        :param custom_attributes: JSON encoded map that represents key/value pairs for custom attributes. Please note that ``terraform import`` will not import these attributes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#custom_attributes User#custom_attributes}
        :param department: Specifies the user's department. This parameter sets the Department property of a user object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#department User#department}
        :param description: Specifies a description of the object. This parameter sets the value of the Description property for the user object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#description User#description}
        :param division: Specifies the user's division. This parameter sets the Division property of a user object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#division User#division}
        :param email_address: Specifies the user's e-mail address. This parameter sets the EmailAddress property of a user object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#email_address User#email_address}
        :param employee_id: Specifies the user's employee ID. This parameter sets the EmployeeID property of a user object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#employee_id User#employee_id}
        :param employee_number: Specifies the user's employee number. This parameter sets the EmployeeNumber property of a user object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#employee_number User#employee_number}
        :param enabled: If set to false, the user will be disabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#enabled User#enabled}
        :param fax: Specifies the user's fax phone number. This parameter sets the Fax property of a user object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#fax User#fax}
        :param given_name: Specifies the user's given name. This parameter sets the GivenName property of a user object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#given_name User#given_name}
        :param home_directory: Specifies a user's home directory. This parameter sets the HomeDirectory property of a user object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#home_directory User#home_directory}
        :param home_drive: Specifies a drive that is associated with the UNC path defined by the HomeDirectory property. The drive letter is specified as : where indicates the letter of the drive to associate. The must be a single, uppercase letter and the colon is required. This parameter sets the HomeDrive property of the user object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#home_drive User#home_drive}
        :param home_page: Specifies the URL of the home page of the object. This parameter sets the homePage property of a user object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#home_page User#home_page}
        :param home_phone: Specifies the user's home telephone number. This parameter sets the HomePhone property of a user object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#home_phone User#home_phone}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#id User#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param initial_password: The user's initial password. This will be set on creation but will *not* be enforced in subsequent plans. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#initial_password User#initial_password}
        :param initials: Specifies the initials that represent part of a user's name. Maximum 6 char. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#initials User#initials}
        :param mobile_phone: Specifies the user's mobile phone number. This parameter sets the MobilePhone property of a user object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#mobile_phone User#mobile_phone}
        :param office: Specifies the location of the user's office or place of business. This parameter sets the Office property of a user object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#office User#office}
        :param office_phone: Specifies the user's office telephone number. This parameter sets the OfficePhone property of a user object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#office_phone User#office_phone}
        :param organization: Specifies the user's organization. This parameter sets the Organization property of a user object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#organization User#organization}
        :param other_name: Specifies a name in addition to a user's given name and surname, such as the user's middle name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#other_name User#other_name}
        :param password_never_expires: If set to true, the password for this user will not expire. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#password_never_expires User#password_never_expires}
        :param po_box: Specifies the user's post office box number. This parameter sets the POBox property of a user object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#po_box User#po_box}
        :param postal_code: Specifies the user's postal code or zip code. This parameter sets the PostalCode property of a user object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#postal_code User#postal_code}
        :param smart_card_logon_required: If set to true, a smart card is required to logon. This parameter sets the SmartCardLoginRequired property for a user object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#smart_card_logon_required User#smart_card_logon_required}
        :param state: Specifies the user's or Organizational Unit's state or province. This parameter sets the State property of a user object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#state User#state}
        :param street_address: Specifies the user's street address. This parameter sets the StreetAddress property of a user object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#street_address User#street_address}
        :param surname: Specifies the user's last name or surname. This parameter sets the Surname property of a user object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#surname User#surname}
        :param title: Specifies the user's title. This parameter sets the Title property of a user object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#title User#title}
        :param trusted_for_delegation: If set to true, the user account is trusted for Kerberos delegation. A service that runs under an account that is trusted for Kerberos delegation can assume the identity of a client requesting the service. This parameter sets the TrustedForDelegation property of an account object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#trusted_for_delegation User#trusted_for_delegation}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf50c00353f44d35109a932cd7f15e60f3ccf4d10d6b4806022ab9ec39ddc3da)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument principal_name", value=principal_name, expected_type=type_hints["principal_name"])
            check_type(argname="argument sam_account_name", value=sam_account_name, expected_type=type_hints["sam_account_name"])
            check_type(argname="argument cannot_change_password", value=cannot_change_password, expected_type=type_hints["cannot_change_password"])
            check_type(argname="argument city", value=city, expected_type=type_hints["city"])
            check_type(argname="argument company", value=company, expected_type=type_hints["company"])
            check_type(argname="argument container", value=container, expected_type=type_hints["container"])
            check_type(argname="argument country", value=country, expected_type=type_hints["country"])
            check_type(argname="argument custom_attributes", value=custom_attributes, expected_type=type_hints["custom_attributes"])
            check_type(argname="argument department", value=department, expected_type=type_hints["department"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument division", value=division, expected_type=type_hints["division"])
            check_type(argname="argument email_address", value=email_address, expected_type=type_hints["email_address"])
            check_type(argname="argument employee_id", value=employee_id, expected_type=type_hints["employee_id"])
            check_type(argname="argument employee_number", value=employee_number, expected_type=type_hints["employee_number"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument fax", value=fax, expected_type=type_hints["fax"])
            check_type(argname="argument given_name", value=given_name, expected_type=type_hints["given_name"])
            check_type(argname="argument home_directory", value=home_directory, expected_type=type_hints["home_directory"])
            check_type(argname="argument home_drive", value=home_drive, expected_type=type_hints["home_drive"])
            check_type(argname="argument home_page", value=home_page, expected_type=type_hints["home_page"])
            check_type(argname="argument home_phone", value=home_phone, expected_type=type_hints["home_phone"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument initial_password", value=initial_password, expected_type=type_hints["initial_password"])
            check_type(argname="argument initials", value=initials, expected_type=type_hints["initials"])
            check_type(argname="argument mobile_phone", value=mobile_phone, expected_type=type_hints["mobile_phone"])
            check_type(argname="argument office", value=office, expected_type=type_hints["office"])
            check_type(argname="argument office_phone", value=office_phone, expected_type=type_hints["office_phone"])
            check_type(argname="argument organization", value=organization, expected_type=type_hints["organization"])
            check_type(argname="argument other_name", value=other_name, expected_type=type_hints["other_name"])
            check_type(argname="argument password_never_expires", value=password_never_expires, expected_type=type_hints["password_never_expires"])
            check_type(argname="argument po_box", value=po_box, expected_type=type_hints["po_box"])
            check_type(argname="argument postal_code", value=postal_code, expected_type=type_hints["postal_code"])
            check_type(argname="argument smart_card_logon_required", value=smart_card_logon_required, expected_type=type_hints["smart_card_logon_required"])
            check_type(argname="argument state", value=state, expected_type=type_hints["state"])
            check_type(argname="argument street_address", value=street_address, expected_type=type_hints["street_address"])
            check_type(argname="argument surname", value=surname, expected_type=type_hints["surname"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
            check_type(argname="argument trusted_for_delegation", value=trusted_for_delegation, expected_type=type_hints["trusted_for_delegation"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "display_name": display_name,
            "principal_name": principal_name,
            "sam_account_name": sam_account_name,
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
        if cannot_change_password is not None:
            self._values["cannot_change_password"] = cannot_change_password
        if city is not None:
            self._values["city"] = city
        if company is not None:
            self._values["company"] = company
        if container is not None:
            self._values["container"] = container
        if country is not None:
            self._values["country"] = country
        if custom_attributes is not None:
            self._values["custom_attributes"] = custom_attributes
        if department is not None:
            self._values["department"] = department
        if description is not None:
            self._values["description"] = description
        if division is not None:
            self._values["division"] = division
        if email_address is not None:
            self._values["email_address"] = email_address
        if employee_id is not None:
            self._values["employee_id"] = employee_id
        if employee_number is not None:
            self._values["employee_number"] = employee_number
        if enabled is not None:
            self._values["enabled"] = enabled
        if fax is not None:
            self._values["fax"] = fax
        if given_name is not None:
            self._values["given_name"] = given_name
        if home_directory is not None:
            self._values["home_directory"] = home_directory
        if home_drive is not None:
            self._values["home_drive"] = home_drive
        if home_page is not None:
            self._values["home_page"] = home_page
        if home_phone is not None:
            self._values["home_phone"] = home_phone
        if id is not None:
            self._values["id"] = id
        if initial_password is not None:
            self._values["initial_password"] = initial_password
        if initials is not None:
            self._values["initials"] = initials
        if mobile_phone is not None:
            self._values["mobile_phone"] = mobile_phone
        if office is not None:
            self._values["office"] = office
        if office_phone is not None:
            self._values["office_phone"] = office_phone
        if organization is not None:
            self._values["organization"] = organization
        if other_name is not None:
            self._values["other_name"] = other_name
        if password_never_expires is not None:
            self._values["password_never_expires"] = password_never_expires
        if po_box is not None:
            self._values["po_box"] = po_box
        if postal_code is not None:
            self._values["postal_code"] = postal_code
        if smart_card_logon_required is not None:
            self._values["smart_card_logon_required"] = smart_card_logon_required
        if state is not None:
            self._values["state"] = state
        if street_address is not None:
            self._values["street_address"] = street_address
        if surname is not None:
            self._values["surname"] = surname
        if title is not None:
            self._values["title"] = title
        if trusted_for_delegation is not None:
            self._values["trusted_for_delegation"] = trusted_for_delegation

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
    def display_name(self) -> builtins.str:
        '''The Display Name of an Active Directory user.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#display_name User#display_name}
        '''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def principal_name(self) -> builtins.str:
        '''The Principal Name of an Active Directory user.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#principal_name User#principal_name}
        '''
        result = self._values.get("principal_name")
        assert result is not None, "Required property 'principal_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sam_account_name(self) -> builtins.str:
        '''The pre-win2k user logon name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#sam_account_name User#sam_account_name}
        '''
        result = self._values.get("sam_account_name")
        assert result is not None, "Required property 'sam_account_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cannot_change_password(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''If set to true, the user will not be allowed to change their password.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#cannot_change_password User#cannot_change_password}
        '''
        result = self._values.get("cannot_change_password")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def city(self) -> typing.Optional[builtins.str]:
        '''Specifies the user's town or city. This parameter sets the City property of a user object.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#city User#city}
        '''
        result = self._values.get("city")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def company(self) -> typing.Optional[builtins.str]:
        '''Specifies the user's company. This parameter sets the Company property of a user object.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#company User#company}
        '''
        result = self._values.get("company")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def container(self) -> typing.Optional[builtins.str]:
        '''A DN of the container object that will be holding the user.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#container User#container}
        '''
        result = self._values.get("container")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def country(self) -> typing.Optional[builtins.str]:
        '''Specifies the country by setting the country code (refer to ISO 3166).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#country User#country}
        '''
        result = self._values.get("country")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_attributes(self) -> typing.Optional[builtins.str]:
        '''JSON encoded map that represents key/value pairs for custom attributes.

        Please note that ``terraform import`` will not import these attributes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#custom_attributes User#custom_attributes}
        '''
        result = self._values.get("custom_attributes")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def department(self) -> typing.Optional[builtins.str]:
        '''Specifies the user's department. This parameter sets the Department property of a user object.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#department User#department}
        '''
        result = self._values.get("department")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Specifies a description of the object. This parameter sets the value of the Description property for the user object.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#description User#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def division(self) -> typing.Optional[builtins.str]:
        '''Specifies the user's division. This parameter sets the Division property of a user object.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#division User#division}
        '''
        result = self._values.get("division")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def email_address(self) -> typing.Optional[builtins.str]:
        '''Specifies the user's e-mail address. This parameter sets the EmailAddress property of a user object.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#email_address User#email_address}
        '''
        result = self._values.get("email_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def employee_id(self) -> typing.Optional[builtins.str]:
        '''Specifies the user's employee ID. This parameter sets the EmployeeID property of a user object.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#employee_id User#employee_id}
        '''
        result = self._values.get("employee_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def employee_number(self) -> typing.Optional[builtins.str]:
        '''Specifies the user's employee number. This parameter sets the EmployeeNumber property of a user object.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#employee_number User#employee_number}
        '''
        result = self._values.get("employee_number")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''If set to false, the user will be disabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#enabled User#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def fax(self) -> typing.Optional[builtins.str]:
        '''Specifies the user's fax phone number. This parameter sets the Fax property of a user object.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#fax User#fax}
        '''
        result = self._values.get("fax")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def given_name(self) -> typing.Optional[builtins.str]:
        '''Specifies the user's given name. This parameter sets the GivenName property of a user object.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#given_name User#given_name}
        '''
        result = self._values.get("given_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def home_directory(self) -> typing.Optional[builtins.str]:
        '''Specifies a user's home directory. This parameter sets the HomeDirectory property of a user object.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#home_directory User#home_directory}
        '''
        result = self._values.get("home_directory")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def home_drive(self) -> typing.Optional[builtins.str]:
        '''Specifies a drive that is associated with the UNC path defined by the HomeDirectory property.

        The drive letter is specified as : where  indicates the letter of the drive to associate. The  must be a single, uppercase letter and the colon is required. This parameter sets the HomeDrive property of the user object.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#home_drive User#home_drive}
        '''
        result = self._values.get("home_drive")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def home_page(self) -> typing.Optional[builtins.str]:
        '''Specifies the URL of the home page of the object.

        This parameter sets the homePage property of a user object.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#home_page User#home_page}
        '''
        result = self._values.get("home_page")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def home_phone(self) -> typing.Optional[builtins.str]:
        '''Specifies the user's home telephone number. This parameter sets the HomePhone property of a user object.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#home_phone User#home_phone}
        '''
        result = self._values.get("home_phone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#id User#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def initial_password(self) -> typing.Optional[builtins.str]:
        '''The user's initial password. This will be set on creation but will *not* be enforced in subsequent plans.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#initial_password User#initial_password}
        '''
        result = self._values.get("initial_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def initials(self) -> typing.Optional[builtins.str]:
        '''Specifies the initials that represent part of a user's name. Maximum 6 char.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#initials User#initials}
        '''
        result = self._values.get("initials")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mobile_phone(self) -> typing.Optional[builtins.str]:
        '''Specifies the user's mobile phone number. This parameter sets the MobilePhone property of a user object.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#mobile_phone User#mobile_phone}
        '''
        result = self._values.get("mobile_phone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def office(self) -> typing.Optional[builtins.str]:
        '''Specifies the location of the user's office or place of business.

        This parameter sets the Office property of a user object.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#office User#office}
        '''
        result = self._values.get("office")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def office_phone(self) -> typing.Optional[builtins.str]:
        '''Specifies the user's office telephone number. This parameter sets the OfficePhone property of a user object.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#office_phone User#office_phone}
        '''
        result = self._values.get("office_phone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def organization(self) -> typing.Optional[builtins.str]:
        '''Specifies the user's organization. This parameter sets the Organization property of a user object.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#organization User#organization}
        '''
        result = self._values.get("organization")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def other_name(self) -> typing.Optional[builtins.str]:
        '''Specifies a name in addition to a user's given name and surname, such as the user's middle name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#other_name User#other_name}
        '''
        result = self._values.get("other_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def password_never_expires(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''If set to true, the password for this user will not expire.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#password_never_expires User#password_never_expires}
        '''
        result = self._values.get("password_never_expires")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def po_box(self) -> typing.Optional[builtins.str]:
        '''Specifies the user's post office box number. This parameter sets the POBox property of a user object.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#po_box User#po_box}
        '''
        result = self._values.get("po_box")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def postal_code(self) -> typing.Optional[builtins.str]:
        '''Specifies the user's postal code or zip code. This parameter sets the PostalCode property of a user object.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#postal_code User#postal_code}
        '''
        result = self._values.get("postal_code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def smart_card_logon_required(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''If set to true, a smart card is required to logon.

        This parameter sets the SmartCardLoginRequired property for a user object.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#smart_card_logon_required User#smart_card_logon_required}
        '''
        result = self._values.get("smart_card_logon_required")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def state(self) -> typing.Optional[builtins.str]:
        '''Specifies the user's or Organizational Unit's state or province. This parameter sets the State property of a user object.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#state User#state}
        '''
        result = self._values.get("state")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def street_address(self) -> typing.Optional[builtins.str]:
        '''Specifies the user's street address. This parameter sets the StreetAddress property of a user object.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#street_address User#street_address}
        '''
        result = self._values.get("street_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def surname(self) -> typing.Optional[builtins.str]:
        '''Specifies the user's last name or surname. This parameter sets the Surname property of a user object.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#surname User#surname}
        '''
        result = self._values.get("surname")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def title(self) -> typing.Optional[builtins.str]:
        '''Specifies the user's title. This parameter sets the Title property of a user object.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#title User#title}
        '''
        result = self._values.get("title")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def trusted_for_delegation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''If set to true, the user account is trusted for Kerberos delegation.

        A service that runs under an account that is trusted for Kerberos delegation can assume the identity of a client requesting the service. This parameter sets the TrustedForDelegation property of an account object.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad/r/user#trusted_for_delegation User#trusted_for_delegation}
        '''
        result = self._values.get("trusted_for_delegation")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "User",
    "UserConfig",
]

publication.publish()

def _typecheckingstub__473ffba57bb63c2caebe785ba245a7b160473d25ed724f7c039cf15799d7751e(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    display_name: builtins.str,
    principal_name: builtins.str,
    sam_account_name: builtins.str,
    cannot_change_password: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    city: typing.Optional[builtins.str] = None,
    company: typing.Optional[builtins.str] = None,
    container: typing.Optional[builtins.str] = None,
    country: typing.Optional[builtins.str] = None,
    custom_attributes: typing.Optional[builtins.str] = None,
    department: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    division: typing.Optional[builtins.str] = None,
    email_address: typing.Optional[builtins.str] = None,
    employee_id: typing.Optional[builtins.str] = None,
    employee_number: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    fax: typing.Optional[builtins.str] = None,
    given_name: typing.Optional[builtins.str] = None,
    home_directory: typing.Optional[builtins.str] = None,
    home_drive: typing.Optional[builtins.str] = None,
    home_page: typing.Optional[builtins.str] = None,
    home_phone: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    initial_password: typing.Optional[builtins.str] = None,
    initials: typing.Optional[builtins.str] = None,
    mobile_phone: typing.Optional[builtins.str] = None,
    office: typing.Optional[builtins.str] = None,
    office_phone: typing.Optional[builtins.str] = None,
    organization: typing.Optional[builtins.str] = None,
    other_name: typing.Optional[builtins.str] = None,
    password_never_expires: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    po_box: typing.Optional[builtins.str] = None,
    postal_code: typing.Optional[builtins.str] = None,
    smart_card_logon_required: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    state: typing.Optional[builtins.str] = None,
    street_address: typing.Optional[builtins.str] = None,
    surname: typing.Optional[builtins.str] = None,
    title: typing.Optional[builtins.str] = None,
    trusted_for_delegation: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
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

def _typecheckingstub__a80b0f6ce5b581a874e9c3d470e5f07fe7dfc65ed7cfe8daf7c13716b0acff33(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6044f40a462f4b68a212d0503ed3a55e9c3c10caffbb9e7541f9468d2064c9ce(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e57a6332148c139e7a6a308f9455fc6e461210f72d9f3da19b27ca46c2ade93a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52f9fdbb05d63b3b67b65f0c6b6d109386da396cdb28cdcb92f85bab3ec835a2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9996abdf62cc55be34d734c3fa862b415aa7eb39d626715072f49bff5bd32007(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__387fad2df257a20a5f2d28314203a64ed4531acd5bee7c774a2df26ab5c8e2f8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b420b50163dc2e0784b562e10e99875aaa5179401a9c9a67c9c1c3b3750e78d2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf8979c91a377b03f3e3fc2ac774a8023f7c245d121e3b8e7475ba3983549415(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fb77e8cb8085999ac46c0d4d94de48ffb6df389a8bab7379335db6aba62f0bb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea8eeb50135a607041a251f1783727d551020fbb241814afe1e9496de1cae9c6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73ac71d5d43dfe36b997b331a2d5425ea897346a5166f3a73471bea028ca013b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cda9a723319432c8ca30859fc5eeb1edabdf136b6853ec4dba974392b00de2db(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd32431072e5d029c6176b7af933e736e0d885b0f3c891a9cf6a1369ca542e4c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__422e5e197ad6b8ea3582b4ecae549442a2b58144b8ee69365a65c50b4289b1e1(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5e06ef152c6ce42f8ad1b4f3af915717a8b4b8b3843bee80b5f358d1ae3a9ba(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fea66ff8e04bd87ae9900ee2c1c6ddd8393114150e85dd954291998c7a77034b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fdd828bbaf59cad241171d832b96dc4003b28343ec13577c41816ff7cb15f1f2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f0e631244b778feb80aaa48870422339fc550591683f7ea1ef04da41c397df5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2f420f046d1064eca3ac697ee5ddded8df754e4c82fea7cf2f000338a965836(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d8e494bae8a6c74947cc18a389eda999fbdd2cdf14c447c793fae1651a445c2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28be6157285c1c2f7a65c2dc0dd2f53c28a7308fb51a09a20517abb850787b13(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c2e4e612570fc30ff46f9f1c8cc5e6602ec3b79534d2b06d3e370fdf59c4837(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53e79608985ecfebc1e3e4f6b2f137501ad0f29e5547fe73d19441347c42d6c9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3991856d796530ab90dbacdfb50ef1f511f084e5ad62a11a6f6641a238d1c2d6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49227137da503425623b40255a56329f4918c71be9f639edaabc8770321d3030(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07643c31c44cb70e9234c0bf8d668ac540b140e3baba4eea67809eac550c1b7f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b73761e28217234ae21d304ba5e8027f732de5c9d7ae7413111b96b294ad838c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eeedd0215f17fb33c9a520672783f3af45d49a3553f5129306ec3cb53c41253d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5689c19c0b10b06dc569de623a45445d790f758441d486450f52bca63fdee8c(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8b46d9276ab8c343bb4880a6a9fd9643725e140eb2c167b48bc07663e493e5b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc5f98ee2364e632c1e3ed707c157640cef93ea8dd2d55f503fe19364fbc6543(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32f038979a6337f9b38df3d1a3d5438b2dc7280b0d5369a6201cb4339f38143f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3d638df0a873e3095758d5ad4ffa01b3edcb5f44ae27fc513003085d3e2b2ac(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__740b36ae422cd72356e8d6eb808fe52a498db27f69735b74efc473a420518bc0(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3bb264b1fc0e0e719c27479ffbacc04e31194ccb2fb1a47c47d0e7c96b436d3a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c8306678b0977af6eff22f4c3444e82512015f8ee341c7e309043b67afe1cd5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07901f2d9e28b9cf97ba1de0fd551cd7470bb340d3e3381ecae125ce6332ca5a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d365578f9b936f5c57d5e0d215e726f88962a91d6bd4768e1f23973848577b9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a5e2234f49b93d8cb4e4170c92146697fdd231bd8fb74c8fd566ad5e3a5aa54(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf50c00353f44d35109a932cd7f15e60f3ccf4d10d6b4806022ab9ec39ddc3da(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    display_name: builtins.str,
    principal_name: builtins.str,
    sam_account_name: builtins.str,
    cannot_change_password: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    city: typing.Optional[builtins.str] = None,
    company: typing.Optional[builtins.str] = None,
    container: typing.Optional[builtins.str] = None,
    country: typing.Optional[builtins.str] = None,
    custom_attributes: typing.Optional[builtins.str] = None,
    department: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    division: typing.Optional[builtins.str] = None,
    email_address: typing.Optional[builtins.str] = None,
    employee_id: typing.Optional[builtins.str] = None,
    employee_number: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    fax: typing.Optional[builtins.str] = None,
    given_name: typing.Optional[builtins.str] = None,
    home_directory: typing.Optional[builtins.str] = None,
    home_drive: typing.Optional[builtins.str] = None,
    home_page: typing.Optional[builtins.str] = None,
    home_phone: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    initial_password: typing.Optional[builtins.str] = None,
    initials: typing.Optional[builtins.str] = None,
    mobile_phone: typing.Optional[builtins.str] = None,
    office: typing.Optional[builtins.str] = None,
    office_phone: typing.Optional[builtins.str] = None,
    organization: typing.Optional[builtins.str] = None,
    other_name: typing.Optional[builtins.str] = None,
    password_never_expires: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    po_box: typing.Optional[builtins.str] = None,
    postal_code: typing.Optional[builtins.str] = None,
    smart_card_logon_required: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    state: typing.Optional[builtins.str] = None,
    street_address: typing.Optional[builtins.str] = None,
    surname: typing.Optional[builtins.str] = None,
    title: typing.Optional[builtins.str] = None,
    trusted_for_delegation: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass
