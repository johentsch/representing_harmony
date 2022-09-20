import re
from typing import Literal, Sequence, Tuple, Union, overload


@overload
def split_note_name(note_name: str, count: Literal[False]) -> Tuple[str, str]:
    ...


@overload
def split_note_name(note_name: str, count: Literal[True]) -> Tuple[int, str]:
    ...


def split_note_name(
    note_name: str, count: bool = False
) -> Union[Tuple[int, str], Tuple[str, str]]:
    """Splits a note name such as 'Ab' into accidentals and name.

    Args:
        note_name: Note name.
        count: Pass True to get the accidentals as integer rather than as string.
    """
    assert isinstance(note_name, str), f"'{note_name}' is not an accepted note name."
    m = re.match(r"^([A-G]|[a-g])(#*|b*)$", note_name)
    assert m is not None, f"{note_name} is not a valid note name."
    note_name, accidentals = m.group(1), m.group(2)
    if count:
        accidentals = accidentals.count("#") - accidentals.count("b")
    return accidentals, note_name


def note_name2fifths(note_name: str) -> int:
    """Turn a note name such as `Ab` into a tonal pitch class, such that -1=F, 0=C, 1=G etc.
        Uses: split_note_name()

    Args:
        note_name: Note name.
    """
    name_tpcs = {"C": 0, "D": 2, "E": 4, "F": -1, "G": 1, "A": 3, "B": 5}
    accidentals, name = split_note_name(note_name, count=True)
    step_tpc = name_tpcs[name.upper()]
    return step_tpc + 7 * accidentals


def interval_name2fifths(interval_name):
    m = re.match(r"^(P|M|m|a+|d+)(\d+)$", interval_name)
    assert m is not None, f"{interval_name} is not a valid interval name."
    quality, int_num = m.group(1), int(m.group(2))
    assert int_num > 0, f"'{interval_name}': the interval needs to be non-zero."
    fifths_base = (
        2 * int_num - 1
    ) % 7 - 1  # base interval class, i.e. P or M version, as fifths
    if quality == "P":
        assert fifths_base in (
            -1,
            0,
            1,
        ), f"'{interval_name}': Only 4ths, 5ths and unisons can be P"
    if quality == "M":
        assert fifths_base in (
            2,
            3,
            4,
            5,
        ), f"'{interval_name}': Only 2nds, 3rds, 6ths, and 7ths can be M"
    elif quality == "m":
        assert fifths_base in (
            2,
            3,
            4,
            5,
        ), f"'{interval_name}': Only 2nds, 3rds, 6ths, and 7ths can be m"
        fifths_base -= 7
    elif "a" in quality:
        fifths_base += 7 * len(quality)
    elif "d" in quality:
        if fifths_base in (-1, 0, 1):
            fifths_base -= 7 * (len(quality))
        else:
            fifths_base -= 7 * (len(quality) + 1)
    return fifths_base


def _fifths2str(fifths: int, steps: Sequence[str], inverted: bool = False) -> str:
    """Boilerplate used by fifths2-functions.

    Args:
        fifths: Fifth to be converted to a string.
        steps: List of seven strings.
        inverted: By default, the accidentals are appended. Pass True to prepend them instead.
    """
    fifths += 1
    acc = abs(fifths // 7) * "b" if fifths < 0 else fifths // 7 * "#"
    if inverted:
        return steps[fifths % 7] + acc
    return acc + steps[fifths % 7]


def fifths2note_name(fifths: int) -> str:
    """Return note name of a stack of fifths such that
       0 = C, -1 = F, -2 = Bb, 1 = G etc.
       Uses: _fifths2str()

    Args:
        fifths: Fifths to be turned into a note name.
    """
    note_names = ["F", "C", "G", "D", "A", "E", "B"]
    name = _fifths2str(fifths, note_names, inverted=True)
    return name


def fifths2interval_name(fifths: int) -> str:
    """Return interval name of a stack of fifths such that
    0 = 'P1', -1 = 'P4', -2 = 'm7', 4 = 'M3' etc.
    """
    fifths_plus_one = fifths + 1  # making 0 = fourth, 1 = unison, 2 = fifth etc.
    int_num = ["4", "1", "5", "2", "6", "3", "7"][fifths_plus_one % 7]
    if -5 <= fifths <= 5:
        quality = ["m", "m", "m", "m", "P", "P", "P", "M", "M", "M", "M"][fifths + 5]
    elif fifths > 5:
        quality = "a" * (fifths_plus_one // 7)
    else:
        quality = "d" * ((-fifths + 1) // 7)
    return quality + int_num
