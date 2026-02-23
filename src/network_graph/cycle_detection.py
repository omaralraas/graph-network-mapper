from __future__ import annotations

from .graph import NetworkGraph


def has_cycle(g: NetworkGraph) -> bool:
    """
    Cycle detection in an undirected graph using DFS.
    Time: O(V + E)
    """
    visited: set[str] = set()

    def dfs(node: str, parent: str | None) -> bool:
        visited.add(node)
        for nb in g.neighbors(node):
            if nb not in visited:
                if dfs(nb, node):
                    return True
            elif nb != parent:
                return True
        return False

    for d in g.devices():
        if d not in visited:
            if dfs(d, None):
                return True
    return False