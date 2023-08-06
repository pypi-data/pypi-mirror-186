from __future__ import annotations
from .parse import clean_content, get_macro_content, parse_title, replace_newcommands
from .card import Card, CardTagException, make_card


class Node:

    def __init__(self, name: str, depth: int, parent: Node) -> None:
        self.name = name
        self.depth = depth
        self.parent = parent
        self.children: list[Node] = list()
        self.cards: list[Card] = list()

    def add_child(self, node: Node) -> None:
        self.children.append(node)

    def __str__(self) -> str:
        return f"{self.name} | depth: {self.depth} | num children: {len(self.children)}"

    def __eq__(self, node: Node) -> bool:
        return self.__str__() == node.__str__()


class Root(Node):
    """Just to init the Tree. """

    def __init__(self) -> None:
        super().__init__("Root", -1, None)


class Tree:

    def __init__(self, root: Root) -> None:
        self.root = root
        self.nodes: list[Node] = list()
        self.structure = dict()
        self.recursive_tree_walk(root)
        self.make_structure(root)

    def recursive_tree_walk(self, node: Node) -> None:
        if len(node.children) == 0:
            return
        for child in node.children:
            self.nodes.append(child)
            self.recursive_tree_walk(child)

    def make_structure(self, root: Node) -> None:
        for node in self.nodes:
            current_node = node
            branch = list()
            while current_node.parent is not None:
                branch.append(current_node.name)
                current_node = current_node.parent
            branch = branch[::-1]
            current_location = self.structure
            for key in branch:
                if key in current_location:
                    current_location = current_location[key]
                else:
                    current_location[key] = dict()


class Source:

    """ Container for a single parsed .tex file. """

    def __init__(self, lines: list[str]) -> None:
        replace_newcommands(lines)
        self.lines = lines
        self.title = parse_title(lines)
        self.tree = self.parse_lines_to_tree()

    def parse_lines_to_tree(self) -> Tree:
        delimiters = [r"\part{", r"\section{", r"\subsection{", r"\subsubsection{"]
        root = Root()
        current_depth = -1
        current_node = root
        for i, line in enumerate(self.lines):
            for delimiter in delimiters:
                if delimiter in line:
                    name = clean_content(get_macro_content(line))
                    depth = delimiters.index(delimiter)
                    if depth > current_depth:
                        current_depth += 1
                        new_node = Node(name, current_depth, current_node)
                        current_node.add_child(new_node)
                    elif depth == current_depth:
                        new_node = Node(name, current_depth, current_node.parent)
                        current_node.parent.add_child(new_node)
                    elif depth < current_depth:
                        current_depth -= 1
                        current_node = current_node.parent
                        new_node = Node(name, current_depth, current_node.parent)
                        current_node.parent.add_child(new_node)
                    current_node = new_node
            if "% <BCT>" in line:
                title_start = i
                for j, subline in enumerate(self.lines[i:]):
                    if "% <ECT>" in subline:
                        title_end = title_start + j
                        break
                else:
                    raise CardTagException(title_start, "<ECT>")
                for j, subline in enumerate(self.lines[title_end:]):
                    if "% <BCC>" in subline:
                        content_start = title_end + j
                        break
                else:
                    raise CardTagException(title_start, "<BCC>")
                for j, subline in enumerate(self.lines[content_start:]):
                    if "% <ECC>" in subline:
                        content_end = content_start + j
                        break
                else:
                    raise CardTagException(title_start, "<ECC>")
                title_start += 1
                content_start += 1
                boundaries = (title_start, title_end, content_start, content_end)
                card: Card = make_card(self.lines, *boundaries)
                current_node.cards.append(card)
        return Tree(root)
