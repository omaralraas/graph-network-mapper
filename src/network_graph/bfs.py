from __future__ import annotations

from collections import deque

from .graph import NetworkGraph


def bfs_shortest_path(g: NetworkGraph, start: str, target: str) -> list[str]:
    """
    BFS shortest path for an unweighted graph.
    Returns list of nodes representing the path, or [] if unreachable.
    Time: O(V + E)
    """
    if start not in g.adj or target not in g.adj:
        return []
    if start == target:
        return [start]

    q = deque([start])
    parent: dict[str, str | None] = {start: None}

    while q:
        node = q.popleft()
        for nb in g.neighbors(node):
            if nb not in parent:
                parent[nb] = node
                if nb == target:
                    # reconstruct
                    path = [target]
                    cur = target
                    while parent[cur] is not None:
                        cur = parent[cur]  # type: ignore[assignment]
                        path.append(cur)
                    return list(reversed(path))
                q.append(nb)

    return []