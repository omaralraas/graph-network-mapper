from __future__ import annotations

from .node import PacketNode


def dfs_print(node: PacketNode, depth: int = 0) -> None:
    """
    Depth-first traversal print of the packet tree.
    """
    indent = "  " * depth
    info_str = f" {node.info}" if node.info else ""
    print(f"{indent}- {node.protocol}{info_str}")
    for child in node.children:
        dfs_print(child, depth + 1)