from __future__ import annotations

from .graph import NetworkGraph


def dfs_traversal(g: NetworkGraph, start: str) -> list[str]:
    """
    DFS traversal order from start.
    Time: O(V + E)
    """
    if start not in g.adj:
        return []

    visited: set[str] = set()
    order: list[str] = []

    def dfs(node: str) -> None:
        visited.add(node)
        order.append(node)
        for nb in g.neighbors(node):
            if nb not in visited:
                dfs(nb)

    dfs(start)
    return order