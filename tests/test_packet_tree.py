from src.packet_tree import parse_packet


def test_parse_packet_builds_tree():
    packet = {
        "ethernet": {"src_mac": "A", "dst_mac": "B"},
        "ip": {"src_ip": "1.1.1.1", "dst_ip": "2.2.2.2"},
        "transport": {"type": "TCP", "src_port": 1, "dst_port": 2},
        "app": {"proto": "HTTP"},
    }
    root = parse_packet(packet)

    assert root.protocol == "Ethernet"
    assert len(root.children) == 1
    assert root.children[0].protocol == "IP"
    assert root.children[0].children[0].protocol == "TCP"
    assert root.children[0].children[0].children[0].protocol == "HTTP"