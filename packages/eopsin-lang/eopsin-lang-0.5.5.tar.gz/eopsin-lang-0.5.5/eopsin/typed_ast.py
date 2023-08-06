import typing
from ast import *
from dataclasses import dataclass

from frozenlist import FrozenList

import pluthon as plt
import uplc


def FrozenFrozenList(l: list):
    fl = FrozenList(l)
    fl.freeze()
    return fl


class Type:
    def constr_type(self) -> "InstanceType":
        """The type of the constructor for this class"""
        raise TypeInferenceError(f"Object of type {self} does not have a constructor")

    def constr(self) -> plt.AST:
        """The constructor for this class"""
        raise NotImplementedError(f"Constructor of {self} not implemented")

    def attribute_type(self, attr) -> "Type":
        """The types of the named attributes of this class"""
        raise TypeInferenceError(
            f"Object of type {self} does not have attribute {attr}"
        )

    def attribute(self, attr) -> plt.AST:
        """The attributes of this class. Needs to be a lambda that expects as first argument the object itself"""
        raise NotImplementedError(f"Attribute {attr} not implemented for type {self}")


@dataclass(frozen=True, unsafe_hash=True)
class Record:
    name: str
    constructor: int
    fields: typing.Union[typing.List[typing.Tuple[str, Type]], FrozenList]


@dataclass(frozen=True, unsafe_hash=True)
class AnyType(Type):
    """The top element in the partial order on types"""

    def __ge__(self, other):
        return True


@dataclass(frozen=True, unsafe_hash=True)
class ClassType(Type):
    def __ge__(self, other):
        raise NotImplementedError("Comparison between raw classtypes impossible")


@dataclass(frozen=True, unsafe_hash=True)
class AtomicType(ClassType):
    def __ge__(self, other):
        # Can only substitute for its own type (also subtypes)
        return isinstance(other, self.__class__)


@dataclass(frozen=True, unsafe_hash=True)
class RecordType(ClassType):
    record: Record

    def constr_type(self) -> "InstanceType":
        return InstanceType(
            FunctionType([f[1] for f in self.record.fields], InstanceType(self))
        )

    def constr(self) -> plt.AST:
        # wrap all constructor values to PlutusData
        build_constr_params = plt.EmptyDataList()
        for n, t in reversed(self.record.fields):
            build_constr_params = plt.MkCons(
                transform_output_map(t)(plt.Var(n)), build_constr_params
            )
        # then build a constr type with this PlutusData
        return plt.Lambda(
            [n for n, _ in self.record.fields] + ["_"],
            plt.ConstrData(
                plt.Integer(self.record.constructor), plt.ListData(build_constr_params)
            ),
        )

    def attribute_type(self, attr: str) -> Type:
        """The types of the named attributes of this class"""
        if attr == "CONSTR_ID":
            return IntegerInstanceType
        for n, t in self.record.fields:
            if n == attr:
                return t
        raise TypeInferenceError(f"Type {self} does not have attribute {attr}")

    def attribute(self, attr: str) -> plt.AST:
        """The attributes of this class. Need to be a lambda that expects as first argument the object itself"""
        if attr == "CONSTR_ID":
            # access to constructor
            return plt.Lambda(
                ["self"],
                plt.Constructor(plt.Var("self")),
            )
        attr_typ = self.attribute_type(attr)
        pos = next(i for i, (n, _) in enumerate(self.record.fields) if n == attr)
        # access to normal fields
        return plt.Lambda(
            ["self"],
            transform_ext_params_map(attr_typ)(
                plt.NthField(
                    plt.Var("self"),
                    plt.Integer(pos),
                ),
            ),
        )

    def __ge__(self, other):
        # Can only substitute for its own type, records need to be equal
        # if someone wants to be funny, they can implement <= to be true if all fields match up to some point
        return isinstance(other, self.__class__) and other.record == self.record


@dataclass(frozen=True, unsafe_hash=True)
class UnionType(ClassType):
    typs: typing.List[ClassType]

    def attribute_type(self, attr) -> "Type":
        if attr == "CONSTR_ID":
            return IntegerInstanceType
        raise TypeInferenceError(
            f"Can not access attribute {attr} of Union type. Cast to desired type with an 'if isinstance(_, _):' branch."
        )

    def attribute(self, attr: str) -> plt.AST:
        if attr == "CONSTR_ID":
            # access to constructor
            return plt.Lambda(
                ["self"],
                plt.Constructor(plt.Var("self")),
            )
        raise NotImplementedError(
            f"Can not access attribute {attr} of Union type. Cast to desired type with an 'if isinstance(_, _):' branch."
        )

    def __ge__(self, other):
        if isinstance(other, UnionType):
            return all(any(t >= ot for ot in other.typs) for t in self.typs)
        return any(t >= other for t in self.typs)


@dataclass(frozen=True, unsafe_hash=True)
class TupleType(ClassType):
    typs: typing.List[Type]

    def __ge__(self, other):
        return isinstance(other, TupleType) and all(
            t >= ot for t, ot in zip(self.typs, other.typs)
        )


@dataclass(frozen=True, unsafe_hash=True)
class ListType(ClassType):
    typ: Type

    def __ge__(self, other):
        return isinstance(other, ListType) and self.typ >= other.typ


@dataclass(frozen=True, unsafe_hash=True)
class DictType(ClassType):
    key_typ: Type
    value_typ: Type

    def __ge__(self, other):
        return (
            isinstance(other, DictType)
            and self.key_typ >= other.key_typ
            and self.value_typ >= other.value_typ
        )


@dataclass(frozen=True, unsafe_hash=True)
class FunctionType(ClassType):
    argtyps: typing.List[Type]
    rettyp: Type

    def __ge__(self, other):
        return (
            isinstance(other, FunctionType)
            and all(a >= oa for a, oa in zip(self.argtyps, other.argtyps))
            and other.rettyp >= self.rettyp
        )


@dataclass(frozen=True, unsafe_hash=True)
class InstanceType(Type):
    typ: ClassType

    def constr_type(self) -> FunctionType:
        raise TypeInferenceError(f"Can not construct an instance {self}")

    def constr(self) -> plt.AST:
        raise NotImplementedError(f"Can not construct an instance {self}")

    def attribute_type(self, attr) -> Type:
        return self.typ.attribute_type(attr)

    def attribute(self, attr) -> plt.AST:
        return self.typ.attribute(attr)

    def __ge__(self, other):
        return isinstance(other, InstanceType) and self.typ >= other.typ


@dataclass(frozen=True, unsafe_hash=True)
class IntegerType(AtomicType):
    pass


@dataclass(frozen=True, unsafe_hash=True)
class StringType(AtomicType):
    pass


@dataclass(frozen=True, unsafe_hash=True)
class ByteStringType(AtomicType):
    def constr_type(self) -> InstanceType:
        return InstanceType(
            FunctionType(
                [InstanceType(ListType(IntegerInstanceType))], InstanceType(self)
            )
        )


@dataclass(frozen=True, unsafe_hash=True)
class BoolType(AtomicType):
    pass


@dataclass(frozen=True, unsafe_hash=True)
class UnitType(AtomicType):
    pass


IntegerInstanceType = InstanceType(IntegerType())
StringInstanceType = InstanceType(StringType())
ByteStringInstanceType = InstanceType(ByteStringType())
BoolInstanceType = InstanceType(BoolType())
UnitInstanceType = InstanceType(UnitType())

ATOMIC_TYPES = {
    int.__name__: IntegerType(),
    str.__name__: StringType(),
    bytes.__name__: ByteStringType(),
    "Unit": UnitType(),
    bool.__name__: BoolType(),
}


NoneRecord = Record("None", 0, FrozenFrozenList([]))
NoneType = RecordType(NoneRecord)
NoneInstanceType = InstanceType(NoneType)


class InaccessibleType(ClassType):
    """A type that blocks overwriting of a function"""

    pass


class PolymorphicFunction:
    def type_from_args(self, args: typing.List[Type]) -> FunctionType:
        raise NotImplementedError()

    def impl_from_args(self, args: typing.List[Type]) -> plt.AST:
        raise NotImplementedError()


@dataclass(frozen=True, unsafe_hash=True)
class PolymorphicFunctionType(ClassType):
    """A special type of builtin that may act differently on different parameters"""

    polymorphic_function: PolymorphicFunction


@dataclass(frozen=True, unsafe_hash=True)
class PolymorphicFunctionInstanceType(InstanceType):
    typ: FunctionType
    polymorphic_function: PolymorphicFunction


class TypedAST(AST):
    typ: Type


class typedexpr(TypedAST, expr):
    pass


class typedstmt(TypedAST, stmt):
    # Statements always have type None
    typ = NoneType


class typedarg(TypedAST, arg):
    pass


class typedarguments(TypedAST, arguments):
    args: typing.List[typedarg]
    vararg: typing.Union[typedarg, None]
    kwonlyargs: typing.List[typedarg]
    kw_defaults: typing.List[typing.Union[typedexpr, None]]
    kwarg: typing.Union[typedarg, None]
    defaults: typing.List[typedexpr]


class TypedModule(typedstmt, Module):
    body: typing.List[typedstmt]


class TypedFunctionDef(typedstmt, FunctionDef):
    body: typing.List[typedstmt]
    args: arguments


class TypedIf(typedstmt, If):
    test: typedexpr
    body: typing.List[typedstmt]
    orelse: typing.List[typedstmt]


class TypedReturn(typedstmt, Return):
    value: typedexpr


class TypedExpression(typedexpr, Expression):
    body: typedexpr


class TypedCall(typedexpr, Call):
    func: typedexpr
    args: typing.List[typedexpr]


class TypedExpr(typedstmt, Expr):
    value: typedexpr


class TypedAssign(typedstmt, Assign):
    targets: typing.List[typedexpr]
    value: typedexpr


class TypedWhile(typedstmt, While):
    test: typedexpr
    body: typing.List[typedstmt]
    orelse: typing.List[typedstmt]


class TypedFor(typedstmt, For):
    target: typedexpr
    iter: typedexpr
    body: typing.List[typedstmt]
    orelse: typing.List[typedstmt]


class TypedPass(typedstmt, Pass):
    pass


class TypedName(typedexpr, Name):
    pass


class TypedConstant(TypedAST, Constant):
    pass


class TypedTuple(typedexpr, Tuple):
    typ: typing.List[TypedAST]


class TypedList(typedexpr, List):
    typ: typing.List[TypedAST]


class TypedCompare(typedexpr, Compare):
    left: typedexpr
    ops: typing.List[cmpop]
    comparators: typing.List[typedexpr]


class TypedBinOp(typedexpr, BinOp):
    left: typedexpr
    right: typedexpr


class TypedUnaryOp(typedexpr, UnaryOp):
    operand: typedexpr


class TypedSubscript(typedexpr, Subscript):
    value: typedexpr


class TypedAttribute(typedexpr, Attribute):
    value: typedexpr
    pos: int


class TypedAssert(typedstmt, Assert):
    test: typedexpr
    msg: typedexpr


class TypeInferenceError(AssertionError):
    pass


EmptyListMap = {
    IntegerInstanceType: plt.EmptyIntegerList(),
    ByteStringInstanceType: plt.EmptyByteStringList(),
    StringInstanceType: plt.EmptyTextList(),
    UnitInstanceType: plt.EmptyUnitList(),
    BoolInstanceType: plt.EmptyBoolList(),
}


def empty_list(p: Type):
    if p in EmptyListMap:
        return EmptyListMap[p]
    assert isinstance(p, InstanceType), "Can only create lists of instances"
    if isinstance(p.typ, ListType):
        el = empty_list(p.typ.typ)
        return plt.EmptyListList(uplc.BuiltinList([], el.sample_value))
    if isinstance(p.typ, DictType):
        el_key = empty_list(p.typ.key_typ)
        el_value = empty_list(p.typ.value_typ)
        return plt.EmptyListList(
            uplc.BuiltinList(
                [], uplc.BuiltinPair(el_key.sample_value, el_value.sample_value)
            )
        )
    if isinstance(p.typ, RecordType):
        return plt.EmptyDataList()
    raise NotImplementedError(f"Empty lists of type {p} can't be constructed yet")


TransformExtParamsMap = {
    IntegerInstanceType: lambda x: plt.UnIData(x),
    ByteStringInstanceType: lambda x: plt.UnBData(x),
    StringInstanceType: lambda x: plt.DecodeUtf8(plt.UnBData(x)),
    UnitInstanceType: lambda x: plt.Lambda(["_"], plt.Unit()),
    BoolInstanceType: lambda x: plt.NotEqualsInteger(x, plt.Integer(0)),
}


def transform_ext_params_map(p: Type):
    assert isinstance(
        p, InstanceType
    ), "Can only transform instances, not classes as input"
    if p in TransformExtParamsMap:
        return TransformExtParamsMap[p]
    if isinstance(p.typ, ListType):
        list_int_typ = p.typ.typ
        return lambda x: plt.MapList(
            plt.UnListData(x),
            plt.Lambda(["x"], transform_ext_params_map(list_int_typ)(plt.Var("x"))),
            empty_list(p.typ.typ),
        )
    if isinstance(p.typ, DictType):
        # TODO also remap in the style the list is mapped (but on pairs)
        raise NotImplementedError(
            "Dictionaries can currently not be parsed from PlutusData"
        )
    return lambda x: x


TransformOutputMap = {
    StringInstanceType: lambda x: plt.BData(plt.EncodeUtf8(x)),
    IntegerInstanceType: lambda x: plt.IData(x),
    ByteStringInstanceType: lambda x: plt.BData(x),
    UnitInstanceType: lambda x: plt.Lambda(["_"], plt.Unit()),
    BoolInstanceType: lambda x: plt.IData(
        plt.IfThenElse(x, plt.Integer(1), plt.Integer(0))
    ),
}


def transform_output_map(p: Type):
    assert isinstance(
        p, InstanceType
    ), "Can only transform instances, not classes as input"
    if p in TransformOutputMap:
        return TransformOutputMap[p]
    if isinstance(p.typ, ListType):
        list_int_typ = p.typ.typ
        return lambda x: plt.ListData(
            plt.MapList(
                x,
                plt.Lambda(["x"], transform_output_map(list_int_typ)(plt.Var("x"))),
            ),
        )
    if isinstance(p.typ, DictType):
        # TODO also remap in the style the list is mapped as input
        raise NotImplementedError(
            "Dictionaries can currently not be mapped to PlutusData"
        )
    return lambda x: x
