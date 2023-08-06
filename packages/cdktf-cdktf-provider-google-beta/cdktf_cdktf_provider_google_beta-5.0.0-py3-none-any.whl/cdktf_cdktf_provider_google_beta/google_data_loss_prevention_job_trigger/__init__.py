'''
# `google_data_loss_prevention_job_trigger`

Refer to the Terraform Registory for docs: [`google_data_loss_prevention_job_trigger`](https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger).
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


class GoogleDataLossPreventionJobTrigger(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTrigger",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger google_data_loss_prevention_job_trigger}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        parent: builtins.str,
        triggers: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDataLossPreventionJobTriggerTriggers", typing.Dict[builtins.str, typing.Any]]]],
        description: typing.Optional[builtins.str] = None,
        display_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        inspect_job: typing.Optional[typing.Union["GoogleDataLossPreventionJobTriggerInspectJob", typing.Dict[builtins.str, typing.Any]]] = None,
        status: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleDataLossPreventionJobTriggerTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger google_data_loss_prevention_job_trigger} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param parent: The parent of the trigger, either in the format 'projects/{{project}}' or 'projects/{{project}}/locations/{{location}}'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#parent GoogleDataLossPreventionJobTrigger#parent}
        :param triggers: triggers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#triggers GoogleDataLossPreventionJobTrigger#triggers}
        :param description: A description of the job trigger. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#description GoogleDataLossPreventionJobTrigger#description}
        :param display_name: User set display name of the job trigger. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#display_name GoogleDataLossPreventionJobTrigger#display_name}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#id GoogleDataLossPreventionJobTrigger#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param inspect_job: inspect_job block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#inspect_job GoogleDataLossPreventionJobTrigger#inspect_job}
        :param status: Whether the trigger is currently active. Default value: "HEALTHY" Possible values: ["PAUSED", "HEALTHY", "CANCELLED"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#status GoogleDataLossPreventionJobTrigger#status}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#timeouts GoogleDataLossPreventionJobTrigger#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d0d9ea6bb81a21c3992292e2afbe9aa9a2f8f38abb4c99bebbd303fdcd845e7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleDataLossPreventionJobTriggerConfig(
            parent=parent,
            triggers=triggers,
            description=description,
            display_name=display_name,
            id=id,
            inspect_job=inspect_job,
            status=status,
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

    @jsii.member(jsii_name="putInspectJob")
    def put_inspect_job(
        self,
        *,
        actions: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDataLossPreventionJobTriggerInspectJobActions", typing.Dict[builtins.str, typing.Any]]]],
        inspect_template_name: builtins.str,
        storage_config: typing.Union["GoogleDataLossPreventionJobTriggerInspectJobStorageConfig", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param actions: actions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#actions GoogleDataLossPreventionJobTrigger#actions}
        :param inspect_template_name: The name of the template to run when this job is triggered. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#inspect_template_name GoogleDataLossPreventionJobTrigger#inspect_template_name}
        :param storage_config: storage_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#storage_config GoogleDataLossPreventionJobTrigger#storage_config}
        '''
        value = GoogleDataLossPreventionJobTriggerInspectJob(
            actions=actions,
            inspect_template_name=inspect_template_name,
            storage_config=storage_config,
        )

        return typing.cast(None, jsii.invoke(self, "putInspectJob", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#create GoogleDataLossPreventionJobTrigger#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#delete GoogleDataLossPreventionJobTrigger#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#update GoogleDataLossPreventionJobTrigger#update}.
        '''
        value = GoogleDataLossPreventionJobTriggerTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putTriggers")
    def put_triggers(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDataLossPreventionJobTriggerTriggers", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__400b0f28743c698651f83b72bafcbabdd42c0c88da17270ff3a0d2e0d18d25c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTriggers", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDisplayName")
    def reset_display_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisplayName", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInspectJob")
    def reset_inspect_job(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInspectJob", []))

    @jsii.member(jsii_name="resetStatus")
    def reset_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatus", []))

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
    @jsii.member(jsii_name="inspectJob")
    def inspect_job(
        self,
    ) -> "GoogleDataLossPreventionJobTriggerInspectJobOutputReference":
        return typing.cast("GoogleDataLossPreventionJobTriggerInspectJobOutputReference", jsii.get(self, "inspectJob"))

    @builtins.property
    @jsii.member(jsii_name="lastRunTime")
    def last_run_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastRunTime"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleDataLossPreventionJobTriggerTimeoutsOutputReference":
        return typing.cast("GoogleDataLossPreventionJobTriggerTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="triggers")
    def triggers(self) -> "GoogleDataLossPreventionJobTriggerTriggersList":
        return typing.cast("GoogleDataLossPreventionJobTriggerTriggersList", jsii.get(self, "triggers"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="inspectJobInput")
    def inspect_job_input(
        self,
    ) -> typing.Optional["GoogleDataLossPreventionJobTriggerInspectJob"]:
        return typing.cast(typing.Optional["GoogleDataLossPreventionJobTriggerInspectJob"], jsii.get(self, "inspectJobInput"))

    @builtins.property
    @jsii.member(jsii_name="parentInput")
    def parent_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parentInput"))

    @builtins.property
    @jsii.member(jsii_name="statusInput")
    def status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleDataLossPreventionJobTriggerTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleDataLossPreventionJobTriggerTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="triggersInput")
    def triggers_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDataLossPreventionJobTriggerTriggers"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDataLossPreventionJobTriggerTriggers"]]], jsii.get(self, "triggersInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__155b1978c1188e118f5fb3d8fc7892595da4bf40caba9edb413eb51d7feace0e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa804a38c1453ebd38dceca6f16a250a172272fb27aab741d9217265095266e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23e06de2f2e31d5ea87be92f71c4221086ff77037865625c0a1db2ffb511f243)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="parent")
    def parent(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parent"))

    @parent.setter
    def parent(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__513067889f32f03cc5583d26fd36be5f01794103f98df7db23fef04129565838)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parent", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e3f36361a9e3b82ec15b503ec8557057dcf268981ff6b8fadf6ca42b5fa520b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "parent": "parent",
        "triggers": "triggers",
        "description": "description",
        "display_name": "displayName",
        "id": "id",
        "inspect_job": "inspectJob",
        "status": "status",
        "timeouts": "timeouts",
    },
)
class GoogleDataLossPreventionJobTriggerConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        parent: builtins.str,
        triggers: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDataLossPreventionJobTriggerTriggers", typing.Dict[builtins.str, typing.Any]]]],
        description: typing.Optional[builtins.str] = None,
        display_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        inspect_job: typing.Optional[typing.Union["GoogleDataLossPreventionJobTriggerInspectJob", typing.Dict[builtins.str, typing.Any]]] = None,
        status: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleDataLossPreventionJobTriggerTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param parent: The parent of the trigger, either in the format 'projects/{{project}}' or 'projects/{{project}}/locations/{{location}}'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#parent GoogleDataLossPreventionJobTrigger#parent}
        :param triggers: triggers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#triggers GoogleDataLossPreventionJobTrigger#triggers}
        :param description: A description of the job trigger. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#description GoogleDataLossPreventionJobTrigger#description}
        :param display_name: User set display name of the job trigger. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#display_name GoogleDataLossPreventionJobTrigger#display_name}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#id GoogleDataLossPreventionJobTrigger#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param inspect_job: inspect_job block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#inspect_job GoogleDataLossPreventionJobTrigger#inspect_job}
        :param status: Whether the trigger is currently active. Default value: "HEALTHY" Possible values: ["PAUSED", "HEALTHY", "CANCELLED"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#status GoogleDataLossPreventionJobTrigger#status}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#timeouts GoogleDataLossPreventionJobTrigger#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(inspect_job, dict):
            inspect_job = GoogleDataLossPreventionJobTriggerInspectJob(**inspect_job)
        if isinstance(timeouts, dict):
            timeouts = GoogleDataLossPreventionJobTriggerTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe4c0cfb50e9869a9b0d7c6b1af7a4b24fb732dde8e14a5cdc4ee7d8bf43dff8)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument parent", value=parent, expected_type=type_hints["parent"])
            check_type(argname="argument triggers", value=triggers, expected_type=type_hints["triggers"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument inspect_job", value=inspect_job, expected_type=type_hints["inspect_job"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "parent": parent,
            "triggers": triggers,
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
        if description is not None:
            self._values["description"] = description
        if display_name is not None:
            self._values["display_name"] = display_name
        if id is not None:
            self._values["id"] = id
        if inspect_job is not None:
            self._values["inspect_job"] = inspect_job
        if status is not None:
            self._values["status"] = status
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
    def parent(self) -> builtins.str:
        '''The parent of the trigger, either in the format 'projects/{{project}}' or 'projects/{{project}}/locations/{{location}}'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#parent GoogleDataLossPreventionJobTrigger#parent}
        '''
        result = self._values.get("parent")
        assert result is not None, "Required property 'parent' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def triggers(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDataLossPreventionJobTriggerTriggers"]]:
        '''triggers block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#triggers GoogleDataLossPreventionJobTrigger#triggers}
        '''
        result = self._values.get("triggers")
        assert result is not None, "Required property 'triggers' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDataLossPreventionJobTriggerTriggers"]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the job trigger.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#description GoogleDataLossPreventionJobTrigger#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        '''User set display name of the job trigger.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#display_name GoogleDataLossPreventionJobTrigger#display_name}
        '''
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#id GoogleDataLossPreventionJobTrigger#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def inspect_job(
        self,
    ) -> typing.Optional["GoogleDataLossPreventionJobTriggerInspectJob"]:
        '''inspect_job block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#inspect_job GoogleDataLossPreventionJobTrigger#inspect_job}
        '''
        result = self._values.get("inspect_job")
        return typing.cast(typing.Optional["GoogleDataLossPreventionJobTriggerInspectJob"], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''Whether the trigger is currently active. Default value: "HEALTHY" Possible values: ["PAUSED", "HEALTHY", "CANCELLED"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#status GoogleDataLossPreventionJobTrigger#status}
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleDataLossPreventionJobTriggerTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#timeouts GoogleDataLossPreventionJobTrigger#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleDataLossPreventionJobTriggerTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataLossPreventionJobTriggerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJob",
    jsii_struct_bases=[],
    name_mapping={
        "actions": "actions",
        "inspect_template_name": "inspectTemplateName",
        "storage_config": "storageConfig",
    },
)
class GoogleDataLossPreventionJobTriggerInspectJob:
    def __init__(
        self,
        *,
        actions: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDataLossPreventionJobTriggerInspectJobActions", typing.Dict[builtins.str, typing.Any]]]],
        inspect_template_name: builtins.str,
        storage_config: typing.Union["GoogleDataLossPreventionJobTriggerInspectJobStorageConfig", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param actions: actions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#actions GoogleDataLossPreventionJobTrigger#actions}
        :param inspect_template_name: The name of the template to run when this job is triggered. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#inspect_template_name GoogleDataLossPreventionJobTrigger#inspect_template_name}
        :param storage_config: storage_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#storage_config GoogleDataLossPreventionJobTrigger#storage_config}
        '''
        if isinstance(storage_config, dict):
            storage_config = GoogleDataLossPreventionJobTriggerInspectJobStorageConfig(**storage_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31c5535fb08c747f6d7a676bf8fa45703765fd33ca44680acc73179a4e6ea5c4)
            check_type(argname="argument actions", value=actions, expected_type=type_hints["actions"])
            check_type(argname="argument inspect_template_name", value=inspect_template_name, expected_type=type_hints["inspect_template_name"])
            check_type(argname="argument storage_config", value=storage_config, expected_type=type_hints["storage_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "actions": actions,
            "inspect_template_name": inspect_template_name,
            "storage_config": storage_config,
        }

    @builtins.property
    def actions(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDataLossPreventionJobTriggerInspectJobActions"]]:
        '''actions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#actions GoogleDataLossPreventionJobTrigger#actions}
        '''
        result = self._values.get("actions")
        assert result is not None, "Required property 'actions' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDataLossPreventionJobTriggerInspectJobActions"]], result)

    @builtins.property
    def inspect_template_name(self) -> builtins.str:
        '''The name of the template to run when this job is triggered.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#inspect_template_name GoogleDataLossPreventionJobTrigger#inspect_template_name}
        '''
        result = self._values.get("inspect_template_name")
        assert result is not None, "Required property 'inspect_template_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def storage_config(
        self,
    ) -> "GoogleDataLossPreventionJobTriggerInspectJobStorageConfig":
        '''storage_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#storage_config GoogleDataLossPreventionJobTrigger#storage_config}
        '''
        result = self._values.get("storage_config")
        assert result is not None, "Required property 'storage_config' is missing"
        return typing.cast("GoogleDataLossPreventionJobTriggerInspectJobStorageConfig", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataLossPreventionJobTriggerInspectJob(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobActions",
    jsii_struct_bases=[],
    name_mapping={"pub_sub": "pubSub", "save_findings": "saveFindings"},
)
class GoogleDataLossPreventionJobTriggerInspectJobActions:
    def __init__(
        self,
        *,
        pub_sub: typing.Optional[typing.Union["GoogleDataLossPreventionJobTriggerInspectJobActionsPubSub", typing.Dict[builtins.str, typing.Any]]] = None,
        save_findings: typing.Optional[typing.Union["GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindings", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param pub_sub: pub_sub block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#pub_sub GoogleDataLossPreventionJobTrigger#pub_sub}
        :param save_findings: save_findings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#save_findings GoogleDataLossPreventionJobTrigger#save_findings}
        '''
        if isinstance(pub_sub, dict):
            pub_sub = GoogleDataLossPreventionJobTriggerInspectJobActionsPubSub(**pub_sub)
        if isinstance(save_findings, dict):
            save_findings = GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindings(**save_findings)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15b42a7716ec1a69e95512aee92a77142168bf2ba103ac5b7dddf38ed3cb422a)
            check_type(argname="argument pub_sub", value=pub_sub, expected_type=type_hints["pub_sub"])
            check_type(argname="argument save_findings", value=save_findings, expected_type=type_hints["save_findings"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if pub_sub is not None:
            self._values["pub_sub"] = pub_sub
        if save_findings is not None:
            self._values["save_findings"] = save_findings

    @builtins.property
    def pub_sub(
        self,
    ) -> typing.Optional["GoogleDataLossPreventionJobTriggerInspectJobActionsPubSub"]:
        '''pub_sub block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#pub_sub GoogleDataLossPreventionJobTrigger#pub_sub}
        '''
        result = self._values.get("pub_sub")
        return typing.cast(typing.Optional["GoogleDataLossPreventionJobTriggerInspectJobActionsPubSub"], result)

    @builtins.property
    def save_findings(
        self,
    ) -> typing.Optional["GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindings"]:
        '''save_findings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#save_findings GoogleDataLossPreventionJobTrigger#save_findings}
        '''
        result = self._values.get("save_findings")
        return typing.cast(typing.Optional["GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindings"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataLossPreventionJobTriggerInspectJobActions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataLossPreventionJobTriggerInspectJobActionsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobActionsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3ada89d2b4bd33bfae64f00c58e4809bad95edb650a9394c8aaa9c9e2337946e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDataLossPreventionJobTriggerInspectJobActionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07166fc1b8bd816095ecb7f70f3ba1fbeca053dad1bc5b7d01a4053431d80813)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDataLossPreventionJobTriggerInspectJobActionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0238de74f76d7a0a29c10c53a0925e4d51afe78a72fb7ad2a45522d3069bde33)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ee82a645360b715581d58d263051a5a1e6dc2803c15c84550dadc383c52cd739)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6b8063ba8e553098fb83f03e0272a4f1fee5c25b923d920ebdddfbb750a42b77)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDataLossPreventionJobTriggerInspectJobActions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDataLossPreventionJobTriggerInspectJobActions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDataLossPreventionJobTriggerInspectJobActions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50eff909f45fb741e3f63b6ff9a2e0f68fa7dfe7a1895fd56473e3607f7e951c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDataLossPreventionJobTriggerInspectJobActionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobActionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4394ed47f2cbfccfc55da7085a29b6f6e08454cfb6e776155c90834adae16187)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putPubSub")
    def put_pub_sub(self, *, topic: builtins.str) -> None:
        '''
        :param topic: Cloud Pub/Sub topic to send notifications to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#topic GoogleDataLossPreventionJobTrigger#topic}
        '''
        value = GoogleDataLossPreventionJobTriggerInspectJobActionsPubSub(topic=topic)

        return typing.cast(None, jsii.invoke(self, "putPubSub", [value]))

    @jsii.member(jsii_name="putSaveFindings")
    def put_save_findings(
        self,
        *,
        output_config: typing.Union["GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfig", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param output_config: output_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#output_config GoogleDataLossPreventionJobTrigger#output_config}
        '''
        value = GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindings(
            output_config=output_config
        )

        return typing.cast(None, jsii.invoke(self, "putSaveFindings", [value]))

    @jsii.member(jsii_name="resetPubSub")
    def reset_pub_sub(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPubSub", []))

    @jsii.member(jsii_name="resetSaveFindings")
    def reset_save_findings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSaveFindings", []))

    @builtins.property
    @jsii.member(jsii_name="pubSub")
    def pub_sub(
        self,
    ) -> "GoogleDataLossPreventionJobTriggerInspectJobActionsPubSubOutputReference":
        return typing.cast("GoogleDataLossPreventionJobTriggerInspectJobActionsPubSubOutputReference", jsii.get(self, "pubSub"))

    @builtins.property
    @jsii.member(jsii_name="saveFindings")
    def save_findings(
        self,
    ) -> "GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputReference":
        return typing.cast("GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputReference", jsii.get(self, "saveFindings"))

    @builtins.property
    @jsii.member(jsii_name="pubSubInput")
    def pub_sub_input(
        self,
    ) -> typing.Optional["GoogleDataLossPreventionJobTriggerInspectJobActionsPubSub"]:
        return typing.cast(typing.Optional["GoogleDataLossPreventionJobTriggerInspectJobActionsPubSub"], jsii.get(self, "pubSubInput"))

    @builtins.property
    @jsii.member(jsii_name="saveFindingsInput")
    def save_findings_input(
        self,
    ) -> typing.Optional["GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindings"]:
        return typing.cast(typing.Optional["GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindings"], jsii.get(self, "saveFindingsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleDataLossPreventionJobTriggerInspectJobActions, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleDataLossPreventionJobTriggerInspectJobActions, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleDataLossPreventionJobTriggerInspectJobActions, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92811793c327aecb7abb5cd4b7a3a65582ea32c25476e925d6e290aba34d74f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobActionsPubSub",
    jsii_struct_bases=[],
    name_mapping={"topic": "topic"},
)
class GoogleDataLossPreventionJobTriggerInspectJobActionsPubSub:
    def __init__(self, *, topic: builtins.str) -> None:
        '''
        :param topic: Cloud Pub/Sub topic to send notifications to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#topic GoogleDataLossPreventionJobTrigger#topic}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87fd1c64967036117c81eccbe629974df83c57db2db988bcdddcae863d8c4762)
            check_type(argname="argument topic", value=topic, expected_type=type_hints["topic"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "topic": topic,
        }

    @builtins.property
    def topic(self) -> builtins.str:
        '''Cloud Pub/Sub topic to send notifications to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#topic GoogleDataLossPreventionJobTrigger#topic}
        '''
        result = self._values.get("topic")
        assert result is not None, "Required property 'topic' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataLossPreventionJobTriggerInspectJobActionsPubSub(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataLossPreventionJobTriggerInspectJobActionsPubSubOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobActionsPubSubOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cf8d19d736c64e816a63c8b64aea56b7df27cab33f0e0e63fc5a0606b424c66b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="topicInput")
    def topic_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "topicInput"))

    @builtins.property
    @jsii.member(jsii_name="topic")
    def topic(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "topic"))

    @topic.setter
    def topic(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa3eee9b5ad9285a28bebf2b19c26b4cbac2322b3b93664faa8c7465fe62701e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "topic", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobActionsPubSub]:
        return typing.cast(typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobActionsPubSub], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobActionsPubSub],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__556acc8c03cdc5ddd8f25d1a40959a946c1390484e86d3e904e3f69ee76551d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindings",
    jsii_struct_bases=[],
    name_mapping={"output_config": "outputConfig"},
)
class GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindings:
    def __init__(
        self,
        *,
        output_config: typing.Union["GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfig", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param output_config: output_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#output_config GoogleDataLossPreventionJobTrigger#output_config}
        '''
        if isinstance(output_config, dict):
            output_config = GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfig(**output_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__653c253abc1015bd8d0c854597a750c18d634b70116c5a33d070ca383cbe736c)
            check_type(argname="argument output_config", value=output_config, expected_type=type_hints["output_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "output_config": output_config,
        }

    @builtins.property
    def output_config(
        self,
    ) -> "GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfig":
        '''output_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#output_config GoogleDataLossPreventionJobTrigger#output_config}
        '''
        result = self._values.get("output_config")
        assert result is not None, "Required property 'output_config' is missing"
        return typing.cast("GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfig", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfig",
    jsii_struct_bases=[],
    name_mapping={"table": "table", "output_schema": "outputSchema"},
)
class GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfig:
    def __init__(
        self,
        *,
        table: typing.Union["GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfigTable", typing.Dict[builtins.str, typing.Any]],
        output_schema: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param table: table block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#table GoogleDataLossPreventionJobTrigger#table}
        :param output_schema: Schema used for writing the findings for Inspect jobs. This field is only used for Inspect and must be unspecified for Risk jobs. Columns are derived from the Finding object. If appending to an existing table, any columns from the predefined schema that are missing will be added. No columns in the existing table will be deleted. If unspecified, then all available columns will be used for a new table or an (existing) table with no schema, and no changes will be made to an existing table that has a schema. Only for use with external storage. Possible values: ["BASIC_COLUMNS", "GCS_COLUMNS", "DATASTORE_COLUMNS", "BIG_QUERY_COLUMNS", "ALL_COLUMNS"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#output_schema GoogleDataLossPreventionJobTrigger#output_schema}
        '''
        if isinstance(table, dict):
            table = GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfigTable(**table)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aff6af371263bf589c86949300f2695ca78641f969b4e20b7f81a977baba1860)
            check_type(argname="argument table", value=table, expected_type=type_hints["table"])
            check_type(argname="argument output_schema", value=output_schema, expected_type=type_hints["output_schema"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "table": table,
        }
        if output_schema is not None:
            self._values["output_schema"] = output_schema

    @builtins.property
    def table(
        self,
    ) -> "GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfigTable":
        '''table block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#table GoogleDataLossPreventionJobTrigger#table}
        '''
        result = self._values.get("table")
        assert result is not None, "Required property 'table' is missing"
        return typing.cast("GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfigTable", result)

    @builtins.property
    def output_schema(self) -> typing.Optional[builtins.str]:
        '''Schema used for writing the findings for Inspect jobs.

        This field is only used for
        Inspect and must be unspecified for Risk jobs. Columns are derived from the Finding
        object. If appending to an existing table, any columns from the predefined schema
        that are missing will be added. No columns in the existing table will be deleted.

        If unspecified, then all available columns will be used for a new table or an (existing)
        table with no schema, and no changes will be made to an existing table that has a schema.
        Only for use with external storage. Possible values: ["BASIC_COLUMNS", "GCS_COLUMNS", "DATASTORE_COLUMNS", "BIG_QUERY_COLUMNS", "ALL_COLUMNS"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#output_schema GoogleDataLossPreventionJobTrigger#output_schema}
        '''
        result = self._values.get("output_schema")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6bc68da821c9c3c64fbcbb6db56df7ddff67663508cae084765d8d851c9ab706)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putTable")
    def put_table(
        self,
        *,
        dataset_id: builtins.str,
        project_id: builtins.str,
        table_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param dataset_id: Dataset ID of the table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#dataset_id GoogleDataLossPreventionJobTrigger#dataset_id}
        :param project_id: The Google Cloud Platform project ID of the project containing the table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#project_id GoogleDataLossPreventionJobTrigger#project_id}
        :param table_id: Name of the table. If is not set a new one will be generated for you with the following format: 'dlp_googleapis_yyyy_mm_dd_[dlp_job_id]'. Pacific timezone will be used for generating the date details. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#table_id GoogleDataLossPreventionJobTrigger#table_id}
        '''
        value = GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfigTable(
            dataset_id=dataset_id, project_id=project_id, table_id=table_id
        )

        return typing.cast(None, jsii.invoke(self, "putTable", [value]))

    @jsii.member(jsii_name="resetOutputSchema")
    def reset_output_schema(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOutputSchema", []))

    @builtins.property
    @jsii.member(jsii_name="table")
    def table(
        self,
    ) -> "GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfigTableOutputReference":
        return typing.cast("GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfigTableOutputReference", jsii.get(self, "table"))

    @builtins.property
    @jsii.member(jsii_name="outputSchemaInput")
    def output_schema_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "outputSchemaInput"))

    @builtins.property
    @jsii.member(jsii_name="tableInput")
    def table_input(
        self,
    ) -> typing.Optional["GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfigTable"]:
        return typing.cast(typing.Optional["GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfigTable"], jsii.get(self, "tableInput"))

    @builtins.property
    @jsii.member(jsii_name="outputSchema")
    def output_schema(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "outputSchema"))

    @output_schema.setter
    def output_schema(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80abc1a808d2392cdf67a6ba7da1ebb8b1ef4b274541e35abb57c6ed9b687113)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outputSchema", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfig]:
        return typing.cast(typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d887bdf2aaff0732dbe05fe4f94be5898830bc575273bd6022ae1e61bdfd582)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfigTable",
    jsii_struct_bases=[],
    name_mapping={
        "dataset_id": "datasetId",
        "project_id": "projectId",
        "table_id": "tableId",
    },
)
class GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfigTable:
    def __init__(
        self,
        *,
        dataset_id: builtins.str,
        project_id: builtins.str,
        table_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param dataset_id: Dataset ID of the table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#dataset_id GoogleDataLossPreventionJobTrigger#dataset_id}
        :param project_id: The Google Cloud Platform project ID of the project containing the table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#project_id GoogleDataLossPreventionJobTrigger#project_id}
        :param table_id: Name of the table. If is not set a new one will be generated for you with the following format: 'dlp_googleapis_yyyy_mm_dd_[dlp_job_id]'. Pacific timezone will be used for generating the date details. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#table_id GoogleDataLossPreventionJobTrigger#table_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4eb1dafabd8bf35ef4fd6a6b8919997be86c26940a85b6b4846de19c08ad1b37)
            check_type(argname="argument dataset_id", value=dataset_id, expected_type=type_hints["dataset_id"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument table_id", value=table_id, expected_type=type_hints["table_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "dataset_id": dataset_id,
            "project_id": project_id,
        }
        if table_id is not None:
            self._values["table_id"] = table_id

    @builtins.property
    def dataset_id(self) -> builtins.str:
        '''Dataset ID of the table.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#dataset_id GoogleDataLossPreventionJobTrigger#dataset_id}
        '''
        result = self._values.get("dataset_id")
        assert result is not None, "Required property 'dataset_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project_id(self) -> builtins.str:
        '''The Google Cloud Platform project ID of the project containing the table.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#project_id GoogleDataLossPreventionJobTrigger#project_id}
        '''
        result = self._values.get("project_id")
        assert result is not None, "Required property 'project_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def table_id(self) -> typing.Optional[builtins.str]:
        '''Name of the table.

        If is not set a new one will be generated for you with the following format:
        'dlp_googleapis_yyyy_mm_dd_[dlp_job_id]'. Pacific timezone will be used for generating the date details.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#table_id GoogleDataLossPreventionJobTrigger#table_id}
        '''
        result = self._values.get("table_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfigTable(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfigTableOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfigTableOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__99c059279c67702a6689b344f4cd666a68c2ed66b484d1909063aaed14817e4a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetTableId")
    def reset_table_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTableId", []))

    @builtins.property
    @jsii.member(jsii_name="datasetIdInput")
    def dataset_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datasetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="projectIdInput")
    def project_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectIdInput"))

    @builtins.property
    @jsii.member(jsii_name="tableIdInput")
    def table_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableIdInput"))

    @builtins.property
    @jsii.member(jsii_name="datasetId")
    def dataset_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datasetId"))

    @dataset_id.setter
    def dataset_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e92610c5c8cf1f5dfe8711345371a151da3d8ebf71276b277805e8a028e9d0f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datasetId", value)

    @builtins.property
    @jsii.member(jsii_name="projectId")
    def project_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "projectId"))

    @project_id.setter
    def project_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82a626d7a5ed0b54ee4b293017fbf1086c98819858bcb818e18287cfa718ea58)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectId", value)

    @builtins.property
    @jsii.member(jsii_name="tableId")
    def table_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tableId"))

    @table_id.setter
    def table_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0efe03f64d4c645e92616373817cec6e6e59824d45ffc2a21dc6fec64d69651c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfigTable]:
        return typing.cast(typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfigTable], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfigTable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8967065c5338b7e415a4b1b5861e9b30235e4f7fe4d9eb1afa911cb6336da5cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e6fb2a2e6c436bd5f88c5ef9cab9483f7babb57f49f83770d8a316ebd5b8c566)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putOutputConfig")
    def put_output_config(
        self,
        *,
        table: typing.Union[GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfigTable, typing.Dict[builtins.str, typing.Any]],
        output_schema: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param table: table block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#table GoogleDataLossPreventionJobTrigger#table}
        :param output_schema: Schema used for writing the findings for Inspect jobs. This field is only used for Inspect and must be unspecified for Risk jobs. Columns are derived from the Finding object. If appending to an existing table, any columns from the predefined schema that are missing will be added. No columns in the existing table will be deleted. If unspecified, then all available columns will be used for a new table or an (existing) table with no schema, and no changes will be made to an existing table that has a schema. Only for use with external storage. Possible values: ["BASIC_COLUMNS", "GCS_COLUMNS", "DATASTORE_COLUMNS", "BIG_QUERY_COLUMNS", "ALL_COLUMNS"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#output_schema GoogleDataLossPreventionJobTrigger#output_schema}
        '''
        value = GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfig(
            table=table, output_schema=output_schema
        )

        return typing.cast(None, jsii.invoke(self, "putOutputConfig", [value]))

    @builtins.property
    @jsii.member(jsii_name="outputConfig")
    def output_config(
        self,
    ) -> GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfigOutputReference:
        return typing.cast(GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfigOutputReference, jsii.get(self, "outputConfig"))

    @builtins.property
    @jsii.member(jsii_name="outputConfigInput")
    def output_config_input(
        self,
    ) -> typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfig]:
        return typing.cast(typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfig], jsii.get(self, "outputConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindings]:
        return typing.cast(typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f092e5d3963e076c06dc47c696b1a744f5d801677b9fbff68c8a8ade0a8bfb2b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDataLossPreventionJobTriggerInspectJobOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5cad2701fbf31fd40d603a71601e1c5aa7850d18835bcc47b7c0c4b63683fa9d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putActions")
    def put_actions(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDataLossPreventionJobTriggerInspectJobActions, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9e35eb8942f23d8ed4a312ebb111d2422a8e579c93e09bdf81499fd7b406f31)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putActions", [value]))

    @jsii.member(jsii_name="putStorageConfig")
    def put_storage_config(
        self,
        *,
        big_query_options: typing.Optional[typing.Union["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        cloud_storage_options: typing.Optional[typing.Union["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        datastore_options: typing.Optional[typing.Union["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        timespan_config: typing.Optional[typing.Union["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param big_query_options: big_query_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#big_query_options GoogleDataLossPreventionJobTrigger#big_query_options}
        :param cloud_storage_options: cloud_storage_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#cloud_storage_options GoogleDataLossPreventionJobTrigger#cloud_storage_options}
        :param datastore_options: datastore_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#datastore_options GoogleDataLossPreventionJobTrigger#datastore_options}
        :param timespan_config: timespan_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#timespan_config GoogleDataLossPreventionJobTrigger#timespan_config}
        '''
        value = GoogleDataLossPreventionJobTriggerInspectJobStorageConfig(
            big_query_options=big_query_options,
            cloud_storage_options=cloud_storage_options,
            datastore_options=datastore_options,
            timespan_config=timespan_config,
        )

        return typing.cast(None, jsii.invoke(self, "putStorageConfig", [value]))

    @builtins.property
    @jsii.member(jsii_name="actions")
    def actions(self) -> GoogleDataLossPreventionJobTriggerInspectJobActionsList:
        return typing.cast(GoogleDataLossPreventionJobTriggerInspectJobActionsList, jsii.get(self, "actions"))

    @builtins.property
    @jsii.member(jsii_name="storageConfig")
    def storage_config(
        self,
    ) -> "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigOutputReference":
        return typing.cast("GoogleDataLossPreventionJobTriggerInspectJobStorageConfigOutputReference", jsii.get(self, "storageConfig"))

    @builtins.property
    @jsii.member(jsii_name="actionsInput")
    def actions_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDataLossPreventionJobTriggerInspectJobActions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDataLossPreventionJobTriggerInspectJobActions]]], jsii.get(self, "actionsInput"))

    @builtins.property
    @jsii.member(jsii_name="inspectTemplateNameInput")
    def inspect_template_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "inspectTemplateNameInput"))

    @builtins.property
    @jsii.member(jsii_name="storageConfigInput")
    def storage_config_input(
        self,
    ) -> typing.Optional["GoogleDataLossPreventionJobTriggerInspectJobStorageConfig"]:
        return typing.cast(typing.Optional["GoogleDataLossPreventionJobTriggerInspectJobStorageConfig"], jsii.get(self, "storageConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="inspectTemplateName")
    def inspect_template_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "inspectTemplateName"))

    @inspect_template_name.setter
    def inspect_template_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ca2ccdff2b660c95c1767469594f616cd41abc70530bab3071929b0939ff037)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inspectTemplateName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataLossPreventionJobTriggerInspectJob]:
        return typing.cast(typing.Optional[GoogleDataLossPreventionJobTriggerInspectJob], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataLossPreventionJobTriggerInspectJob],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bfdd83e0c3fc087e01e8d74b9bab7830f9fdb30e5d3cd4994e3ebb584700b261)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobStorageConfig",
    jsii_struct_bases=[],
    name_mapping={
        "big_query_options": "bigQueryOptions",
        "cloud_storage_options": "cloudStorageOptions",
        "datastore_options": "datastoreOptions",
        "timespan_config": "timespanConfig",
    },
)
class GoogleDataLossPreventionJobTriggerInspectJobStorageConfig:
    def __init__(
        self,
        *,
        big_query_options: typing.Optional[typing.Union["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        cloud_storage_options: typing.Optional[typing.Union["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        datastore_options: typing.Optional[typing.Union["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        timespan_config: typing.Optional[typing.Union["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param big_query_options: big_query_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#big_query_options GoogleDataLossPreventionJobTrigger#big_query_options}
        :param cloud_storage_options: cloud_storage_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#cloud_storage_options GoogleDataLossPreventionJobTrigger#cloud_storage_options}
        :param datastore_options: datastore_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#datastore_options GoogleDataLossPreventionJobTrigger#datastore_options}
        :param timespan_config: timespan_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#timespan_config GoogleDataLossPreventionJobTrigger#timespan_config}
        '''
        if isinstance(big_query_options, dict):
            big_query_options = GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptions(**big_query_options)
        if isinstance(cloud_storage_options, dict):
            cloud_storage_options = GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptions(**cloud_storage_options)
        if isinstance(datastore_options, dict):
            datastore_options = GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptions(**datastore_options)
        if isinstance(timespan_config, dict):
            timespan_config = GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfig(**timespan_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__470cc6c8770a59ea47874d7524831f8907158a8c09276bea5107c098d0b29df4)
            check_type(argname="argument big_query_options", value=big_query_options, expected_type=type_hints["big_query_options"])
            check_type(argname="argument cloud_storage_options", value=cloud_storage_options, expected_type=type_hints["cloud_storage_options"])
            check_type(argname="argument datastore_options", value=datastore_options, expected_type=type_hints["datastore_options"])
            check_type(argname="argument timespan_config", value=timespan_config, expected_type=type_hints["timespan_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if big_query_options is not None:
            self._values["big_query_options"] = big_query_options
        if cloud_storage_options is not None:
            self._values["cloud_storage_options"] = cloud_storage_options
        if datastore_options is not None:
            self._values["datastore_options"] = datastore_options
        if timespan_config is not None:
            self._values["timespan_config"] = timespan_config

    @builtins.property
    def big_query_options(
        self,
    ) -> typing.Optional["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptions"]:
        '''big_query_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#big_query_options GoogleDataLossPreventionJobTrigger#big_query_options}
        '''
        result = self._values.get("big_query_options")
        return typing.cast(typing.Optional["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptions"], result)

    @builtins.property
    def cloud_storage_options(
        self,
    ) -> typing.Optional["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptions"]:
        '''cloud_storage_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#cloud_storage_options GoogleDataLossPreventionJobTrigger#cloud_storage_options}
        '''
        result = self._values.get("cloud_storage_options")
        return typing.cast(typing.Optional["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptions"], result)

    @builtins.property
    def datastore_options(
        self,
    ) -> typing.Optional["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptions"]:
        '''datastore_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#datastore_options GoogleDataLossPreventionJobTrigger#datastore_options}
        '''
        result = self._values.get("datastore_options")
        return typing.cast(typing.Optional["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptions"], result)

    @builtins.property
    def timespan_config(
        self,
    ) -> typing.Optional["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfig"]:
        '''timespan_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#timespan_config GoogleDataLossPreventionJobTrigger#timespan_config}
        '''
        result = self._values.get("timespan_config")
        return typing.cast(typing.Optional["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataLossPreventionJobTriggerInspectJobStorageConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptions",
    jsii_struct_bases=[],
    name_mapping={
        "table_reference": "tableReference",
        "rows_limit": "rowsLimit",
        "rows_limit_percent": "rowsLimitPercent",
        "sample_method": "sampleMethod",
    },
)
class GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptions:
    def __init__(
        self,
        *,
        table_reference: typing.Union["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptionsTableReference", typing.Dict[builtins.str, typing.Any]],
        rows_limit: typing.Optional[jsii.Number] = None,
        rows_limit_percent: typing.Optional[jsii.Number] = None,
        sample_method: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param table_reference: table_reference block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#table_reference GoogleDataLossPreventionJobTrigger#table_reference}
        :param rows_limit: Max number of rows to scan. If the table has more rows than this value, the rest of the rows are omitted. If not set, or if set to 0, all rows will be scanned. Only one of rowsLimit and rowsLimitPercent can be specified. Cannot be used in conjunction with TimespanConfig. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#rows_limit GoogleDataLossPreventionJobTrigger#rows_limit}
        :param rows_limit_percent: Max percentage of rows to scan. The rest are omitted. The number of rows scanned is rounded down. Must be between 0 and 100, inclusively. Both 0 and 100 means no limit. Defaults to 0. Only one of rowsLimit and rowsLimitPercent can be specified. Cannot be used in conjunction with TimespanConfig. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#rows_limit_percent GoogleDataLossPreventionJobTrigger#rows_limit_percent}
        :param sample_method: How to sample rows if not all rows are scanned. Meaningful only when used in conjunction with either rowsLimit or rowsLimitPercent. If not specified, rows are scanned in the order BigQuery reads them. Default value: "TOP" Possible values: ["TOP", "RANDOM_START"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#sample_method GoogleDataLossPreventionJobTrigger#sample_method}
        '''
        if isinstance(table_reference, dict):
            table_reference = GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptionsTableReference(**table_reference)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b8106c2022e7767c786de413eb10f7ae98775626901c5a3ab4abe84bd6488cb)
            check_type(argname="argument table_reference", value=table_reference, expected_type=type_hints["table_reference"])
            check_type(argname="argument rows_limit", value=rows_limit, expected_type=type_hints["rows_limit"])
            check_type(argname="argument rows_limit_percent", value=rows_limit_percent, expected_type=type_hints["rows_limit_percent"])
            check_type(argname="argument sample_method", value=sample_method, expected_type=type_hints["sample_method"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "table_reference": table_reference,
        }
        if rows_limit is not None:
            self._values["rows_limit"] = rows_limit
        if rows_limit_percent is not None:
            self._values["rows_limit_percent"] = rows_limit_percent
        if sample_method is not None:
            self._values["sample_method"] = sample_method

    @builtins.property
    def table_reference(
        self,
    ) -> "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptionsTableReference":
        '''table_reference block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#table_reference GoogleDataLossPreventionJobTrigger#table_reference}
        '''
        result = self._values.get("table_reference")
        assert result is not None, "Required property 'table_reference' is missing"
        return typing.cast("GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptionsTableReference", result)

    @builtins.property
    def rows_limit(self) -> typing.Optional[jsii.Number]:
        '''Max number of rows to scan.

        If the table has more rows than this value, the rest of the rows are omitted.
        If not set, or if set to 0, all rows will be scanned. Only one of rowsLimit and rowsLimitPercent can be
        specified. Cannot be used in conjunction with TimespanConfig.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#rows_limit GoogleDataLossPreventionJobTrigger#rows_limit}
        '''
        result = self._values.get("rows_limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def rows_limit_percent(self) -> typing.Optional[jsii.Number]:
        '''Max percentage of rows to scan.

        The rest are omitted. The number of rows scanned is rounded down.
        Must be between 0 and 100, inclusively. Both 0 and 100 means no limit. Defaults to 0. Only one of
        rowsLimit and rowsLimitPercent can be specified. Cannot be used in conjunction with TimespanConfig.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#rows_limit_percent GoogleDataLossPreventionJobTrigger#rows_limit_percent}
        '''
        result = self._values.get("rows_limit_percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def sample_method(self) -> typing.Optional[builtins.str]:
        '''How to sample rows if not all rows are scanned.

        Meaningful only when used in conjunction with either
        rowsLimit or rowsLimitPercent. If not specified, rows are scanned in the order BigQuery reads them. Default value: "TOP" Possible values: ["TOP", "RANDOM_START"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#sample_method GoogleDataLossPreventionJobTrigger#sample_method}
        '''
        result = self._values.get("sample_method")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1a9f8a81e90a8be6807dac86aa0133dd7e302e20974c9945a892065221f13da5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putTableReference")
    def put_table_reference(
        self,
        *,
        dataset_id: builtins.str,
        project_id: builtins.str,
        table_id: builtins.str,
    ) -> None:
        '''
        :param dataset_id: The dataset ID of the table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#dataset_id GoogleDataLossPreventionJobTrigger#dataset_id}
        :param project_id: The Google Cloud Platform project ID of the project containing the table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#project_id GoogleDataLossPreventionJobTrigger#project_id}
        :param table_id: The name of the table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#table_id GoogleDataLossPreventionJobTrigger#table_id}
        '''
        value = GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptionsTableReference(
            dataset_id=dataset_id, project_id=project_id, table_id=table_id
        )

        return typing.cast(None, jsii.invoke(self, "putTableReference", [value]))

    @jsii.member(jsii_name="resetRowsLimit")
    def reset_rows_limit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRowsLimit", []))

    @jsii.member(jsii_name="resetRowsLimitPercent")
    def reset_rows_limit_percent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRowsLimitPercent", []))

    @jsii.member(jsii_name="resetSampleMethod")
    def reset_sample_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSampleMethod", []))

    @builtins.property
    @jsii.member(jsii_name="tableReference")
    def table_reference(
        self,
    ) -> "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptionsTableReferenceOutputReference":
        return typing.cast("GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptionsTableReferenceOutputReference", jsii.get(self, "tableReference"))

    @builtins.property
    @jsii.member(jsii_name="rowsLimitInput")
    def rows_limit_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "rowsLimitInput"))

    @builtins.property
    @jsii.member(jsii_name="rowsLimitPercentInput")
    def rows_limit_percent_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "rowsLimitPercentInput"))

    @builtins.property
    @jsii.member(jsii_name="sampleMethodInput")
    def sample_method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sampleMethodInput"))

    @builtins.property
    @jsii.member(jsii_name="tableReferenceInput")
    def table_reference_input(
        self,
    ) -> typing.Optional["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptionsTableReference"]:
        return typing.cast(typing.Optional["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptionsTableReference"], jsii.get(self, "tableReferenceInput"))

    @builtins.property
    @jsii.member(jsii_name="rowsLimit")
    def rows_limit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "rowsLimit"))

    @rows_limit.setter
    def rows_limit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54f9a74f63452d66fa169c13d48c1d148d56f299ca72becc27bfa74e003f7997)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rowsLimit", value)

    @builtins.property
    @jsii.member(jsii_name="rowsLimitPercent")
    def rows_limit_percent(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "rowsLimitPercent"))

    @rows_limit_percent.setter
    def rows_limit_percent(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__638ab826ec221a30183f15ea7a93b6b2c0954c6aaf9e34371b5efb54e7e0ff31)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rowsLimitPercent", value)

    @builtins.property
    @jsii.member(jsii_name="sampleMethod")
    def sample_method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sampleMethod"))

    @sample_method.setter
    def sample_method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fae2d214021a015e12903693b0024b7598ec3285936c77bfbc919e04fec7a545)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sampleMethod", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptions]:
        return typing.cast(typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64309101dd0816e55471bc342d94dab5c889be4ab5a6cd831b801c4f633dfc25)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptionsTableReference",
    jsii_struct_bases=[],
    name_mapping={
        "dataset_id": "datasetId",
        "project_id": "projectId",
        "table_id": "tableId",
    },
)
class GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptionsTableReference:
    def __init__(
        self,
        *,
        dataset_id: builtins.str,
        project_id: builtins.str,
        table_id: builtins.str,
    ) -> None:
        '''
        :param dataset_id: The dataset ID of the table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#dataset_id GoogleDataLossPreventionJobTrigger#dataset_id}
        :param project_id: The Google Cloud Platform project ID of the project containing the table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#project_id GoogleDataLossPreventionJobTrigger#project_id}
        :param table_id: The name of the table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#table_id GoogleDataLossPreventionJobTrigger#table_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c570b011b1902eb4439e906ad7c4e7405213ed752661ce8e191b0c2b2f9cdb84)
            check_type(argname="argument dataset_id", value=dataset_id, expected_type=type_hints["dataset_id"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument table_id", value=table_id, expected_type=type_hints["table_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "dataset_id": dataset_id,
            "project_id": project_id,
            "table_id": table_id,
        }

    @builtins.property
    def dataset_id(self) -> builtins.str:
        '''The dataset ID of the table.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#dataset_id GoogleDataLossPreventionJobTrigger#dataset_id}
        '''
        result = self._values.get("dataset_id")
        assert result is not None, "Required property 'dataset_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project_id(self) -> builtins.str:
        '''The Google Cloud Platform project ID of the project containing the table.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#project_id GoogleDataLossPreventionJobTrigger#project_id}
        '''
        result = self._values.get("project_id")
        assert result is not None, "Required property 'project_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def table_id(self) -> builtins.str:
        '''The name of the table.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#table_id GoogleDataLossPreventionJobTrigger#table_id}
        '''
        result = self._values.get("table_id")
        assert result is not None, "Required property 'table_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptionsTableReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptionsTableReferenceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptionsTableReferenceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9e58f5085c6ec7ab98460345a4c26d6b07d990c2b0274f99840caf7746bcb823)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="datasetIdInput")
    def dataset_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datasetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="projectIdInput")
    def project_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectIdInput"))

    @builtins.property
    @jsii.member(jsii_name="tableIdInput")
    def table_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableIdInput"))

    @builtins.property
    @jsii.member(jsii_name="datasetId")
    def dataset_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datasetId"))

    @dataset_id.setter
    def dataset_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8df201893ff971d20c66010e932b24e8996f55564ae5910e27201550aa455c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datasetId", value)

    @builtins.property
    @jsii.member(jsii_name="projectId")
    def project_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "projectId"))

    @project_id.setter
    def project_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90a0118fbbab94dda57c4129b3648ace1cd737df5c5ba10d237c8d264d9c6de1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectId", value)

    @builtins.property
    @jsii.member(jsii_name="tableId")
    def table_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tableId"))

    @table_id.setter
    def table_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__193303ff80d001e7b840306982962241d4ba1e3b01e25d659ab651fcaa3e166d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptionsTableReference]:
        return typing.cast(typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptionsTableReference], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptionsTableReference],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5237a92fd8cb9a7ca01b3f05f7a27d7f48ce923e7358bfc3aee8e99bddb0c596)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptions",
    jsii_struct_bases=[],
    name_mapping={
        "file_set": "fileSet",
        "bytes_limit_per_file": "bytesLimitPerFile",
        "bytes_limit_per_file_percent": "bytesLimitPerFilePercent",
        "files_limit_percent": "filesLimitPercent",
        "file_types": "fileTypes",
        "sample_method": "sampleMethod",
    },
)
class GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptions:
    def __init__(
        self,
        *,
        file_set: typing.Union["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSet", typing.Dict[builtins.str, typing.Any]],
        bytes_limit_per_file: typing.Optional[jsii.Number] = None,
        bytes_limit_per_file_percent: typing.Optional[jsii.Number] = None,
        files_limit_percent: typing.Optional[jsii.Number] = None,
        file_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        sample_method: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param file_set: file_set block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#file_set GoogleDataLossPreventionJobTrigger#file_set}
        :param bytes_limit_per_file: Max number of bytes to scan from a file. If a scanned file's size is bigger than this value then the rest of the bytes are omitted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#bytes_limit_per_file GoogleDataLossPreventionJobTrigger#bytes_limit_per_file}
        :param bytes_limit_per_file_percent: Max percentage of bytes to scan from a file. The rest are omitted. The number of bytes scanned is rounded down. Must be between 0 and 100, inclusively. Both 0 and 100 means no limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#bytes_limit_per_file_percent GoogleDataLossPreventionJobTrigger#bytes_limit_per_file_percent}
        :param files_limit_percent: Limits the number of files to scan to this percentage of the input FileSet. Number of files scanned is rounded down. Must be between 0 and 100, inclusively. Both 0 and 100 means no limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#files_limit_percent GoogleDataLossPreventionJobTrigger#files_limit_percent}
        :param file_types: List of file type groups to include in the scan. If empty, all files are scanned and available data format processors are applied. In addition, the binary content of the selected files is always scanned as well. Images are scanned only as binary if the specified region does not support image inspection and no fileTypes were specified. Possible values: ["BINARY_FILE", "TEXT_FILE", "IMAGE", "WORD", "PDF", "AVRO", "CSV", "TSV"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#file_types GoogleDataLossPreventionJobTrigger#file_types}
        :param sample_method: How to sample bytes if not all bytes are scanned. Meaningful only when used in conjunction with bytesLimitPerFile. If not specified, scanning would start from the top. Possible values: ["TOP", "RANDOM_START"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#sample_method GoogleDataLossPreventionJobTrigger#sample_method}
        '''
        if isinstance(file_set, dict):
            file_set = GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSet(**file_set)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__011773d25ad301e98af04c879d6c51700237ae264b51dedc7fe8d7dc589a3966)
            check_type(argname="argument file_set", value=file_set, expected_type=type_hints["file_set"])
            check_type(argname="argument bytes_limit_per_file", value=bytes_limit_per_file, expected_type=type_hints["bytes_limit_per_file"])
            check_type(argname="argument bytes_limit_per_file_percent", value=bytes_limit_per_file_percent, expected_type=type_hints["bytes_limit_per_file_percent"])
            check_type(argname="argument files_limit_percent", value=files_limit_percent, expected_type=type_hints["files_limit_percent"])
            check_type(argname="argument file_types", value=file_types, expected_type=type_hints["file_types"])
            check_type(argname="argument sample_method", value=sample_method, expected_type=type_hints["sample_method"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "file_set": file_set,
        }
        if bytes_limit_per_file is not None:
            self._values["bytes_limit_per_file"] = bytes_limit_per_file
        if bytes_limit_per_file_percent is not None:
            self._values["bytes_limit_per_file_percent"] = bytes_limit_per_file_percent
        if files_limit_percent is not None:
            self._values["files_limit_percent"] = files_limit_percent
        if file_types is not None:
            self._values["file_types"] = file_types
        if sample_method is not None:
            self._values["sample_method"] = sample_method

    @builtins.property
    def file_set(
        self,
    ) -> "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSet":
        '''file_set block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#file_set GoogleDataLossPreventionJobTrigger#file_set}
        '''
        result = self._values.get("file_set")
        assert result is not None, "Required property 'file_set' is missing"
        return typing.cast("GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSet", result)

    @builtins.property
    def bytes_limit_per_file(self) -> typing.Optional[jsii.Number]:
        '''Max number of bytes to scan from a file.

        If a scanned file's size is bigger than this value
        then the rest of the bytes are omitted.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#bytes_limit_per_file GoogleDataLossPreventionJobTrigger#bytes_limit_per_file}
        '''
        result = self._values.get("bytes_limit_per_file")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def bytes_limit_per_file_percent(self) -> typing.Optional[jsii.Number]:
        '''Max percentage of bytes to scan from a file.

        The rest are omitted. The number of bytes scanned is rounded down.
        Must be between 0 and 100, inclusively. Both 0 and 100 means no limit.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#bytes_limit_per_file_percent GoogleDataLossPreventionJobTrigger#bytes_limit_per_file_percent}
        '''
        result = self._values.get("bytes_limit_per_file_percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def files_limit_percent(self) -> typing.Optional[jsii.Number]:
        '''Limits the number of files to scan to this percentage of the input FileSet.

        Number of files scanned is rounded down.
        Must be between 0 and 100, inclusively. Both 0 and 100 means no limit.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#files_limit_percent GoogleDataLossPreventionJobTrigger#files_limit_percent}
        '''
        result = self._values.get("files_limit_percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def file_types(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of file type groups to include in the scan.

        If empty, all files are scanned and available data
        format processors are applied. In addition, the binary content of the selected files is always scanned as well.
        Images are scanned only as binary if the specified region does not support image inspection and no fileTypes were specified. Possible values: ["BINARY_FILE", "TEXT_FILE", "IMAGE", "WORD", "PDF", "AVRO", "CSV", "TSV"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#file_types GoogleDataLossPreventionJobTrigger#file_types}
        '''
        result = self._values.get("file_types")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def sample_method(self) -> typing.Optional[builtins.str]:
        '''How to sample bytes if not all bytes are scanned.

        Meaningful only when used in conjunction with bytesLimitPerFile.
        If not specified, scanning would start from the top. Possible values: ["TOP", "RANDOM_START"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#sample_method GoogleDataLossPreventionJobTrigger#sample_method}
        '''
        result = self._values.get("sample_method")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSet",
    jsii_struct_bases=[],
    name_mapping={"regex_file_set": "regexFileSet", "url": "url"},
)
class GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSet:
    def __init__(
        self,
        *,
        regex_file_set: typing.Optional[typing.Union["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetRegexFileSet", typing.Dict[builtins.str, typing.Any]]] = None,
        url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param regex_file_set: regex_file_set block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#regex_file_set GoogleDataLossPreventionJobTrigger#regex_file_set}
        :param url: The Cloud Storage url of the file(s) to scan, in the format 'gs:///'. Trailing wildcard in the path is allowed. If the url ends in a trailing slash, the bucket or directory represented by the url will be scanned non-recursively (content in sub-directories will not be scanned). This means that 'gs://mybucket/' is equivalent to 'gs://mybucket/*', and 'gs://mybucket/directory/' is equivalent to 'gs://mybucket/directory/*'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#url GoogleDataLossPreventionJobTrigger#url}
        '''
        if isinstance(regex_file_set, dict):
            regex_file_set = GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetRegexFileSet(**regex_file_set)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea613cbb1936411886dfcf181274f55ce8c9f414d97002627aa94cc06dbb831b)
            check_type(argname="argument regex_file_set", value=regex_file_set, expected_type=type_hints["regex_file_set"])
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if regex_file_set is not None:
            self._values["regex_file_set"] = regex_file_set
        if url is not None:
            self._values["url"] = url

    @builtins.property
    def regex_file_set(
        self,
    ) -> typing.Optional["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetRegexFileSet"]:
        '''regex_file_set block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#regex_file_set GoogleDataLossPreventionJobTrigger#regex_file_set}
        '''
        result = self._values.get("regex_file_set")
        return typing.cast(typing.Optional["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetRegexFileSet"], result)

    @builtins.property
    def url(self) -> typing.Optional[builtins.str]:
        '''The Cloud Storage url of the file(s) to scan, in the format 'gs:///'. Trailing wildcard in the path is allowed.

        If the url ends in a trailing slash, the bucket or directory represented by the url will be scanned
        non-recursively (content in sub-directories will not be scanned). This means that 'gs://mybucket/' is
        equivalent to 'gs://mybucket/*', and 'gs://mybucket/directory/' is equivalent to 'gs://mybucket/directory/*'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#url GoogleDataLossPreventionJobTrigger#url}
        '''
        result = self._values.get("url")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSet(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__87ddf879abec18d153c9ecb1fe9ce8eab5597cef4a48369ac120174c705f78f3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRegexFileSet")
    def put_regex_file_set(
        self,
        *,
        bucket_name: builtins.str,
        exclude_regex: typing.Optional[typing.Sequence[builtins.str]] = None,
        include_regex: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param bucket_name: The name of a Cloud Storage bucket. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#bucket_name GoogleDataLossPreventionJobTrigger#bucket_name}
        :param exclude_regex: A list of regular expressions matching file paths to exclude. All files in the bucket that match at least one of these regular expressions will be excluded from the scan. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#exclude_regex GoogleDataLossPreventionJobTrigger#exclude_regex}
        :param include_regex: A list of regular expressions matching file paths to include. All files in the bucket that match at least one of these regular expressions will be included in the set of files, except for those that also match an item in excludeRegex. Leaving this field empty will match all files by default (this is equivalent to including .* in the list) Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#include_regex GoogleDataLossPreventionJobTrigger#include_regex}
        '''
        value = GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetRegexFileSet(
            bucket_name=bucket_name,
            exclude_regex=exclude_regex,
            include_regex=include_regex,
        )

        return typing.cast(None, jsii.invoke(self, "putRegexFileSet", [value]))

    @jsii.member(jsii_name="resetRegexFileSet")
    def reset_regex_file_set(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegexFileSet", []))

    @jsii.member(jsii_name="resetUrl")
    def reset_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUrl", []))

    @builtins.property
    @jsii.member(jsii_name="regexFileSet")
    def regex_file_set(
        self,
    ) -> "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetRegexFileSetOutputReference":
        return typing.cast("GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetRegexFileSetOutputReference", jsii.get(self, "regexFileSet"))

    @builtins.property
    @jsii.member(jsii_name="regexFileSetInput")
    def regex_file_set_input(
        self,
    ) -> typing.Optional["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetRegexFileSet"]:
        return typing.cast(typing.Optional["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetRegexFileSet"], jsii.get(self, "regexFileSetInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d479b80697bd65be485eaa94a87df63c8d987f4fc05a9d027b3d3bf51ed30de9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSet]:
        return typing.cast(typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSet], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSet],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45d05c35a866a2acf54b439f9f9646749fe4d5aa3705c2acf19ee2f00659f9b0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetRegexFileSet",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_name": "bucketName",
        "exclude_regex": "excludeRegex",
        "include_regex": "includeRegex",
    },
)
class GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetRegexFileSet:
    def __init__(
        self,
        *,
        bucket_name: builtins.str,
        exclude_regex: typing.Optional[typing.Sequence[builtins.str]] = None,
        include_regex: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param bucket_name: The name of a Cloud Storage bucket. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#bucket_name GoogleDataLossPreventionJobTrigger#bucket_name}
        :param exclude_regex: A list of regular expressions matching file paths to exclude. All files in the bucket that match at least one of these regular expressions will be excluded from the scan. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#exclude_regex GoogleDataLossPreventionJobTrigger#exclude_regex}
        :param include_regex: A list of regular expressions matching file paths to include. All files in the bucket that match at least one of these regular expressions will be included in the set of files, except for those that also match an item in excludeRegex. Leaving this field empty will match all files by default (this is equivalent to including .* in the list) Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#include_regex GoogleDataLossPreventionJobTrigger#include_regex}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7207511cb2fc3e4d5ce4cc7e99ed57c29d5809c273864229cf0ee09802f77504)
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument exclude_regex", value=exclude_regex, expected_type=type_hints["exclude_regex"])
            check_type(argname="argument include_regex", value=include_regex, expected_type=type_hints["include_regex"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket_name": bucket_name,
        }
        if exclude_regex is not None:
            self._values["exclude_regex"] = exclude_regex
        if include_regex is not None:
            self._values["include_regex"] = include_regex

    @builtins.property
    def bucket_name(self) -> builtins.str:
        '''The name of a Cloud Storage bucket.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#bucket_name GoogleDataLossPreventionJobTrigger#bucket_name}
        '''
        result = self._values.get("bucket_name")
        assert result is not None, "Required property 'bucket_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def exclude_regex(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of regular expressions matching file paths to exclude.

        All files in the bucket that match at
        least one of these regular expressions will be excluded from the scan.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#exclude_regex GoogleDataLossPreventionJobTrigger#exclude_regex}
        '''
        result = self._values.get("exclude_regex")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def include_regex(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of regular expressions matching file paths to include.

        All files in the bucket
        that match at least one of these regular expressions will be included in the set of files,
        except for those that also match an item in excludeRegex. Leaving this field empty will
        match all files by default (this is equivalent to including .* in the list)

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#include_regex GoogleDataLossPreventionJobTrigger#include_regex}
        '''
        result = self._values.get("include_regex")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetRegexFileSet(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetRegexFileSetOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetRegexFileSetOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__345a30286b67ba2eea9088818dd3f7fd8a2201041f8521aad4f9e4bb7682488f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetExcludeRegex")
    def reset_exclude_regex(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExcludeRegex", []))

    @jsii.member(jsii_name="resetIncludeRegex")
    def reset_include_regex(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeRegex", []))

    @builtins.property
    @jsii.member(jsii_name="bucketNameInput")
    def bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="excludeRegexInput")
    def exclude_regex_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "excludeRegexInput"))

    @builtins.property
    @jsii.member(jsii_name="includeRegexInput")
    def include_regex_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "includeRegexInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketName")
    def bucket_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketName"))

    @bucket_name.setter
    def bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe2896baaaa9434d58943169281dd2f3d0a498180a049d5c0e7d54687e689801)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketName", value)

    @builtins.property
    @jsii.member(jsii_name="excludeRegex")
    def exclude_regex(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "excludeRegex"))

    @exclude_regex.setter
    def exclude_regex(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__958329c24396a5beb84e54211f99ba3dece1b5a02b65e9077a47250d3069bb1c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "excludeRegex", value)

    @builtins.property
    @jsii.member(jsii_name="includeRegex")
    def include_regex(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "includeRegex"))

    @include_regex.setter
    def include_regex(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0ded93286b1c2e56f168c1b8c8fe43dc2b3b740eade8edd90839b0f932a3362)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeRegex", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetRegexFileSet]:
        return typing.cast(typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetRegexFileSet], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetRegexFileSet],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b13516bde22a41d741ebe4cebedc1106e8de7caa68b86c4e67eb353b96b3258f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__591f5a47569bed6356dc433ef62e62a1e0f75a5b71b81eb6cbe5538e8d1c66a8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putFileSet")
    def put_file_set(
        self,
        *,
        regex_file_set: typing.Optional[typing.Union[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetRegexFileSet, typing.Dict[builtins.str, typing.Any]]] = None,
        url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param regex_file_set: regex_file_set block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#regex_file_set GoogleDataLossPreventionJobTrigger#regex_file_set}
        :param url: The Cloud Storage url of the file(s) to scan, in the format 'gs:///'. Trailing wildcard in the path is allowed. If the url ends in a trailing slash, the bucket or directory represented by the url will be scanned non-recursively (content in sub-directories will not be scanned). This means that 'gs://mybucket/' is equivalent to 'gs://mybucket/*', and 'gs://mybucket/directory/' is equivalent to 'gs://mybucket/directory/*'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#url GoogleDataLossPreventionJobTrigger#url}
        '''
        value = GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSet(
            regex_file_set=regex_file_set, url=url
        )

        return typing.cast(None, jsii.invoke(self, "putFileSet", [value]))

    @jsii.member(jsii_name="resetBytesLimitPerFile")
    def reset_bytes_limit_per_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBytesLimitPerFile", []))

    @jsii.member(jsii_name="resetBytesLimitPerFilePercent")
    def reset_bytes_limit_per_file_percent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBytesLimitPerFilePercent", []))

    @jsii.member(jsii_name="resetFilesLimitPercent")
    def reset_files_limit_percent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilesLimitPercent", []))

    @jsii.member(jsii_name="resetFileTypes")
    def reset_file_types(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFileTypes", []))

    @jsii.member(jsii_name="resetSampleMethod")
    def reset_sample_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSampleMethod", []))

    @builtins.property
    @jsii.member(jsii_name="fileSet")
    def file_set(
        self,
    ) -> GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetOutputReference:
        return typing.cast(GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetOutputReference, jsii.get(self, "fileSet"))

    @builtins.property
    @jsii.member(jsii_name="bytesLimitPerFileInput")
    def bytes_limit_per_file_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "bytesLimitPerFileInput"))

    @builtins.property
    @jsii.member(jsii_name="bytesLimitPerFilePercentInput")
    def bytes_limit_per_file_percent_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "bytesLimitPerFilePercentInput"))

    @builtins.property
    @jsii.member(jsii_name="fileSetInput")
    def file_set_input(
        self,
    ) -> typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSet]:
        return typing.cast(typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSet], jsii.get(self, "fileSetInput"))

    @builtins.property
    @jsii.member(jsii_name="filesLimitPercentInput")
    def files_limit_percent_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "filesLimitPercentInput"))

    @builtins.property
    @jsii.member(jsii_name="fileTypesInput")
    def file_types_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "fileTypesInput"))

    @builtins.property
    @jsii.member(jsii_name="sampleMethodInput")
    def sample_method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sampleMethodInput"))

    @builtins.property
    @jsii.member(jsii_name="bytesLimitPerFile")
    def bytes_limit_per_file(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bytesLimitPerFile"))

    @bytes_limit_per_file.setter
    def bytes_limit_per_file(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc56f04e12c0ed1dd28b06f6afd7c91ef1b719a2cfe2eeed4be5f1185e91b771)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bytesLimitPerFile", value)

    @builtins.property
    @jsii.member(jsii_name="bytesLimitPerFilePercent")
    def bytes_limit_per_file_percent(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bytesLimitPerFilePercent"))

    @bytes_limit_per_file_percent.setter
    def bytes_limit_per_file_percent(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03366031435dea843d2f884aa19f8870fd74fac93b7894060fc9cb1feed91f0e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bytesLimitPerFilePercent", value)

    @builtins.property
    @jsii.member(jsii_name="filesLimitPercent")
    def files_limit_percent(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "filesLimitPercent"))

    @files_limit_percent.setter
    def files_limit_percent(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d768974c4528eaa132cdb50255114c3dbb1d7ca9e00e3680826608f2a6d4e322)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filesLimitPercent", value)

    @builtins.property
    @jsii.member(jsii_name="fileTypes")
    def file_types(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "fileTypes"))

    @file_types.setter
    def file_types(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf33bd81bdbc32b739295c37076e7e38d3416290a6f4b587e10e39adbdbf57be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileTypes", value)

    @builtins.property
    @jsii.member(jsii_name="sampleMethod")
    def sample_method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sampleMethod"))

    @sample_method.setter
    def sample_method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a9194a8dcfd2410cf31efe23d560b0f9651b03a4419a61468ef109b1f4fdfd8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sampleMethod", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptions]:
        return typing.cast(typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8af5f8e50c60ff93f8166f46696cef9906c501f460f4a411f7381835c09b23fc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptions",
    jsii_struct_bases=[],
    name_mapping={"kind": "kind", "partition_id": "partitionId"},
)
class GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptions:
    def __init__(
        self,
        *,
        kind: typing.Union["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsKind", typing.Dict[builtins.str, typing.Any]],
        partition_id: typing.Union["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsPartitionId", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param kind: kind block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#kind GoogleDataLossPreventionJobTrigger#kind}
        :param partition_id: partition_id block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#partition_id GoogleDataLossPreventionJobTrigger#partition_id}
        '''
        if isinstance(kind, dict):
            kind = GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsKind(**kind)
        if isinstance(partition_id, dict):
            partition_id = GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsPartitionId(**partition_id)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0df70fe325aff760dadf4c76a30ac090c7462360b26c4c80b6f44dde5a4c857)
            check_type(argname="argument kind", value=kind, expected_type=type_hints["kind"])
            check_type(argname="argument partition_id", value=partition_id, expected_type=type_hints["partition_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "kind": kind,
            "partition_id": partition_id,
        }

    @builtins.property
    def kind(
        self,
    ) -> "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsKind":
        '''kind block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#kind GoogleDataLossPreventionJobTrigger#kind}
        '''
        result = self._values.get("kind")
        assert result is not None, "Required property 'kind' is missing"
        return typing.cast("GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsKind", result)

    @builtins.property
    def partition_id(
        self,
    ) -> "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsPartitionId":
        '''partition_id block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#partition_id GoogleDataLossPreventionJobTrigger#partition_id}
        '''
        result = self._values.get("partition_id")
        assert result is not None, "Required property 'partition_id' is missing"
        return typing.cast("GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsPartitionId", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsKind",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsKind:
    def __init__(self, *, name: builtins.str) -> None:
        '''
        :param name: The name of the Datastore kind. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#name GoogleDataLossPreventionJobTrigger#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32de240167b5f71bbd1b18a6cbb8510724f89f459e18917e2cc38e0957ee08bf)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the Datastore kind.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#name GoogleDataLossPreventionJobTrigger#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsKind(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsKindOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsKindOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__845c2160bf04dfe18d77534cfa400dd3daec156b31b9618f32cde60272ea5954)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b179d4fd81a88df354c76c14d39c787b68c4550fa1280b569bb526c2a5d87b18)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsKind]:
        return typing.cast(typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsKind], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsKind],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29ed8a35bb36910d10960af47fe6aad99d9255a2f1fe3af4407462a00b1d2d79)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__42ab23e9d6e4dddb911e54c5e09f94849dc648f9c0444b5f73ebee4c35722ef8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putKind")
    def put_kind(self, *, name: builtins.str) -> None:
        '''
        :param name: The name of the Datastore kind. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#name GoogleDataLossPreventionJobTrigger#name}
        '''
        value = GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsKind(
            name=name
        )

        return typing.cast(None, jsii.invoke(self, "putKind", [value]))

    @jsii.member(jsii_name="putPartitionId")
    def put_partition_id(
        self,
        *,
        project_id: builtins.str,
        namespace_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param project_id: The ID of the project to which the entities belong. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#project_id GoogleDataLossPreventionJobTrigger#project_id}
        :param namespace_id: If not empty, the ID of the namespace to which the entities belong. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#namespace_id GoogleDataLossPreventionJobTrigger#namespace_id}
        '''
        value = GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsPartitionId(
            project_id=project_id, namespace_id=namespace_id
        )

        return typing.cast(None, jsii.invoke(self, "putPartitionId", [value]))

    @builtins.property
    @jsii.member(jsii_name="kind")
    def kind(
        self,
    ) -> GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsKindOutputReference:
        return typing.cast(GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsKindOutputReference, jsii.get(self, "kind"))

    @builtins.property
    @jsii.member(jsii_name="partitionId")
    def partition_id(
        self,
    ) -> "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsPartitionIdOutputReference":
        return typing.cast("GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsPartitionIdOutputReference", jsii.get(self, "partitionId"))

    @builtins.property
    @jsii.member(jsii_name="kindInput")
    def kind_input(
        self,
    ) -> typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsKind]:
        return typing.cast(typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsKind], jsii.get(self, "kindInput"))

    @builtins.property
    @jsii.member(jsii_name="partitionIdInput")
    def partition_id_input(
        self,
    ) -> typing.Optional["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsPartitionId"]:
        return typing.cast(typing.Optional["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsPartitionId"], jsii.get(self, "partitionIdInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptions]:
        return typing.cast(typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e62269aea7dbceb5e1e44854a12434f646ae59058bc8600c3a449018e411a47e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsPartitionId",
    jsii_struct_bases=[],
    name_mapping={"project_id": "projectId", "namespace_id": "namespaceId"},
)
class GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsPartitionId:
    def __init__(
        self,
        *,
        project_id: builtins.str,
        namespace_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param project_id: The ID of the project to which the entities belong. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#project_id GoogleDataLossPreventionJobTrigger#project_id}
        :param namespace_id: If not empty, the ID of the namespace to which the entities belong. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#namespace_id GoogleDataLossPreventionJobTrigger#namespace_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__090d678c444c13bbd535bfbc1aaac700cdf1e27e496597c0e54b3e76d67b7584)
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument namespace_id", value=namespace_id, expected_type=type_hints["namespace_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "project_id": project_id,
        }
        if namespace_id is not None:
            self._values["namespace_id"] = namespace_id

    @builtins.property
    def project_id(self) -> builtins.str:
        '''The ID of the project to which the entities belong.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#project_id GoogleDataLossPreventionJobTrigger#project_id}
        '''
        result = self._values.get("project_id")
        assert result is not None, "Required property 'project_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace_id(self) -> typing.Optional[builtins.str]:
        '''If not empty, the ID of the namespace to which the entities belong.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#namespace_id GoogleDataLossPreventionJobTrigger#namespace_id}
        '''
        result = self._values.get("namespace_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsPartitionId(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsPartitionIdOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsPartitionIdOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__573268f1e46ce0cac23683741f19a2abf8de99047216746ed926b5ee11c425b0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetNamespaceId")
    def reset_namespace_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespaceId", []))

    @builtins.property
    @jsii.member(jsii_name="namespaceIdInput")
    def namespace_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="projectIdInput")
    def project_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectIdInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceId")
    def namespace_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespaceId"))

    @namespace_id.setter
    def namespace_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45f711b7be9c381cfba7ae23ba26ceaf169c278108c8dcb5a7afa332bdfcbc0f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespaceId", value)

    @builtins.property
    @jsii.member(jsii_name="projectId")
    def project_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "projectId"))

    @project_id.setter
    def project_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ff58d99a84b803f63591572901f1cc2a050350388d92583d7d70f2357f3ee31)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsPartitionId]:
        return typing.cast(typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsPartitionId], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsPartitionId],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ab7a2001772d8134296ce8948e54e1ed14fb7ddcf0aa7bc98fab489e6f1136c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDataLossPreventionJobTriggerInspectJobStorageConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobStorageConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d0a416030319e43eded9f6fc27911924421226085a39e3a1424addf1e560356f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putBigQueryOptions")
    def put_big_query_options(
        self,
        *,
        table_reference: typing.Union[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptionsTableReference, typing.Dict[builtins.str, typing.Any]],
        rows_limit: typing.Optional[jsii.Number] = None,
        rows_limit_percent: typing.Optional[jsii.Number] = None,
        sample_method: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param table_reference: table_reference block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#table_reference GoogleDataLossPreventionJobTrigger#table_reference}
        :param rows_limit: Max number of rows to scan. If the table has more rows than this value, the rest of the rows are omitted. If not set, or if set to 0, all rows will be scanned. Only one of rowsLimit and rowsLimitPercent can be specified. Cannot be used in conjunction with TimespanConfig. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#rows_limit GoogleDataLossPreventionJobTrigger#rows_limit}
        :param rows_limit_percent: Max percentage of rows to scan. The rest are omitted. The number of rows scanned is rounded down. Must be between 0 and 100, inclusively. Both 0 and 100 means no limit. Defaults to 0. Only one of rowsLimit and rowsLimitPercent can be specified. Cannot be used in conjunction with TimespanConfig. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#rows_limit_percent GoogleDataLossPreventionJobTrigger#rows_limit_percent}
        :param sample_method: How to sample rows if not all rows are scanned. Meaningful only when used in conjunction with either rowsLimit or rowsLimitPercent. If not specified, rows are scanned in the order BigQuery reads them. Default value: "TOP" Possible values: ["TOP", "RANDOM_START"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#sample_method GoogleDataLossPreventionJobTrigger#sample_method}
        '''
        value = GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptions(
            table_reference=table_reference,
            rows_limit=rows_limit,
            rows_limit_percent=rows_limit_percent,
            sample_method=sample_method,
        )

        return typing.cast(None, jsii.invoke(self, "putBigQueryOptions", [value]))

    @jsii.member(jsii_name="putCloudStorageOptions")
    def put_cloud_storage_options(
        self,
        *,
        file_set: typing.Union[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSet, typing.Dict[builtins.str, typing.Any]],
        bytes_limit_per_file: typing.Optional[jsii.Number] = None,
        bytes_limit_per_file_percent: typing.Optional[jsii.Number] = None,
        files_limit_percent: typing.Optional[jsii.Number] = None,
        file_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        sample_method: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param file_set: file_set block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#file_set GoogleDataLossPreventionJobTrigger#file_set}
        :param bytes_limit_per_file: Max number of bytes to scan from a file. If a scanned file's size is bigger than this value then the rest of the bytes are omitted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#bytes_limit_per_file GoogleDataLossPreventionJobTrigger#bytes_limit_per_file}
        :param bytes_limit_per_file_percent: Max percentage of bytes to scan from a file. The rest are omitted. The number of bytes scanned is rounded down. Must be between 0 and 100, inclusively. Both 0 and 100 means no limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#bytes_limit_per_file_percent GoogleDataLossPreventionJobTrigger#bytes_limit_per_file_percent}
        :param files_limit_percent: Limits the number of files to scan to this percentage of the input FileSet. Number of files scanned is rounded down. Must be between 0 and 100, inclusively. Both 0 and 100 means no limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#files_limit_percent GoogleDataLossPreventionJobTrigger#files_limit_percent}
        :param file_types: List of file type groups to include in the scan. If empty, all files are scanned and available data format processors are applied. In addition, the binary content of the selected files is always scanned as well. Images are scanned only as binary if the specified region does not support image inspection and no fileTypes were specified. Possible values: ["BINARY_FILE", "TEXT_FILE", "IMAGE", "WORD", "PDF", "AVRO", "CSV", "TSV"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#file_types GoogleDataLossPreventionJobTrigger#file_types}
        :param sample_method: How to sample bytes if not all bytes are scanned. Meaningful only when used in conjunction with bytesLimitPerFile. If not specified, scanning would start from the top. Possible values: ["TOP", "RANDOM_START"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#sample_method GoogleDataLossPreventionJobTrigger#sample_method}
        '''
        value = GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptions(
            file_set=file_set,
            bytes_limit_per_file=bytes_limit_per_file,
            bytes_limit_per_file_percent=bytes_limit_per_file_percent,
            files_limit_percent=files_limit_percent,
            file_types=file_types,
            sample_method=sample_method,
        )

        return typing.cast(None, jsii.invoke(self, "putCloudStorageOptions", [value]))

    @jsii.member(jsii_name="putDatastoreOptions")
    def put_datastore_options(
        self,
        *,
        kind: typing.Union[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsKind, typing.Dict[builtins.str, typing.Any]],
        partition_id: typing.Union[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsPartitionId, typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param kind: kind block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#kind GoogleDataLossPreventionJobTrigger#kind}
        :param partition_id: partition_id block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#partition_id GoogleDataLossPreventionJobTrigger#partition_id}
        '''
        value = GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptions(
            kind=kind, partition_id=partition_id
        )

        return typing.cast(None, jsii.invoke(self, "putDatastoreOptions", [value]))

    @jsii.member(jsii_name="putTimespanConfig")
    def put_timespan_config(
        self,
        *,
        timestamp_field: typing.Union["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfigTimestampField", typing.Dict[builtins.str, typing.Any]],
        enable_auto_population_of_timespan_config: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        end_time: typing.Optional[builtins.str] = None,
        start_time: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param timestamp_field: timestamp_field block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#timestamp_field GoogleDataLossPreventionJobTrigger#timestamp_field}
        :param enable_auto_population_of_timespan_config: When the job is started by a JobTrigger we will automatically figure out a valid startTime to avoid scanning files that have not been modified since the last time the JobTrigger executed. This will be based on the time of the execution of the last run of the JobTrigger. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#enable_auto_population_of_timespan_config GoogleDataLossPreventionJobTrigger#enable_auto_population_of_timespan_config}
        :param end_time: Exclude files or rows newer than this value. If set to zero, no upper time limit is applied. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#end_time GoogleDataLossPreventionJobTrigger#end_time}
        :param start_time: Exclude files or rows older than this value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#start_time GoogleDataLossPreventionJobTrigger#start_time}
        '''
        value = GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfig(
            timestamp_field=timestamp_field,
            enable_auto_population_of_timespan_config=enable_auto_population_of_timespan_config,
            end_time=end_time,
            start_time=start_time,
        )

        return typing.cast(None, jsii.invoke(self, "putTimespanConfig", [value]))

    @jsii.member(jsii_name="resetBigQueryOptions")
    def reset_big_query_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBigQueryOptions", []))

    @jsii.member(jsii_name="resetCloudStorageOptions")
    def reset_cloud_storage_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudStorageOptions", []))

    @jsii.member(jsii_name="resetDatastoreOptions")
    def reset_datastore_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatastoreOptions", []))

    @jsii.member(jsii_name="resetTimespanConfig")
    def reset_timespan_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimespanConfig", []))

    @builtins.property
    @jsii.member(jsii_name="bigQueryOptions")
    def big_query_options(
        self,
    ) -> GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptionsOutputReference:
        return typing.cast(GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptionsOutputReference, jsii.get(self, "bigQueryOptions"))

    @builtins.property
    @jsii.member(jsii_name="cloudStorageOptions")
    def cloud_storage_options(
        self,
    ) -> GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsOutputReference:
        return typing.cast(GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsOutputReference, jsii.get(self, "cloudStorageOptions"))

    @builtins.property
    @jsii.member(jsii_name="datastoreOptions")
    def datastore_options(
        self,
    ) -> GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsOutputReference:
        return typing.cast(GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsOutputReference, jsii.get(self, "datastoreOptions"))

    @builtins.property
    @jsii.member(jsii_name="timespanConfig")
    def timespan_config(
        self,
    ) -> "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfigOutputReference":
        return typing.cast("GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfigOutputReference", jsii.get(self, "timespanConfig"))

    @builtins.property
    @jsii.member(jsii_name="bigQueryOptionsInput")
    def big_query_options_input(
        self,
    ) -> typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptions]:
        return typing.cast(typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptions], jsii.get(self, "bigQueryOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudStorageOptionsInput")
    def cloud_storage_options_input(
        self,
    ) -> typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptions]:
        return typing.cast(typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptions], jsii.get(self, "cloudStorageOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="datastoreOptionsInput")
    def datastore_options_input(
        self,
    ) -> typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptions]:
        return typing.cast(typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptions], jsii.get(self, "datastoreOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="timespanConfigInput")
    def timespan_config_input(
        self,
    ) -> typing.Optional["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfig"]:
        return typing.cast(typing.Optional["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfig"], jsii.get(self, "timespanConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfig]:
        return typing.cast(typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f78ff5a9b71efd577fd3b575b6d6137bcafeaa580baad08591d1eb5fb21bf68f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfig",
    jsii_struct_bases=[],
    name_mapping={
        "timestamp_field": "timestampField",
        "enable_auto_population_of_timespan_config": "enableAutoPopulationOfTimespanConfig",
        "end_time": "endTime",
        "start_time": "startTime",
    },
)
class GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfig:
    def __init__(
        self,
        *,
        timestamp_field: typing.Union["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfigTimestampField", typing.Dict[builtins.str, typing.Any]],
        enable_auto_population_of_timespan_config: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        end_time: typing.Optional[builtins.str] = None,
        start_time: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param timestamp_field: timestamp_field block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#timestamp_field GoogleDataLossPreventionJobTrigger#timestamp_field}
        :param enable_auto_population_of_timespan_config: When the job is started by a JobTrigger we will automatically figure out a valid startTime to avoid scanning files that have not been modified since the last time the JobTrigger executed. This will be based on the time of the execution of the last run of the JobTrigger. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#enable_auto_population_of_timespan_config GoogleDataLossPreventionJobTrigger#enable_auto_population_of_timespan_config}
        :param end_time: Exclude files or rows newer than this value. If set to zero, no upper time limit is applied. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#end_time GoogleDataLossPreventionJobTrigger#end_time}
        :param start_time: Exclude files or rows older than this value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#start_time GoogleDataLossPreventionJobTrigger#start_time}
        '''
        if isinstance(timestamp_field, dict):
            timestamp_field = GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfigTimestampField(**timestamp_field)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f600b382e656d175bb217f904173c392c9ff5f0d95982191d63ec7b31c6fda4)
            check_type(argname="argument timestamp_field", value=timestamp_field, expected_type=type_hints["timestamp_field"])
            check_type(argname="argument enable_auto_population_of_timespan_config", value=enable_auto_population_of_timespan_config, expected_type=type_hints["enable_auto_population_of_timespan_config"])
            check_type(argname="argument end_time", value=end_time, expected_type=type_hints["end_time"])
            check_type(argname="argument start_time", value=start_time, expected_type=type_hints["start_time"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "timestamp_field": timestamp_field,
        }
        if enable_auto_population_of_timespan_config is not None:
            self._values["enable_auto_population_of_timespan_config"] = enable_auto_population_of_timespan_config
        if end_time is not None:
            self._values["end_time"] = end_time
        if start_time is not None:
            self._values["start_time"] = start_time

    @builtins.property
    def timestamp_field(
        self,
    ) -> "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfigTimestampField":
        '''timestamp_field block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#timestamp_field GoogleDataLossPreventionJobTrigger#timestamp_field}
        '''
        result = self._values.get("timestamp_field")
        assert result is not None, "Required property 'timestamp_field' is missing"
        return typing.cast("GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfigTimestampField", result)

    @builtins.property
    def enable_auto_population_of_timespan_config(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''When the job is started by a JobTrigger we will automatically figure out a valid startTime to avoid scanning files that have not been modified since the last time the JobTrigger executed.

        This will
        be based on the time of the execution of the last run of the JobTrigger.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#enable_auto_population_of_timespan_config GoogleDataLossPreventionJobTrigger#enable_auto_population_of_timespan_config}
        '''
        result = self._values.get("enable_auto_population_of_timespan_config")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def end_time(self) -> typing.Optional[builtins.str]:
        '''Exclude files or rows newer than this value. If set to zero, no upper time limit is applied.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#end_time GoogleDataLossPreventionJobTrigger#end_time}
        '''
        result = self._values.get("end_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def start_time(self) -> typing.Optional[builtins.str]:
        '''Exclude files or rows older than this value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#start_time GoogleDataLossPreventionJobTrigger#start_time}
        '''
        result = self._values.get("start_time")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b7ebe486568fbc7cf72b6ea3993aba85860c7b22005ac1a859ad3882757e6a88)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putTimestampField")
    def put_timestamp_field(self, *, name: builtins.str) -> None:
        '''
        :param name: Specification of the field containing the timestamp of scanned items. Used for data sources like Datastore and BigQuery. For BigQuery: Required to filter out rows based on the given start and end times. If not specified and the table was modified between the given start and end times, the entire table will be scanned. The valid data types of the timestamp field are: INTEGER, DATE, TIMESTAMP, or DATETIME BigQuery column. For Datastore. Valid data types of the timestamp field are: TIMESTAMP. Datastore entity will be scanned if the timestamp property does not exist or its value is empty or invalid. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#name GoogleDataLossPreventionJobTrigger#name}
        '''
        value = GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfigTimestampField(
            name=name
        )

        return typing.cast(None, jsii.invoke(self, "putTimestampField", [value]))

    @jsii.member(jsii_name="resetEnableAutoPopulationOfTimespanConfig")
    def reset_enable_auto_population_of_timespan_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableAutoPopulationOfTimespanConfig", []))

    @jsii.member(jsii_name="resetEndTime")
    def reset_end_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndTime", []))

    @jsii.member(jsii_name="resetStartTime")
    def reset_start_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartTime", []))

    @builtins.property
    @jsii.member(jsii_name="timestampField")
    def timestamp_field(
        self,
    ) -> "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfigTimestampFieldOutputReference":
        return typing.cast("GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfigTimestampFieldOutputReference", jsii.get(self, "timestampField"))

    @builtins.property
    @jsii.member(jsii_name="enableAutoPopulationOfTimespanConfigInput")
    def enable_auto_population_of_timespan_config_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableAutoPopulationOfTimespanConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="endTimeInput")
    def end_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="startTimeInput")
    def start_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="timestampFieldInput")
    def timestamp_field_input(
        self,
    ) -> typing.Optional["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfigTimestampField"]:
        return typing.cast(typing.Optional["GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfigTimestampField"], jsii.get(self, "timestampFieldInput"))

    @builtins.property
    @jsii.member(jsii_name="enableAutoPopulationOfTimespanConfig")
    def enable_auto_population_of_timespan_config(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableAutoPopulationOfTimespanConfig"))

    @enable_auto_population_of_timespan_config.setter
    def enable_auto_population_of_timespan_config(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0fe5ed60194cb53649f0037563d195faf34257eecaa4bf94d7453d82dde4a7f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableAutoPopulationOfTimespanConfig", value)

    @builtins.property
    @jsii.member(jsii_name="endTime")
    def end_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endTime"))

    @end_time.setter
    def end_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__606dd34308eb5b17bc8bbdd57ec3ac2d2f4b0f4eb918e84560f4c8ceca5147f0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endTime", value)

    @builtins.property
    @jsii.member(jsii_name="startTime")
    def start_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startTime"))

    @start_time.setter
    def start_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92c400479d32678af9ff9b8f556db388f1a3b775aef9b72d778051087c18e18c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startTime", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfig]:
        return typing.cast(typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__953733e038856ce953dd9f3df41f0c212cf3c19f0346a82204744e88314f80d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfigTimestampField",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfigTimestampField:
    def __init__(self, *, name: builtins.str) -> None:
        '''
        :param name: Specification of the field containing the timestamp of scanned items. Used for data sources like Datastore and BigQuery. For BigQuery: Required to filter out rows based on the given start and end times. If not specified and the table was modified between the given start and end times, the entire table will be scanned. The valid data types of the timestamp field are: INTEGER, DATE, TIMESTAMP, or DATETIME BigQuery column. For Datastore. Valid data types of the timestamp field are: TIMESTAMP. Datastore entity will be scanned if the timestamp property does not exist or its value is empty or invalid. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#name GoogleDataLossPreventionJobTrigger#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4cca4a1a0e0d01e2b7b4dd815070083e4ba32903e79d13f890806ffec1c42338)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Specification of the field containing the timestamp of scanned items. Used for data sources like Datastore and BigQuery.

        For BigQuery: Required to filter out rows based on the given start and end times. If not specified and the table was
        modified between the given start and end times, the entire table will be scanned. The valid data types of the timestamp
        field are: INTEGER, DATE, TIMESTAMP, or DATETIME BigQuery column.

        For Datastore. Valid data types of the timestamp field are: TIMESTAMP. Datastore entity will be scanned if the
        timestamp property does not exist or its value is empty or invalid.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#name GoogleDataLossPreventionJobTrigger#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfigTimestampField(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfigTimestampFieldOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfigTimestampFieldOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a605d15d285fe8c1efd4f483eea1fb866ee51580fad608faa0aac77fc19e141d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3bddd8b1ae5308cdc5537e8f87851532af43da3ffbb5d1ce953c75c674e93f59)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfigTimestampField]:
        return typing.cast(typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfigTimestampField], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfigTimestampField],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__236627631377cc30458d4a9cb85aa125fe334d2d2acb17a05bbb287828171695)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleDataLossPreventionJobTriggerTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#create GoogleDataLossPreventionJobTrigger#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#delete GoogleDataLossPreventionJobTrigger#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#update GoogleDataLossPreventionJobTrigger#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28a69dc1bbd0162e5c6a2f793517529cc3aafbf29095e17e715b93ec100610d0)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#create GoogleDataLossPreventionJobTrigger#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#delete GoogleDataLossPreventionJobTrigger#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#update GoogleDataLossPreventionJobTrigger#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataLossPreventionJobTriggerTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataLossPreventionJobTriggerTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ed0e3419cc2cad7a4369fb91f74c6732b89f5d2c4934882254a938de701a0ef8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ee1a96c3412c6efc06c95fa5090e11b67e4348c38563faee4c70ee038788f26d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2951922c5dc2c0af344219d5b2c237164043f535d7b69c91f0d7301a8d8d41aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96d88b47cf765365d3247be97e0f52fbe746f576e81263be5b76d3a79143de30)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleDataLossPreventionJobTriggerTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleDataLossPreventionJobTriggerTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleDataLossPreventionJobTriggerTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e863f2ca9368abcebd14ac9283e5d19fb37008b5a0ab5e63457b20f7ceaca4fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerTriggers",
    jsii_struct_bases=[],
    name_mapping={"schedule": "schedule"},
)
class GoogleDataLossPreventionJobTriggerTriggers:
    def __init__(
        self,
        *,
        schedule: typing.Optional[typing.Union["GoogleDataLossPreventionJobTriggerTriggersSchedule", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param schedule: schedule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#schedule GoogleDataLossPreventionJobTrigger#schedule}
        '''
        if isinstance(schedule, dict):
            schedule = GoogleDataLossPreventionJobTriggerTriggersSchedule(**schedule)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc8a480e434e0a23ab48b67ea4211cd10dfa60639a1ed0d0eea1d557d4c16ff8)
            check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if schedule is not None:
            self._values["schedule"] = schedule

    @builtins.property
    def schedule(
        self,
    ) -> typing.Optional["GoogleDataLossPreventionJobTriggerTriggersSchedule"]:
        '''schedule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#schedule GoogleDataLossPreventionJobTrigger#schedule}
        '''
        result = self._values.get("schedule")
        return typing.cast(typing.Optional["GoogleDataLossPreventionJobTriggerTriggersSchedule"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataLossPreventionJobTriggerTriggers(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataLossPreventionJobTriggerTriggersList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerTriggersList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6ebfba5fa920928859e306ab34503f76fdf9a6b686d8ddb4e3ee49f4c656a59f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDataLossPreventionJobTriggerTriggersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a68cd8117528236fe1a5db7d8dc038cf74d62d62f291a524126999709967b39)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDataLossPreventionJobTriggerTriggersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5322412c0443b2859688ebc0e69dc04a6499e53b067544603b36eb0121944562)
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
            type_hints = typing.get_type_hints(_typecheckingstub__58d3703b770c1730ece4e9e6f8fc0681795017811fd74b3b2874bb8ff0d2c26d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8474b296512dab021e1c14fb81659aa1e05e3760381f82ee666ae101901fb782)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDataLossPreventionJobTriggerTriggers]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDataLossPreventionJobTriggerTriggers]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDataLossPreventionJobTriggerTriggers]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f59a66d1df3e710f9a78e74044d22526d1a3bb9825d15a93b209105f2424dff1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDataLossPreventionJobTriggerTriggersOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerTriggersOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b171d26728b745fa116f4e8f6733bc5604adc21ce997d164db4d5d16a6573af4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putSchedule")
    def put_schedule(
        self,
        *,
        recurrence_period_duration: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param recurrence_period_duration: With this option a job is started a regular periodic basis. For example: every day (86400 seconds). A scheduled start time will be skipped if the previous execution has not ended when its scheduled time occurs. This value must be set to a time duration greater than or equal to 1 day and can be no longer than 60 days. A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#recurrence_period_duration GoogleDataLossPreventionJobTrigger#recurrence_period_duration}
        '''
        value = GoogleDataLossPreventionJobTriggerTriggersSchedule(
            recurrence_period_duration=recurrence_period_duration
        )

        return typing.cast(None, jsii.invoke(self, "putSchedule", [value]))

    @jsii.member(jsii_name="resetSchedule")
    def reset_schedule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchedule", []))

    @builtins.property
    @jsii.member(jsii_name="schedule")
    def schedule(
        self,
    ) -> "GoogleDataLossPreventionJobTriggerTriggersScheduleOutputReference":
        return typing.cast("GoogleDataLossPreventionJobTriggerTriggersScheduleOutputReference", jsii.get(self, "schedule"))

    @builtins.property
    @jsii.member(jsii_name="scheduleInput")
    def schedule_input(
        self,
    ) -> typing.Optional["GoogleDataLossPreventionJobTriggerTriggersSchedule"]:
        return typing.cast(typing.Optional["GoogleDataLossPreventionJobTriggerTriggersSchedule"], jsii.get(self, "scheduleInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleDataLossPreventionJobTriggerTriggers, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleDataLossPreventionJobTriggerTriggers, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleDataLossPreventionJobTriggerTriggers, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8cb1fb0a2baf581892b6717f0241bfcdbab9991d00ae751aef4a1afbd8a7af9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerTriggersSchedule",
    jsii_struct_bases=[],
    name_mapping={"recurrence_period_duration": "recurrencePeriodDuration"},
)
class GoogleDataLossPreventionJobTriggerTriggersSchedule:
    def __init__(
        self,
        *,
        recurrence_period_duration: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param recurrence_period_duration: With this option a job is started a regular periodic basis. For example: every day (86400 seconds). A scheduled start time will be skipped if the previous execution has not ended when its scheduled time occurs. This value must be set to a time duration greater than or equal to 1 day and can be no longer than 60 days. A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#recurrence_period_duration GoogleDataLossPreventionJobTrigger#recurrence_period_duration}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1753ba366c5259478451cd691f732e667136e3b24ff9cc1d0ecbcc35c51c1b9a)
            check_type(argname="argument recurrence_period_duration", value=recurrence_period_duration, expected_type=type_hints["recurrence_period_duration"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if recurrence_period_duration is not None:
            self._values["recurrence_period_duration"] = recurrence_period_duration

    @builtins.property
    def recurrence_period_duration(self) -> typing.Optional[builtins.str]:
        '''With this option a job is started a regular periodic basis. For example: every day (86400 seconds).

        A scheduled start time will be skipped if the previous execution has not ended when its scheduled time occurs.

        This value must be set to a time duration greater than or equal to 1 day and can be no longer than 60 days.

        A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_loss_prevention_job_trigger#recurrence_period_duration GoogleDataLossPreventionJobTrigger#recurrence_period_duration}
        '''
        result = self._values.get("recurrence_period_duration")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataLossPreventionJobTriggerTriggersSchedule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataLossPreventionJobTriggerTriggersScheduleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataLossPreventionJobTrigger.GoogleDataLossPreventionJobTriggerTriggersScheduleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1ba77c04cc76ec4fb919d7f4241569b7af8509f48534f2af7f20385d06c6e401)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetRecurrencePeriodDuration")
    def reset_recurrence_period_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRecurrencePeriodDuration", []))

    @builtins.property
    @jsii.member(jsii_name="recurrencePeriodDurationInput")
    def recurrence_period_duration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recurrencePeriodDurationInput"))

    @builtins.property
    @jsii.member(jsii_name="recurrencePeriodDuration")
    def recurrence_period_duration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recurrencePeriodDuration"))

    @recurrence_period_duration.setter
    def recurrence_period_duration(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de1773cae7784a12deb8b2d195becf09e34a711351cf1c362748d84d775f7dc4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recurrencePeriodDuration", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataLossPreventionJobTriggerTriggersSchedule]:
        return typing.cast(typing.Optional[GoogleDataLossPreventionJobTriggerTriggersSchedule], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataLossPreventionJobTriggerTriggersSchedule],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e15c216c146ecce28cc440557ff966ef712bff6c43ae013974c62d66982880fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleDataLossPreventionJobTrigger",
    "GoogleDataLossPreventionJobTriggerConfig",
    "GoogleDataLossPreventionJobTriggerInspectJob",
    "GoogleDataLossPreventionJobTriggerInspectJobActions",
    "GoogleDataLossPreventionJobTriggerInspectJobActionsList",
    "GoogleDataLossPreventionJobTriggerInspectJobActionsOutputReference",
    "GoogleDataLossPreventionJobTriggerInspectJobActionsPubSub",
    "GoogleDataLossPreventionJobTriggerInspectJobActionsPubSubOutputReference",
    "GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindings",
    "GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfig",
    "GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfigOutputReference",
    "GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfigTable",
    "GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfigTableOutputReference",
    "GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputReference",
    "GoogleDataLossPreventionJobTriggerInspectJobOutputReference",
    "GoogleDataLossPreventionJobTriggerInspectJobStorageConfig",
    "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptions",
    "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptionsOutputReference",
    "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptionsTableReference",
    "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptionsTableReferenceOutputReference",
    "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptions",
    "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSet",
    "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetOutputReference",
    "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetRegexFileSet",
    "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetRegexFileSetOutputReference",
    "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsOutputReference",
    "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptions",
    "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsKind",
    "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsKindOutputReference",
    "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsOutputReference",
    "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsPartitionId",
    "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsPartitionIdOutputReference",
    "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigOutputReference",
    "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfig",
    "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfigOutputReference",
    "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfigTimestampField",
    "GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfigTimestampFieldOutputReference",
    "GoogleDataLossPreventionJobTriggerTimeouts",
    "GoogleDataLossPreventionJobTriggerTimeoutsOutputReference",
    "GoogleDataLossPreventionJobTriggerTriggers",
    "GoogleDataLossPreventionJobTriggerTriggersList",
    "GoogleDataLossPreventionJobTriggerTriggersOutputReference",
    "GoogleDataLossPreventionJobTriggerTriggersSchedule",
    "GoogleDataLossPreventionJobTriggerTriggersScheduleOutputReference",
]

publication.publish()

def _typecheckingstub__9d0d9ea6bb81a21c3992292e2afbe9aa9a2f8f38abb4c99bebbd303fdcd845e7(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    parent: builtins.str,
    triggers: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDataLossPreventionJobTriggerTriggers, typing.Dict[builtins.str, typing.Any]]]],
    description: typing.Optional[builtins.str] = None,
    display_name: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    inspect_job: typing.Optional[typing.Union[GoogleDataLossPreventionJobTriggerInspectJob, typing.Dict[builtins.str, typing.Any]]] = None,
    status: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[GoogleDataLossPreventionJobTriggerTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__400b0f28743c698651f83b72bafcbabdd42c0c88da17270ff3a0d2e0d18d25c3(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDataLossPreventionJobTriggerTriggers, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__155b1978c1188e118f5fb3d8fc7892595da4bf40caba9edb413eb51d7feace0e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa804a38c1453ebd38dceca6f16a250a172272fb27aab741d9217265095266e5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23e06de2f2e31d5ea87be92f71c4221086ff77037865625c0a1db2ffb511f243(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__513067889f32f03cc5583d26fd36be5f01794103f98df7db23fef04129565838(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e3f36361a9e3b82ec15b503ec8557057dcf268981ff6b8fadf6ca42b5fa520b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe4c0cfb50e9869a9b0d7c6b1af7a4b24fb732dde8e14a5cdc4ee7d8bf43dff8(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    parent: builtins.str,
    triggers: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDataLossPreventionJobTriggerTriggers, typing.Dict[builtins.str, typing.Any]]]],
    description: typing.Optional[builtins.str] = None,
    display_name: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    inspect_job: typing.Optional[typing.Union[GoogleDataLossPreventionJobTriggerInspectJob, typing.Dict[builtins.str, typing.Any]]] = None,
    status: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[GoogleDataLossPreventionJobTriggerTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31c5535fb08c747f6d7a676bf8fa45703765fd33ca44680acc73179a4e6ea5c4(
    *,
    actions: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDataLossPreventionJobTriggerInspectJobActions, typing.Dict[builtins.str, typing.Any]]]],
    inspect_template_name: builtins.str,
    storage_config: typing.Union[GoogleDataLossPreventionJobTriggerInspectJobStorageConfig, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15b42a7716ec1a69e95512aee92a77142168bf2ba103ac5b7dddf38ed3cb422a(
    *,
    pub_sub: typing.Optional[typing.Union[GoogleDataLossPreventionJobTriggerInspectJobActionsPubSub, typing.Dict[builtins.str, typing.Any]]] = None,
    save_findings: typing.Optional[typing.Union[GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindings, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ada89d2b4bd33bfae64f00c58e4809bad95edb650a9394c8aaa9c9e2337946e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07166fc1b8bd816095ecb7f70f3ba1fbeca053dad1bc5b7d01a4053431d80813(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0238de74f76d7a0a29c10c53a0925e4d51afe78a72fb7ad2a45522d3069bde33(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee82a645360b715581d58d263051a5a1e6dc2803c15c84550dadc383c52cd739(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b8063ba8e553098fb83f03e0272a4f1fee5c25b923d920ebdddfbb750a42b77(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50eff909f45fb741e3f63b6ff9a2e0f68fa7dfe7a1895fd56473e3607f7e951c(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDataLossPreventionJobTriggerInspectJobActions]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4394ed47f2cbfccfc55da7085a29b6f6e08454cfb6e776155c90834adae16187(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92811793c327aecb7abb5cd4b7a3a65582ea32c25476e925d6e290aba34d74f2(
    value: typing.Optional[typing.Union[GoogleDataLossPreventionJobTriggerInspectJobActions, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87fd1c64967036117c81eccbe629974df83c57db2db988bcdddcae863d8c4762(
    *,
    topic: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf8d19d736c64e816a63c8b64aea56b7df27cab33f0e0e63fc5a0606b424c66b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa3eee9b5ad9285a28bebf2b19c26b4cbac2322b3b93664faa8c7465fe62701e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__556acc8c03cdc5ddd8f25d1a40959a946c1390484e86d3e904e3f69ee76551d0(
    value: typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobActionsPubSub],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__653c253abc1015bd8d0c854597a750c18d634b70116c5a33d070ca383cbe736c(
    *,
    output_config: typing.Union[GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfig, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aff6af371263bf589c86949300f2695ca78641f969b4e20b7f81a977baba1860(
    *,
    table: typing.Union[GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfigTable, typing.Dict[builtins.str, typing.Any]],
    output_schema: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bc68da821c9c3c64fbcbb6db56df7ddff67663508cae084765d8d851c9ab706(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80abc1a808d2392cdf67a6ba7da1ebb8b1ef4b274541e35abb57c6ed9b687113(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d887bdf2aaff0732dbe05fe4f94be5898830bc575273bd6022ae1e61bdfd582(
    value: typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4eb1dafabd8bf35ef4fd6a6b8919997be86c26940a85b6b4846de19c08ad1b37(
    *,
    dataset_id: builtins.str,
    project_id: builtins.str,
    table_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99c059279c67702a6689b344f4cd666a68c2ed66b484d1909063aaed14817e4a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e92610c5c8cf1f5dfe8711345371a151da3d8ebf71276b277805e8a028e9d0f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82a626d7a5ed0b54ee4b293017fbf1086c98819858bcb818e18287cfa718ea58(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0efe03f64d4c645e92616373817cec6e6e59824d45ffc2a21dc6fec64d69651c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8967065c5338b7e415a4b1b5861e9b30235e4f7fe4d9eb1afa911cb6336da5cb(
    value: typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindingsOutputConfigTable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6fb2a2e6c436bd5f88c5ef9cab9483f7babb57f49f83770d8a316ebd5b8c566(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f092e5d3963e076c06dc47c696b1a744f5d801677b9fbff68c8a8ade0a8bfb2b(
    value: typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobActionsSaveFindings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5cad2701fbf31fd40d603a71601e1c5aa7850d18835bcc47b7c0c4b63683fa9d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9e35eb8942f23d8ed4a312ebb111d2422a8e579c93e09bdf81499fd7b406f31(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDataLossPreventionJobTriggerInspectJobActions, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ca2ccdff2b660c95c1767469594f616cd41abc70530bab3071929b0939ff037(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfdd83e0c3fc087e01e8d74b9bab7830f9fdb30e5d3cd4994e3ebb584700b261(
    value: typing.Optional[GoogleDataLossPreventionJobTriggerInspectJob],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__470cc6c8770a59ea47874d7524831f8907158a8c09276bea5107c098d0b29df4(
    *,
    big_query_options: typing.Optional[typing.Union[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    cloud_storage_options: typing.Optional[typing.Union[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    datastore_options: typing.Optional[typing.Union[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    timespan_config: typing.Optional[typing.Union[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfig, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b8106c2022e7767c786de413eb10f7ae98775626901c5a3ab4abe84bd6488cb(
    *,
    table_reference: typing.Union[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptionsTableReference, typing.Dict[builtins.str, typing.Any]],
    rows_limit: typing.Optional[jsii.Number] = None,
    rows_limit_percent: typing.Optional[jsii.Number] = None,
    sample_method: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a9f8a81e90a8be6807dac86aa0133dd7e302e20974c9945a892065221f13da5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54f9a74f63452d66fa169c13d48c1d148d56f299ca72becc27bfa74e003f7997(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__638ab826ec221a30183f15ea7a93b6b2c0954c6aaf9e34371b5efb54e7e0ff31(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fae2d214021a015e12903693b0024b7598ec3285936c77bfbc919e04fec7a545(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64309101dd0816e55471bc342d94dab5c889be4ab5a6cd831b801c4f633dfc25(
    value: typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c570b011b1902eb4439e906ad7c4e7405213ed752661ce8e191b0c2b2f9cdb84(
    *,
    dataset_id: builtins.str,
    project_id: builtins.str,
    table_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e58f5085c6ec7ab98460345a4c26d6b07d990c2b0274f99840caf7746bcb823(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8df201893ff971d20c66010e932b24e8996f55564ae5910e27201550aa455c8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90a0118fbbab94dda57c4129b3648ace1cd737df5c5ba10d237c8d264d9c6de1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__193303ff80d001e7b840306982962241d4ba1e3b01e25d659ab651fcaa3e166d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5237a92fd8cb9a7ca01b3f05f7a27d7f48ce923e7358bfc3aee8e99bddb0c596(
    value: typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigBigQueryOptionsTableReference],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__011773d25ad301e98af04c879d6c51700237ae264b51dedc7fe8d7dc589a3966(
    *,
    file_set: typing.Union[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSet, typing.Dict[builtins.str, typing.Any]],
    bytes_limit_per_file: typing.Optional[jsii.Number] = None,
    bytes_limit_per_file_percent: typing.Optional[jsii.Number] = None,
    files_limit_percent: typing.Optional[jsii.Number] = None,
    file_types: typing.Optional[typing.Sequence[builtins.str]] = None,
    sample_method: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea613cbb1936411886dfcf181274f55ce8c9f414d97002627aa94cc06dbb831b(
    *,
    regex_file_set: typing.Optional[typing.Union[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetRegexFileSet, typing.Dict[builtins.str, typing.Any]]] = None,
    url: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87ddf879abec18d153c9ecb1fe9ce8eab5597cef4a48369ac120174c705f78f3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d479b80697bd65be485eaa94a87df63c8d987f4fc05a9d027b3d3bf51ed30de9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45d05c35a866a2acf54b439f9f9646749fe4d5aa3705c2acf19ee2f00659f9b0(
    value: typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSet],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7207511cb2fc3e4d5ce4cc7e99ed57c29d5809c273864229cf0ee09802f77504(
    *,
    bucket_name: builtins.str,
    exclude_regex: typing.Optional[typing.Sequence[builtins.str]] = None,
    include_regex: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__345a30286b67ba2eea9088818dd3f7fd8a2201041f8521aad4f9e4bb7682488f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe2896baaaa9434d58943169281dd2f3d0a498180a049d5c0e7d54687e689801(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__958329c24396a5beb84e54211f99ba3dece1b5a02b65e9077a47250d3069bb1c(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0ded93286b1c2e56f168c1b8c8fe43dc2b3b740eade8edd90839b0f932a3362(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b13516bde22a41d741ebe4cebedc1106e8de7caa68b86c4e67eb353b96b3258f(
    value: typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetRegexFileSet],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__591f5a47569bed6356dc433ef62e62a1e0f75a5b71b81eb6cbe5538e8d1c66a8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc56f04e12c0ed1dd28b06f6afd7c91ef1b719a2cfe2eeed4be5f1185e91b771(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03366031435dea843d2f884aa19f8870fd74fac93b7894060fc9cb1feed91f0e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d768974c4528eaa132cdb50255114c3dbb1d7ca9e00e3680826608f2a6d4e322(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf33bd81bdbc32b739295c37076e7e38d3416290a6f4b587e10e39adbdbf57be(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a9194a8dcfd2410cf31efe23d560b0f9651b03a4419a61468ef109b1f4fdfd8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8af5f8e50c60ff93f8166f46696cef9906c501f460f4a411f7381835c09b23fc(
    value: typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigCloudStorageOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0df70fe325aff760dadf4c76a30ac090c7462360b26c4c80b6f44dde5a4c857(
    *,
    kind: typing.Union[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsKind, typing.Dict[builtins.str, typing.Any]],
    partition_id: typing.Union[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsPartitionId, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32de240167b5f71bbd1b18a6cbb8510724f89f459e18917e2cc38e0957ee08bf(
    *,
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__845c2160bf04dfe18d77534cfa400dd3daec156b31b9618f32cde60272ea5954(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b179d4fd81a88df354c76c14d39c787b68c4550fa1280b569bb526c2a5d87b18(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29ed8a35bb36910d10960af47fe6aad99d9255a2f1fe3af4407462a00b1d2d79(
    value: typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsKind],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42ab23e9d6e4dddb911e54c5e09f94849dc648f9c0444b5f73ebee4c35722ef8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e62269aea7dbceb5e1e44854a12434f646ae59058bc8600c3a449018e411a47e(
    value: typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__090d678c444c13bbd535bfbc1aaac700cdf1e27e496597c0e54b3e76d67b7584(
    *,
    project_id: builtins.str,
    namespace_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__573268f1e46ce0cac23683741f19a2abf8de99047216746ed926b5ee11c425b0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45f711b7be9c381cfba7ae23ba26ceaf169c278108c8dcb5a7afa332bdfcbc0f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ff58d99a84b803f63591572901f1cc2a050350388d92583d7d70f2357f3ee31(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ab7a2001772d8134296ce8948e54e1ed14fb7ddcf0aa7bc98fab489e6f1136c(
    value: typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigDatastoreOptionsPartitionId],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0a416030319e43eded9f6fc27911924421226085a39e3a1424addf1e560356f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f78ff5a9b71efd577fd3b575b6d6137bcafeaa580baad08591d1eb5fb21bf68f(
    value: typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f600b382e656d175bb217f904173c392c9ff5f0d95982191d63ec7b31c6fda4(
    *,
    timestamp_field: typing.Union[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfigTimestampField, typing.Dict[builtins.str, typing.Any]],
    enable_auto_population_of_timespan_config: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    end_time: typing.Optional[builtins.str] = None,
    start_time: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7ebe486568fbc7cf72b6ea3993aba85860c7b22005ac1a859ad3882757e6a88(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fe5ed60194cb53649f0037563d195faf34257eecaa4bf94d7453d82dde4a7f7(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__606dd34308eb5b17bc8bbdd57ec3ac2d2f4b0f4eb918e84560f4c8ceca5147f0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92c400479d32678af9ff9b8f556db388f1a3b775aef9b72d778051087c18e18c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__953733e038856ce953dd9f3df41f0c212cf3c19f0346a82204744e88314f80d5(
    value: typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4cca4a1a0e0d01e2b7b4dd815070083e4ba32903e79d13f890806ffec1c42338(
    *,
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a605d15d285fe8c1efd4f483eea1fb866ee51580fad608faa0aac77fc19e141d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3bddd8b1ae5308cdc5537e8f87851532af43da3ffbb5d1ce953c75c674e93f59(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__236627631377cc30458d4a9cb85aa125fe334d2d2acb17a05bbb287828171695(
    value: typing.Optional[GoogleDataLossPreventionJobTriggerInspectJobStorageConfigTimespanConfigTimestampField],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28a69dc1bbd0162e5c6a2f793517529cc3aafbf29095e17e715b93ec100610d0(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed0e3419cc2cad7a4369fb91f74c6732b89f5d2c4934882254a938de701a0ef8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee1a96c3412c6efc06c95fa5090e11b67e4348c38563faee4c70ee038788f26d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2951922c5dc2c0af344219d5b2c237164043f535d7b69c91f0d7301a8d8d41aa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96d88b47cf765365d3247be97e0f52fbe746f576e81263be5b76d3a79143de30(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e863f2ca9368abcebd14ac9283e5d19fb37008b5a0ab5e63457b20f7ceaca4fa(
    value: typing.Optional[typing.Union[GoogleDataLossPreventionJobTriggerTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc8a480e434e0a23ab48b67ea4211cd10dfa60639a1ed0d0eea1d557d4c16ff8(
    *,
    schedule: typing.Optional[typing.Union[GoogleDataLossPreventionJobTriggerTriggersSchedule, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ebfba5fa920928859e306ab34503f76fdf9a6b686d8ddb4e3ee49f4c656a59f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a68cd8117528236fe1a5db7d8dc038cf74d62d62f291a524126999709967b39(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5322412c0443b2859688ebc0e69dc04a6499e53b067544603b36eb0121944562(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58d3703b770c1730ece4e9e6f8fc0681795017811fd74b3b2874bb8ff0d2c26d(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8474b296512dab021e1c14fb81659aa1e05e3760381f82ee666ae101901fb782(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f59a66d1df3e710f9a78e74044d22526d1a3bb9825d15a93b209105f2424dff1(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDataLossPreventionJobTriggerTriggers]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b171d26728b745fa116f4e8f6733bc5604adc21ce997d164db4d5d16a6573af4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8cb1fb0a2baf581892b6717f0241bfcdbab9991d00ae751aef4a1afbd8a7af9(
    value: typing.Optional[typing.Union[GoogleDataLossPreventionJobTriggerTriggers, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1753ba366c5259478451cd691f732e667136e3b24ff9cc1d0ecbcc35c51c1b9a(
    *,
    recurrence_period_duration: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ba77c04cc76ec4fb919d7f4241569b7af8509f48534f2af7f20385d06c6e401(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de1773cae7784a12deb8b2d195becf09e34a711351cf1c362748d84d775f7dc4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e15c216c146ecce28cc440557ff966ef712bff6c43ae013974c62d66982880fe(
    value: typing.Optional[GoogleDataLossPreventionJobTriggerTriggersSchedule],
) -> None:
    """Type checking stubs"""
    pass
