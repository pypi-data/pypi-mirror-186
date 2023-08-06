'''
# `data_consul_keys`

Refer to the Terraform Registory for docs: [`data_consul_keys`](https://www.terraform.io/docs/providers/consul/d/keys).
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


class DataConsulKeys(
    _cdktf_9a9027ec.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-consul.dataConsulKeys.DataConsulKeys",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/consul/d/keys consul_keys}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        datacenter: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        key: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataConsulKeysKey", typing.Dict[builtins.str, typing.Any]]]]] = None,
        namespace: typing.Optional[builtins.str] = None,
        partition: typing.Optional[builtins.str] = None,
        token: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/consul/d/keys consul_keys} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param datacenter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/d/keys#datacenter DataConsulKeys#datacenter}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/d/keys#id DataConsulKeys#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param key: key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/d/keys#key DataConsulKeys#key}
        :param namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/d/keys#namespace DataConsulKeys#namespace}.
        :param partition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/d/keys#partition DataConsulKeys#partition}.
        :param token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/d/keys#token DataConsulKeys#token}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61c8961e59234e4e715f8b75e52be50a561306c716fdaf131fd6b1514fb979fa)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataConsulKeysConfig(
            datacenter=datacenter,
            id=id,
            key=key,
            namespace=namespace,
            partition=partition,
            token=token,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putKey")
    def put_key(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataConsulKeysKey", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83a3bda505d04c116c1beba9486d4a5bc1c8ce9e0b21f38c1c48b6a6d5c84f28)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putKey", [value]))

    @jsii.member(jsii_name="resetDatacenter")
    def reset_datacenter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatacenter", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @jsii.member(jsii_name="resetPartition")
    def reset_partition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPartition", []))

    @jsii.member(jsii_name="resetToken")
    def reset_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetToken", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> "DataConsulKeysKeyList":
        return typing.cast("DataConsulKeysKeyList", jsii.get(self, "key"))

    @builtins.property
    @jsii.member(jsii_name="var")
    def var(self) -> _cdktf_9a9027ec.StringMap:
        return typing.cast(_cdktf_9a9027ec.StringMap, jsii.get(self, "var"))

    @builtins.property
    @jsii.member(jsii_name="datacenterInput")
    def datacenter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datacenterInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataConsulKeysKey"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataConsulKeysKey"]]], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="partitionInput")
    def partition_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "partitionInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenInput")
    def token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenInput"))

    @builtins.property
    @jsii.member(jsii_name="datacenter")
    def datacenter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datacenter"))

    @datacenter.setter
    def datacenter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8e450f9b7760c7477ccbc7c3eed7bc6f96ae1f7106c01ceb3a5d562570bc00f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datacenter", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__521b7b53c01f373c97987af257871b92b262ce98f35eab56436a2915bc559af1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1abf186c7e2fc2c503d2ab9ebe857f6ce73838fe22e76df3e8ebd4f3373bced)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="partition")
    def partition(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "partition"))

    @partition.setter
    def partition(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dbd60f902b5dda84729263ff5de4cb53ea8f2ce77b31b58f8544ff694f15604a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "partition", value)

    @builtins.property
    @jsii.member(jsii_name="token")
    def token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "token"))

    @token.setter
    def token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8339e3500ca639a3950ce77245234bd4d4d3c57a87cbd50d7ce2ca51e9486f35)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "token", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-consul.dataConsulKeys.DataConsulKeysConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "datacenter": "datacenter",
        "id": "id",
        "key": "key",
        "namespace": "namespace",
        "partition": "partition",
        "token": "token",
    },
)
class DataConsulKeysConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        datacenter: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        key: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataConsulKeysKey", typing.Dict[builtins.str, typing.Any]]]]] = None,
        namespace: typing.Optional[builtins.str] = None,
        partition: typing.Optional[builtins.str] = None,
        token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param datacenter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/d/keys#datacenter DataConsulKeys#datacenter}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/d/keys#id DataConsulKeys#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param key: key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/d/keys#key DataConsulKeys#key}
        :param namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/d/keys#namespace DataConsulKeys#namespace}.
        :param partition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/d/keys#partition DataConsulKeys#partition}.
        :param token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/d/keys#token DataConsulKeys#token}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8abed789981867b82f6abd305bc19e9812b7f50c09b1744e324ca3c0d8d11694)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument datacenter", value=datacenter, expected_type=type_hints["datacenter"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument partition", value=partition, expected_type=type_hints["partition"])
            check_type(argname="argument token", value=token, expected_type=type_hints["token"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
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
        if datacenter is not None:
            self._values["datacenter"] = datacenter
        if id is not None:
            self._values["id"] = id
        if key is not None:
            self._values["key"] = key
        if namespace is not None:
            self._values["namespace"] = namespace
        if partition is not None:
            self._values["partition"] = partition
        if token is not None:
            self._values["token"] = token

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
    def datacenter(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/d/keys#datacenter DataConsulKeys#datacenter}.'''
        result = self._values.get("datacenter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/d/keys#id DataConsulKeys#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataConsulKeysKey"]]]:
        '''key block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/d/keys#key DataConsulKeys#key}
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataConsulKeysKey"]]], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/d/keys#namespace DataConsulKeys#namespace}.'''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def partition(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/d/keys#partition DataConsulKeys#partition}.'''
        result = self._values.get("partition")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def token(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/d/keys#token DataConsulKeys#token}.'''
        result = self._values.get("token")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataConsulKeysConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-consul.dataConsulKeys.DataConsulKeysKey",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "path": "path", "default": "default"},
)
class DataConsulKeysKey:
    def __init__(
        self,
        *,
        name: builtins.str,
        path: builtins.str,
        default: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/d/keys#name DataConsulKeys#name}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/d/keys#path DataConsulKeys#path}.
        :param default: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/d/keys#default DataConsulKeys#default}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f300a26f87f2f03ce1eb31c9d5b65466dde6de8e2b99cb380427a013a5fe6bb1)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument default", value=default, expected_type=type_hints["default"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "path": path,
        }
        if default is not None:
            self._values["default"] = default

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/d/keys#name DataConsulKeys#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/d/keys#path DataConsulKeys#path}.'''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/d/keys#default DataConsulKeys#default}.'''
        result = self._values.get("default")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataConsulKeysKey(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataConsulKeysKeyList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-consul.dataConsulKeys.DataConsulKeysKeyList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ddf1606cc8032646e487cf5ea2ab073b565096aff55f3f04f76d46115aa4ed38)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "DataConsulKeysKeyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2d7ab25e79c27f1ed8963767aa218a6dfc5f68021a16e134d2c9426762ef1b2)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataConsulKeysKeyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c8b05610cb65d654010b8ee80465409b72bf5ec20f224305197257f18750588)
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
            type_hints = typing.get_type_hints(_typecheckingstub__933c563ff47aa1da98293664d89918cc91666a705efcd55e687bc6c0c7d7ee7c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__083986a8eb75c57584ff95590bbb1815a6fc83b15804de6f1d0cd7ae91962b16)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataConsulKeysKey]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataConsulKeysKey]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataConsulKeysKey]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1204ef54377a64c01ff6ea1db024bcaf874c7bad5805edae0a2a7bf0d97e8704)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataConsulKeysKeyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-consul.dataConsulKeys.DataConsulKeysKeyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f4025c935699a508424c199cf1dd2407644ffb405a887f0edfc2aaa1cb118631)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDefault")
    def reset_default(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefault", []))

    @builtins.property
    @jsii.member(jsii_name="defaultInput")
    def default_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="default")
    def default(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "default"))

    @default.setter
    def default(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ea69f9000fa145c5046a2be6c7123030d531649e7124a14edbf7d4955db098b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "default", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d248b8bfd9e571017653d48dd2cdea82299cb3aa64df0dfaf9331eb49f8fa40)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__731b3db5405e234e424fb2f8f84da6876d2ca0c9295230557636a0ba36944428)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataConsulKeysKey, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataConsulKeysKey, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataConsulKeysKey, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38f30b236080b276565a4c2793e6d202dcb2f1aa7889a804a71bfe71b6d86a7b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataConsulKeys",
    "DataConsulKeysConfig",
    "DataConsulKeysKey",
    "DataConsulKeysKeyList",
    "DataConsulKeysKeyOutputReference",
]

publication.publish()

def _typecheckingstub__61c8961e59234e4e715f8b75e52be50a561306c716fdaf131fd6b1514fb979fa(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    datacenter: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    key: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataConsulKeysKey, typing.Dict[builtins.str, typing.Any]]]]] = None,
    namespace: typing.Optional[builtins.str] = None,
    partition: typing.Optional[builtins.str] = None,
    token: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__83a3bda505d04c116c1beba9486d4a5bc1c8ce9e0b21f38c1c48b6a6d5c84f28(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataConsulKeysKey, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8e450f9b7760c7477ccbc7c3eed7bc6f96ae1f7106c01ceb3a5d562570bc00f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__521b7b53c01f373c97987af257871b92b262ce98f35eab56436a2915bc559af1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1abf186c7e2fc2c503d2ab9ebe857f6ce73838fe22e76df3e8ebd4f3373bced(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbd60f902b5dda84729263ff5de4cb53ea8f2ce77b31b58f8544ff694f15604a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8339e3500ca639a3950ce77245234bd4d4d3c57a87cbd50d7ce2ca51e9486f35(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8abed789981867b82f6abd305bc19e9812b7f50c09b1744e324ca3c0d8d11694(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    datacenter: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    key: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataConsulKeysKey, typing.Dict[builtins.str, typing.Any]]]]] = None,
    namespace: typing.Optional[builtins.str] = None,
    partition: typing.Optional[builtins.str] = None,
    token: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f300a26f87f2f03ce1eb31c9d5b65466dde6de8e2b99cb380427a013a5fe6bb1(
    *,
    name: builtins.str,
    path: builtins.str,
    default: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddf1606cc8032646e487cf5ea2ab073b565096aff55f3f04f76d46115aa4ed38(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2d7ab25e79c27f1ed8963767aa218a6dfc5f68021a16e134d2c9426762ef1b2(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c8b05610cb65d654010b8ee80465409b72bf5ec20f224305197257f18750588(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__933c563ff47aa1da98293664d89918cc91666a705efcd55e687bc6c0c7d7ee7c(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__083986a8eb75c57584ff95590bbb1815a6fc83b15804de6f1d0cd7ae91962b16(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1204ef54377a64c01ff6ea1db024bcaf874c7bad5805edae0a2a7bf0d97e8704(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataConsulKeysKey]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4025c935699a508424c199cf1dd2407644ffb405a887f0edfc2aaa1cb118631(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ea69f9000fa145c5046a2be6c7123030d531649e7124a14edbf7d4955db098b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d248b8bfd9e571017653d48dd2cdea82299cb3aa64df0dfaf9331eb49f8fa40(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__731b3db5405e234e424fb2f8f84da6876d2ca0c9295230557636a0ba36944428(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38f30b236080b276565a4c2793e6d202dcb2f1aa7889a804a71bfe71b6d86a7b(
    value: typing.Optional[typing.Union[DataConsulKeysKey, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
