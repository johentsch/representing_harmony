# Representing Harmony

Sketches for a flexible extendible harmony representation

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

