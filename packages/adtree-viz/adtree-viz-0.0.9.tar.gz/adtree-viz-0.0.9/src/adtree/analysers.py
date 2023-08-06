from __future__ import annotations

from abc import ABC, abstractmethod

from adtree.models import ADTree, Node, NodeType


class Analyser(ABC):
    @abstractmethod
    def analyse_tree(self, tree: ADTree) -> ADTree:
        pass


# Traverse the tree and mark each nodes as either defended or undefended
# A node is considered defended if:
# - is a Defence node and has no Attack children
# - is an Attack node and all child nodes are defended nodes
# - is an AndGate and at least one child node is defended
class IsDefendedAnalyser(Analyser):
    METADATA_KEY = "IS_DEFENDED"

    def analyse_tree(self, tree: ADTree):
        self._process_node(tree)

    def _process_node(self, node: Node):
        # Process children first (depth first traversal)
        for child_node in node.get_child_nodes():
            self._process_node(child_node)

        # Count total children and total defended children
        total_children = len(node.get_child_nodes())
        total_defended = len(list(filter(IsDefendedAnalyser._is_node_defended, node.get_child_nodes())))
        # print(str(node) + " - " + str(total_defended) + "/" + str(total_children))

        # Handle child nodes
        is_defended = False
        if total_children == 0:
            if node.get_node_type() == NodeType.DEFENCE:
                is_defended = True
        else:
            # Handle the AND gate as a special case
            if node.get_node_type() == NodeType.AND_GATE:
                if total_defended > 0:
                    is_defended = True
            else:
                if total_defended == total_children:
                    is_defended = True

        node.add_metadata(IsDefendedAnalyser.METADATA_KEY, is_defended)

    @staticmethod
    def _is_node_defended(node: Node):
        return node.get_metadata(IsDefendedAnalyser.METADATA_KEY)
