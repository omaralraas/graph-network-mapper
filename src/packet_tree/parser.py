from __future__ import annotations

from typing import Any

from .node import PacketNode


def parse_packet(packet: dict[str, Any]) -> PacketNode:
    """
    Convert a dict-based simulated packet into a protocol encapsulation tree.

    Expected packet format:
    {
      "ethernet": {...},
      "ip": {...},
      "transport": {"type": "TCP"|"UDP", ...},
      "app": {"proto": "HTTP"|"...", ...}   # optional
    }
    """
    ethernet = PacketNode("Ethernet", packet.get("ethernet", {}))

    ip_layer = packet.get("ip")
    if ip_layer:
        ip = PacketNode("IP", ip_layer)
    else:
        # If no IP, return minimal tree
        return ethernet

    transport_layer = packet.get("transport", {})
    trans_type = transport_layer.get("type", "TCP/UDP")
    transport = PacketNode(str(trans_type), transport_layer)

    app_layer = packet.get("app")
    if app_layer:
        app_proto = app_layer.get("proto", "Application")
        app = PacketNode(str(app_proto), app_layer)
        transport.add_child(app)

    ip.add_child(transport)
    ethernet.add_child(ip)
    return ethernet