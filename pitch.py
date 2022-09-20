from abc import abstractmethod
from typing import Union

from abstract import FifthsScalar, IntType, Point, SemitonesScalar, Vector
from pitch_helpers import (
    fifths2interval_name,
    fifths2note_name,
    interval_name2fifths,
    note_name2fifths,
)


class PitchClass(Point):
    @property
    @abstractmethod
    def semitones(self):
        pass


class Pitch(Point):
    @property
    @abstractmethod
    def semitones(self):
        pass


class IntervalClass(Vector):
    @property
    @abstractmethod
    def semitones(self):
        pass


class Interval(Vector):
    @property
    @abstractmethod
    def semitones(self):
        pass


class EnharmonicPitchClass(SemitonesScalar, PitchClass):
    """An EPC value is always within [0, 11] and can be interpreted as an enumeration of piano keys from C up to B
    within the same octave. EnharmonicPitchClassCs are equivalent to the PCs of pitch-class set theory."""

    def __str__(self):
        return f"EPC({self.semitones})"

    def __repr__(self):
        return f"EPC({self.semitones})"

    def __add__(self, other: Union[int, IntType]) -> Union[int, IntType]:
        if isinstance(other, IntervalClass):
            return EnharmonicPitchClass(self.semitones + other.semitones)
        return super().__add__(other)

    def __sub__(self, other: Union[int, IntType]) -> Union[int, IntType]:
        if isinstance(other, IntervalClass):
            return EnharmonicPitchClass(self.semitones - other.semitones)
        return super().__sub__(other)


class EnharmonicIntervalClass(SemitonesScalar, IntervalClass):
    """An EIV value is always within [0, 11] and can be interpreted as the distance between two piano keys when
    projected into the same octave."""

    def __str__(self):
        return f"EIC({self.semitones})"

    def __repr__(self):
        return f"EIC({self.semitones})"

    def __neg__(self):
        return EnharmonicIntervalClass(-self.semitones)

    def __add__(self, other: Union[int, IntType]) -> Union[int, IntType]:
        if isinstance(other, PitchClass):
            return EnharmonicPitchClass(self.semitones + other.semitones)
        if isinstance(other, IntervalClass):
            return EnharmonicIntervalClass(self.semitones + other.semitones)
        return super().__add__(other)

    def __sub__(self, other: Union[int, IntType]) -> Union[int, IntType]:
        if isinstance(other, IntervalClass):
            return EnharmonicIntervalClass(self.semitones - other.semitones)
        return super().__sub__(other)


class SpecificPitchClass(FifthsScalar, PitchClass):
    @staticmethod
    def convert_init_value(value: Union[int, str]) -> int:
        # TODO: Merge into FifthsScalar.convert_init_value()
        if isinstance(value, str):
            converted = note_name2fifths(value)
        else:
            converted = int(value)
        return converted

    @classmethod
    def from_fifths(cls, fifths: int):
        instance = super().__new__(cls, fifths)
        return instance

    @property
    def name(self):
        return fifths2note_name(self.fifths)

    def __str__(self):
        return f"SPC('{self.name}')"

    def __repr__(self):
        return self.name

    def __add__(self, other: Union[int, IntType]) -> Union[int, IntType]:
        if isinstance(other, SpecificIntervalClass):
            return SpecificPitchClass(self.fifths + other.fifths)
        if isinstance(other, EnharmonicIntervalClass):
            return EnharmonicPitchClass(self.semitones + other.semitones)
        return super().__add__(other)

    def __sub__(self, other: Union[int, IntType]) -> Union[int, IntType]:
        if isinstance(other, SpecificIntervalClass):
            return SpecificPitchClass(self.fifths - other.fifths)
        if isinstance(other, EnharmonicIntervalClass):
            return EnharmonicPitchClass(self.semitones - other.semitones)
        return super().__sub__(other)


class SpecificIntervalClass(FifthsScalar, IntervalClass):
    @staticmethod
    def convert_init_value(value: Union[int, str]) -> int:
        # TODO: Merge into FifthsScalar.convert_init_value()
        if isinstance(value, str):
            converted = interval_name2fifths(value)
        else:
            converted = int(value)
        return converted

    @property
    def name(self):
        return fifths2interval_name(self.fifths)

    def __neg__(self):
        return SpecificIntervalClass(-self.fifths)

    def __str__(self):
        return f"SIC('{self.name}')"

    def __repr__(self):
        return self.name

    def __add__(self, other: Union[int, IntType]) -> Union[int, IntType]:
        if isinstance(other, SpecificPitchClass):
            return SpecificPitchClass(self.fifths + other.fifths)
        if isinstance(other, SpecificIntervalClass):
            return SpecificIntervalClass(self.fifths + other.fifths)
        if isinstance(other, EnharmonicPitchClass):
            return EnharmonicPitchClass(self.semitones + other.semitones)
        if isinstance(other, EnharmonicIntervalClass):
            return EnharmonicIntervalClass(self.semitones + other.semitones)
        return super().__add__(other)

    def __sub__(self, other: Union[int, IntType]) -> Union[int, IntType]:
        if isinstance(other, SpecificIntervalClass):
            return SpecificIntervalClass(self.fifths - other.fifths)
        if isinstance(other, EnharmonicIntervalClass):
            return EnharmonicIntervalClass(self.semitones - other.semitones)
        return super().__sub__(other)


EPC = EnharmonicPitchClass
EIC = EnharmonicIntervalClass
SPC = SpecificPitchClass
SIC = SpecificIntervalClass

if __name__ == "__main__":
    from itertools import product

    def test_operators(*instances):
        for i in instances:
            try:
                print(f"-{i} = {-i}")
            except Exception as e:
                print(f'-{i} failed with "{e}"')
        for a, b in product(instances, repeat=2):
            for func, operator in [
                ("__add__", "+"),
                ("__sub__", "-"),
                ("__mul__", "*"),
                ("__truediv__", "/"),
                ("__pow__", "**"),
                ("__lt__", "<"),
                ("__le__", "<="),
                ("__gt__", ">"),
                ("__ge__", ">="),
                ("__eq__", "=="),
            ]:
                operation = f"{a} {operator} {b}"
                try:
                    print(f"{operation} = {eval(operation)}")
                except Exception as e:
                    print(f'{operation} failed with "{e}"')

    epc0 = EnharmonicPitchClass("62")
    print(f"EnharmonicPitchClass('62') = {epc0}")
    eic0 = EnharmonicIntervalClass(-17)
    print(f"EnharmonicIntervalClass(-17) = {eic0}")
    spc0 = SpecificPitchClass(-6)
    print(f"EnharmonicPitchClass(-6) = {spc0}")
    sic0 = SpecificIntervalClass(6)
    print(f"EnharmonicIntervalClass(6) = {sic0}")
    test_operators(-3, 1.5, epc0, spc0, eic0, sic0)
