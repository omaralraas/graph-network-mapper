from __future__ import annotations

from typing import Optional

import matplotlib.pyplot as plt
import networkx as nx

from src.network_graph.graph import NetworkGraph


def draw_network(
    g: NetworkGraph,
    title: str = "Network Topology",
    show_weights: bool = True,
    save_path: Optional[str] = None,
    highlight_path: Optional[list[str]] = None,
) -> None:
    """
    Visualize your custom NetworkGraph using NetworkX for rendering only.

    highlight_path:
        A list of node names representing a path (e.g. Dijkstra result).
        The edges on this path will be highlighted in red.
    """
    G = nx.Graph()

    # Add nodes
    for device in g.devices():
        G.add_node(device)

    # Add edges (avoid duplicates in undirected graph)
    seen = set()
    for a in g.devices():
        for b in g.neighbors(a):
            key = tuple(sorted((a, b)))
            if key in seen:
                continue
            seen.add(key)
            G.add_edge(a, b, weight=g.weight(a, b))

    pos = nx.spring_layout(G, seed=42)  # stable layout

    # Build a set of edges that are in the highlight path
    highlight_edges = set()
    if highlight_path and len(highlight_path) >= 2:
        for i in range(len(highlight_path) - 1):
            u = highlight_path[i]
            v = highlight_path[i + 1]
            # undirected edge -> store sorted tuple
            highlight_edges.add(tuple(sorted((u, v))))

    # Edge styling: red for highlight edges, gray for normal edges
    edge_colors = []
    edge_widths = []
    for u, v in G.edges():
        key = tuple(sorted((u, v)))
        if key in highlight_edges:
            edge_colors.append("red")
            edge_widths.append(3.0)
        else:
            edge_colors.append("gray")
            edge_widths.append(1.5)

    plt.figure()
    nx.draw(
        G,
        pos,
        with_labels=True,
        edge_color=edge_colors,
        width=edge_widths,
    )

    if show_weights:
        labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.title(title)

    if save_path:
        plt.savefig(save_path, bbox_inches="tight")

    plt.show()