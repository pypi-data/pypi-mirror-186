from __future__ import annotations

from abc import ABC, abstractmethod

from adtree.models import ADTree, Node, NodeType


class Analyser(ABC):
    @abstractmethod
    def analyse_tree(self, tree: ADTree) -> ADTree:
        pass


# Traverse the tree and mark each nodes as either defended or undefended
# A node is considered defended if:
# 1. is a Defence node and has no children
# 2. is an Attack node and has a direct defended Defence node as child
# 3. is an Attack or Defence node and all child nodes are defended nodes
# 4. is an AndGate and at least one child node is defended
class IsDefendedAnalyser(Analyser):
    METADATA_KEY = "IS_DEFENDED"

    def analyse_tree(self, tree: ADTree):
        self._process_node(tree)

    def _process_node(self, node: Node):
        # Process children first (depth first traversal)
        for child_node in node.get_child_nodes():
            self._process_node(child_node)

        # Precompute useful counters
        total_children = len(node.get_child_nodes())
        total_defended_nodes = len(list(filter(IsDefendedAnalyser._is_defended_node, node.get_child_nodes())))

        # Check all scenarios
        is_defended = False

        # 1. is a Defence node and has no children
        if node.get_node_type() == NodeType.DEFENCE:
            if total_children == 0:
                is_defended = True

        # 2. is an Attack node and has a direct defended Defence node as child
        if node.get_node_type() == NodeType.ATTACK:
            defended_nodes = filter(IsDefendedAnalyser._is_defended_node, node.get_child_nodes())
            defended_defence_nodes = filter(IsDefendedAnalyser._is_defence_node, defended_nodes)
            if len(list(defended_defence_nodes)) > 0:
                is_defended = True

        # 3. is an Attack or Defence node and all child nodes are defended nodes
        if node.get_node_type() == NodeType.ATTACK or node.get_node_type() == NodeType.ATTACK:
            if total_defended_nodes == total_children and total_children > 0:
                is_defended = True

        # 4. is an AndGate and at least one child node is defended
        if node.get_node_type() == NodeType.AND_GATE:
            if total_defended_nodes > 0:
                is_defended = True

        node.add_metadata(IsDefendedAnalyser.METADATA_KEY, is_defended)

    @staticmethod
    def _is_defended_node(node: Node):
        return node.get_metadata(IsDefendedAnalyser.METADATA_KEY)

    @staticmethod
    def _is_defence_node(node: Node):
        return node.get_node_type() == NodeType.DEFENCE
