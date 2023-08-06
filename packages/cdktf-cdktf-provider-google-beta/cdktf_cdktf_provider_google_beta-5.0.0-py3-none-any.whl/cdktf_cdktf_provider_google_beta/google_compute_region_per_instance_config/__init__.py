'''
# `google_compute_region_per_instance_config`

Refer to the Terraform Registory for docs: [`google_compute_region_per_instance_config`](https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_per_instance_config).
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


class GoogleComputeRegionPerInstanceConfig(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionPerInstanceConfig.GoogleComputeRegionPerInstanceConfig",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_per_instance_config google_compute_region_per_instance_config}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        region_instance_group_manager: builtins.str,
        id: typing.Optional[builtins.str] = None,
        minimal_action: typing.Optional[builtins.str] = None,
        most_disruptive_allowed_action: typing.Optional[builtins.str] = None,
        preserved_state: typing.Optional[typing.Union["GoogleComputeRegionPerInstanceConfigPreservedState", typing.Dict[builtins.str, typing.Any]]] = None,
        project: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        remove_instance_state_on_destroy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        timeouts: typing.Optional[typing.Union["GoogleComputeRegionPerInstanceConfigTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_per_instance_config google_compute_region_per_instance_config} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: The name for this per-instance config and its corresponding instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_per_instance_config#name GoogleComputeRegionPerInstanceConfig#name}
        :param region_instance_group_manager: The region instance group manager this instance config is part of. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_per_instance_config#region_instance_group_manager GoogleComputeRegionPerInstanceConfig#region_instance_group_manager}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_per_instance_config#id GoogleComputeRegionPerInstanceConfig#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param minimal_action: The minimal action to perform on the instance during an update. Default is 'NONE'. Possible values are: REPLACE RESTART REFRESH NONE. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_per_instance_config#minimal_action GoogleComputeRegionPerInstanceConfig#minimal_action}
        :param most_disruptive_allowed_action: The most disruptive action to perform on the instance during an update. Default is 'REPLACE'. Possible values are: REPLACE RESTART REFRESH NONE. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_per_instance_config#most_disruptive_allowed_action GoogleComputeRegionPerInstanceConfig#most_disruptive_allowed_action}
        :param preserved_state: preserved_state block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_per_instance_config#preserved_state GoogleComputeRegionPerInstanceConfig#preserved_state}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_per_instance_config#project GoogleComputeRegionPerInstanceConfig#project}.
        :param region: Region where the containing instance group manager is located. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_per_instance_config#region GoogleComputeRegionPerInstanceConfig#region}
        :param remove_instance_state_on_destroy: When true, deleting this config will immediately remove any specified state from the underlying instance. When false, deleting this config will *not* immediately remove any state from the underlying instance. State will be removed on the next instance recreation or update. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_per_instance_config#remove_instance_state_on_destroy GoogleComputeRegionPerInstanceConfig#remove_instance_state_on_destroy}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_per_instance_config#timeouts GoogleComputeRegionPerInstanceConfig#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0532d16a5706642527169426195d6f22c2097a4359239db98c2585478ebabc23)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleComputeRegionPerInstanceConfigConfig(
            name=name,
            region_instance_group_manager=region_instance_group_manager,
            id=id,
            minimal_action=minimal_action,
            most_disruptive_allowed_action=most_disruptive_allowed_action,
            preserved_state=preserved_state,
            project=project,
            region=region,
            remove_instance_state_on_destroy=remove_instance_state_on_destroy,
            timeouts=timeouts,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putPreservedState")
    def put_preserved_state(
        self,
        *,
        disk: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleComputeRegionPerInstanceConfigPreservedStateDisk", typing.Dict[builtins.str, typing.Any]]]]] = None,
        metadata: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param disk: disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_per_instance_config#disk GoogleComputeRegionPerInstanceConfig#disk}
        :param metadata: Preserved metadata defined for this instance. This is a list of key->value pairs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_per_instance_config#metadata GoogleComputeRegionPerInstanceConfig#metadata}
        '''
        value = GoogleComputeRegionPerInstanceConfigPreservedState(
            disk=disk, metadata=metadata
        )

        return typing.cast(None, jsii.invoke(self, "putPreservedState", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_per_instance_config#create GoogleComputeRegionPerInstanceConfig#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_per_instance_config#delete GoogleComputeRegionPerInstanceConfig#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_per_instance_config#update GoogleComputeRegionPerInstanceConfig#update}.
        '''
        value = GoogleComputeRegionPerInstanceConfigTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMinimalAction")
    def reset_minimal_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinimalAction", []))

    @jsii.member(jsii_name="resetMostDisruptiveAllowedAction")
    def reset_most_disruptive_allowed_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMostDisruptiveAllowedAction", []))

    @jsii.member(jsii_name="resetPreservedState")
    def reset_preserved_state(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreservedState", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @jsii.member(jsii_name="resetRemoveInstanceStateOnDestroy")
    def reset_remove_instance_state_on_destroy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRemoveInstanceStateOnDestroy", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="preservedState")
    def preserved_state(
        self,
    ) -> "GoogleComputeRegionPerInstanceConfigPreservedStateOutputReference":
        return typing.cast("GoogleComputeRegionPerInstanceConfigPreservedStateOutputReference", jsii.get(self, "preservedState"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleComputeRegionPerInstanceConfigTimeoutsOutputReference":
        return typing.cast("GoogleComputeRegionPerInstanceConfigTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="minimalActionInput")
    def minimal_action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "minimalActionInput"))

    @builtins.property
    @jsii.member(jsii_name="mostDisruptiveAllowedActionInput")
    def most_disruptive_allowed_action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mostDisruptiveAllowedActionInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="preservedStateInput")
    def preserved_state_input(
        self,
    ) -> typing.Optional["GoogleComputeRegionPerInstanceConfigPreservedState"]:
        return typing.cast(typing.Optional["GoogleComputeRegionPerInstanceConfigPreservedState"], jsii.get(self, "preservedStateInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInstanceGroupManagerInput")
    def region_instance_group_manager_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInstanceGroupManagerInput"))

    @builtins.property
    @jsii.member(jsii_name="removeInstanceStateOnDestroyInput")
    def remove_instance_state_on_destroy_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "removeInstanceStateOnDestroyInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleComputeRegionPerInstanceConfigTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleComputeRegionPerInstanceConfigTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa623a49a8a19e66cd03c1c35d4fc2ce42b15c8162532767064fe0965744f656)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="minimalAction")
    def minimal_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "minimalAction"))

    @minimal_action.setter
    def minimal_action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a7a8ee49c879ba10968639913f2674964aa0b6f3ab8902f09f2d2af03485ca5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minimalAction", value)

    @builtins.property
    @jsii.member(jsii_name="mostDisruptiveAllowedAction")
    def most_disruptive_allowed_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mostDisruptiveAllowedAction"))

    @most_disruptive_allowed_action.setter
    def most_disruptive_allowed_action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__530c99528ac4db1edc5e751bf633513cf113880bbb74ad2036075efa8285dae8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mostDisruptiveAllowedAction", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__403949c843898e9537a3d6fe33e4ce3a3fa3ad0fcd31373a47817d63ffafdcfe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c860286b46960147d7643c932844140afba1c66d1ddbd94f435015335f06fd3b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__033de3b2cbe4168eac98b9fd0662a3d143c69ebad99289ea16604d472baa9fe2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="regionInstanceGroupManager")
    def region_instance_group_manager(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "regionInstanceGroupManager"))

    @region_instance_group_manager.setter
    def region_instance_group_manager(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e04907c7382a70fc2191fae19b97c59c05a8196117fb2ce4cde8da91113acbd7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "regionInstanceGroupManager", value)

    @builtins.property
    @jsii.member(jsii_name="removeInstanceStateOnDestroy")
    def remove_instance_state_on_destroy(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "removeInstanceStateOnDestroy"))

    @remove_instance_state_on_destroy.setter
    def remove_instance_state_on_destroy(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0472db7195004730a2cd44506d10e5a24d55fac4a268a0194ef823af70a1ac8e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "removeInstanceStateOnDestroy", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionPerInstanceConfig.GoogleComputeRegionPerInstanceConfigConfig",
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
        "region_instance_group_manager": "regionInstanceGroupManager",
        "id": "id",
        "minimal_action": "minimalAction",
        "most_disruptive_allowed_action": "mostDisruptiveAllowedAction",
        "preserved_state": "preservedState",
        "project": "project",
        "region": "region",
        "remove_instance_state_on_destroy": "removeInstanceStateOnDestroy",
        "timeouts": "timeouts",
    },
)
class GoogleComputeRegionPerInstanceConfigConfig(
    _cdktf_9a9027ec.TerraformMetaArguments,
):
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
        region_instance_group_manager: builtins.str,
        id: typing.Optional[builtins.str] = None,
        minimal_action: typing.Optional[builtins.str] = None,
        most_disruptive_allowed_action: typing.Optional[builtins.str] = None,
        preserved_state: typing.Optional[typing.Union["GoogleComputeRegionPerInstanceConfigPreservedState", typing.Dict[builtins.str, typing.Any]]] = None,
        project: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        remove_instance_state_on_destroy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        timeouts: typing.Optional[typing.Union["GoogleComputeRegionPerInstanceConfigTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: The name for this per-instance config and its corresponding instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_per_instance_config#name GoogleComputeRegionPerInstanceConfig#name}
        :param region_instance_group_manager: The region instance group manager this instance config is part of. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_per_instance_config#region_instance_group_manager GoogleComputeRegionPerInstanceConfig#region_instance_group_manager}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_per_instance_config#id GoogleComputeRegionPerInstanceConfig#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param minimal_action: The minimal action to perform on the instance during an update. Default is 'NONE'. Possible values are: REPLACE RESTART REFRESH NONE. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_per_instance_config#minimal_action GoogleComputeRegionPerInstanceConfig#minimal_action}
        :param most_disruptive_allowed_action: The most disruptive action to perform on the instance during an update. Default is 'REPLACE'. Possible values are: REPLACE RESTART REFRESH NONE. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_per_instance_config#most_disruptive_allowed_action GoogleComputeRegionPerInstanceConfig#most_disruptive_allowed_action}
        :param preserved_state: preserved_state block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_per_instance_config#preserved_state GoogleComputeRegionPerInstanceConfig#preserved_state}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_per_instance_config#project GoogleComputeRegionPerInstanceConfig#project}.
        :param region: Region where the containing instance group manager is located. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_per_instance_config#region GoogleComputeRegionPerInstanceConfig#region}
        :param remove_instance_state_on_destroy: When true, deleting this config will immediately remove any specified state from the underlying instance. When false, deleting this config will *not* immediately remove any state from the underlying instance. State will be removed on the next instance recreation or update. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_per_instance_config#remove_instance_state_on_destroy GoogleComputeRegionPerInstanceConfig#remove_instance_state_on_destroy}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_per_instance_config#timeouts GoogleComputeRegionPerInstanceConfig#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(preserved_state, dict):
            preserved_state = GoogleComputeRegionPerInstanceConfigPreservedState(**preserved_state)
        if isinstance(timeouts, dict):
            timeouts = GoogleComputeRegionPerInstanceConfigTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d478ea9903407d14ec8c99c806e3ec0e0853595482654947b2ba4469feba836)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument region_instance_group_manager", value=region_instance_group_manager, expected_type=type_hints["region_instance_group_manager"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument minimal_action", value=minimal_action, expected_type=type_hints["minimal_action"])
            check_type(argname="argument most_disruptive_allowed_action", value=most_disruptive_allowed_action, expected_type=type_hints["most_disruptive_allowed_action"])
            check_type(argname="argument preserved_state", value=preserved_state, expected_type=type_hints["preserved_state"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument remove_instance_state_on_destroy", value=remove_instance_state_on_destroy, expected_type=type_hints["remove_instance_state_on_destroy"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "region_instance_group_manager": region_instance_group_manager,
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
        if id is not None:
            self._values["id"] = id
        if minimal_action is not None:
            self._values["minimal_action"] = minimal_action
        if most_disruptive_allowed_action is not None:
            self._values["most_disruptive_allowed_action"] = most_disruptive_allowed_action
        if preserved_state is not None:
            self._values["preserved_state"] = preserved_state
        if project is not None:
            self._values["project"] = project
        if region is not None:
            self._values["region"] = region
        if remove_instance_state_on_destroy is not None:
            self._values["remove_instance_state_on_destroy"] = remove_instance_state_on_destroy
        if timeouts is not None:
            self._values["timeouts"] = timeouts

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
        '''The name for this per-instance config and its corresponding instance.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_per_instance_config#name GoogleComputeRegionPerInstanceConfig#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def region_instance_group_manager(self) -> builtins.str:
        '''The region instance group manager this instance config is part of.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_per_instance_config#region_instance_group_manager GoogleComputeRegionPerInstanceConfig#region_instance_group_manager}
        '''
        result = self._values.get("region_instance_group_manager")
        assert result is not None, "Required property 'region_instance_group_manager' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_per_instance_config#id GoogleComputeRegionPerInstanceConfig#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def minimal_action(self) -> typing.Optional[builtins.str]:
        '''The minimal action to perform on the instance during an update. Default is 'NONE'. Possible values are: REPLACE RESTART REFRESH NONE.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_per_instance_config#minimal_action GoogleComputeRegionPerInstanceConfig#minimal_action}
        '''
        result = self._values.get("minimal_action")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def most_disruptive_allowed_action(self) -> typing.Optional[builtins.str]:
        '''The most disruptive action to perform on the instance during an update. Default is 'REPLACE'. Possible values are: REPLACE RESTART REFRESH NONE.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_per_instance_config#most_disruptive_allowed_action GoogleComputeRegionPerInstanceConfig#most_disruptive_allowed_action}
        '''
        result = self._values.get("most_disruptive_allowed_action")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def preserved_state(
        self,
    ) -> typing.Optional["GoogleComputeRegionPerInstanceConfigPreservedState"]:
        '''preserved_state block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_per_instance_config#preserved_state GoogleComputeRegionPerInstanceConfig#preserved_state}
        '''
        result = self._values.get("preserved_state")
        return typing.cast(typing.Optional["GoogleComputeRegionPerInstanceConfigPreservedState"], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_per_instance_config#project GoogleComputeRegionPerInstanceConfig#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''Region where the containing instance group manager is located.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_per_instance_config#region GoogleComputeRegionPerInstanceConfig#region}
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def remove_instance_state_on_destroy(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''When true, deleting this config will immediately remove any specified state from the underlying instance.

        When false, deleting this config will *not* immediately remove any state from the underlying instance.
        State will be removed on the next instance recreation or update.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_per_instance_config#remove_instance_state_on_destroy GoogleComputeRegionPerInstanceConfig#remove_instance_state_on_destroy}
        '''
        result = self._values.get("remove_instance_state_on_destroy")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def timeouts(
        self,
    ) -> typing.Optional["GoogleComputeRegionPerInstanceConfigTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_per_instance_config#timeouts GoogleComputeRegionPerInstanceConfig#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleComputeRegionPerInstanceConfigTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionPerInstanceConfigConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionPerInstanceConfig.GoogleComputeRegionPerInstanceConfigPreservedState",
    jsii_struct_bases=[],
    name_mapping={"disk": "disk", "metadata": "metadata"},
)
class GoogleComputeRegionPerInstanceConfigPreservedState:
    def __init__(
        self,
        *,
        disk: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleComputeRegionPerInstanceConfigPreservedStateDisk", typing.Dict[builtins.str, typing.Any]]]]] = None,
        metadata: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param disk: disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_per_instance_config#disk GoogleComputeRegionPerInstanceConfig#disk}
        :param metadata: Preserved metadata defined for this instance. This is a list of key->value pairs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_per_instance_config#metadata GoogleComputeRegionPerInstanceConfig#metadata}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4737f9f945a9438739ebff3a040ef68f00ed5b4fed528ae0fd12ea1291220d1e)
            check_type(argname="argument disk", value=disk, expected_type=type_hints["disk"])
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if disk is not None:
            self._values["disk"] = disk
        if metadata is not None:
            self._values["metadata"] = metadata

    @builtins.property
    def disk(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleComputeRegionPerInstanceConfigPreservedStateDisk"]]]:
        '''disk block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_per_instance_config#disk GoogleComputeRegionPerInstanceConfig#disk}
        '''
        result = self._values.get("disk")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleComputeRegionPerInstanceConfigPreservedStateDisk"]]], result)

    @builtins.property
    def metadata(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Preserved metadata defined for this instance. This is a list of key->value pairs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_per_instance_config#metadata GoogleComputeRegionPerInstanceConfig#metadata}
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionPerInstanceConfigPreservedState(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionPerInstanceConfig.GoogleComputeRegionPerInstanceConfigPreservedStateDisk",
    jsii_struct_bases=[],
    name_mapping={
        "device_name": "deviceName",
        "source": "source",
        "delete_rule": "deleteRule",
        "mode": "mode",
    },
)
class GoogleComputeRegionPerInstanceConfigPreservedStateDisk:
    def __init__(
        self,
        *,
        device_name: builtins.str,
        source: builtins.str,
        delete_rule: typing.Optional[builtins.str] = None,
        mode: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param device_name: A unique device name that is reflected into the /dev/ tree of a Linux operating system running within the instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_per_instance_config#device_name GoogleComputeRegionPerInstanceConfig#device_name}
        :param source: The URI of an existing persistent disk to attach under the specified device-name in the format 'projects/project-id/zones/zone/disks/disk-name'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_per_instance_config#source GoogleComputeRegionPerInstanceConfig#source}
        :param delete_rule: A value that prescribes what should happen to the stateful disk when the VM instance is deleted. The available options are 'NEVER' and 'ON_PERMANENT_INSTANCE_DELETION'. 'NEVER' - detach the disk when the VM is deleted, but do not delete the disk. 'ON_PERMANENT_INSTANCE_DELETION' will delete the stateful disk when the VM is permanently deleted from the instance group. Default value: "NEVER" Possible values: ["NEVER", "ON_PERMANENT_INSTANCE_DELETION"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_per_instance_config#delete_rule GoogleComputeRegionPerInstanceConfig#delete_rule}
        :param mode: The mode of the disk. Default value: "READ_WRITE" Possible values: ["READ_ONLY", "READ_WRITE"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_per_instance_config#mode GoogleComputeRegionPerInstanceConfig#mode}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a64042cdd2c8271f9141173c7daafa1b27bae3cb57b26b3bbf156afe3ac351a6)
            check_type(argname="argument device_name", value=device_name, expected_type=type_hints["device_name"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument delete_rule", value=delete_rule, expected_type=type_hints["delete_rule"])
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "device_name": device_name,
            "source": source,
        }
        if delete_rule is not None:
            self._values["delete_rule"] = delete_rule
        if mode is not None:
            self._values["mode"] = mode

    @builtins.property
    def device_name(self) -> builtins.str:
        '''A unique device name that is reflected into the /dev/ tree of a Linux operating system running within the instance.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_per_instance_config#device_name GoogleComputeRegionPerInstanceConfig#device_name}
        '''
        result = self._values.get("device_name")
        assert result is not None, "Required property 'device_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source(self) -> builtins.str:
        '''The URI of an existing persistent disk to attach under the specified device-name in the format 'projects/project-id/zones/zone/disks/disk-name'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_per_instance_config#source GoogleComputeRegionPerInstanceConfig#source}
        '''
        result = self._values.get("source")
        assert result is not None, "Required property 'source' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def delete_rule(self) -> typing.Optional[builtins.str]:
        '''A value that prescribes what should happen to the stateful disk when the VM instance is deleted.

        The available options are 'NEVER' and 'ON_PERMANENT_INSTANCE_DELETION'.
        'NEVER' - detach the disk when the VM is deleted, but do not delete the disk.
        'ON_PERMANENT_INSTANCE_DELETION' will delete the stateful disk when the VM is permanently
        deleted from the instance group. Default value: "NEVER" Possible values: ["NEVER", "ON_PERMANENT_INSTANCE_DELETION"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_per_instance_config#delete_rule GoogleComputeRegionPerInstanceConfig#delete_rule}
        '''
        result = self._values.get("delete_rule")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mode(self) -> typing.Optional[builtins.str]:
        '''The mode of the disk. Default value: "READ_WRITE" Possible values: ["READ_ONLY", "READ_WRITE"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_per_instance_config#mode GoogleComputeRegionPerInstanceConfig#mode}
        '''
        result = self._values.get("mode")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionPerInstanceConfigPreservedStateDisk(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeRegionPerInstanceConfigPreservedStateDiskList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionPerInstanceConfig.GoogleComputeRegionPerInstanceConfigPreservedStateDiskList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0027e258b7410a2e3fde2cd7e16915ed791cf7b477fd23e662a9eb0d3e678a75)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleComputeRegionPerInstanceConfigPreservedStateDiskOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6c61c404b14293f5b4faffb78b975fbb910e5655437f033b3332c9916438900)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleComputeRegionPerInstanceConfigPreservedStateDiskOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a4698b04ba20c7149b6df0fcbe17dc50d585bef36654597988f31d8185e4e35)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e1046e87ad832d4f5301bc14cbb97f441c2b1e68d9c6f6547677a852cb5fef4b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__92286272108a932af72a91b73066fd361fa07ed30edd0c6eaee3379dab5d85cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleComputeRegionPerInstanceConfigPreservedStateDisk]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleComputeRegionPerInstanceConfigPreservedStateDisk]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleComputeRegionPerInstanceConfigPreservedStateDisk]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9cc1724aabe5ebfe12faf6fdfe5aee0130a67774a499d97dd0c1783cb229dd67)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeRegionPerInstanceConfigPreservedStateDiskOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionPerInstanceConfig.GoogleComputeRegionPerInstanceConfigPreservedStateDiskOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5e2187f53468627de22ff96d606bf2bde3465fa159eee9217159f52c38a1e0ac)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDeleteRule")
    def reset_delete_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeleteRule", []))

    @jsii.member(jsii_name="resetMode")
    def reset_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMode", []))

    @builtins.property
    @jsii.member(jsii_name="deleteRuleInput")
    def delete_rule_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteRuleInput"))

    @builtins.property
    @jsii.member(jsii_name="deviceNameInput")
    def device_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deviceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="modeInput")
    def mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modeInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceInput")
    def source_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteRule")
    def delete_rule(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deleteRule"))

    @delete_rule.setter
    def delete_rule(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d11a06a9e16a8817d839bee5d30ba0bfe629734f72544f3a96aadd911129fe0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deleteRule", value)

    @builtins.property
    @jsii.member(jsii_name="deviceName")
    def device_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deviceName"))

    @device_name.setter
    def device_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7928cd16e36d43bc8ecb172198730698afe580ad9c7d616af6fb4b6ac4bf5bef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deviceName", value)

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mode"))

    @mode.setter
    def mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b9f98373a8079adbe1727249a1fd4424a65e9b9fbfb29fcfd5a464925401775)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value)

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "source"))

    @source.setter
    def source(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b1087912277af00971c36863d0d696903dfbce0bf77f82a1c1f118efa5e398d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "source", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeRegionPerInstanceConfigPreservedStateDisk, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeRegionPerInstanceConfigPreservedStateDisk, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeRegionPerInstanceConfigPreservedStateDisk, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58660c4793d8434ac2c213cc582f472b420f460fd927121c473f7e655a600ee2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeRegionPerInstanceConfigPreservedStateOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionPerInstanceConfig.GoogleComputeRegionPerInstanceConfigPreservedStateOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a66569f33c9876eec06c929ea29d968e3f8e88653e682aca30c96e5f99723eff)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDisk")
    def put_disk(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleComputeRegionPerInstanceConfigPreservedStateDisk, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8534b2e73f0f4f6ed8e3c1fcabb5f09f8cba37c560e952046719e1f27bde84e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDisk", [value]))

    @jsii.member(jsii_name="resetDisk")
    def reset_disk(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisk", []))

    @jsii.member(jsii_name="resetMetadata")
    def reset_metadata(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetadata", []))

    @builtins.property
    @jsii.member(jsii_name="disk")
    def disk(self) -> GoogleComputeRegionPerInstanceConfigPreservedStateDiskList:
        return typing.cast(GoogleComputeRegionPerInstanceConfigPreservedStateDiskList, jsii.get(self, "disk"))

    @builtins.property
    @jsii.member(jsii_name="diskInput")
    def disk_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleComputeRegionPerInstanceConfigPreservedStateDisk]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleComputeRegionPerInstanceConfigPreservedStateDisk]]], jsii.get(self, "diskInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataInput")
    def metadata_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "metadataInput"))

    @builtins.property
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "metadata"))

    @metadata.setter
    def metadata(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d339057c9174a1353b8273b39583dfd718335268c5fd21d0c2939ed5e6ece446)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metadata", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeRegionPerInstanceConfigPreservedState]:
        return typing.cast(typing.Optional[GoogleComputeRegionPerInstanceConfigPreservedState], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeRegionPerInstanceConfigPreservedState],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77ddd84803f477bef97c4cf951d26188e22d7b7ddb6b67b9f906f24580c6aa06)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionPerInstanceConfig.GoogleComputeRegionPerInstanceConfigTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleComputeRegionPerInstanceConfigTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_per_instance_config#create GoogleComputeRegionPerInstanceConfig#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_per_instance_config#delete GoogleComputeRegionPerInstanceConfig#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_per_instance_config#update GoogleComputeRegionPerInstanceConfig#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae9a5c5ddadfe7df94e123afcdd998b11ff779b4d77a1371edbecbe1e9373bbc)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_per_instance_config#create GoogleComputeRegionPerInstanceConfig#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_per_instance_config#delete GoogleComputeRegionPerInstanceConfig#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_per_instance_config#update GoogleComputeRegionPerInstanceConfig#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionPerInstanceConfigTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeRegionPerInstanceConfigTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionPerInstanceConfig.GoogleComputeRegionPerInstanceConfigTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__41ce1f7bd1f8c3a7fa3e0eb2ba04f7f1dab965d3ca7aeacd3ad93d52c71ab53c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__573d431fb3b9f72472f1e7e971c071f58880e2f1c411f5edb64698d67bb2e759)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9cf38c5e726a76830c9bf16e75c9a4355b4f0c001f94a941015a2b30adf0336a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3982575beef89781069ca8c40b18d6b2bbf69e1542f609157b774d7611a9940)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeRegionPerInstanceConfigTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeRegionPerInstanceConfigTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeRegionPerInstanceConfigTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb6b38cc9c56308a38f5bebfdbfc9bf9b68caa582f33e6cdc60ec25079670c68)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleComputeRegionPerInstanceConfig",
    "GoogleComputeRegionPerInstanceConfigConfig",
    "GoogleComputeRegionPerInstanceConfigPreservedState",
    "GoogleComputeRegionPerInstanceConfigPreservedStateDisk",
    "GoogleComputeRegionPerInstanceConfigPreservedStateDiskList",
    "GoogleComputeRegionPerInstanceConfigPreservedStateDiskOutputReference",
    "GoogleComputeRegionPerInstanceConfigPreservedStateOutputReference",
    "GoogleComputeRegionPerInstanceConfigTimeouts",
    "GoogleComputeRegionPerInstanceConfigTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__0532d16a5706642527169426195d6f22c2097a4359239db98c2585478ebabc23(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    region_instance_group_manager: builtins.str,
    id: typing.Optional[builtins.str] = None,
    minimal_action: typing.Optional[builtins.str] = None,
    most_disruptive_allowed_action: typing.Optional[builtins.str] = None,
    preserved_state: typing.Optional[typing.Union[GoogleComputeRegionPerInstanceConfigPreservedState, typing.Dict[builtins.str, typing.Any]]] = None,
    project: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    remove_instance_state_on_destroy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    timeouts: typing.Optional[typing.Union[GoogleComputeRegionPerInstanceConfigTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__aa623a49a8a19e66cd03c1c35d4fc2ce42b15c8162532767064fe0965744f656(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a7a8ee49c879ba10968639913f2674964aa0b6f3ab8902f09f2d2af03485ca5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__530c99528ac4db1edc5e751bf633513cf113880bbb74ad2036075efa8285dae8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__403949c843898e9537a3d6fe33e4ce3a3fa3ad0fcd31373a47817d63ffafdcfe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c860286b46960147d7643c932844140afba1c66d1ddbd94f435015335f06fd3b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__033de3b2cbe4168eac98b9fd0662a3d143c69ebad99289ea16604d472baa9fe2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e04907c7382a70fc2191fae19b97c59c05a8196117fb2ce4cde8da91113acbd7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0472db7195004730a2cd44506d10e5a24d55fac4a268a0194ef823af70a1ac8e(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d478ea9903407d14ec8c99c806e3ec0e0853595482654947b2ba4469feba836(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    region_instance_group_manager: builtins.str,
    id: typing.Optional[builtins.str] = None,
    minimal_action: typing.Optional[builtins.str] = None,
    most_disruptive_allowed_action: typing.Optional[builtins.str] = None,
    preserved_state: typing.Optional[typing.Union[GoogleComputeRegionPerInstanceConfigPreservedState, typing.Dict[builtins.str, typing.Any]]] = None,
    project: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    remove_instance_state_on_destroy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    timeouts: typing.Optional[typing.Union[GoogleComputeRegionPerInstanceConfigTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4737f9f945a9438739ebff3a040ef68f00ed5b4fed528ae0fd12ea1291220d1e(
    *,
    disk: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleComputeRegionPerInstanceConfigPreservedStateDisk, typing.Dict[builtins.str, typing.Any]]]]] = None,
    metadata: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a64042cdd2c8271f9141173c7daafa1b27bae3cb57b26b3bbf156afe3ac351a6(
    *,
    device_name: builtins.str,
    source: builtins.str,
    delete_rule: typing.Optional[builtins.str] = None,
    mode: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0027e258b7410a2e3fde2cd7e16915ed791cf7b477fd23e662a9eb0d3e678a75(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6c61c404b14293f5b4faffb78b975fbb910e5655437f033b3332c9916438900(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a4698b04ba20c7149b6df0fcbe17dc50d585bef36654597988f31d8185e4e35(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1046e87ad832d4f5301bc14cbb97f441c2b1e68d9c6f6547677a852cb5fef4b(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92286272108a932af72a91b73066fd361fa07ed30edd0c6eaee3379dab5d85cb(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9cc1724aabe5ebfe12faf6fdfe5aee0130a67774a499d97dd0c1783cb229dd67(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleComputeRegionPerInstanceConfigPreservedStateDisk]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e2187f53468627de22ff96d606bf2bde3465fa159eee9217159f52c38a1e0ac(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d11a06a9e16a8817d839bee5d30ba0bfe629734f72544f3a96aadd911129fe0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7928cd16e36d43bc8ecb172198730698afe580ad9c7d616af6fb4b6ac4bf5bef(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b9f98373a8079adbe1727249a1fd4424a65e9b9fbfb29fcfd5a464925401775(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b1087912277af00971c36863d0d696903dfbce0bf77f82a1c1f118efa5e398d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58660c4793d8434ac2c213cc582f472b420f460fd927121c473f7e655a600ee2(
    value: typing.Optional[typing.Union[GoogleComputeRegionPerInstanceConfigPreservedStateDisk, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a66569f33c9876eec06c929ea29d968e3f8e88653e682aca30c96e5f99723eff(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8534b2e73f0f4f6ed8e3c1fcabb5f09f8cba37c560e952046719e1f27bde84e(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleComputeRegionPerInstanceConfigPreservedStateDisk, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d339057c9174a1353b8273b39583dfd718335268c5fd21d0c2939ed5e6ece446(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77ddd84803f477bef97c4cf951d26188e22d7b7ddb6b67b9f906f24580c6aa06(
    value: typing.Optional[GoogleComputeRegionPerInstanceConfigPreservedState],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae9a5c5ddadfe7df94e123afcdd998b11ff779b4d77a1371edbecbe1e9373bbc(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41ce1f7bd1f8c3a7fa3e0eb2ba04f7f1dab965d3ca7aeacd3ad93d52c71ab53c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__573d431fb3b9f72472f1e7e971c071f58880e2f1c411f5edb64698d67bb2e759(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9cf38c5e726a76830c9bf16e75c9a4355b4f0c001f94a941015a2b30adf0336a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3982575beef89781069ca8c40b18d6b2bbf69e1542f609157b774d7611a9940(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb6b38cc9c56308a38f5bebfdbfc9bf9b68caa582f33e6cdc60ec25079670c68(
    value: typing.Optional[typing.Union[GoogleComputeRegionPerInstanceConfigTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
