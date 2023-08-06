from __future__ import annotations

from graphviz import Graph

from adtree.models import Node, ADTree
from adtree.themes import Theme, NoFormatTheme


class Renderer(object):
    def __init__(self, theme: Theme = None, output_format: str = "png", view=False):
        self.theme = NoFormatTheme() if theme is None else theme
        self.output_format = output_format
        self.view = view
        self.references_to_expand = set()

    def render(self, tree: ADTree, subtrees_to_expand: list[ADTree] = None, filename: str = "attacktree-graph"):
        dot = Graph(graph_attr=self.theme.get_graph_attrs(tree),
                    format=self.output_format)
        dot.graph_attr["label"] = tree.get_reference_id() + " - " + tree.get_label()

        node_cache = set()
        references_to_expand = set()
        references_to_expand.add(tree.get_reference_id())
        if subtrees_to_expand is not None:
            for subtree in subtrees_to_expand:
                references_to_expand.add(subtree.get_reference_id())

        self._add_node(dot, tree, node_cache, references_to_expand)

        dot.render(filename, view=self.view)

    def _add_node(self, dot: Graph, current_node: Node, node_cache: set[str], references_to_expand: set[str]):
        node_attrs = self.theme.get_node_attrs_for(current_node)

        should_expand_node = True
        label = current_node.get_label()

        # Hide subtrees, unless explicitly told to expand
        if current_node.get_reference_id() != "" and \
                current_node.get_reference_id() not in references_to_expand:
            should_expand_node = False
            label += "\n(" + current_node.get_reference_id() + ")"

        dot.node(current_node.get_id(), label, **node_attrs)
        node_cache.add(current_node.get_id())

        if should_expand_node:
            for child_index, child_node in enumerate(current_node.get_child_nodes()):
                if child_node.get_id() not in node_cache:
                    self._add_node(dot, child_node, node_cache, references_to_expand)
                edge_attrs = self.theme.get_edge_attrs_for(current_node, child_node)
                dot.edge(current_node.get_id(), child_node.get_id(), **edge_attrs)
