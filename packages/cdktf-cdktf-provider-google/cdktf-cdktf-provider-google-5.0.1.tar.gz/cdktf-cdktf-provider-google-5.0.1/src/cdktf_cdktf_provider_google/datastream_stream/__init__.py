'''
# `google_datastream_stream`

Refer to the Terraform Registory for docs: [`google_datastream_stream`](https://www.terraform.io/docs/providers/google/r/datastream_stream).
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


class DatastreamStream(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.datastreamStream.DatastreamStream",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google/r/datastream_stream google_datastream_stream}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        destination_config: typing.Union["DatastreamStreamDestinationConfig", typing.Dict[builtins.str, typing.Any]],
        display_name: builtins.str,
        location: builtins.str,
        source_config: typing.Union["DatastreamStreamSourceConfig", typing.Dict[builtins.str, typing.Any]],
        stream_id: builtins.str,
        backfill_all: typing.Optional[typing.Union["DatastreamStreamBackfillAll", typing.Dict[builtins.str, typing.Any]]] = None,
        backfill_none: typing.Optional[typing.Union["DatastreamStreamBackfillNone", typing.Dict[builtins.str, typing.Any]]] = None,
        desired_state: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        project: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["DatastreamStreamTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google/r/datastream_stream google_datastream_stream} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param destination_config: destination_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#destination_config DatastreamStream#destination_config}
        :param display_name: Display name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#display_name DatastreamStream#display_name}
        :param location: The name of the location this stream is located in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#location DatastreamStream#location}
        :param source_config: source_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#source_config DatastreamStream#source_config}
        :param stream_id: The stream identifier. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#stream_id DatastreamStream#stream_id}
        :param backfill_all: backfill_all block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#backfill_all DatastreamStream#backfill_all}
        :param backfill_none: backfill_none block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#backfill_none DatastreamStream#backfill_none}
        :param desired_state: Desired state of the Stream. Set this field to 'RUNNING' to start the stream, and 'PAUSED' to pause the stream. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#desired_state DatastreamStream#desired_state}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#id DatastreamStream#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: Labels. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#labels DatastreamStream#labels}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#project DatastreamStream#project}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#timeouts DatastreamStream#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c3ae3a9775ec6a2f34ba62bb34fac9132ef80c080cb4f5fc8bb6686d10ac590)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DatastreamStreamConfig(
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
        mysql_excluded_objects: typing.Optional[typing.Union["DatastreamStreamBackfillAllMysqlExcludedObjects", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param mysql_excluded_objects: mysql_excluded_objects block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#mysql_excluded_objects DatastreamStream#mysql_excluded_objects}
        '''
        value = DatastreamStreamBackfillAll(
            mysql_excluded_objects=mysql_excluded_objects
        )

        return typing.cast(None, jsii.invoke(self, "putBackfillAll", [value]))

    @jsii.member(jsii_name="putBackfillNone")
    def put_backfill_none(self) -> None:
        value = DatastreamStreamBackfillNone()

        return typing.cast(None, jsii.invoke(self, "putBackfillNone", [value]))

    @jsii.member(jsii_name="putDestinationConfig")
    def put_destination_config(
        self,
        *,
        destination_connection_profile: builtins.str,
        bigquery_destination_config: typing.Optional[typing.Union["DatastreamStreamDestinationConfigBigqueryDestinationConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        gcs_destination_config: typing.Optional[typing.Union["DatastreamStreamDestinationConfigGcsDestinationConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param destination_connection_profile: Destination connection profile resource. Format: projects/{project}/locations/{location}/connectionProfiles/{name}. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#destination_connection_profile DatastreamStream#destination_connection_profile}
        :param bigquery_destination_config: bigquery_destination_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#bigquery_destination_config DatastreamStream#bigquery_destination_config}
        :param gcs_destination_config: gcs_destination_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#gcs_destination_config DatastreamStream#gcs_destination_config}
        '''
        value = DatastreamStreamDestinationConfig(
            destination_connection_profile=destination_connection_profile,
            bigquery_destination_config=bigquery_destination_config,
            gcs_destination_config=gcs_destination_config,
        )

        return typing.cast(None, jsii.invoke(self, "putDestinationConfig", [value]))

    @jsii.member(jsii_name="putSourceConfig")
    def put_source_config(
        self,
        *,
        mysql_source_config: typing.Union["DatastreamStreamSourceConfigMysqlSourceConfig", typing.Dict[builtins.str, typing.Any]],
        source_connection_profile: builtins.str,
    ) -> None:
        '''
        :param mysql_source_config: mysql_source_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#mysql_source_config DatastreamStream#mysql_source_config}
        :param source_connection_profile: Source connection profile resource. Format: projects/{project}/locations/{location}/connectionProfiles/{name}. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#source_connection_profile DatastreamStream#source_connection_profile}
        '''
        value = DatastreamStreamSourceConfig(
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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#create DatastreamStream#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#delete DatastreamStream#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#update DatastreamStream#update}.
        '''
        value = DatastreamStreamTimeouts(create=create, delete=delete, update=update)

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
    def backfill_all(self) -> "DatastreamStreamBackfillAllOutputReference":
        return typing.cast("DatastreamStreamBackfillAllOutputReference", jsii.get(self, "backfillAll"))

    @builtins.property
    @jsii.member(jsii_name="backfillNone")
    def backfill_none(self) -> "DatastreamStreamBackfillNoneOutputReference":
        return typing.cast("DatastreamStreamBackfillNoneOutputReference", jsii.get(self, "backfillNone"))

    @builtins.property
    @jsii.member(jsii_name="destinationConfig")
    def destination_config(self) -> "DatastreamStreamDestinationConfigOutputReference":
        return typing.cast("DatastreamStreamDestinationConfigOutputReference", jsii.get(self, "destinationConfig"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="sourceConfig")
    def source_config(self) -> "DatastreamStreamSourceConfigOutputReference":
        return typing.cast("DatastreamStreamSourceConfigOutputReference", jsii.get(self, "sourceConfig"))

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "DatastreamStreamTimeoutsOutputReference":
        return typing.cast("DatastreamStreamTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="backfillAllInput")
    def backfill_all_input(self) -> typing.Optional["DatastreamStreamBackfillAll"]:
        return typing.cast(typing.Optional["DatastreamStreamBackfillAll"], jsii.get(self, "backfillAllInput"))

    @builtins.property
    @jsii.member(jsii_name="backfillNoneInput")
    def backfill_none_input(self) -> typing.Optional["DatastreamStreamBackfillNone"]:
        return typing.cast(typing.Optional["DatastreamStreamBackfillNone"], jsii.get(self, "backfillNoneInput"))

    @builtins.property
    @jsii.member(jsii_name="desiredStateInput")
    def desired_state_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "desiredStateInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationConfigInput")
    def destination_config_input(
        self,
    ) -> typing.Optional["DatastreamStreamDestinationConfig"]:
        return typing.cast(typing.Optional["DatastreamStreamDestinationConfig"], jsii.get(self, "destinationConfigInput"))

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
    def source_config_input(self) -> typing.Optional["DatastreamStreamSourceConfig"]:
        return typing.cast(typing.Optional["DatastreamStreamSourceConfig"], jsii.get(self, "sourceConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="streamIdInput")
    def stream_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "streamIdInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["DatastreamStreamTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["DatastreamStreamTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="desiredState")
    def desired_state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "desiredState"))

    @desired_state.setter
    def desired_state(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52394fe12c454915c68b7f5c0e1158a297c28bf8edc5470752d8d03bdadb3ff5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "desiredState", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__075bf1e3249baeb8aa177ed19b3f502beb142b110c60b7139a705093ce1b0a7d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07f951eeadca73ea4a620fa2306732bbea40433c714d9c7f9ff106a61a7faead)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aef205b5c5ab66f32171c7535e21c4e68b81ebab105a33f1ff35977ad01202a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ecf79e1cbe57e9eb4ed393c90fd467db45153af81195ed412bfacee8feaa28a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__643d9836b9fc11f1901e2a2838ff876acef8280f6554dd37d2d02fa890104d78)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="streamId")
    def stream_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "streamId"))

    @stream_id.setter
    def stream_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__283627036b55d75a53badb063b8cbdcac874d10da468b6abae149456f4ed27d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "streamId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.datastreamStream.DatastreamStreamBackfillAll",
    jsii_struct_bases=[],
    name_mapping={"mysql_excluded_objects": "mysqlExcludedObjects"},
)
class DatastreamStreamBackfillAll:
    def __init__(
        self,
        *,
        mysql_excluded_objects: typing.Optional[typing.Union["DatastreamStreamBackfillAllMysqlExcludedObjects", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param mysql_excluded_objects: mysql_excluded_objects block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#mysql_excluded_objects DatastreamStream#mysql_excluded_objects}
        '''
        if isinstance(mysql_excluded_objects, dict):
            mysql_excluded_objects = DatastreamStreamBackfillAllMysqlExcludedObjects(**mysql_excluded_objects)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__548fd10e905731875c7b597865e08230b888f6d65781f1f9e58cc54902b013a8)
            check_type(argname="argument mysql_excluded_objects", value=mysql_excluded_objects, expected_type=type_hints["mysql_excluded_objects"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if mysql_excluded_objects is not None:
            self._values["mysql_excluded_objects"] = mysql_excluded_objects

    @builtins.property
    def mysql_excluded_objects(
        self,
    ) -> typing.Optional["DatastreamStreamBackfillAllMysqlExcludedObjects"]:
        '''mysql_excluded_objects block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#mysql_excluded_objects DatastreamStream#mysql_excluded_objects}
        '''
        result = self._values.get("mysql_excluded_objects")
        return typing.cast(typing.Optional["DatastreamStreamBackfillAllMysqlExcludedObjects"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatastreamStreamBackfillAll(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google.datastreamStream.DatastreamStreamBackfillAllMysqlExcludedObjects",
    jsii_struct_bases=[],
    name_mapping={"mysql_databases": "mysqlDatabases"},
)
class DatastreamStreamBackfillAllMysqlExcludedObjects:
    def __init__(
        self,
        *,
        mysql_databases: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabases", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param mysql_databases: mysql_databases block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#mysql_databases DatastreamStream#mysql_databases}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69c73ea13a69e84cb5c059ba0260ae859d8c602b57e97a85cc24ad93dfc88b5f)
            check_type(argname="argument mysql_databases", value=mysql_databases, expected_type=type_hints["mysql_databases"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "mysql_databases": mysql_databases,
        }

    @builtins.property
    def mysql_databases(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabases"]]:
        '''mysql_databases block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#mysql_databases DatastreamStream#mysql_databases}
        '''
        result = self._values.get("mysql_databases")
        assert result is not None, "Required property 'mysql_databases' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabases"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatastreamStreamBackfillAllMysqlExcludedObjects(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google.datastreamStream.DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabases",
    jsii_struct_bases=[],
    name_mapping={"database": "database", "mysql_tables": "mysqlTables"},
)
class DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabases:
    def __init__(
        self,
        *,
        database: builtins.str,
        mysql_tables: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTables", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param database: Database name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#database DatastreamStream#database}
        :param mysql_tables: mysql_tables block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#mysql_tables DatastreamStream#mysql_tables}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13410b2bfcca2c97647224c4a67319d908e9d319c6a9237cc85a4e41f55b548f)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#database DatastreamStream#database}
        '''
        result = self._values.get("database")
        assert result is not None, "Required property 'database' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def mysql_tables(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTables"]]]:
        '''mysql_tables block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#mysql_tables DatastreamStream#mysql_tables}
        '''
        result = self._values.get("mysql_tables")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTables"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabases(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.datastreamStream.DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ea67c8ef97a0bde8fc840322d14b0b15cad0751a347171e7dc7803d39cec09bb)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e433a44dd8df3a9cadc62af5b456b9bc010f04b3ba73bafaf04a805db07586db)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae3201f4411b84a193a6646dd047aa80f26f7dde220aef2aef705c5287e252e0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d3c44068e63d483ac615dac0b8b6f39ba7905423e373797afbe8cc55e6cd75e9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__28ae6f5b98dab77299fa101efba9a44e8d9bd7f7ad9211e91cba088aa6c700ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabases]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabases]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabases]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aebbfa9a89be0456ea53147d93d92bf800659d380f16345317d1f06cc039aa0a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.datastreamStream.DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTables",
    jsii_struct_bases=[],
    name_mapping={"table": "table", "mysql_columns": "mysqlColumns"},
)
class DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTables:
    def __init__(
        self,
        *,
        table: builtins.str,
        mysql_columns: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumns", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param table: Table name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#table DatastreamStream#table}
        :param mysql_columns: mysql_columns block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#mysql_columns DatastreamStream#mysql_columns}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c949b7e6ad7f4b38807ff06c703f595dfd880a47c4b1d04b04a3915dec77355a)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#table DatastreamStream#table}
        '''
        result = self._values.get("table")
        assert result is not None, "Required property 'table' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def mysql_columns(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumns"]]]:
        '''mysql_columns block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#mysql_columns DatastreamStream#mysql_columns}
        '''
        result = self._values.get("mysql_columns")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumns"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTables(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.datastreamStream.DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e065db95f692750c0a4063feef0b9379251d390020ae9aa8597c39b18492722e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f71340320398dcd9797361c897dd802615c2838318ad836b9a8a7a371389ce73)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6fae007e595a16d2276fc86cc2a375a7ac4c4e4fdf0b5e9c3807728d0312608d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6f42f8dee5cb9de65146de9913d0470c79954bff38cb9237b2821934c9d38ba3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__09927ad10009415e1a205ef82c502175614a7e64824510e9b69fbf9eec02feb4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTables]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTables]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTables]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0487084e9cacd7c8d5ac7a0aa828f1cf005979ca02f03bd6ac2db3f9e309f1c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.datastreamStream.DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumns",
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
class DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumns:
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
        :param collation: Column collation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#collation DatastreamStream#collation}
        :param column: Column name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#column DatastreamStream#column}
        :param data_type: The MySQL data type. Full data types list can be found here: https://dev.mysql.com/doc/refman/8.0/en/data-types.html. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#data_type DatastreamStream#data_type}
        :param nullable: Whether or not the column can accept a null value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#nullable DatastreamStream#nullable}
        :param ordinal_position: The ordinal position of the column in the table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#ordinal_position DatastreamStream#ordinal_position}
        :param primary_key: Whether or not the column represents a primary key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#primary_key DatastreamStream#primary_key}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__358f467e5b0f4377a34511fe2df79cd3ce7c42608d71ea9bc665657743281de9)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#collation DatastreamStream#collation}
        '''
        result = self._values.get("collation")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def column(self) -> typing.Optional[builtins.str]:
        '''Column name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#column DatastreamStream#column}
        '''
        result = self._values.get("column")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_type(self) -> typing.Optional[builtins.str]:
        '''The MySQL data type. Full data types list can be found here: https://dev.mysql.com/doc/refman/8.0/en/data-types.html.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#data_type DatastreamStream#data_type}
        '''
        result = self._values.get("data_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def nullable(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether or not the column can accept a null value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#nullable DatastreamStream#nullable}
        '''
        result = self._values.get("nullable")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def ordinal_position(self) -> typing.Optional[jsii.Number]:
        '''The ordinal position of the column in the table.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#ordinal_position DatastreamStream#ordinal_position}
        '''
        result = self._values.get("ordinal_position")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def primary_key(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether or not the column represents a primary key.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#primary_key DatastreamStream#primary_key}
        '''
        result = self._values.get("primary_key")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumns(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumnsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.datastreamStream.DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumnsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__154f8dbef744b6d64d4b273c1aee6e622e76745c185fc129b20166f1d3b1983d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumnsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__713d5e717689a63ec3720f83c87565cadea875f763aa9cc85738d05e657e219d)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumnsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bfa9e390d9ad10ccedd8763652c1adc0808202e386abbe93d623f621504e76ce)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9301374e73e0c50562a61bc71b8dd7a070d34619dda616483dea5909e9f46f98)
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
            type_hints = typing.get_type_hints(_typecheckingstub__91c7b000f7d51a6d417fbacbfba2f039c7d7c3eb9281b41955951acec133650c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumns]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumns]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumns]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e5df9305e59f038bfd61176fa4734ffa910d0bf7dee993b79f7d55c7529c3a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumnsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.datastreamStream.DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumnsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f018984efb7d263d0ffcb99493054e866b0c5304311041e893283f901e4a6c5f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__70a552d16c9eeee74bbdd4efdd9298e085ed23856eae9264a8b1de5d65bc128c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "collation", value)

    @builtins.property
    @jsii.member(jsii_name="column")
    def column(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "column"))

    @column.setter
    def column(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ef3bcf0cf613c3945de3f7f965b20939420613dbf0bda0a777109acd57296b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "column", value)

    @builtins.property
    @jsii.member(jsii_name="dataType")
    def data_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataType"))

    @data_type.setter
    def data_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4ccd286da9f0d1f1989f8eff655c80e6b67fe37f7ff035a8f81704b1c1948fe)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f42f8e7181c09785a11ef026e085afe5bbd15bce5111673479bccb9c3566cc49)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nullable", value)

    @builtins.property
    @jsii.member(jsii_name="ordinalPosition")
    def ordinal_position(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ordinalPosition"))

    @ordinal_position.setter
    def ordinal_position(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__097daa092a18ee02bf8669de9bd114d35e6fadb3ea65a486cabfd5b2425b3f73)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2d4cd8ea957cbc5045edf6e2553556a3e684a0ab60fb1a5fa3c7c003e727ee3f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "primaryKey", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumns, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumns, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumns, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9e079a8c2bf48a82f26ea7ebb4307d6a05b485fc96ce3f041b43af86038484f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.datastreamStream.DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__87a74c6f0174c2f917092188e7a5baac1b4376e817d30c3ddac8bfdd08ace52b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putMysqlColumns")
    def put_mysql_columns(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumns, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e9d4d13b08ecd8dfe67092ac6f87dde17666a854de010456318e3bdd9e068bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMysqlColumns", [value]))

    @jsii.member(jsii_name="resetMysqlColumns")
    def reset_mysql_columns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMysqlColumns", []))

    @builtins.property
    @jsii.member(jsii_name="mysqlColumns")
    def mysql_columns(
        self,
    ) -> DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumnsList:
        return typing.cast(DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumnsList, jsii.get(self, "mysqlColumns"))

    @builtins.property
    @jsii.member(jsii_name="mysqlColumnsInput")
    def mysql_columns_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumns]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumns]]], jsii.get(self, "mysqlColumnsInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__0f0e90b83d1fa5fa9212c0d7bb6231593356596ff82ad67b135f440e2c462282)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "table", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTables, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTables, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTables, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de0b4e25f18b8e00271d40dc319fa34c7902a7c2c0ad6fd321f7f236706f10f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.datastreamStream.DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8f5f8347e6725fe1f7f0267f7c851ffb9628cb21ac0e30564b95091505abfc30)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putMysqlTables")
    def put_mysql_tables(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTables, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f814fec22f6e810871992154543a73b1af75cbbc27447a3fe884a5a80fb50c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMysqlTables", [value]))

    @jsii.member(jsii_name="resetMysqlTables")
    def reset_mysql_tables(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMysqlTables", []))

    @builtins.property
    @jsii.member(jsii_name="mysqlTables")
    def mysql_tables(
        self,
    ) -> DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesList:
        return typing.cast(DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesList, jsii.get(self, "mysqlTables"))

    @builtins.property
    @jsii.member(jsii_name="databaseInput")
    def database_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseInput"))

    @builtins.property
    @jsii.member(jsii_name="mysqlTablesInput")
    def mysql_tables_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTables]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTables]]], jsii.get(self, "mysqlTablesInput"))

    @builtins.property
    @jsii.member(jsii_name="database")
    def database(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "database"))

    @database.setter
    def database(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3151b274792b3f93fe09adbe180c158913e6bd5db0b114d7f42e9a220f02a568)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "database", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabases, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabases, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabases, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a7388148daab50b0ac722ba039b4763c332b0cf752fb7ecd0b82947dc468abe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DatastreamStreamBackfillAllMysqlExcludedObjectsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.datastreamStream.DatastreamStreamBackfillAllMysqlExcludedObjectsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0f1d7a4d992a763ac519977aaaad6c758ee59d5bab019a7a7745a4616285a28d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMysqlDatabases")
    def put_mysql_databases(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabases, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__931bbf966cb9ba2aae819fbebe1786809f88f7da77ce8346aaffbdcfad968a76)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMysqlDatabases", [value]))

    @builtins.property
    @jsii.member(jsii_name="mysqlDatabases")
    def mysql_databases(
        self,
    ) -> DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesList:
        return typing.cast(DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesList, jsii.get(self, "mysqlDatabases"))

    @builtins.property
    @jsii.member(jsii_name="mysqlDatabasesInput")
    def mysql_databases_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabases]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabases]]], jsii.get(self, "mysqlDatabasesInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DatastreamStreamBackfillAllMysqlExcludedObjects]:
        return typing.cast(typing.Optional[DatastreamStreamBackfillAllMysqlExcludedObjects], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DatastreamStreamBackfillAllMysqlExcludedObjects],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__811433edaf8b7400da4083dd0803cdd680452b065b43ce1320c11977ab1cc96f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DatastreamStreamBackfillAllOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.datastreamStream.DatastreamStreamBackfillAllOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3f2165189e7c8f1b458755c804ed55962f85c000ded00d4c56f68f9f3bcf3eb1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMysqlExcludedObjects")
    def put_mysql_excluded_objects(
        self,
        *,
        mysql_databases: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabases, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param mysql_databases: mysql_databases block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#mysql_databases DatastreamStream#mysql_databases}
        '''
        value = DatastreamStreamBackfillAllMysqlExcludedObjects(
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
    ) -> DatastreamStreamBackfillAllMysqlExcludedObjectsOutputReference:
        return typing.cast(DatastreamStreamBackfillAllMysqlExcludedObjectsOutputReference, jsii.get(self, "mysqlExcludedObjects"))

    @builtins.property
    @jsii.member(jsii_name="mysqlExcludedObjectsInput")
    def mysql_excluded_objects_input(
        self,
    ) -> typing.Optional[DatastreamStreamBackfillAllMysqlExcludedObjects]:
        return typing.cast(typing.Optional[DatastreamStreamBackfillAllMysqlExcludedObjects], jsii.get(self, "mysqlExcludedObjectsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DatastreamStreamBackfillAll]:
        return typing.cast(typing.Optional[DatastreamStreamBackfillAll], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DatastreamStreamBackfillAll],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef5097bf84b7756c5e909c8358f325e4cc1c90362407525d463c71a947058c4a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.datastreamStream.DatastreamStreamBackfillNone",
    jsii_struct_bases=[],
    name_mapping={},
)
class DatastreamStreamBackfillNone:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatastreamStreamBackfillNone(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatastreamStreamBackfillNoneOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.datastreamStream.DatastreamStreamBackfillNoneOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2fe33cc0ef94cf2a41dd327fc0be0593dc211e9743a24827b5ee773542c7a8c7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DatastreamStreamBackfillNone]:
        return typing.cast(typing.Optional[DatastreamStreamBackfillNone], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DatastreamStreamBackfillNone],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af34f772ce61a51e2c5569138f820502f4470ede6042b4080b30aef00600f8a6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.datastreamStream.DatastreamStreamConfig",
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
class DatastreamStreamConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        destination_config: typing.Union["DatastreamStreamDestinationConfig", typing.Dict[builtins.str, typing.Any]],
        display_name: builtins.str,
        location: builtins.str,
        source_config: typing.Union["DatastreamStreamSourceConfig", typing.Dict[builtins.str, typing.Any]],
        stream_id: builtins.str,
        backfill_all: typing.Optional[typing.Union[DatastreamStreamBackfillAll, typing.Dict[builtins.str, typing.Any]]] = None,
        backfill_none: typing.Optional[typing.Union[DatastreamStreamBackfillNone, typing.Dict[builtins.str, typing.Any]]] = None,
        desired_state: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        project: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["DatastreamStreamTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param destination_config: destination_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#destination_config DatastreamStream#destination_config}
        :param display_name: Display name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#display_name DatastreamStream#display_name}
        :param location: The name of the location this stream is located in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#location DatastreamStream#location}
        :param source_config: source_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#source_config DatastreamStream#source_config}
        :param stream_id: The stream identifier. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#stream_id DatastreamStream#stream_id}
        :param backfill_all: backfill_all block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#backfill_all DatastreamStream#backfill_all}
        :param backfill_none: backfill_none block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#backfill_none DatastreamStream#backfill_none}
        :param desired_state: Desired state of the Stream. Set this field to 'RUNNING' to start the stream, and 'PAUSED' to pause the stream. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#desired_state DatastreamStream#desired_state}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#id DatastreamStream#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: Labels. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#labels DatastreamStream#labels}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#project DatastreamStream#project}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#timeouts DatastreamStream#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(destination_config, dict):
            destination_config = DatastreamStreamDestinationConfig(**destination_config)
        if isinstance(source_config, dict):
            source_config = DatastreamStreamSourceConfig(**source_config)
        if isinstance(backfill_all, dict):
            backfill_all = DatastreamStreamBackfillAll(**backfill_all)
        if isinstance(backfill_none, dict):
            backfill_none = DatastreamStreamBackfillNone(**backfill_none)
        if isinstance(timeouts, dict):
            timeouts = DatastreamStreamTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__010b9566f8020e188444914b63cda5178f17cff35ec3ccd2e68861aaf3a93e42)
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
    def destination_config(self) -> "DatastreamStreamDestinationConfig":
        '''destination_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#destination_config DatastreamStream#destination_config}
        '''
        result = self._values.get("destination_config")
        assert result is not None, "Required property 'destination_config' is missing"
        return typing.cast("DatastreamStreamDestinationConfig", result)

    @builtins.property
    def display_name(self) -> builtins.str:
        '''Display name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#display_name DatastreamStream#display_name}
        '''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def location(self) -> builtins.str:
        '''The name of the location this stream is located in.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#location DatastreamStream#location}
        '''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_config(self) -> "DatastreamStreamSourceConfig":
        '''source_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#source_config DatastreamStream#source_config}
        '''
        result = self._values.get("source_config")
        assert result is not None, "Required property 'source_config' is missing"
        return typing.cast("DatastreamStreamSourceConfig", result)

    @builtins.property
    def stream_id(self) -> builtins.str:
        '''The stream identifier.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#stream_id DatastreamStream#stream_id}
        '''
        result = self._values.get("stream_id")
        assert result is not None, "Required property 'stream_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def backfill_all(self) -> typing.Optional[DatastreamStreamBackfillAll]:
        '''backfill_all block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#backfill_all DatastreamStream#backfill_all}
        '''
        result = self._values.get("backfill_all")
        return typing.cast(typing.Optional[DatastreamStreamBackfillAll], result)

    @builtins.property
    def backfill_none(self) -> typing.Optional[DatastreamStreamBackfillNone]:
        '''backfill_none block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#backfill_none DatastreamStream#backfill_none}
        '''
        result = self._values.get("backfill_none")
        return typing.cast(typing.Optional[DatastreamStreamBackfillNone], result)

    @builtins.property
    def desired_state(self) -> typing.Optional[builtins.str]:
        '''Desired state of the Stream.

        Set this field to 'RUNNING' to start the stream, and 'PAUSED' to pause the stream.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#desired_state DatastreamStream#desired_state}
        '''
        result = self._values.get("desired_state")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#id DatastreamStream#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Labels.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#labels DatastreamStream#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#project DatastreamStream#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["DatastreamStreamTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#timeouts DatastreamStream#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["DatastreamStreamTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatastreamStreamConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google.datastreamStream.DatastreamStreamDestinationConfig",
    jsii_struct_bases=[],
    name_mapping={
        "destination_connection_profile": "destinationConnectionProfile",
        "bigquery_destination_config": "bigqueryDestinationConfig",
        "gcs_destination_config": "gcsDestinationConfig",
    },
)
class DatastreamStreamDestinationConfig:
    def __init__(
        self,
        *,
        destination_connection_profile: builtins.str,
        bigquery_destination_config: typing.Optional[typing.Union["DatastreamStreamDestinationConfigBigqueryDestinationConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        gcs_destination_config: typing.Optional[typing.Union["DatastreamStreamDestinationConfigGcsDestinationConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param destination_connection_profile: Destination connection profile resource. Format: projects/{project}/locations/{location}/connectionProfiles/{name}. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#destination_connection_profile DatastreamStream#destination_connection_profile}
        :param bigquery_destination_config: bigquery_destination_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#bigquery_destination_config DatastreamStream#bigquery_destination_config}
        :param gcs_destination_config: gcs_destination_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#gcs_destination_config DatastreamStream#gcs_destination_config}
        '''
        if isinstance(bigquery_destination_config, dict):
            bigquery_destination_config = DatastreamStreamDestinationConfigBigqueryDestinationConfig(**bigquery_destination_config)
        if isinstance(gcs_destination_config, dict):
            gcs_destination_config = DatastreamStreamDestinationConfigGcsDestinationConfig(**gcs_destination_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f00248466cff6f376a67121eae26291d4773ff89be51d7e77bcce5aef3e183c)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#destination_connection_profile DatastreamStream#destination_connection_profile}
        '''
        result = self._values.get("destination_connection_profile")
        assert result is not None, "Required property 'destination_connection_profile' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bigquery_destination_config(
        self,
    ) -> typing.Optional["DatastreamStreamDestinationConfigBigqueryDestinationConfig"]:
        '''bigquery_destination_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#bigquery_destination_config DatastreamStream#bigquery_destination_config}
        '''
        result = self._values.get("bigquery_destination_config")
        return typing.cast(typing.Optional["DatastreamStreamDestinationConfigBigqueryDestinationConfig"], result)

    @builtins.property
    def gcs_destination_config(
        self,
    ) -> typing.Optional["DatastreamStreamDestinationConfigGcsDestinationConfig"]:
        '''gcs_destination_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#gcs_destination_config DatastreamStream#gcs_destination_config}
        '''
        result = self._values.get("gcs_destination_config")
        return typing.cast(typing.Optional["DatastreamStreamDestinationConfigGcsDestinationConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatastreamStreamDestinationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google.datastreamStream.DatastreamStreamDestinationConfigBigqueryDestinationConfig",
    jsii_struct_bases=[],
    name_mapping={
        "data_freshness": "dataFreshness",
        "single_target_dataset": "singleTargetDataset",
        "source_hierarchy_datasets": "sourceHierarchyDatasets",
    },
)
class DatastreamStreamDestinationConfigBigqueryDestinationConfig:
    def __init__(
        self,
        *,
        data_freshness: typing.Optional[builtins.str] = None,
        single_target_dataset: typing.Optional[typing.Union["DatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDataset", typing.Dict[builtins.str, typing.Any]]] = None,
        source_hierarchy_datasets: typing.Optional[typing.Union["DatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasets", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param data_freshness: The guaranteed data freshness (in seconds) when querying tables created by the stream. Editing this field will only affect new tables created in the future, but existing tables will not be impacted. Lower values mean that queries will return fresher data, but may result in higher cost. A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s". Defaults to 900s. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#data_freshness DatastreamStream#data_freshness}
        :param single_target_dataset: single_target_dataset block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#single_target_dataset DatastreamStream#single_target_dataset}
        :param source_hierarchy_datasets: source_hierarchy_datasets block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#source_hierarchy_datasets DatastreamStream#source_hierarchy_datasets}
        '''
        if isinstance(single_target_dataset, dict):
            single_target_dataset = DatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDataset(**single_target_dataset)
        if isinstance(source_hierarchy_datasets, dict):
            source_hierarchy_datasets = DatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasets(**source_hierarchy_datasets)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05d3281f73805ef674d65a156cd694bf3f6a088663f008143e968719408b4685)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#data_freshness DatastreamStream#data_freshness}
        '''
        result = self._values.get("data_freshness")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def single_target_dataset(
        self,
    ) -> typing.Optional["DatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDataset"]:
        '''single_target_dataset block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#single_target_dataset DatastreamStream#single_target_dataset}
        '''
        result = self._values.get("single_target_dataset")
        return typing.cast(typing.Optional["DatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDataset"], result)

    @builtins.property
    def source_hierarchy_datasets(
        self,
    ) -> typing.Optional["DatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasets"]:
        '''source_hierarchy_datasets block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#source_hierarchy_datasets DatastreamStream#source_hierarchy_datasets}
        '''
        result = self._values.get("source_hierarchy_datasets")
        return typing.cast(typing.Optional["DatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasets"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatastreamStreamDestinationConfigBigqueryDestinationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatastreamStreamDestinationConfigBigqueryDestinationConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.datastreamStream.DatastreamStreamDestinationConfigBigqueryDestinationConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d7a8b609b22768f789ea3611aa0ef25787c5d73f4a59a9be4ef77efa3c492a81)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSingleTargetDataset")
    def put_single_target_dataset(self, *, dataset_id: builtins.str) -> None:
        '''
        :param dataset_id: Dataset ID in the format projects/{project}/datasets/{dataset_id}. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#dataset_id DatastreamStream#dataset_id}
        '''
        value = DatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDataset(
            dataset_id=dataset_id
        )

        return typing.cast(None, jsii.invoke(self, "putSingleTargetDataset", [value]))

    @jsii.member(jsii_name="putSourceHierarchyDatasets")
    def put_source_hierarchy_datasets(
        self,
        *,
        dataset_template: typing.Union["DatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplate", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param dataset_template: dataset_template block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#dataset_template DatastreamStream#dataset_template}
        '''
        value = DatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasets(
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
    ) -> "DatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDatasetOutputReference":
        return typing.cast("DatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDatasetOutputReference", jsii.get(self, "singleTargetDataset"))

    @builtins.property
    @jsii.member(jsii_name="sourceHierarchyDatasets")
    def source_hierarchy_datasets(
        self,
    ) -> "DatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsOutputReference":
        return typing.cast("DatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsOutputReference", jsii.get(self, "sourceHierarchyDatasets"))

    @builtins.property
    @jsii.member(jsii_name="dataFreshnessInput")
    def data_freshness_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataFreshnessInput"))

    @builtins.property
    @jsii.member(jsii_name="singleTargetDatasetInput")
    def single_target_dataset_input(
        self,
    ) -> typing.Optional["DatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDataset"]:
        return typing.cast(typing.Optional["DatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDataset"], jsii.get(self, "singleTargetDatasetInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceHierarchyDatasetsInput")
    def source_hierarchy_datasets_input(
        self,
    ) -> typing.Optional["DatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasets"]:
        return typing.cast(typing.Optional["DatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasets"], jsii.get(self, "sourceHierarchyDatasetsInput"))

    @builtins.property
    @jsii.member(jsii_name="dataFreshness")
    def data_freshness(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataFreshness"))

    @data_freshness.setter
    def data_freshness(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62b7da575aade1c71be6745c30a44eae934f6539e34ccd51a86b8facf00d5060)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataFreshness", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DatastreamStreamDestinationConfigBigqueryDestinationConfig]:
        return typing.cast(typing.Optional[DatastreamStreamDestinationConfigBigqueryDestinationConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DatastreamStreamDestinationConfigBigqueryDestinationConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10290314eb6f6d825712b6b3207d7da992e62e51fc0be399239f7e7d53e2f846)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.datastreamStream.DatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDataset",
    jsii_struct_bases=[],
    name_mapping={"dataset_id": "datasetId"},
)
class DatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDataset:
    def __init__(self, *, dataset_id: builtins.str) -> None:
        '''
        :param dataset_id: Dataset ID in the format projects/{project}/datasets/{dataset_id}. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#dataset_id DatastreamStream#dataset_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e44dd24643e8aa60468a62619c2ae48ae367e05d23c573afcfa2a6d3a4c91dd)
            check_type(argname="argument dataset_id", value=dataset_id, expected_type=type_hints["dataset_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "dataset_id": dataset_id,
        }

    @builtins.property
    def dataset_id(self) -> builtins.str:
        '''Dataset ID in the format projects/{project}/datasets/{dataset_id}.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#dataset_id DatastreamStream#dataset_id}
        '''
        result = self._values.get("dataset_id")
        assert result is not None, "Required property 'dataset_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDataset(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDatasetOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.datastreamStream.DatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDatasetOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__441adf3b7f63f750260d12b3416082c5faf64d5c7e1832c2a1046cb0a48d5538)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b51999bc75c9b0fd3a12023b18a370bbc03175387133548ee3a57791a877640d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datasetId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDataset]:
        return typing.cast(typing.Optional[DatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDataset], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDataset],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__268f1df491bfb370cbc33b522997f6031a2165748ce5ce4e0e09666537abd721)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.datastreamStream.DatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasets",
    jsii_struct_bases=[],
    name_mapping={"dataset_template": "datasetTemplate"},
)
class DatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasets:
    def __init__(
        self,
        *,
        dataset_template: typing.Union["DatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplate", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param dataset_template: dataset_template block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#dataset_template DatastreamStream#dataset_template}
        '''
        if isinstance(dataset_template, dict):
            dataset_template = DatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplate(**dataset_template)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d309147145fe77e14e6be2ec7f8089a10173d914dfbdb30bdc6fed0fd183a299)
            check_type(argname="argument dataset_template", value=dataset_template, expected_type=type_hints["dataset_template"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "dataset_template": dataset_template,
        }

    @builtins.property
    def dataset_template(
        self,
    ) -> "DatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplate":
        '''dataset_template block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#dataset_template DatastreamStream#dataset_template}
        '''
        result = self._values.get("dataset_template")
        assert result is not None, "Required property 'dataset_template' is missing"
        return typing.cast("DatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplate", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasets(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google.datastreamStream.DatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplate",
    jsii_struct_bases=[],
    name_mapping={"location": "location", "dataset_id_prefix": "datasetIdPrefix"},
)
class DatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplate:
    def __init__(
        self,
        *,
        location: builtins.str,
        dataset_id_prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param location: The geographic location where the dataset should reside. See https://cloud.google.com/bigquery/docs/locations for supported locations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#location DatastreamStream#location}
        :param dataset_id_prefix: If supplied, every created dataset will have its name prefixed by the provided value. The prefix and name will be separated by an underscore. i.e. _. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#dataset_id_prefix DatastreamStream#dataset_id_prefix}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21923ae44eb0f0bb463b3690f3b8ab6ee48575a23420bfc03244d26df8ce50fc)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#location DatastreamStream#location}
        '''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dataset_id_prefix(self) -> typing.Optional[builtins.str]:
        '''If supplied, every created dataset will have its name prefixed by the provided value.

        The prefix and name will be separated by an underscore. i.e. _.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#dataset_id_prefix DatastreamStream#dataset_id_prefix}
        '''
        result = self._values.get("dataset_id_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplateOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.datastreamStream.DatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplateOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7f3e1a71a02260fed7254d25a21729daa348bde759c05a201e378a1427397ba5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b12137ad883f1e8198a7e8a9d33112667f3a9d542fe239263ff41c443ac959f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datasetIdPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7f6a99aaed1e86235d35130b250c4ef94bbb8b532409fcb8b414027c2e8f90f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplate]:
        return typing.cast(typing.Optional[DatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplate], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplate],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d649ea10fa687d496860280b0eb24cd52cc782d27783590f0680bfa4689aa1c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.datastreamStream.DatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__57dd2ede080c713c2f1230e7c848e67a25284bcfc9dddcff5c0399b99b877959)
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
        :param location: The geographic location where the dataset should reside. See https://cloud.google.com/bigquery/docs/locations for supported locations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#location DatastreamStream#location}
        :param dataset_id_prefix: If supplied, every created dataset will have its name prefixed by the provided value. The prefix and name will be separated by an underscore. i.e. _. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#dataset_id_prefix DatastreamStream#dataset_id_prefix}
        '''
        value = DatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplate(
            location=location, dataset_id_prefix=dataset_id_prefix
        )

        return typing.cast(None, jsii.invoke(self, "putDatasetTemplate", [value]))

    @builtins.property
    @jsii.member(jsii_name="datasetTemplate")
    def dataset_template(
        self,
    ) -> DatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplateOutputReference:
        return typing.cast(DatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplateOutputReference, jsii.get(self, "datasetTemplate"))

    @builtins.property
    @jsii.member(jsii_name="datasetTemplateInput")
    def dataset_template_input(
        self,
    ) -> typing.Optional[DatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplate]:
        return typing.cast(typing.Optional[DatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplate], jsii.get(self, "datasetTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasets]:
        return typing.cast(typing.Optional[DatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasets], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasets],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ca05e8ee9521ac9812e47448dd7ed280d2aded497ee45b96dd7daca59deabbe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.datastreamStream.DatastreamStreamDestinationConfigGcsDestinationConfig",
    jsii_struct_bases=[],
    name_mapping={
        "avro_file_format": "avroFileFormat",
        "file_rotation_interval": "fileRotationInterval",
        "file_rotation_mb": "fileRotationMb",
        "json_file_format": "jsonFileFormat",
        "path": "path",
    },
)
class DatastreamStreamDestinationConfigGcsDestinationConfig:
    def __init__(
        self,
        *,
        avro_file_format: typing.Optional[typing.Union["DatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormat", typing.Dict[builtins.str, typing.Any]]] = None,
        file_rotation_interval: typing.Optional[builtins.str] = None,
        file_rotation_mb: typing.Optional[jsii.Number] = None,
        json_file_format: typing.Optional[typing.Union["DatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormat", typing.Dict[builtins.str, typing.Any]]] = None,
        path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param avro_file_format: avro_file_format block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#avro_file_format DatastreamStream#avro_file_format}
        :param file_rotation_interval: The maximum duration for which new events are added before a file is closed and a new file is created. A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s". Defaults to 900s. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#file_rotation_interval DatastreamStream#file_rotation_interval}
        :param file_rotation_mb: The maximum file size to be saved in the bucket. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#file_rotation_mb DatastreamStream#file_rotation_mb}
        :param json_file_format: json_file_format block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#json_file_format DatastreamStream#json_file_format}
        :param path: Path inside the Cloud Storage bucket to write data to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#path DatastreamStream#path}
        '''
        if isinstance(avro_file_format, dict):
            avro_file_format = DatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormat(**avro_file_format)
        if isinstance(json_file_format, dict):
            json_file_format = DatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormat(**json_file_format)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff6fe7bc7051957d6ef5b4a2c8ba1b43b7844b9948287f7a5f36e8a41e8cc412)
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
    ) -> typing.Optional["DatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormat"]:
        '''avro_file_format block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#avro_file_format DatastreamStream#avro_file_format}
        '''
        result = self._values.get("avro_file_format")
        return typing.cast(typing.Optional["DatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormat"], result)

    @builtins.property
    def file_rotation_interval(self) -> typing.Optional[builtins.str]:
        '''The maximum duration for which new events are added before a file is closed and a new file is created.

        A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s". Defaults to 900s.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#file_rotation_interval DatastreamStream#file_rotation_interval}
        '''
        result = self._values.get("file_rotation_interval")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def file_rotation_mb(self) -> typing.Optional[jsii.Number]:
        '''The maximum file size to be saved in the bucket.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#file_rotation_mb DatastreamStream#file_rotation_mb}
        '''
        result = self._values.get("file_rotation_mb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def json_file_format(
        self,
    ) -> typing.Optional["DatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormat"]:
        '''json_file_format block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#json_file_format DatastreamStream#json_file_format}
        '''
        result = self._values.get("json_file_format")
        return typing.cast(typing.Optional["DatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormat"], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Path inside the Cloud Storage bucket to write data to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#path DatastreamStream#path}
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatastreamStreamDestinationConfigGcsDestinationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google.datastreamStream.DatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormat",
    jsii_struct_bases=[],
    name_mapping={},
)
class DatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormat:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormat(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormatOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.datastreamStream.DatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormatOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__53992334d0a36b22747670910ec781eeb695714367669655fdf9bf4af1963833)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormat]:
        return typing.cast(typing.Optional[DatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormat], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormat],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afaa1094b2bf96eb2aaa9a004fc98a4308a6190a94060ab74654bb2b416c437a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.datastreamStream.DatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormat",
    jsii_struct_bases=[],
    name_mapping={
        "compression": "compression",
        "schema_file_format": "schemaFileFormat",
    },
)
class DatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormat:
    def __init__(
        self,
        *,
        compression: typing.Optional[builtins.str] = None,
        schema_file_format: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param compression: Compression of the loaded JSON file. Possible values: ["NO_COMPRESSION", "GZIP"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#compression DatastreamStream#compression}
        :param schema_file_format: The schema file format along JSON data files. Possible values: ["NO_SCHEMA_FILE", "AVRO_SCHEMA_FILE"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#schema_file_format DatastreamStream#schema_file_format}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5c14e2cab90478a730fd4d9ac6ca6c8d7ba3f67ff802f4dcd2d5c9c08fb9803)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#compression DatastreamStream#compression}
        '''
        result = self._values.get("compression")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schema_file_format(self) -> typing.Optional[builtins.str]:
        '''The schema file format along JSON data files. Possible values: ["NO_SCHEMA_FILE", "AVRO_SCHEMA_FILE"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#schema_file_format DatastreamStream#schema_file_format}
        '''
        result = self._values.get("schema_file_format")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormat(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormatOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.datastreamStream.DatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormatOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__03cf334b7c9b733612b8ea0e5a5a7807c143ca675f4524c8a5e0e7755406bd56)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ded649c1e18a3afe723a46d8ef0cf7b3bd23261d1183fd169e1f378122c2eef7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "compression", value)

    @builtins.property
    @jsii.member(jsii_name="schemaFileFormat")
    def schema_file_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schemaFileFormat"))

    @schema_file_format.setter
    def schema_file_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4267f271d814121eca55dad65d9c3869f72e7c0df0c37798d71a0517c8e56d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schemaFileFormat", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormat]:
        return typing.cast(typing.Optional[DatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormat], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormat],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69a0efe2299c605431235b27746ddef41abdcec0e56eac6382ae8204a6a451f0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DatastreamStreamDestinationConfigGcsDestinationConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.datastreamStream.DatastreamStreamDestinationConfigGcsDestinationConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__db9a6d5e7f6df721016eecca5688540ca539f31acd6bda59a8493f4c20acd453)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAvroFileFormat")
    def put_avro_file_format(self) -> None:
        value = DatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormat()

        return typing.cast(None, jsii.invoke(self, "putAvroFileFormat", [value]))

    @jsii.member(jsii_name="putJsonFileFormat")
    def put_json_file_format(
        self,
        *,
        compression: typing.Optional[builtins.str] = None,
        schema_file_format: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param compression: Compression of the loaded JSON file. Possible values: ["NO_COMPRESSION", "GZIP"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#compression DatastreamStream#compression}
        :param schema_file_format: The schema file format along JSON data files. Possible values: ["NO_SCHEMA_FILE", "AVRO_SCHEMA_FILE"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#schema_file_format DatastreamStream#schema_file_format}
        '''
        value = DatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormat(
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
    ) -> DatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormatOutputReference:
        return typing.cast(DatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormatOutputReference, jsii.get(self, "avroFileFormat"))

    @builtins.property
    @jsii.member(jsii_name="jsonFileFormat")
    def json_file_format(
        self,
    ) -> DatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormatOutputReference:
        return typing.cast(DatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormatOutputReference, jsii.get(self, "jsonFileFormat"))

    @builtins.property
    @jsii.member(jsii_name="avroFileFormatInput")
    def avro_file_format_input(
        self,
    ) -> typing.Optional[DatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormat]:
        return typing.cast(typing.Optional[DatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormat], jsii.get(self, "avroFileFormatInput"))

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
    ) -> typing.Optional[DatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormat]:
        return typing.cast(typing.Optional[DatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormat], jsii.get(self, "jsonFileFormatInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__97148b45365aadc2e39b6e2e4fccc374cdbca79b05f3f52571e08319d4ee9036)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileRotationInterval", value)

    @builtins.property
    @jsii.member(jsii_name="fileRotationMb")
    def file_rotation_mb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "fileRotationMb"))

    @file_rotation_mb.setter
    def file_rotation_mb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fae1649d074402474b5d7bd00712aabfc874730cfff03823ae354457233f2608)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileRotationMb", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f182119df80ece606c9383959c86ab83e4448a8f8744859baad283fd405e45d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DatastreamStreamDestinationConfigGcsDestinationConfig]:
        return typing.cast(typing.Optional[DatastreamStreamDestinationConfigGcsDestinationConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DatastreamStreamDestinationConfigGcsDestinationConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f01a9c52ede76f92056982b7da315f974384e0fb43ded2f1d40f4d8e1832207)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DatastreamStreamDestinationConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.datastreamStream.DatastreamStreamDestinationConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f46069e1a4d2de7a3c29ede9cae6610ea00fcde99ec2ae63eab68dc303a751c0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putBigqueryDestinationConfig")
    def put_bigquery_destination_config(
        self,
        *,
        data_freshness: typing.Optional[builtins.str] = None,
        single_target_dataset: typing.Optional[typing.Union[DatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDataset, typing.Dict[builtins.str, typing.Any]]] = None,
        source_hierarchy_datasets: typing.Optional[typing.Union[DatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasets, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param data_freshness: The guaranteed data freshness (in seconds) when querying tables created by the stream. Editing this field will only affect new tables created in the future, but existing tables will not be impacted. Lower values mean that queries will return fresher data, but may result in higher cost. A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s". Defaults to 900s. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#data_freshness DatastreamStream#data_freshness}
        :param single_target_dataset: single_target_dataset block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#single_target_dataset DatastreamStream#single_target_dataset}
        :param source_hierarchy_datasets: source_hierarchy_datasets block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#source_hierarchy_datasets DatastreamStream#source_hierarchy_datasets}
        '''
        value = DatastreamStreamDestinationConfigBigqueryDestinationConfig(
            data_freshness=data_freshness,
            single_target_dataset=single_target_dataset,
            source_hierarchy_datasets=source_hierarchy_datasets,
        )

        return typing.cast(None, jsii.invoke(self, "putBigqueryDestinationConfig", [value]))

    @jsii.member(jsii_name="putGcsDestinationConfig")
    def put_gcs_destination_config(
        self,
        *,
        avro_file_format: typing.Optional[typing.Union[DatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormat, typing.Dict[builtins.str, typing.Any]]] = None,
        file_rotation_interval: typing.Optional[builtins.str] = None,
        file_rotation_mb: typing.Optional[jsii.Number] = None,
        json_file_format: typing.Optional[typing.Union[DatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormat, typing.Dict[builtins.str, typing.Any]]] = None,
        path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param avro_file_format: avro_file_format block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#avro_file_format DatastreamStream#avro_file_format}
        :param file_rotation_interval: The maximum duration for which new events are added before a file is closed and a new file is created. A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s". Defaults to 900s. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#file_rotation_interval DatastreamStream#file_rotation_interval}
        :param file_rotation_mb: The maximum file size to be saved in the bucket. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#file_rotation_mb DatastreamStream#file_rotation_mb}
        :param json_file_format: json_file_format block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#json_file_format DatastreamStream#json_file_format}
        :param path: Path inside the Cloud Storage bucket to write data to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#path DatastreamStream#path}
        '''
        value = DatastreamStreamDestinationConfigGcsDestinationConfig(
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
    ) -> DatastreamStreamDestinationConfigBigqueryDestinationConfigOutputReference:
        return typing.cast(DatastreamStreamDestinationConfigBigqueryDestinationConfigOutputReference, jsii.get(self, "bigqueryDestinationConfig"))

    @builtins.property
    @jsii.member(jsii_name="gcsDestinationConfig")
    def gcs_destination_config(
        self,
    ) -> DatastreamStreamDestinationConfigGcsDestinationConfigOutputReference:
        return typing.cast(DatastreamStreamDestinationConfigGcsDestinationConfigOutputReference, jsii.get(self, "gcsDestinationConfig"))

    @builtins.property
    @jsii.member(jsii_name="bigqueryDestinationConfigInput")
    def bigquery_destination_config_input(
        self,
    ) -> typing.Optional[DatastreamStreamDestinationConfigBigqueryDestinationConfig]:
        return typing.cast(typing.Optional[DatastreamStreamDestinationConfigBigqueryDestinationConfig], jsii.get(self, "bigqueryDestinationConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationConnectionProfileInput")
    def destination_connection_profile_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationConnectionProfileInput"))

    @builtins.property
    @jsii.member(jsii_name="gcsDestinationConfigInput")
    def gcs_destination_config_input(
        self,
    ) -> typing.Optional[DatastreamStreamDestinationConfigGcsDestinationConfig]:
        return typing.cast(typing.Optional[DatastreamStreamDestinationConfigGcsDestinationConfig], jsii.get(self, "gcsDestinationConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationConnectionProfile")
    def destination_connection_profile(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destinationConnectionProfile"))

    @destination_connection_profile.setter
    def destination_connection_profile(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07c51932c7c579a452dfb4bd688f68fa8208002be445062eda4e86430be29b96)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationConnectionProfile", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DatastreamStreamDestinationConfig]:
        return typing.cast(typing.Optional[DatastreamStreamDestinationConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DatastreamStreamDestinationConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c94d7479b7d04eadd4b49a8a517d1d766123d5a712238cd25314c50439da47d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.datastreamStream.DatastreamStreamSourceConfig",
    jsii_struct_bases=[],
    name_mapping={
        "mysql_source_config": "mysqlSourceConfig",
        "source_connection_profile": "sourceConnectionProfile",
    },
)
class DatastreamStreamSourceConfig:
    def __init__(
        self,
        *,
        mysql_source_config: typing.Union["DatastreamStreamSourceConfigMysqlSourceConfig", typing.Dict[builtins.str, typing.Any]],
        source_connection_profile: builtins.str,
    ) -> None:
        '''
        :param mysql_source_config: mysql_source_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#mysql_source_config DatastreamStream#mysql_source_config}
        :param source_connection_profile: Source connection profile resource. Format: projects/{project}/locations/{location}/connectionProfiles/{name}. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#source_connection_profile DatastreamStream#source_connection_profile}
        '''
        if isinstance(mysql_source_config, dict):
            mysql_source_config = DatastreamStreamSourceConfigMysqlSourceConfig(**mysql_source_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__995aa3d40c0014eb42472704f6e2a586227929c23daf612b5bc02630f522ee9c)
            check_type(argname="argument mysql_source_config", value=mysql_source_config, expected_type=type_hints["mysql_source_config"])
            check_type(argname="argument source_connection_profile", value=source_connection_profile, expected_type=type_hints["source_connection_profile"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "mysql_source_config": mysql_source_config,
            "source_connection_profile": source_connection_profile,
        }

    @builtins.property
    def mysql_source_config(self) -> "DatastreamStreamSourceConfigMysqlSourceConfig":
        '''mysql_source_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#mysql_source_config DatastreamStream#mysql_source_config}
        '''
        result = self._values.get("mysql_source_config")
        assert result is not None, "Required property 'mysql_source_config' is missing"
        return typing.cast("DatastreamStreamSourceConfigMysqlSourceConfig", result)

    @builtins.property
    def source_connection_profile(self) -> builtins.str:
        '''Source connection profile resource. Format: projects/{project}/locations/{location}/connectionProfiles/{name}.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#source_connection_profile DatastreamStream#source_connection_profile}
        '''
        result = self._values.get("source_connection_profile")
        assert result is not None, "Required property 'source_connection_profile' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatastreamStreamSourceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google.datastreamStream.DatastreamStreamSourceConfigMysqlSourceConfig",
    jsii_struct_bases=[],
    name_mapping={
        "exclude_objects": "excludeObjects",
        "include_objects": "includeObjects",
        "max_concurrent_cdc_tasks": "maxConcurrentCdcTasks",
    },
)
class DatastreamStreamSourceConfigMysqlSourceConfig:
    def __init__(
        self,
        *,
        exclude_objects: typing.Optional[typing.Union["DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjects", typing.Dict[builtins.str, typing.Any]]] = None,
        include_objects: typing.Optional[typing.Union["DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjects", typing.Dict[builtins.str, typing.Any]]] = None,
        max_concurrent_cdc_tasks: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param exclude_objects: exclude_objects block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#exclude_objects DatastreamStream#exclude_objects}
        :param include_objects: include_objects block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#include_objects DatastreamStream#include_objects}
        :param max_concurrent_cdc_tasks: Maximum number of concurrent CDC tasks. The number should be non negative. If not set (or set to 0), the system's default value will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#max_concurrent_cdc_tasks DatastreamStream#max_concurrent_cdc_tasks}
        '''
        if isinstance(exclude_objects, dict):
            exclude_objects = DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjects(**exclude_objects)
        if isinstance(include_objects, dict):
            include_objects = DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjects(**include_objects)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03986ed8942ca5af140f857a63fa4f9bf36dc4bc0034824c870a09ee77f3377f)
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
    ) -> typing.Optional["DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjects"]:
        '''exclude_objects block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#exclude_objects DatastreamStream#exclude_objects}
        '''
        result = self._values.get("exclude_objects")
        return typing.cast(typing.Optional["DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjects"], result)

    @builtins.property
    def include_objects(
        self,
    ) -> typing.Optional["DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjects"]:
        '''include_objects block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#include_objects DatastreamStream#include_objects}
        '''
        result = self._values.get("include_objects")
        return typing.cast(typing.Optional["DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjects"], result)

    @builtins.property
    def max_concurrent_cdc_tasks(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of concurrent CDC tasks.

        The number should be non negative.
        If not set (or set to 0), the system's default value will be used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#max_concurrent_cdc_tasks DatastreamStream#max_concurrent_cdc_tasks}
        '''
        result = self._values.get("max_concurrent_cdc_tasks")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatastreamStreamSourceConfigMysqlSourceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google.datastreamStream.DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjects",
    jsii_struct_bases=[],
    name_mapping={"mysql_databases": "mysqlDatabases"},
)
class DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjects:
    def __init__(
        self,
        *,
        mysql_databases: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabases", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param mysql_databases: mysql_databases block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#mysql_databases DatastreamStream#mysql_databases}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd8924ba08b53e76420d1040aea7107d9f8f4a35a42d203306a4dc5eef847746)
            check_type(argname="argument mysql_databases", value=mysql_databases, expected_type=type_hints["mysql_databases"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "mysql_databases": mysql_databases,
        }

    @builtins.property
    def mysql_databases(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabases"]]:
        '''mysql_databases block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#mysql_databases DatastreamStream#mysql_databases}
        '''
        result = self._values.get("mysql_databases")
        assert result is not None, "Required property 'mysql_databases' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabases"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjects(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google.datastreamStream.DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabases",
    jsii_struct_bases=[],
    name_mapping={"database": "database", "mysql_tables": "mysqlTables"},
)
class DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabases:
    def __init__(
        self,
        *,
        database: builtins.str,
        mysql_tables: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTables", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param database: Database name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#database DatastreamStream#database}
        :param mysql_tables: mysql_tables block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#mysql_tables DatastreamStream#mysql_tables}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__47003e7f3dfe4568bdfbecbecdfeca8cc5c1dc824fd507147bcf69d0e11c8907)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#database DatastreamStream#database}
        '''
        result = self._values.get("database")
        assert result is not None, "Required property 'database' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def mysql_tables(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTables"]]]:
        '''mysql_tables block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#mysql_tables DatastreamStream#mysql_tables}
        '''
        result = self._values.get("mysql_tables")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTables"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabases(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.datastreamStream.DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6ad30ac80003dfb56e29240af179446ad988b2d56141cc9ac9173a417b271330)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03e3be48b4d7ea91ea507468b666eb92e908b90eaa4b72909e6e563ba639959a)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82d098f2c688f84fafc6dd0afd35bf6d5c61a2a9469a607a83c9f3adea7ec6a1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__af2024f15ee7b08a23d14347a6bf4886348cdd4fe08b134d84d142af2d64b50b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__87c0d3373e4a860d69ba9b1b96343c0a1a37400cad0c26a35d9976a03a2abbcf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabases]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabases]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabases]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2195e2190f719cbe019609d3ec53f80debd66c7511eec9350b50efae0d491363)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.datastreamStream.DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTables",
    jsii_struct_bases=[],
    name_mapping={"table": "table", "mysql_columns": "mysqlColumns"},
)
class DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTables:
    def __init__(
        self,
        *,
        table: builtins.str,
        mysql_columns: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumns", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param table: Table name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#table DatastreamStream#table}
        :param mysql_columns: mysql_columns block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#mysql_columns DatastreamStream#mysql_columns}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36fef275c6ec7b8d609cafa0d2641bd263c44a10bc7249473f713a05683ba4f4)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#table DatastreamStream#table}
        '''
        result = self._values.get("table")
        assert result is not None, "Required property 'table' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def mysql_columns(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumns"]]]:
        '''mysql_columns block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#mysql_columns DatastreamStream#mysql_columns}
        '''
        result = self._values.get("mysql_columns")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumns"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTables(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.datastreamStream.DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__69c33a987c9a7ecb67924cb1032a96cc931edf369e360ae95e58e1551d69b163)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2137ca458d7db27e59eaa11790cf81f0760027a1075e78cbd3fd912b7fdbfe53)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b152c3de915d6fc96d08112f4da3d2632e4a1feb8ed9a6e739b1e322d056eba)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9761d0c70fb470dda84cafcf21d16c981695392477d4566b2b58631c6a17a85c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e35fc4adff6fe3aeb36b4c144ff1bef8d8bfec907ca5fe8808db292d4698d710)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTables]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTables]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTables]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf3b7e194a1b17a44374dff58788f3134ef276f1b232460d9f088bc36c194fbf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.datastreamStream.DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumns",
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
class DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumns:
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
        :param collation: Column collation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#collation DatastreamStream#collation}
        :param column: Column name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#column DatastreamStream#column}
        :param data_type: The MySQL data type. Full data types list can be found here: https://dev.mysql.com/doc/refman/8.0/en/data-types.html. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#data_type DatastreamStream#data_type}
        :param nullable: Whether or not the column can accept a null value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#nullable DatastreamStream#nullable}
        :param ordinal_position: The ordinal position of the column in the table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#ordinal_position DatastreamStream#ordinal_position}
        :param primary_key: Whether or not the column represents a primary key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#primary_key DatastreamStream#primary_key}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa1d840e397f01a70c2cddb58c957e80c59d39fb16bbea2a1c04910d8abb0218)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#collation DatastreamStream#collation}
        '''
        result = self._values.get("collation")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def column(self) -> typing.Optional[builtins.str]:
        '''Column name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#column DatastreamStream#column}
        '''
        result = self._values.get("column")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_type(self) -> typing.Optional[builtins.str]:
        '''The MySQL data type. Full data types list can be found here: https://dev.mysql.com/doc/refman/8.0/en/data-types.html.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#data_type DatastreamStream#data_type}
        '''
        result = self._values.get("data_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def nullable(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether or not the column can accept a null value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#nullable DatastreamStream#nullable}
        '''
        result = self._values.get("nullable")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def ordinal_position(self) -> typing.Optional[jsii.Number]:
        '''The ordinal position of the column in the table.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#ordinal_position DatastreamStream#ordinal_position}
        '''
        result = self._values.get("ordinal_position")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def primary_key(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether or not the column represents a primary key.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#primary_key DatastreamStream#primary_key}
        '''
        result = self._values.get("primary_key")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumns(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumnsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.datastreamStream.DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumnsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b934e1cd2f1b6e46749d3a3ee4ea123a5feab018bcbd9e1dc3d82577fc52b54d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumnsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b0462a33c37e557fcf3c2fd74887a5508dff56bcde35fa593f04f4b8607580c)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumnsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23b5fb04fe528246556f11f40ffb8e2ce0da1af40d4741f1ba0bc113654bb796)
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
            type_hints = typing.get_type_hints(_typecheckingstub__30ff55614afd8ecea5a474c3db78ec06d5d81fc6e8371a0cc4fb16372f124bf1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ad32f42f77fac61d1715b212cb332883b311819b8cd438d36beb15bde86030dc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumns]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumns]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumns]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9320334886970de6c5ea55c48a2818daa32156be2f9f75dd5e042a36ad100d27)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumnsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.datastreamStream.DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumnsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5bc27762ed3847a2a4997c6417d746b2344e6ce7b9e40d4295c780394da67d35)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f10c35f21ec76d9b9b6f802e3565c8ba67ffd07a03db61a1a05cab01b31b5cd1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "collation", value)

    @builtins.property
    @jsii.member(jsii_name="column")
    def column(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "column"))

    @column.setter
    def column(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5e84862d7e010156638f260885c74211c45e9be7238c8249465e6db2a06d368)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "column", value)

    @builtins.property
    @jsii.member(jsii_name="dataType")
    def data_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataType"))

    @data_type.setter
    def data_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84a4831ac66409ce770fc99b6de33638206edf8c50979ecf8d0cc42c7b84f450)
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
            type_hints = typing.get_type_hints(_typecheckingstub__600dbdaafece9c5dbfc122b3a1509faf6dc3db4dd21050d0da9936f77db7d0e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nullable", value)

    @builtins.property
    @jsii.member(jsii_name="ordinalPosition")
    def ordinal_position(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ordinalPosition"))

    @ordinal_position.setter
    def ordinal_position(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96f73fe59063cff45a5fabe46cc5ef9301038e2ca51363160acfdd6ff6a518a7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__64b2a7fe0df84f84031671b52e419f6be035d371a5bfd7fa6e4eed2354f0730f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "primaryKey", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumns, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumns, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumns, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b2f92998ae8b6c8fd59179b9167917d5e06e3da0bf7f6a17d89c1a9d34958d9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.datastreamStream.DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__74c7edf517db15210471252d18fb4c0295e1f6d17ac794c71b59dad9fa34cde3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putMysqlColumns")
    def put_mysql_columns(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumns, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2a0c2eed43d5a92c7dd35f9d3b898447ed32f9260596e554f0bf82139dabb27)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMysqlColumns", [value]))

    @jsii.member(jsii_name="resetMysqlColumns")
    def reset_mysql_columns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMysqlColumns", []))

    @builtins.property
    @jsii.member(jsii_name="mysqlColumns")
    def mysql_columns(
        self,
    ) -> DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumnsList:
        return typing.cast(DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumnsList, jsii.get(self, "mysqlColumns"))

    @builtins.property
    @jsii.member(jsii_name="mysqlColumnsInput")
    def mysql_columns_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumns]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumns]]], jsii.get(self, "mysqlColumnsInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__8a802aba7a80609e781d874483717985a77c791a6d610d086e56342e5ebdfea4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "table", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTables, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTables, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTables, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81a3c95f2945ef79610f226e7de8f82f4dd6c488b2cdea201b5adee9eb165a18)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.datastreamStream.DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__339d0233b5e3939582ec717c6235f70b3bcfce5011c933d1fa7b7b221a1b3f98)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putMysqlTables")
    def put_mysql_tables(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTables, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00e753886968f6ad8529639aad8ba094d4d936e8fb59d04017d16679362ce906)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMysqlTables", [value]))

    @jsii.member(jsii_name="resetMysqlTables")
    def reset_mysql_tables(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMysqlTables", []))

    @builtins.property
    @jsii.member(jsii_name="mysqlTables")
    def mysql_tables(
        self,
    ) -> DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesList:
        return typing.cast(DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesList, jsii.get(self, "mysqlTables"))

    @builtins.property
    @jsii.member(jsii_name="databaseInput")
    def database_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseInput"))

    @builtins.property
    @jsii.member(jsii_name="mysqlTablesInput")
    def mysql_tables_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTables]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTables]]], jsii.get(self, "mysqlTablesInput"))

    @builtins.property
    @jsii.member(jsii_name="database")
    def database(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "database"))

    @database.setter
    def database(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7ddba99321e758ecfffe491c01f502472c59352bb67f1530bbaea001f0a7062)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "database", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabases, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabases, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabases, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e753e427d29d0ade6f4009149848849060b763be17e45608a15cca438775be09)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.datastreamStream.DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__93d8c032e45bf0ac57ac3d0979da5b6ffe8c1f99b09476d82280a9af84df9c6d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMysqlDatabases")
    def put_mysql_databases(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabases, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc57f764ac9d739ecc943fad16909c32b76e6c97dea9a5df494ab6c104e29123)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMysqlDatabases", [value]))

    @builtins.property
    @jsii.member(jsii_name="mysqlDatabases")
    def mysql_databases(
        self,
    ) -> DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesList:
        return typing.cast(DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesList, jsii.get(self, "mysqlDatabases"))

    @builtins.property
    @jsii.member(jsii_name="mysqlDatabasesInput")
    def mysql_databases_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabases]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabases]]], jsii.get(self, "mysqlDatabasesInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjects]:
        return typing.cast(typing.Optional[DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjects], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjects],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72b7210b8484ca8aea5f7a6f1596f56ef4c03fe2c76a48dee6597741f3c6ff5b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.datastreamStream.DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjects",
    jsii_struct_bases=[],
    name_mapping={"mysql_databases": "mysqlDatabases"},
)
class DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjects:
    def __init__(
        self,
        *,
        mysql_databases: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabases", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param mysql_databases: mysql_databases block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#mysql_databases DatastreamStream#mysql_databases}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40db11a5bb1c2aca7472fd834428a2203489803a28b44b1e4962ad4ab1b66159)
            check_type(argname="argument mysql_databases", value=mysql_databases, expected_type=type_hints["mysql_databases"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "mysql_databases": mysql_databases,
        }

    @builtins.property
    def mysql_databases(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabases"]]:
        '''mysql_databases block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#mysql_databases DatastreamStream#mysql_databases}
        '''
        result = self._values.get("mysql_databases")
        assert result is not None, "Required property 'mysql_databases' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabases"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjects(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google.datastreamStream.DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabases",
    jsii_struct_bases=[],
    name_mapping={"database": "database", "mysql_tables": "mysqlTables"},
)
class DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabases:
    def __init__(
        self,
        *,
        database: builtins.str,
        mysql_tables: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTables", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param database: Database name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#database DatastreamStream#database}
        :param mysql_tables: mysql_tables block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#mysql_tables DatastreamStream#mysql_tables}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ff4d778c3932f51b621c3ff1675a74882c85bb24341f2bf1594c06d9c82f36f)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#database DatastreamStream#database}
        '''
        result = self._values.get("database")
        assert result is not None, "Required property 'database' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def mysql_tables(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTables"]]]:
        '''mysql_tables block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#mysql_tables DatastreamStream#mysql_tables}
        '''
        result = self._values.get("mysql_tables")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTables"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabases(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.datastreamStream.DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ade2a69c288d1345efb3bb511b247830dfd4432c1cd9cbefcabf6c9078c58dc5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__264cc6b382219d468fd08c237199dbe2f9c342a7f5890d61df2f62ee150f6ee4)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43dfcfbaa01fb883388f2b178ba7a5408a426f709176123962218ff85fdb5262)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9a3c66c27ba53c72edcb3b6f85cf2f84f3bd4afd152aa8d8bbdce895bca382e5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__824badd6fb7e5f770535729d1e915a227b98a14597f969bc12aaf2635f49b992)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabases]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabases]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabases]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec8b65c0e93aeb7913ed2a822757e31ec88018bc0633b32238f9b6ad54df3bab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.datastreamStream.DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTables",
    jsii_struct_bases=[],
    name_mapping={"table": "table", "mysql_columns": "mysqlColumns"},
)
class DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTables:
    def __init__(
        self,
        *,
        table: builtins.str,
        mysql_columns: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumns", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param table: Table name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#table DatastreamStream#table}
        :param mysql_columns: mysql_columns block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#mysql_columns DatastreamStream#mysql_columns}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91f8c103e5beb0d973e5d209018bdb2893707dc54045bf4164625d73468a4327)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#table DatastreamStream#table}
        '''
        result = self._values.get("table")
        assert result is not None, "Required property 'table' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def mysql_columns(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumns"]]]:
        '''mysql_columns block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#mysql_columns DatastreamStream#mysql_columns}
        '''
        result = self._values.get("mysql_columns")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumns"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTables(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.datastreamStream.DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1f2ae67802bc4d46269f15e251ca61b00cd7e6cc4c72696f5ef1e117bd0b9351)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba47fc823bc86f85b46f3c7d66c7ef36e848bf6a8f9d4e4e4ec74485144daaa4)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96c60478bf9cf99a40bd62622ba84b3b4844306f809ead2f0c86eb8fe301fc9d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__72e164afb7b4632e6e21ba9fe40e4060ded214f779343520f8ae627e64f6c416)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b4fba8425facced2e35d16bc08d9f9df4a3cfe6e09828f27fbfdcbf3a5ec6751)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTables]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTables]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTables]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__811d23977ea46d8bb808a32e998c0cdeec1202920f1232c14e3d4e536d8f9934)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.datastreamStream.DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumns",
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
class DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumns:
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
        :param collation: Column collation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#collation DatastreamStream#collation}
        :param column: Column name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#column DatastreamStream#column}
        :param data_type: The MySQL data type. Full data types list can be found here: https://dev.mysql.com/doc/refman/8.0/en/data-types.html. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#data_type DatastreamStream#data_type}
        :param nullable: Whether or not the column can accept a null value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#nullable DatastreamStream#nullable}
        :param ordinal_position: The ordinal position of the column in the table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#ordinal_position DatastreamStream#ordinal_position}
        :param primary_key: Whether or not the column represents a primary key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#primary_key DatastreamStream#primary_key}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6b2437de5afb4d3d3062eedf288787c94f774d386adc5570fd611e7a929e190)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#collation DatastreamStream#collation}
        '''
        result = self._values.get("collation")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def column(self) -> typing.Optional[builtins.str]:
        '''Column name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#column DatastreamStream#column}
        '''
        result = self._values.get("column")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_type(self) -> typing.Optional[builtins.str]:
        '''The MySQL data type. Full data types list can be found here: https://dev.mysql.com/doc/refman/8.0/en/data-types.html.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#data_type DatastreamStream#data_type}
        '''
        result = self._values.get("data_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def nullable(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether or not the column can accept a null value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#nullable DatastreamStream#nullable}
        '''
        result = self._values.get("nullable")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def ordinal_position(self) -> typing.Optional[jsii.Number]:
        '''The ordinal position of the column in the table.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#ordinal_position DatastreamStream#ordinal_position}
        '''
        result = self._values.get("ordinal_position")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def primary_key(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether or not the column represents a primary key.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#primary_key DatastreamStream#primary_key}
        '''
        result = self._values.get("primary_key")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumns(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumnsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.datastreamStream.DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumnsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__37248826856ca9dfb4e91cb36937cd1b038e5edac9cce3f3be797f674e6933ca)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumnsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c227d69d63e5037e72560f8cfe9e7b04578befbe5130eed9150a61b587d3a0f)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumnsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59c1f9241ec90839a4e9c7459608fec5eb625c2fb68430051ad1689fdad8eb56)
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
            type_hints = typing.get_type_hints(_typecheckingstub__25ca7dd00f97fbe18a2c49875f68a9eae6a6255a559ad69db9a3ee209ef6192b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__473f5e905f2848a2ccb19b790fd4c15eea0c52576954c9e7e48a8935c5db34a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumns]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumns]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumns]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37b258a7501901c9867024fa4f2c4c003140669bebbfe47678087094d1c19ec1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumnsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.datastreamStream.DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumnsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a2c5f7ad9b605e87fa3c703004388f9d973ac9b1e61d381ca0e122e420260396)
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
            type_hints = typing.get_type_hints(_typecheckingstub__18623f5e4a5f5e41edc82a5f6793879500c107969e69faabe743ec280dd16351)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "collation", value)

    @builtins.property
    @jsii.member(jsii_name="column")
    def column(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "column"))

    @column.setter
    def column(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8aed8cbdee483c61be882e1558fc23ea2e3a910b66185dfcf543429f50ddb176)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "column", value)

    @builtins.property
    @jsii.member(jsii_name="dataType")
    def data_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataType"))

    @data_type.setter
    def data_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__812c5406870508b7dcac28e9456b090b4d1f89406cc88a2040c859c09e71567a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2aec533a8ba2c7f9ab6215ed1c075b98a28fec4443e3ca719d34ffa4e7ecfdd4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nullable", value)

    @builtins.property
    @jsii.member(jsii_name="ordinalPosition")
    def ordinal_position(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ordinalPosition"))

    @ordinal_position.setter
    def ordinal_position(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f8982e4523ee32bb9d8365de4142ceb42cf0144c0a45c49e41ef9accfc902e1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ab7726d162a19d90a4da0f120eca91dc0bb17ff7e32bd9045dda1f36ab000b80)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "primaryKey", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumns, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumns, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumns, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a64b1902d4fee186b4bb8f2adde3aa0c8258831ed76e5ef9445f475913abaa0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.datastreamStream.DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__237381b8637307cc7ee36e5718bb088f29692ac30282fe330db0d08e2e0b4532)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putMysqlColumns")
    def put_mysql_columns(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumns, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1e02dfc07a981322c5b8eced3743447d9a805a9b4f8533beddfc23764b5edfc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMysqlColumns", [value]))

    @jsii.member(jsii_name="resetMysqlColumns")
    def reset_mysql_columns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMysqlColumns", []))

    @builtins.property
    @jsii.member(jsii_name="mysqlColumns")
    def mysql_columns(
        self,
    ) -> DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumnsList:
        return typing.cast(DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumnsList, jsii.get(self, "mysqlColumns"))

    @builtins.property
    @jsii.member(jsii_name="mysqlColumnsInput")
    def mysql_columns_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumns]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumns]]], jsii.get(self, "mysqlColumnsInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__194e3ac627639d568a0e45fb6174fdf679bf1a46f154a89120f30df44737d4bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "table", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTables, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTables, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTables, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc9c4f92d7944ed623c164ccc25807fc788a1a13862f4b03cdc329bc1e5a194e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.datastreamStream.DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__edbedda5850481069316e19fe67cce30cc1c84aa2742bdd454adc48f1f439f86)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putMysqlTables")
    def put_mysql_tables(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTables, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b495122f684f8a6aff9d3cacd4b489d00bc74085863a55a9cc6ed61d8016dee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMysqlTables", [value]))

    @jsii.member(jsii_name="resetMysqlTables")
    def reset_mysql_tables(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMysqlTables", []))

    @builtins.property
    @jsii.member(jsii_name="mysqlTables")
    def mysql_tables(
        self,
    ) -> DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesList:
        return typing.cast(DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesList, jsii.get(self, "mysqlTables"))

    @builtins.property
    @jsii.member(jsii_name="databaseInput")
    def database_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseInput"))

    @builtins.property
    @jsii.member(jsii_name="mysqlTablesInput")
    def mysql_tables_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTables]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTables]]], jsii.get(self, "mysqlTablesInput"))

    @builtins.property
    @jsii.member(jsii_name="database")
    def database(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "database"))

    @database.setter
    def database(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74b85c9f253102ec7dfb09677425de6dbdb1f44d41faf0afd71a5b30519d4668)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "database", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabases, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabases, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabases, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__871843b0fb3d6e912f71a0f4656946654572899c708f26ad9164fc7e039f8b5a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.datastreamStream.DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ad7739c0c903f5d4eed5b61e16a039adbae564ad438ed843c2408b9ca2174b4b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMysqlDatabases")
    def put_mysql_databases(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabases, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0564a6ef5fbb63d7a0fd01455b2db2106097444d2ec9d14b5793b6facddd8242)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMysqlDatabases", [value]))

    @builtins.property
    @jsii.member(jsii_name="mysqlDatabases")
    def mysql_databases(
        self,
    ) -> DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesList:
        return typing.cast(DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesList, jsii.get(self, "mysqlDatabases"))

    @builtins.property
    @jsii.member(jsii_name="mysqlDatabasesInput")
    def mysql_databases_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabases]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabases]]], jsii.get(self, "mysqlDatabasesInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjects]:
        return typing.cast(typing.Optional[DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjects], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjects],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a075919af5790565e078286520be7fc44a00af876994a9d576c8d2e79ad9e0a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DatastreamStreamSourceConfigMysqlSourceConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.datastreamStream.DatastreamStreamSourceConfigMysqlSourceConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f3dd658cd4fa3e196ac9065595cccd04322f9aa72e82d158c577d95074f21d5e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putExcludeObjects")
    def put_exclude_objects(
        self,
        *,
        mysql_databases: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabases, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param mysql_databases: mysql_databases block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#mysql_databases DatastreamStream#mysql_databases}
        '''
        value = DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjects(
            mysql_databases=mysql_databases
        )

        return typing.cast(None, jsii.invoke(self, "putExcludeObjects", [value]))

    @jsii.member(jsii_name="putIncludeObjects")
    def put_include_objects(
        self,
        *,
        mysql_databases: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabases, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param mysql_databases: mysql_databases block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#mysql_databases DatastreamStream#mysql_databases}
        '''
        value = DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjects(
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
    ) -> DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsOutputReference:
        return typing.cast(DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsOutputReference, jsii.get(self, "excludeObjects"))

    @builtins.property
    @jsii.member(jsii_name="includeObjects")
    def include_objects(
        self,
    ) -> DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsOutputReference:
        return typing.cast(DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsOutputReference, jsii.get(self, "includeObjects"))

    @builtins.property
    @jsii.member(jsii_name="excludeObjectsInput")
    def exclude_objects_input(
        self,
    ) -> typing.Optional[DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjects]:
        return typing.cast(typing.Optional[DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjects], jsii.get(self, "excludeObjectsInput"))

    @builtins.property
    @jsii.member(jsii_name="includeObjectsInput")
    def include_objects_input(
        self,
    ) -> typing.Optional[DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjects]:
        return typing.cast(typing.Optional[DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjects], jsii.get(self, "includeObjectsInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__53b176c9e31729438ec79fb94e1db18e775b08f3ea14b518ee846998caad54c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxConcurrentCdcTasks", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DatastreamStreamSourceConfigMysqlSourceConfig]:
        return typing.cast(typing.Optional[DatastreamStreamSourceConfigMysqlSourceConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DatastreamStreamSourceConfigMysqlSourceConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b5ff671da4949da1a3fd7811aa6a121febb36c82cdc6828d84d473f27be21b0b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DatastreamStreamSourceConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.datastreamStream.DatastreamStreamSourceConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__09a3549b6717770d6733410684731e269f34c59ed1d70ad04082a2cb1b372371)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMysqlSourceConfig")
    def put_mysql_source_config(
        self,
        *,
        exclude_objects: typing.Optional[typing.Union[DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjects, typing.Dict[builtins.str, typing.Any]]] = None,
        include_objects: typing.Optional[typing.Union[DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjects, typing.Dict[builtins.str, typing.Any]]] = None,
        max_concurrent_cdc_tasks: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param exclude_objects: exclude_objects block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#exclude_objects DatastreamStream#exclude_objects}
        :param include_objects: include_objects block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#include_objects DatastreamStream#include_objects}
        :param max_concurrent_cdc_tasks: Maximum number of concurrent CDC tasks. The number should be non negative. If not set (or set to 0), the system's default value will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#max_concurrent_cdc_tasks DatastreamStream#max_concurrent_cdc_tasks}
        '''
        value = DatastreamStreamSourceConfigMysqlSourceConfig(
            exclude_objects=exclude_objects,
            include_objects=include_objects,
            max_concurrent_cdc_tasks=max_concurrent_cdc_tasks,
        )

        return typing.cast(None, jsii.invoke(self, "putMysqlSourceConfig", [value]))

    @builtins.property
    @jsii.member(jsii_name="mysqlSourceConfig")
    def mysql_source_config(
        self,
    ) -> DatastreamStreamSourceConfigMysqlSourceConfigOutputReference:
        return typing.cast(DatastreamStreamSourceConfigMysqlSourceConfigOutputReference, jsii.get(self, "mysqlSourceConfig"))

    @builtins.property
    @jsii.member(jsii_name="mysqlSourceConfigInput")
    def mysql_source_config_input(
        self,
    ) -> typing.Optional[DatastreamStreamSourceConfigMysqlSourceConfig]:
        return typing.cast(typing.Optional[DatastreamStreamSourceConfigMysqlSourceConfig], jsii.get(self, "mysqlSourceConfigInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__0241e5b41a94a409e82cab6012190e0005a0636d4cf36be768a9f6a56556cb14)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceConnectionProfile", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DatastreamStreamSourceConfig]:
        return typing.cast(typing.Optional[DatastreamStreamSourceConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DatastreamStreamSourceConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac91b8aafb6713d91456fefe65121644675bbb9cb229a0456370ca2b40569268)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.datastreamStream.DatastreamStreamTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class DatastreamStreamTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#create DatastreamStream#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#delete DatastreamStream#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#update DatastreamStream#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe3c43d69f12289839f31d381d72fc17e555fa583862cecacfb6539c6d58e6e9)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#create DatastreamStream#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#delete DatastreamStream#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/datastream_stream#update DatastreamStream#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatastreamStreamTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatastreamStreamTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.datastreamStream.DatastreamStreamTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4cac18995955222a43bb9b35c0136372f39bb89f568cf37a95aa304a07adf928)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c8643526e3db645744eade7d744fa2156e3d4720ede8a3f92d13bb328ce9c950)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bfbc2b3312d9160fbb91182305e5ed12d586cd6f792084f07eadff56090eb376)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4fd7cdc806265f3b7a72b6ee739412e8ca9ccb9efa8c1e3155c46a10919fe0c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DatastreamStreamTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DatastreamStreamTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DatastreamStreamTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__201682a522c85e6608f5a77eb390ed891ff39af25038c474f9af88101c6414a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DatastreamStream",
    "DatastreamStreamBackfillAll",
    "DatastreamStreamBackfillAllMysqlExcludedObjects",
    "DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabases",
    "DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesList",
    "DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTables",
    "DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesList",
    "DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumns",
    "DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumnsList",
    "DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumnsOutputReference",
    "DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesOutputReference",
    "DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesOutputReference",
    "DatastreamStreamBackfillAllMysqlExcludedObjectsOutputReference",
    "DatastreamStreamBackfillAllOutputReference",
    "DatastreamStreamBackfillNone",
    "DatastreamStreamBackfillNoneOutputReference",
    "DatastreamStreamConfig",
    "DatastreamStreamDestinationConfig",
    "DatastreamStreamDestinationConfigBigqueryDestinationConfig",
    "DatastreamStreamDestinationConfigBigqueryDestinationConfigOutputReference",
    "DatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDataset",
    "DatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDatasetOutputReference",
    "DatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasets",
    "DatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplate",
    "DatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplateOutputReference",
    "DatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsOutputReference",
    "DatastreamStreamDestinationConfigGcsDestinationConfig",
    "DatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormat",
    "DatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormatOutputReference",
    "DatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormat",
    "DatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormatOutputReference",
    "DatastreamStreamDestinationConfigGcsDestinationConfigOutputReference",
    "DatastreamStreamDestinationConfigOutputReference",
    "DatastreamStreamSourceConfig",
    "DatastreamStreamSourceConfigMysqlSourceConfig",
    "DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjects",
    "DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabases",
    "DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesList",
    "DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTables",
    "DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesList",
    "DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumns",
    "DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumnsList",
    "DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumnsOutputReference",
    "DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesOutputReference",
    "DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesOutputReference",
    "DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsOutputReference",
    "DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjects",
    "DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabases",
    "DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesList",
    "DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTables",
    "DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesList",
    "DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumns",
    "DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumnsList",
    "DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumnsOutputReference",
    "DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesOutputReference",
    "DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesOutputReference",
    "DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsOutputReference",
    "DatastreamStreamSourceConfigMysqlSourceConfigOutputReference",
    "DatastreamStreamSourceConfigOutputReference",
    "DatastreamStreamTimeouts",
    "DatastreamStreamTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__6c3ae3a9775ec6a2f34ba62bb34fac9132ef80c080cb4f5fc8bb6686d10ac590(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    destination_config: typing.Union[DatastreamStreamDestinationConfig, typing.Dict[builtins.str, typing.Any]],
    display_name: builtins.str,
    location: builtins.str,
    source_config: typing.Union[DatastreamStreamSourceConfig, typing.Dict[builtins.str, typing.Any]],
    stream_id: builtins.str,
    backfill_all: typing.Optional[typing.Union[DatastreamStreamBackfillAll, typing.Dict[builtins.str, typing.Any]]] = None,
    backfill_none: typing.Optional[typing.Union[DatastreamStreamBackfillNone, typing.Dict[builtins.str, typing.Any]]] = None,
    desired_state: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    project: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[DatastreamStreamTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__52394fe12c454915c68b7f5c0e1158a297c28bf8edc5470752d8d03bdadb3ff5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__075bf1e3249baeb8aa177ed19b3f502beb142b110c60b7139a705093ce1b0a7d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07f951eeadca73ea4a620fa2306732bbea40433c714d9c7f9ff106a61a7faead(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aef205b5c5ab66f32171c7535e21c4e68b81ebab105a33f1ff35977ad01202a1(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecf79e1cbe57e9eb4ed393c90fd467db45153af81195ed412bfacee8feaa28a1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__643d9836b9fc11f1901e2a2838ff876acef8280f6554dd37d2d02fa890104d78(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__283627036b55d75a53badb063b8cbdcac874d10da468b6abae149456f4ed27d0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__548fd10e905731875c7b597865e08230b888f6d65781f1f9e58cc54902b013a8(
    *,
    mysql_excluded_objects: typing.Optional[typing.Union[DatastreamStreamBackfillAllMysqlExcludedObjects, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69c73ea13a69e84cb5c059ba0260ae859d8c602b57e97a85cc24ad93dfc88b5f(
    *,
    mysql_databases: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabases, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13410b2bfcca2c97647224c4a67319d908e9d319c6a9237cc85a4e41f55b548f(
    *,
    database: builtins.str,
    mysql_tables: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTables, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea67c8ef97a0bde8fc840322d14b0b15cad0751a347171e7dc7803d39cec09bb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e433a44dd8df3a9cadc62af5b456b9bc010f04b3ba73bafaf04a805db07586db(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae3201f4411b84a193a6646dd047aa80f26f7dde220aef2aef705c5287e252e0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3c44068e63d483ac615dac0b8b6f39ba7905423e373797afbe8cc55e6cd75e9(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28ae6f5b98dab77299fa101efba9a44e8d9bd7f7ad9211e91cba088aa6c700ab(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aebbfa9a89be0456ea53147d93d92bf800659d380f16345317d1f06cc039aa0a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabases]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c949b7e6ad7f4b38807ff06c703f595dfd880a47c4b1d04b04a3915dec77355a(
    *,
    table: builtins.str,
    mysql_columns: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumns, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e065db95f692750c0a4063feef0b9379251d390020ae9aa8597c39b18492722e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f71340320398dcd9797361c897dd802615c2838318ad836b9a8a7a371389ce73(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6fae007e595a16d2276fc86cc2a375a7ac4c4e4fdf0b5e9c3807728d0312608d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f42f8dee5cb9de65146de9913d0470c79954bff38cb9237b2821934c9d38ba3(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09927ad10009415e1a205ef82c502175614a7e64824510e9b69fbf9eec02feb4(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0487084e9cacd7c8d5ac7a0aa828f1cf005979ca02f03bd6ac2db3f9e309f1c3(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTables]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__358f467e5b0f4377a34511fe2df79cd3ce7c42608d71ea9bc665657743281de9(
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

def _typecheckingstub__154f8dbef744b6d64d4b273c1aee6e622e76745c185fc129b20166f1d3b1983d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__713d5e717689a63ec3720f83c87565cadea875f763aa9cc85738d05e657e219d(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfa9e390d9ad10ccedd8763652c1adc0808202e386abbe93d623f621504e76ce(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9301374e73e0c50562a61bc71b8dd7a070d34619dda616483dea5909e9f46f98(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91c7b000f7d51a6d417fbacbfba2f039c7d7c3eb9281b41955951acec133650c(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e5df9305e59f038bfd61176fa4734ffa910d0bf7dee993b79f7d55c7529c3a0(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumns]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f018984efb7d263d0ffcb99493054e866b0c5304311041e893283f901e4a6c5f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70a552d16c9eeee74bbdd4efdd9298e085ed23856eae9264a8b1de5d65bc128c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ef3bcf0cf613c3945de3f7f965b20939420613dbf0bda0a777109acd57296b6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4ccd286da9f0d1f1989f8eff655c80e6b67fe37f7ff035a8f81704b1c1948fe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f42f8e7181c09785a11ef026e085afe5bbd15bce5111673479bccb9c3566cc49(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__097daa092a18ee02bf8669de9bd114d35e6fadb3ea65a486cabfd5b2425b3f73(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d4cd8ea957cbc5045edf6e2553556a3e684a0ab60fb1a5fa3c7c003e727ee3f(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9e079a8c2bf48a82f26ea7ebb4307d6a05b485fc96ce3f041b43af86038484f(
    value: typing.Optional[typing.Union[DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumns, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87a74c6f0174c2f917092188e7a5baac1b4376e817d30c3ddac8bfdd08ace52b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e9d4d13b08ecd8dfe67092ac6f87dde17666a854de010456318e3bdd9e068bd(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTablesMysqlColumns, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f0e90b83d1fa5fa9212c0d7bb6231593356596ff82ad67b135f440e2c462282(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de0b4e25f18b8e00271d40dc319fa34c7902a7c2c0ad6fd321f7f236706f10f2(
    value: typing.Optional[typing.Union[DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTables, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f5f8347e6725fe1f7f0267f7c851ffb9628cb21ac0e30564b95091505abfc30(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f814fec22f6e810871992154543a73b1af75cbbc27447a3fe884a5a80fb50c9(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabasesMysqlTables, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3151b274792b3f93fe09adbe180c158913e6bd5db0b114d7f42e9a220f02a568(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a7388148daab50b0ac722ba039b4763c332b0cf752fb7ecd0b82947dc468abe(
    value: typing.Optional[typing.Union[DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabases, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f1d7a4d992a763ac519977aaaad6c758ee59d5bab019a7a7745a4616285a28d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__931bbf966cb9ba2aae819fbebe1786809f88f7da77ce8346aaffbdcfad968a76(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DatastreamStreamBackfillAllMysqlExcludedObjectsMysqlDatabases, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__811433edaf8b7400da4083dd0803cdd680452b065b43ce1320c11977ab1cc96f(
    value: typing.Optional[DatastreamStreamBackfillAllMysqlExcludedObjects],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f2165189e7c8f1b458755c804ed55962f85c000ded00d4c56f68f9f3bcf3eb1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef5097bf84b7756c5e909c8358f325e4cc1c90362407525d463c71a947058c4a(
    value: typing.Optional[DatastreamStreamBackfillAll],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fe33cc0ef94cf2a41dd327fc0be0593dc211e9743a24827b5ee773542c7a8c7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af34f772ce61a51e2c5569138f820502f4470ede6042b4080b30aef00600f8a6(
    value: typing.Optional[DatastreamStreamBackfillNone],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__010b9566f8020e188444914b63cda5178f17cff35ec3ccd2e68861aaf3a93e42(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    destination_config: typing.Union[DatastreamStreamDestinationConfig, typing.Dict[builtins.str, typing.Any]],
    display_name: builtins.str,
    location: builtins.str,
    source_config: typing.Union[DatastreamStreamSourceConfig, typing.Dict[builtins.str, typing.Any]],
    stream_id: builtins.str,
    backfill_all: typing.Optional[typing.Union[DatastreamStreamBackfillAll, typing.Dict[builtins.str, typing.Any]]] = None,
    backfill_none: typing.Optional[typing.Union[DatastreamStreamBackfillNone, typing.Dict[builtins.str, typing.Any]]] = None,
    desired_state: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    project: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[DatastreamStreamTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f00248466cff6f376a67121eae26291d4773ff89be51d7e77bcce5aef3e183c(
    *,
    destination_connection_profile: builtins.str,
    bigquery_destination_config: typing.Optional[typing.Union[DatastreamStreamDestinationConfigBigqueryDestinationConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    gcs_destination_config: typing.Optional[typing.Union[DatastreamStreamDestinationConfigGcsDestinationConfig, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05d3281f73805ef674d65a156cd694bf3f6a088663f008143e968719408b4685(
    *,
    data_freshness: typing.Optional[builtins.str] = None,
    single_target_dataset: typing.Optional[typing.Union[DatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDataset, typing.Dict[builtins.str, typing.Any]]] = None,
    source_hierarchy_datasets: typing.Optional[typing.Union[DatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasets, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7a8b609b22768f789ea3611aa0ef25787c5d73f4a59a9be4ef77efa3c492a81(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62b7da575aade1c71be6745c30a44eae934f6539e34ccd51a86b8facf00d5060(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10290314eb6f6d825712b6b3207d7da992e62e51fc0be399239f7e7d53e2f846(
    value: typing.Optional[DatastreamStreamDestinationConfigBigqueryDestinationConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e44dd24643e8aa60468a62619c2ae48ae367e05d23c573afcfa2a6d3a4c91dd(
    *,
    dataset_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__441adf3b7f63f750260d12b3416082c5faf64d5c7e1832c2a1046cb0a48d5538(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b51999bc75c9b0fd3a12023b18a370bbc03175387133548ee3a57791a877640d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__268f1df491bfb370cbc33b522997f6031a2165748ce5ce4e0e09666537abd721(
    value: typing.Optional[DatastreamStreamDestinationConfigBigqueryDestinationConfigSingleTargetDataset],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d309147145fe77e14e6be2ec7f8089a10173d914dfbdb30bdc6fed0fd183a299(
    *,
    dataset_template: typing.Union[DatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplate, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21923ae44eb0f0bb463b3690f3b8ab6ee48575a23420bfc03244d26df8ce50fc(
    *,
    location: builtins.str,
    dataset_id_prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f3e1a71a02260fed7254d25a21729daa348bde759c05a201e378a1427397ba5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b12137ad883f1e8198a7e8a9d33112667f3a9d542fe239263ff41c443ac959f5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7f6a99aaed1e86235d35130b250c4ef94bbb8b532409fcb8b414027c2e8f90f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d649ea10fa687d496860280b0eb24cd52cc782d27783590f0680bfa4689aa1c(
    value: typing.Optional[DatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplate],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57dd2ede080c713c2f1230e7c848e67a25284bcfc9dddcff5c0399b99b877959(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ca05e8ee9521ac9812e47448dd7ed280d2aded497ee45b96dd7daca59deabbe(
    value: typing.Optional[DatastreamStreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasets],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff6fe7bc7051957d6ef5b4a2c8ba1b43b7844b9948287f7a5f36e8a41e8cc412(
    *,
    avro_file_format: typing.Optional[typing.Union[DatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormat, typing.Dict[builtins.str, typing.Any]]] = None,
    file_rotation_interval: typing.Optional[builtins.str] = None,
    file_rotation_mb: typing.Optional[jsii.Number] = None,
    json_file_format: typing.Optional[typing.Union[DatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormat, typing.Dict[builtins.str, typing.Any]]] = None,
    path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53992334d0a36b22747670910ec781eeb695714367669655fdf9bf4af1963833(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afaa1094b2bf96eb2aaa9a004fc98a4308a6190a94060ab74654bb2b416c437a(
    value: typing.Optional[DatastreamStreamDestinationConfigGcsDestinationConfigAvroFileFormat],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5c14e2cab90478a730fd4d9ac6ca6c8d7ba3f67ff802f4dcd2d5c9c08fb9803(
    *,
    compression: typing.Optional[builtins.str] = None,
    schema_file_format: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03cf334b7c9b733612b8ea0e5a5a7807c143ca675f4524c8a5e0e7755406bd56(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ded649c1e18a3afe723a46d8ef0cf7b3bd23261d1183fd169e1f378122c2eef7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4267f271d814121eca55dad65d9c3869f72e7c0df0c37798d71a0517c8e56d2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69a0efe2299c605431235b27746ddef41abdcec0e56eac6382ae8204a6a451f0(
    value: typing.Optional[DatastreamStreamDestinationConfigGcsDestinationConfigJsonFileFormat],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db9a6d5e7f6df721016eecca5688540ca539f31acd6bda59a8493f4c20acd453(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97148b45365aadc2e39b6e2e4fccc374cdbca79b05f3f52571e08319d4ee9036(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fae1649d074402474b5d7bd00712aabfc874730cfff03823ae354457233f2608(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f182119df80ece606c9383959c86ab83e4448a8f8744859baad283fd405e45d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f01a9c52ede76f92056982b7da315f974384e0fb43ded2f1d40f4d8e1832207(
    value: typing.Optional[DatastreamStreamDestinationConfigGcsDestinationConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f46069e1a4d2de7a3c29ede9cae6610ea00fcde99ec2ae63eab68dc303a751c0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07c51932c7c579a452dfb4bd688f68fa8208002be445062eda4e86430be29b96(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c94d7479b7d04eadd4b49a8a517d1d766123d5a712238cd25314c50439da47d(
    value: typing.Optional[DatastreamStreamDestinationConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__995aa3d40c0014eb42472704f6e2a586227929c23daf612b5bc02630f522ee9c(
    *,
    mysql_source_config: typing.Union[DatastreamStreamSourceConfigMysqlSourceConfig, typing.Dict[builtins.str, typing.Any]],
    source_connection_profile: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03986ed8942ca5af140f857a63fa4f9bf36dc4bc0034824c870a09ee77f3377f(
    *,
    exclude_objects: typing.Optional[typing.Union[DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjects, typing.Dict[builtins.str, typing.Any]]] = None,
    include_objects: typing.Optional[typing.Union[DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjects, typing.Dict[builtins.str, typing.Any]]] = None,
    max_concurrent_cdc_tasks: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd8924ba08b53e76420d1040aea7107d9f8f4a35a42d203306a4dc5eef847746(
    *,
    mysql_databases: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabases, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47003e7f3dfe4568bdfbecbecdfeca8cc5c1dc824fd507147bcf69d0e11c8907(
    *,
    database: builtins.str,
    mysql_tables: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTables, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ad30ac80003dfb56e29240af179446ad988b2d56141cc9ac9173a417b271330(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03e3be48b4d7ea91ea507468b666eb92e908b90eaa4b72909e6e563ba639959a(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82d098f2c688f84fafc6dd0afd35bf6d5c61a2a9469a607a83c9f3adea7ec6a1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af2024f15ee7b08a23d14347a6bf4886348cdd4fe08b134d84d142af2d64b50b(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87c0d3373e4a860d69ba9b1b96343c0a1a37400cad0c26a35d9976a03a2abbcf(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2195e2190f719cbe019609d3ec53f80debd66c7511eec9350b50efae0d491363(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabases]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36fef275c6ec7b8d609cafa0d2641bd263c44a10bc7249473f713a05683ba4f4(
    *,
    table: builtins.str,
    mysql_columns: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumns, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69c33a987c9a7ecb67924cb1032a96cc931edf369e360ae95e58e1551d69b163(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2137ca458d7db27e59eaa11790cf81f0760027a1075e78cbd3fd912b7fdbfe53(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b152c3de915d6fc96d08112f4da3d2632e4a1feb8ed9a6e739b1e322d056eba(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9761d0c70fb470dda84cafcf21d16c981695392477d4566b2b58631c6a17a85c(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e35fc4adff6fe3aeb36b4c144ff1bef8d8bfec907ca5fe8808db292d4698d710(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf3b7e194a1b17a44374dff58788f3134ef276f1b232460d9f088bc36c194fbf(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTables]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa1d840e397f01a70c2cddb58c957e80c59d39fb16bbea2a1c04910d8abb0218(
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

def _typecheckingstub__b934e1cd2f1b6e46749d3a3ee4ea123a5feab018bcbd9e1dc3d82577fc52b54d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b0462a33c37e557fcf3c2fd74887a5508dff56bcde35fa593f04f4b8607580c(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23b5fb04fe528246556f11f40ffb8e2ce0da1af40d4741f1ba0bc113654bb796(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30ff55614afd8ecea5a474c3db78ec06d5d81fc6e8371a0cc4fb16372f124bf1(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad32f42f77fac61d1715b212cb332883b311819b8cd438d36beb15bde86030dc(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9320334886970de6c5ea55c48a2818daa32156be2f9f75dd5e042a36ad100d27(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumns]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bc27762ed3847a2a4997c6417d746b2344e6ce7b9e40d4295c780394da67d35(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f10c35f21ec76d9b9b6f802e3565c8ba67ffd07a03db61a1a05cab01b31b5cd1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5e84862d7e010156638f260885c74211c45e9be7238c8249465e6db2a06d368(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84a4831ac66409ce770fc99b6de33638206edf8c50979ecf8d0cc42c7b84f450(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__600dbdaafece9c5dbfc122b3a1509faf6dc3db4dd21050d0da9936f77db7d0e8(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96f73fe59063cff45a5fabe46cc5ef9301038e2ca51363160acfdd6ff6a518a7(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64b2a7fe0df84f84031671b52e419f6be035d371a5bfd7fa6e4eed2354f0730f(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b2f92998ae8b6c8fd59179b9167917d5e06e3da0bf7f6a17d89c1a9d34958d9(
    value: typing.Optional[typing.Union[DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumns, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74c7edf517db15210471252d18fb4c0295e1f6d17ac794c71b59dad9fa34cde3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2a0c2eed43d5a92c7dd35f9d3b898447ed32f9260596e554f0bf82139dabb27(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTablesMysqlColumns, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a802aba7a80609e781d874483717985a77c791a6d610d086e56342e5ebdfea4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81a3c95f2945ef79610f226e7de8f82f4dd6c488b2cdea201b5adee9eb165a18(
    value: typing.Optional[typing.Union[DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTables, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__339d0233b5e3939582ec717c6235f70b3bcfce5011c933d1fa7b7b221a1b3f98(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00e753886968f6ad8529639aad8ba094d4d936e8fb59d04017d16679362ce906(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabasesMysqlTables, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7ddba99321e758ecfffe491c01f502472c59352bb67f1530bbaea001f0a7062(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e753e427d29d0ade6f4009149848849060b763be17e45608a15cca438775be09(
    value: typing.Optional[typing.Union[DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabases, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93d8c032e45bf0ac57ac3d0979da5b6ffe8c1f99b09476d82280a9af84df9c6d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc57f764ac9d739ecc943fad16909c32b76e6c97dea9a5df494ab6c104e29123(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabases, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72b7210b8484ca8aea5f7a6f1596f56ef4c03fe2c76a48dee6597741f3c6ff5b(
    value: typing.Optional[DatastreamStreamSourceConfigMysqlSourceConfigExcludeObjects],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40db11a5bb1c2aca7472fd834428a2203489803a28b44b1e4962ad4ab1b66159(
    *,
    mysql_databases: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabases, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ff4d778c3932f51b621c3ff1675a74882c85bb24341f2bf1594c06d9c82f36f(
    *,
    database: builtins.str,
    mysql_tables: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTables, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ade2a69c288d1345efb3bb511b247830dfd4432c1cd9cbefcabf6c9078c58dc5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__264cc6b382219d468fd08c237199dbe2f9c342a7f5890d61df2f62ee150f6ee4(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43dfcfbaa01fb883388f2b178ba7a5408a426f709176123962218ff85fdb5262(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a3c66c27ba53c72edcb3b6f85cf2f84f3bd4afd152aa8d8bbdce895bca382e5(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__824badd6fb7e5f770535729d1e915a227b98a14597f969bc12aaf2635f49b992(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec8b65c0e93aeb7913ed2a822757e31ec88018bc0633b32238f9b6ad54df3bab(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabases]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91f8c103e5beb0d973e5d209018bdb2893707dc54045bf4164625d73468a4327(
    *,
    table: builtins.str,
    mysql_columns: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumns, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f2ae67802bc4d46269f15e251ca61b00cd7e6cc4c72696f5ef1e117bd0b9351(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba47fc823bc86f85b46f3c7d66c7ef36e848bf6a8f9d4e4e4ec74485144daaa4(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96c60478bf9cf99a40bd62622ba84b3b4844306f809ead2f0c86eb8fe301fc9d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72e164afb7b4632e6e21ba9fe40e4060ded214f779343520f8ae627e64f6c416(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4fba8425facced2e35d16bc08d9f9df4a3cfe6e09828f27fbfdcbf3a5ec6751(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__811d23977ea46d8bb808a32e998c0cdeec1202920f1232c14e3d4e536d8f9934(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTables]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6b2437de5afb4d3d3062eedf288787c94f774d386adc5570fd611e7a929e190(
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

def _typecheckingstub__37248826856ca9dfb4e91cb36937cd1b038e5edac9cce3f3be797f674e6933ca(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c227d69d63e5037e72560f8cfe9e7b04578befbe5130eed9150a61b587d3a0f(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59c1f9241ec90839a4e9c7459608fec5eb625c2fb68430051ad1689fdad8eb56(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25ca7dd00f97fbe18a2c49875f68a9eae6a6255a559ad69db9a3ee209ef6192b(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__473f5e905f2848a2ccb19b790fd4c15eea0c52576954c9e7e48a8935c5db34a2(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37b258a7501901c9867024fa4f2c4c003140669bebbfe47678087094d1c19ec1(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumns]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2c5f7ad9b605e87fa3c703004388f9d973ac9b1e61d381ca0e122e420260396(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18623f5e4a5f5e41edc82a5f6793879500c107969e69faabe743ec280dd16351(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8aed8cbdee483c61be882e1558fc23ea2e3a910b66185dfcf543429f50ddb176(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__812c5406870508b7dcac28e9456b090b4d1f89406cc88a2040c859c09e71567a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2aec533a8ba2c7f9ab6215ed1c075b98a28fec4443e3ca719d34ffa4e7ecfdd4(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f8982e4523ee32bb9d8365de4142ceb42cf0144c0a45c49e41ef9accfc902e1(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab7726d162a19d90a4da0f120eca91dc0bb17ff7e32bd9045dda1f36ab000b80(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a64b1902d4fee186b4bb8f2adde3aa0c8258831ed76e5ef9445f475913abaa0(
    value: typing.Optional[typing.Union[DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumns, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__237381b8637307cc7ee36e5718bb088f29692ac30282fe330db0d08e2e0b4532(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1e02dfc07a981322c5b8eced3743447d9a805a9b4f8533beddfc23764b5edfc(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTablesMysqlColumns, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__194e3ac627639d568a0e45fb6174fdf679bf1a46f154a89120f30df44737d4bc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc9c4f92d7944ed623c164ccc25807fc788a1a13862f4b03cdc329bc1e5a194e(
    value: typing.Optional[typing.Union[DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTables, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__edbedda5850481069316e19fe67cce30cc1c84aa2742bdd454adc48f1f439f86(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b495122f684f8a6aff9d3cacd4b489d00bc74085863a55a9cc6ed61d8016dee(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabasesMysqlTables, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74b85c9f253102ec7dfb09677425de6dbdb1f44d41faf0afd71a5b30519d4668(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__871843b0fb3d6e912f71a0f4656946654572899c708f26ad9164fc7e039f8b5a(
    value: typing.Optional[typing.Union[DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabases, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad7739c0c903f5d4eed5b61e16a039adbae564ad438ed843c2408b9ca2174b4b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0564a6ef5fbb63d7a0fd01455b2db2106097444d2ec9d14b5793b6facddd8242(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabases, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a075919af5790565e078286520be7fc44a00af876994a9d576c8d2e79ad9e0a(
    value: typing.Optional[DatastreamStreamSourceConfigMysqlSourceConfigIncludeObjects],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3dd658cd4fa3e196ac9065595cccd04322f9aa72e82d158c577d95074f21d5e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53b176c9e31729438ec79fb94e1db18e775b08f3ea14b518ee846998caad54c3(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5ff671da4949da1a3fd7811aa6a121febb36c82cdc6828d84d473f27be21b0b(
    value: typing.Optional[DatastreamStreamSourceConfigMysqlSourceConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09a3549b6717770d6733410684731e269f34c59ed1d70ad04082a2cb1b372371(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0241e5b41a94a409e82cab6012190e0005a0636d4cf36be768a9f6a56556cb14(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac91b8aafb6713d91456fefe65121644675bbb9cb229a0456370ca2b40569268(
    value: typing.Optional[DatastreamStreamSourceConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe3c43d69f12289839f31d381d72fc17e555fa583862cecacfb6539c6d58e6e9(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4cac18995955222a43bb9b35c0136372f39bb89f568cf37a95aa304a07adf928(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8643526e3db645744eade7d744fa2156e3d4720ede8a3f92d13bb328ce9c950(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfbc2b3312d9160fbb91182305e5ed12d586cd6f792084f07eadff56090eb376(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4fd7cdc806265f3b7a72b6ee739412e8ca9ccb9efa8c1e3155c46a10919fe0c8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__201682a522c85e6608f5a77eb390ed891ff39af25038c474f9af88101c6414a9(
    value: typing.Optional[typing.Union[DatastreamStreamTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
