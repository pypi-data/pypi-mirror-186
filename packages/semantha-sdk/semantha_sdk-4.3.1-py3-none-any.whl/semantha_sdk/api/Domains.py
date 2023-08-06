from __future__ import annotations

from semantha_sdk.model.DomainConfiguration import DomainConfiguration
from semantha_sdk.model.DomainSettings import DomainSettings
from semantha_sdk.model.Domains import Domains as _DomainsDTO, Domain as _DomainDTO
from semantha_sdk.rest.RestClient import RestClient
from semantha_sdk.response.SemanthaPlatformResponse import SemanthaPlatformResponse
from semantha_sdk.api.Documents import Documents
from semantha_sdk.api.ReferenceDocuments import ReferenceDocuments
from semantha_sdk.api.References import References
from semantha_sdk.api.DocumentAnnotations import DocumentAnnotations
from semantha_sdk.api.DocumentComparisons import DocumentComparisons
from semantha_sdk.api import SemanthaAPIEndpoint


class Domain(SemanthaAPIEndpoint):
    """ Endpoint for a specific domain.

        References: documents, documentannotations, documentcomparisons, documentclasses,
            modelclasses, modelinstances, referencedocuments, references,
            settings, stopwords, similaritymatrix, tags and validation.
    """
    def __init__(self, session: RestClient, parent_endpoint: str, domain_name: str):
        super().__init__(session, parent_endpoint)
        self._domain_name = domain_name
        self.__documents = Documents(session, self._endpoint)
        self.__document_annotations = DocumentAnnotations(session, self._endpoint)
        self.__document_comparisons = DocumentComparisons(session, self._endpoint)
        self.__reference_documents = ReferenceDocuments(session, self._endpoint)
        self.__references = References(session, self._endpoint)

    @property
    def _endpoint(self):
        return self._parent_endpoint + f"/{self._domain_name}"

    @property
    def documents(self):
        return self.__documents

    @property
    def document_annotations(self):
        return self.__document_annotations

    @property
    def reference_documents(self) -> ReferenceDocuments:
        return self.__reference_documents

    @property
    def references(self) -> References:
        return self.__references

    def get_metadata(self) -> SemanthaPlatformResponse:
        return self._session.get(f"{self._endpoint}/metadata").execute()

    def get_rule(self) -> SemanthaPlatformResponse:
        return self._session.get(f"{self._endpoint}/rules").execute()

    def get_documentclasses(self) -> SemanthaPlatformResponse:
        return self._session.get(f"{self._endpoint}/documentclasses").execute()

    def get_subclasses(self, id: str) -> SemanthaPlatformResponse:
        return self._session.get(
            f"{self._endpoint}/documentclasses/{id.lower()}/documentclasses"
        ).execute()

    def get_class_with_subclasses(self, id: str) -> SemanthaPlatformResponse:
        return self._session.get(f"{self._endpoint}/documentclasses/{id.lower()}").execute()

    def get_class_documents(self, id: str) -> SemanthaPlatformResponse:
        return self._session.get(
            f"{self._endpoint}/documentclasses/{id.lower()}/referencedocuments"
        ).execute()

    def get_configuration(self) -> DomainConfiguration:
        """Get the domain configuration"""
        return self._session.get(f"{self._endpoint}").execute().to(DomainConfiguration)

    def get_model_classes(self) -> SemanthaPlatformResponse:
        return self._session.get(f"{self._endpoint}/modelclasses").execute()

    def get_settings(self) -> DomainSettings:
        """Get the domain settings"""
        return self._session.get(f"{self._endpoint}/settings").execute().to(DomainSettings)

    def patch_settings(
            self,
            similarity_model_id: str = None,
            keep_numbers: bool = None,
            min_tokens: int = None,
            similarity_measure: str = None,
            context_weight: float = None,
            enable_string_comparison: bool = None,
            default_document_type: bool = None,
            enable_paragraph_sorting: bool = None,
            enable_paragraph_end_detection: bool = None,
            enable_paragraph_merging_based_on_formatting: bool = None,
            enable_boost_word_filtering_for_input_documents: bool = None,
            tagging_similarity_mode: str = None,
            enable_updating_fingerprints_on_tag_updates: bool = None,
            similarity_matcher: str = None,
            similarity_max_deviation: int = None,
            similarity_threshold: float = None,
            enable_tagging: bool = None,
            tagging_threshold: float = None,
            tagging_strategy: str = None,
            extraction_threshold: float = None,
            extraction_strategy: str = None,
            resize_paragraphs_on_extraction: bool = None
    ) -> DomainSettings:
        """Patch one or more domain setting(s)"""
        #TODO: add Args description
        body = {}
        if similarity_model_id is not None:
            body["similarityModelId"] = similarity_model_id
        if keep_numbers is not None:
            body["keepNumbers"] = keep_numbers.__str__()
        if min_tokens is not None:
            body["minTokens"] = min_tokens.__str__()
        if similarity_measure is not None:
            body["similarityMeasure"] = similarity_measure
        if context_weight is not None:
            body["contextWeight"] = context_weight.__str__()
        if enable_string_comparison is not None:
            body["enableStringComparison"] = enable_string_comparison.__str__()
        if default_document_type is not None:
            body["defaultDocumentType"] = default_document_type
        if enable_paragraph_sorting is not None:
            body["enableParagraphSorting"] = enable_paragraph_sorting.__str__()
        if enable_paragraph_end_detection is not None:
            body["enableParagraphEndDetection"] = enable_paragraph_end_detection.__str__()
        if enable_paragraph_merging_based_on_formatting is not None:
            body["enableParagraphMergingBasedOnFormatting"] = enable_paragraph_merging_based_on_formatting.__str__()
        if enable_boost_word_filtering_for_input_documents is not None:
            body["enableBoostWordFilteringForInputDocuments"] = enable_boost_word_filtering_for_input_documents.__str__()
        if tagging_similarity_mode is not None:
            body["taggingSimilarityMode"] = tagging_similarity_mode
        if enable_updating_fingerprints_on_tag_updates is not None:
            body["enableUpdatingFingerprintsOnTagUpdates"] = enable_updating_fingerprints_on_tag_updates.__str__()
        if similarity_matcher is not None:
            body["similarityMatcher"] = similarity_matcher
        if similarity_max_deviation is not None:
            body["similarityMaxDeviation"] = similarity_max_deviation.__str__()
        if similarity_threshold is not None:
            body["similarityThreshold"] = keep_numbers.__str__()
        if enable_tagging is not None:
            body["enableTagging"] = enable_tagging.__str__()
        if tagging_threshold is not None:
            body["taggingThreshold"] = tagging_threshold.__str__()
        if tagging_strategy is not None:
            body["taggingStrategy"] = tagging_strategy
        if extraction_threshold is not None:
            body["extractionThreshold"] = extraction_threshold.__str__()
        if extraction_strategy is not None:
            body["extractionStrategy"] = extraction_strategy
        if resize_paragraphs_on_extraction is not None:
            body["resizeParagraphsOnExtraction"] = resize_paragraphs_on_extraction.__str__()
        response = self._session.patch(f"{self._endpoint}/settings", json=body).execute()
        return response.to(DomainSettings)

    def get_stopwords(self) -> list[str]:
        """Get all stopwords that are defined for the domain"""
        return self._session.get(f"{self._endpoint}/stopwords").execute().as_list()

    def get_tags(self) -> list[str]:
        """Get all tags that are defined for the domain"""
        return self._session.get(f"{self._endpoint}/tags").execute().as_list()



# TODO: Add docstrings, comments, type hints and error handling.
class Domains(SemanthaAPIEndpoint):
    """
        References:
            Specific domains by name
    """

    @property
    def _endpoint(self):
        return self._parent_endpoint + "/domains"

    def get_all(self) -> list[_DomainDTO]:
        """ Get all available domains """
        return self._session.get(self._endpoint).execute().to(_DomainsDTO).domains

    def get_one(self, domain_name: str) -> Domain:
        # Returns a Domain object for the given domainname, throws error if id doesn't exist
        return Domain(self._session, self._endpoint, domain_name)
