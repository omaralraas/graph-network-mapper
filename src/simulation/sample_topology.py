from __future__ import annotations

from src.network_graph.graph import NetworkGraph


def build_sample_topology() -> NetworkGraph:
    """
    Create a small sample topology with weights to demonstrate Dijkstra.
    """
    g = NetworkGraph()

    # Core
    g.connect("Router", "Firewall", weight=1.0)

    # Servers behind firewall
    g.connect("Firewall", "Server1", weight=2.0)
    g.connect("Firewall", "Server2", weight=2.5)

    # Clients
    g.connect("Router", "ClientA", weight=1.2)
    g.connect("Router", "ClientB", weight=1.0)

    # IoT / lateral link
    g.connect("ClientA", "IoT1", weight=3.0)

    # Add a loop/cycle (optional) by uncommenting:
    # g.connect("Server1", "Router", weight=4.0)

    return g