"""Concept classes."""

from __future__ import annotations

from dataclasses import dataclass, field
from itertools import permutations
from typing import cast, get_args, Iterable

from toisto.metadata import Language
from toisto.tools import zip_and_cycle

from ..model_types import ConceptId
from .grammar import GrammaticalCategory
from .label import Labels, Label


@dataclass
class Concept:
    """Class representing language concepts.

    A concept is either a composite or a leaf concept. Composite concepts have have two or more constituent concepts,
    representing different grammatical categories, for example singular and plural forms. Leaf concepts have labels
    in different languages.
    """

    concept_id: ConceptId
    uses: tuple[ConceptId, ...]
    constituent_concepts: tuple[Concept, ...] = ()
    _labels: dict[Language, Labels] = field(default_factory=dict)

    def leaf_concepts(self) -> Iterable[Concept]:
        """Return this concept's leaf concepts, or self if this concept is a leaf concept."""
        if self.constituent_concepts:
            for concept in self.constituent_concepts:
                yield from concept.leaf_concepts()
        else:
            yield self

    def paired_leaf_concepts(self) -> Iterable[tuple[Concept, Concept]]:
        """Pair the leaf concepts from the constituent concepts."""
        for concept_group in zip_and_cycle(*[list(concept.leaf_concepts()) for concept in self.constituent_concepts]):
            for permutation in permutations(concept_group, r=2):
                yield cast(tuple[Concept, Concept], permutation)

    def labels(self, language: Language) -> Labels:
        """Return the labels for the language."""
        return self._labels.get(language, Labels())

    def meanings(self, language: Language) -> Labels:
        """Return the meaning of the concept in the specified language."""
        meaning = Label(self._labels.get(language, [""])[0])
        return (meaning,) if meaning else ()

    def grammatical_categories(self) -> tuple[GrammaticalCategory, ...]:
        """Return the grammatical categories of this concept."""
        keys = self.concept_id.split("/")
        return tuple(cast(GrammaticalCategory, key) for key in keys if key in get_args(GrammaticalCategory))
