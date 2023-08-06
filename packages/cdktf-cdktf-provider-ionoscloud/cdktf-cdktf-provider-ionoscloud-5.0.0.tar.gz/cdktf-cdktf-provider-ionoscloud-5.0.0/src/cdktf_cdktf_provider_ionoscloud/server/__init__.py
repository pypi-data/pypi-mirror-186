'''
# `ionoscloud_server`

Refer to the Terraform Registory for docs: [`ionoscloud_server`](https://www.terraform.io/docs/providers/ionoscloud/r/server).
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


class Server(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-ionoscloud.server.Server",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/ionoscloud/r/server ionoscloud_server}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        datacenter_id: builtins.str,
        name: builtins.str,
        nic: typing.Union["ServerNic", typing.Dict[builtins.str, typing.Any]],
        volume: typing.Union["ServerVolume", typing.Dict[builtins.str, typing.Any]],
        availability_zone: typing.Optional[builtins.str] = None,
        boot_cdrom: typing.Optional[builtins.str] = None,
        boot_image: typing.Optional[builtins.str] = None,
        cores: typing.Optional[jsii.Number] = None,
        cpu_family: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        image_name: typing.Optional[builtins.str] = None,
        image_password: typing.Optional[builtins.str] = None,
        ram: typing.Optional[jsii.Number] = None,
        ssh_key_path: typing.Optional[typing.Sequence[builtins.str]] = None,
        template_uuid: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["ServerTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        type: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/ionoscloud/r/server ionoscloud_server} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param datacenter_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#datacenter_id Server#datacenter_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#name Server#name}.
        :param nic: nic block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#nic Server#nic}
        :param volume: volume block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#volume Server#volume}
        :param availability_zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#availability_zone Server#availability_zone}.
        :param boot_cdrom: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#boot_cdrom Server#boot_cdrom}.
        :param boot_image: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#boot_image Server#boot_image}.
        :param cores: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#cores Server#cores}.
        :param cpu_family: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#cpu_family Server#cpu_family}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#id Server#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param image_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#image_name Server#image_name}.
        :param image_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#image_password Server#image_password}.
        :param ram: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#ram Server#ram}.
        :param ssh_key_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#ssh_key_path Server#ssh_key_path}.
        :param template_uuid: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#template_uuid Server#template_uuid}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#timeouts Server#timeouts}
        :param type: server usages: ENTERPRISE or CUBE. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#type Server#type}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2a0c6ec6dcb3a1e07a0f940d7d1481dc2a214ea66934d51fe05a0166a1aa493)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ServerConfig(
            datacenter_id=datacenter_id,
            name=name,
            nic=nic,
            volume=volume,
            availability_zone=availability_zone,
            boot_cdrom=boot_cdrom,
            boot_image=boot_image,
            cores=cores,
            cpu_family=cpu_family,
            id=id,
            image_name=image_name,
            image_password=image_password,
            ram=ram,
            ssh_key_path=ssh_key_path,
            template_uuid=template_uuid,
            timeouts=timeouts,
            type=type,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putNic")
    def put_nic(
        self,
        *,
        lan: jsii.Number,
        dhcp: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        firewall: typing.Optional[typing.Union["ServerNicFirewall", typing.Dict[builtins.str, typing.Any]]] = None,
        firewall_active: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        firewall_type: typing.Optional[builtins.str] = None,
        ips: typing.Optional[typing.Sequence[builtins.str]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param lan: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#lan Server#lan}.
        :param dhcp: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#dhcp Server#dhcp}.
        :param firewall: firewall block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#firewall Server#firewall}
        :param firewall_active: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#firewall_active Server#firewall_active}.
        :param firewall_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#firewall_type Server#firewall_type}.
        :param ips: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#ips Server#ips}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#name Server#name}.
        '''
        value = ServerNic(
            lan=lan,
            dhcp=dhcp,
            firewall=firewall,
            firewall_active=firewall_active,
            firewall_type=firewall_type,
            ips=ips,
            name=name,
        )

        return typing.cast(None, jsii.invoke(self, "putNic", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#create Server#create}.
        :param default: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#default Server#default}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#delete Server#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#update Server#update}.
        '''
        value = ServerTimeouts(
            create=create, default=default, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putVolume")
    def put_volume(
        self,
        *,
        disk_type: builtins.str,
        availability_zone: typing.Optional[builtins.str] = None,
        backup_unit_id: typing.Optional[builtins.str] = None,
        bus: typing.Optional[builtins.str] = None,
        image_password: typing.Optional[builtins.str] = None,
        licence_type: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        size: typing.Optional[jsii.Number] = None,
        ssh_key_path: typing.Optional[typing.Sequence[builtins.str]] = None,
        user_data: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param disk_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#disk_type Server#disk_type}.
        :param availability_zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#availability_zone Server#availability_zone}.
        :param backup_unit_id: The uuid of the Backup Unit that user has access to. The property is immutable and is only allowed to be set on a new volume creation. It is mandatory to provide either 'public image' or 'imageAlias' in conjunction with this property. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#backup_unit_id Server#backup_unit_id}
        :param bus: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#bus Server#bus}.
        :param image_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#image_password Server#image_password}.
        :param licence_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#licence_type Server#licence_type}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#name Server#name}.
        :param size: The size of the volume in GB. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#size Server#size}
        :param ssh_key_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#ssh_key_path Server#ssh_key_path}.
        :param user_data: The cloud-init configuration for the volume as base64 encoded string. The property is immutable and is only allowed to be set on a new volume creation. It is mandatory to provide either 'public image' or 'imageAlias' that has cloud-init compatibility in conjunction with this property. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#user_data Server#user_data}
        '''
        value = ServerVolume(
            disk_type=disk_type,
            availability_zone=availability_zone,
            backup_unit_id=backup_unit_id,
            bus=bus,
            image_password=image_password,
            licence_type=licence_type,
            name=name,
            size=size,
            ssh_key_path=ssh_key_path,
            user_data=user_data,
        )

        return typing.cast(None, jsii.invoke(self, "putVolume", [value]))

    @jsii.member(jsii_name="resetAvailabilityZone")
    def reset_availability_zone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAvailabilityZone", []))

    @jsii.member(jsii_name="resetBootCdrom")
    def reset_boot_cdrom(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBootCdrom", []))

    @jsii.member(jsii_name="resetBootImage")
    def reset_boot_image(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBootImage", []))

    @jsii.member(jsii_name="resetCores")
    def reset_cores(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCores", []))

    @jsii.member(jsii_name="resetCpuFamily")
    def reset_cpu_family(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCpuFamily", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetImageName")
    def reset_image_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImageName", []))

    @jsii.member(jsii_name="resetImagePassword")
    def reset_image_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImagePassword", []))

    @jsii.member(jsii_name="resetRam")
    def reset_ram(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRam", []))

    @jsii.member(jsii_name="resetSshKeyPath")
    def reset_ssh_key_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSshKeyPath", []))

    @jsii.member(jsii_name="resetTemplateUuid")
    def reset_template_uuid(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTemplateUuid", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="bootVolume")
    def boot_volume(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bootVolume"))

    @builtins.property
    @jsii.member(jsii_name="firewallruleId")
    def firewallrule_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "firewallruleId"))

    @builtins.property
    @jsii.member(jsii_name="nic")
    def nic(self) -> "ServerNicOutputReference":
        return typing.cast("ServerNicOutputReference", jsii.get(self, "nic"))

    @builtins.property
    @jsii.member(jsii_name="primaryIp")
    def primary_ip(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primaryIp"))

    @builtins.property
    @jsii.member(jsii_name="primaryNic")
    def primary_nic(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primaryNic"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "ServerTimeoutsOutputReference":
        return typing.cast("ServerTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="volume")
    def volume(self) -> "ServerVolumeOutputReference":
        return typing.cast("ServerVolumeOutputReference", jsii.get(self, "volume"))

    @builtins.property
    @jsii.member(jsii_name="availabilityZoneInput")
    def availability_zone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilityZoneInput"))

    @builtins.property
    @jsii.member(jsii_name="bootCdromInput")
    def boot_cdrom_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bootCdromInput"))

    @builtins.property
    @jsii.member(jsii_name="bootImageInput")
    def boot_image_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bootImageInput"))

    @builtins.property
    @jsii.member(jsii_name="coresInput")
    def cores_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "coresInput"))

    @builtins.property
    @jsii.member(jsii_name="cpuFamilyInput")
    def cpu_family_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cpuFamilyInput"))

    @builtins.property
    @jsii.member(jsii_name="datacenterIdInput")
    def datacenter_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datacenterIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="imageNameInput")
    def image_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageNameInput"))

    @builtins.property
    @jsii.member(jsii_name="imagePasswordInput")
    def image_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imagePasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="nicInput")
    def nic_input(self) -> typing.Optional["ServerNic"]:
        return typing.cast(typing.Optional["ServerNic"], jsii.get(self, "nicInput"))

    @builtins.property
    @jsii.member(jsii_name="ramInput")
    def ram_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ramInput"))

    @builtins.property
    @jsii.member(jsii_name="sshKeyPathInput")
    def ssh_key_path_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sshKeyPathInput"))

    @builtins.property
    @jsii.member(jsii_name="templateUuidInput")
    def template_uuid_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "templateUuidInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["ServerTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["ServerTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeInput")
    def volume_input(self) -> typing.Optional["ServerVolume"]:
        return typing.cast(typing.Optional["ServerVolume"], jsii.get(self, "volumeInput"))

    @builtins.property
    @jsii.member(jsii_name="availabilityZone")
    def availability_zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "availabilityZone"))

    @availability_zone.setter
    def availability_zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c40e8bf10013b101c5c122436bd17ec845753ece42395e8973b27a2fab69f4f0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilityZone", value)

    @builtins.property
    @jsii.member(jsii_name="bootCdrom")
    def boot_cdrom(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bootCdrom"))

    @boot_cdrom.setter
    def boot_cdrom(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3fd3c9596f20e7ffa3aa73c0b22e498e172a37364fcd7bd3857e4afc03da5a5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bootCdrom", value)

    @builtins.property
    @jsii.member(jsii_name="bootImage")
    def boot_image(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bootImage"))

    @boot_image.setter
    def boot_image(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f930c79c58e86c71938382e75b68e46615646afc18cd80585f183487a769edea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bootImage", value)

    @builtins.property
    @jsii.member(jsii_name="cores")
    def cores(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cores"))

    @cores.setter
    def cores(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b40226fb89e488105e341bad05b1157bd2217a6719bb0e523a0e9ddba792dabf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cores", value)

    @builtins.property
    @jsii.member(jsii_name="cpuFamily")
    def cpu_family(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cpuFamily"))

    @cpu_family.setter
    def cpu_family(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__731155d18763f0282f662298ac88dddb34ced7fb542a1e698e2886cb8b87a163)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpuFamily", value)

    @builtins.property
    @jsii.member(jsii_name="datacenterId")
    def datacenter_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datacenterId"))

    @datacenter_id.setter
    def datacenter_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77b17aa73ca68cebab214ab381c4af5668edc0f6db5a815468b06797045c063d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datacenterId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__330462605e3e6d1d020e339d2a99eedd88c7daf23b3d730d4c8165692f7d9bf6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="imageName")
    def image_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "imageName"))

    @image_name.setter
    def image_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4658431f765ad191ab9a055be7492327a68a2d940ae81b80b7cf0517a7b8bd5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageName", value)

    @builtins.property
    @jsii.member(jsii_name="imagePassword")
    def image_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "imagePassword"))

    @image_password.setter
    def image_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53ef6bbf20814c35bd53fbbf8db1aaccd070634f02860689aa2c2aaa5b56a387)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imagePassword", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dbff757f49b27e1ccd6e20ae6e826ba42c07006ad5f197bc49cc067b4584558c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="ram")
    def ram(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ram"))

    @ram.setter
    def ram(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd8b82d0664ddc62aac16874051ea124bcea5619aacdbd5504f38489edbc3192)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ram", value)

    @builtins.property
    @jsii.member(jsii_name="sshKeyPath")
    def ssh_key_path(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sshKeyPath"))

    @ssh_key_path.setter
    def ssh_key_path(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b8b5c2b21c12f9ccd9b8fe055a31a5bb04c06b8fb46b7b6fbd65edc757f9f97)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sshKeyPath", value)

    @builtins.property
    @jsii.member(jsii_name="templateUuid")
    def template_uuid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "templateUuid"))

    @template_uuid.setter
    def template_uuid(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9483f26fb4dc1d9c1f90bcced0a85d5cd7fd5f2883d0bda390c8cf4340203d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "templateUuid", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e314d6600c97c9a4ba14a77d1f8be8e5cde26c791d796aebdee514ccb1d137a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-ionoscloud.server.ServerConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "datacenter_id": "datacenterId",
        "name": "name",
        "nic": "nic",
        "volume": "volume",
        "availability_zone": "availabilityZone",
        "boot_cdrom": "bootCdrom",
        "boot_image": "bootImage",
        "cores": "cores",
        "cpu_family": "cpuFamily",
        "id": "id",
        "image_name": "imageName",
        "image_password": "imagePassword",
        "ram": "ram",
        "ssh_key_path": "sshKeyPath",
        "template_uuid": "templateUuid",
        "timeouts": "timeouts",
        "type": "type",
    },
)
class ServerConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        datacenter_id: builtins.str,
        name: builtins.str,
        nic: typing.Union["ServerNic", typing.Dict[builtins.str, typing.Any]],
        volume: typing.Union["ServerVolume", typing.Dict[builtins.str, typing.Any]],
        availability_zone: typing.Optional[builtins.str] = None,
        boot_cdrom: typing.Optional[builtins.str] = None,
        boot_image: typing.Optional[builtins.str] = None,
        cores: typing.Optional[jsii.Number] = None,
        cpu_family: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        image_name: typing.Optional[builtins.str] = None,
        image_password: typing.Optional[builtins.str] = None,
        ram: typing.Optional[jsii.Number] = None,
        ssh_key_path: typing.Optional[typing.Sequence[builtins.str]] = None,
        template_uuid: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["ServerTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param datacenter_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#datacenter_id Server#datacenter_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#name Server#name}.
        :param nic: nic block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#nic Server#nic}
        :param volume: volume block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#volume Server#volume}
        :param availability_zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#availability_zone Server#availability_zone}.
        :param boot_cdrom: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#boot_cdrom Server#boot_cdrom}.
        :param boot_image: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#boot_image Server#boot_image}.
        :param cores: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#cores Server#cores}.
        :param cpu_family: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#cpu_family Server#cpu_family}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#id Server#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param image_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#image_name Server#image_name}.
        :param image_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#image_password Server#image_password}.
        :param ram: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#ram Server#ram}.
        :param ssh_key_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#ssh_key_path Server#ssh_key_path}.
        :param template_uuid: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#template_uuid Server#template_uuid}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#timeouts Server#timeouts}
        :param type: server usages: ENTERPRISE or CUBE. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#type Server#type}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(nic, dict):
            nic = ServerNic(**nic)
        if isinstance(volume, dict):
            volume = ServerVolume(**volume)
        if isinstance(timeouts, dict):
            timeouts = ServerTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2400b7d4c9d1d0d94d05866887b5445902c000ecaccf00650d0380ea4e52e4ee)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument datacenter_id", value=datacenter_id, expected_type=type_hints["datacenter_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument nic", value=nic, expected_type=type_hints["nic"])
            check_type(argname="argument volume", value=volume, expected_type=type_hints["volume"])
            check_type(argname="argument availability_zone", value=availability_zone, expected_type=type_hints["availability_zone"])
            check_type(argname="argument boot_cdrom", value=boot_cdrom, expected_type=type_hints["boot_cdrom"])
            check_type(argname="argument boot_image", value=boot_image, expected_type=type_hints["boot_image"])
            check_type(argname="argument cores", value=cores, expected_type=type_hints["cores"])
            check_type(argname="argument cpu_family", value=cpu_family, expected_type=type_hints["cpu_family"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument image_name", value=image_name, expected_type=type_hints["image_name"])
            check_type(argname="argument image_password", value=image_password, expected_type=type_hints["image_password"])
            check_type(argname="argument ram", value=ram, expected_type=type_hints["ram"])
            check_type(argname="argument ssh_key_path", value=ssh_key_path, expected_type=type_hints["ssh_key_path"])
            check_type(argname="argument template_uuid", value=template_uuid, expected_type=type_hints["template_uuid"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "datacenter_id": datacenter_id,
            "name": name,
            "nic": nic,
            "volume": volume,
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
        if availability_zone is not None:
            self._values["availability_zone"] = availability_zone
        if boot_cdrom is not None:
            self._values["boot_cdrom"] = boot_cdrom
        if boot_image is not None:
            self._values["boot_image"] = boot_image
        if cores is not None:
            self._values["cores"] = cores
        if cpu_family is not None:
            self._values["cpu_family"] = cpu_family
        if id is not None:
            self._values["id"] = id
        if image_name is not None:
            self._values["image_name"] = image_name
        if image_password is not None:
            self._values["image_password"] = image_password
        if ram is not None:
            self._values["ram"] = ram
        if ssh_key_path is not None:
            self._values["ssh_key_path"] = ssh_key_path
        if template_uuid is not None:
            self._values["template_uuid"] = template_uuid
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if type is not None:
            self._values["type"] = type

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
    def datacenter_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#datacenter_id Server#datacenter_id}.'''
        result = self._values.get("datacenter_id")
        assert result is not None, "Required property 'datacenter_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#name Server#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def nic(self) -> "ServerNic":
        '''nic block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#nic Server#nic}
        '''
        result = self._values.get("nic")
        assert result is not None, "Required property 'nic' is missing"
        return typing.cast("ServerNic", result)

    @builtins.property
    def volume(self) -> "ServerVolume":
        '''volume block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#volume Server#volume}
        '''
        result = self._values.get("volume")
        assert result is not None, "Required property 'volume' is missing"
        return typing.cast("ServerVolume", result)

    @builtins.property
    def availability_zone(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#availability_zone Server#availability_zone}.'''
        result = self._values.get("availability_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def boot_cdrom(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#boot_cdrom Server#boot_cdrom}.'''
        result = self._values.get("boot_cdrom")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def boot_image(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#boot_image Server#boot_image}.'''
        result = self._values.get("boot_image")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cores(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#cores Server#cores}.'''
        result = self._values.get("cores")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def cpu_family(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#cpu_family Server#cpu_family}.'''
        result = self._values.get("cpu_family")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#id Server#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def image_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#image_name Server#image_name}.'''
        result = self._values.get("image_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def image_password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#image_password Server#image_password}.'''
        result = self._values.get("image_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ram(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#ram Server#ram}.'''
        result = self._values.get("ram")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ssh_key_path(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#ssh_key_path Server#ssh_key_path}.'''
        result = self._values.get("ssh_key_path")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def template_uuid(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#template_uuid Server#template_uuid}.'''
        result = self._values.get("template_uuid")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["ServerTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#timeouts Server#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["ServerTimeouts"], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''server usages: ENTERPRISE or CUBE.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#type Server#type}
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-ionoscloud.server.ServerNic",
    jsii_struct_bases=[],
    name_mapping={
        "lan": "lan",
        "dhcp": "dhcp",
        "firewall": "firewall",
        "firewall_active": "firewallActive",
        "firewall_type": "firewallType",
        "ips": "ips",
        "name": "name",
    },
)
class ServerNic:
    def __init__(
        self,
        *,
        lan: jsii.Number,
        dhcp: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        firewall: typing.Optional[typing.Union["ServerNicFirewall", typing.Dict[builtins.str, typing.Any]]] = None,
        firewall_active: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        firewall_type: typing.Optional[builtins.str] = None,
        ips: typing.Optional[typing.Sequence[builtins.str]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param lan: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#lan Server#lan}.
        :param dhcp: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#dhcp Server#dhcp}.
        :param firewall: firewall block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#firewall Server#firewall}
        :param firewall_active: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#firewall_active Server#firewall_active}.
        :param firewall_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#firewall_type Server#firewall_type}.
        :param ips: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#ips Server#ips}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#name Server#name}.
        '''
        if isinstance(firewall, dict):
            firewall = ServerNicFirewall(**firewall)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2d8426508d3f02c55a616c8e4d652773e3efed9b07cf7c155f21d788d1f78ae)
            check_type(argname="argument lan", value=lan, expected_type=type_hints["lan"])
            check_type(argname="argument dhcp", value=dhcp, expected_type=type_hints["dhcp"])
            check_type(argname="argument firewall", value=firewall, expected_type=type_hints["firewall"])
            check_type(argname="argument firewall_active", value=firewall_active, expected_type=type_hints["firewall_active"])
            check_type(argname="argument firewall_type", value=firewall_type, expected_type=type_hints["firewall_type"])
            check_type(argname="argument ips", value=ips, expected_type=type_hints["ips"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "lan": lan,
        }
        if dhcp is not None:
            self._values["dhcp"] = dhcp
        if firewall is not None:
            self._values["firewall"] = firewall
        if firewall_active is not None:
            self._values["firewall_active"] = firewall_active
        if firewall_type is not None:
            self._values["firewall_type"] = firewall_type
        if ips is not None:
            self._values["ips"] = ips
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def lan(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#lan Server#lan}.'''
        result = self._values.get("lan")
        assert result is not None, "Required property 'lan' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def dhcp(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#dhcp Server#dhcp}.'''
        result = self._values.get("dhcp")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def firewall(self) -> typing.Optional["ServerNicFirewall"]:
        '''firewall block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#firewall Server#firewall}
        '''
        result = self._values.get("firewall")
        return typing.cast(typing.Optional["ServerNicFirewall"], result)

    @builtins.property
    def firewall_active(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#firewall_active Server#firewall_active}.'''
        result = self._values.get("firewall_active")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def firewall_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#firewall_type Server#firewall_type}.'''
        result = self._values.get("firewall_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ips(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#ips Server#ips}.'''
        result = self._values.get("ips")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#name Server#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServerNic(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-ionoscloud.server.ServerNicFirewall",
    jsii_struct_bases=[],
    name_mapping={
        "protocol": "protocol",
        "icmp_code": "icmpCode",
        "icmp_type": "icmpType",
        "name": "name",
        "port_range_end": "portRangeEnd",
        "port_range_start": "portRangeStart",
        "source_ip": "sourceIp",
        "source_mac": "sourceMac",
        "target_ip": "targetIp",
        "type": "type",
    },
)
class ServerNicFirewall:
    def __init__(
        self,
        *,
        protocol: builtins.str,
        icmp_code: typing.Optional[builtins.str] = None,
        icmp_type: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        port_range_end: typing.Optional[jsii.Number] = None,
        port_range_start: typing.Optional[jsii.Number] = None,
        source_ip: typing.Optional[builtins.str] = None,
        source_mac: typing.Optional[builtins.str] = None,
        target_ip: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#protocol Server#protocol}.
        :param icmp_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#icmp_code Server#icmp_code}.
        :param icmp_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#icmp_type Server#icmp_type}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#name Server#name}.
        :param port_range_end: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#port_range_end Server#port_range_end}.
        :param port_range_start: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#port_range_start Server#port_range_start}.
        :param source_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#source_ip Server#source_ip}.
        :param source_mac: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#source_mac Server#source_mac}.
        :param target_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#target_ip Server#target_ip}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#type Server#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14250c4e60ed029940154d0f58fa445c8a6baf10d212f9c9c37dc04848e35e48)
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument icmp_code", value=icmp_code, expected_type=type_hints["icmp_code"])
            check_type(argname="argument icmp_type", value=icmp_type, expected_type=type_hints["icmp_type"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument port_range_end", value=port_range_end, expected_type=type_hints["port_range_end"])
            check_type(argname="argument port_range_start", value=port_range_start, expected_type=type_hints["port_range_start"])
            check_type(argname="argument source_ip", value=source_ip, expected_type=type_hints["source_ip"])
            check_type(argname="argument source_mac", value=source_mac, expected_type=type_hints["source_mac"])
            check_type(argname="argument target_ip", value=target_ip, expected_type=type_hints["target_ip"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "protocol": protocol,
        }
        if icmp_code is not None:
            self._values["icmp_code"] = icmp_code
        if icmp_type is not None:
            self._values["icmp_type"] = icmp_type
        if name is not None:
            self._values["name"] = name
        if port_range_end is not None:
            self._values["port_range_end"] = port_range_end
        if port_range_start is not None:
            self._values["port_range_start"] = port_range_start
        if source_ip is not None:
            self._values["source_ip"] = source_ip
        if source_mac is not None:
            self._values["source_mac"] = source_mac
        if target_ip is not None:
            self._values["target_ip"] = target_ip
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def protocol(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#protocol Server#protocol}.'''
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def icmp_code(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#icmp_code Server#icmp_code}.'''
        result = self._values.get("icmp_code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def icmp_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#icmp_type Server#icmp_type}.'''
        result = self._values.get("icmp_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#name Server#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port_range_end(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#port_range_end Server#port_range_end}.'''
        result = self._values.get("port_range_end")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def port_range_start(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#port_range_start Server#port_range_start}.'''
        result = self._values.get("port_range_start")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def source_ip(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#source_ip Server#source_ip}.'''
        result = self._values.get("source_ip")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_mac(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#source_mac Server#source_mac}.'''
        result = self._values.get("source_mac")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_ip(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#target_ip Server#target_ip}.'''
        result = self._values.get("target_ip")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#type Server#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServerNicFirewall(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServerNicFirewallOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-ionoscloud.server.ServerNicFirewallOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0d297e7258a8cc85fa8a839950b10cc07c86614cdeab35d5eb10462ba914d934)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIcmpCode")
    def reset_icmp_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIcmpCode", []))

    @jsii.member(jsii_name="resetIcmpType")
    def reset_icmp_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIcmpType", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetPortRangeEnd")
    def reset_port_range_end(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPortRangeEnd", []))

    @jsii.member(jsii_name="resetPortRangeStart")
    def reset_port_range_start(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPortRangeStart", []))

    @jsii.member(jsii_name="resetSourceIp")
    def reset_source_ip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceIp", []))

    @jsii.member(jsii_name="resetSourceMac")
    def reset_source_mac(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceMac", []))

    @jsii.member(jsii_name="resetTargetIp")
    def reset_target_ip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetIp", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="icmpCodeInput")
    def icmp_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "icmpCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="icmpTypeInput")
    def icmp_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "icmpTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="portRangeEndInput")
    def port_range_end_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portRangeEndInput"))

    @builtins.property
    @jsii.member(jsii_name="portRangeStartInput")
    def port_range_start_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portRangeStartInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceIpInput")
    def source_ip_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceIpInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceMacInput")
    def source_mac_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceMacInput"))

    @builtins.property
    @jsii.member(jsii_name="targetIpInput")
    def target_ip_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetIpInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="icmpCode")
    def icmp_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "icmpCode"))

    @icmp_code.setter
    def icmp_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2aa5830b3483ebe46a70f3affa39df77c0bcbed351a5681ed67966aec28bc57)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "icmpCode", value)

    @builtins.property
    @jsii.member(jsii_name="icmpType")
    def icmp_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "icmpType"))

    @icmp_type.setter
    def icmp_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2cba88b1a7205304a78b352e54433dd2ee69966bb655125d43f61ff95e3a8871)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "icmpType", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a47f58a908e0d9ced08f6f7d2b4d64e4afb926356509ebb411cf6f1d998e7db7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="portRangeEnd")
    def port_range_end(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "portRangeEnd"))

    @port_range_end.setter
    def port_range_end(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bafa074f49a8e309695cde57921a187a6caf09abd6f8045443ef36a82964a04e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "portRangeEnd", value)

    @builtins.property
    @jsii.member(jsii_name="portRangeStart")
    def port_range_start(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "portRangeStart"))

    @port_range_start.setter
    def port_range_start(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__455296888f78db790aab26fbc54a165a45801f570a767b4fef7172b241e1d752)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "portRangeStart", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c3bf76fb7027c206935b8f1ded59912bdb99431526744b2db72bd7ff7e76c21)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="sourceIp")
    def source_ip(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceIp"))

    @source_ip.setter
    def source_ip(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da23071b46e3d8504625af34c54b9eda803d3581732ca2f415984054314d8261)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceIp", value)

    @builtins.property
    @jsii.member(jsii_name="sourceMac")
    def source_mac(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceMac"))

    @source_mac.setter
    def source_mac(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc84fcf6bfe187cdfdfdbd659d26c0c51b6aff446f11eabdee25817e7f81ce11)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceMac", value)

    @builtins.property
    @jsii.member(jsii_name="targetIp")
    def target_ip(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetIp"))

    @target_ip.setter
    def target_ip(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19d3fbe12c30a2a5e03dd882e16561baa4b6faccb77bcead47eb98db342587f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetIp", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5693126bc17a77034013ca1917fd396c0410c7fc34abfe3b24286f4e6859f61e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ServerNicFirewall]:
        return typing.cast(typing.Optional[ServerNicFirewall], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ServerNicFirewall]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__395ed72147c19bce1f68db1bc549693523cc4a12b205d93df788fa8e5d1d886f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ServerNicOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-ionoscloud.server.ServerNicOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f41472e5a11b6b0e11dce08d677ae47611daf07ec43aa28b524b8036b4cb6dc1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putFirewall")
    def put_firewall(
        self,
        *,
        protocol: builtins.str,
        icmp_code: typing.Optional[builtins.str] = None,
        icmp_type: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        port_range_end: typing.Optional[jsii.Number] = None,
        port_range_start: typing.Optional[jsii.Number] = None,
        source_ip: typing.Optional[builtins.str] = None,
        source_mac: typing.Optional[builtins.str] = None,
        target_ip: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#protocol Server#protocol}.
        :param icmp_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#icmp_code Server#icmp_code}.
        :param icmp_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#icmp_type Server#icmp_type}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#name Server#name}.
        :param port_range_end: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#port_range_end Server#port_range_end}.
        :param port_range_start: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#port_range_start Server#port_range_start}.
        :param source_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#source_ip Server#source_ip}.
        :param source_mac: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#source_mac Server#source_mac}.
        :param target_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#target_ip Server#target_ip}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#type Server#type}.
        '''
        value = ServerNicFirewall(
            protocol=protocol,
            icmp_code=icmp_code,
            icmp_type=icmp_type,
            name=name,
            port_range_end=port_range_end,
            port_range_start=port_range_start,
            source_ip=source_ip,
            source_mac=source_mac,
            target_ip=target_ip,
            type=type,
        )

        return typing.cast(None, jsii.invoke(self, "putFirewall", [value]))

    @jsii.member(jsii_name="resetDhcp")
    def reset_dhcp(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDhcp", []))

    @jsii.member(jsii_name="resetFirewall")
    def reset_firewall(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFirewall", []))

    @jsii.member(jsii_name="resetFirewallActive")
    def reset_firewall_active(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFirewallActive", []))

    @jsii.member(jsii_name="resetFirewallType")
    def reset_firewall_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFirewallType", []))

    @jsii.member(jsii_name="resetIps")
    def reset_ips(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIps", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="deviceNumber")
    def device_number(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "deviceNumber"))

    @builtins.property
    @jsii.member(jsii_name="firewall")
    def firewall(self) -> ServerNicFirewallOutputReference:
        return typing.cast(ServerNicFirewallOutputReference, jsii.get(self, "firewall"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="mac")
    def mac(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mac"))

    @builtins.property
    @jsii.member(jsii_name="pciSlot")
    def pci_slot(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "pciSlot"))

    @builtins.property
    @jsii.member(jsii_name="dhcpInput")
    def dhcp_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "dhcpInput"))

    @builtins.property
    @jsii.member(jsii_name="firewallActiveInput")
    def firewall_active_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "firewallActiveInput"))

    @builtins.property
    @jsii.member(jsii_name="firewallInput")
    def firewall_input(self) -> typing.Optional[ServerNicFirewall]:
        return typing.cast(typing.Optional[ServerNicFirewall], jsii.get(self, "firewallInput"))

    @builtins.property
    @jsii.member(jsii_name="firewallTypeInput")
    def firewall_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "firewallTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="ipsInput")
    def ips_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "ipsInput"))

    @builtins.property
    @jsii.member(jsii_name="lanInput")
    def lan_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "lanInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="dhcp")
    def dhcp(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "dhcp"))

    @dhcp.setter
    def dhcp(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca593f83be0f20cdda731839123992c98b22aceaaf85a7ce7f486df3de005afa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dhcp", value)

    @builtins.property
    @jsii.member(jsii_name="firewallActive")
    def firewall_active(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "firewallActive"))

    @firewall_active.setter
    def firewall_active(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__374a3efef93f7d8f4333da4bfb5762670f621059254b704475dca63364ddcf03)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firewallActive", value)

    @builtins.property
    @jsii.member(jsii_name="firewallType")
    def firewall_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "firewallType"))

    @firewall_type.setter
    def firewall_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce3adffeb68a647eaa966f0380939ea8fe9b1ab159f01e409613ec99279ea9bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firewallType", value)

    @builtins.property
    @jsii.member(jsii_name="ips")
    def ips(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ips"))

    @ips.setter
    def ips(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70f4929730f5a009d652b4fd1e42890a58131dc1d4f99751759d61c3cd766f5a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ips", value)

    @builtins.property
    @jsii.member(jsii_name="lan")
    def lan(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "lan"))

    @lan.setter
    def lan(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ecdcf439efae018b1f118d31d43fada644a5e7c428e1d5ebf4d6de1e14dbac0b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lan", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99bcb671e3548aed5be8ccadb3dacdb63ac958bd45f46d516c4e3d7a8c12cac4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ServerNic]:
        return typing.cast(typing.Optional[ServerNic], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ServerNic]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3af5d9673a8183dc13e3a32fcefebba43cc290ab1550d07f59d5ba7f8ca981a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-ionoscloud.server.ServerTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "default": "default",
        "delete": "delete",
        "update": "update",
    },
)
class ServerTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        default: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#create Server#create}.
        :param default: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#default Server#default}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#delete Server#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#update Server#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9715f9f91828a802039eac63a25c973bd56edc373942d1afd41dfeaa583e3e0)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#create Server#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#default Server#default}.'''
        result = self._values.get("default")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#delete Server#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#update Server#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServerTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServerTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-ionoscloud.server.ServerTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1f84e5e2010b08f12a68eb28cd123b7557114c594b502bdbfa23a22cd377f8f9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9dd96344b5d7c98d17227e504754fe11c27f4d9476b4ca57b21aceaaf67d0a4d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="default")
    def default(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "default"))

    @default.setter
    def default(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ce22705a93219ce9a3c7509167b42f0311dc36647ed2ec653788b06203081a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "default", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c19dacf8b47bf889af69c7a1fecbecf2664877fda80e206c25c7e8bc7f83eda5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bff7f587911914dd2fb6b3e8537129e1274e3b12d6692e1fda996bd40b19fc72)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ServerTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ServerTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ServerTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40500c3dd1b0237c1997c51c78f087e0973414bb3caef29abeeb1c42cee53c53)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-ionoscloud.server.ServerVolume",
    jsii_struct_bases=[],
    name_mapping={
        "disk_type": "diskType",
        "availability_zone": "availabilityZone",
        "backup_unit_id": "backupUnitId",
        "bus": "bus",
        "image_password": "imagePassword",
        "licence_type": "licenceType",
        "name": "name",
        "size": "size",
        "ssh_key_path": "sshKeyPath",
        "user_data": "userData",
    },
)
class ServerVolume:
    def __init__(
        self,
        *,
        disk_type: builtins.str,
        availability_zone: typing.Optional[builtins.str] = None,
        backup_unit_id: typing.Optional[builtins.str] = None,
        bus: typing.Optional[builtins.str] = None,
        image_password: typing.Optional[builtins.str] = None,
        licence_type: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        size: typing.Optional[jsii.Number] = None,
        ssh_key_path: typing.Optional[typing.Sequence[builtins.str]] = None,
        user_data: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param disk_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#disk_type Server#disk_type}.
        :param availability_zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#availability_zone Server#availability_zone}.
        :param backup_unit_id: The uuid of the Backup Unit that user has access to. The property is immutable and is only allowed to be set on a new volume creation. It is mandatory to provide either 'public image' or 'imageAlias' in conjunction with this property. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#backup_unit_id Server#backup_unit_id}
        :param bus: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#bus Server#bus}.
        :param image_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#image_password Server#image_password}.
        :param licence_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#licence_type Server#licence_type}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#name Server#name}.
        :param size: The size of the volume in GB. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#size Server#size}
        :param ssh_key_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#ssh_key_path Server#ssh_key_path}.
        :param user_data: The cloud-init configuration for the volume as base64 encoded string. The property is immutable and is only allowed to be set on a new volume creation. It is mandatory to provide either 'public image' or 'imageAlias' that has cloud-init compatibility in conjunction with this property. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#user_data Server#user_data}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5da2e0361c7606090c866f3b9012311f26869d5b07a34d9a001a3905f8968ce)
            check_type(argname="argument disk_type", value=disk_type, expected_type=type_hints["disk_type"])
            check_type(argname="argument availability_zone", value=availability_zone, expected_type=type_hints["availability_zone"])
            check_type(argname="argument backup_unit_id", value=backup_unit_id, expected_type=type_hints["backup_unit_id"])
            check_type(argname="argument bus", value=bus, expected_type=type_hints["bus"])
            check_type(argname="argument image_password", value=image_password, expected_type=type_hints["image_password"])
            check_type(argname="argument licence_type", value=licence_type, expected_type=type_hints["licence_type"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument size", value=size, expected_type=type_hints["size"])
            check_type(argname="argument ssh_key_path", value=ssh_key_path, expected_type=type_hints["ssh_key_path"])
            check_type(argname="argument user_data", value=user_data, expected_type=type_hints["user_data"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "disk_type": disk_type,
        }
        if availability_zone is not None:
            self._values["availability_zone"] = availability_zone
        if backup_unit_id is not None:
            self._values["backup_unit_id"] = backup_unit_id
        if bus is not None:
            self._values["bus"] = bus
        if image_password is not None:
            self._values["image_password"] = image_password
        if licence_type is not None:
            self._values["licence_type"] = licence_type
        if name is not None:
            self._values["name"] = name
        if size is not None:
            self._values["size"] = size
        if ssh_key_path is not None:
            self._values["ssh_key_path"] = ssh_key_path
        if user_data is not None:
            self._values["user_data"] = user_data

    @builtins.property
    def disk_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#disk_type Server#disk_type}.'''
        result = self._values.get("disk_type")
        assert result is not None, "Required property 'disk_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def availability_zone(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#availability_zone Server#availability_zone}.'''
        result = self._values.get("availability_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def backup_unit_id(self) -> typing.Optional[builtins.str]:
        '''The uuid of the Backup Unit that user has access to.

        The property is immutable and is only allowed to be set on a new volume creation. It is mandatory to provide either 'public image' or 'imageAlias' in conjunction with this property.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#backup_unit_id Server#backup_unit_id}
        '''
        result = self._values.get("backup_unit_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bus(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#bus Server#bus}.'''
        result = self._values.get("bus")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def image_password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#image_password Server#image_password}.'''
        result = self._values.get("image_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def licence_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#licence_type Server#licence_type}.'''
        result = self._values.get("licence_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#name Server#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def size(self) -> typing.Optional[jsii.Number]:
        '''The size of the volume in GB.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#size Server#size}
        '''
        result = self._values.get("size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ssh_key_path(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#ssh_key_path Server#ssh_key_path}.'''
        result = self._values.get("ssh_key_path")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def user_data(self) -> typing.Optional[builtins.str]:
        '''The cloud-init configuration for the volume as base64 encoded string.

        The property is immutable and is only allowed to be set on a new volume creation. It is mandatory to provide either 'public image' or 'imageAlias' that has cloud-init compatibility in conjunction with this property.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/server#user_data Server#user_data}
        '''
        result = self._values.get("user_data")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServerVolume(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServerVolumeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-ionoscloud.server.ServerVolumeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b7f07f93caf6a7b411895443ae8bc2da9a7e743793a8928f8c9830c7d492ae78)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAvailabilityZone")
    def reset_availability_zone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAvailabilityZone", []))

    @jsii.member(jsii_name="resetBackupUnitId")
    def reset_backup_unit_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackupUnitId", []))

    @jsii.member(jsii_name="resetBus")
    def reset_bus(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBus", []))

    @jsii.member(jsii_name="resetImagePassword")
    def reset_image_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImagePassword", []))

    @jsii.member(jsii_name="resetLicenceType")
    def reset_licence_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLicenceType", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetSize")
    def reset_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSize", []))

    @jsii.member(jsii_name="resetSshKeyPath")
    def reset_ssh_key_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSshKeyPath", []))

    @jsii.member(jsii_name="resetUserData")
    def reset_user_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserData", []))

    @builtins.property
    @jsii.member(jsii_name="bootServer")
    def boot_server(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bootServer"))

    @builtins.property
    @jsii.member(jsii_name="cpuHotPlug")
    def cpu_hot_plug(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "cpuHotPlug"))

    @builtins.property
    @jsii.member(jsii_name="deviceNumber")
    def device_number(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "deviceNumber"))

    @builtins.property
    @jsii.member(jsii_name="discVirtioHotPlug")
    def disc_virtio_hot_plug(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "discVirtioHotPlug"))

    @builtins.property
    @jsii.member(jsii_name="discVirtioHotUnplug")
    def disc_virtio_hot_unplug(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "discVirtioHotUnplug"))

    @builtins.property
    @jsii.member(jsii_name="nicHotPlug")
    def nic_hot_plug(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "nicHotPlug"))

    @builtins.property
    @jsii.member(jsii_name="nicHotUnplug")
    def nic_hot_unplug(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "nicHotUnplug"))

    @builtins.property
    @jsii.member(jsii_name="pciSlot")
    def pci_slot(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "pciSlot"))

    @builtins.property
    @jsii.member(jsii_name="ramHotPlug")
    def ram_hot_plug(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "ramHotPlug"))

    @builtins.property
    @jsii.member(jsii_name="availabilityZoneInput")
    def availability_zone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilityZoneInput"))

    @builtins.property
    @jsii.member(jsii_name="backupUnitIdInput")
    def backup_unit_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backupUnitIdInput"))

    @builtins.property
    @jsii.member(jsii_name="busInput")
    def bus_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "busInput"))

    @builtins.property
    @jsii.member(jsii_name="diskTypeInput")
    def disk_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "diskTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="imagePasswordInput")
    def image_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imagePasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="licenceTypeInput")
    def licence_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "licenceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="sizeInput")
    def size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sizeInput"))

    @builtins.property
    @jsii.member(jsii_name="sshKeyPathInput")
    def ssh_key_path_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sshKeyPathInput"))

    @builtins.property
    @jsii.member(jsii_name="userDataInput")
    def user_data_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userDataInput"))

    @builtins.property
    @jsii.member(jsii_name="availabilityZone")
    def availability_zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "availabilityZone"))

    @availability_zone.setter
    def availability_zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59a42d9b09384feb88af7f3812c63fd4c4845239c270c665e64f73b63d252ff1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilityZone", value)

    @builtins.property
    @jsii.member(jsii_name="backupUnitId")
    def backup_unit_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backupUnitId"))

    @backup_unit_id.setter
    def backup_unit_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b12bfc6cf21c610a77d1c79635a623c8cea68c9440ee923d98704f61c4ebc4d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupUnitId", value)

    @builtins.property
    @jsii.member(jsii_name="bus")
    def bus(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bus"))

    @bus.setter
    def bus(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d8055c02480fd7584d5804fe680187eeee1e1d8a0bf2ff71480a25c7bbafec0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bus", value)

    @builtins.property
    @jsii.member(jsii_name="diskType")
    def disk_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "diskType"))

    @disk_type.setter
    def disk_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5b5213f4029962277510c5950173b6588acde92efcf73cac87e7121a0ba744f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskType", value)

    @builtins.property
    @jsii.member(jsii_name="imagePassword")
    def image_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "imagePassword"))

    @image_password.setter
    def image_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d79dcbf7b02bd2a75cea95d59f99b7c6eca73b7cd4c4b13a0a769a3f7f8268a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imagePassword", value)

    @builtins.property
    @jsii.member(jsii_name="licenceType")
    def licence_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "licenceType"))

    @licence_type.setter
    def licence_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e47a8a256e0c71a0b720c34fffcd2d1f1f7e611d828a79129535945f8bd6d5b0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "licenceType", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3be5b880a0dad453ec2f131925971550344c8bc56e794ee1ea10501a5eac8ff0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="size")
    def size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "size"))

    @size.setter
    def size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__496c2cc3407f4408c1be3a6474dcae963c14ea77bc9e76ba0339541735431f55)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "size", value)

    @builtins.property
    @jsii.member(jsii_name="sshKeyPath")
    def ssh_key_path(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sshKeyPath"))

    @ssh_key_path.setter
    def ssh_key_path(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06770a984ce1a511a00ffb89deb2a0993e99007e9f62c282256f773d3e3c59ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sshKeyPath", value)

    @builtins.property
    @jsii.member(jsii_name="userData")
    def user_data(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userData"))

    @user_data.setter
    def user_data(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f92910d15b88fc2b9368967abcf0669e2e1f4fbbf1201411498e9ce6873c92c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userData", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ServerVolume]:
        return typing.cast(typing.Optional[ServerVolume], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ServerVolume]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ea2ec2f8aef6687c72bfad46410fe80e7b80926c4e42dabb8bafd6ec138e2e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Server",
    "ServerConfig",
    "ServerNic",
    "ServerNicFirewall",
    "ServerNicFirewallOutputReference",
    "ServerNicOutputReference",
    "ServerTimeouts",
    "ServerTimeoutsOutputReference",
    "ServerVolume",
    "ServerVolumeOutputReference",
]

publication.publish()

def _typecheckingstub__a2a0c6ec6dcb3a1e07a0f940d7d1481dc2a214ea66934d51fe05a0166a1aa493(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    datacenter_id: builtins.str,
    name: builtins.str,
    nic: typing.Union[ServerNic, typing.Dict[builtins.str, typing.Any]],
    volume: typing.Union[ServerVolume, typing.Dict[builtins.str, typing.Any]],
    availability_zone: typing.Optional[builtins.str] = None,
    boot_cdrom: typing.Optional[builtins.str] = None,
    boot_image: typing.Optional[builtins.str] = None,
    cores: typing.Optional[jsii.Number] = None,
    cpu_family: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    image_name: typing.Optional[builtins.str] = None,
    image_password: typing.Optional[builtins.str] = None,
    ram: typing.Optional[jsii.Number] = None,
    ssh_key_path: typing.Optional[typing.Sequence[builtins.str]] = None,
    template_uuid: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[ServerTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    type: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__c40e8bf10013b101c5c122436bd17ec845753ece42395e8973b27a2fab69f4f0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3fd3c9596f20e7ffa3aa73c0b22e498e172a37364fcd7bd3857e4afc03da5a5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f930c79c58e86c71938382e75b68e46615646afc18cd80585f183487a769edea(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b40226fb89e488105e341bad05b1157bd2217a6719bb0e523a0e9ddba792dabf(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__731155d18763f0282f662298ac88dddb34ced7fb542a1e698e2886cb8b87a163(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77b17aa73ca68cebab214ab381c4af5668edc0f6db5a815468b06797045c063d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__330462605e3e6d1d020e339d2a99eedd88c7daf23b3d730d4c8165692f7d9bf6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4658431f765ad191ab9a055be7492327a68a2d940ae81b80b7cf0517a7b8bd5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53ef6bbf20814c35bd53fbbf8db1aaccd070634f02860689aa2c2aaa5b56a387(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbff757f49b27e1ccd6e20ae6e826ba42c07006ad5f197bc49cc067b4584558c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd8b82d0664ddc62aac16874051ea124bcea5619aacdbd5504f38489edbc3192(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b8b5c2b21c12f9ccd9b8fe055a31a5bb04c06b8fb46b7b6fbd65edc757f9f97(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9483f26fb4dc1d9c1f90bcced0a85d5cd7fd5f2883d0bda390c8cf4340203d5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e314d6600c97c9a4ba14a77d1f8be8e5cde26c791d796aebdee514ccb1d137a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2400b7d4c9d1d0d94d05866887b5445902c000ecaccf00650d0380ea4e52e4ee(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    datacenter_id: builtins.str,
    name: builtins.str,
    nic: typing.Union[ServerNic, typing.Dict[builtins.str, typing.Any]],
    volume: typing.Union[ServerVolume, typing.Dict[builtins.str, typing.Any]],
    availability_zone: typing.Optional[builtins.str] = None,
    boot_cdrom: typing.Optional[builtins.str] = None,
    boot_image: typing.Optional[builtins.str] = None,
    cores: typing.Optional[jsii.Number] = None,
    cpu_family: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    image_name: typing.Optional[builtins.str] = None,
    image_password: typing.Optional[builtins.str] = None,
    ram: typing.Optional[jsii.Number] = None,
    ssh_key_path: typing.Optional[typing.Sequence[builtins.str]] = None,
    template_uuid: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[ServerTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2d8426508d3f02c55a616c8e4d652773e3efed9b07cf7c155f21d788d1f78ae(
    *,
    lan: jsii.Number,
    dhcp: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    firewall: typing.Optional[typing.Union[ServerNicFirewall, typing.Dict[builtins.str, typing.Any]]] = None,
    firewall_active: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    firewall_type: typing.Optional[builtins.str] = None,
    ips: typing.Optional[typing.Sequence[builtins.str]] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14250c4e60ed029940154d0f58fa445c8a6baf10d212f9c9c37dc04848e35e48(
    *,
    protocol: builtins.str,
    icmp_code: typing.Optional[builtins.str] = None,
    icmp_type: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    port_range_end: typing.Optional[jsii.Number] = None,
    port_range_start: typing.Optional[jsii.Number] = None,
    source_ip: typing.Optional[builtins.str] = None,
    source_mac: typing.Optional[builtins.str] = None,
    target_ip: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d297e7258a8cc85fa8a839950b10cc07c86614cdeab35d5eb10462ba914d934(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2aa5830b3483ebe46a70f3affa39df77c0bcbed351a5681ed67966aec28bc57(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cba88b1a7205304a78b352e54433dd2ee69966bb655125d43f61ff95e3a8871(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a47f58a908e0d9ced08f6f7d2b4d64e4afb926356509ebb411cf6f1d998e7db7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bafa074f49a8e309695cde57921a187a6caf09abd6f8045443ef36a82964a04e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__455296888f78db790aab26fbc54a165a45801f570a767b4fef7172b241e1d752(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c3bf76fb7027c206935b8f1ded59912bdb99431526744b2db72bd7ff7e76c21(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da23071b46e3d8504625af34c54b9eda803d3581732ca2f415984054314d8261(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc84fcf6bfe187cdfdfdbd659d26c0c51b6aff446f11eabdee25817e7f81ce11(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19d3fbe12c30a2a5e03dd882e16561baa4b6faccb77bcead47eb98db342587f5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5693126bc17a77034013ca1917fd396c0410c7fc34abfe3b24286f4e6859f61e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__395ed72147c19bce1f68db1bc549693523cc4a12b205d93df788fa8e5d1d886f(
    value: typing.Optional[ServerNicFirewall],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f41472e5a11b6b0e11dce08d677ae47611daf07ec43aa28b524b8036b4cb6dc1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca593f83be0f20cdda731839123992c98b22aceaaf85a7ce7f486df3de005afa(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__374a3efef93f7d8f4333da4bfb5762670f621059254b704475dca63364ddcf03(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce3adffeb68a647eaa966f0380939ea8fe9b1ab159f01e409613ec99279ea9bb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70f4929730f5a009d652b4fd1e42890a58131dc1d4f99751759d61c3cd766f5a(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecdcf439efae018b1f118d31d43fada644a5e7c428e1d5ebf4d6de1e14dbac0b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99bcb671e3548aed5be8ccadb3dacdb63ac958bd45f46d516c4e3d7a8c12cac4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3af5d9673a8183dc13e3a32fcefebba43cc290ab1550d07f59d5ba7f8ca981a(
    value: typing.Optional[ServerNic],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9715f9f91828a802039eac63a25c973bd56edc373942d1afd41dfeaa583e3e0(
    *,
    create: typing.Optional[builtins.str] = None,
    default: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f84e5e2010b08f12a68eb28cd123b7557114c594b502bdbfa23a22cd377f8f9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9dd96344b5d7c98d17227e504754fe11c27f4d9476b4ca57b21aceaaf67d0a4d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ce22705a93219ce9a3c7509167b42f0311dc36647ed2ec653788b06203081a7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c19dacf8b47bf889af69c7a1fecbecf2664877fda80e206c25c7e8bc7f83eda5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bff7f587911914dd2fb6b3e8537129e1274e3b12d6692e1fda996bd40b19fc72(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40500c3dd1b0237c1997c51c78f087e0973414bb3caef29abeeb1c42cee53c53(
    value: typing.Optional[typing.Union[ServerTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5da2e0361c7606090c866f3b9012311f26869d5b07a34d9a001a3905f8968ce(
    *,
    disk_type: builtins.str,
    availability_zone: typing.Optional[builtins.str] = None,
    backup_unit_id: typing.Optional[builtins.str] = None,
    bus: typing.Optional[builtins.str] = None,
    image_password: typing.Optional[builtins.str] = None,
    licence_type: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    size: typing.Optional[jsii.Number] = None,
    ssh_key_path: typing.Optional[typing.Sequence[builtins.str]] = None,
    user_data: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7f07f93caf6a7b411895443ae8bc2da9a7e743793a8928f8c9830c7d492ae78(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59a42d9b09384feb88af7f3812c63fd4c4845239c270c665e64f73b63d252ff1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b12bfc6cf21c610a77d1c79635a623c8cea68c9440ee923d98704f61c4ebc4d8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d8055c02480fd7584d5804fe680187eeee1e1d8a0bf2ff71480a25c7bbafec0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5b5213f4029962277510c5950173b6588acde92efcf73cac87e7121a0ba744f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d79dcbf7b02bd2a75cea95d59f99b7c6eca73b7cd4c4b13a0a769a3f7f8268a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e47a8a256e0c71a0b720c34fffcd2d1f1f7e611d828a79129535945f8bd6d5b0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3be5b880a0dad453ec2f131925971550344c8bc56e794ee1ea10501a5eac8ff0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__496c2cc3407f4408c1be3a6474dcae963c14ea77bc9e76ba0339541735431f55(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06770a984ce1a511a00ffb89deb2a0993e99007e9f62c282256f773d3e3c59ea(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f92910d15b88fc2b9368967abcf0669e2e1f4fbbf1201411498e9ce6873c92c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ea2ec2f8aef6687c72bfad46410fe80e7b80926c4e42dabb8bafd6ec138e2e3(
    value: typing.Optional[ServerVolume],
) -> None:
    """Type checking stubs"""
    pass
