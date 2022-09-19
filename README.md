# Representing Harmony

Sketches for a flexible extendible harmony representation

```terminal
> pip install pre-commit
> pre-commit install
```

## Motivation

Traditional methods and syntaxes for harmonic analysis are inadequate, especially in complex cases such as “extended tonal” and “atonal” where Stufen/Functions fall short.

### Issues to address 1: Types of harmony

* Existing theoretical and computational provisions (syntaxes etc) for encoding analyses in Roman numeral or chord symbols.
* Existing theoretical, but not really computational provisions for analysis by pitch class sets (pcset).

**TODO**: a wider vocabulary for connecting all of the above (see Hentschel et al. 2021).

### Issues to address 2: Contiguous, Serial, Simultaneous, Poly-, Totality of Registral Space

The typical analysis framework involves two layers (chord and keys) which are

* entirely separate and
* internally contiguous: the end of one chord is the start of the next.

This is perhaps most clearly inadequate in pcset analysis where it is common for set classes to overlap and / or only apply to part of the surface.

**TODO**:

* minimal: specify end points
* better: specify exactly which notes are considered (wider that those in the harmony)
* Even incomplete / work in progress (sketch analysis of a section)

### Issues to address 3: Confidence, reappraisal, multiple roles

Various cases:

* Multiple options:
  * Two viable analyses, hard to choose between.
  * One preferred, others possible (ranking / probability?).
  * Etc. (any number of readings)
* Initially one reading, then reappraised: a change of mind, not a chord.
* One chord functioning simultaneously in two ways
  * End of one form function unit and start of next.
  * Key pivot common; chord pivot not.

**TODO**:

* minimal:
·   the representation should be minimal since implementation frameworks (presumably Python) allow extensions and the addition of properties
* better: confidence on every attribute, including roots etc.

### Issues to address 4: Variants and connections

Grey area between:

* Momentary, disconnected variant reading
* Completely separate analysis

**TODO**: ways of connecting readings and variants as related or not.

* Branches? Named variants (`moreTonicizations`)?

Likewise processes and transformations. Sequences

**TODO**: Define N harmonies per block and relation between


## Proposal

_Updated after initial code sketches_

### Objects

#### Context

* Representation of a segment of music, the harmony of which is to be encoded.
  * e.g. a score, note matrix, wave form, spectrogram, vector graphic, etc.
* Requires some notion and encoding of musical time
  * e.g. absolute time (seconds), musical time (measure & beat), symbolic or spacial time (offset from beginning), etc.
* Should be, in the widest sense, a set of musical elements considered as harmonically pertinent
  * Each element's temporal dimensions need to be encoded.
  * Elements need to be addressable, at least through their temporal dimensions.
  * Elements of the same context are necessarily related to each other
    * at least implicitly through their temporal dimensions
    * through other implicit relations, e.g. pitch classes
    * or through explicitly encoded relations (e.g. color codes)
* Can be composed of other contexts
  * Since the elements are addressable and defined over time, new contexts can be created by applying a filter or selector.
    * such as a time span
    * or by selecting/excluding elements with certain features such as pitch classes
    * or by selecting a set of elements using their addressability

#### Label

* Associates a musical context with one or several Harmony objects
* Therefore, a label needs to be able
  * to address an existing Context (or parts of it) or create a new one
    * for example, a typical chord label refers to a score segment, a context within a larger context,
    * it might then assign functions to certain pitch classes within this context, such as chordal root;
    * selected pitch classes can, in principle, form or be viewed as new contexts
  * to refer to a Harmony object
* the association between labels and Harmony objects often suffers from uncertainty
  * ideally it is accomplished and/or verified by the labels' creator (annotator), or
  * it is achieved through a formalism that unequivocally maps labels to harmonic objects

#### Harmony

* Represents a concept (type)
* Can have concrete instances on several levels of abstraction
  * example for the most abstract: 'a triad'
  * example for less abstract: 'the diminished chord sitting on scale degree vii/V'
  * example for the most concrete: 'the E diminished triad instantiated @ segment X of piece Y'
* can be made up of several Harmony objects
  * e.g. one where a pitch is held over several bars as a pedal, plus a sequence of Harmony Objects representing chords
    (where some of the chords' roots coincide with the pedal)
  * or a harmonic sequence object with some contrapuntal/transformative logic (which, again, has multiple layers of abstraction down
    the level of the musical representation)
* The most concrete instance of a harmonic object is the one associated (e.g. through a label) with a concrete musical context
  * Such a concrete instance encodes concrete propositional statements concerning the associated context and/or elements within it
  * For example,
    * when the Harmony object `root=E` is associated with a chromagram segment, its concrete instance
      is this segment's chroma band belonging to the pitch class E.
    * when the Harmony object `root=C, chord_type=major` is associated with a score segment, all pitches with spelled pitch C
      (or, by conversion, enharmonic pitch 0) will be instances of this object's root, all E's its thirds, all G's its fifths.
      Depending on the underlying theoretical assumptions, all C's, or only those of a particular register or layer, or no notes
      at all will additionally be considered as bass note.
  * In that sense, the concrete instantiation of a Harmony object corresponds to the attribution of meaning to one, several
    or all elements contained in a musical context

### Considerations

_Written-out thoughts to collect and discuss arguments for future design decisions._

* In order to stick to one basic principle of associating Harmonic objects acting at various levels with contexts, we
  could try to find a recursive structure for organizing the various propositions that a Harmony object encodes and a
  recursive logic for resolving it against a given context. For example:
  * The label `ii6`, associated to a score segment, resolves to `root=SD(2), (third, bass)=SD(4), fifths=SD(6)` (SD standing
    for scale degree), i.e. an abstract triad that cannot immediately be instantiated within a musical context.
    The exact chord type is undefined until it is resolved against a Harmony
    object of type `Scale`, selecting its scale degrees and, if they are defined in terms of pitch classes, can then be
    applied as a pitch class filter to a score. Following this logic, Harmonic objects resulting from Roman numerals or
    other form of relatively defined labels require contextualization through a scale before they can be instantiated on
    the most concrete level.
  * The chord symbol `A7` may be resolved against
    * a score segment right away, explicitly assigning the meanings
      `(root, third, fifths, seventh)` to the pitch classes `(A, C#, E, G)`, and, optionally, all other notes' intervallic distances
      to the root A. From here, an algorithm might further qualify the 'out-of-chord' tones in order to produce a more elaborate
      chord label based on a different theory, e.g. a `A7,#9,13`.
    * a Harmony object representing the A minor scale in order to produce a more abstract `I7`, which can be further
      processed to yield `V7/iv`, depending on the theory at hand.
  * Based on these examples, it might make sense to draw a terminological line between the alleged manifestation of a
    Harmony in a particular musical context, and the more abstract, potentially time-less, versions that can only be
    represented in virtual musical spaces and would require an actual musical context to view them (consider, for example,
    music21 using default durations and registers in order to represent a virtual chord such as `V7 in D minor`).
    * In particular, the word 'to instantiate' needs to be carefully defined to avoid confusion between instantiation
      in the OOP sense and concretely instantiating a Harmony within a musical context.
    * Suggestion:
      * "to instantiate" for creating any Harmony object (both abstract and concrete), i.e. in the OOP sense
      * "to concretize" for bringing a Harmony object to a more concrete level (e.g. from 'V7' to 'A7')
      * "to abstract (away)" or "translate" for the opposite direction (e.g. from 'A7' to 'V7')
      * "to contextualize" for the most concrete level, a harmony's actual manifestation in a musical context
* data structures should be conceived in a way that makes very common tasks computationally cheap
  * for example, looking up interval combinations within a Harmony object to infer chord type
