"""Module for working with scientific references.

Creates reference.json from given pubmed id.
Pubmed information is retrieved using web services.
"""
import json
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any, Dict, Final, Optional

import requests
from Bio import Entrez
from pymetadata.log import get_logger

from pkdb_data.management.utils import recursive_iter, set_keys


logger = get_logger(__name__)
entrez_email: Final = "janekg89@hotmail.de"
reference_filename: Final = "reference.json"


def create_reference_for_pmid(study_name: str, pmid: str, output_path: Path) -> None:
    """Run function."""

    xml = load_pmid_from_biopython(pmid)

    # create json
    json_dict: Dict[str, Any] = {
        "sid": pmid,
        "name": study_name,
    }
    try:
        pmid_int = int(pmid)
        json_dict["pmid"] = pmid_int
    except ValueError:
        pass

    xml_data = ET.fromstring(xml)

    for date in xml_data.iter("DateCompleted"):
        year = date.find("Year").text  # type: ignore
        month = date.find("Month").text  # type: ignore
        day = date.find("Day").text  # type: ignore
        json_dict["date"] = f"{year}-{str(month).zfill(2)}-{str(day).zfill(2)}"
        break

    for journal in xml_data.iter("Title"):
        json_dict["journal"] = journal.text
        break

    for title in xml_data.iter("ArticleTitle"):
        json_dict["title"] = title.text
        break
    for abstract in xml_data.iter("AbstractText"):
        json_dict["abstract"] = abstract.text
        break

    authors = []
    for author in xml_data.iter("Author"):
        author_dict = {}
        for key, value in {"first_name": "ForeName", "last_name": "LastName"}.items():
            try:
                author_dict[key] = author.find(value).text  # type: ignore
            except AttributeError:
                msg = (
                    f"No information on author <{key}>. Consider adding the {key} "
                    "manually to <reference.json>."
                )
                logger.warning(msg)
        authors.append(author_dict)

    json_dict["authors"] = authors
    json_dict["doi"] = get_doi_for_pmid(pmid)

    for keys, item in recursive_iter(json_dict):
        if item == "":
            set_keys(json_dict, None, *keys)

    # serialize data
    with open(Path(output_path) / reference_filename, "w") as f_json:
        json.dump(json_dict, fp=f_json, indent=2)


def load_pmid_from_biopython(pmid: str) -> str:
    """Retrieve pubmed information."""
    Entrez.email = entrez_email

    xml_str: str
    try:
        pmid_int: int = int(pmid)
        handle = Entrez.efetch(db="pubmed", id=pmid_int, retmode="xml")
        xml_str = handle.read()
        handle.close()
    except ValueError:
        logger.warning(
            "Empty `reference.json` created. Fill out required fields "
            "['title', 'date']. "
        )
        xml_str = (
            "<all>"
            "<PMID> 12345 </PMID>"
            "<DateCompleted>"
            "<Year>1000</Year>"
            "<Month>10</Month>"
            "<Day>10</Day>"
            "</DateCompleted>"
            "<Article>"
            "<Journal>"
            "<Title>Add your title</Title>"
            "</Journal>"
            "<ArticleTitle>Add your title</ArticleTitle>"
            "<AuthorList>"
            "<Author>"
            "<LastName>Mustermann</LastName>"
            "<ForeName>Max</ForeName>"
            "<Initials>MM</Initials>"
            "</Author>"
            "</AuthorList>"
            "</Article>"
            "</all>"
        )

    return xml_str


def get_doi_for_pmid(pmid: str) -> Optional[str]:
    """Get DOI for pubmed.

    If no DOI exists None is returned.
    """

    response = requests.get(
        f"https://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/?tool=my_tool&email=my_email@example.com&ids={pmid}"
    )
    pmcids = ET.fromstring(response.content)

    for records in pmcids.iter("record"):
        record_doi = records.get("doi", None)
        if record_doi:
            return record_doi

    return None
