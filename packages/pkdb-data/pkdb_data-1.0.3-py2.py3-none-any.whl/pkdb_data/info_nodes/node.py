"""Functions related to the InfoNodes."""
from __future__ import annotations

from enum import Enum
from typing import Any, Dict, Iterable, Iterator, List, Optional

from pint import UndefinedUnitError
from pymetadata.chebi import ChebiQuery
from pymetadata.core.xref import CrossReference
from pymetadata.identifiers.miriam import BQB
from pymetadata.log import get_logger
from pymetadata.unichem import UnichemQuery
from slugify import slugify

from pkdb_data import CACHE_PATH, CACHE_USE
from pkdb_data.info_nodes.annotation import NodeAnnotation
from pkdb_data.info_nodes.units import ureg


logger = get_logger(__name__)


class DType(str, Enum):
    """Data types."""

    ABSTRACT = "abstract"
    BOOLEAN = "boolean"
    NUMERIC = "numeric"
    CATEGORICAL = "categorical"
    NUMERIC_CATEGORICAL = ("numeric_categorical",)
    UNDEFINED = "undefined"


class NType(str, Enum):
    """Node types."""

    INFO_NODE = "info_node"
    CHOICE = "choice"
    MEASUREMENT_TYPE = "measurement_type"
    CALCULATION_TYPE = "calculation_type"
    APPLICATION = "application"
    TISSUE = "tissue"
    METHOD = "method"
    Route = "route"
    FORM = "form"
    SUBSTANCE = "substance"
    SUBSTANCE_SET = "substance_set"


class InfoObject:
    """Object for defining node information."""

    required_fields = ["sid", "name", "label", "ntype", "dtype"]

    def __init__(
        self,
        sid: str,
        name: Optional[str] = None,
        label: Optional[str] = None,
        description: Optional[str] = None,
        ntype: Optional[str] = None,
        dtype: Optional[str] = None,
        annotations: Optional[List] = None,
        synonyms: Optional[List[str]] = None,
        xrefs: Optional[list] = None,
        deprecated: bool = False,
    ):
        """Initialize InfoObject.

        :param sid: unique identifier
        :param name: curation identifier (used for curation!, mostly sid)
        :param label: display name
        :param ntype: node type
        :param dtype: data type
        :param description: description details.
        :param annotations:
        :param synonyms:
        :param deprecated: deprecation flag for validation
        """
        self.sid = InfoObject.url_slugify(sid)
        self.name = name if name else sid
        self.label = label if label else self.name
        self.description = description
        self.annotations = annotations
        self.synonyms = set(synonyms) if synonyms is not None else set()
        self.xrefs = xrefs
        self.ntype = ntype
        self.dtype = dtype
        self.deprecated = deprecated

        # init with empty list
        for key in ["annotations", "synonyms", "xrefs"]:
            if getattr(self, key) is None:
                setattr(self, key, list())

        self._process_annotations()
        self.validate()

    def __repr__(self) -> str:
        """Get string representation."""
        return f"<{self.__class__.__name__} {self.sid} | {self.name} | {self.label}>"

    @staticmethod
    def url_slugify(key: str) -> str:
        """Sanitizes sid for use in url."""
        slug = slugify(
            key, replacements=[["*", "-times-"], ["/", "-over-"], ["+", "-plus-"]]
        )
        return str(slug)

    def validate(self) -> None:
        """Validate info node."""
        self.validate_ntype()
        self.validate_dtype()

        # check that fields are simple iterables
        for key in ["annotations", "synonyms"]:
            data = getattr(self, key)
            if not isinstance(data, (list, set, tuple)):
                raise ValueError(
                    f"<{key}> must be list, " f"set or tuple for <{self.sid}>"
                )

        for field in InfoObject.required_fields:
            if not getattr(self, field):
                raise ValueError(
                    f"'Required information <{field}> missing on <{self.sid}>"
                )

        if not self.description:
            logger.warning(f"{self.__class__.__name__} <{self.sid}> misses description")

    def validate_ntype(self) -> None:
        """Validate the node type."""
        if self.ntype not in NType:
            raise ValueError(f"<{self.ntype}> is not in Ntype for sid <{self.sid}>.")

    def validate_dtype(self) -> None:
        """Validate the data type."""
        if self.dtype not in DType:
            raise ValueError(
                f"<{self.dtype}> is not in Dtype for for sid <{self.sid}>."
            )

    def _process_annotations(self) -> None:
        """Create and set annotation objects from annotation strings."""
        full_annotations = []
        if self.annotations:
            for a_data in self.annotations:
                if isinstance(a_data, tuple):
                    annotation = NodeAnnotation(relation=a_data[0], resource=a_data[1])
                elif isinstance(a_data, NodeAnnotation):
                    annotation = a_data
                else:
                    raise ValueError(
                        f"Unsupported annotation type: {type(a_data)}"
                        f" for {self.sid!r}: {a_data!r}"
                    )

                full_annotations.append(annotation)

        self.annotations = full_annotations

    def query_metadata(self) -> None:
        """Query management for given annotations.

        Only call once before serialization when the complete tree exists!.
        This can be a slow operation due to the underlying web service calls.
        """

        # query annotation information from ols
        if self.annotations:
            for annotation in self.annotations:
                # validate annotation
                annotation.validate()

                annotation.query_ols()
                if annotation.relation == BQB.IS:
                    if annotation.label:
                        self.synonyms.add(annotation.label)
                    if annotation.synonyms:
                        for synonym in annotation.synonyms:
                            if isinstance(synonym, dict):
                                self.synonyms.add(synonym["name"])
                            else:
                                self.synonyms.add(synonym)

                    # FIXME: THIS ARE ANNOTATION XREFS, ONLY INTERESTED IN uniquem xrefs
                    # if annotation.xrefs:
                    #     if self.xrefs is None:
                    #         self.xrefs = []
                    #     self.xrefs.extend(annotation.xrefs)

    def serialize(self) -> Dict[str, Any]:
        """Serialize information to dictionary."""
        xrefs_info = []
        if self.xrefs:
            for xref in self.xrefs:
                if isinstance(xref, dict):
                    if "description" not in xref:
                        xref["description"] = None
                    xrefs_info.append(xref)
                else:
                    xrefs_info.append(xref.to_dict())

        annotations_info = []
        if self.annotations:
            for annotation in self.annotations:
                annotations_info.append(annotation.to_dict())

        return {
            "sid": self.sid,
            "name": self.name,
            "label": self.label,
            "ntype": self.ntype,
            "dtype": self.dtype,
            "description": self.description,
            "annotations": annotations_info,
            "synonyms": sorted(list(self.synonyms)),
            "xrefs": xrefs_info,
            "deprecated": self.deprecated,
        }


class InfoNode(InfoObject):
    """Node."""

    def __init__(
        self,
        sid: str,
        description: str,
        parents: list[str],
        ntype: NType = NType.INFO_NODE,
        dtype: DType = DType.ABSTRACT,
        name: Optional[str] = None,
        label: Optional[str] = None,
        annotations: Optional[list] = None,
        synonyms: Optional[list[str]] = None,
        xrefs: Optional[list] = None,
        deprecated: bool = False,
    ):
        """Initialize InfoNode."""
        super().__init__(
            sid=sid,
            name=name,
            label=label,
            ntype=ntype,
            dtype=dtype,
            description=description,
            annotations=annotations,
            synonyms=synonyms,
            xrefs=xrefs,
            deprecated=deprecated,
        )
        self.parents = [self.url_slugify(p) for p in parents] if parents else list()
        self._children: Optional[List[InfoNode]] = None

    @property
    def can_choice(self) -> bool:
        """Field if it can be a choice."""
        return False

    def children(
        self, all_nodes: Iterable[InfoNode], force_calculation: bool = True
    ) -> List[InfoNode]:
        """Return children from set of given nodes.

        Does not check if all children have been found.
        """
        if (force_calculation is True) or (self._children is None):
            # This is very expensive and should only be done once
            self._children = [node for node in all_nodes if self.sid in node.parents]

        return self._children

    def children_sids(
        self, all_nodes: Iterable[InfoNode], force_calculation: bool = True
    ) -> List[str]:
        """Get list of children SIds."""
        return [node.sid for node in self.children(all_nodes, force_calculation)]

    def serialize(self, all_nodes: Iterable[InfoNode]) -> Dict[str, Any]:  # type: ignore
        """Serialize to dictionary."""
        into_dict = super().serialize()
        this_dict = {
            **into_dict,
            "parents": self.parents,
            "children": self.children_sids(all_nodes),
        }
        return this_dict

    def choices(self, all_nodes: Iterable[InfoNode]) -> Iterator[str]:
        """Get choices."""
        for child in self.children(all_nodes):
            if not child.can_choice:
                yield from child.choices(all_nodes)

            if child.ntype == NType.CHOICE:
                yield child.sid


class MeasurementType(InfoNode):
    """MeasurementType."""

    def __init__(
        self,
        sid: str,
        description: str,
        parents: list[str],
        dtype: DType,
        name: Optional[str] = None,
        label: Optional[str] = None,
        units: Optional[list] = None,
        annotations: Optional[list] = None,
        synonyms: Optional[list] = None,
        xrefs: Optional[list] = None,
        deprecated: bool = False,
    ):
        """Initialize MeasurementType."""
        super().__init__(
            sid=sid,
            name=name,
            label=label,
            ntype=NType.MEASUREMENT_TYPE,
            dtype=dtype,
            description=description,
            annotations=annotations,
            synonyms=synonyms,
            xrefs=xrefs,
            parents=parents,
            deprecated=deprecated,
        )
        self.units = units if units else list()
        self.validate_units()

    @property
    def can_choice(self) -> bool:
        """Can the info node have choices."""
        return self.dtype in [
            DType.CATEGORICAL,
            DType.NUMERIC_CATEGORICAL,
            DType.BOOLEAN,
        ]

    def serialize(self, all_nodes: Iterable[InfoNode]) -> Dict[str, Any]:  # type: ignore
        """Serialze information to dictionary."""
        into_dict = super().serialize(all_nodes)
        return {
            **into_dict,
            "measurement_type": self.measurement_type_extra(all_nodes),
        }

    def measurement_type_extra(self, all_nodes: Iterable[InfoNode]) -> Dict[str, Any]:
        """Additional measurement type information."""
        measurement_type_extra = {"units": self.units}
        if self.can_choice:
            measurement_type_extra["choices"] = list(self.choices(all_nodes))
        else:
            measurement_type_extra["choices"] = []
        return measurement_type_extra

    def validate_units(self) -> None:
        """Validate that units are defined in unit registry."""
        for unit in self.units:
            try:
                ureg(unit)
            except UndefinedUnitError as err:
                logger.error(f"UndefinedUnitError for {self}: {err}")
                raise err


class Substance(InfoNode):
    """Substance."""

    def __init__(
        self,
        sid: str,
        description: str,
        name: Optional[str] = None,
        label: Optional[str] = None,
        parents: Optional[List[str]] = None,
        synonyms: Optional[List[str]] = None,
        annotations: Optional[List] = None,
        xrefs: Optional[List] = None,
        deprecated: bool = False,
        dtype: DType = DType.UNDEFINED,
        formula: Optional[str] = None,
        charge: Optional[int] = None,
        mass: Optional[float] = None,
    ):
        """Init substance."""
        super().__init__(
            sid=sid,
            name=name,
            label=label,
            description=description,
            parents=parents if parents else [],
            ntype=NType.SUBSTANCE,
            dtype=dtype,
            annotations=annotations,
            synonyms=synonyms,
            xrefs=xrefs,
            deprecated=deprecated,
        )

        self.formula = formula
        self.charge = charge
        self.mass = mass

        # retrieve chebi information
        chebi = self.chebi()
        if chebi:
            chebi_dict = ChebiQuery.query(chebi, cache_path=CACHE_PATH, cache=CACHE_USE)
            if self.description is None:
                self.description = chebi_dict.get("description", None)

            # chemical information
            for key in ["mass", "charge", "formula"]:
                if key in chebi_dict:
                    value = chebi_dict[key]
                    if value is None:
                        continue
                    if getattr(self, key) is not None:
                        logger.warning(
                            f"<{self.sid}> <{key}> overwritten: {getattr(self, key)} -> {value}"
                        )
                    setattr(self, key, value)

            # add inchikey to annotations
            inchikey = chebi_dict.get("inchikey", None)
            if inchikey:
                if self.annotations is None:
                    self.annotations = []
                self.annotations.append(
                    NodeAnnotation(relation=BQB.IS, resource=f"inchikey/{inchikey}")
                )

                # query cross references from unichem using the inchikey
                xrefs_unichem: List[CrossReference] = UnichemQuery(
                    cache_path=CACHE_PATH,
                    cache=CACHE_USE,
                ).query_xrefs_for_inchikey(inchikey=inchikey)
                if self.xrefs is None:
                    self.xrefs = []
                for xref in xrefs_unichem:
                    if xref.validate(warnings=False):
                        self.xrefs.append(xref)

        self.substance = {
            "mass": self.mass,
            "charge": self.charge,
            "formula": self.formula,
            "stype": "derived" if self.parents else "basic",
        }

    def chebi(self) -> Optional[str]:
        """Read chebi term from the annotations.

        Returns None of no chebi annotation exists.
        """
        # FIXME: this can be dangerous if additional chebi terms are added
        if self.annotations:
            for annotation in self.annotations:
                # check if a chebi annotation exists (returns first)
                if (annotation.relation == BQB.IS) and (
                    annotation.collection == "chebi"
                ):
                    return str(annotation.term)

        return None

    def serialize(self, all_nodes: Iterable[InfoNode]) -> Dict[str, Any]:  # type: ignore
        """Serialize to dictionary."""
        info_dict = super().serialize(all_nodes)
        info_dict["substance"] = self.substance
        return info_dict


class InfoNodeUndefined(InfoNode):
    """Undefined InfoNode."""

    def __init__(
        self,
        sid: str,
        name: Optional[str] = None,
        label: Optional[str] = None,
        parents: Optional[List[str]] = None,
        synonyms: Optional[List[str]] = None,
        description: Optional[str] = None,
        annotations: Optional[List] = None,
        dtype: DType = DType.UNDEFINED,
        deprecated: bool = False,
    ):
        """Initialize InfoNodeUndefined."""
        super().__init__(
            sid=sid,
            name=name,
            label=label,
            description=description if description else "",
            parents=parents if parents else [],
            ntype=NType.METHOD,
            dtype=dtype,
            annotations=annotations,
            synonyms=synonyms,
            deprecated=deprecated,
        )


class Method(InfoNode):
    """Method."""

    def __init__(
        self,
        sid: str,
        description: str,
        name: Optional[str] = None,
        label: Optional[str] = None,
        parents: Optional[List[str]] = None,
        synonyms: Optional[List[str]] = None,
        annotations: Optional[List] = None,
        dtype: DType = DType.UNDEFINED,
        deprecated: bool = False,
    ):
        """Initialize Method."""
        super().__init__(
            sid=sid,
            name=name,
            label=label,
            description=description,
            parents=parents if parents else [],
            ntype=NType.METHOD,
            dtype=dtype,
            annotations=annotations,
            synonyms=synonyms,
            deprecated=deprecated,
        )


class Tissue(InfoNode):
    """Tissue."""

    def __init__(
        self,
        sid: str,
        description: str,
        name: Optional[str] = None,
        label: Optional[str] = None,
        parents: Optional[List[str]] = None,
        synonyms: Optional[List[str]] = None,
        annotations: Optional[List] = None,
        dtype: DType = DType.UNDEFINED,
        deprecated: bool = False,
    ):
        """Initialize Tissue."""
        super().__init__(
            sid=sid,
            name=name,
            label=label,
            description=description,
            parents=parents if parents else [],
            ntype=NType.TISSUE,
            dtype=dtype,
            annotations=annotations,
            synonyms=synonyms,
            deprecated=deprecated,
        )


class Route(InfoNode):
    """Route."""

    def __init__(
        self,
        sid: str,
        description: str,
        name: Optional[str] = None,
        label: Optional[str] = None,
        parents: Optional[List[str]] = None,
        synonyms: Optional[List[str]] = None,
        annotations: Optional[List] = None,
        dtype: DType = DType.UNDEFINED,
        deprecated: bool = False,
    ):
        """Initialize route."""
        super().__init__(
            sid=sid,
            name=name,
            label=label,
            description=description,
            parents=parents if parents else [],
            ntype=NType.Route,
            dtype=dtype,
            annotations=annotations,
            synonyms=synonyms,
            deprecated=deprecated,
        )


class Application(InfoNode):
    """Application."""

    def __init__(
        self,
        sid: str,
        description: str,
        name: Optional[str] = None,
        label: Optional[str] = None,
        parents: Optional[List[str]] = None,
        synonyms: Optional[List[str]] = None,
        annotations: Optional[List] = None,
        dtype: DType = DType.UNDEFINED,
        deprecated: bool = False,
    ):
        """Initialize application."""
        super().__init__(
            sid=sid,
            name=name,
            label=label,
            description=description,
            parents=parents if parents else [],
            ntype=NType.APPLICATION,
            dtype=dtype,
            annotations=annotations,
            synonyms=synonyms,
            deprecated=deprecated,
        )


class Form(InfoNode):
    """Form."""

    def __init__(
        self,
        sid: str,
        description: str,
        name: Optional[str] = None,
        label: Optional[str] = None,
        parents: Optional[List[str]] = None,
        synonyms: Optional[List[str]] = None,
        annotations: Optional[List] = None,
        dtype: DType = DType.UNDEFINED,
        deprecated: bool = False,
    ):
        """Initialize form."""
        super().__init__(
            sid=sid,
            name=name,
            label=label,
            description=description,
            parents=parents if parents else [],
            ntype=NType.FORM,
            dtype=dtype,
            annotations=annotations,
            synonyms=synonyms,
            deprecated=deprecated,
        )


class CalculationType(InfoNode):
    """CalculationType."""

    def __init__(
        self,
        sid: str,
        description: str,
        name: Optional[str] = None,
        label: Optional[str] = None,
        parents: Optional[List[str]] = None,
        synonyms: Optional[List[str]] = None,
        annotations: Optional[List] = None,
        dtype: DType = DType.CATEGORICAL,
        deprecated: bool = False,
    ):
        """Initialize CalculationType."""
        super().__init__(
            sid=sid,
            name=name,
            label=label,
            description=description,
            parents=parents if parents else [],
            ntype=NType.CALCULATION_TYPE,
            dtype=dtype,
            annotations=annotations,
            synonyms=synonyms,
            deprecated=deprecated,
        )


class Choice(InfoNode):
    """Choice."""

    def __init__(
        self,
        sid: str,
        description: str,
        name: Optional[str] = None,
        label: Optional[str] = None,
        parents: Optional[List[str]] = None,
        synonyms: Optional[List[str]] = None,
        annotations: Optional[List] = None,
        dtype: DType = DType.UNDEFINED,
        deprecated: bool = False,
    ):
        """Initialize Choice."""
        super().__init__(
            sid=sid,
            name=name,
            label=label,
            description=description,
            parents=parents if parents else [],
            ntype=NType.CHOICE,
            dtype=dtype,
            annotations=annotations,
            synonyms=synonyms,
            deprecated=deprecated,
        )

    def measurement_type(self, all_nodes: Iterable[InfoNode]) -> List[str]:
        """Get measurement type for nodes."""
        measurement_types = []
        for node in all_nodes:
            if node.ntype == NType.MEASUREMENT_TYPE:
                if self.sid in node.choices(all_nodes):
                    measurement_types.append(node.sid)
        return measurement_types

    def serialize(self, all_nodes: Iterable[InfoNode]) -> Dict[str, Any]:  # type: ignore
        """Serialize choice."""
        into_dict = super().serialize(all_nodes)
        return {
            **into_dict,
            "choice": {"measurement_types": self.measurement_type(all_nodes)},
        }
