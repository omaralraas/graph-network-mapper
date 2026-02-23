from __future__ import annotations

from src.packet_tree import parse_packet, dfs_print
from src.network_graph import (
    NetworkGraph,
    bfs_shortest_path,
    dfs_traversal,
    has_cycle,
    dijkstra_shortest_path,
)
from src.simulation import build_sample_topology, scan_network
from src.visualization.network_viz import draw_network


def demo_packet_tree() -> None:
    packet = {
        "ethernet": {"src_mac": "AA:BB:CC:DD:EE:01", "dst_mac": "AA:BB:CC:DD:EE:FF"},
        "ip": {"src_ip": "192.168.1.10", "dst_ip": "10.0.0.5", "ttl": 64},
        "transport": {"type": "TCP", "src_port": 51514, "dst_port": 443, "flags": "SYN"},
        "app": {"proto": "TLS", "sni": "example.com"},
    }

    root = parse_packet(packet)

    print("=== Packet Parsing Tree ===")
    dfs_print(root)


def demo_graph() -> None:
    # Build sample topology
    g: NetworkGraph = build_sample_topology()

    print("\n=== Network Mapper Graph ===")
    print("Devices:", ", ".join(sorted(g.devices())))

    # Cycle detection
    print("\nCycle present:", has_cycle(g))

    # BFS shortest path (unweighted)
    start, target = "ClientA", "Server2"
    path = bfs_shortest_path(g, start, target)
    print(f"\nBFS shortest path ({start} -> {target}):", path if path else "No path found")

    # DFS traversal
    start_scan = "Router"
    order = dfs_traversal(g, start_scan)
    print(f"\nDFS traversal from {start_scan}:", order)

    # Network scan simulation
    report = scan_network(g, start_scan)
    print("\nScan report:", report)

    # ✅ Dijkstra weighted shortest path (cheapest path)
    cheapest_path, cheapest_cost = dijkstra_shortest_path(g, "ClientA", "Server2")
    print(f"\nDijkstra cheapest path (ClientA -> Server2): {cheapest_path} | cost={cheapest_cost}")

    # 🎨 Visualization with cheapest path highlighted in red
    print("\nOpening network visualization window (cheapest path highlighted in red)...")
    draw_network(
        g,
        title="Sample Network Topology (Cheapest Path Highlighted)",
        show_weights=True,
        save_path="topology.png",
        highlight_path=cheapest_path,
    )


def main() -> None:
    demo_packet_tree()
    demo_graph()


if __name__ == "__main__":
    main()