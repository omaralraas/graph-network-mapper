from src.network_graph import NetworkGraph, bfs_shortest_path


def test_bfs_shortest_path():
    g = NetworkGraph()
    g.connect("A", "B")
    g.connect("B", "C")
    g.connect("A", "D")
    assert bfs_shortest_path(g, "A", "C") == ["A", "B", "C"]