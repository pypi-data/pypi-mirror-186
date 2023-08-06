'''
# `google_compute_per_instance_config`

Refer to the Terraform Registory for docs: [`google_compute_per_instance_config`](https://www.terraform.io/docs/providers/google-beta/r/google_compute_per_instance_config).
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


class GoogleComputePerInstanceConfig(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputePerInstanceConfig.GoogleComputePerInstanceConfig",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_per_instance_config google_compute_per_instance_config}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        instance_group_manager: builtins.str,
        name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        minimal_action: typing.Optional[builtins.str] = None,
        most_disruptive_allowed_action: typing.Optional[builtins.str] = None,
        preserved_state: typing.Optional[typing.Union["GoogleComputePerInstanceConfigPreservedState", typing.Dict[builtins.str, typing.Any]]] = None,
        project: typing.Optional[builtins.str] = None,
        remove_instance_state_on_destroy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        timeouts: typing.Optional[typing.Union["GoogleComputePerInstanceConfigTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        zone: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_per_instance_config google_compute_per_instance_config} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param instance_group_manager: The instance group manager this instance config is part of. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_per_instance_config#instance_group_manager GoogleComputePerInstanceConfig#instance_group_manager}
        :param name: The name for this per-instance config and its corresponding instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_per_instance_config#name GoogleComputePerInstanceConfig#name}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_per_instance_config#id GoogleComputePerInstanceConfig#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param minimal_action: The minimal action to perform on the instance during an update. Default is 'NONE'. Possible values are: REPLACE RESTART REFRESH NONE. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_per_instance_config#minimal_action GoogleComputePerInstanceConfig#minimal_action}
        :param most_disruptive_allowed_action: The most disruptive action to perform on the instance during an update. Default is 'REPLACE'. Possible values are: REPLACE RESTART REFRESH NONE. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_per_instance_config#most_disruptive_allowed_action GoogleComputePerInstanceConfig#most_disruptive_allowed_action}
        :param preserved_state: preserved_state block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_per_instance_config#preserved_state GoogleComputePerInstanceConfig#preserved_state}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_per_instance_config#project GoogleComputePerInstanceConfig#project}.
        :param remove_instance_state_on_destroy: When true, deleting this config will immediately remove any specified state from the underlying instance. When false, deleting this config will *not* immediately remove any state from the underlying instance. State will be removed on the next instance recreation or update. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_per_instance_config#remove_instance_state_on_destroy GoogleComputePerInstanceConfig#remove_instance_state_on_destroy}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_per_instance_config#timeouts GoogleComputePerInstanceConfig#timeouts}
        :param zone: Zone where the containing instance group manager is located. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_per_instance_config#zone GoogleComputePerInstanceConfig#zone}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d6ea5e34e160210e85ffe56ba7c44f68dc8af3da2e18947dfeb06686e451cf4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleComputePerInstanceConfigConfig(
            instance_group_manager=instance_group_manager,
            name=name,
            id=id,
            minimal_action=minimal_action,
            most_disruptive_allowed_action=most_disruptive_allowed_action,
            preserved_state=preserved_state,
            project=project,
            remove_instance_state_on_destroy=remove_instance_state_on_destroy,
            timeouts=timeouts,
            zone=zone,
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
        disk: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleComputePerInstanceConfigPreservedStateDisk", typing.Dict[builtins.str, typing.Any]]]]] = None,
        metadata: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param disk: disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_per_instance_config#disk GoogleComputePerInstanceConfig#disk}
        :param metadata: Preserved metadata defined for this instance. This is a list of key->value pairs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_per_instance_config#metadata GoogleComputePerInstanceConfig#metadata}
        '''
        value = GoogleComputePerInstanceConfigPreservedState(
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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_per_instance_config#create GoogleComputePerInstanceConfig#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_per_instance_config#delete GoogleComputePerInstanceConfig#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_per_instance_config#update GoogleComputePerInstanceConfig#update}.
        '''
        value = GoogleComputePerInstanceConfigTimeouts(
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

    @jsii.member(jsii_name="resetRemoveInstanceStateOnDestroy")
    def reset_remove_instance_state_on_destroy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRemoveInstanceStateOnDestroy", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetZone")
    def reset_zone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZone", []))

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
    ) -> "GoogleComputePerInstanceConfigPreservedStateOutputReference":
        return typing.cast("GoogleComputePerInstanceConfigPreservedStateOutputReference", jsii.get(self, "preservedState"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleComputePerInstanceConfigTimeoutsOutputReference":
        return typing.cast("GoogleComputePerInstanceConfigTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceGroupManagerInput")
    def instance_group_manager_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceGroupManagerInput"))

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
    ) -> typing.Optional["GoogleComputePerInstanceConfigPreservedState"]:
        return typing.cast(typing.Optional["GoogleComputePerInstanceConfigPreservedState"], jsii.get(self, "preservedStateInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

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
    ) -> typing.Optional[typing.Union["GoogleComputePerInstanceConfigTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleComputePerInstanceConfigTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="zoneInput")
    def zone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "zoneInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8278f3359e57530b3a5f6eb6dbbab68d743cb6145a94510a0c10685a4006261)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="instanceGroupManager")
    def instance_group_manager(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceGroupManager"))

    @instance_group_manager.setter
    def instance_group_manager(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36b735eb367bef12da391d14925ea22a8e4ab0a11800cd440e150e67d82de258)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceGroupManager", value)

    @builtins.property
    @jsii.member(jsii_name="minimalAction")
    def minimal_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "minimalAction"))

    @minimal_action.setter
    def minimal_action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__936b566f347ae65bdf01c76d1df52cc8e03b3d18030ab803e06efe0909e15d9e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minimalAction", value)

    @builtins.property
    @jsii.member(jsii_name="mostDisruptiveAllowedAction")
    def most_disruptive_allowed_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mostDisruptiveAllowedAction"))

    @most_disruptive_allowed_action.setter
    def most_disruptive_allowed_action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1dd261f0f59a74a857a4342e95de50a2f49545de43f5c202b6e599ed3a7e314c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mostDisruptiveAllowedAction", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf77f19dd8abbfeaa0f5ba228614486e291ecc0079f7f41125f845dd3e4362e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e401e4bdd8c48fab04859f6693f35788e2dfd90d1ef120483d037992aaef7f6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__8cb75e35bdf6181e8a84f22dc80b6871c3b919c7ea2fc2211ddcd36cfedd1311)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "removeInstanceStateOnDestroy", value)

    @builtins.property
    @jsii.member(jsii_name="zone")
    def zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zone"))

    @zone.setter
    def zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d0e1c756fca8156dfc76ba81af3f41ae42433ba368e7118dcb4a3ddb3e64ed7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zone", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputePerInstanceConfig.GoogleComputePerInstanceConfigConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "instance_group_manager": "instanceGroupManager",
        "name": "name",
        "id": "id",
        "minimal_action": "minimalAction",
        "most_disruptive_allowed_action": "mostDisruptiveAllowedAction",
        "preserved_state": "preservedState",
        "project": "project",
        "remove_instance_state_on_destroy": "removeInstanceStateOnDestroy",
        "timeouts": "timeouts",
        "zone": "zone",
    },
)
class GoogleComputePerInstanceConfigConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        instance_group_manager: builtins.str,
        name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        minimal_action: typing.Optional[builtins.str] = None,
        most_disruptive_allowed_action: typing.Optional[builtins.str] = None,
        preserved_state: typing.Optional[typing.Union["GoogleComputePerInstanceConfigPreservedState", typing.Dict[builtins.str, typing.Any]]] = None,
        project: typing.Optional[builtins.str] = None,
        remove_instance_state_on_destroy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        timeouts: typing.Optional[typing.Union["GoogleComputePerInstanceConfigTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        zone: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param instance_group_manager: The instance group manager this instance config is part of. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_per_instance_config#instance_group_manager GoogleComputePerInstanceConfig#instance_group_manager}
        :param name: The name for this per-instance config and its corresponding instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_per_instance_config#name GoogleComputePerInstanceConfig#name}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_per_instance_config#id GoogleComputePerInstanceConfig#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param minimal_action: The minimal action to perform on the instance during an update. Default is 'NONE'. Possible values are: REPLACE RESTART REFRESH NONE. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_per_instance_config#minimal_action GoogleComputePerInstanceConfig#minimal_action}
        :param most_disruptive_allowed_action: The most disruptive action to perform on the instance during an update. Default is 'REPLACE'. Possible values are: REPLACE RESTART REFRESH NONE. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_per_instance_config#most_disruptive_allowed_action GoogleComputePerInstanceConfig#most_disruptive_allowed_action}
        :param preserved_state: preserved_state block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_per_instance_config#preserved_state GoogleComputePerInstanceConfig#preserved_state}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_per_instance_config#project GoogleComputePerInstanceConfig#project}.
        :param remove_instance_state_on_destroy: When true, deleting this config will immediately remove any specified state from the underlying instance. When false, deleting this config will *not* immediately remove any state from the underlying instance. State will be removed on the next instance recreation or update. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_per_instance_config#remove_instance_state_on_destroy GoogleComputePerInstanceConfig#remove_instance_state_on_destroy}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_per_instance_config#timeouts GoogleComputePerInstanceConfig#timeouts}
        :param zone: Zone where the containing instance group manager is located. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_per_instance_config#zone GoogleComputePerInstanceConfig#zone}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(preserved_state, dict):
            preserved_state = GoogleComputePerInstanceConfigPreservedState(**preserved_state)
        if isinstance(timeouts, dict):
            timeouts = GoogleComputePerInstanceConfigTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f998ea4712855d1be888eceec50544f441ff34bb377e5a9631154b81d81dcd50)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument instance_group_manager", value=instance_group_manager, expected_type=type_hints["instance_group_manager"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument minimal_action", value=minimal_action, expected_type=type_hints["minimal_action"])
            check_type(argname="argument most_disruptive_allowed_action", value=most_disruptive_allowed_action, expected_type=type_hints["most_disruptive_allowed_action"])
            check_type(argname="argument preserved_state", value=preserved_state, expected_type=type_hints["preserved_state"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument remove_instance_state_on_destroy", value=remove_instance_state_on_destroy, expected_type=type_hints["remove_instance_state_on_destroy"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument zone", value=zone, expected_type=type_hints["zone"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_group_manager": instance_group_manager,
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
        if remove_instance_state_on_destroy is not None:
            self._values["remove_instance_state_on_destroy"] = remove_instance_state_on_destroy
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if zone is not None:
            self._values["zone"] = zone

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
    def instance_group_manager(self) -> builtins.str:
        '''The instance group manager this instance config is part of.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_per_instance_config#instance_group_manager GoogleComputePerInstanceConfig#instance_group_manager}
        '''
        result = self._values.get("instance_group_manager")
        assert result is not None, "Required property 'instance_group_manager' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name for this per-instance config and its corresponding instance.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_per_instance_config#name GoogleComputePerInstanceConfig#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_per_instance_config#id GoogleComputePerInstanceConfig#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def minimal_action(self) -> typing.Optional[builtins.str]:
        '''The minimal action to perform on the instance during an update. Default is 'NONE'. Possible values are: REPLACE RESTART REFRESH NONE.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_per_instance_config#minimal_action GoogleComputePerInstanceConfig#minimal_action}
        '''
        result = self._values.get("minimal_action")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def most_disruptive_allowed_action(self) -> typing.Optional[builtins.str]:
        '''The most disruptive action to perform on the instance during an update. Default is 'REPLACE'. Possible values are: REPLACE RESTART REFRESH NONE.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_per_instance_config#most_disruptive_allowed_action GoogleComputePerInstanceConfig#most_disruptive_allowed_action}
        '''
        result = self._values.get("most_disruptive_allowed_action")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def preserved_state(
        self,
    ) -> typing.Optional["GoogleComputePerInstanceConfigPreservedState"]:
        '''preserved_state block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_per_instance_config#preserved_state GoogleComputePerInstanceConfig#preserved_state}
        '''
        result = self._values.get("preserved_state")
        return typing.cast(typing.Optional["GoogleComputePerInstanceConfigPreservedState"], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_per_instance_config#project GoogleComputePerInstanceConfig#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def remove_instance_state_on_destroy(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''When true, deleting this config will immediately remove any specified state from the underlying instance.

        When false, deleting this config will *not* immediately remove any state from the underlying instance.
        State will be removed on the next instance recreation or update.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_per_instance_config#remove_instance_state_on_destroy GoogleComputePerInstanceConfig#remove_instance_state_on_destroy}
        '''
        result = self._values.get("remove_instance_state_on_destroy")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleComputePerInstanceConfigTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_per_instance_config#timeouts GoogleComputePerInstanceConfig#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleComputePerInstanceConfigTimeouts"], result)

    @builtins.property
    def zone(self) -> typing.Optional[builtins.str]:
        '''Zone where the containing instance group manager is located.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_per_instance_config#zone GoogleComputePerInstanceConfig#zone}
        '''
        result = self._values.get("zone")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputePerInstanceConfigConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputePerInstanceConfig.GoogleComputePerInstanceConfigPreservedState",
    jsii_struct_bases=[],
    name_mapping={"disk": "disk", "metadata": "metadata"},
)
class GoogleComputePerInstanceConfigPreservedState:
    def __init__(
        self,
        *,
        disk: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleComputePerInstanceConfigPreservedStateDisk", typing.Dict[builtins.str, typing.Any]]]]] = None,
        metadata: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param disk: disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_per_instance_config#disk GoogleComputePerInstanceConfig#disk}
        :param metadata: Preserved metadata defined for this instance. This is a list of key->value pairs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_per_instance_config#metadata GoogleComputePerInstanceConfig#metadata}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c4389d7c80256afc81f566550befe9d689b94f3be5447991b3f8a3cb155589a)
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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleComputePerInstanceConfigPreservedStateDisk"]]]:
        '''disk block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_per_instance_config#disk GoogleComputePerInstanceConfig#disk}
        '''
        result = self._values.get("disk")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleComputePerInstanceConfigPreservedStateDisk"]]], result)

    @builtins.property
    def metadata(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Preserved metadata defined for this instance. This is a list of key->value pairs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_per_instance_config#metadata GoogleComputePerInstanceConfig#metadata}
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputePerInstanceConfigPreservedState(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputePerInstanceConfig.GoogleComputePerInstanceConfigPreservedStateDisk",
    jsii_struct_bases=[],
    name_mapping={
        "device_name": "deviceName",
        "source": "source",
        "delete_rule": "deleteRule",
        "mode": "mode",
    },
)
class GoogleComputePerInstanceConfigPreservedStateDisk:
    def __init__(
        self,
        *,
        device_name: builtins.str,
        source: builtins.str,
        delete_rule: typing.Optional[builtins.str] = None,
        mode: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param device_name: A unique device name that is reflected into the /dev/ tree of a Linux operating system running within the instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_per_instance_config#device_name GoogleComputePerInstanceConfig#device_name}
        :param source: The URI of an existing persistent disk to attach under the specified device-name in the format 'projects/project-id/zones/zone/disks/disk-name'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_per_instance_config#source GoogleComputePerInstanceConfig#source}
        :param delete_rule: A value that prescribes what should happen to the stateful disk when the VM instance is deleted. The available options are 'NEVER' and 'ON_PERMANENT_INSTANCE_DELETION'. 'NEVER' - detach the disk when the VM is deleted, but do not delete the disk. 'ON_PERMANENT_INSTANCE_DELETION' will delete the stateful disk when the VM is permanently deleted from the instance group. Default value: "NEVER" Possible values: ["NEVER", "ON_PERMANENT_INSTANCE_DELETION"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_per_instance_config#delete_rule GoogleComputePerInstanceConfig#delete_rule}
        :param mode: The mode of the disk. Default value: "READ_WRITE" Possible values: ["READ_ONLY", "READ_WRITE"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_per_instance_config#mode GoogleComputePerInstanceConfig#mode}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e06f80d577747714cb1a05e4e42b64c3fa32d581e4809c68c80ea084d934f8d)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_per_instance_config#device_name GoogleComputePerInstanceConfig#device_name}
        '''
        result = self._values.get("device_name")
        assert result is not None, "Required property 'device_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source(self) -> builtins.str:
        '''The URI of an existing persistent disk to attach under the specified device-name in the format 'projects/project-id/zones/zone/disks/disk-name'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_per_instance_config#source GoogleComputePerInstanceConfig#source}
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_per_instance_config#delete_rule GoogleComputePerInstanceConfig#delete_rule}
        '''
        result = self._values.get("delete_rule")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mode(self) -> typing.Optional[builtins.str]:
        '''The mode of the disk. Default value: "READ_WRITE" Possible values: ["READ_ONLY", "READ_WRITE"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_per_instance_config#mode GoogleComputePerInstanceConfig#mode}
        '''
        result = self._values.get("mode")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputePerInstanceConfigPreservedStateDisk(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputePerInstanceConfigPreservedStateDiskList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputePerInstanceConfig.GoogleComputePerInstanceConfigPreservedStateDiskList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e4537b9bbe4d280175ee2b310a97edf407bcf8690ad76154ccb851dd286e9248)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleComputePerInstanceConfigPreservedStateDiskOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46c72d459d8683b0942038c816749f9734cd7de11bb260ec49ed332224b91d93)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleComputePerInstanceConfigPreservedStateDiskOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee2ca15c7f69809f26a1c3329263c70dd16146f94a4b98cef0690af19350f5a2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__52f7ea74e13d143b95fd1eaf3a3b7d95a41ce04b6c35225acedb9988f71eeb91)
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
            type_hints = typing.get_type_hints(_typecheckingstub__98f313fbfeec1f0a1c5907dfb6b79865601430d81f324c4abb6aa3c28e23c601)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleComputePerInstanceConfigPreservedStateDisk]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleComputePerInstanceConfigPreservedStateDisk]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleComputePerInstanceConfigPreservedStateDisk]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4d152066d1c078fdfb6b29d260f95b1468332e1ebbb6d75d21c442326c13353)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputePerInstanceConfigPreservedStateDiskOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputePerInstanceConfig.GoogleComputePerInstanceConfigPreservedStateDiskOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__76f81701819149aac6eb78c661d914e0d44c12386b8c1b4934e629566aa9558b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__25e4b66a2ee75e26bb6b877debbad531f294a2a0344972ed24590ceb9c71e0f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deleteRule", value)

    @builtins.property
    @jsii.member(jsii_name="deviceName")
    def device_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deviceName"))

    @device_name.setter
    def device_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08f0ccfaca99b26035f7131dddd3761e34a4eb2636d26355d4b9a262fc3ce15f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deviceName", value)

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mode"))

    @mode.setter
    def mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c4228d64462afbe94b97dcecfd31aa9040fc261bd53a2e860d6d72b4850c567)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value)

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "source"))

    @source.setter
    def source(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b58b861095cb016a43797130da13f434a81c36aeb6665cd688da6345e2d4f2a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "source", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputePerInstanceConfigPreservedStateDisk, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputePerInstanceConfigPreservedStateDisk, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputePerInstanceConfigPreservedStateDisk, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5fe5fbe4d32d9a1ac2e2a51e8b94024a42aa3daf581c63c96fa76240f91571e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputePerInstanceConfigPreservedStateOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputePerInstanceConfig.GoogleComputePerInstanceConfigPreservedStateOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5636b28264ae2e88c5430457421d47c0040f72871cf72d6b4aaf839e1b3b4107)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDisk")
    def put_disk(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleComputePerInstanceConfigPreservedStateDisk, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74fbe6378bc8b46bfdd2c8d68c8c7975a2247091b271c05b7769d68bc3b84b4e)
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
    def disk(self) -> GoogleComputePerInstanceConfigPreservedStateDiskList:
        return typing.cast(GoogleComputePerInstanceConfigPreservedStateDiskList, jsii.get(self, "disk"))

    @builtins.property
    @jsii.member(jsii_name="diskInput")
    def disk_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleComputePerInstanceConfigPreservedStateDisk]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleComputePerInstanceConfigPreservedStateDisk]]], jsii.get(self, "diskInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__bf8a554eabfe2b7e5eb3ca9c22116a1c43e815f4262644c30e0d5c2610ec1bd3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metadata", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputePerInstanceConfigPreservedState]:
        return typing.cast(typing.Optional[GoogleComputePerInstanceConfigPreservedState], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputePerInstanceConfigPreservedState],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6f4430b61fbc62fba59a9906f03d48151ca869047d77b9e31984d0834dc950c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputePerInstanceConfig.GoogleComputePerInstanceConfigTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleComputePerInstanceConfigTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_per_instance_config#create GoogleComputePerInstanceConfig#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_per_instance_config#delete GoogleComputePerInstanceConfig#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_per_instance_config#update GoogleComputePerInstanceConfig#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e49e84ebc1bf6f84c329596fcc62b193faf9d88fcadbc32b7e306f108de43540)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_per_instance_config#create GoogleComputePerInstanceConfig#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_per_instance_config#delete GoogleComputePerInstanceConfig#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_per_instance_config#update GoogleComputePerInstanceConfig#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputePerInstanceConfigTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputePerInstanceConfigTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputePerInstanceConfig.GoogleComputePerInstanceConfigTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fc880323e897483ad728f2eb54e9c64d201413420d608220200291145c51c071)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2b5459295843162c233457028180c5cbeaa6f4fb96dc1a8537962422c25a3ccb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24172ee0c9f4ea9bc39354b3d55c66b72d6815ed3e4eae5485921aecde24101c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69fbdb9c7e39faaefa253bcc2cf30057efbef5f1f05b175ae878bf2067193436)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputePerInstanceConfigTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputePerInstanceConfigTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputePerInstanceConfigTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef862ccb1bc778a116898489f418a64de619e80e853ff03ee22bca340eb04a73)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleComputePerInstanceConfig",
    "GoogleComputePerInstanceConfigConfig",
    "GoogleComputePerInstanceConfigPreservedState",
    "GoogleComputePerInstanceConfigPreservedStateDisk",
    "GoogleComputePerInstanceConfigPreservedStateDiskList",
    "GoogleComputePerInstanceConfigPreservedStateDiskOutputReference",
    "GoogleComputePerInstanceConfigPreservedStateOutputReference",
    "GoogleComputePerInstanceConfigTimeouts",
    "GoogleComputePerInstanceConfigTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__7d6ea5e34e160210e85ffe56ba7c44f68dc8af3da2e18947dfeb06686e451cf4(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    instance_group_manager: builtins.str,
    name: builtins.str,
    id: typing.Optional[builtins.str] = None,
    minimal_action: typing.Optional[builtins.str] = None,
    most_disruptive_allowed_action: typing.Optional[builtins.str] = None,
    preserved_state: typing.Optional[typing.Union[GoogleComputePerInstanceConfigPreservedState, typing.Dict[builtins.str, typing.Any]]] = None,
    project: typing.Optional[builtins.str] = None,
    remove_instance_state_on_destroy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    timeouts: typing.Optional[typing.Union[GoogleComputePerInstanceConfigTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    zone: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__b8278f3359e57530b3a5f6eb6dbbab68d743cb6145a94510a0c10685a4006261(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36b735eb367bef12da391d14925ea22a8e4ab0a11800cd440e150e67d82de258(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__936b566f347ae65bdf01c76d1df52cc8e03b3d18030ab803e06efe0909e15d9e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1dd261f0f59a74a857a4342e95de50a2f49545de43f5c202b6e599ed3a7e314c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf77f19dd8abbfeaa0f5ba228614486e291ecc0079f7f41125f845dd3e4362e9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e401e4bdd8c48fab04859f6693f35788e2dfd90d1ef120483d037992aaef7f6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cb75e35bdf6181e8a84f22dc80b6871c3b919c7ea2fc2211ddcd36cfedd1311(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d0e1c756fca8156dfc76ba81af3f41ae42433ba368e7118dcb4a3ddb3e64ed7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f998ea4712855d1be888eceec50544f441ff34bb377e5a9631154b81d81dcd50(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    instance_group_manager: builtins.str,
    name: builtins.str,
    id: typing.Optional[builtins.str] = None,
    minimal_action: typing.Optional[builtins.str] = None,
    most_disruptive_allowed_action: typing.Optional[builtins.str] = None,
    preserved_state: typing.Optional[typing.Union[GoogleComputePerInstanceConfigPreservedState, typing.Dict[builtins.str, typing.Any]]] = None,
    project: typing.Optional[builtins.str] = None,
    remove_instance_state_on_destroy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    timeouts: typing.Optional[typing.Union[GoogleComputePerInstanceConfigTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    zone: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c4389d7c80256afc81f566550befe9d689b94f3be5447991b3f8a3cb155589a(
    *,
    disk: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleComputePerInstanceConfigPreservedStateDisk, typing.Dict[builtins.str, typing.Any]]]]] = None,
    metadata: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e06f80d577747714cb1a05e4e42b64c3fa32d581e4809c68c80ea084d934f8d(
    *,
    device_name: builtins.str,
    source: builtins.str,
    delete_rule: typing.Optional[builtins.str] = None,
    mode: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4537b9bbe4d280175ee2b310a97edf407bcf8690ad76154ccb851dd286e9248(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46c72d459d8683b0942038c816749f9734cd7de11bb260ec49ed332224b91d93(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee2ca15c7f69809f26a1c3329263c70dd16146f94a4b98cef0690af19350f5a2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52f7ea74e13d143b95fd1eaf3a3b7d95a41ce04b6c35225acedb9988f71eeb91(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98f313fbfeec1f0a1c5907dfb6b79865601430d81f324c4abb6aa3c28e23c601(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4d152066d1c078fdfb6b29d260f95b1468332e1ebbb6d75d21c442326c13353(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleComputePerInstanceConfigPreservedStateDisk]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76f81701819149aac6eb78c661d914e0d44c12386b8c1b4934e629566aa9558b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25e4b66a2ee75e26bb6b877debbad531f294a2a0344972ed24590ceb9c71e0f5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08f0ccfaca99b26035f7131dddd3761e34a4eb2636d26355d4b9a262fc3ce15f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c4228d64462afbe94b97dcecfd31aa9040fc261bd53a2e860d6d72b4850c567(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b58b861095cb016a43797130da13f434a81c36aeb6665cd688da6345e2d4f2a8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5fe5fbe4d32d9a1ac2e2a51e8b94024a42aa3daf581c63c96fa76240f91571e(
    value: typing.Optional[typing.Union[GoogleComputePerInstanceConfigPreservedStateDisk, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5636b28264ae2e88c5430457421d47c0040f72871cf72d6b4aaf839e1b3b4107(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74fbe6378bc8b46bfdd2c8d68c8c7975a2247091b271c05b7769d68bc3b84b4e(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleComputePerInstanceConfigPreservedStateDisk, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf8a554eabfe2b7e5eb3ca9c22116a1c43e815f4262644c30e0d5c2610ec1bd3(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6f4430b61fbc62fba59a9906f03d48151ca869047d77b9e31984d0834dc950c(
    value: typing.Optional[GoogleComputePerInstanceConfigPreservedState],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e49e84ebc1bf6f84c329596fcc62b193faf9d88fcadbc32b7e306f108de43540(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc880323e897483ad728f2eb54e9c64d201413420d608220200291145c51c071(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b5459295843162c233457028180c5cbeaa6f4fb96dc1a8537962422c25a3ccb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24172ee0c9f4ea9bc39354b3d55c66b72d6815ed3e4eae5485921aecde24101c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69fbdb9c7e39faaefa253bcc2cf30057efbef5f1f05b175ae878bf2067193436(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef862ccb1bc778a116898489f418a64de619e80e853ff03ee22bca340eb04a73(
    value: typing.Optional[typing.Union[GoogleComputePerInstanceConfigTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
