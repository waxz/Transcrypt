from .. import util
from .visitors import Visitable, VisitableType

class TypeEngine(Visitable): ...
class VisitableCheckKWArg(util.EnsureKWArgType, VisitableType): ...
# TODO: class UserDefinedType(util.with_metaclass(VisitableCheckKWArg, TypeEngine)):
class UserDefinedType(VisitableCheckKWArg, TypeEngine): ...
class TypeDecorator(TypeEngine): ...
class Variant(TypeDecorator): ...