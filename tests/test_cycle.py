from src.network_graph import NetworkGraph, has_cycle


def test_cycle_detection_true():
    g = NetworkGraph()
    g.connect("A", "B")
    g.connect("B", "C")
    g.connect("C", "A")
    assert has_cycle(g) is True


def test_cycle_detection_false():
    g = NetworkGraph()
    g.connect("A", "B")
    g.connect("B", "C")
    assert has_cycle(g) is False