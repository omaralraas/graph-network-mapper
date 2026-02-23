from __future__ import annotations

import heapq
from math import inf

from .graph import NetworkGraph


def dijkstra_shortest_path(g: NetworkGraph, start: str, target: str) -> tuple[list[str], float]:
    """
    Dijkstra shortest path for positive weights.
    Returns (path, total_cost). If unreachable => ([], inf)

    Complexity: O((V + E) log V) using a binary heap.
    """
    if start not in g.adj or target not in g.adj:
        return ([], inf)
    if start == target:
        return ([start], 0.0)

    dist: dict[str, float] = {node: inf for node in g.devices()}
    parent: dict[str, str | None] = {start: None}
    dist[start] = 0.0

    pq: list[tuple[float, str]] = [(0.0, start)]

    while pq:
        cur_dist, node = heapq.heappop(pq)
        if cur_dist != dist[node]:
            continue
        if node == target:
            break

        for nb in g.neighbors(node):
            w = g.weight(node, nb)
            nd = cur_dist + w
            if nd < dist[nb]:
                dist[nb] = nd
                parent[nb] = node
                heapq.heappush(pq, (nd, nb))

    if dist[target] == inf:
        return ([], inf)

    # reconstruct path
    path: list[str] = []
    cur: str | None = target
    while cur is not None:
        path.append(cur)
        cur = parent.get(cur)
    path.reverse()
    return (path, dist[target])