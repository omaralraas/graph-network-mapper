from src.network_graph import NetworkGraph, dfs_traversal


def test_dfs_traversal_reaches_all_connected():
    g = NetworkGraph()
    g.connect("A", "B")
    g.connect("B", "C")
    order = dfs_traversal(g, "A")
    assert set(order) == {"A", "B", "C"}