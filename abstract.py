from typing import Type, TypeVar, Union


class Point:
    pass


class Vector:
    pass


T = TypeVar("T", bound="IntType")


class IntType(int):
    """Abstract class for custom integer types. For the usual numerical operators, instances behave
    like an integer when the other value is also an integer. If the other value, however, is an
    IntType, an NotImplementedError is thrown unless the operation is defined for this IntType.
    The actual int value is stored in the field _value. The various subclasses provide different properties for
    accessing this field.
    """

    @staticmethod
    def convert_init_value(value: Union[int, str]) -> int:
        """Used by the constructor to convert the initial value into the integer that will be stored."""
        return int(value)

    def __new__(cls, value: Union[int, str]) -> Type[T]:
        """Can be created from an integer or any type that int() accepts."""
        converted_value = cls.convert_init_value(value)
        instance = int.__new__(cls, converted_value)
        instance._value = converted_value
        return instance

    @property
    def name(self) -> str:
        return str(self._value)

    def __str__(self) -> str:
        """String representation should work as a constructor."""
        return f"{type(self).__name__}({self.name})"

    def __repr__(self) -> str:
        """Representation should be short for slim display within containers."""
        return f"{type(self).__name__}({self.name})"

    def __neg__(self) -> Type[T]:
        raise NotImplementedError(f"Negation operation not defined: - {type(self)}")

    def __add__(self, other: Union[Type[T], int]) -> Type[T]:
        if isinstance(other, IntType):
            raise NotImplementedError(
                f"Operation not defined: {type(self)} + {type(other)}"
            )
        return self.__class__(self._value + other)

    def __sub__(self, other: Union[Type[T], int]) -> Type[T]:
        if isinstance(other, IntType):
            raise NotImplementedError(
                f"Operation not defined: {type(self)} - {type(other)}"
            )
        return self.__class__(self._value - other)

    def __mul__(self, other: Union[Type[T], int]) -> Type[T]:
        if isinstance(other, IntType):
            raise NotImplementedError(
                f"Operation not defined: {type(self)} * {type(other)}"
            )
        return self.__class__(self._value * other)

    def __floordiv__(self, other: Union[Type[T], int]) -> Type[T]:
        if isinstance(other, IntType):
            raise NotImplementedError(
                f"Operation not defined: {type(self)} // {type(other)}"
            )
        return self.__class__(self._value // other)

    def __truediv__(self, other: Union[Type[T], int]) -> Type[T]:
        if isinstance(other, IntType):
            raise NotImplementedError(
                f"Operation not defined: {type(self)} / {type(other)}"
            )
        return self.__class__(int(self._value / other))

    def __mod__(self, other: Union[Type[T], int]) -> Type[T]:
        if isinstance(other, IntType):
            raise NotImplementedError(
                f"Operation not defined: {type(self)} % {type(other)}"
            )
        return self.__class__(self._value % other)

    def __divmod__(self, other: Union[Type[T], int]) -> tuple[int, int]:
        if isinstance(other, IntType):
            raise NotImplementedError(
                f"Operation not defined: divmod({type(self)}, {type(other)})"
            )
        return int(self._value).__divmod__(other)

    def __radd__(self, other: Union[Type[T], int]) -> Type[T]:
        if isinstance(other, IntType):
            raise NotImplementedError(
                f"Operation not defined: {type(other)} + {type(self)}"
            )
        return self.__class__(other + self._value)

    def __rsub__(self, other: Union[Type[T], int]) -> Type[T]:
        if isinstance(other, IntType):
            raise NotImplementedError(
                f"Operation not defined: {type(other)} - {type(self)}"
            )
        return self.__class__(other - self._value)

    def __rmul__(self, other: Union[Type[T], int]) -> Type[T]:
        if isinstance(other, IntType):
            raise NotImplementedError(
                f"Operation not defined: {type(other)} * {type(self)}"
            )
        return self.__class__(other * self._value)

    def __rfloordiv__(self, other: Union[Type[T], int]) -> Type[T]:
        if isinstance(other, IntType):
            raise NotImplementedError(
                f"Operation not defined: {type(other)} // {type(self)}"
            )
        return self.__class__(other // self._value)

    def __rtruediv__(self, other: Union[Type[T], int]) -> Type[T]:
        if isinstance(other, IntType):
            raise NotImplementedError(
                f"Operation not defined: {type(other)} / {type(self)}"
            )
        return self.__class__(int(other / self._value))

    def __rmod__(self, other: Union[Type[T], int]) -> Type[T]:
        if isinstance(other, IntType):
            raise NotImplementedError(
                f"Operation not defined: {type(other)} % {type(self)}"
            )
        return self.__class__(other % self._value)

    def __rdivmod__(self, other: Union[Type[T], int]) -> tuple[int, int]:
        if isinstance(other, IntType):
            raise NotImplementedError(
                f"Operation not defined: divmod({type(other)}, {type(self)})"
            )
        return int(other).__divmod__(self._value)

    def __pow__(self, other: Union[Type[T], int]) -> Type[T]:
        if isinstance(other, IntType):
            raise NotImplementedError(
                f"Operation not defined: {type(self)} ** {type(other)}"
            )
        return self.__class__(self._value**other)

    def __rpow__(self, other: Union[Type[T], int]) -> Type[T]:
        if isinstance(other, IntType):
            raise NotImplementedError(
                f"Operation not defined: {type(other)} ** {type(self)}"
            )
        return self.__class__(other**self._value)

    def __and__(self, other: Union[Type[T], int]) -> Type[T]:
        if isinstance(other, IntType):
            raise NotImplementedError(
                f"Operation not defined: {type(self)} & {type(other)}"
            )
        return self.__class__(self._value & other)

    def __or__(self, other: Union[Type[T], int]) -> Type[T]:
        if isinstance(other, IntType):
            raise NotImplementedError(
                f"Operation not defined: {type(self)} | {type(other)}"
            )
        return self.__class__(self._value | other)

    def __xor__(self, other: Union[Type[T], int]) -> Type[T]:
        if isinstance(other, IntType):
            raise NotImplementedError(
                f"Operation not defined: {type(self)} ^ {type(other)}"
            )
        return self.__class__(self._value ^ other)

    def __lshift__(self, other: Union[Type[T], int]) -> Type[T]:
        if isinstance(other, IntType):
            raise NotImplementedError(
                f"Operation not defined: {type(self)} << {type(other)}"
            )
        return self.__class__(self._value << other)

    def __rshift__(self, other: Union[Type[T], int]) -> Type[T]:
        if isinstance(other, IntType):
            raise NotImplementedError(
                f"Operation not defined: {type(self)} >> {type(other)}"
            )
        return self.__class__(self._value >> other)

    def __rand__(self, other: Union[Type[T], int]) -> Type[T]:
        if isinstance(other, IntType):
            raise NotImplementedError(
                f"Operation not defined: {type(other)} & {type(self)}"
            )
        return self.__class__(other & self._value)

    def __ror__(self, other: Union[Type[T], int]) -> Type[T]:
        if isinstance(other, IntType):
            raise NotImplementedError(
                f"Operation not defined: {type(other)} | {type(self)}"
            )
        return self.__class__(other | self._value)

    def __rxor__(self, other: Union[Type[T], int]) -> Type[T]:
        if isinstance(other, IntType):
            raise NotImplementedError(
                f"Operation not defined: {type(other)} ^ {type(self)}"
            )
        return self.__class__(other ^ self._value)

    def __rlshift__(self, other: Union[Type[T], int]) -> Type[T]:
        if isinstance(other, IntType):
            raise NotImplementedError(
                f"Operation not defined: {type(other)} << {type(self)}"
            )
        return self.__class__(other << self._value)

    def __rrshift__(self, other: Union[Type[T], int]) -> Type[T]:
        if isinstance(other, IntType):
            raise NotImplementedError(
                f"Operation not defined: {type(other)} >> {type(self)}"
            )
        return self.__class__(other >> self._value)

    def __eq__(self, other) -> bool:
        if isinstance(other, IntType) and not (type(self) == type(other)):
            raise NotImplementedError(
                f"Comparison not defined: {type(self)} == {type(other)}"
            )
        return self._value == other

    def __lt__(self, other: Union[Type[T], int]) -> bool:
        if isinstance(other, IntType) and not (type(self) == type(other)):
            raise NotImplementedError(
                f"Comparison not defined: {type(self)} < {type(other)}"
            )
        return self._value < other

    def __le__(self, other: Union[Type[T], int]) -> bool:
        if isinstance(other, IntType) and not (type(self) == type(other)):
            raise NotImplementedError(
                f"Comparison not defined: {type(self)} <= {type(other)}"
            )
        return self._value <= other

    def __gt__(self, other: Union[Type[T], int]) -> bool:
        if isinstance(other, IntType) and not (type(self) == type(other)):
            raise NotImplementedError(
                f"Comparison not defined: {type(self)} > {type(other)}"
            )
        return self._value > other

    def __ge__(self, other: Union[Type[T], int]) -> bool:
        if isinstance(other, IntType) and not (type(self) == type(other)):
            raise NotImplementedError(
                f"Comparison not defined: {type(self)} >= {type(other)}"
            )
        return self._value >= other


class SemitonesScalar(IntType):
    """Integer type whose _value field represents a number of semitones,
    such as a MIDI number or chromatic pitch class."""

    @staticmethod
    def convert_init_value(value: Union[int, str, IntType]) -> int:
        # TODO: convert note name or interval strings to semitones
        if isinstance(value, FifthsScalar):
            converted = value.semitones
        else:
            converted = int(value)
        return converted % 12

    @property
    def semitones(self) -> int:
        """This scalar's value."""
        return self._value

    @property
    def fifths(self) -> None:
        """Semitones expressed as the number of fifths. Will require inference logic or additional information."""
        return

    @property
    def octave(self) -> None:
        """Octave information will depend on the subtype."""
        return

    def __neg__(self) -> int:
        return super().__neg__()


class FifthsScalar(IntType):
    """Integer type whose _value field represents a number of perfect fifth intervals,
    such as a spelled pitch class or a specific interval."""

    @staticmethod
    def convert_init_value(value: Union[int, str, IntType]) -> int:
        # TODO: convert note name or interval strings to fifths
        if isinstance(value, SemitonesScalar):
            converted = value.fifths
        else:
            converted = int(value)
        return converted

    @property
    def fifths(self) -> int:
        """This scalar's value."""
        return self._value

    @property
    def semitones(self) -> int:
        """The stack of fifths represented by this scalar, expressed in semitones."""
        return 7 * self._value % 12

    @property
    def octave(self) -> None:
        """Octave information will depend on the subtype."""
        return

    def __str__(self) -> str:
        """Constructors of subtypes will work with string representations."""
        return f"{type(self).__name__}('{self.name}')"

    def __repr__(self) -> str:
        return self.name

    def __neg__(self) -> int:
        return super().__neg__()


if __name__ == "__main__":
    a = SemitonesScalar(4)
    b = SemitonesScalar("5")
    c = FifthsScalar(6)
    d = FifthsScalar("7")
    # these operations will return integers
    print(f"{a} + 1 = {a + 1}")
    print(f"{b} * -1 = {b * -1}")
    print(f"{c} // 2 = {c // 2}")
    print(f"{d} ** 2 = {d ** 2}")
    # these operations will fail
    try:
        a + b
    except NotImplementedError as e:
        print(f'{a} + {b} failed with "{e}"')
    try:
        b * c
    except NotImplementedError as e:
        print(f'{b} * {c} failed with "{e}"')
    try:
        -a
    except NotImplementedError as e:
        print(f'-{a} failed with "{e}"')
