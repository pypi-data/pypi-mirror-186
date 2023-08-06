"""Annotations for InfoNodes."""

import urllib
from typing import Any, Dict, List, Optional, Union

from pymetadata.core.annotation import RDFAnnotation
from pymetadata.core.xref import CrossReference, is_url
from pymetadata.identifiers.miriam import BQB, BQM
from pymetadata.identifiers.registry import Registry, Resource
from pymetadata.log import get_logger
from pymetadata.ontologies.ols import ONTOLOGIES, OLSQuery

from pkdb_data import CACHE_PATH, CACHE_USE


logger = get_logger(__name__)

REGISTRY = Registry()
OLS_QUERY = OLSQuery(ontologies=ONTOLOGIES, cache_path=CACHE_PATH, cache=CACHE_USE)


class NodeAnnotation(object):
    """Annotation information for info node."""

    def __init__(
        self,
        relation: Union[BQB, BQM],
        resource: str,
    ):
        """Initialize NodeAnnotation."""
        self.relation: Union[BQB, BQM] = relation
        self.description: Optional[str] = None
        self.label: Optional[str] = None
        self.url: Optional[str] = None
        self.synonyms: List[str] = []
        self.xrefs: list = []

        # get the collection/term part from identifiers.org urls
        for prefix in ["http://identifiers.org/", "https://identifiers.org/"]:
            if resource.startswith(prefix):
                resource = resource.replace(prefix, "")

        # other urls are directly stored as resources
        if resource.startswith("http"):
            self.collection = None
            self.term = resource
        else:
            # get term and collection
            tokens = resource.split("/")
            if len(tokens) < 2:
                raise ValueError(
                    f"resource `{resource}` must be of the form "
                    f"`collection/term` or an url starting with `http`)"
                )
            self.collection = tokens[0]
            self.term = "/".join(tokens[1:])

        self.validate()

        if self.collection:

            # register MIRIAM xrefs
            namespace = REGISTRY.ns_dict.get(self.collection)
            namespace_embedded = namespace.namespaceEmbeddedInLui
            # print("-" * 80)
            # print(namespace.prefix, "embedded=", namespace_embedded)

            ns_resource: Resource
            for ns_resource in namespace.resources:

                # create url
                url: str = ns_resource.urlPattern
                term = self.term

                # remove prefix
                if namespace_embedded:
                    term = term[len(namespace.prefix) + 1 :]

                # urlencode term
                term = urllib.parse.quote(term)

                # create url
                url = url.replace("{$Id}", term)
                url = url.replace("{$id}", term)
                url = url.replace(
                    f"{prefix.upper}:", urllib.parse.quote(f"{prefix.upper}:")
                )

                if not self.url:
                    # set url to first resource url
                    self.url = url

                _xref = CrossReference(
                    name=ns_resource.name, accession=self.term, url=url
                )
                valid = _xref.validate() and is_url(self.url)
                if valid:
                    self.xrefs.append(_xref)

    def query_ols(self) -> None:
        """Query information from ontology lookup services.

        Sets the information on the object.
        """
        d = OLS_QUERY.query_ols(ontology=self.collection, term=self.term)
        info: Dict[str, Any] = OLS_QUERY.process_response(d)
        if info:
            if self.label is None:
                self.label = info.get("label")

            if self.description is None:
                description = info.get("description")
                if isinstance(description, str):
                    self.description = description

            # TODO: process synonmys and xrefs
            self.synonyms = info["synonyms"]
            self.xrefs = info["xrefs"]

    def __repr__(self) -> str:
        """Get string representation."""
        return f"Annotation({self.collection}|{self.term}|{self.description}|{self.synonyms}|{self.xrefs})"

    def validate(self) -> None:
        """Validate annotation."""

        RDFAnnotation.check_qualifier(self.relation)
        if self.collection:
            RDFAnnotation.check_term(collection=self.collection, term=self.term)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation."""
        return {
            "term": self.term,
            "relation": self.relation.value,
            "collection": self.collection,
            "description": self.description,
            "label": self.label,
            "url": self.url,
            # synonyms and xrefs are not serialized
        }
