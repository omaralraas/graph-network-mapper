from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class NetworkGraph:
    """
    Undirected graph with an adjacency list.
    Supports optional edge weights for routing simulations.

    adj structure:
        {
          "A": {"B": 1.0, "C": 3.0},
          "B": {"A": 1.0}
        }
    """
    adj: dict[str, dict[str, float]] = field(default_factory=dict)

    def add_device(self, device: str) -> None:
        if device not in self.adj:
            self.adj[device] = {}

    def connect(self, a: str, b: str, weight: float = 1.0) -> None:
        """
        Connect two devices (undirected). Weight defaults to 1.0.
        """
        if weight <= 0:
            raise ValueError("Edge weight must be positive.")
        self.add_device(a)
        self.add_device(b)
        self.adj[a][b] = float(weight)
        self.adj[b][a] = float(weight)

    def devices(self) -> list[str]:
        return list(self.adj.keys())

    def neighbors(self, device: str) -> list[str]:
        return list(self.adj.get(device, {}).keys())

    def weight(self, a: str, b: str) -> float:
        return self.adj[a][b]