"""Quiz factory."""

from dataclasses import dataclass
from itertools import zip_longest

from toisto.metadata import Language

from .quiz import Quiz, Quizzes, QuizType, GRAMMATICAL_QUIZ_TYPES
from ..language import Concept


@dataclass
class QuizFactory:
    """Create quizzes for concepts."""

    language: Language
    source_language: Language

    def create_quizzes(self, *concepts: Concept) -> Quizzes:
        """Create quizzes for the concepts."""
        quizzes = Quizzes()
        for concept in concepts:
            quizzes |= self.create_concept_quizzes(concept, Quizzes())
        return quizzes

    def create_concept_quizzes(self, concept: Concept, previous_quizzes: Quizzes) -> Quizzes:
        """Create the quizzes for a concept."""
        if concept.constituent_concepts:
            return self.create_composite_concept_quizzes(concept, previous_quizzes)
        return self.create_leaf_concept_quizzes(concept, previous_quizzes)

    def create_composite_concept_quizzes(self, concept: Concept, previous_quizzes: Quizzes) -> Quizzes:
        """Create the quizzes for a composite concept."""
        quizzes = Quizzes()
        for constituent_concept in concept.constituent_concepts:
            quizzes |= self.create_concept_quizzes(constituent_concept, quizzes.copy() | previous_quizzes)
        quizzes |= self.create_grammatical_quizzes(concept, quizzes.copy() | previous_quizzes)
        return quizzes

    def create_leaf_concept_quizzes(self, concept: Concept, previous_quizzes: Quizzes) -> Quizzes:
        """Create the quizzes for a leaf concept."""
        translation_quizzes = self.create_translation_quizzes(concept, previous_quizzes)
        listening_quizzes = self.create_listening_quizzes(concept, translation_quizzes.copy() | previous_quizzes)
        return translation_quizzes | listening_quizzes

    def create_translation_quizzes(self, concept: Concept, previous_quizzes: Quizzes) -> Quizzes:
        """Create translation quizzes for the concept."""
        language, source_language = self.language, self.source_language
        labels, source_labels = concept.labels(language), concept.labels(source_language)
        if not labels or not source_labels:
            return Quizzes()
        concept_id = concept.concept_id
        blocked_by = tuple(previous_quizzes)
        back = Quizzes(
            Quiz(concept_id, language, source_language, label, source_labels, uses=concept.uses, blocked_by=blocked_by)
            for label in labels
        )
        forth = Quizzes(
            Quiz(concept_id, source_language, language, label, labels, uses=concept.uses, blocked_by=blocked_by)
            for label in source_labels
        )
        return back | forth

    def create_listening_quizzes(self, concept: Concept, previous_quizzes: Quizzes) -> Quizzes:
        """Create listening quizzes for the concept."""
        language, source_language = self.language, self.source_language
        labels = concept.labels(language)
        concept_id = concept.concept_id
        blocked_by = tuple(previous_quizzes)
        meanings = concept.meanings(source_language)
        return Quizzes(
            Quiz(concept_id, language, language, label, (label,), ("listen",), concept.uses, blocked_by, meanings)
            for label in labels
        )

    def create_grammatical_quizzes(self, concept: Concept, previous_quizzes: Quizzes) -> Quizzes:
        """Create grammatical quizzes for the concept."""
        language, source_language = self.language, self.source_language
        concept_id = concept.concept_id
        blocked_by = tuple(previous_quizzes)
        uses = concept.uses
        quizzes = Quizzes()
        for concept1, concept2 in concept.paired_leaf_concepts():
            labels1, labels2 = concept1.labels(language), concept2.labels(language)
            meanings = concept1.meanings(source_language) + concept2.meanings(source_language)
            quiz_types = grammatical_quiz_types(concept1, concept2)
            quizzes |= Quizzes(
                Quiz(concept_id, language, language, label1, (label2,), quiz_types, uses, blocked_by, meanings)
                for label1, label2 in zip(labels1, labels2)
                if label1 != label2
            )
        return quizzes


def grammatical_quiz_types(concept1: Concept, concept2: Concept) -> tuple[QuizType, ...]:
    """Return the quiz types to change the grammatical category of concept1 into that of concept2."""
    quiz_types = []
    for category1, category2 in zip_longest(concept1.grammatical_categories(), concept2.grammatical_categories()):
        if category1 != category2 and category2 is not None:
            quiz_types.append(GRAMMATICAL_QUIZ_TYPES[category2])
    return tuple(quiz_types)
