from __future__ import annotations
from pydantic import BaseModel, validator
from typing import Union, Optional, Dict, DefaultDict, List
from enum import Enum
from collections import defaultdict


class Level(Enum):
    ROOT = 0
    SOC = 1
    HLTG = 2
    HLT = 3
    LLT = 4

    def __add__(self, other: int) -> Union[Level, None]:
        if self.ROOT.value <= self.value + other <= self.LLT.value:
            return Level(self.value + other)
        else:
            return None

    def __lt__(self, other: Node) -> bool:
        return self.value < other.value

    def __le__(self, other: Node) -> bool:
        return self.value <= other.value

    def __gt__(self, other: Node) -> bool:
        return self.value > other.value

    def __ge__(self, other: Node) -> bool:
        return self.value >= other.value

    def __sub__(self, other: Node) -> int:
        return self.value - other.value


class Node(BaseModel):
    id: str
    term: str
    level: Level

    parent: Optional[Node] = None
    children: Dict[str, Node] = {}

    # maps for efficient nested children lookups
    id_to_nodes: Optional[DefaultDict[str, List[Node]]] = None
    term_to_nodes: Optional[DefaultDict[str, List[Node]]] = None

    def get_parent_at_level(self, target_level: Level) -> Union[Node, None]:
        # check if current node is deeper than target_level
        level_diff = target_level - self.level
        if level_diff > 0:
            return None
        else:
            node = self
            for _ in range(-level_diff):
                node = node.parent
            return node

    def get_children_at_level(self, target_level: Level) -> List[Node]:
        raise NotImplementedError

    def lookup_id(self, id: str) -> Union[List[Node], None]:
        # create lookup tables if they do not exists
        if self.id_to_nodes == None:
            self._set_lookup_tables()
        # lookup
        if id in self.id_to_nodes:
            return self.id_to_nodes[id]
        else:
            return None

    def lookup_term(self, term: str) -> Union[List[Node], None]:
        # create lookup tables if they do not exists
        if self.term_to_nodes == None:
            self._set_lookup_tables()
        # lookup
        if term in self.term_to_nodes:
            return self.term_to_nodes[term]
        else:
            return None

    def _set_lookup_tables(self) -> None:
        # get a flat list of all nodes
        self.term_to_nodes = defaultdict(list)
        self.id_to_nodes = defaultdict(list)

        # breadth-first traversal
        candidates = [self]
        while len(candidates):
            candidate = candidates.pop(0)
            # track nodes
            self.term_to_nodes[candidate.term].append(candidate)
            self.id_to_nodes[candidate.id].append(candidate)
            # add candidate's children to candidate list
            if candidate.children:
                candidates.extend(candidate.children.values())
        return None

    def __key(self):
        return (self.id, self.term, self.parent, len(self.children))

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other: Node) -> bool:
        # undeep equals operator, does not check children
        return self.__key() == other.__key()

    def __str__(self) -> str:
        return f"Node(id={self.id}, term={self.term}, level={self.level}, parent={self.parent.term if self.parent else None}, #children={len(self.children)})"

    def __repr__(self) -> str:
        return self.__str__()
