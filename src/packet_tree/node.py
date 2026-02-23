from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class PacketNode:
    """
    A node representing a protocol layer in a parsed packet.
    Example: Ethernet -> IP -> TCP -> HTTP
    """
    protocol: str
    info: dict[str, Any] = field(default_factory=dict)
    children: list["PacketNode"] = field(default_factory=list)

    def add_child(self, node: "PacketNode") -> None:
        self.children.append(node)