'''
# `google_datastream_stream`

Refer to the Terraform Registory for docs: [`google_datastream_stream`](https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream).
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


class GoogleDatastreamStream(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStream",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream google_datastream_stream}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        destination_config: typing.Union["GoogleDatastreamStreamDestinationConfig", typing.Dict[builtins.str, typing.Any]],
        display_name: builtins.str,
        location: builtins.str,
        source_config: typing.Union["GoogleDatastreamStreamSourceConfig", typing.Dict[builtins.str, typing.Any]],
        stream_id: builtins.str,
        backfill_all: typing.Optional[typing.Union["GoogleDatastreamStreamBackfillAll", typing.Dict[builtins.str, typing.Any]]] = None,
        backfill_none: typing.Optional[typing.Union["GoogleDatastreamStreamBackfillNone", typing.Dict[builtins.str, typing.Any]]] = None,
        desired_state: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        project: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleDatastreamStreamTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream google_datastream_stream} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param destination_config: destination_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#destination_config GoogleDatastreamStream#destination_config}
        :param display_name: Display name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#display_name GoogleDatastreamStream#display_name}
        :param location: The name of the location this stream is located in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#location GoogleDatastreamStream#location}
        :param source_config: source_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#source_config GoogleDatastreamStream#source_config}
        :param stream_id: The stream identifier. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#stream_id GoogleDatastreamStream#stream_id}
        :param backfill_all: backfill_all block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#backfill_all GoogleDatastreamStream#backfill_all}
        :param backfill_none: backfill_none block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#backfill_none GoogleDatastreamStream#backfill_none}
        :param desired_state: Desired state of the Stream. Set this field to 'RUNNING' to start the stream, and 'PAUSED' to pause the stream. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#desired_state GoogleDatastreamStream#desired_state}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#id GoogleDatastreamStream#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: Labels. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#labels GoogleDatastreamStream#labels}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#project GoogleDatastreamStream#project}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#timeouts GoogleDatastreamStream#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6cfa931a0c0c189dada75078e20e325e1684379e1ca40acf3c5e5b9c924ed26)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleDatastreamStreamConfig(
            destination_config=destination_config,
            display_name=display_name,
            location=location,
            source_config=source_config,
            stream_id=stream_id,
            backfill_all=backfill_all,
            backfill_none=backfill_none,
            desired_state=desired_state,
            id=id,
            labels=labels,
            project=project,
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

    @jsii.member(jsii_name="putBackfillAll")
    def put_backfill_all(
        self,
        *,
        mysql_excluded_objects: typing.Optional[typing.Union["GoogleDatastreamStreamBackfillAllMysqlExcludedObjects", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param mysql_excluded_objects: mysql_excluded_objects block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#mysql_excluded_objects GoogleDatastreamStream#mysql_excluded_objects}
        '''
        value = GoogleDatastreamStreamBackfillAll(
            mysql_excluded_objects=mysql_excluded_objects
        )

        return typing.cast(None, jsii.invoke(self, "putBackfillAll", [value]))

    @jsii.member(jsii_name="putBackfillNone")
    def put_backfill_none(self) -> None:
        value = GoogleDatastreamStreamBackfillNone()

        return typing.cast(None, jsii.invoke(self, "putBackfillNone", [value]))

    @jsii.member(jsii_name="putDestinationConfig")
    def put_destination_config(
        self,
        *,
        destination_connection_profile: builtins.str,
        bigquery_destination_config: typing.Optional[typing.Union["GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        gcs_destination_config: typing.Optional[typing.Union["GoogleDatastreamStreamDestinationConfigGcsDestinationConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param destination_connection_profile: Destination connection profile resource. Format: projects/{project}/locations/{location}/connectionProfiles/{name}. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#destination_connection_profile GoogleDatastreamStream#destination_connection_profile}
        :param bigquery_destination_config: bigquery_destination_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#bigquery_destination_config GoogleDatastreamStream#bigquery_destination_config}
        :param gcs_destination_config: gcs_destination_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#gcs_destination_config GoogleDatastreamStream#gcs_destination_config}
        '''
        value = GoogleDatastreamStreamDestinationConfig(
            destination_connection_profile=destination_connection_profile,
            bigquery_destination_config=bigquery_destination_config,
            gcs_destination_config=gcs_destination_config,
        )

        return typing.cast(None, jsii.invoke(self, "putDestinationConfig", [value]))

    @jsii.member(jsii_name="putSourceConfig")
    def put_source_config(
        self,
        *,
        mysql_source_config: typing.Union["GoogleDatastreamStreamSourceConfigMysqlSourceConfig", typing.Dict[builtins.str, typing.Any]],
        source_connection_profile: builtins.str,
    ) -> None:
        '''
        :param mysql_source_config: mysql_source_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#mysql_source_config GoogleDatastreamStream#mysql_source_config}
        :param source_connection_profile: Source connection profile resource. Format: projects/{project}/locations/{location}/connectionProfiles/{name}. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#source_connection_profile GoogleDatastreamStream#source_connection_profile}
        '''
        value = GoogleDatastreamStreamSourceConfig(
            mysql_source_config=mysql_source_config,
            source_connection_profile=source_connection_profile,
        )

        return typing.cast(None, jsii.invoke(self, "putSourceConfig", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#create GoogleDatastreamStream#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#delete GoogleDatastreamStream#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#update GoogleDatastreamStream#update}.
        '''
        value = GoogleDatastreamStreamTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetBackfillAll")
    def reset_backfill_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackfillAll", []))

    @jsii.member(jsii_name="resetBackfillNone")
    def reset_backfill_none(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackfillNone", []))

    @jsii.member(jsii_name="resetDesiredState")
    def reset_desired_state(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDesiredState", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

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
    @jsii.member(jsii_name="backfillAll")
    def backfill_all(self) -> "GoogleDatastreamStreamBackfillAllOutputReference":
        return typing.cast("GoogleDatastreamStreamBackfillAllOutputReference", jsii.get(self, "backfillAll"))

    @builtins.property
    @jsii.member(jsii_name="backfillNone")
    def backfill_none(self) -> "GoogleDatastreamStreamBackfillNoneOutputReference":
        return typing.cast("GoogleDatastreamStreamBackfillNoneOutputReference", jsii.get(self, "backfillNone"))

    @builtins.property
    @jsii.member(jsii_name="destinationConfig")
    def destination_config(
        self,
    ) -> "GoogleDatastreamStreamDestinationConfigOutputReference":
        return typing.cast("GoogleDatastreamStreamDestinationConfigOutputReference", jsii.get(self, "destinationConfig"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="sourceConfig")
    def source_config(self) -> "GoogleDatastreamStreamSourceConfigOutputReference":
        return typing.cast("GoogleDatastreamStreamSourceConfigOutputReference", jsii.get(self, "sourceConfig"))

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleDatastreamStreamTimeoutsOutputReference":
        return typing.cast("GoogleDatastreamStreamTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="backfillAllInput")
    def backfill_all_input(
        self,
    ) -> typing.Optional["GoogleDatastreamStreamBackfillAll"]:
        return typing.cast(typing.Optional["GoogleDatastreamStreamBackfillAll"], jsii.get(self, "backfillAllInput"))

    @builtins.property
    @jsii.member(jsii_name="backfillNoneInput")
    def backfill_none_input(
        self,
    ) -> typing.Optional["GoogleDatastreamStreamBackfillNone"]:
        return typing.cast(typing.Optional["GoogleDatastreamStreamBackfillNone"], jsii.get(self, "backfillNoneInput"))

    @builtins.property
    @jsii.member(jsii_name="desiredStateInput")
    def desired_state_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "desiredStateInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationConfigInput")
    def destination_config_input(
        self,
    ) -> typing.Optional["GoogleDatastreamStreamDestinationConfig"]:
        return typing.cast(typing.Optional["GoogleDatastreamStreamDestinationConfig"], jsii.get(self, "destinationConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceConfigInput")
    def source_config_input(
        self,
    ) -> typing.Optional["GoogleDatastreamStreamSourceConfig"]:
        return typing.cast(typing.Optional["GoogleDatastreamStreamSourceConfig"], jsii.get(self, "sourceConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="streamIdInput")
    def stream_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "streamIdInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleDatastreamStreamTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleDatastreamStreamTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="desiredState")
    def desired_state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "desiredState"))

    @desired_state.setter
    def desired_state(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f02e6d6086a6388386fbb0384210f4e368b675aedef36739e15a9b27dc467a86)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "desiredState", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ece6a77832fb6e89cc0916a10ebc588b04c7d7e93bf43677ad16f9563954cdc9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f14ff4627f324370937935159e22c59189775d0e3b599757fff0ae7935aca61)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6f63ddf26cb02e92cafbfd7bc5446de232f6b8cb951cc5271c9cd8ef7edbd70)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08807dc9fe2f3212f60603e2be9674d576d9b9ebb97552f37256b43f078e57e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c2f2d9b51d02843746ef23bac88dfc96d8afb17d58d75cfc3fd4c132223b5fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="streamId")
    def stream_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "streamId"))

    @stream_id.setter
    def stream_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83b1410afdedd1ac85863a7d2b94759e47bfea699a0ad11b60e2b915ef038f04)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "streamId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamBackfillAll",
    jsii_struct_bases=[],
    name_mapping={"mysql_excluded_objects": "mysqlExcludedObjects"},
)
class GoogleDatastreamStreamBackfillAll:
    def __init__(
        self,
        *,
        mysql_excluded_objects: typing.Optional[typing.Union["GoogleDatastreamStreamBackfillAllMysqlExcludedObjects", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param mysql_excluded_objects: mysql_excluded_objects block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#mysql_excluded_objects GoogleDatastreamStream#mysql_excluded_objects}
        '''
        if isinstance(mysql_excluded_objects, dict):
            mysql_excluded_objects = GoogleDatastreamStreamBackfillAllMysqlExcludedObjects(**mysql_excluded_objects)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e29d6dac06c9011c575a9755f405c8c91c314097f849d543ea610c2ae0604ac9)
            check_type(argname="argument mysql_excluded_objects", value=mysql_excluded_objects, expected_type=type_hints["mysql_excluded_objects"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if mysql_excluded_objects is not None:
            self._values["mysql_excluded_objects"] = mysql_excluded_objects

    @builtins.property
    def mysql_excluded_objects(
        self,
    ) -> typing.Optional["GoogleDatastreamStreamBackfillAllMysqlExcludedObjects"]:
        '''mysql_excluded_objects block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#mysql_excluded_objects GoogleDatastreamStream#mysql_excluded_objects}
        '''
        result = self._values.get("mysql_excluded_objects")
        return typing.cast(typing.Optional["GoogleDatastreamStreamBackfillAllMysqlExcludedObjects"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamBackfillAll(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamBackfillAllMysqlExcludedObjects",
    jsii_struct_bases=[],
    name_mapping={"mysql_databases": "mysqlDatabases"},
)
class GoogleDatastreamStreamBackfillAllMysqlExcludedObjects:
    def __init__(
        self,
        *,
        mysql_databases: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabases", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param mysql_databases: mysql_databases block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#mysql_databases GoogleDatastreamStream#mysql_databases}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d07bf1e73cbfa0c9924cbdd112f8758d8c5843cb05b182d0821feebbecf1bbfe)
            check_type(argname="argument mysql_databases", value=mysql_databases, expected_type=type_hints["mysql_databases"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "mysql_databases": mysql_databases,
        }

    @builtins.property
    def mysql_databases(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabases"]]:
        '''mysql_databases block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#mysql_databases GoogleDatastreamStream#mysql_databases}
        '''
        result = self._values.get("mysql_databases")
        assert result is not None, "Required property 'mysql_databases' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabases"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamBackfillAllMysqlExcludedObjects(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabases",
    jsii_struct_bases=[],
    name_mapping={"database": "database", "mysql_tables": "mysqlTables"},
)
class GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabases:
    def __init__(
        self,
        *,
        database: builtins.str,
        mysql_tables: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTables", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param database: Database name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#database GoogleDatastreamStream#database}
        :param mysql_tables: mysql_tables block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#mysql_tables GoogleDatastreamStream#mysql_tables}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__520481cec23840384472636822f5e61482b5d1f652a122cd771b9d999695e41c)
            check_type(argname="argument database", value=database, expected_type=type_hints["database"])
            check_type(argname="argument mysql_tables", value=mysql_tables, expected_type=type_hints["mysql_tables"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "database": database,
        }
        if mysql_tables is not None:
            self._values["mysql_tables"] = mysql_tables

    @builtins.property
    def database(self) -> builtins.str:
        '''Database name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#database GoogleDatastreamStream#database}
        '''
        result = self._values.get("database")
        assert result is not None, "Required property 'database' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def mysql_tables(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTables"]]]:
        '''mysql_tables block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#mysql_tables GoogleDatastreamStream#mysql_tables}
        '''
        result = self._values.get("mysql_tables")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTables"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabases(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__42870644565e23d6a0facda4476561b2c813f8b187a9bef2d4b42bd3b22f4ad7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c27e6265ec073c6cb9d937296a3009c85694518ceb542eb262dc396c0fa0643)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b9f5caf8e7a7472f002063d637ce85c365c019c129961190ee0484f83cb0204)
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
            type_hints = typing.get_type_hints(_typecheckingstub__df989554faa58557b3cee076a0334b3352d497fa9a172a9bc1154b271b849c0d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8ff79f76bcf20116f1f916672658b25c9c6061a155abec3dc69a9fe18fcebc28)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabases]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabases]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabases]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef052bf283a0faa4298ce68f02ad4567fa25c2230ddec569bcbb3eee18d62299)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTables",
    jsii_struct_bases=[],
    name_mapping={"table": "table", "mysql_columns": "mysqlColumns"},
)
class GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTables:
    def __init__(
        self,
        *,
        table: builtins.str,
        mysql_columns: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumns", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param table: Table name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#table GoogleDatastreamStream#table}
        :param mysql_columns: mysql_columns block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#mysql_columns GoogleDatastreamStream#mysql_columns}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3636dc049bfc21560723eff546dfc6111fc1c67103fa20091fcb54e69eb14642)
            check_type(argname="argument table", value=table, expected_type=type_hints["table"])
            check_type(argname="argument mysql_columns", value=mysql_columns, expected_type=type_hints["mysql_columns"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "table": table,
        }
        if mysql_columns is not None:
            self._values["mysql_columns"] = mysql_columns

    @builtins.property
    def table(self) -> builtins.str:
        '''Table name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#table GoogleDatastreamStream#table}
        '''
        result = self._values.get("table")
        assert result is not None, "Required property 'table' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def mysql_columns(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumns"]]]:
        '''mysql_columns block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#mysql_columns GoogleDatastreamStream#mysql_columns}
        '''
        result = self._values.get("mysql_columns")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumns"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTables(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__bb36c3ec485d5aa4159c543dbc6060937941194b2d7d16197d5fb5b186c37df9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ea3aa0c93b140d0d206e8e869f0817da6984fb7a0b1aff3d6241d5e683dbbe6)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ad0c9c602594fd4c30646475e0cb03862cdafe47fef23ee13c7b73b8b81d3bf)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4e409c71a7a46ac3ff0a29f111eb9a54fb36f9b824b997eebe0be60e76c7c343)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c0be506fa80b767248dcaa2cb7ed0462bf54b31e761efd4e0fa33f50b4cc6fe9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTables]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTables]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTables]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4fd33626f965d1fd3a29041aa974d9db1d19cf1b45b7027bfc2e9bd65550d21d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumns",
    jsii_struct_bases=[],
    name_mapping={
        "collation": "collation",
        "column": "column",
        "data_type": "dataType",
        "nullable": "nullable",
        "ordinal_position": "ordinalPosition",
        "primary_key": "primaryKey",
    },
)
class GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumns:
    def __init__(
        self,
        *,
        collation: typing.Optional[builtins.str] = None,
        column: typing.Optional[builtins.str] = None,
        data_type: typing.Optional[builtins.str] = None,
        nullable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        ordinal_position: typing.Optional[jsii.Number] = None,
        primary_key: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param collation: Column collation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#collation GoogleDatastreamStream#collation}
        :param column: Column name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#column GoogleDatastreamStream#column}
        :param data_type: The MySQL data type. Full data types list can be found here: https://dev.mysql.com/doc/refman/8.0/en/data-types.html. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#data_type GoogleDatastreamStream#data_type}
        :param nullable: Whether or not the column can accept a null value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#nullable GoogleDatastreamStream#nullable}
        :param ordinal_position: The ordinal position of the column in the table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#ordinal_position GoogleDatastreamStream#ordinal_position}
        :param primary_key: Whether or not the column represents a primary key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#primary_key GoogleDatastreamStream#primary_key}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23a54185e20f6073f2e24e14685a1bb95703a2f3f4ab9e6eea9d3117b60799c9)
            check_type(argname="argument collation", value=collation, expected_type=type_hints["collation"])
            check_type(argname="argument column", value=column, expected_type=type_hints["column"])
            check_type(argname="argument data_type", value=data_type, expected_type=type_hints["data_type"])
            check_type(argname="argument nullable", value=nullable, expected_type=type_hints["nullable"])
            check_type(argname="argument ordinal_position", value=ordinal_position, expected_type=type_hints["ordinal_position"])
            check_type(argname="argument primary_key", value=primary_key, expected_type=type_hints["primary_key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if collation is not None:
            self._values["collation"] = collation
        if column is not None:
            self._values["column"] = column
        if data_type is not None:
            self._values["data_type"] = data_type
        if nullable is not None:
            self._values["nullable"] = nullable
        if ordinal_position is not None:
            self._values["ordinal_position"] = ordinal_position
        if primary_key is not None:
            self._values["primary_key"] = primary_key

    @builtins.property
    def collation(self) -> typing.Optional[builtins.str]:
        '''Column collation.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#collation GoogleDatastreamStream#collation}
        '''
        result = self._values.get("collation")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def column(self) -> typing.Optional[builtins.str]:
        '''Column name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#column GoogleDatastreamStream#column}
        '''
        result = self._values.get("column")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_type(self) -> typing.Optional[builtins.str]:
        '''The MySQL data type. Full data types list can be found here: https://dev.mysql.com/doc/refman/8.0/en/data-types.html.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#data_type GoogleDatastreamStream#data_type}
        '''
        result = self._values.get("data_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def nullable(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether or not the column can accept a null value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#nullable GoogleDatastreamStream#nullable}
        '''
        result = self._values.get("nullable")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def ordinal_position(self) -> typing.Optional[jsii.Number]:
        '''The ordinal position of the column in the table.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#ordinal_position GoogleDatastreamStream#ordinal_position}
        '''
        result = self._values.get("ordinal_position")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def primary_key(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether or not the column represents a primary key.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#primary_key GoogleDatastreamStream#primary_key}
        '''
        result = self._values.get("primary_key")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumns(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumnsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumnsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6e6d7e7079d2c891205e2b32b0cf2ceba725f724854f198bf8512979a5696ce8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumnsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84e67f89a6476bdc5c731333cf2029e4a5c782f368d3d69f03978d2ce9dcd94b)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumnsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa3cdc2a83c6840973d4070e34bf50a07ee5f2c7d1f3c68e499ac847bfa79317)
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
            type_hints = typing.get_type_hints(_typecheckingstub__22b091b27124f81de04d4b89dc1049358fc60349f3193740d406a0ce1c9e7eeb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__88ef5e48f6385d0236f06a58e25f81251bbc3e6f2240cd75930e6be6beaec4de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumns]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumns]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumns]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f64de49e3b7a392b9d7c9e39a5e5b791d02929fb6fb384bc5ded7da1c10e90da)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumnsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumnsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7292c72a6c771de19158c3d655adc2ba6b3d55d617a83d86255518effa23ba98)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCollation")
    def reset_collation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCollation", []))

    @jsii.member(jsii_name="resetColumn")
    def reset_column(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetColumn", []))

    @jsii.member(jsii_name="resetDataType")
    def reset_data_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataType", []))

    @jsii.member(jsii_name="resetNullable")
    def reset_nullable(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNullable", []))

    @jsii.member(jsii_name="resetOrdinalPosition")
    def reset_ordinal_position(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrdinalPosition", []))

    @jsii.member(jsii_name="resetPrimaryKey")
    def reset_primary_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrimaryKey", []))

    @builtins.property
    @jsii.member(jsii_name="length")
    def length(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "length"))

    @builtins.property
    @jsii.member(jsii_name="collationInput")
    def collation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "collationInput"))

    @builtins.property
    @jsii.member(jsii_name="columnInput")
    def column_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "columnInput"))

    @builtins.property
    @jsii.member(jsii_name="dataTypeInput")
    def data_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="nullableInput")
    def nullable_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "nullableInput"))

    @builtins.property
    @jsii.member(jsii_name="ordinalPositionInput")
    def ordinal_position_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ordinalPositionInput"))

    @builtins.property
    @jsii.member(jsii_name="primaryKeyInput")
    def primary_key_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "primaryKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="collation")
    def collation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "collation"))

    @collation.setter
    def collation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bbe8e9c9cb2a678b797af0d6f265ede6140c005c291f7a871610e2b0c46c1239)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "collation", value)

    @builtins.property
    @jsii.member(jsii_name="column")
    def column(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "column"))

    @column.setter
    def column(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5e78f3a0e42427fb9fe7d3218cf22fcd63107183474d933dbe292a0f22ada60)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "column", value)

    @builtins.property
    @jsii.member(jsii_name="dataType")
    def data_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataType"))

    @data_type.setter
    def data_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__801b81a5be1dff9dc10685707b5806e4749464fea9dee3509b069be09a39915d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataType", value)

    @builtins.property
    @jsii.member(jsii_name="nullable")
    def nullable(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "nullable"))

    @nullable.setter
    def nullable(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a4491c86d6cbca170107672efa5ae073217977e38d890ee684dfabffcdc9bbc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nullable", value)

    @builtins.property
    @jsii.member(jsii_name="ordinalPosition")
    def ordinal_position(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ordinalPosition"))

    @ordinal_position.setter
    def ordinal_position(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8adf2449960f783a3598bbe1db28d2f83ca4c95a6ca774684164731a9ca4603)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ordinalPosition", value)

    @builtins.property
    @jsii.member(jsii_name="primaryKey")
    def primary_key(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "primaryKey"))

    @primary_key.setter
    def primary_key(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3cfd6c4c2f5f53f106b06e68701b9e7338a0198f1de4971a3980cb71319134f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "primaryKey", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumns, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumns, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumns, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4e5c86192b35d7aa9f1c9ff0b2312d4c56114766b1948aeaa6cdb4a187c7447)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5510498980068046efbd3bccc489edaa11d41baf610cf3c6d8b04640da29f441)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putMysqlColumns")
    def put_mysql_columns(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumns, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1393719f87438cd6e681938c318697c567154ef4d21de037b9794b496d5c053)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMysqlColumns", [value]))

    @jsii.member(jsii_name="resetMysqlColumns")
    def reset_mysql_columns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMysqlColumns", []))

    @builtins.property
    @jsii.member(jsii_name="mysqlColumns")
    def mysql_columns(
        self,
    ) -> GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumnsList:
        return typing.cast(GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumnsList, jsii.get(self, "mysqlColumns"))

    @builtins.property
    @jsii.member(jsii_name="mysqlColumnsInput")
    def mysql_columns_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumns]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumns]]], jsii.get(self, "mysqlColumnsInput"))

    @builtins.property
    @jsii.member(jsii_name="tableInput")
    def table_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableInput"))

    @builtins.property
    @jsii.member(jsii_name="table")
    def table(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "table"))

    @table.setter
    def table(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b5cdd451c93c14f8bf1348dbc84d1613ee34bee075f1a7ef30641b00e9cc6ddf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "table", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTables, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTables, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTables, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40a46438b33027c86396b4bad6c02ccc4329f55d360d33ee604e8932c6d1d25f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9bb2b89ed5c7ab305b2df59f9f1fcae91cadc3414f28c3659364e57a3e1b6dbe)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putMysqlTables")
    def put_mysql_tables(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTables, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6be4542a5978109673a55f553153be687fb0155ae52e28084709f661e644b3d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMysqlTables", [value]))

    @jsii.member(jsii_name="resetMysqlTables")
    def reset_mysql_tables(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMysqlTables", []))

    @builtins.property
    @jsii.member(jsii_name="mysqlTables")
    def mysql_tables(
        self,
    ) -> GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesList:
        return typing.cast(GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesList, jsii.get(self, "mysqlTables"))

    @builtins.property
    @jsii.member(jsii_name="databaseInput")
    def database_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseInput"))

    @builtins.property
    @jsii.member(jsii_name="mysqlTablesInput")
    def mysql_tables_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTables]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTables]]], jsii.get(self, "mysqlTablesInput"))

    @builtins.property
    @jsii.member(jsii_name="database")
    def database(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "database"))

    @database.setter
    def database(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a8764873fb24dfdd954a5d2dbc34cad2573c675bedecb4826b1febb63d5437b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "database", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabases, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabases, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabases, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed873de9162601787f1de0b1f1d7bbc82ff2ff4f4f29dcdd5060713a530c99bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5b17ebe8e257a4918dda760ce5f15ec271e6f36463b2e0b3b2102f151e7afa5a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMysqlDatabases")
    def put_mysql_databases(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabases, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72168f0c6c5360f01d1caa68b898ee8a3874c0c09c031475e80aefbaf55f483b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMysqlDatabases", [value]))

    @builtins.property
    @jsii.member(jsii_name="mysqlDatabases")
    def mysql_databases(
        self,
    ) -> GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesList:
        return typing.cast(GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesList, jsii.get(self, "mysqlDatabases"))

    @builtins.property
    @jsii.member(jsii_name="mysqlDatabasesInput")
    def mysql_databases_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabases]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabases]]], jsii.get(self, "mysqlDatabasesInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDatastreamStreamBackfillAllMysqlExcludedObjects]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamBackfillAllMysqlExcludedObjects], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDatastreamStreamBackfillAllMysqlExcludedObjects],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49719e784f731e00fa4b5f129ee237712081738ae7d610fb8420b43adc072ede)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDatastreamStreamBackfillAllOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamBackfillAllOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e274f1c79b478e8a9935941ed6e1cae337452327e7e0df1b2e287933f42cb449)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMysqlExcludedObjects")
    def put_mysql_excluded_objects(
        self,
        *,
        mysql_databases: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabases, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param mysql_databases: mysql_databases block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#mysql_databases GoogleDatastreamStream#mysql_databases}
        '''
        value = GoogleDatastreamStreamBackfillAllMysqlExcludedObjects(
            mysql_databases=mysql_databases
        )

        return typing.cast(None, jsii.invoke(self, "putMysqlExcludedObjects", [value]))

    @jsii.member(jsii_name="resetMysqlExcludedObjects")
    def reset_mysql_excluded_objects(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMysqlExcludedObjects", []))

    @builtins.property
    @jsii.member(jsii_name="mysqlExcludedObjects")
    def mysql_excluded_objects(
        self,
    ) -> GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsOutputReference:
        return typing.cast(GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsOutputReference, jsii.get(self, "mysqlExcludedObjects"))

    @builtins.property
    @jsii.member(jsii_name="mysqlExcludedObjectsInput")
    def mysql_excluded_objects_input(
        self,
    ) -> typing.Optional[GoogleDatastreamStreamBackfillAllMysqlExcludedObjects]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamBackfillAllMysqlExcludedObjects], jsii.get(self, "mysqlExcludedObjectsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleDatastreamStreamBackfillAll]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamBackfillAll], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDatastreamStreamBackfillAll],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e18596f2739b568b00dc8878957e1a0ae36c322e4460e1efcc618a1fbd80dfb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamBackfillNone",
    jsii_struct_bases=[],
    name_mapping={},
)
class GoogleDatastreamStreamBackfillNone:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamBackfillNone(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDatastreamStreamBackfillNoneOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamBackfillNoneOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a7d92abc899aebc8d6d75893b1acd1ccfce0f432db79b875d3d4e45b3724468b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleDatastreamStreamBackfillNone]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamBackfillNone], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDatastreamStreamBackfillNone],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfa1cb735e7372c389d187e9df62ce48602d5e810e1d37efcc2c795f44eae0eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "destination_config": "destinationConfig",
        "display_name": "displayName",
        "location": "location",
        "source_config": "sourceConfig",
        "stream_id": "streamId",
        "backfill_all": "backfillAll",
        "backfill_none": "backfillNone",
        "desired_state": "desiredState",
        "id": "id",
        "labels": "labels",
        "project": "project",
        "timeouts": "timeouts",
    },
)
class GoogleDatastreamStreamConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        destination_config: typing.Union["GoogleDatastreamStreamDestinationConfig", typing.Dict[builtins.str, typing.Any]],
        display_name: builtins.str,
        location: builtins.str,
        source_config: typing.Union["GoogleDatastreamStreamSourceConfig", typing.Dict[builtins.str, typing.Any]],
        stream_id: builtins.str,
        backfill_all: typing.Optional[typing.Union[GoogleDatastreamStreamBackfillAll, typing.Dict[builtins.str, typing.Any]]] = None,
        backfill_none: typing.Optional[typing.Union[GoogleDatastreamStreamBackfillNone, typing.Dict[builtins.str, typing.Any]]] = None,
        desired_state: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        project: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleDatastreamStreamTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param destination_config: destination_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#destination_config GoogleDatastreamStream#destination_config}
        :param display_name: Display name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#display_name GoogleDatastreamStream#display_name}
        :param location: The name of the location this stream is located in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#location GoogleDatastreamStream#location}
        :param source_config: source_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#source_config GoogleDatastreamStream#source_config}
        :param stream_id: The stream identifier. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#stream_id GoogleDatastreamStream#stream_id}
        :param backfill_all: backfill_all block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#backfill_all GoogleDatastreamStream#backfill_all}
        :param backfill_none: backfill_none block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#backfill_none GoogleDatastreamStream#backfill_none}
        :param desired_state: Desired state of the Stream. Set this field to 'RUNNING' to start the stream, and 'PAUSED' to pause the stream. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#desired_state GoogleDatastreamStream#desired_state}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#id GoogleDatastreamStream#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: Labels. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#labels GoogleDatastreamStream#labels}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#project GoogleDatastreamStream#project}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#timeouts GoogleDatastreamStream#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(destination_config, dict):
            destination_config = GoogleDatastreamStreamDestinationConfig(**destination_config)
        if isinstance(source_config, dict):
            source_config = GoogleDatastreamStreamSourceConfig(**source_config)
        if isinstance(backfill_all, dict):
            backfill_all = GoogleDatastreamStreamBackfillAll(**backfill_all)
        if isinstance(backfill_none, dict):
            backfill_none = GoogleDatastreamStreamBackfillNone(**backfill_none)
        if isinstance(timeouts, dict):
            timeouts = GoogleDatastreamStreamTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8212616678ebc8f5f13dc67f8ecb8284c7ae5d6006e98280adbb52774b08f47)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument destination_config", value=destination_config, expected_type=type_hints["destination_config"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument source_config", value=source_config, expected_type=type_hints["source_config"])
            check_type(argname="argument stream_id", value=stream_id, expected_type=type_hints["stream_id"])
            check_type(argname="argument backfill_all", value=backfill_all, expected_type=type_hints["backfill_all"])
            check_type(argname="argument backfill_none", value=backfill_none, expected_type=type_hints["backfill_none"])
            check_type(argname="argument desired_state", value=desired_state, expected_type=type_hints["desired_state"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destination_config": destination_config,
            "display_name": display_name,
            "location": location,
            "source_config": source_config,
            "stream_id": stream_id,
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
        if backfill_all is not None:
            self._values["backfill_all"] = backfill_all
        if backfill_none is not None:
            self._values["backfill_none"] = backfill_none
        if desired_state is not None:
            self._values["desired_state"] = desired_state
        if id is not None:
            self._values["id"] = id
        if labels is not None:
            self._values["labels"] = labels
        if project is not None:
            self._values["project"] = project
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
    def destination_config(self) -> "GoogleDatastreamStreamDestinationConfig":
        '''destination_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#destination_config GoogleDatastreamStream#destination_config}
        '''
        result = self._values.get("destination_config")
        assert result is not None, "Required property 'destination_config' is missing"
        return typing.cast("GoogleDatastreamStreamDestinationConfig", result)

    @builtins.property
    def display_name(self) -> builtins.str:
        '''Display name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#display_name GoogleDatastreamStream#display_name}
        '''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def location(self) -> builtins.str:
        '''The name of the location this stream is located in.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#location GoogleDatastreamStream#location}
        '''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_config(self) -> "GoogleDatastreamStreamSourceConfig":
        '''source_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#source_config GoogleDatastreamStream#source_config}
        '''
        result = self._values.get("source_config")
        assert result is not None, "Required property 'source_config' is missing"
        return typing.cast("GoogleDatastreamStreamSourceConfig", result)

    @builtins.property
    def stream_id(self) -> builtins.str:
        '''The stream identifier.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#stream_id GoogleDatastreamStream#stream_id}
        '''
        result = self._values.get("stream_id")
        assert result is not None, "Required property 'stream_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def backfill_all(self) -> typing.Optional[GoogleDatastreamStreamBackfillAll]:
        '''backfill_all block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#backfill_all GoogleDatastreamStream#backfill_all}
        '''
        result = self._values.get("backfill_all")
        return typing.cast(typing.Optional[GoogleDatastreamStreamBackfillAll], result)

    @builtins.property
    def backfill_none(self) -> typing.Optional[GoogleDatastreamStreamBackfillNone]:
        '''backfill_none block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#backfill_none GoogleDatastreamStream#backfill_none}
        '''
        result = self._values.get("backfill_none")
        return typing.cast(typing.Optional[GoogleDatastreamStreamBackfillNone], result)

    @builtins.property
    def desired_state(self) -> typing.Optional[builtins.str]:
        '''Desired state of the Stream.

        Set this field to 'RUNNING' to start the stream, and 'PAUSED' to pause the stream.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#desired_state GoogleDatastreamStream#desired_state}
        '''
        result = self._values.get("desired_state")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#id GoogleDatastreamStream#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Labels.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#labels GoogleDatastreamStream#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#project GoogleDatastreamStream#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleDatastreamStreamTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#timeouts GoogleDatastreamStream#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleDatastreamStreamTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamDestinationConfig",
    jsii_struct_bases=[],
    name_mapping={
        "destination_connection_profile": "destinationConnectionProfile",
        "bigquery_destination_config": "bigqueryDestinationConfig",
        "gcs_destination_config": "gcsDestinationConfig",
    },
)
class GoogleDatastreamStreamDestinationConfig:
    def __init__(
        self,
        *,
        destination_connection_profile: builtins.str,
        bigquery_destination_config: typing.Optional[typing.Union["GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        gcs_destination_config: typing.Optional[typing.Union["GoogleDatastreamStreamDestinationConfigGcsDestinationConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param destination_connection_profile: Destination connection profile resource. Format: projects/{project}/locations/{location}/connectionProfiles/{name}. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#destination_connection_profile GoogleDatastreamStream#destination_connection_profile}
        :param bigquery_destination_config: bigquery_destination_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#bigquery_destination_config GoogleDatastreamStream#bigquery_destination_config}
        :param gcs_destination_config: gcs_destination_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#gcs_destination_config GoogleDatastreamStream#gcs_destination_config}
        '''
        if isinstance(bigquery_destination_config, dict):
            bigquery_destination_config = GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfig(**bigquery_destination_config)
        if isinstance(gcs_destination_config, dict):
            gcs_destination_config = GoogleDatastreamStreamDestinationConfigGcsDestinationConfig(**gcs_destination_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a082f18c6634f77c5c989c278a91ddf6916c61c1c1c1ecaeb403873feb786f6f)
            check_type(argname="argument destination_connection_profile", value=destination_connection_profile, expected_type=type_hints["destination_connection_profile"])
            check_type(argname="argument bigquery_destination_config", value=bigquery_destination_config, expected_type=type_hints["bigquery_destination_config"])
            check_type(argname="argument gcs_destination_config", value=gcs_destination_config, expected_type=type_hints["gcs_destination_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destination_connection_profile": destination_connection_profile,
        }
        if bigquery_destination_config is not None:
            self._values["bigquery_destination_config"] = bigquery_destination_config
        if gcs_destination_config is not None:
            self._values["gcs_destination_config"] = gcs_destination_config

    @builtins.property
    def destination_connection_profile(self) -> builtins.str:
        '''Destination connection profile resource. Format: projects/{project}/locations/{location}/connectionProfiles/{name}.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#destination_connection_profile GoogleDatastreamStream#destination_connection_profile}
        '''
        result = self._values.get("destination_connection_profile")
        assert result is not None, "Required property 'destination_connection_profile' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bigquery_destination_config(
        self,
    ) -> typing.Optional["GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfig"]:
        '''bigquery_destination_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#bigquery_destination_config GoogleDatastreamStream#bigquery_destination_config}
        '''
        result = self._values.get("bigquery_destination_config")
        return typing.cast(typing.Optional["GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfig"], result)

    @builtins.property
    def gcs_destination_config(
        self,
    ) -> typing.Optional["GoogleDatastreamStreamDestinationConfigGcsDestinationConfig"]:
        '''gcs_destination_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#gcs_destination_config GoogleDatastreamStream#gcs_destination_config}
        '''
        result = self._values.get("gcs_destination_config")
        return typing.cast(typing.Optional["GoogleDatastreamStreamDestinationConfigGcsDestinationConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamDestinationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfig",
    jsii_struct_bases=[],
    name_mapping={
        "data_freshness": "dataFreshness",
        "single_target_dataset": "singleTargetDataset",
        "source_hierarchy_datasets": "sourceHierarchyDatasets",
    },
)
class GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfig:
    def __init__(
        self,
        *,
        data_freshness: typing.Optional[builtins.str] = None,
        single_target_dataset: typing.Optional[typing.Union["GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDataset", typing.Dict[builtins.str, typing.Any]]] = None,
        source_hierarchy_datasets: typing.Optional[typing.Union["GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasets", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param data_freshness: The guaranteed data freshness (in seconds) when querying tables created by the stream. Editing this field will only affect new tables created in the future, but existing tables will not be impacted. Lower values mean that queries will return fresher data, but may result in higher cost. A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s". Defaults to 900s. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#data_freshness GoogleDatastreamStream#data_freshness}
        :param single_target_dataset: single_target_dataset block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#single_target_dataset GoogleDatastreamStream#single_target_dataset}
        :param source_hierarchy_datasets: source_hierarchy_datasets block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#source_hierarchy_datasets GoogleDatastreamStream#source_hierarchy_datasets}
        '''
        if isinstance(single_target_dataset, dict):
            single_target_dataset = GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDataset(**single_target_dataset)
        if isinstance(source_hierarchy_datasets, dict):
            source_hierarchy_datasets = GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasets(**source_hierarchy_datasets)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3a49c814b4f2ebe3deb762ed064f6ce81ac50435614e1bd2718d7e8651def96)
            check_type(argname="argument data_freshness", value=data_freshness, expected_type=type_hints["data_freshness"])
            check_type(argname="argument single_target_dataset", value=single_target_dataset, expected_type=type_hints["single_target_dataset"])
            check_type(argname="argument source_hierarchy_datasets", value=source_hierarchy_datasets, expected_type=type_hints["source_hierarchy_datasets"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if data_freshness is not None:
            self._values["data_freshness"] = data_freshness
        if single_target_dataset is not None:
            self._values["single_target_dataset"] = single_target_dataset
        if source_hierarchy_datasets is not None:
            self._values["source_hierarchy_datasets"] = source_hierarchy_datasets

    @builtins.property
    def data_freshness(self) -> typing.Optional[builtins.str]:
        '''The guaranteed data freshness (in seconds) when querying tables created by the stream.

        Editing this field will only affect new tables created in the future, but existing tables
        will not be impacted. Lower values mean that queries will return fresher data, but may result in higher cost.
        A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s". Defaults to 900s.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#data_freshness GoogleDatastreamStream#data_freshness}
        '''
        result = self._values.get("data_freshness")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def single_target_dataset(
        self,
    ) -> typing.Optional["GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDataset"]:
        '''single_target_dataset block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#single_target_dataset GoogleDatastreamStream#single_target_dataset}
        '''
        result = self._values.get("single_target_dataset")
        return typing.cast(typing.Optional["GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDataset"], result)

    @builtins.property
    def source_hierarchy_datasets(
        self,
    ) -> typing.Optional["GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasets"]:
        '''source_hierarchy_datasets block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#source_hierarchy_datasets GoogleDatastreamStream#source_hierarchy_datasets}
        '''
        result = self._values.get("source_hierarchy_datasets")
        return typing.cast(typing.Optional["GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasets"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a3391270fd72825792750d900baabf072a22d3aa8bfdf9b72803fa90f89feb99)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSingleTargetDataset")
    def put_single_target_dataset(self, *, dataset_id: builtins.str) -> None:
        '''
        :param dataset_id: Dataset ID in the format projects/{project}/datasets/{dataset_id}. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#dataset_id GoogleDatastreamStream#dataset_id}
        '''
        value = GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDataset(
            dataset_id=dataset_id
        )

        return typing.cast(None, jsii.invoke(self, "putSingleTargetDataset", [value]))

    @jsii.member(jsii_name="putSourceHierarchyDatasets")
    def put_source_hierarchy_datasets(
        self,
        *,
        dataset_template: typing.Union["GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplate", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param dataset_template: dataset_template block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#dataset_template GoogleDatastreamStream#dataset_template}
        '''
        value = GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasets(
            dataset_template=dataset_template
        )

        return typing.cast(None, jsii.invoke(self, "putSourceHierarchyDatasets", [value]))

    @jsii.member(jsii_name="resetDataFreshness")
    def reset_data_freshness(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataFreshness", []))

    @jsii.member(jsii_name="resetSingleTargetDataset")
    def reset_single_target_dataset(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSingleTargetDataset", []))

    @jsii.member(jsii_name="resetSourceHierarchyDatasets")
    def reset_source_hierarchy_datasets(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceHierarchyDatasets", []))

    @builtins.property
    @jsii.member(jsii_name="singleTargetDataset")
    def single_target_dataset(
        self,
    ) -> "GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDatasetOutputReference":
        return typing.cast("GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDatasetOutputReference", jsii.get(self, "singleTargetDataset"))

    @builtins.property
    @jsii.member(jsii_name="sourceHierarchyDatasets")
    def source_hierarchy_datasets(
        self,
    ) -> "GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsOutputReference":
        return typing.cast("GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsOutputReference", jsii.get(self, "sourceHierarchyDatasets"))

    @builtins.property
    @jsii.member(jsii_name="dataFreshnessInput")
    def data_freshness_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataFreshnessInput"))

    @builtins.property
    @jsii.member(jsii_name="singleTargetDatasetInput")
    def single_target_dataset_input(
        self,
    ) -> typing.Optional["GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDataset"]:
        return typing.cast(typing.Optional["GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDataset"], jsii.get(self, "singleTargetDatasetInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceHierarchyDatasetsInput")
    def source_hierarchy_datasets_input(
        self,
    ) -> typing.Optional["GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasets"]:
        return typing.cast(typing.Optional["GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasets"], jsii.get(self, "sourceHierarchyDatasetsInput"))

    @builtins.property
    @jsii.member(jsii_name="dataFreshness")
    def data_freshness(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataFreshness"))

    @data_freshness.setter
    def data_freshness(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc227360efefd83c13161506d90374637c3c2dba1821899cf3a429435283aaa2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataFreshness", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfig]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1e71cd219e14ea812cecfdb4e16eae14cb53d03b3d7baea51323b1fb77a39c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDataset",
    jsii_struct_bases=[],
    name_mapping={"dataset_id": "datasetId"},
)
class GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDataset:
    def __init__(self, *, dataset_id: builtins.str) -> None:
        '''
        :param dataset_id: Dataset ID in the format projects/{project}/datasets/{dataset_id}. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#dataset_id GoogleDatastreamStream#dataset_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8fb9ad9224f683a8eb1f9139234f286bd44fddeece5772c9709e709e591a645)
            check_type(argname="argument dataset_id", value=dataset_id, expected_type=type_hints["dataset_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "dataset_id": dataset_id,
        }

    @builtins.property
    def dataset_id(self) -> builtins.str:
        '''Dataset ID in the format projects/{project}/datasets/{dataset_id}.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#dataset_id GoogleDatastreamStream#dataset_id}
        '''
        result = self._values.get("dataset_id")
        assert result is not None, "Required property 'dataset_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDataset(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDatasetOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDatasetOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0a3d055ab4e6752ba6dfdb4394295e7f7318d4a3b762834c187cc27231d4ca7a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="datasetIdInput")
    def dataset_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datasetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="datasetId")
    def dataset_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datasetId"))

    @dataset_id.setter
    def dataset_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4c9b188fd123021caa994f45cf0394e7b3f43765b979d928e6f4d9f0621a963)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datasetId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDataset]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDataset], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDataset],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04350676f2a57de4c6c34fd5c31fe09fe4989c93a30002c55349461fcd324dd8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasets",
    jsii_struct_bases=[],
    name_mapping={"dataset_template": "datasetTemplate"},
)
class GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasets:
    def __init__(
        self,
        *,
        dataset_template: typing.Union["GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplate", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param dataset_template: dataset_template block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#dataset_template GoogleDatastreamStream#dataset_template}
        '''
        if isinstance(dataset_template, dict):
            dataset_template = GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplate(**dataset_template)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe99655d10da1ece8d92b4b95410a92466fc73978fb56cabdd00ce4872af7f30)
            check_type(argname="argument dataset_template", value=dataset_template, expected_type=type_hints["dataset_template"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "dataset_template": dataset_template,
        }

    @builtins.property
    def dataset_template(
        self,
    ) -> "GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplate":
        '''dataset_template block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#dataset_template GoogleDatastreamStream#dataset_template}
        '''
        result = self._values.get("dataset_template")
        assert result is not None, "Required property 'dataset_template' is missing"
        return typing.cast("GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplate", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasets(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplate",
    jsii_struct_bases=[],
    name_mapping={"location": "location", "dataset_id_prefix": "datasetIdPrefix"},
)
class GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplate:
    def __init__(
        self,
        *,
        location: builtins.str,
        dataset_id_prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param location: The geographic location where the dataset should reside. See https://cloud.google.com/bigquery/docs/locations for supported locations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#location GoogleDatastreamStream#location}
        :param dataset_id_prefix: If supplied, every created dataset will have its name prefixed by the provided value. The prefix and name will be separated by an underscore. i.e. _. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#dataset_id_prefix GoogleDatastreamStream#dataset_id_prefix}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10bc9309ea21fa94f6d71ec05001d53825566fb8b23e70b72f26ff70b216afbf)
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument dataset_id_prefix", value=dataset_id_prefix, expected_type=type_hints["dataset_id_prefix"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "location": location,
        }
        if dataset_id_prefix is not None:
            self._values["dataset_id_prefix"] = dataset_id_prefix

    @builtins.property
    def location(self) -> builtins.str:
        '''The geographic location where the dataset should reside. See https://cloud.google.com/bigquery/docs/locations for supported locations.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#location GoogleDatastreamStream#location}
        '''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dataset_id_prefix(self) -> typing.Optional[builtins.str]:
        '''If supplied, every created dataset will have its name prefixed by the provided value.

        The prefix and name will be separated by an underscore. i.e. _.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#dataset_id_prefix GoogleDatastreamStream#dataset_id_prefix}
        '''
        result = self._values.get("dataset_id_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplateOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplateOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__589f4d7cacffa3fe9eaf1ee753fd3bb86c046e23b7c2e374b0f0fe1f59848e72)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDatasetIdPrefix")
    def reset_dataset_id_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatasetIdPrefix", []))

    @builtins.property
    @jsii.member(jsii_name="datasetIdPrefixInput")
    def dataset_id_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datasetIdPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="datasetIdPrefix")
    def dataset_id_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datasetIdPrefix"))

    @dataset_id_prefix.setter
    def dataset_id_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3fa782c14749e41909d2558ed573b112c4f62c763ad09af5bb8000ea5bb08163)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datasetIdPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04028b6cda5a7527cf51ede06922de56ad34e57e9e59dc68cf55dbb105f0a0db)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplate]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplate], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplate],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5de30ee6e92d12ceb0bda2317dd12bfa52377bec516b2b2a517385018ff4fd37)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ec59f9ec651149d0621d83bf49acbf8ee0bbd34767529437d0eaab1d43196fba)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDatasetTemplate")
    def put_dataset_template(
        self,
        *,
        location: builtins.str,
        dataset_id_prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param location: The geographic location where the dataset should reside. See https://cloud.google.com/bigquery/docs/locations for supported locations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#location GoogleDatastreamStream#location}
        :param dataset_id_prefix: If supplied, every created dataset will have its name prefixed by the provided value. The prefix and name will be separated by an underscore. i.e. _. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#dataset_id_prefix GoogleDatastreamStream#dataset_id_prefix}
        '''
        value = GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplate(
            location=location, dataset_id_prefix=dataset_id_prefix
        )

        return typing.cast(None, jsii.invoke(self, "putDatasetTemplate", [value]))

    @builtins.property
    @jsii.member(jsii_name="datasetTemplate")
    def dataset_template(
        self,
    ) -> GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplateOutputReference:
        return typing.cast(GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplateOutputReference, jsii.get(self, "datasetTemplate"))

    @builtins.property
    @jsii.member(jsii_name="datasetTemplateInput")
    def dataset_template_input(
        self,
    ) -> typing.Optional[GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplate]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplate], jsii.get(self, "datasetTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasets]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasets], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasets],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ead61d6997a472aca9d935cc8910fa587fa5ce5f4d399617f914993534cca402)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamDestinationConfigGcsDestinationConfig",
    jsii_struct_bases=[],
    name_mapping={
        "avro_file_format": "avroFileFormat",
        "file_rotation_interval": "fileRotationInterval",
        "file_rotation_mb": "fileRotationMb",
        "json_file_format": "jsonFileFormat",
        "path": "path",
    },
)
class GoogleDatastreamStreamDestinationConfigGcsDestinationConfig:
    def __init__(
        self,
        *,
        avro_file_format: typing.Optional[typing.Union["GoogleDatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormat", typing.Dict[builtins.str, typing.Any]]] = None,
        file_rotation_interval: typing.Optional[builtins.str] = None,
        file_rotation_mb: typing.Optional[jsii.Number] = None,
        json_file_format: typing.Optional[typing.Union["GoogleDatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormat", typing.Dict[builtins.str, typing.Any]]] = None,
        path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param avro_file_format: avro_file_format block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#avro_file_format GoogleDatastreamStream#avro_file_format}
        :param file_rotation_interval: The maximum duration for which new events are added before a file is closed and a new file is created. A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s". Defaults to 900s. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#file_rotation_interval GoogleDatastreamStream#file_rotation_interval}
        :param file_rotation_mb: The maximum file size to be saved in the bucket. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#file_rotation_mb GoogleDatastreamStream#file_rotation_mb}
        :param json_file_format: json_file_format block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#json_file_format GoogleDatastreamStream#json_file_format}
        :param path: Path inside the Cloud Storage bucket to write data to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#path GoogleDatastreamStream#path}
        '''
        if isinstance(avro_file_format, dict):
            avro_file_format = GoogleDatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormat(**avro_file_format)
        if isinstance(json_file_format, dict):
            json_file_format = GoogleDatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormat(**json_file_format)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d10163a88a5e865a15e425114c10f9f67bb19cad50eff789fae98679356656a)
            check_type(argname="argument avro_file_format", value=avro_file_format, expected_type=type_hints["avro_file_format"])
            check_type(argname="argument file_rotation_interval", value=file_rotation_interval, expected_type=type_hints["file_rotation_interval"])
            check_type(argname="argument file_rotation_mb", value=file_rotation_mb, expected_type=type_hints["file_rotation_mb"])
            check_type(argname="argument json_file_format", value=json_file_format, expected_type=type_hints["json_file_format"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if avro_file_format is not None:
            self._values["avro_file_format"] = avro_file_format
        if file_rotation_interval is not None:
            self._values["file_rotation_interval"] = file_rotation_interval
        if file_rotation_mb is not None:
            self._values["file_rotation_mb"] = file_rotation_mb
        if json_file_format is not None:
            self._values["json_file_format"] = json_file_format
        if path is not None:
            self._values["path"] = path

    @builtins.property
    def avro_file_format(
        self,
    ) -> typing.Optional["GoogleDatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormat"]:
        '''avro_file_format block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#avro_file_format GoogleDatastreamStream#avro_file_format}
        '''
        result = self._values.get("avro_file_format")
        return typing.cast(typing.Optional["GoogleDatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormat"], result)

    @builtins.property
    def file_rotation_interval(self) -> typing.Optional[builtins.str]:
        '''The maximum duration for which new events are added before a file is closed and a new file is created.

        A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s". Defaults to 900s.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#file_rotation_interval GoogleDatastreamStream#file_rotation_interval}
        '''
        result = self._values.get("file_rotation_interval")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def file_rotation_mb(self) -> typing.Optional[jsii.Number]:
        '''The maximum file size to be saved in the bucket.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#file_rotation_mb GoogleDatastreamStream#file_rotation_mb}
        '''
        result = self._values.get("file_rotation_mb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def json_file_format(
        self,
    ) -> typing.Optional["GoogleDatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormat"]:
        '''json_file_format block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#json_file_format GoogleDatastreamStream#json_file_format}
        '''
        result = self._values.get("json_file_format")
        return typing.cast(typing.Optional["GoogleDatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormat"], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Path inside the Cloud Storage bucket to write data to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#path GoogleDatastreamStream#path}
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamDestinationConfigGcsDestinationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormat",
    jsii_struct_bases=[],
    name_mapping={},
)
class GoogleDatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormat:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormat(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormatOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormatOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d068a5a28bd2dac3ef4546b05167198e8dc3f67c53ef66378117e2eb38de3e13)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormat]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormat], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormat],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f08298ba4d0b3313ce13d92f69a9b0d3e473996f7259553f11037794731faf97)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormat",
    jsii_struct_bases=[],
    name_mapping={
        "compression": "compression",
        "schema_file_format": "schemaFileFormat",
    },
)
class GoogleDatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormat:
    def __init__(
        self,
        *,
        compression: typing.Optional[builtins.str] = None,
        schema_file_format: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param compression: Compression of the loaded JSON file. Possible values: ["NO_COMPRESSION", "GZIP"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#compression GoogleDatastreamStream#compression}
        :param schema_file_format: The schema file format along JSON data files. Possible values: ["NO_SCHEMA_FILE", "AVRO_SCHEMA_FILE"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#schema_file_format GoogleDatastreamStream#schema_file_format}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac5bf24309609d454116747fe1a8433f1d6909fbbae89e976eff2fea5165e8d7)
            check_type(argname="argument compression", value=compression, expected_type=type_hints["compression"])
            check_type(argname="argument schema_file_format", value=schema_file_format, expected_type=type_hints["schema_file_format"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if compression is not None:
            self._values["compression"] = compression
        if schema_file_format is not None:
            self._values["schema_file_format"] = schema_file_format

    @builtins.property
    def compression(self) -> typing.Optional[builtins.str]:
        '''Compression of the loaded JSON file. Possible values: ["NO_COMPRESSION", "GZIP"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#compression GoogleDatastreamStream#compression}
        '''
        result = self._values.get("compression")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schema_file_format(self) -> typing.Optional[builtins.str]:
        '''The schema file format along JSON data files. Possible values: ["NO_SCHEMA_FILE", "AVRO_SCHEMA_FILE"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#schema_file_format GoogleDatastreamStream#schema_file_format}
        '''
        result = self._values.get("schema_file_format")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormat(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormatOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormatOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__56acedeeab88a59e046f3eda7acc9a87997bd1e847f3661a1d2ecffcaf8ece46)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCompression")
    def reset_compression(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCompression", []))

    @jsii.member(jsii_name="resetSchemaFileFormat")
    def reset_schema_file_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchemaFileFormat", []))

    @builtins.property
    @jsii.member(jsii_name="compressionInput")
    def compression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "compressionInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaFileFormatInput")
    def schema_file_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schemaFileFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="compression")
    def compression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "compression"))

    @compression.setter
    def compression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca5cc438ef5b106f7a336d20a5581f3c31250831e9ffddefcd61b4d1d9ff878f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "compression", value)

    @builtins.property
    @jsii.member(jsii_name="schemaFileFormat")
    def schema_file_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schemaFileFormat"))

    @schema_file_format.setter
    def schema_file_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac1ec35e9777f4ddf604ec41ee7052c7ac0d48e85abfb0a0bc9ffd10834276d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schemaFileFormat", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormat]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormat], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormat],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d5e3c16b98749306678a7e9992adf27157907012286429f2c66df988d0f0bc0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDatastreamStreamDestinationConfigGcsDestinationConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamDestinationConfigGcsDestinationConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__47a5f5a8a9d9f19534aeab03cc71f662ec8150fb452e35333840e1fa4d19587e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAvroFileFormat")
    def put_avro_file_format(self) -> None:
        value = GoogleDatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormat()

        return typing.cast(None, jsii.invoke(self, "putAvroFileFormat", [value]))

    @jsii.member(jsii_name="putJsonFileFormat")
    def put_json_file_format(
        self,
        *,
        compression: typing.Optional[builtins.str] = None,
        schema_file_format: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param compression: Compression of the loaded JSON file. Possible values: ["NO_COMPRESSION", "GZIP"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#compression GoogleDatastreamStream#compression}
        :param schema_file_format: The schema file format along JSON data files. Possible values: ["NO_SCHEMA_FILE", "AVRO_SCHEMA_FILE"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#schema_file_format GoogleDatastreamStream#schema_file_format}
        '''
        value = GoogleDatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormat(
            compression=compression, schema_file_format=schema_file_format
        )

        return typing.cast(None, jsii.invoke(self, "putJsonFileFormat", [value]))

    @jsii.member(jsii_name="resetAvroFileFormat")
    def reset_avro_file_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAvroFileFormat", []))

    @jsii.member(jsii_name="resetFileRotationInterval")
    def reset_file_rotation_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFileRotationInterval", []))

    @jsii.member(jsii_name="resetFileRotationMb")
    def reset_file_rotation_mb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFileRotationMb", []))

    @jsii.member(jsii_name="resetJsonFileFormat")
    def reset_json_file_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJsonFileFormat", []))

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @builtins.property
    @jsii.member(jsii_name="avroFileFormat")
    def avro_file_format(
        self,
    ) -> GoogleDatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormatOutputReference:
        return typing.cast(GoogleDatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormatOutputReference, jsii.get(self, "avroFileFormat"))

    @builtins.property
    @jsii.member(jsii_name="jsonFileFormat")
    def json_file_format(
        self,
    ) -> GoogleDatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormatOutputReference:
        return typing.cast(GoogleDatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormatOutputReference, jsii.get(self, "jsonFileFormat"))

    @builtins.property
    @jsii.member(jsii_name="avroFileFormatInput")
    def avro_file_format_input(
        self,
    ) -> typing.Optional[GoogleDatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormat]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormat], jsii.get(self, "avroFileFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="fileRotationIntervalInput")
    def file_rotation_interval_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fileRotationIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="fileRotationMbInput")
    def file_rotation_mb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "fileRotationMbInput"))

    @builtins.property
    @jsii.member(jsii_name="jsonFileFormatInput")
    def json_file_format_input(
        self,
    ) -> typing.Optional[GoogleDatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormat]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormat], jsii.get(self, "jsonFileFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="fileRotationInterval")
    def file_rotation_interval(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fileRotationInterval"))

    @file_rotation_interval.setter
    def file_rotation_interval(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9074e840158c242a6584f690b9de8519093a095062560f763cb0081827756a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileRotationInterval", value)

    @builtins.property
    @jsii.member(jsii_name="fileRotationMb")
    def file_rotation_mb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "fileRotationMb"))

    @file_rotation_mb.setter
    def file_rotation_mb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d6fa5c42e1b054c724b34adb45f27353c6ae294899a9d8e80d90a167757cf2f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileRotationMb", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa2957bdccb90ef0e1d993d38c3afe8f4b14b633ee4a561bb96646544890cbd0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDatastreamStreamDestinationConfigGcsDestinationConfig]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamDestinationConfigGcsDestinationConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDatastreamStreamDestinationConfigGcsDestinationConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7c83b1266ba6a9af784fac1c33e0f366fe2d370e2f056e83a4d926ae455c27b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDatastreamStreamDestinationConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamDestinationConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a7c6a55cbd18393a53cb1933e95b4e468f4a520e2aad658c6da60f7b52de2f3b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putBigqueryDestinationConfig")
    def put_bigquery_destination_config(
        self,
        *,
        data_freshness: typing.Optional[builtins.str] = None,
        single_target_dataset: typing.Optional[typing.Union[GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDataset, typing.Dict[builtins.str, typing.Any]]] = None,
        source_hierarchy_datasets: typing.Optional[typing.Union[GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasets, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param data_freshness: The guaranteed data freshness (in seconds) when querying tables created by the stream. Editing this field will only affect new tables created in the future, but existing tables will not be impacted. Lower values mean that queries will return fresher data, but may result in higher cost. A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s". Defaults to 900s. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#data_freshness GoogleDatastreamStream#data_freshness}
        :param single_target_dataset: single_target_dataset block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#single_target_dataset GoogleDatastreamStream#single_target_dataset}
        :param source_hierarchy_datasets: source_hierarchy_datasets block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#source_hierarchy_datasets GoogleDatastreamStream#source_hierarchy_datasets}
        '''
        value = GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfig(
            data_freshness=data_freshness,
            single_target_dataset=single_target_dataset,
            source_hierarchy_datasets=source_hierarchy_datasets,
        )

        return typing.cast(None, jsii.invoke(self, "putBigqueryDestinationConfig", [value]))

    @jsii.member(jsii_name="putGcsDestinationConfig")
    def put_gcs_destination_config(
        self,
        *,
        avro_file_format: typing.Optional[typing.Union[GoogleDatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormat, typing.Dict[builtins.str, typing.Any]]] = None,
        file_rotation_interval: typing.Optional[builtins.str] = None,
        file_rotation_mb: typing.Optional[jsii.Number] = None,
        json_file_format: typing.Optional[typing.Union[GoogleDatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormat, typing.Dict[builtins.str, typing.Any]]] = None,
        path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param avro_file_format: avro_file_format block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#avro_file_format GoogleDatastreamStream#avro_file_format}
        :param file_rotation_interval: The maximum duration for which new events are added before a file is closed and a new file is created. A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s". Defaults to 900s. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#file_rotation_interval GoogleDatastreamStream#file_rotation_interval}
        :param file_rotation_mb: The maximum file size to be saved in the bucket. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#file_rotation_mb GoogleDatastreamStream#file_rotation_mb}
        :param json_file_format: json_file_format block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#json_file_format GoogleDatastreamStream#json_file_format}
        :param path: Path inside the Cloud Storage bucket to write data to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#path GoogleDatastreamStream#path}
        '''
        value = GoogleDatastreamStreamDestinationConfigGcsDestinationConfig(
            avro_file_format=avro_file_format,
            file_rotation_interval=file_rotation_interval,
            file_rotation_mb=file_rotation_mb,
            json_file_format=json_file_format,
            path=path,
        )

        return typing.cast(None, jsii.invoke(self, "putGcsDestinationConfig", [value]))

    @jsii.member(jsii_name="resetBigqueryDestinationConfig")
    def reset_bigquery_destination_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBigqueryDestinationConfig", []))

    @jsii.member(jsii_name="resetGcsDestinationConfig")
    def reset_gcs_destination_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGcsDestinationConfig", []))

    @builtins.property
    @jsii.member(jsii_name="bigqueryDestinationConfig")
    def bigquery_destination_config(
        self,
    ) -> GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigOutputReference:
        return typing.cast(GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigOutputReference, jsii.get(self, "bigqueryDestinationConfig"))

    @builtins.property
    @jsii.member(jsii_name="gcsDestinationConfig")
    def gcs_destination_config(
        self,
    ) -> GoogleDatastreamStreamDestinationConfigGcsDestinationConfigOutputReference:
        return typing.cast(GoogleDatastreamStreamDestinationConfigGcsDestinationConfigOutputReference, jsii.get(self, "gcsDestinationConfig"))

    @builtins.property
    @jsii.member(jsii_name="bigqueryDestinationConfigInput")
    def bigquery_destination_config_input(
        self,
    ) -> typing.Optional[GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfig]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfig], jsii.get(self, "bigqueryDestinationConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationConnectionProfileInput")
    def destination_connection_profile_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationConnectionProfileInput"))

    @builtins.property
    @jsii.member(jsii_name="gcsDestinationConfigInput")
    def gcs_destination_config_input(
        self,
    ) -> typing.Optional[GoogleDatastreamStreamDestinationConfigGcsDestinationConfig]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamDestinationConfigGcsDestinationConfig], jsii.get(self, "gcsDestinationConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationConnectionProfile")
    def destination_connection_profile(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destinationConnectionProfile"))

    @destination_connection_profile.setter
    def destination_connection_profile(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4017d208188843d4929bba3e8132e98451cac7713ab722eee13604f90c45b18b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationConnectionProfile", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDatastreamStreamDestinationConfig]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamDestinationConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDatastreamStreamDestinationConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9dcc83c10b6513136386af9d65f30bf2f699f914858eb91aaeeea5968e7dc3c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfig",
    jsii_struct_bases=[],
    name_mapping={
        "mysql_source_config": "mysqlSourceConfig",
        "source_connection_profile": "sourceConnectionProfile",
    },
)
class GoogleDatastreamStreamSourceConfig:
    def __init__(
        self,
        *,
        mysql_source_config: typing.Union["GoogleDatastreamStreamSourceConfigMysqlSourceConfig", typing.Dict[builtins.str, typing.Any]],
        source_connection_profile: builtins.str,
    ) -> None:
        '''
        :param mysql_source_config: mysql_source_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#mysql_source_config GoogleDatastreamStream#mysql_source_config}
        :param source_connection_profile: Source connection profile resource. Format: projects/{project}/locations/{location}/connectionProfiles/{name}. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#source_connection_profile GoogleDatastreamStream#source_connection_profile}
        '''
        if isinstance(mysql_source_config, dict):
            mysql_source_config = GoogleDatastreamStreamSourceConfigMysqlSourceConfig(**mysql_source_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2219a962a105c32324aa42c0ebabb89901efc5212a250e8d5cbf7c24fdf77d88)
            check_type(argname="argument mysql_source_config", value=mysql_source_config, expected_type=type_hints["mysql_source_config"])
            check_type(argname="argument source_connection_profile", value=source_connection_profile, expected_type=type_hints["source_connection_profile"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "mysql_source_config": mysql_source_config,
            "source_connection_profile": source_connection_profile,
        }

    @builtins.property
    def mysql_source_config(
        self,
    ) -> "GoogleDatastreamStreamSourceConfigMysqlSourceConfig":
        '''mysql_source_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#mysql_source_config GoogleDatastreamStream#mysql_source_config}
        '''
        result = self._values.get("mysql_source_config")
        assert result is not None, "Required property 'mysql_source_config' is missing"
        return typing.cast("GoogleDatastreamStreamSourceConfigMysqlSourceConfig", result)

    @builtins.property
    def source_connection_profile(self) -> builtins.str:
        '''Source connection profile resource. Format: projects/{project}/locations/{location}/connectionProfiles/{name}.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#source_connection_profile GoogleDatastreamStream#source_connection_profile}
        '''
        result = self._values.get("source_connection_profile")
        assert result is not None, "Required property 'source_connection_profile' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamSourceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigMysqlSourceConfig",
    jsii_struct_bases=[],
    name_mapping={
        "exclude_objects": "excludeObjects",
        "include_objects": "includeObjects",
        "max_concurrent_cdc_tasks": "maxConcurrentCdcTasks",
    },
)
class GoogleDatastreamStreamSourceConfigMysqlSourceConfig:
    def __init__(
        self,
        *,
        exclude_objects: typing.Optional[typing.Union["GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjects", typing.Dict[builtins.str, typing.Any]]] = None,
        include_objects: typing.Optional[typing.Union["GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjects", typing.Dict[builtins.str, typing.Any]]] = None,
        max_concurrent_cdc_tasks: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param exclude_objects: exclude_objects block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#exclude_objects GoogleDatastreamStream#exclude_objects}
        :param include_objects: include_objects block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#include_objects GoogleDatastreamStream#include_objects}
        :param max_concurrent_cdc_tasks: Maximum number of concurrent CDC tasks. The number should be non negative. If not set (or set to 0), the system's default value will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#max_concurrent_cdc_tasks GoogleDatastreamStream#max_concurrent_cdc_tasks}
        '''
        if isinstance(exclude_objects, dict):
            exclude_objects = GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjects(**exclude_objects)
        if isinstance(include_objects, dict):
            include_objects = GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjects(**include_objects)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4778bbd828e1594c449bc443537ebe755eb4c886943cdf45c60649a2abdad88)
            check_type(argname="argument exclude_objects", value=exclude_objects, expected_type=type_hints["exclude_objects"])
            check_type(argname="argument include_objects", value=include_objects, expected_type=type_hints["include_objects"])
            check_type(argname="argument max_concurrent_cdc_tasks", value=max_concurrent_cdc_tasks, expected_type=type_hints["max_concurrent_cdc_tasks"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if exclude_objects is not None:
            self._values["exclude_objects"] = exclude_objects
        if include_objects is not None:
            self._values["include_objects"] = include_objects
        if max_concurrent_cdc_tasks is not None:
            self._values["max_concurrent_cdc_tasks"] = max_concurrent_cdc_tasks

    @builtins.property
    def exclude_objects(
        self,
    ) -> typing.Optional["GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjects"]:
        '''exclude_objects block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#exclude_objects GoogleDatastreamStream#exclude_objects}
        '''
        result = self._values.get("exclude_objects")
        return typing.cast(typing.Optional["GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjects"], result)

    @builtins.property
    def include_objects(
        self,
    ) -> typing.Optional["GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjects"]:
        '''include_objects block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#include_objects GoogleDatastreamStream#include_objects}
        '''
        result = self._values.get("include_objects")
        return typing.cast(typing.Optional["GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjects"], result)

    @builtins.property
    def max_concurrent_cdc_tasks(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of concurrent CDC tasks.

        The number should be non negative.
        If not set (or set to 0), the system's default value will be used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#max_concurrent_cdc_tasks GoogleDatastreamStream#max_concurrent_cdc_tasks}
        '''
        result = self._values.get("max_concurrent_cdc_tasks")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamSourceConfigMysqlSourceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjects",
    jsii_struct_bases=[],
    name_mapping={"mysql_databases": "mysqlDatabases"},
)
class GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjects:
    def __init__(
        self,
        *,
        mysql_databases: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabases", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param mysql_databases: mysql_databases block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#mysql_databases GoogleDatastreamStream#mysql_databases}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d83157a8b7dabb6f6a578ba371ae7606ca73d8b886f676352d01e59c8b975065)
            check_type(argname="argument mysql_databases", value=mysql_databases, expected_type=type_hints["mysql_databases"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "mysql_databases": mysql_databases,
        }

    @builtins.property
    def mysql_databases(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabases"]]:
        '''mysql_databases block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#mysql_databases GoogleDatastreamStream#mysql_databases}
        '''
        result = self._values.get("mysql_databases")
        assert result is not None, "Required property 'mysql_databases' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabases"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjects(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabases",
    jsii_struct_bases=[],
    name_mapping={"database": "database", "mysql_tables": "mysqlTables"},
)
class GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabases:
    def __init__(
        self,
        *,
        database: builtins.str,
        mysql_tables: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTables", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param database: Database name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#database GoogleDatastreamStream#database}
        :param mysql_tables: mysql_tables block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#mysql_tables GoogleDatastreamStream#mysql_tables}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb545565a9647ff9db741b384db4f82c54b58032c7b2d4e18818cd7d16eeeb69)
            check_type(argname="argument database", value=database, expected_type=type_hints["database"])
            check_type(argname="argument mysql_tables", value=mysql_tables, expected_type=type_hints["mysql_tables"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "database": database,
        }
        if mysql_tables is not None:
            self._values["mysql_tables"] = mysql_tables

    @builtins.property
    def database(self) -> builtins.str:
        '''Database name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#database GoogleDatastreamStream#database}
        '''
        result = self._values.get("database")
        assert result is not None, "Required property 'database' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def mysql_tables(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTables"]]]:
        '''mysql_tables block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#mysql_tables GoogleDatastreamStream#mysql_tables}
        '''
        result = self._values.get("mysql_tables")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTables"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabases(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e2e56eed75c4420627cc1b1ea20e73bc1bbede9df3a2fd8199d4497aa838d16d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a1012ecc8549b81e5e4aa9d9923e204f999b9b29fd4483cafcd96ee9d37e92a)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__749cad1c5353daa5443baca3acaaa68fdf3ee0496883fec1e0a8e7bf6e478f43)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2ed34b487f8807df8a3089ff0bf45f39c9f22d366421e027795a5d5ff3b031d3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__47fc60e67695921f46d329ab49e84fb7a745d5f9e52ef95fd339c406ed1f5337)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabases]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabases]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabases]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6580eacf3a0fa9ef788be946237924b568d6c34ca0ce2997d700ceb0ec5909e2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTables",
    jsii_struct_bases=[],
    name_mapping={"table": "table", "mysql_columns": "mysqlColumns"},
)
class GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTables:
    def __init__(
        self,
        *,
        table: builtins.str,
        mysql_columns: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumns", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param table: Table name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#table GoogleDatastreamStream#table}
        :param mysql_columns: mysql_columns block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#mysql_columns GoogleDatastreamStream#mysql_columns}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8fd22251a137acbd8b6d4011e790c862bba2bc6baff5731831f4aaeb1f09bc8e)
            check_type(argname="argument table", value=table, expected_type=type_hints["table"])
            check_type(argname="argument mysql_columns", value=mysql_columns, expected_type=type_hints["mysql_columns"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "table": table,
        }
        if mysql_columns is not None:
            self._values["mysql_columns"] = mysql_columns

    @builtins.property
    def table(self) -> builtins.str:
        '''Table name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#table GoogleDatastreamStream#table}
        '''
        result = self._values.get("table")
        assert result is not None, "Required property 'table' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def mysql_columns(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumns"]]]:
        '''mysql_columns block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#mysql_columns GoogleDatastreamStream#mysql_columns}
        '''
        result = self._values.get("mysql_columns")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumns"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTables(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fb19d59bcaf47d9126f742045b4d73f2d47c6d705e98fc433966bc88d02bd5ea)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc62e64aa47cf54d533fff2c0ef281c96989464e75c918ffb64f1d14c9d9e79d)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09ac2c33a67547e5fc09ad6eab15b4937398704f7e0dccd16e467818f83a6edd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__78f38e38e105221d16e5180f0a1d2c8909391494a32349303610ab95030c9c8c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d20ad137b3b082c078fd7a5bc38642356759a7fc420d24b61cf649a1f7ed1ad8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTables]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTables]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTables]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__244522fde9aceac31a2e149744987ae023545406b794b7618a16cb61f5434d3a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumns",
    jsii_struct_bases=[],
    name_mapping={
        "collation": "collation",
        "column": "column",
        "data_type": "dataType",
        "nullable": "nullable",
        "ordinal_position": "ordinalPosition",
        "primary_key": "primaryKey",
    },
)
class GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumns:
    def __init__(
        self,
        *,
        collation: typing.Optional[builtins.str] = None,
        column: typing.Optional[builtins.str] = None,
        data_type: typing.Optional[builtins.str] = None,
        nullable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        ordinal_position: typing.Optional[jsii.Number] = None,
        primary_key: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param collation: Column collation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#collation GoogleDatastreamStream#collation}
        :param column: Column name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#column GoogleDatastreamStream#column}
        :param data_type: The MySQL data type. Full data types list can be found here: https://dev.mysql.com/doc/refman/8.0/en/data-types.html. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#data_type GoogleDatastreamStream#data_type}
        :param nullable: Whether or not the column can accept a null value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#nullable GoogleDatastreamStream#nullable}
        :param ordinal_position: The ordinal position of the column in the table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#ordinal_position GoogleDatastreamStream#ordinal_position}
        :param primary_key: Whether or not the column represents a primary key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#primary_key GoogleDatastreamStream#primary_key}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1fe080b67925fa358036b8642a0299bcbe1d9e7f96a77e04e3df091ce8d56d79)
            check_type(argname="argument collation", value=collation, expected_type=type_hints["collation"])
            check_type(argname="argument column", value=column, expected_type=type_hints["column"])
            check_type(argname="argument data_type", value=data_type, expected_type=type_hints["data_type"])
            check_type(argname="argument nullable", value=nullable, expected_type=type_hints["nullable"])
            check_type(argname="argument ordinal_position", value=ordinal_position, expected_type=type_hints["ordinal_position"])
            check_type(argname="argument primary_key", value=primary_key, expected_type=type_hints["primary_key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if collation is not None:
            self._values["collation"] = collation
        if column is not None:
            self._values["column"] = column
        if data_type is not None:
            self._values["data_type"] = data_type
        if nullable is not None:
            self._values["nullable"] = nullable
        if ordinal_position is not None:
            self._values["ordinal_position"] = ordinal_position
        if primary_key is not None:
            self._values["primary_key"] = primary_key

    @builtins.property
    def collation(self) -> typing.Optional[builtins.str]:
        '''Column collation.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#collation GoogleDatastreamStream#collation}
        '''
        result = self._values.get("collation")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def column(self) -> typing.Optional[builtins.str]:
        '''Column name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#column GoogleDatastreamStream#column}
        '''
        result = self._values.get("column")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_type(self) -> typing.Optional[builtins.str]:
        '''The MySQL data type. Full data types list can be found here: https://dev.mysql.com/doc/refman/8.0/en/data-types.html.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#data_type GoogleDatastreamStream#data_type}
        '''
        result = self._values.get("data_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def nullable(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether or not the column can accept a null value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#nullable GoogleDatastreamStream#nullable}
        '''
        result = self._values.get("nullable")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def ordinal_position(self) -> typing.Optional[jsii.Number]:
        '''The ordinal position of the column in the table.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#ordinal_position GoogleDatastreamStream#ordinal_position}
        '''
        result = self._values.get("ordinal_position")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def primary_key(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether or not the column represents a primary key.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#primary_key GoogleDatastreamStream#primary_key}
        '''
        result = self._values.get("primary_key")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumns(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumnsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumnsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__201e84943daf6e96eef782d9aca244517f562921989a0d02638fa0c6272b71f8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumnsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa8e8e1d140504fda11f4c3773ed96c2555f2d0a8e4e54dd2649412cdce8913b)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumnsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09f48286efb01f277d2532514c20596f929b4f09bdd712cce896d54029581845)
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
            type_hints = typing.get_type_hints(_typecheckingstub__412ca5ab78995949f165cc648a1345246edeca119614f829c8466a957611327d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e8513a9f97f6e8b890e45ed0436f080d3b24af266ac66156a0234692ec528671)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumns]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumns]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumns]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d52d72230d6b4de322b1c93887aea771351503b11807485568c93d0e395bad14)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumnsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumnsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cea7b45fb19736020b1719a17d6aec42bd6508059c9e7f8abc1ab4eff5bcf48b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCollation")
    def reset_collation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCollation", []))

    @jsii.member(jsii_name="resetColumn")
    def reset_column(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetColumn", []))

    @jsii.member(jsii_name="resetDataType")
    def reset_data_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataType", []))

    @jsii.member(jsii_name="resetNullable")
    def reset_nullable(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNullable", []))

    @jsii.member(jsii_name="resetOrdinalPosition")
    def reset_ordinal_position(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrdinalPosition", []))

    @jsii.member(jsii_name="resetPrimaryKey")
    def reset_primary_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrimaryKey", []))

    @builtins.property
    @jsii.member(jsii_name="length")
    def length(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "length"))

    @builtins.property
    @jsii.member(jsii_name="collationInput")
    def collation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "collationInput"))

    @builtins.property
    @jsii.member(jsii_name="columnInput")
    def column_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "columnInput"))

    @builtins.property
    @jsii.member(jsii_name="dataTypeInput")
    def data_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="nullableInput")
    def nullable_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "nullableInput"))

    @builtins.property
    @jsii.member(jsii_name="ordinalPositionInput")
    def ordinal_position_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ordinalPositionInput"))

    @builtins.property
    @jsii.member(jsii_name="primaryKeyInput")
    def primary_key_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "primaryKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="collation")
    def collation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "collation"))

    @collation.setter
    def collation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77e9ee7094ccb2bbda850d8033cde908a302188b4966ed9026a0addd79294f25)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "collation", value)

    @builtins.property
    @jsii.member(jsii_name="column")
    def column(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "column"))

    @column.setter
    def column(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3769df6b39afdb7b53797c325a30a0a86634ec6359d219686195fabb6bc4ade)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "column", value)

    @builtins.property
    @jsii.member(jsii_name="dataType")
    def data_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataType"))

    @data_type.setter
    def data_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95e94c186c0638d6e197288bd999f087d07a4e38f94a0c930fded96c19b30a06)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataType", value)

    @builtins.property
    @jsii.member(jsii_name="nullable")
    def nullable(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "nullable"))

    @nullable.setter
    def nullable(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57c29013747c1114bb244cb6f55298a74d6c22ed57f735b6c3fcf456523e93bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nullable", value)

    @builtins.property
    @jsii.member(jsii_name="ordinalPosition")
    def ordinal_position(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ordinalPosition"))

    @ordinal_position.setter
    def ordinal_position(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8083b61ac53f7e64f6d293d8795f8cfcb1af5dcc4641991d8c21d7d14d6a090)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ordinalPosition", value)

    @builtins.property
    @jsii.member(jsii_name="primaryKey")
    def primary_key(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "primaryKey"))

    @primary_key.setter
    def primary_key(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4ce157d33b04ca603a11a14e186e508173db15b13bca2edab6f487ed885c277)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "primaryKey", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumns, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumns, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumns, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a14532a7d8ee26125f14790252a94be3a764732ba59c7e09374d740bd35cb0a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e9ad39a49db2deb62da532182c908182089fb53ff855492f00ca108bfb38702e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putMysqlColumns")
    def put_mysql_columns(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumns, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6805013dab1076ffb632b34e127ba4a5b8181fe496c7c0083216d785c6f51a6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMysqlColumns", [value]))

    @jsii.member(jsii_name="resetMysqlColumns")
    def reset_mysql_columns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMysqlColumns", []))

    @builtins.property
    @jsii.member(jsii_name="mysqlColumns")
    def mysql_columns(
        self,
    ) -> GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumnsList:
        return typing.cast(GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumnsList, jsii.get(self, "mysqlColumns"))

    @builtins.property
    @jsii.member(jsii_name="mysqlColumnsInput")
    def mysql_columns_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumns]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumns]]], jsii.get(self, "mysqlColumnsInput"))

    @builtins.property
    @jsii.member(jsii_name="tableInput")
    def table_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableInput"))

    @builtins.property
    @jsii.member(jsii_name="table")
    def table(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "table"))

    @table.setter
    def table(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f635e21d9372998fc0be54b333ef130ee85a23b090304aa7d38db1c57f56b6df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "table", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTables, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTables, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTables, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bcc850b4e3cb4779e1466342590aca58d03c507861a481a9b9fd924abaa00461)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ba70a81582b78786b580f56388706a6188061700c80a5ac1049d58ea4ceda106)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putMysqlTables")
    def put_mysql_tables(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTables, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25736e01b271cf2c953cc3fe6752d0c6af2a0cefb5fdadb58a006ce4cd317ca1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMysqlTables", [value]))

    @jsii.member(jsii_name="resetMysqlTables")
    def reset_mysql_tables(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMysqlTables", []))

    @builtins.property
    @jsii.member(jsii_name="mysqlTables")
    def mysql_tables(
        self,
    ) -> GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesList:
        return typing.cast(GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesList, jsii.get(self, "mysqlTables"))

    @builtins.property
    @jsii.member(jsii_name="databaseInput")
    def database_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseInput"))

    @builtins.property
    @jsii.member(jsii_name="mysqlTablesInput")
    def mysql_tables_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTables]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTables]]], jsii.get(self, "mysqlTablesInput"))

    @builtins.property
    @jsii.member(jsii_name="database")
    def database(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "database"))

    @database.setter
    def database(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c255dc0ac974e3e989e48a72c5479f88eb080a9286525bb3f1310e4e41d29747)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "database", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabases, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabases, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabases, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78514113923d93d64011f19fc8e7df61bc8b692c1ca133f55e2039d7a76a635d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1c84a482c246e68a2697c2dbe687609ff014a57db45d072800f00517f2aa6a56)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMysqlDatabases")
    def put_mysql_databases(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabases, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__084ed61c2edc5493618eaa16135dff2755b5c72b0b42e1db898c18b18dc6f41f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMysqlDatabases", [value]))

    @builtins.property
    @jsii.member(jsii_name="mysqlDatabases")
    def mysql_databases(
        self,
    ) -> GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesList:
        return typing.cast(GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesList, jsii.get(self, "mysqlDatabases"))

    @builtins.property
    @jsii.member(jsii_name="mysqlDatabasesInput")
    def mysql_databases_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabases]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabases]]], jsii.get(self, "mysqlDatabasesInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjects]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjects], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjects],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e809bf11601f9faeac3e63217a488b72d3894ca5740326dce20994d858714f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjects",
    jsii_struct_bases=[],
    name_mapping={"mysql_databases": "mysqlDatabases"},
)
class GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjects:
    def __init__(
        self,
        *,
        mysql_databases: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabases", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param mysql_databases: mysql_databases block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#mysql_databases GoogleDatastreamStream#mysql_databases}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b782ad37d159e6fc26ccecf102c72c7754e16dda5dfcd19b2bc64b597b89e07)
            check_type(argname="argument mysql_databases", value=mysql_databases, expected_type=type_hints["mysql_databases"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "mysql_databases": mysql_databases,
        }

    @builtins.property
    def mysql_databases(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabases"]]:
        '''mysql_databases block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#mysql_databases GoogleDatastreamStream#mysql_databases}
        '''
        result = self._values.get("mysql_databases")
        assert result is not None, "Required property 'mysql_databases' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabases"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjects(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabases",
    jsii_struct_bases=[],
    name_mapping={"database": "database", "mysql_tables": "mysqlTables"},
)
class GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabases:
    def __init__(
        self,
        *,
        database: builtins.str,
        mysql_tables: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTables", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param database: Database name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#database GoogleDatastreamStream#database}
        :param mysql_tables: mysql_tables block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#mysql_tables GoogleDatastreamStream#mysql_tables}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f44f39ebafbebf8e628605efe61a5348b73f5c5884eb1c28dde453f8bf8523a5)
            check_type(argname="argument database", value=database, expected_type=type_hints["database"])
            check_type(argname="argument mysql_tables", value=mysql_tables, expected_type=type_hints["mysql_tables"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "database": database,
        }
        if mysql_tables is not None:
            self._values["mysql_tables"] = mysql_tables

    @builtins.property
    def database(self) -> builtins.str:
        '''Database name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#database GoogleDatastreamStream#database}
        '''
        result = self._values.get("database")
        assert result is not None, "Required property 'database' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def mysql_tables(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTables"]]]:
        '''mysql_tables block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#mysql_tables GoogleDatastreamStream#mysql_tables}
        '''
        result = self._values.get("mysql_tables")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTables"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabases(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c3950f8fb1b59cab5c5f81358a344ffbf164f405bda8837307b833c993cc758d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90939e89008258e8e5fb13b17b64dcac780a64cb8cbe81abc7341daf57a122e8)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__217aa69718caac050d609fc9d8ce57f8bb611e4fa934e6be20a0b57f11f7a1ee)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c7dc49121ffff0463e398d82b102cb8ff336eb3cbcd5683e60e9dd1109e48f61)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a7ba15a2cd54a82cbc63ae4621ab87db797cd62dcd7ed63ba155e2de063b189e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabases]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabases]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabases]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d004f44683df7b5074728264cf889cbf037304edfcd3f994117693183d9f5db)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTables",
    jsii_struct_bases=[],
    name_mapping={"table": "table", "mysql_columns": "mysqlColumns"},
)
class GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTables:
    def __init__(
        self,
        *,
        table: builtins.str,
        mysql_columns: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumns", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param table: Table name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#table GoogleDatastreamStream#table}
        :param mysql_columns: mysql_columns block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#mysql_columns GoogleDatastreamStream#mysql_columns}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa194010af037f05469911f39778136fc3ed69ba254253f1224c1a9bbe628999)
            check_type(argname="argument table", value=table, expected_type=type_hints["table"])
            check_type(argname="argument mysql_columns", value=mysql_columns, expected_type=type_hints["mysql_columns"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "table": table,
        }
        if mysql_columns is not None:
            self._values["mysql_columns"] = mysql_columns

    @builtins.property
    def table(self) -> builtins.str:
        '''Table name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#table GoogleDatastreamStream#table}
        '''
        result = self._values.get("table")
        assert result is not None, "Required property 'table' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def mysql_columns(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumns"]]]:
        '''mysql_columns block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#mysql_columns GoogleDatastreamStream#mysql_columns}
        '''
        result = self._values.get("mysql_columns")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumns"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTables(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__dcb77d2e3fb3b195efed0d69e822264d59c5fbf7c1b4cee8e8964364dc9c2123)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba2fe890e741e0c6b63029866f84e111f3cd478bbf199d640a82d12c574d7aa7)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1c7b2e8a8945bd904b6786cb2b4d1aea6874c1ee6838435ab9323baa835b2e0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e69a309bddb1478976b492ae7fb3fd3f17336bc920c0b40e545744ada6341c29)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2671e1f1942c6cb0e3c3ba36f58e950eb50a102df253a43e899c96a138842ff7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTables]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTables]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTables]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8af2eb875cdae7d71d393ba6e098c6da4c3110914133b1dd079c070354a7a205)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumns",
    jsii_struct_bases=[],
    name_mapping={
        "collation": "collation",
        "column": "column",
        "data_type": "dataType",
        "nullable": "nullable",
        "ordinal_position": "ordinalPosition",
        "primary_key": "primaryKey",
    },
)
class GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumns:
    def __init__(
        self,
        *,
        collation: typing.Optional[builtins.str] = None,
        column: typing.Optional[builtins.str] = None,
        data_type: typing.Optional[builtins.str] = None,
        nullable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        ordinal_position: typing.Optional[jsii.Number] = None,
        primary_key: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param collation: Column collation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#collation GoogleDatastreamStream#collation}
        :param column: Column name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#column GoogleDatastreamStream#column}
        :param data_type: The MySQL data type. Full data types list can be found here: https://dev.mysql.com/doc/refman/8.0/en/data-types.html. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#data_type GoogleDatastreamStream#data_type}
        :param nullable: Whether or not the column can accept a null value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#nullable GoogleDatastreamStream#nullable}
        :param ordinal_position: The ordinal position of the column in the table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#ordinal_position GoogleDatastreamStream#ordinal_position}
        :param primary_key: Whether or not the column represents a primary key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#primary_key GoogleDatastreamStream#primary_key}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41215ce0b14ba24427640cc4700269ad49a0faadf8295e7ac03b7f47f2b37132)
            check_type(argname="argument collation", value=collation, expected_type=type_hints["collation"])
            check_type(argname="argument column", value=column, expected_type=type_hints["column"])
            check_type(argname="argument data_type", value=data_type, expected_type=type_hints["data_type"])
            check_type(argname="argument nullable", value=nullable, expected_type=type_hints["nullable"])
            check_type(argname="argument ordinal_position", value=ordinal_position, expected_type=type_hints["ordinal_position"])
            check_type(argname="argument primary_key", value=primary_key, expected_type=type_hints["primary_key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if collation is not None:
            self._values["collation"] = collation
        if column is not None:
            self._values["column"] = column
        if data_type is not None:
            self._values["data_type"] = data_type
        if nullable is not None:
            self._values["nullable"] = nullable
        if ordinal_position is not None:
            self._values["ordinal_position"] = ordinal_position
        if primary_key is not None:
            self._values["primary_key"] = primary_key

    @builtins.property
    def collation(self) -> typing.Optional[builtins.str]:
        '''Column collation.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#collation GoogleDatastreamStream#collation}
        '''
        result = self._values.get("collation")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def column(self) -> typing.Optional[builtins.str]:
        '''Column name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#column GoogleDatastreamStream#column}
        '''
        result = self._values.get("column")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_type(self) -> typing.Optional[builtins.str]:
        '''The MySQL data type. Full data types list can be found here: https://dev.mysql.com/doc/refman/8.0/en/data-types.html.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#data_type GoogleDatastreamStream#data_type}
        '''
        result = self._values.get("data_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def nullable(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether or not the column can accept a null value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#nullable GoogleDatastreamStream#nullable}
        '''
        result = self._values.get("nullable")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def ordinal_position(self) -> typing.Optional[jsii.Number]:
        '''The ordinal position of the column in the table.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#ordinal_position GoogleDatastreamStream#ordinal_position}
        '''
        result = self._values.get("ordinal_position")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def primary_key(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether or not the column represents a primary key.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#primary_key GoogleDatastreamStream#primary_key}
        '''
        result = self._values.get("primary_key")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumns(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumnsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumnsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6861e4975493055a6649272b537f648980427a9301bfb234da05242b7f0c49ec)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumnsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9427d6862c644b6d507a55730df9f5fdf5c926418390d5de45f4e2f3f5ee9f5e)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumnsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69adb63c3ab9af12da7590f7aae32e0a5104845d11c1ddd67b18b08745828402)
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
            type_hints = typing.get_type_hints(_typecheckingstub__60e663fc168673b4aa74cd1ee2009d59cd03ee3b03440bc1bae19ab2dffb2cdf)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b58a7d494136d2ac7db279ee2b91810061fadc45f6d73f86e92229382749f59a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumns]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumns]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumns]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7fad90c17f32bc7ae1fccc7cb1431033ed4c2ce630fffd4d769c94decdd59083)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumnsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumnsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__65b3ccfaf3bad8ab5e06b93c91c603524b0f7f199e7256dfbce872b77ccc667a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCollation")
    def reset_collation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCollation", []))

    @jsii.member(jsii_name="resetColumn")
    def reset_column(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetColumn", []))

    @jsii.member(jsii_name="resetDataType")
    def reset_data_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataType", []))

    @jsii.member(jsii_name="resetNullable")
    def reset_nullable(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNullable", []))

    @jsii.member(jsii_name="resetOrdinalPosition")
    def reset_ordinal_position(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrdinalPosition", []))

    @jsii.member(jsii_name="resetPrimaryKey")
    def reset_primary_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrimaryKey", []))

    @builtins.property
    @jsii.member(jsii_name="length")
    def length(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "length"))

    @builtins.property
    @jsii.member(jsii_name="collationInput")
    def collation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "collationInput"))

    @builtins.property
    @jsii.member(jsii_name="columnInput")
    def column_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "columnInput"))

    @builtins.property
    @jsii.member(jsii_name="dataTypeInput")
    def data_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="nullableInput")
    def nullable_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "nullableInput"))

    @builtins.property
    @jsii.member(jsii_name="ordinalPositionInput")
    def ordinal_position_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ordinalPositionInput"))

    @builtins.property
    @jsii.member(jsii_name="primaryKeyInput")
    def primary_key_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "primaryKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="collation")
    def collation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "collation"))

    @collation.setter
    def collation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68e45a2b6f0d78f15e06a1e14dbc279680b842b3d346da672fb3da0ba499caa5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "collation", value)

    @builtins.property
    @jsii.member(jsii_name="column")
    def column(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "column"))

    @column.setter
    def column(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a954aaaf4ecbb61bdb80680a5308a4650ff1f930fdff1565938a80865567e4b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "column", value)

    @builtins.property
    @jsii.member(jsii_name="dataType")
    def data_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataType"))

    @data_type.setter
    def data_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8bfd73c16927e583d02f4ece4c98e6e285936610b6ea37d64cb9c6731b30c6e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataType", value)

    @builtins.property
    @jsii.member(jsii_name="nullable")
    def nullable(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "nullable"))

    @nullable.setter
    def nullable(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c58d677fcfdede4d959a221ab875d5089fa903aa656d2b774755c9e2be2e790)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nullable", value)

    @builtins.property
    @jsii.member(jsii_name="ordinalPosition")
    def ordinal_position(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ordinalPosition"))

    @ordinal_position.setter
    def ordinal_position(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c454d64cfc5be1fab8c89b6180a07485a1e3934e24523bc92f3900e58a45b43b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ordinalPosition", value)

    @builtins.property
    @jsii.member(jsii_name="primaryKey")
    def primary_key(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "primaryKey"))

    @primary_key.setter
    def primary_key(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__990ed112f00ba5b2fd44cdebb437b9c639030938839325738ece2803bbbee1f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "primaryKey", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumns, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumns, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumns, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac1001f24a95b45f13518456c95010ca63139d5bf238d99bcc2e6386f283bc2d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a6b4a00ce373e23cd5b51bfba3c664c9f9a51885d2951423d35c58dea7aa5613)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putMysqlColumns")
    def put_mysql_columns(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumns, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c9a1375628b7f6b29a695647f3434428d773a775a513a4c340d0cf934ac7d32)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMysqlColumns", [value]))

    @jsii.member(jsii_name="resetMysqlColumns")
    def reset_mysql_columns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMysqlColumns", []))

    @builtins.property
    @jsii.member(jsii_name="mysqlColumns")
    def mysql_columns(
        self,
    ) -> GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumnsList:
        return typing.cast(GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumnsList, jsii.get(self, "mysqlColumns"))

    @builtins.property
    @jsii.member(jsii_name="mysqlColumnsInput")
    def mysql_columns_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumns]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumns]]], jsii.get(self, "mysqlColumnsInput"))

    @builtins.property
    @jsii.member(jsii_name="tableInput")
    def table_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableInput"))

    @builtins.property
    @jsii.member(jsii_name="table")
    def table(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "table"))

    @table.setter
    def table(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__629184c09083c28c9f035a8074dcd1f16f0a61d948bc2393377da3130506e2f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "table", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTables, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTables, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTables, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__759a721a0536fba67735d0dd4283007387dadc2eb076cdb2d65fda1402b5e5f6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e8548900250b3351b1c6d41c39a3f7fc3652815a7c6184c8c707341c35763ac3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putMysqlTables")
    def put_mysql_tables(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTables, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b269534d2b5371b90449e0d4dd96df396fbca76931cb7a5f54a30f1b654543d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMysqlTables", [value]))

    @jsii.member(jsii_name="resetMysqlTables")
    def reset_mysql_tables(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMysqlTables", []))

    @builtins.property
    @jsii.member(jsii_name="mysqlTables")
    def mysql_tables(
        self,
    ) -> GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesList:
        return typing.cast(GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesList, jsii.get(self, "mysqlTables"))

    @builtins.property
    @jsii.member(jsii_name="databaseInput")
    def database_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseInput"))

    @builtins.property
    @jsii.member(jsii_name="mysqlTablesInput")
    def mysql_tables_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTables]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTables]]], jsii.get(self, "mysqlTablesInput"))

    @builtins.property
    @jsii.member(jsii_name="database")
    def database(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "database"))

    @database.setter
    def database(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0dc2394f1204551f9f707dbf0479faf9458fafc6a03c129b132c5e409293bb9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "database", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabases, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabases, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabases, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32b6f477c199b7d70e86e7f6dec51b8b579ebe58c787a257fcb73e04d3cc5bcf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4b401a73888aa3eedea89455bd1d7e18731ee7412824c21d4be2f36a727cd8a7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMysqlDatabases")
    def put_mysql_databases(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabases, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__613d8a98ff90be15005996fdfac043d333f8645c71d52edfc24b79e3b6031649)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMysqlDatabases", [value]))

    @builtins.property
    @jsii.member(jsii_name="mysqlDatabases")
    def mysql_databases(
        self,
    ) -> GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesList:
        return typing.cast(GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesList, jsii.get(self, "mysqlDatabases"))

    @builtins.property
    @jsii.member(jsii_name="mysqlDatabasesInput")
    def mysql_databases_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabases]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabases]]], jsii.get(self, "mysqlDatabasesInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjects]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjects], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjects],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc63fda8e348ad1f4425fc05aec528be1a2b9aabab914770a3fb1f72c46604b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDatastreamStreamSourceConfigMysqlSourceConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigMysqlSourceConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__efb86a24b39d875af0044075b654f055d4cf52279a7e2097cdcb5b797e5ff174)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putExcludeObjects")
    def put_exclude_objects(
        self,
        *,
        mysql_databases: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabases, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param mysql_databases: mysql_databases block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#mysql_databases GoogleDatastreamStream#mysql_databases}
        '''
        value = GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjects(
            mysql_databases=mysql_databases
        )

        return typing.cast(None, jsii.invoke(self, "putExcludeObjects", [value]))

    @jsii.member(jsii_name="putIncludeObjects")
    def put_include_objects(
        self,
        *,
        mysql_databases: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabases, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param mysql_databases: mysql_databases block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#mysql_databases GoogleDatastreamStream#mysql_databases}
        '''
        value = GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjects(
            mysql_databases=mysql_databases
        )

        return typing.cast(None, jsii.invoke(self, "putIncludeObjects", [value]))

    @jsii.member(jsii_name="resetExcludeObjects")
    def reset_exclude_objects(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExcludeObjects", []))

    @jsii.member(jsii_name="resetIncludeObjects")
    def reset_include_objects(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeObjects", []))

    @jsii.member(jsii_name="resetMaxConcurrentCdcTasks")
    def reset_max_concurrent_cdc_tasks(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxConcurrentCdcTasks", []))

    @builtins.property
    @jsii.member(jsii_name="excludeObjects")
    def exclude_objects(
        self,
    ) -> GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsOutputReference:
        return typing.cast(GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsOutputReference, jsii.get(self, "excludeObjects"))

    @builtins.property
    @jsii.member(jsii_name="includeObjects")
    def include_objects(
        self,
    ) -> GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsOutputReference:
        return typing.cast(GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsOutputReference, jsii.get(self, "includeObjects"))

    @builtins.property
    @jsii.member(jsii_name="excludeObjectsInput")
    def exclude_objects_input(
        self,
    ) -> typing.Optional[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjects]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjects], jsii.get(self, "excludeObjectsInput"))

    @builtins.property
    @jsii.member(jsii_name="includeObjectsInput")
    def include_objects_input(
        self,
    ) -> typing.Optional[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjects]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjects], jsii.get(self, "includeObjectsInput"))

    @builtins.property
    @jsii.member(jsii_name="maxConcurrentCdcTasksInput")
    def max_concurrent_cdc_tasks_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxConcurrentCdcTasksInput"))

    @builtins.property
    @jsii.member(jsii_name="maxConcurrentCdcTasks")
    def max_concurrent_cdc_tasks(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxConcurrentCdcTasks"))

    @max_concurrent_cdc_tasks.setter
    def max_concurrent_cdc_tasks(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75042a2bfae52ebd1b965d7005d120750faa2993f31c1eeb04500e45bd87a769)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxConcurrentCdcTasks", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDatastreamStreamSourceConfigMysqlSourceConfig]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamSourceConfigMysqlSourceConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDatastreamStreamSourceConfigMysqlSourceConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5301d37e1a77c15dc3423d2d6672f672b5059dd74d24e85d8326831c85d9c317)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDatastreamStreamSourceConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamSourceConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__935aa7233aaac0fbc524f35d41c8b42f4f855c3d54fd43f35f0e7b9d7528b61d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMysqlSourceConfig")
    def put_mysql_source_config(
        self,
        *,
        exclude_objects: typing.Optional[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjects, typing.Dict[builtins.str, typing.Any]]] = None,
        include_objects: typing.Optional[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjects, typing.Dict[builtins.str, typing.Any]]] = None,
        max_concurrent_cdc_tasks: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param exclude_objects: exclude_objects block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#exclude_objects GoogleDatastreamStream#exclude_objects}
        :param include_objects: include_objects block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#include_objects GoogleDatastreamStream#include_objects}
        :param max_concurrent_cdc_tasks: Maximum number of concurrent CDC tasks. The number should be non negative. If not set (or set to 0), the system's default value will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#max_concurrent_cdc_tasks GoogleDatastreamStream#max_concurrent_cdc_tasks}
        '''
        value = GoogleDatastreamStreamSourceConfigMysqlSourceConfig(
            exclude_objects=exclude_objects,
            include_objects=include_objects,
            max_concurrent_cdc_tasks=max_concurrent_cdc_tasks,
        )

        return typing.cast(None, jsii.invoke(self, "putMysqlSourceConfig", [value]))

    @builtins.property
    @jsii.member(jsii_name="mysqlSourceConfig")
    def mysql_source_config(
        self,
    ) -> GoogleDatastreamStreamSourceConfigMysqlSourceConfigOutputReference:
        return typing.cast(GoogleDatastreamStreamSourceConfigMysqlSourceConfigOutputReference, jsii.get(self, "mysqlSourceConfig"))

    @builtins.property
    @jsii.member(jsii_name="mysqlSourceConfigInput")
    def mysql_source_config_input(
        self,
    ) -> typing.Optional[GoogleDatastreamStreamSourceConfigMysqlSourceConfig]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamSourceConfigMysqlSourceConfig], jsii.get(self, "mysqlSourceConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceConnectionProfileInput")
    def source_connection_profile_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceConnectionProfileInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceConnectionProfile")
    def source_connection_profile(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceConnectionProfile"))

    @source_connection_profile.setter
    def source_connection_profile(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad6aaf1380cfd2cad252287f4082eac6cb898c810899506186dbc4bf8daf22af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceConnectionProfile", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleDatastreamStreamSourceConfig]:
        return typing.cast(typing.Optional[GoogleDatastreamStreamSourceConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDatastreamStreamSourceConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d31a3dae34b03d71885cecf9357ff558547f3eba368913731781633806d28251)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleDatastreamStreamTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#create GoogleDatastreamStream#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#delete GoogleDatastreamStream#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#update GoogleDatastreamStream#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a54b49f7561784b6ddbf39b45bfd0f91cd4d531a183f057a0f51c1fb036c6ee4)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#create GoogleDatastreamStream#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#delete GoogleDatastreamStream#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_datastream_stream#update GoogleDatastreamStream#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDatastreamStreamTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDatastreamStreamTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDatastreamStream.GoogleDatastreamStreamTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5a1e593819993f0b26e94eb2825132a675053b005efe8ffb05266fd2c2530166)
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
            type_hints = typing.get_type_hints(_typecheckingstub__72ae4642fb1a34ac292bc77f8755496644a696b2005d238ad3d096cf94340334)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f50f1677bf065b391c40444994d038f923d9d5c282b68e34cbff128a610e0e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27df4af47c20495c8bd3cfc96cc0d9e42b03499ba5a08622470954ed4ff13101)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleDatastreamStreamTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleDatastreamStreamTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleDatastreamStreamTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9644ba1934244050f95ca839e3c9e108ad0d0d1156a6d8051eae93e46bb4269a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleDatastreamStream",
    "GoogleDatastreamStreamBackfillAll",
    "GoogleDatastreamStreamBackfillAllMysqlExcludedObjects",
    "GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabases",
    "GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesList",
    "GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTables",
    "GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesList",
    "GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumns",
    "GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumnsList",
    "GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumnsOutputReference",
    "GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesOutputReference",
    "GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesOutputReference",
    "GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsOutputReference",
    "GoogleDatastreamStreamBackfillAllOutputReference",
    "GoogleDatastreamStreamBackfillNone",
    "GoogleDatastreamStreamBackfillNoneOutputReference",
    "GoogleDatastreamStreamConfig",
    "GoogleDatastreamStreamDestinationConfig",
    "GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfig",
    "GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigOutputReference",
    "GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDataset",
    "GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDatasetOutputReference",
    "GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasets",
    "GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplate",
    "GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplateOutputReference",
    "GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsOutputReference",
    "GoogleDatastreamStreamDestinationConfigGcsDestinationConfig",
    "GoogleDatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormat",
    "GoogleDatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormatOutputReference",
    "GoogleDatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormat",
    "GoogleDatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormatOutputReference",
    "GoogleDatastreamStreamDestinationConfigGcsDestinationConfigOutputReference",
    "GoogleDatastreamStreamDestinationConfigOutputReference",
    "GoogleDatastreamStreamSourceConfig",
    "GoogleDatastreamStreamSourceConfigMysqlSourceConfig",
    "GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjects",
    "GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabases",
    "GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesList",
    "GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTables",
    "GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesList",
    "GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumns",
    "GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumnsList",
    "GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumnsOutputReference",
    "GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesOutputReference",
    "GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesOutputReference",
    "GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsOutputReference",
    "GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjects",
    "GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabases",
    "GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesList",
    "GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTables",
    "GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesList",
    "GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumns",
    "GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumnsList",
    "GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumnsOutputReference",
    "GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesOutputReference",
    "GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesOutputReference",
    "GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsOutputReference",
    "GoogleDatastreamStreamSourceConfigMysqlSourceConfigOutputReference",
    "GoogleDatastreamStreamSourceConfigOutputReference",
    "GoogleDatastreamStreamTimeouts",
    "GoogleDatastreamStreamTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__b6cfa931a0c0c189dada75078e20e325e1684379e1ca40acf3c5e5b9c924ed26(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    destination_config: typing.Union[GoogleDatastreamStreamDestinationConfig, typing.Dict[builtins.str, typing.Any]],
    display_name: builtins.str,
    location: builtins.str,
    source_config: typing.Union[GoogleDatastreamStreamSourceConfig, typing.Dict[builtins.str, typing.Any]],
    stream_id: builtins.str,
    backfill_all: typing.Optional[typing.Union[GoogleDatastreamStreamBackfillAll, typing.Dict[builtins.str, typing.Any]]] = None,
    backfill_none: typing.Optional[typing.Union[GoogleDatastreamStreamBackfillNone, typing.Dict[builtins.str, typing.Any]]] = None,
    desired_state: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    project: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[GoogleDatastreamStreamTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__f02e6d6086a6388386fbb0384210f4e368b675aedef36739e15a9b27dc467a86(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ece6a77832fb6e89cc0916a10ebc588b04c7d7e93bf43677ad16f9563954cdc9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f14ff4627f324370937935159e22c59189775d0e3b599757fff0ae7935aca61(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6f63ddf26cb02e92cafbfd7bc5446de232f6b8cb951cc5271c9cd8ef7edbd70(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08807dc9fe2f3212f60603e2be9674d576d9b9ebb97552f37256b43f078e57e1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c2f2d9b51d02843746ef23bac88dfc96d8afb17d58d75cfc3fd4c132223b5fa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83b1410afdedd1ac85863a7d2b94759e47bfea699a0ad11b60e2b915ef038f04(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e29d6dac06c9011c575a9755f405c8c91c314097f849d543ea610c2ae0604ac9(
    *,
    mysql_excluded_objects: typing.Optional[typing.Union[GoogleDatastreamStreamBackfillAllMysqlExcludedObjects, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d07bf1e73cbfa0c9924cbdd112f8758d8c5843cb05b182d0821feebbecf1bbfe(
    *,
    mysql_databases: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabases, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__520481cec23840384472636822f5e61482b5d1f652a122cd771b9d999695e41c(
    *,
    database: builtins.str,
    mysql_tables: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTables, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42870644565e23d6a0facda4476561b2c813f8b187a9bef2d4b42bd3b22f4ad7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c27e6265ec073c6cb9d937296a3009c85694518ceb542eb262dc396c0fa0643(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b9f5caf8e7a7472f002063d637ce85c365c019c129961190ee0484f83cb0204(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df989554faa58557b3cee076a0334b3352d497fa9a172a9bc1154b271b849c0d(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ff79f76bcf20116f1f916672658b25c9c6061a155abec3dc69a9fe18fcebc28(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef052bf283a0faa4298ce68f02ad4567fa25c2230ddec569bcbb3eee18d62299(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabases]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3636dc049bfc21560723eff546dfc6111fc1c67103fa20091fcb54e69eb14642(
    *,
    table: builtins.str,
    mysql_columns: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumns, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb36c3ec485d5aa4159c543dbc6060937941194b2d7d16197d5fb5b186c37df9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ea3aa0c93b140d0d206e8e869f0817da6984fb7a0b1aff3d6241d5e683dbbe6(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ad0c9c602594fd4c30646475e0cb03862cdafe47fef23ee13c7b73b8b81d3bf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e409c71a7a46ac3ff0a29f111eb9a54fb36f9b824b997eebe0be60e76c7c343(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0be506fa80b767248dcaa2cb7ed0462bf54b31e761efd4e0fa33f50b4cc6fe9(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4fd33626f965d1fd3a29041aa974d9db1d19cf1b45b7027bfc2e9bd65550d21d(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTables]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23a54185e20f6073f2e24e14685a1bb95703a2f3f4ab9e6eea9d3117b60799c9(
    *,
    collation: typing.Optional[builtins.str] = None,
    column: typing.Optional[builtins.str] = None,
    data_type: typing.Optional[builtins.str] = None,
    nullable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ordinal_position: typing.Optional[jsii.Number] = None,
    primary_key: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e6d7e7079d2c891205e2b32b0cf2ceba725f724854f198bf8512979a5696ce8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84e67f89a6476bdc5c731333cf2029e4a5c782f368d3d69f03978d2ce9dcd94b(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa3cdc2a83c6840973d4070e34bf50a07ee5f2c7d1f3c68e499ac847bfa79317(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22b091b27124f81de04d4b89dc1049358fc60349f3193740d406a0ce1c9e7eeb(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88ef5e48f6385d0236f06a58e25f81251bbc3e6f2240cd75930e6be6beaec4de(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f64de49e3b7a392b9d7c9e39a5e5b791d02929fb6fb384bc5ded7da1c10e90da(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumns]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7292c72a6c771de19158c3d655adc2ba6b3d55d617a83d86255518effa23ba98(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbe8e9c9cb2a678b797af0d6f265ede6140c005c291f7a871610e2b0c46c1239(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5e78f3a0e42427fb9fe7d3218cf22fcd63107183474d933dbe292a0f22ada60(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__801b81a5be1dff9dc10685707b5806e4749464fea9dee3509b069be09a39915d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a4491c86d6cbca170107672efa5ae073217977e38d890ee684dfabffcdc9bbc(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8adf2449960f783a3598bbe1db28d2f83ca4c95a6ca774684164731a9ca4603(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3cfd6c4c2f5f53f106b06e68701b9e7338a0198f1de4971a3980cb71319134f(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4e5c86192b35d7aa9f1c9ff0b2312d4c56114766b1948aeaa6cdb4a187c7447(
    value: typing.Optional[typing.Union[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumns, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5510498980068046efbd3bccc489edaa11d41baf610cf3c6d8b04640da29f441(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1393719f87438cd6e681938c318697c567154ef4d21de037b9794b496d5c053(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumns, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5cdd451c93c14f8bf1348dbc84d1613ee34bee075f1a7ef30641b00e9cc6ddf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40a46438b33027c86396b4bad6c02ccc4329f55d360d33ee604e8932c6d1d25f(
    value: typing.Optional[typing.Union[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTables, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bb2b89ed5c7ab305b2df59f9f1fcae91cadc3414f28c3659364e57a3e1b6dbe(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6be4542a5978109673a55f553153be687fb0155ae52e28084709f661e644b3d1(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTables, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a8764873fb24dfdd954a5d2dbc34cad2573c675bedecb4826b1febb63d5437b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed873de9162601787f1de0b1f1d7bbc82ff2ff4f4f29dcdd5060713a530c99bb(
    value: typing.Optional[typing.Union[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabases, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b17ebe8e257a4918dda760ce5f15ec271e6f36463b2e0b3b2102f151e7afa5a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72168f0c6c5360f01d1caa68b898ee8a3874c0c09c031475e80aefbaf55f483b(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabases, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49719e784f731e00fa4b5f129ee237712081738ae7d610fb8420b43adc072ede(
    value: typing.Optional[GoogleDatastreamStreamBackfillAllMysqlExcludedObjects],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e274f1c79b478e8a9935941ed6e1cae337452327e7e0df1b2e287933f42cb449(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e18596f2739b568b00dc8878957e1a0ae36c322e4460e1efcc618a1fbd80dfb(
    value: typing.Optional[GoogleDatastreamStreamBackfillAll],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7d92abc899aebc8d6d75893b1acd1ccfce0f432db79b875d3d4e45b3724468b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfa1cb735e7372c389d187e9df62ce48602d5e810e1d37efcc2c795f44eae0eb(
    value: typing.Optional[GoogleDatastreamStreamBackfillNone],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8212616678ebc8f5f13dc67f8ecb8284c7ae5d6006e98280adbb52774b08f47(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    destination_config: typing.Union[GoogleDatastreamStreamDestinationConfig, typing.Dict[builtins.str, typing.Any]],
    display_name: builtins.str,
    location: builtins.str,
    source_config: typing.Union[GoogleDatastreamStreamSourceConfig, typing.Dict[builtins.str, typing.Any]],
    stream_id: builtins.str,
    backfill_all: typing.Optional[typing.Union[GoogleDatastreamStreamBackfillAll, typing.Dict[builtins.str, typing.Any]]] = None,
    backfill_none: typing.Optional[typing.Union[GoogleDatastreamStreamBackfillNone, typing.Dict[builtins.str, typing.Any]]] = None,
    desired_state: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    project: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[GoogleDatastreamStreamTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a082f18c6634f77c5c989c278a91ddf6916c61c1c1c1ecaeb403873feb786f6f(
    *,
    destination_connection_profile: builtins.str,
    bigquery_destination_config: typing.Optional[typing.Union[GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    gcs_destination_config: typing.Optional[typing.Union[GoogleDatastreamStreamDestinationConfigGcsDestinationConfig, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3a49c814b4f2ebe3deb762ed064f6ce81ac50435614e1bd2718d7e8651def96(
    *,
    data_freshness: typing.Optional[builtins.str] = None,
    single_target_dataset: typing.Optional[typing.Union[GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDataset, typing.Dict[builtins.str, typing.Any]]] = None,
    source_hierarchy_datasets: typing.Optional[typing.Union[GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasets, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3391270fd72825792750d900baabf072a22d3aa8bfdf9b72803fa90f89feb99(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc227360efefd83c13161506d90374637c3c2dba1821899cf3a429435283aaa2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1e71cd219e14ea812cecfdb4e16eae14cb53d03b3d7baea51323b1fb77a39c3(
    value: typing.Optional[GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8fb9ad9224f683a8eb1f9139234f286bd44fddeece5772c9709e709e591a645(
    *,
    dataset_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a3d055ab4e6752ba6dfdb4394295e7f7318d4a3b762834c187cc27231d4ca7a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4c9b188fd123021caa994f45cf0394e7b3f43765b979d928e6f4d9f0621a963(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04350676f2a57de4c6c34fd5c31fe09fe4989c93a30002c55349461fcd324dd8(
    value: typing.Optional[GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDataset],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe99655d10da1ece8d92b4b95410a92466fc73978fb56cabdd00ce4872af7f30(
    *,
    dataset_template: typing.Union[GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplate, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10bc9309ea21fa94f6d71ec05001d53825566fb8b23e70b72f26ff70b216afbf(
    *,
    location: builtins.str,
    dataset_id_prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__589f4d7cacffa3fe9eaf1ee753fd3bb86c046e23b7c2e374b0f0fe1f59848e72(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3fa782c14749e41909d2558ed573b112c4f62c763ad09af5bb8000ea5bb08163(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04028b6cda5a7527cf51ede06922de56ad34e57e9e59dc68cf55dbb105f0a0db(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5de30ee6e92d12ceb0bda2317dd12bfa52377bec516b2b2a517385018ff4fd37(
    value: typing.Optional[GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplate],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec59f9ec651149d0621d83bf49acbf8ee0bbd34767529437d0eaab1d43196fba(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ead61d6997a472aca9d935cc8910fa587fa5ce5f4d399617f914993534cca402(
    value: typing.Optional[GoogleDatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasets],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d10163a88a5e865a15e425114c10f9f67bb19cad50eff789fae98679356656a(
    *,
    avro_file_format: typing.Optional[typing.Union[GoogleDatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormat, typing.Dict[builtins.str, typing.Any]]] = None,
    file_rotation_interval: typing.Optional[builtins.str] = None,
    file_rotation_mb: typing.Optional[jsii.Number] = None,
    json_file_format: typing.Optional[typing.Union[GoogleDatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormat, typing.Dict[builtins.str, typing.Any]]] = None,
    path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d068a5a28bd2dac3ef4546b05167198e8dc3f67c53ef66378117e2eb38de3e13(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f08298ba4d0b3313ce13d92f69a9b0d3e473996f7259553f11037794731faf97(
    value: typing.Optional[GoogleDatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormat],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac5bf24309609d454116747fe1a8433f1d6909fbbae89e976eff2fea5165e8d7(
    *,
    compression: typing.Optional[builtins.str] = None,
    schema_file_format: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56acedeeab88a59e046f3eda7acc9a87997bd1e847f3661a1d2ecffcaf8ece46(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca5cc438ef5b106f7a336d20a5581f3c31250831e9ffddefcd61b4d1d9ff878f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac1ec35e9777f4ddf604ec41ee7052c7ac0d48e85abfb0a0bc9ffd10834276d3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d5e3c16b98749306678a7e9992adf27157907012286429f2c66df988d0f0bc0(
    value: typing.Optional[GoogleDatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormat],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47a5f5a8a9d9f19534aeab03cc71f662ec8150fb452e35333840e1fa4d19587e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9074e840158c242a6584f690b9de8519093a095062560f763cb0081827756a7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d6fa5c42e1b054c724b34adb45f27353c6ae294899a9d8e80d90a167757cf2f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa2957bdccb90ef0e1d993d38c3afe8f4b14b633ee4a561bb96646544890cbd0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7c83b1266ba6a9af784fac1c33e0f366fe2d370e2f056e83a4d926ae455c27b(
    value: typing.Optional[GoogleDatastreamStreamDestinationConfigGcsDestinationConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7c6a55cbd18393a53cb1933e95b4e468f4a520e2aad658c6da60f7b52de2f3b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4017d208188843d4929bba3e8132e98451cac7713ab722eee13604f90c45b18b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9dcc83c10b6513136386af9d65f30bf2f699f914858eb91aaeeea5968e7dc3c2(
    value: typing.Optional[GoogleDatastreamStreamDestinationConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2219a962a105c32324aa42c0ebabb89901efc5212a250e8d5cbf7c24fdf77d88(
    *,
    mysql_source_config: typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfig, typing.Dict[builtins.str, typing.Any]],
    source_connection_profile: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4778bbd828e1594c449bc443537ebe755eb4c886943cdf45c60649a2abdad88(
    *,
    exclude_objects: typing.Optional[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjects, typing.Dict[builtins.str, typing.Any]]] = None,
    include_objects: typing.Optional[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjects, typing.Dict[builtins.str, typing.Any]]] = None,
    max_concurrent_cdc_tasks: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d83157a8b7dabb6f6a578ba371ae7606ca73d8b886f676352d01e59c8b975065(
    *,
    mysql_databases: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabases, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb545565a9647ff9db741b384db4f82c54b58032c7b2d4e18818cd7d16eeeb69(
    *,
    database: builtins.str,
    mysql_tables: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTables, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2e56eed75c4420627cc1b1ea20e73bc1bbede9df3a2fd8199d4497aa838d16d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a1012ecc8549b81e5e4aa9d9923e204f999b9b29fd4483cafcd96ee9d37e92a(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__749cad1c5353daa5443baca3acaaa68fdf3ee0496883fec1e0a8e7bf6e478f43(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ed34b487f8807df8a3089ff0bf45f39c9f22d366421e027795a5d5ff3b031d3(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47fc60e67695921f46d329ab49e84fb7a745d5f9e52ef95fd339c406ed1f5337(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6580eacf3a0fa9ef788be946237924b568d6c34ca0ce2997d700ceb0ec5909e2(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabases]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8fd22251a137acbd8b6d4011e790c862bba2bc6baff5731831f4aaeb1f09bc8e(
    *,
    table: builtins.str,
    mysql_columns: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumns, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb19d59bcaf47d9126f742045b4d73f2d47c6d705e98fc433966bc88d02bd5ea(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc62e64aa47cf54d533fff2c0ef281c96989464e75c918ffb64f1d14c9d9e79d(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09ac2c33a67547e5fc09ad6eab15b4937398704f7e0dccd16e467818f83a6edd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78f38e38e105221d16e5180f0a1d2c8909391494a32349303610ab95030c9c8c(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d20ad137b3b082c078fd7a5bc38642356759a7fc420d24b61cf649a1f7ed1ad8(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__244522fde9aceac31a2e149744987ae023545406b794b7618a16cb61f5434d3a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTables]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fe080b67925fa358036b8642a0299bcbe1d9e7f96a77e04e3df091ce8d56d79(
    *,
    collation: typing.Optional[builtins.str] = None,
    column: typing.Optional[builtins.str] = None,
    data_type: typing.Optional[builtins.str] = None,
    nullable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ordinal_position: typing.Optional[jsii.Number] = None,
    primary_key: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__201e84943daf6e96eef782d9aca244517f562921989a0d02638fa0c6272b71f8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa8e8e1d140504fda11f4c3773ed96c2555f2d0a8e4e54dd2649412cdce8913b(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09f48286efb01f277d2532514c20596f929b4f09bdd712cce896d54029581845(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__412ca5ab78995949f165cc648a1345246edeca119614f829c8466a957611327d(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8513a9f97f6e8b890e45ed0436f080d3b24af266ac66156a0234692ec528671(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d52d72230d6b4de322b1c93887aea771351503b11807485568c93d0e395bad14(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumns]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cea7b45fb19736020b1719a17d6aec42bd6508059c9e7f8abc1ab4eff5bcf48b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77e9ee7094ccb2bbda850d8033cde908a302188b4966ed9026a0addd79294f25(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3769df6b39afdb7b53797c325a30a0a86634ec6359d219686195fabb6bc4ade(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95e94c186c0638d6e197288bd999f087d07a4e38f94a0c930fded96c19b30a06(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57c29013747c1114bb244cb6f55298a74d6c22ed57f735b6c3fcf456523e93bb(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8083b61ac53f7e64f6d293d8795f8cfcb1af5dcc4641991d8c21d7d14d6a090(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4ce157d33b04ca603a11a14e186e508173db15b13bca2edab6f487ed885c277(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a14532a7d8ee26125f14790252a94be3a764732ba59c7e09374d740bd35cb0a(
    value: typing.Optional[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumns, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9ad39a49db2deb62da532182c908182089fb53ff855492f00ca108bfb38702e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6805013dab1076ffb632b34e127ba4a5b8181fe496c7c0083216d785c6f51a6(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumns, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f635e21d9372998fc0be54b333ef130ee85a23b090304aa7d38db1c57f56b6df(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bcc850b4e3cb4779e1466342590aca58d03c507861a481a9b9fd924abaa00461(
    value: typing.Optional[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTables, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba70a81582b78786b580f56388706a6188061700c80a5ac1049d58ea4ceda106(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25736e01b271cf2c953cc3fe6752d0c6af2a0cefb5fdadb58a006ce4cd317ca1(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTables, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c255dc0ac974e3e989e48a72c5479f88eb080a9286525bb3f1310e4e41d29747(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78514113923d93d64011f19fc8e7df61bc8b692c1ca133f55e2039d7a76a635d(
    value: typing.Optional[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabases, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c84a482c246e68a2697c2dbe687609ff014a57db45d072800f00517f2aa6a56(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__084ed61c2edc5493618eaa16135dff2755b5c72b0b42e1db898c18b18dc6f41f(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabases, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e809bf11601f9faeac3e63217a488b72d3894ca5740326dce20994d858714f2(
    value: typing.Optional[GoogleDatastreamStreamSourceConfigMysqlSourceConfigExcludeObjects],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b782ad37d159e6fc26ccecf102c72c7754e16dda5dfcd19b2bc64b597b89e07(
    *,
    mysql_databases: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabases, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f44f39ebafbebf8e628605efe61a5348b73f5c5884eb1c28dde453f8bf8523a5(
    *,
    database: builtins.str,
    mysql_tables: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTables, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3950f8fb1b59cab5c5f81358a344ffbf164f405bda8837307b833c993cc758d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90939e89008258e8e5fb13b17b64dcac780a64cb8cbe81abc7341daf57a122e8(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__217aa69718caac050d609fc9d8ce57f8bb611e4fa934e6be20a0b57f11f7a1ee(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7dc49121ffff0463e398d82b102cb8ff336eb3cbcd5683e60e9dd1109e48f61(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7ba15a2cd54a82cbc63ae4621ab87db797cd62dcd7ed63ba155e2de063b189e(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d004f44683df7b5074728264cf889cbf037304edfcd3f994117693183d9f5db(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabases]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa194010af037f05469911f39778136fc3ed69ba254253f1224c1a9bbe628999(
    *,
    table: builtins.str,
    mysql_columns: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumns, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dcb77d2e3fb3b195efed0d69e822264d59c5fbf7c1b4cee8e8964364dc9c2123(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba2fe890e741e0c6b63029866f84e111f3cd478bbf199d640a82d12c574d7aa7(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1c7b2e8a8945bd904b6786cb2b4d1aea6874c1ee6838435ab9323baa835b2e0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e69a309bddb1478976b492ae7fb3fd3f17336bc920c0b40e545744ada6341c29(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2671e1f1942c6cb0e3c3ba36f58e950eb50a102df253a43e899c96a138842ff7(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8af2eb875cdae7d71d393ba6e098c6da4c3110914133b1dd079c070354a7a205(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTables]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41215ce0b14ba24427640cc4700269ad49a0faadf8295e7ac03b7f47f2b37132(
    *,
    collation: typing.Optional[builtins.str] = None,
    column: typing.Optional[builtins.str] = None,
    data_type: typing.Optional[builtins.str] = None,
    nullable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ordinal_position: typing.Optional[jsii.Number] = None,
    primary_key: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6861e4975493055a6649272b537f648980427a9301bfb234da05242b7f0c49ec(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9427d6862c644b6d507a55730df9f5fdf5c926418390d5de45f4e2f3f5ee9f5e(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69adb63c3ab9af12da7590f7aae32e0a5104845d11c1ddd67b18b08745828402(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60e663fc168673b4aa74cd1ee2009d59cd03ee3b03440bc1bae19ab2dffb2cdf(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b58a7d494136d2ac7db279ee2b91810061fadc45f6d73f86e92229382749f59a(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7fad90c17f32bc7ae1fccc7cb1431033ed4c2ce630fffd4d769c94decdd59083(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumns]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65b3ccfaf3bad8ab5e06b93c91c603524b0f7f199e7256dfbce872b77ccc667a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68e45a2b6f0d78f15e06a1e14dbc279680b842b3d346da672fb3da0ba499caa5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a954aaaf4ecbb61bdb80680a5308a4650ff1f930fdff1565938a80865567e4b6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8bfd73c16927e583d02f4ece4c98e6e285936610b6ea37d64cb9c6731b30c6e9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c58d677fcfdede4d959a221ab875d5089fa903aa656d2b774755c9e2be2e790(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c454d64cfc5be1fab8c89b6180a07485a1e3934e24523bc92f3900e58a45b43b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__990ed112f00ba5b2fd44cdebb437b9c639030938839325738ece2803bbbee1f4(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac1001f24a95b45f13518456c95010ca63139d5bf238d99bcc2e6386f283bc2d(
    value: typing.Optional[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumns, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6b4a00ce373e23cd5b51bfba3c664c9f9a51885d2951423d35c58dea7aa5613(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c9a1375628b7f6b29a695647f3434428d773a775a513a4c340d0cf934ac7d32(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumns, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__629184c09083c28c9f035a8074dcd1f16f0a61d948bc2393377da3130506e2f1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__759a721a0536fba67735d0dd4283007387dadc2eb076cdb2d65fda1402b5e5f6(
    value: typing.Optional[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTables, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8548900250b3351b1c6d41c39a3f7fc3652815a7c6184c8c707341c35763ac3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b269534d2b5371b90449e0d4dd96df396fbca76931cb7a5f54a30f1b654543d(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTables, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0dc2394f1204551f9f707dbf0479faf9458fafc6a03c129b132c5e409293bb9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32b6f477c199b7d70e86e7f6dec51b8b579ebe58c787a257fcb73e04d3cc5bcf(
    value: typing.Optional[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabases, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b401a73888aa3eedea89455bd1d7e18731ee7412824c21d4be2f36a727cd8a7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__613d8a98ff90be15005996fdfac043d333f8645c71d52edfc24b79e3b6031649(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabases, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc63fda8e348ad1f4425fc05aec528be1a2b9aabab914770a3fb1f72c46604b1(
    value: typing.Optional[GoogleDatastreamStreamSourceConfigMysqlSourceConfigIncludeObjects],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efb86a24b39d875af0044075b654f055d4cf52279a7e2097cdcb5b797e5ff174(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75042a2bfae52ebd1b965d7005d120750faa2993f31c1eeb04500e45bd87a769(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5301d37e1a77c15dc3423d2d6672f672b5059dd74d24e85d8326831c85d9c317(
    value: typing.Optional[GoogleDatastreamStreamSourceConfigMysqlSourceConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__935aa7233aaac0fbc524f35d41c8b42f4f855c3d54fd43f35f0e7b9d7528b61d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad6aaf1380cfd2cad252287f4082eac6cb898c810899506186dbc4bf8daf22af(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d31a3dae34b03d71885cecf9357ff558547f3eba368913731781633806d28251(
    value: typing.Optional[GoogleDatastreamStreamSourceConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a54b49f7561784b6ddbf39b45bfd0f91cd4d531a183f057a0f51c1fb036c6ee4(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a1e593819993f0b26e94eb2825132a675053b005efe8ffb05266fd2c2530166(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72ae4642fb1a34ac292bc77f8755496644a696b2005d238ad3d096cf94340334(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f50f1677bf065b391c40444994d038f923d9d5c282b68e34cbff128a610e0e0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27df4af47c20495c8bd3cfc96cc0d9e42b03499ba5a08622470954ed4ff13101(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9644ba1934244050f95ca839e3c9e108ad0d0d1156a6d8051eae93e46bb4269a(
    value: typing.Optional[typing.Union[GoogleDatastreamStreamTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
