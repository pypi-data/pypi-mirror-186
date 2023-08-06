"""Create network graph of InfoNodes.

- creates network view
- creates SIF network file
- creates node attribute TSV
"""

import json
import logging
from pathlib import Path
from typing import Dict, Iterable, Optional, Tuple

import networkx
import networkx as nx
import pandas as pd
from pymetadata.console import console

from pkdb_data import RESOURCES_DIR


def read_json(path: Path) -> Optional[Dict]:
    """Read info node json."""
    with open(path) as f:
        try:
            json_data: Dict[str, str] = json.loads(
                f.read(), object_pairs_hook=dict_raise_on_duplicates
            )
        except json.decoder.JSONDecodeError as err:
            logging.warning(f"{err} in {path}")
            return None
        except ValueError as err:
            logging.warning(f"{err} in {path}")
            return None

    return json_data


def dict_raise_on_duplicates(
    ordered_pairs: Iterable[Tuple[str, str]]
) -> Dict[str, str]:
    """Reject duplicate keys."""
    d = {}
    for k, v in ordered_pairs:
        if k in d:
            raise ValueError("duplicate key: %r" % (k,))
        else:
            d[k] = v
    return d


def create_graph(
    info_nodes_path: Path, sif_path: Path, nodes_table_path: Path
) -> networkx.Graph:
    """Create graph and edges from given Info Nodes JSON.

    Stores the graph edges as SIF for import in cytoscape.
    """
    console.print(f"graph from info nodes: {info_nodes_path}")
    node_js = read_json(info_nodes_path)

    nodes = pd.DataFrame(node_js)
    links = []
    for _, row in nodes.iterrows():
        df = pd.DataFrame(row["parents"], columns=["parent"])
        df["node"] = row["sid"]
        links.append(df)
    edges: pd.DataFrame = pd.concat(links)
    edges["interaction"] = "is_a"

    graph: networkx.Graph = nx.from_pandas_edgelist(
        edges, source="node", target="parent", create_using=nx.Graph()
    )

    # export edges to SIF network format
    console.print(f"write edge file: {sif_path}")
    edges[["node", "interaction", "parent"]].to_csv(
        sif_path, sep="\t", index=False, header=False
    )
    # export nodes to table
    console.print(f"write nodes file: {nodes_table_path}")
    nodes[
        ["sid", "name", "ntype", "dtype", "description", "annotations", "children"]
    ].to_csv(nodes_table_path, sep="\t", index=False)

    return graph


if __name__ == "__main__":
    base_dir = Path(__file__).parent
    results_dir = base_dir / "results"

    info_nodes_json = RESOURCES_DIR / "json" / "info_nodes.json"
    sif_path = results_dir / "pkdb_network.sif"
    nodes_table_path = results_dir / "pkdb_nodes.tsv"

    create_graph(
        info_nodes_path=info_nodes_json,
        sif_path=sif_path,
        nodes_table_path=nodes_table_path,
    )
