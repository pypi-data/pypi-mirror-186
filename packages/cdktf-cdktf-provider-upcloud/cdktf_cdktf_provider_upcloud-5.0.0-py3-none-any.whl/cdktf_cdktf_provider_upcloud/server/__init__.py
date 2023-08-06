'''
# `upcloud_server`

Refer to the Terraform Registory for docs: [`upcloud_server`](https://www.terraform.io/docs/providers/upcloud/r/server).
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
    jsii_type="@cdktf/provider-upcloud.server.Server",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/upcloud/r/server upcloud_server}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        hostname: builtins.str,
        network_interface: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ServerNetworkInterface", typing.Dict[builtins.str, typing.Any]]]],
        zone: builtins.str,
        cpu: typing.Optional[jsii.Number] = None,
        firewall: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        host: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        login: typing.Optional[typing.Union["ServerLogin", typing.Dict[builtins.str, typing.Any]]] = None,
        mem: typing.Optional[jsii.Number] = None,
        metadata: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        plan: typing.Optional[builtins.str] = None,
        simple_backup: typing.Optional[typing.Union["ServerSimpleBackup", typing.Dict[builtins.str, typing.Any]]] = None,
        storage_devices: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ServerStorageDevices", typing.Dict[builtins.str, typing.Any]]]]] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        template: typing.Optional[typing.Union["ServerTemplate", typing.Dict[builtins.str, typing.Any]]] = None,
        title: typing.Optional[builtins.str] = None,
        user_data: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/upcloud/r/server upcloud_server} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param hostname: A valid domain name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#hostname Server#hostname}
        :param network_interface: network_interface block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#network_interface Server#network_interface}
        :param zone: The zone in which the server will be hosted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#zone Server#zone}
        :param cpu: The number of CPU for the server. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#cpu Server#cpu}
        :param firewall: Are firewall rules active for the server. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#firewall Server#firewall}
        :param host: Use this to start the VM on a specific host. Refers to value from host -attribute. Only available for private cloud hosts Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#host Server#host}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#id Server#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: Labels contain key-value pairs to classify the server. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#labels Server#labels}
        :param login: login block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#login Server#login}
        :param mem: The size of memory for the server (in megabytes). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#mem Server#mem}
        :param metadata: Is the metadata service active for the server. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#metadata Server#metadata}
        :param plan: The pricing plan used for the server. You can list available server plans with ``upctl server plans``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#plan Server#plan}
        :param simple_backup: simple_backup block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#simple_backup Server#simple_backup}
        :param storage_devices: storage_devices block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#storage_devices Server#storage_devices}
        :param tags: The server related tags. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#tags Server#tags}
        :param template: template block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#template Server#template}
        :param title: A short, informational description. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#title Server#title}
        :param user_data: Defines URL for a server setup script, or the script body itself. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#user_data Server#user_data}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b83690e478f8730a1b183dfb2bf71b179dc55ba8028fd8cc73841eff54172a9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ServerConfig(
            hostname=hostname,
            network_interface=network_interface,
            zone=zone,
            cpu=cpu,
            firewall=firewall,
            host=host,
            id=id,
            labels=labels,
            login=login,
            mem=mem,
            metadata=metadata,
            plan=plan,
            simple_backup=simple_backup,
            storage_devices=storage_devices,
            tags=tags,
            template=template,
            title=title,
            user_data=user_data,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putLogin")
    def put_login(
        self,
        *,
        create_password: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        password_delivery: typing.Optional[builtins.str] = None,
        user: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create_password: Indicates a password should be create to allow access. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#create_password Server#create_password}
        :param keys: A list of ssh keys to access the server. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#keys Server#keys}
        :param password_delivery: The delivery method for the server's root password (one of ``none``, ``email`` or ``sms``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#password_delivery Server#password_delivery}
        :param user: Username to be create to access the server. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#user Server#user}
        '''
        value = ServerLogin(
            create_password=create_password,
            keys=keys,
            password_delivery=password_delivery,
            user=user,
        )

        return typing.cast(None, jsii.invoke(self, "putLogin", [value]))

    @jsii.member(jsii_name="putNetworkInterface")
    def put_network_interface(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ServerNetworkInterface", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2784a2f8e61298bcd760c00280858e93027365e3107df743c65e925390d065ff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNetworkInterface", [value]))

    @jsii.member(jsii_name="putSimpleBackup")
    def put_simple_backup(self, *, plan: builtins.str, time: builtins.str) -> None:
        '''
        :param plan: Simple backup plan. Accepted values: dailies, weeklies, monthlies. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#plan Server#plan}
        :param time: Time of the day at which backup will be taken. Should be provided in a hhmm format (e.g. 2230). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#time Server#time}
        '''
        value = ServerSimpleBackup(plan=plan, time=time)

        return typing.cast(None, jsii.invoke(self, "putSimpleBackup", [value]))

    @jsii.member(jsii_name="putStorageDevices")
    def put_storage_devices(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ServerStorageDevices", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2c4cd707e662e8744252abfd6f62940a96bcdfc90c7389a218eb5a2acab2006)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putStorageDevices", [value]))

    @jsii.member(jsii_name="putTemplate")
    def put_template(
        self,
        *,
        storage: builtins.str,
        address: typing.Optional[builtins.str] = None,
        backup_rule: typing.Optional[typing.Union["ServerTemplateBackupRule", typing.Dict[builtins.str, typing.Any]]] = None,
        delete_autoresize_backup: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        filesystem_autoresize: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        size: typing.Optional[jsii.Number] = None,
        title: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param storage: A valid storage UUID or template name. You can list available public templates with ``upctl storage list --public --template`` and available private templates with ``upctl storage list --template``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#storage Server#storage}
        :param address: The device address the storage will be attached to. Specify only the bus name (ide/scsi/virtio) to auto-select next available address from that bus. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#address Server#address}
        :param backup_rule: backup_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#backup_rule Server#backup_rule}
        :param delete_autoresize_backup: If set to true, the backup taken before the partition and filesystem resize attempt will be deleted immediately after success. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#delete_autoresize_backup Server#delete_autoresize_backup}
        :param filesystem_autoresize: If set to true, provider will attempt to resize partition and filesystem when the size of template storage changes. Please note that before the resize attempt is made, backup of the storage will be taken. If the resize attempt fails, the backup will be used to restore the storage and then deleted. If the resize attempt succeeds, backup will be kept (unless delete_autoresize_backup option is set to true). Taking and keeping backups incure costs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#filesystem_autoresize Server#filesystem_autoresize}
        :param size: The size of the storage in gigabytes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#size Server#size}
        :param title: A short, informative description. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#title Server#title}
        '''
        value = ServerTemplate(
            storage=storage,
            address=address,
            backup_rule=backup_rule,
            delete_autoresize_backup=delete_autoresize_backup,
            filesystem_autoresize=filesystem_autoresize,
            size=size,
            title=title,
        )

        return typing.cast(None, jsii.invoke(self, "putTemplate", [value]))

    @jsii.member(jsii_name="resetCpu")
    def reset_cpu(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCpu", []))

    @jsii.member(jsii_name="resetFirewall")
    def reset_firewall(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFirewall", []))

    @jsii.member(jsii_name="resetHost")
    def reset_host(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHost", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetLogin")
    def reset_login(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogin", []))

    @jsii.member(jsii_name="resetMem")
    def reset_mem(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMem", []))

    @jsii.member(jsii_name="resetMetadata")
    def reset_metadata(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetadata", []))

    @jsii.member(jsii_name="resetPlan")
    def reset_plan(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlan", []))

    @jsii.member(jsii_name="resetSimpleBackup")
    def reset_simple_backup(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSimpleBackup", []))

    @jsii.member(jsii_name="resetStorageDevices")
    def reset_storage_devices(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageDevices", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTemplate")
    def reset_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTemplate", []))

    @jsii.member(jsii_name="resetTitle")
    def reset_title(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTitle", []))

    @jsii.member(jsii_name="resetUserData")
    def reset_user_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserData", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="login")
    def login(self) -> "ServerLoginOutputReference":
        return typing.cast("ServerLoginOutputReference", jsii.get(self, "login"))

    @builtins.property
    @jsii.member(jsii_name="networkInterface")
    def network_interface(self) -> "ServerNetworkInterfaceList":
        return typing.cast("ServerNetworkInterfaceList", jsii.get(self, "networkInterface"))

    @builtins.property
    @jsii.member(jsii_name="simpleBackup")
    def simple_backup(self) -> "ServerSimpleBackupOutputReference":
        return typing.cast("ServerSimpleBackupOutputReference", jsii.get(self, "simpleBackup"))

    @builtins.property
    @jsii.member(jsii_name="storageDevices")
    def storage_devices(self) -> "ServerStorageDevicesList":
        return typing.cast("ServerStorageDevicesList", jsii.get(self, "storageDevices"))

    @builtins.property
    @jsii.member(jsii_name="template")
    def template(self) -> "ServerTemplateOutputReference":
        return typing.cast("ServerTemplateOutputReference", jsii.get(self, "template"))

    @builtins.property
    @jsii.member(jsii_name="cpuInput")
    def cpu_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "cpuInput"))

    @builtins.property
    @jsii.member(jsii_name="firewallInput")
    def firewall_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "firewallInput"))

    @builtins.property
    @jsii.member(jsii_name="hostInput")
    def host_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "hostInput"))

    @builtins.property
    @jsii.member(jsii_name="hostnameInput")
    def hostname_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostnameInput"))

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
    @jsii.member(jsii_name="loginInput")
    def login_input(self) -> typing.Optional["ServerLogin"]:
        return typing.cast(typing.Optional["ServerLogin"], jsii.get(self, "loginInput"))

    @builtins.property
    @jsii.member(jsii_name="memInput")
    def mem_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "memInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataInput")
    def metadata_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "metadataInput"))

    @builtins.property
    @jsii.member(jsii_name="networkInterfaceInput")
    def network_interface_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ServerNetworkInterface"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ServerNetworkInterface"]]], jsii.get(self, "networkInterfaceInput"))

    @builtins.property
    @jsii.member(jsii_name="planInput")
    def plan_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "planInput"))

    @builtins.property
    @jsii.member(jsii_name="simpleBackupInput")
    def simple_backup_input(self) -> typing.Optional["ServerSimpleBackup"]:
        return typing.cast(typing.Optional["ServerSimpleBackup"], jsii.get(self, "simpleBackupInput"))

    @builtins.property
    @jsii.member(jsii_name="storageDevicesInput")
    def storage_devices_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ServerStorageDevices"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ServerStorageDevices"]]], jsii.get(self, "storageDevicesInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="templateInput")
    def template_input(self) -> typing.Optional["ServerTemplate"]:
        return typing.cast(typing.Optional["ServerTemplate"], jsii.get(self, "templateInput"))

    @builtins.property
    @jsii.member(jsii_name="titleInput")
    def title_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "titleInput"))

    @builtins.property
    @jsii.member(jsii_name="userDataInput")
    def user_data_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userDataInput"))

    @builtins.property
    @jsii.member(jsii_name="zoneInput")
    def zone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "zoneInput"))

    @builtins.property
    @jsii.member(jsii_name="cpu")
    def cpu(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cpu"))

    @cpu.setter
    def cpu(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0bf29acd3dd45353eecfc5a63f6040bd66f55ef883a41491d92f1bdbe810a40)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpu", value)

    @builtins.property
    @jsii.member(jsii_name="firewall")
    def firewall(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "firewall"))

    @firewall.setter
    def firewall(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__faf5fe2f1617d856951894b09503ce986b9b9e75f119670e34925d2d45d2e9ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firewall", value)

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "host"))

    @host.setter
    def host(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb33c3002695f65e8de16860ddf00ce31ac89ba44e937051e0add8e77bb120c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "host", value)

    @builtins.property
    @jsii.member(jsii_name="hostname")
    def hostname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostname"))

    @hostname.setter
    def hostname(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4bd72ca4af6dd9b479c0262e490984bdbd3191d9b6e06c6924b98a95b88a2ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostname", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a84cfa579ab88830b19af88519f30728d1a5668fda89bc3e98d7b7cb076e00cc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a7892fe5de8b838249765679a48d6de643cd5ca2b10527938954d152ae696ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="mem")
    def mem(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "mem"))

    @mem.setter
    def mem(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__124e11a99805e080ae09bb64a779c4f3bf94f05876de9f8f9b682c9fe74e79e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mem", value)

    @builtins.property
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "metadata"))

    @metadata.setter
    def metadata(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64fa85207ab264b6f079b98afe3eef4ec2bf20d249f7caa10f6ab31566841844)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metadata", value)

    @builtins.property
    @jsii.member(jsii_name="plan")
    def plan(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "plan"))

    @plan.setter
    def plan(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2da76f679e87688e11b6f83fb15ba717554341797b152012a0fb49e67140b935)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "plan", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e7175151be1c034f617e5043b4a582fa7a23b63257729e9f6b6957e2b922bfb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @title.setter
    def title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae9bce333377a9eba2c28adc33c40c562a185ced6585b2a01045577d13004430)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value)

    @builtins.property
    @jsii.member(jsii_name="userData")
    def user_data(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userData"))

    @user_data.setter
    def user_data(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64b2aea0b37c12d0056c07c0c4281a978b335a3259b4e52cc2e9287e80bfa864)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userData", value)

    @builtins.property
    @jsii.member(jsii_name="zone")
    def zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zone"))

    @zone.setter
    def zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__189f51a8a94e7de544c3857c63fb20bd2ee94539e95189dafb4bab5cb85e9236)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zone", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-upcloud.server.ServerConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "hostname": "hostname",
        "network_interface": "networkInterface",
        "zone": "zone",
        "cpu": "cpu",
        "firewall": "firewall",
        "host": "host",
        "id": "id",
        "labels": "labels",
        "login": "login",
        "mem": "mem",
        "metadata": "metadata",
        "plan": "plan",
        "simple_backup": "simpleBackup",
        "storage_devices": "storageDevices",
        "tags": "tags",
        "template": "template",
        "title": "title",
        "user_data": "userData",
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
        hostname: builtins.str,
        network_interface: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ServerNetworkInterface", typing.Dict[builtins.str, typing.Any]]]],
        zone: builtins.str,
        cpu: typing.Optional[jsii.Number] = None,
        firewall: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        host: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        login: typing.Optional[typing.Union["ServerLogin", typing.Dict[builtins.str, typing.Any]]] = None,
        mem: typing.Optional[jsii.Number] = None,
        metadata: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        plan: typing.Optional[builtins.str] = None,
        simple_backup: typing.Optional[typing.Union["ServerSimpleBackup", typing.Dict[builtins.str, typing.Any]]] = None,
        storage_devices: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ServerStorageDevices", typing.Dict[builtins.str, typing.Any]]]]] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        template: typing.Optional[typing.Union["ServerTemplate", typing.Dict[builtins.str, typing.Any]]] = None,
        title: typing.Optional[builtins.str] = None,
        user_data: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param hostname: A valid domain name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#hostname Server#hostname}
        :param network_interface: network_interface block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#network_interface Server#network_interface}
        :param zone: The zone in which the server will be hosted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#zone Server#zone}
        :param cpu: The number of CPU for the server. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#cpu Server#cpu}
        :param firewall: Are firewall rules active for the server. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#firewall Server#firewall}
        :param host: Use this to start the VM on a specific host. Refers to value from host -attribute. Only available for private cloud hosts Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#host Server#host}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#id Server#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: Labels contain key-value pairs to classify the server. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#labels Server#labels}
        :param login: login block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#login Server#login}
        :param mem: The size of memory for the server (in megabytes). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#mem Server#mem}
        :param metadata: Is the metadata service active for the server. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#metadata Server#metadata}
        :param plan: The pricing plan used for the server. You can list available server plans with ``upctl server plans``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#plan Server#plan}
        :param simple_backup: simple_backup block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#simple_backup Server#simple_backup}
        :param storage_devices: storage_devices block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#storage_devices Server#storage_devices}
        :param tags: The server related tags. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#tags Server#tags}
        :param template: template block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#template Server#template}
        :param title: A short, informational description. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#title Server#title}
        :param user_data: Defines URL for a server setup script, or the script body itself. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#user_data Server#user_data}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(login, dict):
            login = ServerLogin(**login)
        if isinstance(simple_backup, dict):
            simple_backup = ServerSimpleBackup(**simple_backup)
        if isinstance(template, dict):
            template = ServerTemplate(**template)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea0c30195fdb4e86d473d86dcc3b49fe1de4f105b946dcc2035464e29e243e2a)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument hostname", value=hostname, expected_type=type_hints["hostname"])
            check_type(argname="argument network_interface", value=network_interface, expected_type=type_hints["network_interface"])
            check_type(argname="argument zone", value=zone, expected_type=type_hints["zone"])
            check_type(argname="argument cpu", value=cpu, expected_type=type_hints["cpu"])
            check_type(argname="argument firewall", value=firewall, expected_type=type_hints["firewall"])
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument login", value=login, expected_type=type_hints["login"])
            check_type(argname="argument mem", value=mem, expected_type=type_hints["mem"])
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument plan", value=plan, expected_type=type_hints["plan"])
            check_type(argname="argument simple_backup", value=simple_backup, expected_type=type_hints["simple_backup"])
            check_type(argname="argument storage_devices", value=storage_devices, expected_type=type_hints["storage_devices"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument template", value=template, expected_type=type_hints["template"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
            check_type(argname="argument user_data", value=user_data, expected_type=type_hints["user_data"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "hostname": hostname,
            "network_interface": network_interface,
            "zone": zone,
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
        if cpu is not None:
            self._values["cpu"] = cpu
        if firewall is not None:
            self._values["firewall"] = firewall
        if host is not None:
            self._values["host"] = host
        if id is not None:
            self._values["id"] = id
        if labels is not None:
            self._values["labels"] = labels
        if login is not None:
            self._values["login"] = login
        if mem is not None:
            self._values["mem"] = mem
        if metadata is not None:
            self._values["metadata"] = metadata
        if plan is not None:
            self._values["plan"] = plan
        if simple_backup is not None:
            self._values["simple_backup"] = simple_backup
        if storage_devices is not None:
            self._values["storage_devices"] = storage_devices
        if tags is not None:
            self._values["tags"] = tags
        if template is not None:
            self._values["template"] = template
        if title is not None:
            self._values["title"] = title
        if user_data is not None:
            self._values["user_data"] = user_data

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
    def hostname(self) -> builtins.str:
        '''A valid domain name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#hostname Server#hostname}
        '''
        result = self._values.get("hostname")
        assert result is not None, "Required property 'hostname' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def network_interface(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ServerNetworkInterface"]]:
        '''network_interface block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#network_interface Server#network_interface}
        '''
        result = self._values.get("network_interface")
        assert result is not None, "Required property 'network_interface' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ServerNetworkInterface"]], result)

    @builtins.property
    def zone(self) -> builtins.str:
        '''The zone in which the server will be hosted.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#zone Server#zone}
        '''
        result = self._values.get("zone")
        assert result is not None, "Required property 'zone' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cpu(self) -> typing.Optional[jsii.Number]:
        '''The number of CPU for the server.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#cpu Server#cpu}
        '''
        result = self._values.get("cpu")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def firewall(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Are firewall rules active for the server.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#firewall Server#firewall}
        '''
        result = self._values.get("firewall")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def host(self) -> typing.Optional[jsii.Number]:
        '''Use this to start the VM on a specific host.

        Refers to value from host -attribute. Only available for private cloud hosts

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#host Server#host}
        '''
        result = self._values.get("host")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#id Server#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Labels contain key-value pairs to classify the server.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#labels Server#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def login(self) -> typing.Optional["ServerLogin"]:
        '''login block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#login Server#login}
        '''
        result = self._values.get("login")
        return typing.cast(typing.Optional["ServerLogin"], result)

    @builtins.property
    def mem(self) -> typing.Optional[jsii.Number]:
        '''The size of memory for the server (in megabytes).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#mem Server#mem}
        '''
        result = self._values.get("mem")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def metadata(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Is the metadata service active for the server.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#metadata Server#metadata}
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def plan(self) -> typing.Optional[builtins.str]:
        '''The pricing plan used for the server. You can list available server plans with ``upctl server plans``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#plan Server#plan}
        '''
        result = self._values.get("plan")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def simple_backup(self) -> typing.Optional["ServerSimpleBackup"]:
        '''simple_backup block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#simple_backup Server#simple_backup}
        '''
        result = self._values.get("simple_backup")
        return typing.cast(typing.Optional["ServerSimpleBackup"], result)

    @builtins.property
    def storage_devices(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ServerStorageDevices"]]]:
        '''storage_devices block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#storage_devices Server#storage_devices}
        '''
        result = self._values.get("storage_devices")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ServerStorageDevices"]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The server related tags.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#tags Server#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def template(self) -> typing.Optional["ServerTemplate"]:
        '''template block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#template Server#template}
        '''
        result = self._values.get("template")
        return typing.cast(typing.Optional["ServerTemplate"], result)

    @builtins.property
    def title(self) -> typing.Optional[builtins.str]:
        '''A short, informational description.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#title Server#title}
        '''
        result = self._values.get("title")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_data(self) -> typing.Optional[builtins.str]:
        '''Defines URL for a server setup script, or the script body itself.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#user_data Server#user_data}
        '''
        result = self._values.get("user_data")
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
    jsii_type="@cdktf/provider-upcloud.server.ServerLogin",
    jsii_struct_bases=[],
    name_mapping={
        "create_password": "createPassword",
        "keys": "keys",
        "password_delivery": "passwordDelivery",
        "user": "user",
    },
)
class ServerLogin:
    def __init__(
        self,
        *,
        create_password: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        password_delivery: typing.Optional[builtins.str] = None,
        user: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create_password: Indicates a password should be create to allow access. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#create_password Server#create_password}
        :param keys: A list of ssh keys to access the server. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#keys Server#keys}
        :param password_delivery: The delivery method for the server's root password (one of ``none``, ``email`` or ``sms``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#password_delivery Server#password_delivery}
        :param user: Username to be create to access the server. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#user Server#user}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba39a2ee1d911b76fb74554613ea114a5a572a0bf44aae12941ef4644ef7377a)
            check_type(argname="argument create_password", value=create_password, expected_type=type_hints["create_password"])
            check_type(argname="argument keys", value=keys, expected_type=type_hints["keys"])
            check_type(argname="argument password_delivery", value=password_delivery, expected_type=type_hints["password_delivery"])
            check_type(argname="argument user", value=user, expected_type=type_hints["user"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create_password is not None:
            self._values["create_password"] = create_password
        if keys is not None:
            self._values["keys"] = keys
        if password_delivery is not None:
            self._values["password_delivery"] = password_delivery
        if user is not None:
            self._values["user"] = user

    @builtins.property
    def create_password(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Indicates a password should be create to allow access.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#create_password Server#create_password}
        '''
        result = self._values.get("create_password")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def keys(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of ssh keys to access the server.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#keys Server#keys}
        '''
        result = self._values.get("keys")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def password_delivery(self) -> typing.Optional[builtins.str]:
        '''The delivery method for the server's root password (one of ``none``, ``email`` or ``sms``).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#password_delivery Server#password_delivery}
        '''
        result = self._values.get("password_delivery")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user(self) -> typing.Optional[builtins.str]:
        '''Username to be create to access the server.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#user Server#user}
        '''
        result = self._values.get("user")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServerLogin(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServerLoginOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.server.ServerLoginOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cb37b4e00c78f37c38cbba42c725d341426cd4846a37328a858efbce8e63b347)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreatePassword")
    def reset_create_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreatePassword", []))

    @jsii.member(jsii_name="resetKeys")
    def reset_keys(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeys", []))

    @jsii.member(jsii_name="resetPasswordDelivery")
    def reset_password_delivery(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPasswordDelivery", []))

    @jsii.member(jsii_name="resetUser")
    def reset_user(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUser", []))

    @builtins.property
    @jsii.member(jsii_name="createPasswordInput")
    def create_password_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "createPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="keysInput")
    def keys_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "keysInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordDeliveryInput")
    def password_delivery_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordDeliveryInput"))

    @builtins.property
    @jsii.member(jsii_name="userInput")
    def user_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userInput"))

    @builtins.property
    @jsii.member(jsii_name="createPassword")
    def create_password(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "createPassword"))

    @create_password.setter
    def create_password(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52fef0f21493a08a9b1120b5e06665743a76af6b2c68ad33657352e375d30f83)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createPassword", value)

    @builtins.property
    @jsii.member(jsii_name="keys")
    def keys(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "keys"))

    @keys.setter
    def keys(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b692749540d070af5a9539957a6fb3b45c73bf325a279cde1ce841cb2b3a368)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keys", value)

    @builtins.property
    @jsii.member(jsii_name="passwordDelivery")
    def password_delivery(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "passwordDelivery"))

    @password_delivery.setter
    def password_delivery(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0cb6ee9476d3d13341856fea701d89ab77f7390a5c83899ab22e0865a2cfaf45)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "passwordDelivery", value)

    @builtins.property
    @jsii.member(jsii_name="user")
    def user(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "user"))

    @user.setter
    def user(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5428294ae30fe53a9c3e6f59c5d7345c00077d52ca2969ca46d13b15b72bcf2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "user", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ServerLogin]:
        return typing.cast(typing.Optional[ServerLogin], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ServerLogin]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5a2e407880016cbd5838a509393761434aa730eb60add2b4b29eadad0776d3b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-upcloud.server.ServerNetworkInterface",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "bootable": "bootable",
        "ip_address": "ipAddress",
        "ip_address_family": "ipAddressFamily",
        "network": "network",
        "source_ip_filtering": "sourceIpFiltering",
    },
)
class ServerNetworkInterface:
    def __init__(
        self,
        *,
        type: builtins.str,
        bootable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        ip_address: typing.Optional[builtins.str] = None,
        ip_address_family: typing.Optional[builtins.str] = None,
        network: typing.Optional[builtins.str] = None,
        source_ip_filtering: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param type: Network interface type. For private network interfaces, a network must be specified with an existing network id. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#type Server#type}
        :param bootable: ``true`` if this interface should be used for network booting. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#bootable Server#bootable}
        :param ip_address: The assigned IP address. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#ip_address Server#ip_address}
        :param ip_address_family: The IP address type of this interface (one of ``IPv4`` or ``IPv6``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#ip_address_family Server#ip_address_family}
        :param network: The unique ID of a network to attach this network to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#network Server#network}
        :param source_ip_filtering: ``true`` if source IP should be filtered. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#source_ip_filtering Server#source_ip_filtering}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd495e0f43b555636347e658837821c13810606782b5f840f155acbfbcf8b7ea)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument bootable", value=bootable, expected_type=type_hints["bootable"])
            check_type(argname="argument ip_address", value=ip_address, expected_type=type_hints["ip_address"])
            check_type(argname="argument ip_address_family", value=ip_address_family, expected_type=type_hints["ip_address_family"])
            check_type(argname="argument network", value=network, expected_type=type_hints["network"])
            check_type(argname="argument source_ip_filtering", value=source_ip_filtering, expected_type=type_hints["source_ip_filtering"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }
        if bootable is not None:
            self._values["bootable"] = bootable
        if ip_address is not None:
            self._values["ip_address"] = ip_address
        if ip_address_family is not None:
            self._values["ip_address_family"] = ip_address_family
        if network is not None:
            self._values["network"] = network
        if source_ip_filtering is not None:
            self._values["source_ip_filtering"] = source_ip_filtering

    @builtins.property
    def type(self) -> builtins.str:
        '''Network interface type. For private network interfaces, a network must be specified with an existing network id.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#type Server#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bootable(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''``true`` if this interface should be used for network booting.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#bootable Server#bootable}
        '''
        result = self._values.get("bootable")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def ip_address(self) -> typing.Optional[builtins.str]:
        '''The assigned IP address.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#ip_address Server#ip_address}
        '''
        result = self._values.get("ip_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ip_address_family(self) -> typing.Optional[builtins.str]:
        '''The IP address type of this interface (one of ``IPv4`` or ``IPv6``).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#ip_address_family Server#ip_address_family}
        '''
        result = self._values.get("ip_address_family")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def network(self) -> typing.Optional[builtins.str]:
        '''The unique ID of a network to attach this network to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#network Server#network}
        '''
        result = self._values.get("network")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_ip_filtering(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''``true`` if source IP should be filtered.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#source_ip_filtering Server#source_ip_filtering}
        '''
        result = self._values.get("source_ip_filtering")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServerNetworkInterface(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServerNetworkInterfaceList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.server.ServerNetworkInterfaceList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fc54b91b5d0d7c97de16d571e1bd39a117d649214c8689ebf9994e4e990fd340)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ServerNetworkInterfaceOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33afd8f34658cdde16c336c0c57cf4773e6fec818004f2ef62f5737777f120ea)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ServerNetworkInterfaceOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__964638e95b9eb64f9888fef8669fefd3199a22770bc88f1e9e55385ffcf19266)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4f425debfe0fca1e3b8c8cd983ff8f17a5cee4a67bedbf8b9045e682766c159c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ecc2284e90d7a1c3606d00ad08be4fb4481c645e68a00a279e10ebf0666a6875)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ServerNetworkInterface]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ServerNetworkInterface]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ServerNetworkInterface]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05c518a721134139fda2b2f95e72e1fc5c01453ef555dec5b958772b12cc8b9c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ServerNetworkInterfaceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.server.ServerNetworkInterfaceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f351e78b8ed148a38258a4e1044dee8183c1dc0faa0e2ff98d6538a768811b64)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetBootable")
    def reset_bootable(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBootable", []))

    @jsii.member(jsii_name="resetIpAddress")
    def reset_ip_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpAddress", []))

    @jsii.member(jsii_name="resetIpAddressFamily")
    def reset_ip_address_family(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpAddressFamily", []))

    @jsii.member(jsii_name="resetNetwork")
    def reset_network(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetwork", []))

    @jsii.member(jsii_name="resetSourceIpFiltering")
    def reset_source_ip_filtering(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceIpFiltering", []))

    @builtins.property
    @jsii.member(jsii_name="ipAddressFloating")
    def ip_address_floating(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "ipAddressFloating"))

    @builtins.property
    @jsii.member(jsii_name="macAddress")
    def mac_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "macAddress"))

    @builtins.property
    @jsii.member(jsii_name="bootableInput")
    def bootable_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "bootableInput"))

    @builtins.property
    @jsii.member(jsii_name="ipAddressFamilyInput")
    def ip_address_family_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipAddressFamilyInput"))

    @builtins.property
    @jsii.member(jsii_name="ipAddressInput")
    def ip_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="networkInput")
    def network_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceIpFilteringInput")
    def source_ip_filtering_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "sourceIpFilteringInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="bootable")
    def bootable(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "bootable"))

    @bootable.setter
    def bootable(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__47ed0e3d16bdd5428b4c7adf673350899ade00d8859059ed0f26439a53c0b519)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bootable", value)

    @builtins.property
    @jsii.member(jsii_name="ipAddress")
    def ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipAddress"))

    @ip_address.setter
    def ip_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97b4cbf583d41648739b128bd01df2684cfe29bc55efc08b02280697b7207be3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipAddress", value)

    @builtins.property
    @jsii.member(jsii_name="ipAddressFamily")
    def ip_address_family(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipAddressFamily"))

    @ip_address_family.setter
    def ip_address_family(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27ca96659b5cf24779fba934b13768313666a313e1ec402934147d93b04c671d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipAddressFamily", value)

    @builtins.property
    @jsii.member(jsii_name="network")
    def network(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "network"))

    @network.setter
    def network(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4455383f612dd1e5e7b829b5df56c87f6147838c2bd408299074c0fe1fcb3457)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "network", value)

    @builtins.property
    @jsii.member(jsii_name="sourceIpFiltering")
    def source_ip_filtering(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "sourceIpFiltering"))

    @source_ip_filtering.setter
    def source_ip_filtering(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67715c977e47025dc675151bb1733aeb13846dd9b753760e7f626bb21f196235)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceIpFiltering", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21f40dacaedad9009711ae5ffd3910b0ae85807a8cec83e69f5f166a7cf791ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ServerNetworkInterface, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ServerNetworkInterface, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ServerNetworkInterface, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8653f81da3a79a9a2fd0667eb122024a0e78b7183d06eaf233aa6b039ab88013)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-upcloud.server.ServerSimpleBackup",
    jsii_struct_bases=[],
    name_mapping={"plan": "plan", "time": "time"},
)
class ServerSimpleBackup:
    def __init__(self, *, plan: builtins.str, time: builtins.str) -> None:
        '''
        :param plan: Simple backup plan. Accepted values: dailies, weeklies, monthlies. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#plan Server#plan}
        :param time: Time of the day at which backup will be taken. Should be provided in a hhmm format (e.g. 2230). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#time Server#time}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0bd20cac4bdde3b91171ae0bf44e53e9583617261eaf0793a175a7d8da3cee3)
            check_type(argname="argument plan", value=plan, expected_type=type_hints["plan"])
            check_type(argname="argument time", value=time, expected_type=type_hints["time"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "plan": plan,
            "time": time,
        }

    @builtins.property
    def plan(self) -> builtins.str:
        '''Simple backup plan. Accepted values: dailies, weeklies, monthlies.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#plan Server#plan}
        '''
        result = self._values.get("plan")
        assert result is not None, "Required property 'plan' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def time(self) -> builtins.str:
        '''Time of the day at which backup will be taken. Should be provided in a hhmm format (e.g. 2230).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#time Server#time}
        '''
        result = self._values.get("time")
        assert result is not None, "Required property 'time' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServerSimpleBackup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServerSimpleBackupOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.server.ServerSimpleBackupOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__543283afc6e5dcbaed6d63b62679b76fe001c3a94535d560e5ee698bde877d12)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="planInput")
    def plan_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "planInput"))

    @builtins.property
    @jsii.member(jsii_name="timeInput")
    def time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeInput"))

    @builtins.property
    @jsii.member(jsii_name="plan")
    def plan(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "plan"))

    @plan.setter
    def plan(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3fcfd10d4cc42b7a124d6deb709aed8a84109c8a6ccf87e6ea1c1446e290e765)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "plan", value)

    @builtins.property
    @jsii.member(jsii_name="time")
    def time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "time"))

    @time.setter
    def time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2a12363cbec7f1b1136e6a05c23fd0826a6915ccf0b0b64f9f4fccc66a7b1da)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "time", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ServerSimpleBackup]:
        return typing.cast(typing.Optional[ServerSimpleBackup], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ServerSimpleBackup]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__047ada69f3d10e42273140f60146f8fdf26e9f7c5b02497edf7ff0b3533062bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-upcloud.server.ServerStorageDevices",
    jsii_struct_bases=[],
    name_mapping={"storage": "storage", "address": "address", "type": "type"},
)
class ServerStorageDevices:
    def __init__(
        self,
        *,
        storage: builtins.str,
        address: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param storage: A valid storage UUID. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#storage Server#storage}
        :param address: The device address the storage will be attached to. Specify only the bus name (ide/scsi/virtio) to auto-select next available address from that bus. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#address Server#address}
        :param type: The device type the storage will be attached as. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#type Server#type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__deefc3ca26ddd4529dd49d665d0a7e4d178ed9e318d7a6ed318fe000f57713ea)
            check_type(argname="argument storage", value=storage, expected_type=type_hints["storage"])
            check_type(argname="argument address", value=address, expected_type=type_hints["address"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "storage": storage,
        }
        if address is not None:
            self._values["address"] = address
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def storage(self) -> builtins.str:
        '''A valid storage UUID.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#storage Server#storage}
        '''
        result = self._values.get("storage")
        assert result is not None, "Required property 'storage' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def address(self) -> typing.Optional[builtins.str]:
        '''The device address the storage will be attached to.

        Specify only the bus name (ide/scsi/virtio) to auto-select next available address from that bus.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#address Server#address}
        '''
        result = self._values.get("address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''The device type the storage will be attached as.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#type Server#type}
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServerStorageDevices(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServerStorageDevicesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.server.ServerStorageDevicesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1b1a8309ae0e42008d4d9a04fa384232a242ebf581bdfe667b3d4d9318c423e1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ServerStorageDevicesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0cd494dc7b3e8661672bce1c045c252c6330d80b0f7be6bfd03cb3eab0419cfc)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ServerStorageDevicesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c36a029bc93903864475ea526a1d5d88d1c38739833442c25954cc78734d073)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c6106531b80754e3450342cca25dccc97ecca94111c0beac393fdf0cc5992ba2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__404155dd5b9ae6ef51ecbd295a6258fba082b02c4edde041ed4e3fdd0e39479f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ServerStorageDevices]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ServerStorageDevices]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ServerStorageDevices]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d8da2a7cdb20f04a3d3e26873cb26f1bad3c31fb192cec0590a5630aa8934c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ServerStorageDevicesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.server.ServerStorageDevicesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__aa16490722cfc16de5acf5abd8405741b021c9e9aed0265729c5cee56a81c760)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAddress")
    def reset_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAddress", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="addressInput")
    def address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "addressInput"))

    @builtins.property
    @jsii.member(jsii_name="storageInput")
    def storage_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="address")
    def address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "address"))

    @address.setter
    def address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77d5b7c93220faaf6dd9467054774e5725fd8a75225556068d9412f7776111ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "address", value)

    @builtins.property
    @jsii.member(jsii_name="storage")
    def storage(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storage"))

    @storage.setter
    def storage(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9014362108e66a3d08ae0f2e9738528cfc887bea97394f5c9b3dbc053ab6d4e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storage", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__427c05296edc8e6c494743347b21ce68fe3ff0196dbcfb139503e9399ed4639b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ServerStorageDevices, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ServerStorageDevices, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ServerStorageDevices, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__963c88004521ac2a561739e84d699c5d8a33bbce0a64a04986268a9aeb455593)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-upcloud.server.ServerTemplate",
    jsii_struct_bases=[],
    name_mapping={
        "storage": "storage",
        "address": "address",
        "backup_rule": "backupRule",
        "delete_autoresize_backup": "deleteAutoresizeBackup",
        "filesystem_autoresize": "filesystemAutoresize",
        "size": "size",
        "title": "title",
    },
)
class ServerTemplate:
    def __init__(
        self,
        *,
        storage: builtins.str,
        address: typing.Optional[builtins.str] = None,
        backup_rule: typing.Optional[typing.Union["ServerTemplateBackupRule", typing.Dict[builtins.str, typing.Any]]] = None,
        delete_autoresize_backup: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        filesystem_autoresize: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        size: typing.Optional[jsii.Number] = None,
        title: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param storage: A valid storage UUID or template name. You can list available public templates with ``upctl storage list --public --template`` and available private templates with ``upctl storage list --template``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#storage Server#storage}
        :param address: The device address the storage will be attached to. Specify only the bus name (ide/scsi/virtio) to auto-select next available address from that bus. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#address Server#address}
        :param backup_rule: backup_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#backup_rule Server#backup_rule}
        :param delete_autoresize_backup: If set to true, the backup taken before the partition and filesystem resize attempt will be deleted immediately after success. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#delete_autoresize_backup Server#delete_autoresize_backup}
        :param filesystem_autoresize: If set to true, provider will attempt to resize partition and filesystem when the size of template storage changes. Please note that before the resize attempt is made, backup of the storage will be taken. If the resize attempt fails, the backup will be used to restore the storage and then deleted. If the resize attempt succeeds, backup will be kept (unless delete_autoresize_backup option is set to true). Taking and keeping backups incure costs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#filesystem_autoresize Server#filesystem_autoresize}
        :param size: The size of the storage in gigabytes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#size Server#size}
        :param title: A short, informative description. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#title Server#title}
        '''
        if isinstance(backup_rule, dict):
            backup_rule = ServerTemplateBackupRule(**backup_rule)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a85c384316c005f9127a81fcbc356ef71508b188a9b9433bf88b08a22e08cad)
            check_type(argname="argument storage", value=storage, expected_type=type_hints["storage"])
            check_type(argname="argument address", value=address, expected_type=type_hints["address"])
            check_type(argname="argument backup_rule", value=backup_rule, expected_type=type_hints["backup_rule"])
            check_type(argname="argument delete_autoresize_backup", value=delete_autoresize_backup, expected_type=type_hints["delete_autoresize_backup"])
            check_type(argname="argument filesystem_autoresize", value=filesystem_autoresize, expected_type=type_hints["filesystem_autoresize"])
            check_type(argname="argument size", value=size, expected_type=type_hints["size"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "storage": storage,
        }
        if address is not None:
            self._values["address"] = address
        if backup_rule is not None:
            self._values["backup_rule"] = backup_rule
        if delete_autoresize_backup is not None:
            self._values["delete_autoresize_backup"] = delete_autoresize_backup
        if filesystem_autoresize is not None:
            self._values["filesystem_autoresize"] = filesystem_autoresize
        if size is not None:
            self._values["size"] = size
        if title is not None:
            self._values["title"] = title

    @builtins.property
    def storage(self) -> builtins.str:
        '''A valid storage UUID or template name.

        You can list available public templates with ``upctl storage list --public --template`` and available private templates with ``upctl storage list --template``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#storage Server#storage}
        '''
        result = self._values.get("storage")
        assert result is not None, "Required property 'storage' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def address(self) -> typing.Optional[builtins.str]:
        '''The device address the storage will be attached to.

        Specify only the bus name (ide/scsi/virtio) to auto-select next available address from that bus.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#address Server#address}
        '''
        result = self._values.get("address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def backup_rule(self) -> typing.Optional["ServerTemplateBackupRule"]:
        '''backup_rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#backup_rule Server#backup_rule}
        '''
        result = self._values.get("backup_rule")
        return typing.cast(typing.Optional["ServerTemplateBackupRule"], result)

    @builtins.property
    def delete_autoresize_backup(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''If set to true, the backup taken before the partition and filesystem resize attempt will be deleted immediately after success.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#delete_autoresize_backup Server#delete_autoresize_backup}
        '''
        result = self._values.get("delete_autoresize_backup")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def filesystem_autoresize(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''If set to true, provider will attempt to resize partition and filesystem when the size of template storage changes.

        Please note that before the resize attempt is made, backup of the storage will be taken. If the resize attempt fails, the backup will be used
        to restore the storage and then deleted. If the resize attempt succeeds, backup will be kept (unless delete_autoresize_backup option is set to true).
        Taking and keeping backups incure costs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#filesystem_autoresize Server#filesystem_autoresize}
        '''
        result = self._values.get("filesystem_autoresize")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def size(self) -> typing.Optional[jsii.Number]:
        '''The size of the storage in gigabytes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#size Server#size}
        '''
        result = self._values.get("size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def title(self) -> typing.Optional[builtins.str]:
        '''A short, informative description.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#title Server#title}
        '''
        result = self._values.get("title")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServerTemplate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-upcloud.server.ServerTemplateBackupRule",
    jsii_struct_bases=[],
    name_mapping={"interval": "interval", "retention": "retention", "time": "time"},
)
class ServerTemplateBackupRule:
    def __init__(
        self,
        *,
        interval: builtins.str,
        retention: jsii.Number,
        time: builtins.str,
    ) -> None:
        '''
        :param interval: The weekday when the backup is created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#interval Server#interval}
        :param retention: The number of days before a backup is automatically deleted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#retention Server#retention}
        :param time: The time of day when the backup is created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#time Server#time}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0da849dc75d0030fd1866a13a6da5cd60acc32df054d4b38c21875c14c699895)
            check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
            check_type(argname="argument retention", value=retention, expected_type=type_hints["retention"])
            check_type(argname="argument time", value=time, expected_type=type_hints["time"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "interval": interval,
            "retention": retention,
            "time": time,
        }

    @builtins.property
    def interval(self) -> builtins.str:
        '''The weekday when the backup is created.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#interval Server#interval}
        '''
        result = self._values.get("interval")
        assert result is not None, "Required property 'interval' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def retention(self) -> jsii.Number:
        '''The number of days before a backup is automatically deleted.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#retention Server#retention}
        '''
        result = self._values.get("retention")
        assert result is not None, "Required property 'retention' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def time(self) -> builtins.str:
        '''The time of day when the backup is created.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#time Server#time}
        '''
        result = self._values.get("time")
        assert result is not None, "Required property 'time' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServerTemplateBackupRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServerTemplateBackupRuleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.server.ServerTemplateBackupRuleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8f25fb81968507d7e0b08a8dae5389ce95f026c45c28659add975e29c3404498)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="intervalInput")
    def interval_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "intervalInput"))

    @builtins.property
    @jsii.member(jsii_name="retentionInput")
    def retention_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retentionInput"))

    @builtins.property
    @jsii.member(jsii_name="timeInput")
    def time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeInput"))

    @builtins.property
    @jsii.member(jsii_name="interval")
    def interval(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "interval"))

    @interval.setter
    def interval(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8cd2c8f9ea443c20df23e85c3d00b8531501ef9634bd80450d111108f50be9d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "interval", value)

    @builtins.property
    @jsii.member(jsii_name="retention")
    def retention(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retention"))

    @retention.setter
    def retention(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a0b6af220df68085dcd97fccc4054a701b00b30a71638fbb4622b6b58f40373)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retention", value)

    @builtins.property
    @jsii.member(jsii_name="time")
    def time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "time"))

    @time.setter
    def time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42394eda9846bee43e13e31d1369893420594a1dbd33748f0f779d28b0dcb636)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "time", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ServerTemplateBackupRule]:
        return typing.cast(typing.Optional[ServerTemplateBackupRule], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ServerTemplateBackupRule]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68c5ccec377ad7d0ea9393f2fef6f5c45854a0e7848329cc404b17ecd5b941f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ServerTemplateOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.server.ServerTemplateOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3c497b3f58769bfb15770786b38a0d3cab824f167e30d427dd79147063221ef9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putBackupRule")
    def put_backup_rule(
        self,
        *,
        interval: builtins.str,
        retention: jsii.Number,
        time: builtins.str,
    ) -> None:
        '''
        :param interval: The weekday when the backup is created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#interval Server#interval}
        :param retention: The number of days before a backup is automatically deleted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#retention Server#retention}
        :param time: The time of day when the backup is created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/server#time Server#time}
        '''
        value = ServerTemplateBackupRule(
            interval=interval, retention=retention, time=time
        )

        return typing.cast(None, jsii.invoke(self, "putBackupRule", [value]))

    @jsii.member(jsii_name="resetAddress")
    def reset_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAddress", []))

    @jsii.member(jsii_name="resetBackupRule")
    def reset_backup_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackupRule", []))

    @jsii.member(jsii_name="resetDeleteAutoresizeBackup")
    def reset_delete_autoresize_backup(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeleteAutoresizeBackup", []))

    @jsii.member(jsii_name="resetFilesystemAutoresize")
    def reset_filesystem_autoresize(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilesystemAutoresize", []))

    @jsii.member(jsii_name="resetSize")
    def reset_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSize", []))

    @jsii.member(jsii_name="resetTitle")
    def reset_title(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTitle", []))

    @builtins.property
    @jsii.member(jsii_name="backupRule")
    def backup_rule(self) -> ServerTemplateBackupRuleOutputReference:
        return typing.cast(ServerTemplateBackupRuleOutputReference, jsii.get(self, "backupRule"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="tier")
    def tier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tier"))

    @builtins.property
    @jsii.member(jsii_name="addressInput")
    def address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "addressInput"))

    @builtins.property
    @jsii.member(jsii_name="backupRuleInput")
    def backup_rule_input(self) -> typing.Optional[ServerTemplateBackupRule]:
        return typing.cast(typing.Optional[ServerTemplateBackupRule], jsii.get(self, "backupRuleInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteAutoresizeBackupInput")
    def delete_autoresize_backup_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "deleteAutoresizeBackupInput"))

    @builtins.property
    @jsii.member(jsii_name="filesystemAutoresizeInput")
    def filesystem_autoresize_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "filesystemAutoresizeInput"))

    @builtins.property
    @jsii.member(jsii_name="sizeInput")
    def size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sizeInput"))

    @builtins.property
    @jsii.member(jsii_name="storageInput")
    def storage_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageInput"))

    @builtins.property
    @jsii.member(jsii_name="titleInput")
    def title_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "titleInput"))

    @builtins.property
    @jsii.member(jsii_name="address")
    def address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "address"))

    @address.setter
    def address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ec88e6f0117f5a01bf0be4edaac88182f98191d5898e18968a024f2c7eca1a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "address", value)

    @builtins.property
    @jsii.member(jsii_name="deleteAutoresizeBackup")
    def delete_autoresize_backup(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "deleteAutoresizeBackup"))

    @delete_autoresize_backup.setter
    def delete_autoresize_backup(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c856e0710f9cda94f9f1271c085ee9d4a1499307057c893c123eafc72fc313e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deleteAutoresizeBackup", value)

    @builtins.property
    @jsii.member(jsii_name="filesystemAutoresize")
    def filesystem_autoresize(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "filesystemAutoresize"))

    @filesystem_autoresize.setter
    def filesystem_autoresize(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15a41032ac46233b165e6594cff61432ce1029e197ad6bac634749812056291b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filesystemAutoresize", value)

    @builtins.property
    @jsii.member(jsii_name="size")
    def size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "size"))

    @size.setter
    def size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bdfb49737c8824193509f7b4f8be69cc4f8f53b26b54e65c015fca12ea711265)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "size", value)

    @builtins.property
    @jsii.member(jsii_name="storage")
    def storage(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storage"))

    @storage.setter
    def storage(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f908c7d0cd75d51f9555bfd6ab8e64de276cac6a09657d4f952345bcf403779)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storage", value)

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @title.setter
    def title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64f0d7019cf74d0117aacc7a12f88f6a61c491221ba27a95745ec4a01a80eec4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ServerTemplate]:
        return typing.cast(typing.Optional[ServerTemplate], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ServerTemplate]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd8f4ccfba9e26748588ee2d5a223525d90da38d9c2cb1de9bf069079f9853f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Server",
    "ServerConfig",
    "ServerLogin",
    "ServerLoginOutputReference",
    "ServerNetworkInterface",
    "ServerNetworkInterfaceList",
    "ServerNetworkInterfaceOutputReference",
    "ServerSimpleBackup",
    "ServerSimpleBackupOutputReference",
    "ServerStorageDevices",
    "ServerStorageDevicesList",
    "ServerStorageDevicesOutputReference",
    "ServerTemplate",
    "ServerTemplateBackupRule",
    "ServerTemplateBackupRuleOutputReference",
    "ServerTemplateOutputReference",
]

publication.publish()

def _typecheckingstub__6b83690e478f8730a1b183dfb2bf71b179dc55ba8028fd8cc73841eff54172a9(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    hostname: builtins.str,
    network_interface: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ServerNetworkInterface, typing.Dict[builtins.str, typing.Any]]]],
    zone: builtins.str,
    cpu: typing.Optional[jsii.Number] = None,
    firewall: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    host: typing.Optional[jsii.Number] = None,
    id: typing.Optional[builtins.str] = None,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    login: typing.Optional[typing.Union[ServerLogin, typing.Dict[builtins.str, typing.Any]]] = None,
    mem: typing.Optional[jsii.Number] = None,
    metadata: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    plan: typing.Optional[builtins.str] = None,
    simple_backup: typing.Optional[typing.Union[ServerSimpleBackup, typing.Dict[builtins.str, typing.Any]]] = None,
    storage_devices: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ServerStorageDevices, typing.Dict[builtins.str, typing.Any]]]]] = None,
    tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    template: typing.Optional[typing.Union[ServerTemplate, typing.Dict[builtins.str, typing.Any]]] = None,
    title: typing.Optional[builtins.str] = None,
    user_data: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__2784a2f8e61298bcd760c00280858e93027365e3107df743c65e925390d065ff(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ServerNetworkInterface, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2c4cd707e662e8744252abfd6f62940a96bcdfc90c7389a218eb5a2acab2006(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ServerStorageDevices, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0bf29acd3dd45353eecfc5a63f6040bd66f55ef883a41491d92f1bdbe810a40(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__faf5fe2f1617d856951894b09503ce986b9b9e75f119670e34925d2d45d2e9ed(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb33c3002695f65e8de16860ddf00ce31ac89ba44e937051e0add8e77bb120c2(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4bd72ca4af6dd9b479c0262e490984bdbd3191d9b6e06c6924b98a95b88a2ce(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a84cfa579ab88830b19af88519f30728d1a5668fda89bc3e98d7b7cb076e00cc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a7892fe5de8b838249765679a48d6de643cd5ca2b10527938954d152ae696ef(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__124e11a99805e080ae09bb64a779c4f3bf94f05876de9f8f9b682c9fe74e79e6(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64fa85207ab264b6f079b98afe3eef4ec2bf20d249f7caa10f6ab31566841844(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2da76f679e87688e11b6f83fb15ba717554341797b152012a0fb49e67140b935(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e7175151be1c034f617e5043b4a582fa7a23b63257729e9f6b6957e2b922bfb(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae9bce333377a9eba2c28adc33c40c562a185ced6585b2a01045577d13004430(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64b2aea0b37c12d0056c07c0c4281a978b335a3259b4e52cc2e9287e80bfa864(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__189f51a8a94e7de544c3857c63fb20bd2ee94539e95189dafb4bab5cb85e9236(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea0c30195fdb4e86d473d86dcc3b49fe1de4f105b946dcc2035464e29e243e2a(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    hostname: builtins.str,
    network_interface: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ServerNetworkInterface, typing.Dict[builtins.str, typing.Any]]]],
    zone: builtins.str,
    cpu: typing.Optional[jsii.Number] = None,
    firewall: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    host: typing.Optional[jsii.Number] = None,
    id: typing.Optional[builtins.str] = None,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    login: typing.Optional[typing.Union[ServerLogin, typing.Dict[builtins.str, typing.Any]]] = None,
    mem: typing.Optional[jsii.Number] = None,
    metadata: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    plan: typing.Optional[builtins.str] = None,
    simple_backup: typing.Optional[typing.Union[ServerSimpleBackup, typing.Dict[builtins.str, typing.Any]]] = None,
    storage_devices: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ServerStorageDevices, typing.Dict[builtins.str, typing.Any]]]]] = None,
    tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    template: typing.Optional[typing.Union[ServerTemplate, typing.Dict[builtins.str, typing.Any]]] = None,
    title: typing.Optional[builtins.str] = None,
    user_data: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba39a2ee1d911b76fb74554613ea114a5a572a0bf44aae12941ef4644ef7377a(
    *,
    create_password: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    keys: typing.Optional[typing.Sequence[builtins.str]] = None,
    password_delivery: typing.Optional[builtins.str] = None,
    user: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb37b4e00c78f37c38cbba42c725d341426cd4846a37328a858efbce8e63b347(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52fef0f21493a08a9b1120b5e06665743a76af6b2c68ad33657352e375d30f83(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b692749540d070af5a9539957a6fb3b45c73bf325a279cde1ce841cb2b3a368(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0cb6ee9476d3d13341856fea701d89ab77f7390a5c83899ab22e0865a2cfaf45(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5428294ae30fe53a9c3e6f59c5d7345c00077d52ca2969ca46d13b15b72bcf2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5a2e407880016cbd5838a509393761434aa730eb60add2b4b29eadad0776d3b(
    value: typing.Optional[ServerLogin],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd495e0f43b555636347e658837821c13810606782b5f840f155acbfbcf8b7ea(
    *,
    type: builtins.str,
    bootable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ip_address: typing.Optional[builtins.str] = None,
    ip_address_family: typing.Optional[builtins.str] = None,
    network: typing.Optional[builtins.str] = None,
    source_ip_filtering: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc54b91b5d0d7c97de16d571e1bd39a117d649214c8689ebf9994e4e990fd340(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33afd8f34658cdde16c336c0c57cf4773e6fec818004f2ef62f5737777f120ea(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__964638e95b9eb64f9888fef8669fefd3199a22770bc88f1e9e55385ffcf19266(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f425debfe0fca1e3b8c8cd983ff8f17a5cee4a67bedbf8b9045e682766c159c(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecc2284e90d7a1c3606d00ad08be4fb4481c645e68a00a279e10ebf0666a6875(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05c518a721134139fda2b2f95e72e1fc5c01453ef555dec5b958772b12cc8b9c(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ServerNetworkInterface]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f351e78b8ed148a38258a4e1044dee8183c1dc0faa0e2ff98d6538a768811b64(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47ed0e3d16bdd5428b4c7adf673350899ade00d8859059ed0f26439a53c0b519(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97b4cbf583d41648739b128bd01df2684cfe29bc55efc08b02280697b7207be3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27ca96659b5cf24779fba934b13768313666a313e1ec402934147d93b04c671d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4455383f612dd1e5e7b829b5df56c87f6147838c2bd408299074c0fe1fcb3457(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67715c977e47025dc675151bb1733aeb13846dd9b753760e7f626bb21f196235(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21f40dacaedad9009711ae5ffd3910b0ae85807a8cec83e69f5f166a7cf791ec(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8653f81da3a79a9a2fd0667eb122024a0e78b7183d06eaf233aa6b039ab88013(
    value: typing.Optional[typing.Union[ServerNetworkInterface, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0bd20cac4bdde3b91171ae0bf44e53e9583617261eaf0793a175a7d8da3cee3(
    *,
    plan: builtins.str,
    time: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__543283afc6e5dcbaed6d63b62679b76fe001c3a94535d560e5ee698bde877d12(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3fcfd10d4cc42b7a124d6deb709aed8a84109c8a6ccf87e6ea1c1446e290e765(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2a12363cbec7f1b1136e6a05c23fd0826a6915ccf0b0b64f9f4fccc66a7b1da(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__047ada69f3d10e42273140f60146f8fdf26e9f7c5b02497edf7ff0b3533062bd(
    value: typing.Optional[ServerSimpleBackup],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__deefc3ca26ddd4529dd49d665d0a7e4d178ed9e318d7a6ed318fe000f57713ea(
    *,
    storage: builtins.str,
    address: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b1a8309ae0e42008d4d9a04fa384232a242ebf581bdfe667b3d4d9318c423e1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0cd494dc7b3e8661672bce1c045c252c6330d80b0f7be6bfd03cb3eab0419cfc(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c36a029bc93903864475ea526a1d5d88d1c38739833442c25954cc78734d073(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6106531b80754e3450342cca25dccc97ecca94111c0beac393fdf0cc5992ba2(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__404155dd5b9ae6ef51ecbd295a6258fba082b02c4edde041ed4e3fdd0e39479f(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d8da2a7cdb20f04a3d3e26873cb26f1bad3c31fb192cec0590a5630aa8934c6(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ServerStorageDevices]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa16490722cfc16de5acf5abd8405741b021c9e9aed0265729c5cee56a81c760(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77d5b7c93220faaf6dd9467054774e5725fd8a75225556068d9412f7776111ea(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9014362108e66a3d08ae0f2e9738528cfc887bea97394f5c9b3dbc053ab6d4e5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__427c05296edc8e6c494743347b21ce68fe3ff0196dbcfb139503e9399ed4639b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__963c88004521ac2a561739e84d699c5d8a33bbce0a64a04986268a9aeb455593(
    value: typing.Optional[typing.Union[ServerStorageDevices, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a85c384316c005f9127a81fcbc356ef71508b188a9b9433bf88b08a22e08cad(
    *,
    storage: builtins.str,
    address: typing.Optional[builtins.str] = None,
    backup_rule: typing.Optional[typing.Union[ServerTemplateBackupRule, typing.Dict[builtins.str, typing.Any]]] = None,
    delete_autoresize_backup: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    filesystem_autoresize: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    size: typing.Optional[jsii.Number] = None,
    title: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0da849dc75d0030fd1866a13a6da5cd60acc32df054d4b38c21875c14c699895(
    *,
    interval: builtins.str,
    retention: jsii.Number,
    time: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f25fb81968507d7e0b08a8dae5389ce95f026c45c28659add975e29c3404498(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8cd2c8f9ea443c20df23e85c3d00b8531501ef9634bd80450d111108f50be9d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a0b6af220df68085dcd97fccc4054a701b00b30a71638fbb4622b6b58f40373(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42394eda9846bee43e13e31d1369893420594a1dbd33748f0f779d28b0dcb636(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68c5ccec377ad7d0ea9393f2fef6f5c45854a0e7848329cc404b17ecd5b941f9(
    value: typing.Optional[ServerTemplateBackupRule],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c497b3f58769bfb15770786b38a0d3cab824f167e30d427dd79147063221ef9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ec88e6f0117f5a01bf0be4edaac88182f98191d5898e18968a024f2c7eca1a0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c856e0710f9cda94f9f1271c085ee9d4a1499307057c893c123eafc72fc313e7(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15a41032ac46233b165e6594cff61432ce1029e197ad6bac634749812056291b(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bdfb49737c8824193509f7b4f8be69cc4f8f53b26b54e65c015fca12ea711265(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f908c7d0cd75d51f9555bfd6ab8e64de276cac6a09657d4f952345bcf403779(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64f0d7019cf74d0117aacc7a12f88f6a61c491221ba27a95745ec4a01a80eec4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd8f4ccfba9e26748588ee2d5a223525d90da38d9c2cb1de9bf069079f9853f4(
    value: typing.Optional[ServerTemplate],
) -> None:
    """Type checking stubs"""
    pass
