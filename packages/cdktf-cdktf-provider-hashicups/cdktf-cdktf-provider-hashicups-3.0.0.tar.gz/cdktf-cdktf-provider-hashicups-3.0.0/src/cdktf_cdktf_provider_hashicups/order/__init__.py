'''
# `hashicups_order`

Refer to the Terraform Registory for docs: [`hashicups_order`](https://www.terraform.io/docs/providers/hashicups/r/order).
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


class Order(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-hashicups.order.Order",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/hashicups/r/order hashicups_order}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        items: typing.Union[typing.Sequence[typing.Union["OrderItems", typing.Dict[builtins.str, typing.Any]]], _cdktf_9a9027ec.IResolvable],
        id: typing.Optional[builtins.str] = None,
        last_updated: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/hashicups/r/order hashicups_order} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param items: items block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hashicups/r/order#items Order#items}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hashicups/r/order#id Order#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param last_updated: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hashicups/r/order#last_updated Order#last_updated}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5e0cc08d09507ec04b0e5240dda5abaa2d7cc7ec2829dd9c342af637ce82076)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = OrderConfig(
            items=items,
            id=id,
            last_updated=last_updated,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putItems")
    def put_items(
        self,
        value: typing.Union[typing.Sequence[typing.Union["OrderItems", typing.Dict[builtins.str, typing.Any]]], _cdktf_9a9027ec.IResolvable],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c126a8a81246546b9febbfee691d1e0ccdd346e075087ffb9cd55a8f020d5911)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putItems", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLastUpdated")
    def reset_last_updated(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLastUpdated", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="items")
    def items(self) -> "OrderItemsList":
        return typing.cast("OrderItemsList", jsii.get(self, "items"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="itemsInput")
    def items_input(
        self,
    ) -> typing.Optional[typing.Union[typing.List["OrderItems"], _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[typing.List["OrderItems"], _cdktf_9a9027ec.IResolvable]], jsii.get(self, "itemsInput"))

    @builtins.property
    @jsii.member(jsii_name="lastUpdatedInput")
    def last_updated_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lastUpdatedInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16e14b82c182a97b287eb772d0a958de8882cfc86524d3014e82b88e27f7a511)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="lastUpdated")
    def last_updated(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastUpdated"))

    @last_updated.setter
    def last_updated(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91a3b5ad67a47d449d9dded5e97a7ef3020b7228a8536c82e7727040d183b20d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lastUpdated", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-hashicups.order.OrderConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "items": "items",
        "id": "id",
        "last_updated": "lastUpdated",
    },
)
class OrderConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        items: typing.Union[typing.Sequence[typing.Union["OrderItems", typing.Dict[builtins.str, typing.Any]]], _cdktf_9a9027ec.IResolvable],
        id: typing.Optional[builtins.str] = None,
        last_updated: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param items: items block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hashicups/r/order#items Order#items}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hashicups/r/order#id Order#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param last_updated: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hashicups/r/order#last_updated Order#last_updated}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__508754e3122383f854f4d8512bfbc631821c67977e6d2fa3c09b732d9441b140)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument items", value=items, expected_type=type_hints["items"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument last_updated", value=last_updated, expected_type=type_hints["last_updated"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "items": items,
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
        if last_updated is not None:
            self._values["last_updated"] = last_updated

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
    def items(
        self,
    ) -> typing.Union[typing.List["OrderItems"], _cdktf_9a9027ec.IResolvable]:
        '''items block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hashicups/r/order#items Order#items}
        '''
        result = self._values.get("items")
        assert result is not None, "Required property 'items' is missing"
        return typing.cast(typing.Union[typing.List["OrderItems"], _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hashicups/r/order#id Order#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def last_updated(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hashicups/r/order#last_updated Order#last_updated}.'''
        result = self._values.get("last_updated")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OrderConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-hashicups.order.OrderItems",
    jsii_struct_bases=[],
    name_mapping={"coffee": "coffee", "quantity": "quantity"},
)
class OrderItems:
    def __init__(
        self,
        *,
        coffee: typing.Union["OrderItemsCoffee", typing.Dict[builtins.str, typing.Any]],
        quantity: jsii.Number,
    ) -> None:
        '''
        :param coffee: coffee block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hashicups/r/order#coffee Order#coffee}
        :param quantity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hashicups/r/order#quantity Order#quantity}.
        '''
        if isinstance(coffee, dict):
            coffee = OrderItemsCoffee(**coffee)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f004744e71417b2d7f1a3c6e6bd0bf65f1e2c947c1fa63be99afb6b20703338)
            check_type(argname="argument coffee", value=coffee, expected_type=type_hints["coffee"])
            check_type(argname="argument quantity", value=quantity, expected_type=type_hints["quantity"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "coffee": coffee,
            "quantity": quantity,
        }

    @builtins.property
    def coffee(self) -> "OrderItemsCoffee":
        '''coffee block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hashicups/r/order#coffee Order#coffee}
        '''
        result = self._values.get("coffee")
        assert result is not None, "Required property 'coffee' is missing"
        return typing.cast("OrderItemsCoffee", result)

    @builtins.property
    def quantity(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hashicups/r/order#quantity Order#quantity}.'''
        result = self._values.get("quantity")
        assert result is not None, "Required property 'quantity' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OrderItems(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-hashicups.order.OrderItemsCoffee",
    jsii_struct_bases=[],
    name_mapping={"id": "id"},
)
class OrderItemsCoffee:
    def __init__(self, *, id: jsii.Number) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hashicups/r/order#id Order#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1cb8596abd2c21dcab116d0a08df0b710a96059bbf5945b8f24b9ee89d2d431)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "id": id,
        }

    @builtins.property
    def id(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hashicups/r/order#id Order#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OrderItemsCoffee(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OrderItemsCoffeeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-hashicups.order.OrderItemsCoffeeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__995a181c50f868f953d9bde724a597e41b80e5422e48edd37ff3bebef3db157f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @builtins.property
    @jsii.member(jsii_name="image")
    def image(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "image"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="price")
    def price(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "price"))

    @builtins.property
    @jsii.member(jsii_name="teaser")
    def teaser(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "teaser"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "id"))

    @id.setter
    def id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__071408598a69f37b03d80bc1c07a3783bc2c84037ad393cbd908500277031c39)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OrderItemsCoffee]:
        return typing.cast(typing.Optional[OrderItemsCoffee], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[OrderItemsCoffee]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__499f0b81bb0bc1a00893f9c28bb1847fe3627aa8f3380d2c8853c2011cb7cd8c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OrderItemsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-hashicups.order.OrderItemsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5101bebe39f69cf03f70d7378aa01542aa663cb97459138de3f53146bef7be8e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "OrderItemsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e2ad16f74686dc7f817a080870bb15cd4c0fad3ac95c97af149faa5f45fc2ab)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OrderItemsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b24a245ad87da8f605504b2514ebcf2e6150dc89281157b2d372a3fd9da6e43)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d137f129b5bfcd34a525e10c6556319c7a78430a1a72b67aaef141470bdea2bc)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0b5bda55ba4230bff8efbcdffe5d263d920eba2bb92101960bda02e0f4679d69)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[typing.List[OrderItems], _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[typing.List[OrderItems], _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[typing.List[OrderItems], _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9cdc37f913f3849c41be3fd8293207669f7c15daa73f972022decac1cfe0a0a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OrderItemsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-hashicups.order.OrderItemsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e21fddbe165eb9d403b1a8e799e4637883f11903dcc51df3eb88d3f222c311f2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putCoffee")
    def put_coffee(self, *, id: jsii.Number) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hashicups/r/order#id Order#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        value = OrderItemsCoffee(id=id)

        return typing.cast(None, jsii.invoke(self, "putCoffee", [value]))

    @builtins.property
    @jsii.member(jsii_name="coffee")
    def coffee(self) -> OrderItemsCoffeeOutputReference:
        return typing.cast(OrderItemsCoffeeOutputReference, jsii.get(self, "coffee"))

    @builtins.property
    @jsii.member(jsii_name="coffeeInput")
    def coffee_input(self) -> typing.Optional[OrderItemsCoffee]:
        return typing.cast(typing.Optional[OrderItemsCoffee], jsii.get(self, "coffeeInput"))

    @builtins.property
    @jsii.member(jsii_name="quantityInput")
    def quantity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "quantityInput"))

    @builtins.property
    @jsii.member(jsii_name="quantity")
    def quantity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "quantity"))

    @quantity.setter
    def quantity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02a3f8e09572eedc8c8f2472978dab11d950d7b2590fdbdef72969b8eb1502ba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "quantity", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OrderItems, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OrderItems, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OrderItems, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d693df4eededdf816297774f4f059cfe5f35819b2989fbf108356f0d1b966c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Order",
    "OrderConfig",
    "OrderItems",
    "OrderItemsCoffee",
    "OrderItemsCoffeeOutputReference",
    "OrderItemsList",
    "OrderItemsOutputReference",
]

publication.publish()

def _typecheckingstub__a5e0cc08d09507ec04b0e5240dda5abaa2d7cc7ec2829dd9c342af637ce82076(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    items: typing.Union[typing.Sequence[typing.Union[OrderItems, typing.Dict[builtins.str, typing.Any]]], _cdktf_9a9027ec.IResolvable],
    id: typing.Optional[builtins.str] = None,
    last_updated: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__c126a8a81246546b9febbfee691d1e0ccdd346e075087ffb9cd55a8f020d5911(
    value: typing.Union[typing.Sequence[typing.Union[OrderItems, typing.Dict[builtins.str, typing.Any]]], _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16e14b82c182a97b287eb772d0a958de8882cfc86524d3014e82b88e27f7a511(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91a3b5ad67a47d449d9dded5e97a7ef3020b7228a8536c82e7727040d183b20d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__508754e3122383f854f4d8512bfbc631821c67977e6d2fa3c09b732d9441b140(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    items: typing.Union[typing.Sequence[typing.Union[OrderItems, typing.Dict[builtins.str, typing.Any]]], _cdktf_9a9027ec.IResolvable],
    id: typing.Optional[builtins.str] = None,
    last_updated: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f004744e71417b2d7f1a3c6e6bd0bf65f1e2c947c1fa63be99afb6b20703338(
    *,
    coffee: typing.Union[OrderItemsCoffee, typing.Dict[builtins.str, typing.Any]],
    quantity: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1cb8596abd2c21dcab116d0a08df0b710a96059bbf5945b8f24b9ee89d2d431(
    *,
    id: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__995a181c50f868f953d9bde724a597e41b80e5422e48edd37ff3bebef3db157f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__071408598a69f37b03d80bc1c07a3783bc2c84037ad393cbd908500277031c39(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__499f0b81bb0bc1a00893f9c28bb1847fe3627aa8f3380d2c8853c2011cb7cd8c(
    value: typing.Optional[OrderItemsCoffee],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5101bebe39f69cf03f70d7378aa01542aa663cb97459138de3f53146bef7be8e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e2ad16f74686dc7f817a080870bb15cd4c0fad3ac95c97af149faa5f45fc2ab(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b24a245ad87da8f605504b2514ebcf2e6150dc89281157b2d372a3fd9da6e43(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d137f129b5bfcd34a525e10c6556319c7a78430a1a72b67aaef141470bdea2bc(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b5bda55ba4230bff8efbcdffe5d263d920eba2bb92101960bda02e0f4679d69(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9cdc37f913f3849c41be3fd8293207669f7c15daa73f972022decac1cfe0a0a(
    value: typing.Optional[typing.Union[typing.List[OrderItems], _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e21fddbe165eb9d403b1a8e799e4637883f11903dcc51df3eb88d3f222c311f2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02a3f8e09572eedc8c8f2472978dab11d950d7b2590fdbdef72969b8eb1502ba(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d693df4eededdf816297774f4f059cfe5f35819b2989fbf108356f0d1b966c6(
    value: typing.Optional[typing.Union[OrderItems, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
