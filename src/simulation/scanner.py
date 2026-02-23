from __future__ import annotations

from src.network_graph.dfs import dfs_traversal
from src.network_graph.graph import NetworkGraph


def scan_network(g: NetworkGraph, start: str) -> dict:
    """
    Simulate a network scan: discover devices reachable from a start node.
    Uses DFS for exploration (can swap with BFS if desired).
    """
    discovered = dfs_traversal(g, start)
    return {
        "start": start,
        "discovered_count": len(discovered),
        "discovered_devices": discovered,
    }