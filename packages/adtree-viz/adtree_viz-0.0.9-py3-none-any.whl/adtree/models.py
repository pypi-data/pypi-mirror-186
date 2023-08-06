from __future__ import annotations

import hashlib
from enum import Enum
from types import MappingProxyType
from typing import List


class NodeType(Enum):
    ATTACK = 1
    DEFENCE = 2
    AND_GATE = 3


class Node(object):
    def __init__(self,
                 node_type: NodeType = NodeType.ATTACK,
                 label: str = "",
                 reference_id: str = "",
                 child_nodes: List[Node] = None,
                 metadata: dict = MappingProxyType({})):
        self.node_type = node_type
        self.label = label
        self.reference_id = reference_id
        self.child_nodes = [] if child_nodes is None else child_nodes
        self.metadata = {} | metadata

    def get_id(self) -> str:
        return hashlib.md5(self.label.encode()).hexdigest()

    def get_reference_id(self) -> str:
        return self.reference_id

    def get_node_type(self) -> NodeType:
        return self.node_type

    def get_label(self) -> str:
        return self.label

    def get_child_nodes(self) -> List[Node]:
        return self.child_nodes

    def add_metadata(self, key, value):
        self.metadata[key] = value

    def get_metadata(self, key):
        return self.metadata[key] if key in self.metadata else None

    def has_metadata(self, key):
        return key in self.metadata

    def __repr__(self):
        return f"{self.__class__.__name__}:{self.label}"


class Attack(Node):
    def __init__(self, label: str = "", child_nodes: List[Node] = None):
        super().__init__(node_type=NodeType.ATTACK,
                         label=label,
                         child_nodes=child_nodes)


class Defence(Node):
    def __init__(self, label: str = "", child_nodes: List[Node] = None):
        super().__init__(node_type=NodeType.DEFENCE,
                         label=label,
                         child_nodes=child_nodes)


class AndGate(Node):
    def __init__(self, child_nodes: List[Node] = None):
        super().__init__(node_type=NodeType.AND_GATE,
                         label="AND",
                         child_nodes=child_nodes)

    def get_id(self) -> str:
        # Set ID as the hash of all children labels
        children_labels = ""
        for child_node in self.child_nodes:
            children_labels += child_node.get_label()
        return hashlib.md5(children_labels.encode()).hexdigest()


class ADTree(Node):
    def __init__(self, reference_id: str = "", root_node: Node = None):
        super().__init__(node_type=root_node.node_type,
                         label=root_node.label,
                         reference_id=reference_id,
                         child_nodes=root_node.child_nodes)


class ExternalADTree(Node):
    def __init__(self, reference_id: str = "", label: str = ""):
        super().__init__(node_type=NodeType.ATTACK,
                         label=label,
                         reference_id=reference_id)
