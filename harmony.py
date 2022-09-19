"""Module for harmonic objects of all kinds and all levels of abstraction."""
from abc import ABC, abstractmethod
from typing import Collection, Tuple

from abstract import Point
from pitch import IntervalClass, PitchClass


class Harmony(ABC):
    """Superclass for harmonic objects of all kinds and all levels of abstraction."""

    pass


class PitchClassSelector(Harmony):
    """Superclass for all Harmony objects that act as a pitch class filter when contextualized,
    such as chords."""

    intervals: Collection[IntervalClass]
    """Collection of intervals that define a collection of pitch classes when added to a reference, the root."""

    def __init__(self, root: PitchClass = None):
        """

        Args:
            root: Root against which the _.intervals can be concretized, e.g., turned into pitch classes.
        """
        self.root = root

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, root: Point):
        self._root = root
        self._concretize()

    @abstractmethod
    def _concretize(self) -> None:
        """The method that turns self.intervals into some other collection based on self.root."""
        pass


class Chord(PitchClassSelector):
    """Superclass for all PitchClassSelectors that assign meaning within a chord to one or several pitch classes."""

    intervals: Tuple[IntervalClass] = ()

    def __init__(self, root: PitchClass = None):
        self.chord_tones = ()
        super().__init__(root)

    def _concretize(self) -> None:
        if self.root is None:
            # scale degrees expressed as intervals
            self.chord_tones = tuple(self.intervals)
        else:
            # scale degrees expressed as pitch classes because self.root is a pitch class
            self.chord_tones = tuple(
                self.root + interval for interval in self.intervals
            )

    def __str__(self):
        return f"Chord{self.chord_tones}"


class Scale(PitchClassSelector):
    """Superclass for all PitchClassSelectors that assign meaning within a scale to one or several pitch classes."""

    intervals: Tuple[IntervalClass] = ()

    def __init__(self, root: PitchClass = None):
        self.scale_degrees = ()
        super().__init__(root)

    def _concretize(self) -> None:
        if self.root is None:
            # scale degrees expressed as intervals
            self.scale_degrees = tuple(self.intervals)
        else:
            # scale degrees expressed as pitch classes because self.root is a pitch class
            self.scale_degrees = tuple(
                self.root + interval for interval in self.intervals
            )

    def __str__(self):
        return f"Scale{self.scale_degrees}"


class MajorChord(Chord):
    intervals = (0, 4, 7)


class MajorScale(Scale):
    intervals = (0, 2, 4, 5, 7, 9, 11)


class MajorPentatonicScale(Scale):
    intervals = (0, 2, 4, 7, 9)


if __name__ == "__main__":
    major_chord = MajorChord()
    print(
        f"Abstract major chord with scale degrees expressed as enharmonic intervals: {major_chord.__dict__}"
    )
    major_chord.root = 55
    print(
        f"Concrete major chord after setting root to {major_chord.root}: {major_chord.__dict__}"
    )
    print(f"Major chord initialized with root D4: {MajorChord(62)}")
    major_scale = MajorScale()
    print(
        f"Abstract major scale with scale degrees expressed as enharmonic intervals: {major_scale.__dict__}"
    )
    major_scale.root = 60
    print(
        f"Concrete major scale after setting root to {major_scale.root}: {major_scale.__dict__}"
    )
    print(f"Major pentatonic scale with root F#4: {MajorPentatonicScale(66)}")
