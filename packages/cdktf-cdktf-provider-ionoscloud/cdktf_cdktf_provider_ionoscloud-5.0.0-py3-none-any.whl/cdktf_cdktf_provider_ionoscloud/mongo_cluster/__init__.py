'''
# `ionoscloud_mongo_cluster`

Refer to the Terraform Registory for docs: [`ionoscloud_mongo_cluster`](https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster).
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


class MongoCluster(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-ionoscloud.mongoCluster.MongoCluster",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster ionoscloud_mongo_cluster}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        connections: typing.Union["MongoClusterConnections", typing.Dict[builtins.str, typing.Any]],
        credentials: typing.Union["MongoClusterCredentials", typing.Dict[builtins.str, typing.Any]],
        display_name: builtins.str,
        instances: jsii.Number,
        location: builtins.str,
        mongodb_version: builtins.str,
        template_id: builtins.str,
        id: typing.Optional[builtins.str] = None,
        maintenance_window: typing.Optional[typing.Union["MongoClusterMaintenanceWindow", typing.Dict[builtins.str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["MongoClusterTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster ionoscloud_mongo_cluster} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param connections: connections block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster#connections MongoCluster#connections}
        :param credentials: credentials block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster#credentials MongoCluster#credentials}
        :param display_name: The name of your cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster#display_name MongoCluster#display_name}
        :param instances: The total number of instances in the cluster (one master and n-1 standbys). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster#instances MongoCluster#instances}
        :param location: The physical location where the cluster will be created. This will be where all of your instances live. Property cannot be modified after datacenter creation (disallowed in update requests). Available locations: de/txl, gb/lhr, es/vit Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster#location MongoCluster#location}
        :param mongodb_version: The MongoDB version of your cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster#mongodb_version MongoCluster#mongodb_version}
        :param template_id: The unique ID of the template, which specifies the number of cores, storage size, and memory. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster#template_id MongoCluster#template_id}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster#id MongoCluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param maintenance_window: maintenance_window block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster#maintenance_window MongoCluster#maintenance_window}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster#timeouts MongoCluster#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a42d26061608ff45da50ca3a2af0ae83fa7b699e21a4271aa2c43ea98009a34)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = MongoClusterConfig(
            connections=connections,
            credentials=credentials,
            display_name=display_name,
            instances=instances,
            location=location,
            mongodb_version=mongodb_version,
            template_id=template_id,
            id=id,
            maintenance_window=maintenance_window,
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

    @jsii.member(jsii_name="putConnections")
    def put_connections(
        self,
        *,
        cidr_list: typing.Sequence[builtins.str],
        datacenter_id: builtins.str,
        lan_id: builtins.str,
    ) -> None:
        '''
        :param cidr_list: The list of IPs and subnet for your cluster. Note the following unavailable IP ranges: 10.233.64.0/18 10.233.0.0/18 10.233.114.0/24 example: [192.168.1.100/24, 192.168.1.101/24] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster#cidr_list MongoCluster#cidr_list}
        :param datacenter_id: The datacenter to connect your cluster to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster#datacenter_id MongoCluster#datacenter_id}
        :param lan_id: The LAN to connect your cluster to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster#lan_id MongoCluster#lan_id}
        '''
        value = MongoClusterConnections(
            cidr_list=cidr_list, datacenter_id=datacenter_id, lan_id=lan_id
        )

        return typing.cast(None, jsii.invoke(self, "putConnections", [value]))

    @jsii.member(jsii_name="putCredentials")
    def put_credentials(
        self,
        *,
        password: builtins.str,
        username: builtins.str,
    ) -> None:
        '''
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster#password MongoCluster#password}.
        :param username: the username for the initial mongoDB user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster#username MongoCluster#username}
        '''
        value = MongoClusterCredentials(password=password, username=username)

        return typing.cast(None, jsii.invoke(self, "putCredentials", [value]))

    @jsii.member(jsii_name="putMaintenanceWindow")
    def put_maintenance_window(
        self,
        *,
        day_of_the_week: builtins.str,
        time: builtins.str,
    ) -> None:
        '''
        :param day_of_the_week: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster#day_of_the_week MongoCluster#day_of_the_week}.
        :param time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster#time MongoCluster#time}.
        '''
        value = MongoClusterMaintenanceWindow(
            day_of_the_week=day_of_the_week, time=time
        )

        return typing.cast(None, jsii.invoke(self, "putMaintenanceWindow", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        default: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster#create MongoCluster#create}.
        :param default: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster#default MongoCluster#default}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster#delete MongoCluster#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster#update MongoCluster#update}.
        '''
        value = MongoClusterTimeouts(
            create=create, default=default, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMaintenanceWindow")
    def reset_maintenance_window(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaintenanceWindow", []))

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
    @jsii.member(jsii_name="connections")
    def connections(self) -> "MongoClusterConnectionsOutputReference":
        return typing.cast("MongoClusterConnectionsOutputReference", jsii.get(self, "connections"))

    @builtins.property
    @jsii.member(jsii_name="connectionString")
    def connection_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectionString"))

    @builtins.property
    @jsii.member(jsii_name="credentials")
    def credentials(self) -> "MongoClusterCredentialsOutputReference":
        return typing.cast("MongoClusterCredentialsOutputReference", jsii.get(self, "credentials"))

    @builtins.property
    @jsii.member(jsii_name="maintenanceWindow")
    def maintenance_window(self) -> "MongoClusterMaintenanceWindowOutputReference":
        return typing.cast("MongoClusterMaintenanceWindowOutputReference", jsii.get(self, "maintenanceWindow"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "MongoClusterTimeoutsOutputReference":
        return typing.cast("MongoClusterTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="connectionsInput")
    def connections_input(self) -> typing.Optional["MongoClusterConnections"]:
        return typing.cast(typing.Optional["MongoClusterConnections"], jsii.get(self, "connectionsInput"))

    @builtins.property
    @jsii.member(jsii_name="credentialsInput")
    def credentials_input(self) -> typing.Optional["MongoClusterCredentials"]:
        return typing.cast(typing.Optional["MongoClusterCredentials"], jsii.get(self, "credentialsInput"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="instancesInput")
    def instances_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "instancesInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="maintenanceWindowInput")
    def maintenance_window_input(
        self,
    ) -> typing.Optional["MongoClusterMaintenanceWindow"]:
        return typing.cast(typing.Optional["MongoClusterMaintenanceWindow"], jsii.get(self, "maintenanceWindowInput"))

    @builtins.property
    @jsii.member(jsii_name="mongodbVersionInput")
    def mongodb_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mongodbVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="templateIdInput")
    def template_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "templateIdInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["MongoClusterTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["MongoClusterTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa0053b5c0f14bccaa25c474590d9951ff3dea23eca75465d6418c5471c9ff57)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1dcbad60da59e5e5d9edb8dc88f32ccba5119961411db1ca628d23dcc1abe46d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="instances")
    def instances(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "instances"))

    @instances.setter
    def instances(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19dc756326b5cf21ce11e8dff10aa46231890747bea9233fb6be6965f567b4a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instances", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2d712b91d80a7bc9d45be651c5fe31f2db583d94e01bb68d0bd31993713198c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="mongodbVersion")
    def mongodb_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mongodbVersion"))

    @mongodb_version.setter
    def mongodb_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51a155107aaab7c778604aac3a6f794381680322a023c3538862a5f06b30b92b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mongodbVersion", value)

    @builtins.property
    @jsii.member(jsii_name="templateId")
    def template_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "templateId"))

    @template_id.setter
    def template_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9cc1a2fe3014ad55e78d4638cf1e018bc2720690c1d23d7ef6ce40cd0d7956b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "templateId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-ionoscloud.mongoCluster.MongoClusterConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "connections": "connections",
        "credentials": "credentials",
        "display_name": "displayName",
        "instances": "instances",
        "location": "location",
        "mongodb_version": "mongodbVersion",
        "template_id": "templateId",
        "id": "id",
        "maintenance_window": "maintenanceWindow",
        "timeouts": "timeouts",
    },
)
class MongoClusterConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        connections: typing.Union["MongoClusterConnections", typing.Dict[builtins.str, typing.Any]],
        credentials: typing.Union["MongoClusterCredentials", typing.Dict[builtins.str, typing.Any]],
        display_name: builtins.str,
        instances: jsii.Number,
        location: builtins.str,
        mongodb_version: builtins.str,
        template_id: builtins.str,
        id: typing.Optional[builtins.str] = None,
        maintenance_window: typing.Optional[typing.Union["MongoClusterMaintenanceWindow", typing.Dict[builtins.str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["MongoClusterTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param connections: connections block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster#connections MongoCluster#connections}
        :param credentials: credentials block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster#credentials MongoCluster#credentials}
        :param display_name: The name of your cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster#display_name MongoCluster#display_name}
        :param instances: The total number of instances in the cluster (one master and n-1 standbys). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster#instances MongoCluster#instances}
        :param location: The physical location where the cluster will be created. This will be where all of your instances live. Property cannot be modified after datacenter creation (disallowed in update requests). Available locations: de/txl, gb/lhr, es/vit Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster#location MongoCluster#location}
        :param mongodb_version: The MongoDB version of your cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster#mongodb_version MongoCluster#mongodb_version}
        :param template_id: The unique ID of the template, which specifies the number of cores, storage size, and memory. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster#template_id MongoCluster#template_id}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster#id MongoCluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param maintenance_window: maintenance_window block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster#maintenance_window MongoCluster#maintenance_window}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster#timeouts MongoCluster#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(connections, dict):
            connections = MongoClusterConnections(**connections)
        if isinstance(credentials, dict):
            credentials = MongoClusterCredentials(**credentials)
        if isinstance(maintenance_window, dict):
            maintenance_window = MongoClusterMaintenanceWindow(**maintenance_window)
        if isinstance(timeouts, dict):
            timeouts = MongoClusterTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8fb454f71a78c55f953ba7fe2ceec44ae6b5525b41d230bad9af2e67e70c5a4)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument connections", value=connections, expected_type=type_hints["connections"])
            check_type(argname="argument credentials", value=credentials, expected_type=type_hints["credentials"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument instances", value=instances, expected_type=type_hints["instances"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument mongodb_version", value=mongodb_version, expected_type=type_hints["mongodb_version"])
            check_type(argname="argument template_id", value=template_id, expected_type=type_hints["template_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument maintenance_window", value=maintenance_window, expected_type=type_hints["maintenance_window"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "connections": connections,
            "credentials": credentials,
            "display_name": display_name,
            "instances": instances,
            "location": location,
            "mongodb_version": mongodb_version,
            "template_id": template_id,
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
        if maintenance_window is not None:
            self._values["maintenance_window"] = maintenance_window
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
    def connections(self) -> "MongoClusterConnections":
        '''connections block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster#connections MongoCluster#connections}
        '''
        result = self._values.get("connections")
        assert result is not None, "Required property 'connections' is missing"
        return typing.cast("MongoClusterConnections", result)

    @builtins.property
    def credentials(self) -> "MongoClusterCredentials":
        '''credentials block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster#credentials MongoCluster#credentials}
        '''
        result = self._values.get("credentials")
        assert result is not None, "Required property 'credentials' is missing"
        return typing.cast("MongoClusterCredentials", result)

    @builtins.property
    def display_name(self) -> builtins.str:
        '''The name of your cluster.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster#display_name MongoCluster#display_name}
        '''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def instances(self) -> jsii.Number:
        '''The total number of instances in the cluster (one master and n-1 standbys).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster#instances MongoCluster#instances}
        '''
        result = self._values.get("instances")
        assert result is not None, "Required property 'instances' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def location(self) -> builtins.str:
        '''The physical location where the cluster will be created.

        This will be where all of your instances live. Property cannot be modified after datacenter creation (disallowed in update requests). Available locations: de/txl, gb/lhr, es/vit

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster#location MongoCluster#location}
        '''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def mongodb_version(self) -> builtins.str:
        '''The MongoDB version of your cluster.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster#mongodb_version MongoCluster#mongodb_version}
        '''
        result = self._values.get("mongodb_version")
        assert result is not None, "Required property 'mongodb_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def template_id(self) -> builtins.str:
        '''The unique ID of the template, which specifies the number of cores, storage size, and memory.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster#template_id MongoCluster#template_id}
        '''
        result = self._values.get("template_id")
        assert result is not None, "Required property 'template_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster#id MongoCluster#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def maintenance_window(self) -> typing.Optional["MongoClusterMaintenanceWindow"]:
        '''maintenance_window block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster#maintenance_window MongoCluster#maintenance_window}
        '''
        result = self._values.get("maintenance_window")
        return typing.cast(typing.Optional["MongoClusterMaintenanceWindow"], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["MongoClusterTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster#timeouts MongoCluster#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["MongoClusterTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MongoClusterConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-ionoscloud.mongoCluster.MongoClusterConnections",
    jsii_struct_bases=[],
    name_mapping={
        "cidr_list": "cidrList",
        "datacenter_id": "datacenterId",
        "lan_id": "lanId",
    },
)
class MongoClusterConnections:
    def __init__(
        self,
        *,
        cidr_list: typing.Sequence[builtins.str],
        datacenter_id: builtins.str,
        lan_id: builtins.str,
    ) -> None:
        '''
        :param cidr_list: The list of IPs and subnet for your cluster. Note the following unavailable IP ranges: 10.233.64.0/18 10.233.0.0/18 10.233.114.0/24 example: [192.168.1.100/24, 192.168.1.101/24] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster#cidr_list MongoCluster#cidr_list}
        :param datacenter_id: The datacenter to connect your cluster to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster#datacenter_id MongoCluster#datacenter_id}
        :param lan_id: The LAN to connect your cluster to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster#lan_id MongoCluster#lan_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef7c56af8c323083878e68eb0a14d8ceb4919a475185b1a0d2a31901c56ec507)
            check_type(argname="argument cidr_list", value=cidr_list, expected_type=type_hints["cidr_list"])
            check_type(argname="argument datacenter_id", value=datacenter_id, expected_type=type_hints["datacenter_id"])
            check_type(argname="argument lan_id", value=lan_id, expected_type=type_hints["lan_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cidr_list": cidr_list,
            "datacenter_id": datacenter_id,
            "lan_id": lan_id,
        }

    @builtins.property
    def cidr_list(self) -> typing.List[builtins.str]:
        '''The list of IPs and subnet for your cluster.

        Note the following unavailable IP ranges:
        10.233.64.0/18
        10.233.0.0/18
        10.233.114.0/24
        example: [192.168.1.100/24, 192.168.1.101/24]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster#cidr_list MongoCluster#cidr_list}
        '''
        result = self._values.get("cidr_list")
        assert result is not None, "Required property 'cidr_list' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def datacenter_id(self) -> builtins.str:
        '''The datacenter to connect your cluster to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster#datacenter_id MongoCluster#datacenter_id}
        '''
        result = self._values.get("datacenter_id")
        assert result is not None, "Required property 'datacenter_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def lan_id(self) -> builtins.str:
        '''The LAN to connect your cluster to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster#lan_id MongoCluster#lan_id}
        '''
        result = self._values.get("lan_id")
        assert result is not None, "Required property 'lan_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MongoClusterConnections(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MongoClusterConnectionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-ionoscloud.mongoCluster.MongoClusterConnectionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e314a3307e0a8c064c7f30b26fc884ef154ab3344f0193966f8b4a5e6c2fe182)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="cidrListInput")
    def cidr_list_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "cidrListInput"))

    @builtins.property
    @jsii.member(jsii_name="datacenterIdInput")
    def datacenter_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datacenterIdInput"))

    @builtins.property
    @jsii.member(jsii_name="lanIdInput")
    def lan_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lanIdInput"))

    @builtins.property
    @jsii.member(jsii_name="cidrList")
    def cidr_list(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "cidrList"))

    @cidr_list.setter
    def cidr_list(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a82343f2d30b87fd592e819a8b4280d70dc881d5c48316d79f5beca6e9cc0888)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cidrList", value)

    @builtins.property
    @jsii.member(jsii_name="datacenterId")
    def datacenter_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datacenterId"))

    @datacenter_id.setter
    def datacenter_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f5c28b3eb998d51e786648d9bffb45023a639e9c46e3f0785a7b4151808a52e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datacenterId", value)

    @builtins.property
    @jsii.member(jsii_name="lanId")
    def lan_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lanId"))

    @lan_id.setter
    def lan_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8eeee68c96f4a24ddde42dc4ffd3f38a875858b3610e776b4e44cf5ec7408364)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lanId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MongoClusterConnections]:
        return typing.cast(typing.Optional[MongoClusterConnections], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[MongoClusterConnections]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ccff2c6267ce769672f1eb1b527f9f13e1224c17849c96cf336609fc9b766935)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-ionoscloud.mongoCluster.MongoClusterCredentials",
    jsii_struct_bases=[],
    name_mapping={"password": "password", "username": "username"},
)
class MongoClusterCredentials:
    def __init__(self, *, password: builtins.str, username: builtins.str) -> None:
        '''
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster#password MongoCluster#password}.
        :param username: the username for the initial mongoDB user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster#username MongoCluster#username}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd596e77ddabfeaab94440fa1cb0f018fc77ffae23cdd85281d35be956303a36)
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "password": password,
            "username": username,
        }

    @builtins.property
    def password(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster#password MongoCluster#password}.'''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''the username for the initial mongoDB user.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster#username MongoCluster#username}
        '''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MongoClusterCredentials(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MongoClusterCredentialsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-ionoscloud.mongoCluster.MongoClusterCredentialsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a3c22fb5840927a8d01154ab079b9d17d11e5ac2f715383082710a3236f56218)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c5383566ed4b87b116cf6d31771f751e8b7e0dfb8671a068fef641e0c15a70f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__621ff0d10adc831fdb3a83e2a6115c68f668bf02ff9f036c2c53f88625749da6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MongoClusterCredentials]:
        return typing.cast(typing.Optional[MongoClusterCredentials], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[MongoClusterCredentials]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16731cc0f6bd6b604ef50328c9a7940a9a7b1a1a4a95fa8a0450da45b354b5ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-ionoscloud.mongoCluster.MongoClusterMaintenanceWindow",
    jsii_struct_bases=[],
    name_mapping={"day_of_the_week": "dayOfTheWeek", "time": "time"},
)
class MongoClusterMaintenanceWindow:
    def __init__(self, *, day_of_the_week: builtins.str, time: builtins.str) -> None:
        '''
        :param day_of_the_week: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster#day_of_the_week MongoCluster#day_of_the_week}.
        :param time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster#time MongoCluster#time}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__421318b6ba20092a579d3f220b98f02358edef22f00eff2ae1356b9a601b903d)
            check_type(argname="argument day_of_the_week", value=day_of_the_week, expected_type=type_hints["day_of_the_week"])
            check_type(argname="argument time", value=time, expected_type=type_hints["time"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "day_of_the_week": day_of_the_week,
            "time": time,
        }

    @builtins.property
    def day_of_the_week(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster#day_of_the_week MongoCluster#day_of_the_week}.'''
        result = self._values.get("day_of_the_week")
        assert result is not None, "Required property 'day_of_the_week' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def time(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster#time MongoCluster#time}.'''
        result = self._values.get("time")
        assert result is not None, "Required property 'time' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MongoClusterMaintenanceWindow(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MongoClusterMaintenanceWindowOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-ionoscloud.mongoCluster.MongoClusterMaintenanceWindowOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__11d51c6b9a2f02b86aeb4d8885b9cbb062f9e1e490f330bcf004237ca416d5e6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="dayOfTheWeekInput")
    def day_of_the_week_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dayOfTheWeekInput"))

    @builtins.property
    @jsii.member(jsii_name="timeInput")
    def time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeInput"))

    @builtins.property
    @jsii.member(jsii_name="dayOfTheWeek")
    def day_of_the_week(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dayOfTheWeek"))

    @day_of_the_week.setter
    def day_of_the_week(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e0e03a1e507dfd09a5381beeb536ac06b19ed446e8464f8ad9952f0cc37b136)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dayOfTheWeek", value)

    @builtins.property
    @jsii.member(jsii_name="time")
    def time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "time"))

    @time.setter
    def time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b838f55e7721c42d86322ed9734d1a0a195fd3b8067831a1ae6a4f00d64e183d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "time", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MongoClusterMaintenanceWindow]:
        return typing.cast(typing.Optional[MongoClusterMaintenanceWindow], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MongoClusterMaintenanceWindow],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84611be84595e1202f28d9790d284d2fa18480fdc255beb05e3626874cfb204c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-ionoscloud.mongoCluster.MongoClusterTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "default": "default",
        "delete": "delete",
        "update": "update",
    },
)
class MongoClusterTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        default: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster#create MongoCluster#create}.
        :param default: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster#default MongoCluster#default}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster#delete MongoCluster#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster#update MongoCluster#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6085053f4064a51de0be39081bc634b1f0448b8ea5f556a80b31862027995ca)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument default", value=default, expected_type=type_hints["default"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if default is not None:
            self._values["default"] = default
        if delete is not None:
            self._values["delete"] = delete
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster#create MongoCluster#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster#default MongoCluster#default}.'''
        result = self._values.get("default")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster#delete MongoCluster#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/mongo_cluster#update MongoCluster#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MongoClusterTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MongoClusterTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-ionoscloud.mongoCluster.MongoClusterTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9286af292886504f9b37a019491d019d245d39d15633ad593e2d58bcf6ce53c8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDefault")
    def reset_default(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefault", []))

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
    @jsii.member(jsii_name="defaultInput")
    def default_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__158561af1d8b4d346a01dc917df64946880d4d9a7d0b9f4bb45e5341daf9d5c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="default")
    def default(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "default"))

    @default.setter
    def default(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00c66f738ae251306b54c21613f0bc7805e217f8bde87d51fdb5101858fb53f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "default", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1d7bf9fa10ad374a66279bc9a46f566bf4b71adfb6336e372828be270c56f7a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a637fb1ce3343c360f888702a4f5c603da828839d43fc78f55be210dad95256c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MongoClusterTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MongoClusterTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MongoClusterTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4bbf8b7bdd56ed86764046f529e0a62efc541da63c3849a9fbad65ba81f80713)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "MongoCluster",
    "MongoClusterConfig",
    "MongoClusterConnections",
    "MongoClusterConnectionsOutputReference",
    "MongoClusterCredentials",
    "MongoClusterCredentialsOutputReference",
    "MongoClusterMaintenanceWindow",
    "MongoClusterMaintenanceWindowOutputReference",
    "MongoClusterTimeouts",
    "MongoClusterTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__7a42d26061608ff45da50ca3a2af0ae83fa7b699e21a4271aa2c43ea98009a34(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    connections: typing.Union[MongoClusterConnections, typing.Dict[builtins.str, typing.Any]],
    credentials: typing.Union[MongoClusterCredentials, typing.Dict[builtins.str, typing.Any]],
    display_name: builtins.str,
    instances: jsii.Number,
    location: builtins.str,
    mongodb_version: builtins.str,
    template_id: builtins.str,
    id: typing.Optional[builtins.str] = None,
    maintenance_window: typing.Optional[typing.Union[MongoClusterMaintenanceWindow, typing.Dict[builtins.str, typing.Any]]] = None,
    timeouts: typing.Optional[typing.Union[MongoClusterTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__fa0053b5c0f14bccaa25c474590d9951ff3dea23eca75465d6418c5471c9ff57(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1dcbad60da59e5e5d9edb8dc88f32ccba5119961411db1ca628d23dcc1abe46d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19dc756326b5cf21ce11e8dff10aa46231890747bea9233fb6be6965f567b4a2(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2d712b91d80a7bc9d45be651c5fe31f2db583d94e01bb68d0bd31993713198c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51a155107aaab7c778604aac3a6f794381680322a023c3538862a5f06b30b92b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9cc1a2fe3014ad55e78d4638cf1e018bc2720690c1d23d7ef6ce40cd0d7956b6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8fb454f71a78c55f953ba7fe2ceec44ae6b5525b41d230bad9af2e67e70c5a4(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    connections: typing.Union[MongoClusterConnections, typing.Dict[builtins.str, typing.Any]],
    credentials: typing.Union[MongoClusterCredentials, typing.Dict[builtins.str, typing.Any]],
    display_name: builtins.str,
    instances: jsii.Number,
    location: builtins.str,
    mongodb_version: builtins.str,
    template_id: builtins.str,
    id: typing.Optional[builtins.str] = None,
    maintenance_window: typing.Optional[typing.Union[MongoClusterMaintenanceWindow, typing.Dict[builtins.str, typing.Any]]] = None,
    timeouts: typing.Optional[typing.Union[MongoClusterTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef7c56af8c323083878e68eb0a14d8ceb4919a475185b1a0d2a31901c56ec507(
    *,
    cidr_list: typing.Sequence[builtins.str],
    datacenter_id: builtins.str,
    lan_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e314a3307e0a8c064c7f30b26fc884ef154ab3344f0193966f8b4a5e6c2fe182(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a82343f2d30b87fd592e819a8b4280d70dc881d5c48316d79f5beca6e9cc0888(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f5c28b3eb998d51e786648d9bffb45023a639e9c46e3f0785a7b4151808a52e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8eeee68c96f4a24ddde42dc4ffd3f38a875858b3610e776b4e44cf5ec7408364(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccff2c6267ce769672f1eb1b527f9f13e1224c17849c96cf336609fc9b766935(
    value: typing.Optional[MongoClusterConnections],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd596e77ddabfeaab94440fa1cb0f018fc77ffae23cdd85281d35be956303a36(
    *,
    password: builtins.str,
    username: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3c22fb5840927a8d01154ab079b9d17d11e5ac2f715383082710a3236f56218(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c5383566ed4b87b116cf6d31771f751e8b7e0dfb8671a068fef641e0c15a70f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__621ff0d10adc831fdb3a83e2a6115c68f668bf02ff9f036c2c53f88625749da6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16731cc0f6bd6b604ef50328c9a7940a9a7b1a1a4a95fa8a0450da45b354b5ad(
    value: typing.Optional[MongoClusterCredentials],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__421318b6ba20092a579d3f220b98f02358edef22f00eff2ae1356b9a601b903d(
    *,
    day_of_the_week: builtins.str,
    time: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11d51c6b9a2f02b86aeb4d8885b9cbb062f9e1e490f330bcf004237ca416d5e6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e0e03a1e507dfd09a5381beeb536ac06b19ed446e8464f8ad9952f0cc37b136(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b838f55e7721c42d86322ed9734d1a0a195fd3b8067831a1ae6a4f00d64e183d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84611be84595e1202f28d9790d284d2fa18480fdc255beb05e3626874cfb204c(
    value: typing.Optional[MongoClusterMaintenanceWindow],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6085053f4064a51de0be39081bc634b1f0448b8ea5f556a80b31862027995ca(
    *,
    create: typing.Optional[builtins.str] = None,
    default: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9286af292886504f9b37a019491d019d245d39d15633ad593e2d58bcf6ce53c8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__158561af1d8b4d346a01dc917df64946880d4d9a7d0b9f4bb45e5341daf9d5c0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00c66f738ae251306b54c21613f0bc7805e217f8bde87d51fdb5101858fb53f9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1d7bf9fa10ad374a66279bc9a46f566bf4b71adfb6336e372828be270c56f7a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a637fb1ce3343c360f888702a4f5c603da828839d43fc78f55be210dad95256c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bbf8b7bdd56ed86764046f529e0a62efc541da63c3849a9fbad65ba81f80713(
    value: typing.Optional[typing.Union[MongoClusterTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
