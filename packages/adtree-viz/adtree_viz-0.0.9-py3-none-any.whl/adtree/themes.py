from __future__ import annotations

from abc import ABC, abstractmethod

from adtree.analysers import IsDefendedAnalyser
from adtree.models import Node, NodeType, ADTree


class Theme(ABC):
    @abstractmethod
    def get_graph_attrs(self, tree: ADTree) -> dict:
        pass

    @abstractmethod
    def get_node_attrs_for(self, node: Node) -> dict:
        pass

    @abstractmethod
    def get_edge_attrs_for(self, node_parent: Node, node_child: Node) -> dict:
        pass


class NoFormatTheme(Theme):

    def get_graph_attrs(self, tree: ADTree):
        return {}

    def get_node_attrs_for(self, node: Node):
        return {}

    def get_edge_attrs_for(self, node_parent: Node, node_child: Node):
        return {}


class BaseTheme(Theme):

    def get_graph_attrs(self, tree: ADTree):
        return {
            "overlap": "False",
            "splines": "True",
            "nodesep": "0.2",
            "ranksep": "0.4",
            "labelloc": "t",
            "labeljust": "l",
        }

    def get_node_attrs_for(self, node: Node):
        return {
            "color": "#000000",
            "fillcolor": "#ffffff",
            "shape": "box",
            "style": "rounded",
            "fontname": "Arial",
            "margin": "0.2"
        }

    def get_edge_attrs_for(self, node_parent: Node, node_child: Node):
        base_attrs = {
            "fontname": "Arial",
            "color": "#1f1f1f",
            "style": "solid"
        }

        if (node_parent.get_node_type() == NodeType.ATTACK and node_child.get_node_type() == NodeType.DEFENCE) or \
                (node_parent.get_node_type() == NodeType.DEFENCE and node_child.get_node_type() == NodeType.ATTACK):
            return base_attrs | {
                "style": "dashed"
            }
        else:
            return base_attrs


class RedBlueFillTheme(BaseTheme):

    def get_node_attrs_for(self, node: Node):
        base_attrs = super().get_node_attrs_for(node) | {
            "shape": "plaintext",
            "style": "filled, rounded"
        }

        if node.get_node_type() == NodeType.ATTACK:
            return base_attrs | {
                "fillcolor": "#ff5c5c",
            }
        elif node.get_node_type() == NodeType.DEFENCE:
            return base_attrs | {
                "fillcolor": "#5cc1ff",
            }
        elif node.get_node_type() == NodeType.AND_GATE:
            return base_attrs | {
                "shape": "triangle",
                "color": "#ff5c5c",
                "fillcolor": "#ff5c5c",
                "margin": "0.05"
            }
        else:
            return base_attrs


class RedGreenOutlineTheme(BaseTheme):

    def get_node_attrs_for(self, node: Node):
        default_style = "filled, setlinewidth(3)"

        base_attrs = super().get_node_attrs_for(node) | {
            "color": "#000000",
            "fillcolor": "#ffffff",
            "margin": "0.1",
            "style": default_style,
        }

        # Process attr based on node types
        node_type_attrs = base_attrs
        if node.get_node_type() == NodeType.ATTACK:
            node_type_attrs |= {
                "shape": "ellipse",
                "color": "#ff5c5c",
                "style": default_style,
            }
        elif node.get_node_type() == NodeType.DEFENCE:
            node_type_attrs |= node_type_attrs | {
                "shape": "box",
                "color": "#27B011",
                "style": default_style,
            }
        elif node.get_node_type() == NodeType.AND_GATE:
            node_type_attrs |= node_type_attrs | {
                "shape": "triangle",
                "color": "#ff5c5c",
                "margin": "0.05",
                "style": "rounded, "+default_style,
            }

        # Process attr based on metadata
        metadata_attrs = node_type_attrs
        if node.has_metadata(IsDefendedAnalyser.METADATA_KEY):
            fillcolor = "#C8FFCB" if node.get_metadata(IsDefendedAnalyser.METADATA_KEY) else "#FFD3D6"
            metadata_attrs |= {
                "fillcolor": fillcolor,
            }
        return metadata_attrs
