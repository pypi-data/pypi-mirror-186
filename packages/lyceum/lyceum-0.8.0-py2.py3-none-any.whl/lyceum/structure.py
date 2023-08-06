"""Module relatif aux structures de données."""
import random
from collections import deque
from dataclasses import dataclass
from subprocess import SubprocessError
from typing import Any, Deque, Dict, Iterator, List, Optional, Tuple, Union

from pkg_resources import get_distribution


class Pile:
    """Classe représentant une pile"""

    def __init__(self):
        """On initialise la pile vide.

        L'attribut _data est de type list
        """
        self._data = []

    def empiler(self, élément):
        """Ajoute l'élément au sommet de la pile."""
        self._data.append(élément)

    def dépiler(self):
        """Retire l'élément au sommet de la pile et le renvoie."""
        return self._data.pop()

    def est_vide(self):
        """Renvoie `True` si la pile est vide et `False` sinon."""
        return not self._data

    def sommet(self):
        """Renvoie l'élément présent au sommet de la pile, et `None` si la pile est
        vide."""
        if self.est_vide():
            return None
        return self._data[-1]

    def __repr__(self):
        """Représente la pile verticalement"""
        # si la pile est vide on la dessine quand même
        if self.est_vide():
            N = 3
            txt = "|   | <- Sommet\n"
        else:
            # cherche la plus longue valeur de la pile
            N = 2 + max([len(str(x)) for x in self._data])
            txt = ""
            for i, e in enumerate(self._data[::-1]):
                txt += "|{:^{N}}|".format(str(e), N=N)
                if i == 0:
                    txt += " <- Sommet\n"
                else:
                    txt += "\n"
        # Tiret bas
        txt += chr(8254) * (N + 2)
        txt += "\n{:^{N}}\n".format("PILE", N=N + 2)
        return txt


class File:
    """Classe représentant une file"""

    def __init__(self):
        """On initialise la file vide.

        L'attribut _data est de type collections.deque
        """
        self._data = deque()

    def enfiler(self, élément):
        """Ajoute l'élément à la queue la file."""
        self._data.appendleft(élément)

    def défiler(self):
        """Retire l'élément à la tête de la file et le renvoie."""
        return self._data.pop()

    def est_vide(self):
        """Renvoie `True` si la file est vide et `False` sinon."""
        return not self._data

    def tête(self):
        """Renvoie l'élément présent à la tête de la file, et `None` si la file est
        vide."""
        if self.est_vide():
            return None
        return self._data[-1]

    def __repr__(self):
        """Représente la file horizontalement vers la droitee"""
        # cherche la plus longue valeur de la pile
        txt_0 = "Queue -> | "
        txt_1 = " | ".join([str(e) for e in self._data])
        txt_2 = " | -> Tête"

        # contours
        CONTOUR_UP = (
            " " * (len(txt_0) - 2) + "_" * (len(txt_1) + 4) + " " * (len(txt_2) - 2)
        )
        CONTOUR_DOWN = (
            " " * (len(txt_0) - 2)
            + chr(8254) * (len(txt_1) + 4)
            + " " * (len(txt_2) - 2)
        )

        # Affiche FILE au milieu en dessous
        LABEL = "\n{:^{N}}\n".format("FILE", N=len(CONTOUR_DOWN))
        return CONTOUR_UP + "\n" + txt_0 + txt_1 + txt_2 + "\n" + CONTOUR_DOWN + LABEL


# Arbres binaires
# Code adapté de binarytree https://github.com/joowani/binarytree sous licence MIT
""" binarytree en un module basé sur mon commit svg

https://github.com/joowani/binarytree/commit/9ad3616ff61b1cc0c58e126ebe38841045787431
"""


class BinaryTreeError(Exception):
    """Base (catch-all) binarytree exception."""


class ArbreBinaireIndexError(BinaryTreeError):
    """ArbreBinaire index was invalid."""


class ArbreBinaireModifyError(BinaryTreeError):
    """User tried to overwrite or delete the root node."""


class ArbreBinaireNotFoundError(BinaryTreeError):
    """ArbreBinaire was missing from the binary tree."""


class ArbreBinaireReferenceError(BinaryTreeError):
    """ArbreBinaire reference was invalid (e.g. cyclic reference)."""


class ArbreBinaireTypeError(BinaryTreeError):
    """ArbreBinaire was not an instance of :class:`ArbreBinaire`."""


class ArbreBinaireValeurError(BinaryTreeError):
    """ArbreBinaire valeur was not a number (e.g. int, float)."""


class TreeHeightError(BinaryTreeError):
    """Tree height was invalid."""


class GraphvizImportError(BinaryTreeError):
    """graphviz module is not installed"""


""" Module containing layout related algorithms."""
from typing import List, Tuple, Union


def _get_coords(
    valeurs: List[Union[float, int, None]]
) -> Tuple[
    List[Tuple[int, int, Union[float, int, None]]], List[Tuple[int, int, int, int]]
]:
    """Generate the coordinates used for rendering the nodes and edges.

    node and edges are stored as tuples in the form node: (x, y, label) and
    edge: (x1, y1, x2, y2)

    Each coordinate is relative y is the depth, x is the position of the node
    on a level from gauche to droite 0 to 2**depth -1

    :param valeurs: Valeurs of the binary tree.
    :type valeurs: list of ints
    :return: nodes and edges list
    :rtype: two lists of tuples

    """
    x = 0
    y = 0
    nodes = []
    edges = []

    # root node
    nodes.append((x, y, valeurs[0]))
    # append other nodes and their edges
    y += 1
    for valeur in valeurs[1:]:
        if valeur is not None:
            nodes.append((x, y, valeur))
            edges.append((x // 2, y - 1, x, y))
        x += 1
        # check if level is full
        if x == 2**y:
            x = 0
            y += 1
    return nodes, edges


def generate_svg(valeurs: List[Union[float, int, None]]) -> str:
    """Generate a svg image from a binary tree

    A simple layout is used based on a perfect tree of same height in which all
    leaves would be regularly spaced.

    :param valeurs: Valeurs of the binary tree.
    :type valeurs: list of ints
    :return: the svg image of the tree.
    :rtype: str
    """
    node_size = 16.0
    stroke_width = 1.5
    gutter = 0.5
    x_scale = (2 + gutter) * node_size
    y_scale = 3.0 * node_size

    # retrieve relative coordinates
    nodes, edges = _get_coords(valeurs)
    y_min = min([n[1] for n in nodes])
    y_max = max([n[1] for n in nodes])

    # generate the svg string
    svg = f"""
    <svg width="{x_scale * 2**y_max}" height="{y_scale * (2 + y_max)}"
         xmlns="http://www.w3.org/2000/svg">
        <style>
            .bt-label {{
                font: 300 {node_size}px sans-serif;;
                text-align: center;
                dominant-baseline: middle;
                text-anchor: middle;
            }}
            .bt-node {{
                fill: lightgray;
                stroke-width: {stroke_width};
            }}

        </style>
        <g stroke="#111">
    """
    # scales

    def scalex(x: int, y: int) -> float:
        depth = y_max - y
        # offset
        x = 2 ** (depth + 1) * x + 2**depth - 1
        return 1 + node_size + x_scale * x / 2

    def scaley(y: int) -> float:
        return float(y_scale * (1 + y - y_min))

    # edges
    def svg_edge(x1: float, y1: float, x2: float, y2: float) -> str:
        """Generate svg code for an edge"""
        return f"""<line x1="{x1}" x2="{x2}" y1="{y1}" y2="{y2}"/>"""

    for a in edges:
        x1, y1, x2, y2 = a
        svg += svg_edge(scalex(x1, y1), scaley(y1), scalex(x2, y2), scaley(y2))

    # nodes
    def svg_node(x: float, y: float, label: str = "") -> str:
        """Generate svg code for a node and his label"""
        return f"""
            <circle class="bt-node" cx="{x}" cy="{y}" r="{node_size}"/>
            <text class="bt-label" x="{x}" y="{y}">{label}</text>"""

    for n in nodes:
        x, y, label = n
        svg += svg_node(scalex(x, y), scaley(y), str(label))

    svg += "</g></svg>"
    return svg


import heapq
import random
from dataclasses import dataclass
from typing import Any, Dict, Iterator, List, Optional, Tuple, Union

from pkg_resources import get_distribution

gauche_FIELD = "gauche"
droite_FIELD = "droite"
VAL_FIELDS = ("val", "valeur", "étiquette")

ArbreBinaireValeur = Union[float, int]


@dataclass
class ArbreBinaireProperties:
    height: int
    size: int
    is_max_heap: bool
    is_min_heap: bool
    is_perfect: bool
    is_strict: bool
    is_complete: bool
    leaf_count: int
    min_node_valeur: ArbreBinaireValeur
    max_node_valeur: ArbreBinaireValeur
    min_leaf_depth: int
    max_leaf_depth: int


class ArbreBinaire:
    """Represents a binary tree node.

    This class provides methods and properties for managing the current node,
    and the binary tree in which the node is the root. When a docstring in
    this class mentions "binary tree", it is referring to the current node and
    its descendants.

    :param valeur(alias: val et étiquette): ArbreBinaire valeur (must be a number or str).
    :type valeur: int | float
    :param gauche: gauche child node (default: None).
    :type gauche: ArbreBinaire | None
    :param droite: droite child node (default: None).
    :type droite: ArbreBinaire | None
    :raise binarytree.exceptions.ArbreBinaireTypeError: If gauche or droite child node is
        not an instance of :class:`ArbreBinaire`.
    :raise binarytree.exceptions.ArbreBinaireValeurError: If node valeur is not an int or float.
    """

    def __init__(
        self,
        valeur: ArbreBinaireValeur,
        gauche: Optional["ArbreBinaire"] = None,
        droite: Optional["ArbreBinaire"] = None,
    ) -> None:
        self.valeur = self.val = self.étiquette = valeur
        self.gauche = gauche
        self.droite = droite

        if not isinstance(valeur, (float, int, str)):
            raise ArbreBinaireValeurError("node valeur must be a float or int or str")

        if gauche is not None and not isinstance(gauche, ArbreBinaire):
            raise ArbreBinaireTypeError("gauche child must be a ArbreBinaire instance")

        if droite is not None and not isinstance(droite, ArbreBinaire):
            raise ArbreBinaireTypeError("droite child must be a ArbreBinaire instance")

    def __repr__(self) -> str:
        """Return the string representation of the current node.

        :return: String representation.
        :rtype: str

        **Example**:

        .. doctest::

            >>> from binarytree import ArbreBinaire
            >>>
            >>> ArbreBinaire(1)
            ArbreBinaire(1)
        """
        return "ArbreBinaire({})".format(self.val)

    def __str__(self) -> str:
        """Return the pretty-print string for the binary tree.

        :return: Pretty-print string.
        :rtype: str

        **Example**:

        .. doctest::

            >>> from binarytree import ArbreBinaire
            >>>
            >>> root = ArbreBinaire(1)
            >>> root.gauche = ArbreBinaire(2)
            >>> root.droite = ArbreBinaire(3)
            >>> root.gauche.droite = ArbreBinaire(4)
            >>>
            >>> print(root)
            <BLANKLINE>
              __1
             /   \\
            2     3
             \\
              4
            <BLANKLINE>

        .. note::
            To include level-order_ indexes in the output string, use
            :func:`ArbreBinaire.pprint` instead.

        .. _level-order:
            https://en.wikipedia.org/wiki/Tree_traversal#Breadth-first_search
        """
        lines = _build_tree_string(self, 0, False, "-")[0]
        return "\n" + "\n".join((line.rstrip() for line in lines))

    def __setattr__(self, attr: str, obj: Any) -> None:
        """Modified version of ``__setattr__`` with extra sanity checking.

        Class attributes **gauche**, **droite** and **valeur** are validated.

        :param attr: Name of the class attribute.
        :type attr: str
        :param obj: Object to set.
        :type obj: object
        :raise binarytree.exceptions.ArbreBinaireTypeError: If gauche or droite child is
            not an instance of :class:`ArbreBinaire`.
        :raise binarytree.exceptions.ArbreBinaireValeurError: If node valeur is not a
            number (e.g. int, float, str).

        **Example**:

        .. doctest::

            >>> from binarytree import ArbreBinaire
            >>>
            >>> node = ArbreBinaire(1)
            >>> node.gauche = 'invalid'  # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
             ...
            ArbreBinaireTypeError: gauche child must be a ArbreBinaire instance

        .. doctest::

            >>> from binarytree import ArbreBinaire
            >>>
            >>> node = ArbreBinaire(1)
            >>> node.val = 'invalid'  # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
             ...
            ArbreBinaireValeurError: node valeur must be a float or int or str
        """
        if attr == gauche_FIELD:
            if obj is not None and not isinstance(obj, ArbreBinaire):
                raise ArbreBinaireTypeError(
                    "gauche child must be a ArbreBinaire instance"
                )
        elif attr == droite_FIELD:
            if obj is not None and not isinstance(obj, ArbreBinaire):
                raise ArbreBinaireTypeError(
                    "droite child must be a ArbreBinaire instance"
                )
        elif attr in VAL_FIELDS:
            if not isinstance(obj, (float, int, str)):
                raise ArbreBinaireValeurError(
                    "node valeur must be a float or int or str"
                )
            # On met à jour tous les attributs
            # TODO Est-ce une bonne idée? ou doit-on imposer une API plus stricte?
            for attr in VAL_FIELDS:
                object.__setattr__(self, attr, obj)

        object.__setattr__(self, attr, obj)

    def __iter__(self) -> Iterator["ArbreBinaire"]:
        """Iterate through the nodes in the binary tree in level-order_.

        .. _level-order:
            https://en.wikipedia.org/wiki/Tree_traversal#Breadth-first_search

        :return: ArbreBinaire iterator.
        :rtype: Iterator[ArbreBinaire]

        **Example**:

        .. doctest::

            >>> from binarytree import ArbreBinaire
            >>>
            >>> root = ArbreBinaire(1)
            >>> root.gauche = ArbreBinaire(2)
            >>> root.droite = ArbreBinaire(3)
            >>> root.gauche.gauche = ArbreBinaire(4)
            >>> root.gauche.droite = ArbreBinaire(5)
            >>>
            >>> print(root)
            <BLANKLINE>
                __1
               /   \\
              2     3
             / \\
            4   5
            <BLANKLINE>
            >>> list(root)
            [ArbreBinaire(1), ArbreBinaire(2), ArbreBinaire(3), ArbreBinaire(4), ArbreBinaire(5)]
        """
        current_level = [self]

        while len(current_level) > 0:
            next_level = []
            for node in current_level:
                yield node
                if node.gauche is not None:
                    next_level.append(node.gauche)
                if node.droite is not None:
                    next_level.append(node.droite)
            current_level = next_level

    def __len__(self) -> int:
        """Return the total number of nodes in the binary tree.

        :return: Total number of nodes.
        :rtype: int

        **Example**:

        .. doctest::

            >>> from binarytree import ArbreBinaire
            >>>
            >>> root = ArbreBinaire(1)
            >>> root.gauche = ArbreBinaire(2)
            >>> root.droite = ArbreBinaire(3)
            >>>
            >>> len(root)
            3

        .. note::
            This method is equivalent to :attr:`ArbreBinaire.size`.
        """
        return sum(1 for _ in iter(self))

    def __getitem__(self, index: int) -> "ArbreBinaire":
        """Return the node (or subtree) at the given level-order_ index.

        .. _level-order:
            https://en.wikipedia.org/wiki/Tree_traversal#Breadth-first_search

        :param index: Level-order index of the node.
        :type index: int
        :return: ArbreBinaire (or subtree) at the given index.
        :rtype: ArbreBinaire
        :raise binarytree.exceptions.ArbreBinaireIndexError: If node index is invalid.
        :raise binarytree.exceptions.ArbreBinaireNotFoundError: If the node is missing.

        **Example**:

        .. doctest::

            >>> from binarytree import ArbreBinaire
            >>>
            >>> root = ArbreBinaire(1)       # index: 0, valeur: 1
            >>> root.gauche = ArbreBinaire(2)  # index: 1, valeur: 2
            >>> root.droite = ArbreBinaire(3) # index: 2, valeur: 3
            >>>
            >>> root[0]
            ArbreBinaire(1)
            >>> root[1]
            ArbreBinaire(2)
            >>> root[2]
            ArbreBinaire(3)
            >>> root[3]  # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
             ...
            ArbreBinaireNotFoundError: node missing at index 3
        """
        if not isinstance(index, int) or index < 0:
            raise ArbreBinaireIndexError("node index must be a non-negative int")

        current_level: List[Optional[ArbreBinaire]] = [self]
        current_index = 0
        has_more_nodes = True

        while has_more_nodes:
            has_more_nodes = False
            next_level: List[Optional[ArbreBinaire]] = []

            for node in current_level:
                if current_index == index:
                    if node is None:
                        break
                    else:
                        return node
                current_index += 1

                if node is None:
                    next_level.append(None)
                    next_level.append(None)
                    continue
                next_level.append(node.gauche)
                next_level.append(node.droite)
                if node.gauche is not None or node.droite is not None:
                    has_more_nodes = True

            current_level = next_level

        raise ArbreBinaireNotFoundError("node missing at index {}".format(index))

    def __setitem__(self, index: int, node: "ArbreBinaire") -> None:
        """Insert a node (or subtree) at the given level-order_ index.

        * An exception is raised if the parent node is missing.
        * Any existing node or subtree is overwritten.
        * Root node (current node) cannot be replaced.

        .. _level-order:
            https://en.wikipedia.org/wiki/Tree_traversal#Breadth-first_search

        :param index: Level-order index of the node.
        :type index: int
        :param node: ArbreBinaire to insert.
        :type node: ArbreBinaire
        :raise binarytree.exceptions.ArbreBinaireTypeError: If new node is not an
            instance of :class:`ArbreBinaire`.
        :raise binarytree.exceptions.ArbreBinaireNotFoundError: If parent is missing.
        :raise binarytree.exceptions.ArbreBinaireModifyError: If user attempts to
            overwrite the root node (current node).

        **Example**:

        .. doctest::

            >>> from binarytree import ArbreBinaire
            >>>
            >>> root = ArbreBinaire(1)       # index: 0, valeur: 1
            >>> root.gauche = ArbreBinaire(2)  # index: 1, valeur: 2
            >>> root.droite = ArbreBinaire(3) # index: 2, valeur: 3
            >>>
            >>> root[0] = ArbreBinaire(4)  # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
             ...
            ArbreBinaireModifyError: cannot modify the root node

        .. doctest::

            >>> from binarytree import ArbreBinaire
            >>>
            >>> root = ArbreBinaire(1)       # index: 0, valeur: 1
            >>> root.gauche = ArbreBinaire(2)  # index: 1, valeur: 2
            >>> root.droite = ArbreBinaire(3) # index: 2, valeur: 3
            >>>
            >>> root[11] = ArbreBinaire(4)  # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
             ...
            ArbreBinaireNotFoundError: parent node missing at index 5

        .. doctest::

            >>> from binarytree import ArbreBinaire
            >>>
            >>> root = ArbreBinaire(1)       # index: 0, valeur: 1
            >>> root.gauche = ArbreBinaire(2)  # index: 1, valeur: 2
            >>> root.droite = ArbreBinaire(3) # index: 2, valeur: 3
            >>>
            >>> root[1] = ArbreBinaire(4)
            >>>
            >>> root.gauche
            ArbreBinaire(4)
        """
        if index == 0:
            raise ArbreBinaireModifyError("cannot modify the root node")

        parent_index = (index - 1) // 2
        try:
            parent = self.__getitem__(parent_index)
        except ArbreBinaireNotFoundError:
            raise ArbreBinaireNotFoundError(
                "parent node missing at index {}".format(parent_index)
            )

        setattr(parent, gauche_FIELD if index % 2 else droite_FIELD, node)

    def __delitem__(self, index: int) -> None:
        """Remove the node (or subtree) at the given level-order_ index.

        * An exception is raised if the target node is missing.
        * The descendants of the target node (if any) are also removed.
        * Root node (current node) cannot be deleted.

        .. _level-order:
            https://en.wikipedia.org/wiki/Tree_traversal#Breadth-first_search

        :param index: Level-order index of the node.
        :type index: int
        :raise binarytree.exceptions.ArbreBinaireNotFoundError: If the target node or
            its parent is missing.
        :raise binarytree.exceptions.ArbreBinaireModifyError: If user attempts to
            delete the root node (current node).

        **Example**:

        .. doctest::

            >>> from binarytree import ArbreBinaire
            >>>
            >>> root = ArbreBinaire(1)          # index: 0, valeur: 1
            >>> root.gauche = ArbreBinaire(2)     # index: 1, valeur: 2
            >>> root.droite = ArbreBinaire(3)    # index: 2, valeur: 3
            >>>
            >>> del root[0]  # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
             ...
            ArbreBinaireModifyError: cannot delete the root node

        .. doctest::

            >>> from binarytree import ArbreBinaire
            >>>
            >>> root = ArbreBinaire(1)          # index: 0, valeur: 1
            >>> root.gauche = ArbreBinaire(2)     # index: 1, valeur: 2
            >>> root.droite = ArbreBinaire(3)    # index: 2, valeur: 3
            >>>
            >>> del root[2]
            >>>
            >>> root[2]  # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
             ...
            ArbreBinaireNotFoundError: node missing at index 2
        """
        if index == 0:
            raise ArbreBinaireModifyError("cannot delete the root node")

        parent_index = (index - 1) // 2
        try:
            parent = self.__getitem__(parent_index)
        except ArbreBinaireNotFoundError:
            raise ArbreBinaireNotFoundError(
                "no node to delete at index {}".format(index)
            )

        child_attr = gauche_FIELD if index % 2 == 1 else droite_FIELD
        if getattr(parent, child_attr) is None:
            raise ArbreBinaireNotFoundError(
                "no node to delete at index {}".format(index)
            )

        setattr(parent, child_attr, None)

    def _repr_svg_(self) -> str:
        """Display the binary tree in svg (used for `Jupyter notebooks`_).

        .. _Jupyter notebooks: https://jupyter.org
        """
        return generate_svg(self.valeurs)  # pragma: no cover

    def pprint(self, index: bool = False, delimiter: str = "-") -> None:
        """Pretty-print the binary tree.

        :param index: If set to True (default: False), display level-order_
            indexes using the format: ``{index}{delimiter}{valeur}``.
        :type index: bool
        :param delimiter: Delimiter character between the node index and
            the node valeur (default: '-').
        :type delimiter: str

        **Example**:

        .. doctest::

            >>> from binarytree import ArbreBinaire
            >>>
            >>> root = ArbreBinaire(1)              # index: 0, valeur: 1
            >>> root.gauche = ArbreBinaire(2)         # index: 1, valeur: 2
            >>> root.droite = ArbreBinaire(3)        # index: 2, valeur: 3
            >>> root.gauche.droite = ArbreBinaire(4)   # index: 4, valeur: 4
            >>>
            >>> root.pprint()
            <BLANKLINE>
              __1
             /   \\
            2     3
             \\
              4
            <BLANKLINE>
            >>> root.pprint(index=True)     # Format: {index}-{valeur}
            <BLANKLINE>
               _____0-1_
              /         \\
            1-2_        2-3
                \\
                4-4
            <BLANKLINE>

        .. note::
            If you do not need level-order_ indexes in the output string, use
            :func:`ArbreBinaire.__str__` instead.

        .. _level-order:
            https://en.wikipedia.org/wiki/Tree_traversal#Breadth-first_search
        """
        lines = _build_tree_string(self, 0, index, delimiter)[0]
        print("\n" + "\n".join((line.rstrip() for line in lines)))

    def validate(self) -> None:
        """Check if the binary tree is malformed.

        :raise binarytree.exceptions.ArbreBinaireReferenceError: If there is a
            cyclic reference to a node in the binary tree.
        :raise binarytree.exceptions.ArbreBinaireTypeError: If a node is not an
            instance of :class:`ArbreBinaire`.
        :raise binarytree.exceptions.ArbreBinaireValeurError: If a node valeur is not a
            number (e.g. int, float) or str.

        **Example**:

        .. doctest::

            >>> from binarytree import ArbreBinaire
            >>>
            >>> root = ArbreBinaire(1)
            >>> root.gauche = ArbreBinaire(2)
            >>> root.droite = root  # Cyclic reference to root
            >>>
            >>> root.validate()  # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
             ...
            ArbreBinaireReferenceError: cyclic node reference at index 0
        """
        has_more_nodes = True
        visited = set()
        to_visit: List[Optional[ArbreBinaire]] = [self]
        index = 0

        while has_more_nodes:
            has_more_nodes = False
            next_level: List[Optional[ArbreBinaire]] = []

            for node in to_visit:
                if node is None:
                    next_level.append(None)
                    next_level.append(None)
                else:
                    if node in visited:
                        raise ArbreBinaireReferenceError(
                            f"cyclic reference at ArbreBinaire({node.val}) "
                            + f"(level-order index {index})"
                        )
                    if not isinstance(node, ArbreBinaire):
                        raise ArbreBinaireTypeError(
                            "invalid node instance at index {}".format(index)
                        )
                    if not isinstance(node.val, (float, int, str)):
                        raise ArbreBinaireValeurError(
                            "invalid node valeur at index {}".format(index)
                        )
                    if not isinstance(node.valeur, (float, int, str)):
                        raise ArbreBinaireValeurError(
                            "invalid node valeur at index {}".format(index)
                        )
                    if node.gauche is not None or node.droite is not None:
                        has_more_nodes = True

                    visited.add(node)
                    next_level.append(node.gauche)
                    next_level.append(node.droite)

                index += 1

            to_visit = next_level

    @property
    def valeurs(self) -> List[Optional[ArbreBinaireValeur]]:
        """Return the `list representation`_ of the binary tree.

        .. _list representation:
            https://en.wikipedia.org/wiki/Binary_tree#Arrays

        :return: List representation of the binary tree, which is a list of
            node valeurs in breadth-first order starting from the root (current
            node). If a node is at index i, its gauche child is always at 2i + 1,
            droite child at 2i + 2, and parent at index floor((i - 1) / 2). None
            indicates absence of a node at that index. See example below for an
            illustration.
        :rtype: [float | int | None]

        **Example**:

        .. doctest::

            >>> from binarytree import ArbreBinaire
            >>>
            >>> root = ArbreBinaire(1)
            >>> root.gauche = ArbreBinaire(2)
            >>> root.droite = ArbreBinaire(3)
            >>> root.gauche.droite = ArbreBinaire(4)
            >>>
            >>> root.valeurs
            [1, 2, 3, None, 4]
        """
        current_level: List[Optional[ArbreBinaire]] = [self]
        has_more_nodes = True
        valeurs: List[Optional[ArbreBinaireValeur]] = []

        while has_more_nodes:
            has_more_nodes = False
            next_level: List[Optional[ArbreBinaire]] = []

            for node in current_level:
                if node is None:
                    valeurs.append(None)
                    next_level.append(None)
                    next_level.append(None)
                    continue

                if node.gauche is not None or node.droite is not None:
                    has_more_nodes = True

                valeurs.append(node.val)
                next_level.append(node.gauche)
                next_level.append(node.droite)

            current_level = next_level

        # Get rid of trailing None valeurs
        while valeurs and valeurs[-1] is None:
            valeurs.pop()

        return valeurs

    @property
    def leaves(self) -> List["ArbreBinaire"]:
        """Return the leaf nodes of the binary tree.

        A leaf node is any node that does not have child nodes.

        :return: List of leaf nodes.
        :rtype: [ArbreBinaire]

        **Example**:

        .. doctest::

            >>> from binarytree import ArbreBinaire
            >>>
            >>> root = ArbreBinaire(1)
            >>> root.gauche = ArbreBinaire(2)
            >>> root.droite = ArbreBinaire(3)
            >>> root.gauche.droite = ArbreBinaire(4)
            >>>
            >>> print(root)
            <BLANKLINE>
              __1
             /   \\
            2     3
             \\
              4
            <BLANKLINE>
            >>> root.leaves
            [ArbreBinaire(3), ArbreBinaire(4)]
        """
        current_level = [self]
        leaves = []

        while len(current_level) > 0:
            next_level = []
            for node in current_level:
                if node.gauche is None and node.droite is None:
                    leaves.append(node)
                    continue
                if node.gauche is not None:
                    next_level.append(node.gauche)
                if node.droite is not None:
                    next_level.append(node.droite)
            current_level = next_level
        return leaves

    @property
    def levels(self) -> List[List["ArbreBinaire"]]:
        """Return the nodes in the binary tree level by level.

        :return: Lists of nodes level by level.
        :rtype: [[ArbreBinaire]]

        **Example**:

        .. doctest::

            >>> from binarytree import ArbreBinaire
            >>>
            >>> root = ArbreBinaire(1)
            >>> root.gauche = ArbreBinaire(2)
            >>> root.droite = ArbreBinaire(3)
            >>> root.gauche.droite = ArbreBinaire(4)
            >>>
            >>> print(root)
            <BLANKLINE>
              __1
             /   \\
            2     3
             \\
              4
            <BLANKLINE>
            >>>
            >>> root.levels
            [[ArbreBinaire(1)], [ArbreBinaire(2), ArbreBinaire(3)], [ArbreBinaire(4)]]
        """
        current_level = [self]
        levels = []

        while len(current_level) > 0:
            next_level = []
            for node in current_level:
                if node.gauche is not None:
                    next_level.append(node.gauche)
                if node.droite is not None:
                    next_level.append(node.droite)
            levels.append(current_level)
            current_level = next_level
        return levels

    @property
    def height(self) -> int:
        """Return the height of the binary tree.

        Height of a binary tree is the number of edges on the longest path
        between the root node and a leaf node. Binary tree with just a single
        node has a height of 0.

        :return: Height of the binary tree.
        :rtype: int

        **Example**:

        .. doctest::

            >>> from binarytree import ArbreBinaire
            >>>
            >>> root = ArbreBinaire(1)
            >>> root.gauche = ArbreBinaire(2)
            >>> root.gauche.gauche = ArbreBinaire(3)
            >>>
            >>> print(root)
            <BLANKLINE>
                1
               /
              2
             /
            3
            <BLANKLINE>
            >>> root.height
            2

        .. note::
            A binary tree with only a root node has a height of 0.
        """
        return _get_tree_properties(self).height

    @property
    def size(self) -> int:
        """Return the total number of nodes in the binary tree.

        :return: Total number of nodes.
        :rtype: int

        **Example**:

        .. doctest::

            >>> from binarytree import ArbreBinaire
            >>>
            >>> root = ArbreBinaire(1)
            >>> root.gauche = ArbreBinaire(2)
            >>> root.droite = ArbreBinaire(3)
            >>> root.gauche.droite = ArbreBinaire(4)
            >>>
            >>> root.size
            4

        .. note::
            This method is equivalent to :func:`ArbreBinaire.__len__`.
        """
        return self.__len__()

    @property
    def leaf_count(self) -> int:
        """Return the total number of leaf nodes in the binary tree.

        A leaf node is a node with no child nodes.

        :return: Total number of leaf nodes.
        :rtype: int

        **Example**:

        .. doctest::

            >>> from binarytree import ArbreBinaire
            >>>
            >>> root = ArbreBinaire(1)
            >>> root.gauche = ArbreBinaire(2)
            >>> root.droite = ArbreBinaire(3)
            >>> root.gauche.droite = ArbreBinaire(4)
            >>>
            >>> root.leaf_count
            2
        """
        return _get_tree_properties(self).leaf_count

    @property
    def is_balanced(self) -> bool:
        """Check if the binary tree is height-balanced.

        A binary tree is height-balanced if it meets the following criteria:

        * gauche subtree is height-balanced.
        * droite subtree is height-balanced.
        * The difference between heights of gauche and droite subtrees is no more
          than 1.
        * An empty binary tree is always height-balanced.

        :return: True if the binary tree is balanced, False otherwise.
        :rtype: bool

        **Example**:

        .. doctest::

            >>> from binarytree import ArbreBinaire
            >>>
            >>> root = ArbreBinaire(1)
            >>> root.gauche = ArbreBinaire(2)
            >>> root.gauche.gauche = ArbreBinaire(3)
            >>>
            >>> print(root)
            <BLANKLINE>
                1
               /
              2
             /
            3
            <BLANKLINE>
            >>> root.is_balanced
            False
        """
        return _is_balanced(self) >= 0

    @property
    def is_abr(self) -> bool:
        """Check if the binary tree is a ABR_ (binary search tree).

        :return: True if the binary tree is a ABR_, False otherwise.
        :rtype: bool

        .. _ABR: https://en.wikipedia.org/wiki/Binary_search_tree

        **Example**:

        .. doctest::

            >>> from binarytree import ArbreBinaire
            >>>
            >>> root = ArbreBinaire(2)
            >>> root.gauche = ArbreBinaire(1)
            >>> root.droite = ArbreBinaire(3)
            >>>
            >>> print(root)
            <BLANKLINE>
              2
             / \\
            1   3
            <BLANKLINE>
            >>> root.is_abr
            True
        """
        return _is_abr(self)

    @property
    def is_symmetric(self) -> bool:
        """Check if the binary tree is symmetric.

        A binary tree is symmetric if it meets the following criteria:

        * gauche subtree is a mirror of the droite subtree about the root node.

        :return: True if the binary tree is a symmetric, False otherwise.
        :rtype: bool

        **Example**:

        .. doctest::

            >>> from binarytree import ArbreBinaire
            >>>
            >>> root = ArbreBinaire(1)
            >>> root.gauche = ArbreBinaire(2)
            >>> root.droite = ArbreBinaire(2)
            >>> root.gauche.gauche = ArbreBinaire(3)
            >>> root.gauche.droite = ArbreBinaire(4)
            >>> root.droite.gauche = ArbreBinaire(4)
            >>> root.droite.droite = ArbreBinaire(3)
            >>>
            >>> print(root)
            <BLANKLINE>
                __1__
               /     \\
              2       2
             / \\     / \\
            3   4   4   3
            <BLANKLINE>
            >>> root.is_symmetric
            True
        """
        return _is_symmetric(self)

    @property
    def is_max_heap(self) -> bool:
        """Check if the binary tree is a `max heap`_.

        :return: True if the binary tree is a `max heap`_, False otherwise.
        :rtype: bool

        .. _max heap: https://en.wikipedia.org/wiki/Min-max_heap

        **Example**:

        .. doctest::

            >>> from binarytree import ArbreBinaire
            >>>
            >>> root = ArbreBinaire(3)
            >>> root.gauche = ArbreBinaire(1)
            >>> root.droite = ArbreBinaire(2)
            >>>
            >>> print(root)
            <BLANKLINE>
              3
             / \\
            1   2
            <BLANKLINE>
            >>> root.is_max_heap
            True
        """
        return _get_tree_properties(self).is_max_heap

    @property
    def is_min_heap(self) -> bool:
        """Check if the binary tree is a `min heap`_.

        :return: True if the binary tree is a `min heap`_, False otherwise.
        :rtype: bool

        .. _min heap: https://en.wikipedia.org/wiki/Min-max_heap

        **Example**:

        .. doctest::

            >>> from binarytree import ArbreBinaire
            >>>
            >>> root = ArbreBinaire(1)
            >>> root.gauche = ArbreBinaire(2)
            >>> root.droite = ArbreBinaire(3)
            >>>
            >>> print(root)
            <BLANKLINE>
              1
             / \\
            2   3
            <BLANKLINE>
            >>> root.is_min_heap
            True
        """
        return _get_tree_properties(self).is_min_heap

    @property
    def is_perfect(self) -> bool:
        """Check if the binary tree is perfect.

        A binary tree is perfect if all its levels are completely filled. See
        example below for an illustration.

        :return: True if the binary tree is perfect, False otherwise.
        :rtype: bool

        **Example**:

        .. doctest::

            >>> from binarytree import ArbreBinaire
            >>>
            >>> root = ArbreBinaire(1)
            >>> root.gauche = ArbreBinaire(2)
            >>> root.droite = ArbreBinaire(3)
            >>> root.gauche.gauche = ArbreBinaire(4)
            >>> root.gauche.droite = ArbreBinaire(5)
            >>> root.droite.gauche = ArbreBinaire(6)
            >>> root.droite.droite = ArbreBinaire(7)
            >>>
            >>> print(root)
            <BLANKLINE>
                __1__
               /     \\
              2       3
             / \\     / \\
            4   5   6   7
            <BLANKLINE>
            >>> root.is_perfect
            True
        """
        return _get_tree_properties(self).is_perfect

    @property
    def is_strict(self) -> bool:
        """Check if the binary tree is strict.

        A binary tree is strict if all its non-leaf nodes have both the gauche
        and droite child nodes.

        :return: True if the binary tree is strict, False otherwise.
        :rtype: bool

        **Example**:

        .. doctest::

            >>> from binarytree import ArbreBinaire
            >>>
            >>> root = ArbreBinaire(1)
            >>> root.gauche = ArbreBinaire(2)
            >>> root.droite = ArbreBinaire(3)
            >>> root.gauche.gauche = ArbreBinaire(4)
            >>> root.gauche.droite = ArbreBinaire(5)
            >>>
            >>> print(root)
            <BLANKLINE>
                __1
               /   \\
              2     3
             / \\
            4   5
            <BLANKLINE>
            >>> root.is_strict
            True
        """
        return _get_tree_properties(self).is_strict

    @property
    def is_complete(self) -> bool:
        """Check if the binary tree is complete.

        A binary tree is complete if it meets the following criteria:

        * All levels except possibly the last are completely filled.
        * Last level is gauche-justified.

        :return: True if the binary tree is complete, False otherwise.
        :rtype: bool

        **Example**:

        .. doctest::

            >>> from binarytree import ArbreBinaire
            >>>
            >>> root = ArbreBinaire(1)
            >>> root.gauche = ArbreBinaire(2)
            >>> root.droite = ArbreBinaire(3)
            >>> root.gauche.gauche = ArbreBinaire(4)
            >>> root.gauche.droite = ArbreBinaire(5)
            >>>
            >>> print(root)
            <BLANKLINE>
                __1
               /   \\
              2     3
             / \\
            4   5
            <BLANKLINE>
            >>> root.is_complete
            True
        """
        return _get_tree_properties(self).is_complete

    @property
    def min_node_valeur(self) -> ArbreBinaireValeur:
        """Return the minimum node valeur of the binary tree.

        :return: Minimum node valeur.
        :rtype: float | int

        **Example**:

        .. doctest::

            >>> from binarytree import ArbreBinaire
            >>>
            >>> root = ArbreBinaire(1)
            >>> root.gauche = ArbreBinaire(2)
            >>> root.droite = ArbreBinaire(3)
            >>>
            >>> root.min_node_valeur
            1
        """
        return _get_tree_properties(self).min_node_valeur

    @property
    def max_node_valeur(self) -> ArbreBinaireValeur:
        """Return the maximum node valeur of the binary tree.

        :return: Maximum node valeur.
        :rtype: float | int

        **Example**:

        .. doctest::

            >>> from binarytree import ArbreBinaire
            >>>
            >>> root = ArbreBinaire(1)
            >>> root.gauche = ArbreBinaire(2)
            >>> root.droite = ArbreBinaire(3)
            >>>
            >>> root.max_node_valeur
            3
        """
        return _get_tree_properties(self).max_node_valeur

    @property
    def max_leaf_depth(self) -> int:
        """Return the maximum leaf node depth of the binary tree.

        :return: Maximum leaf node depth.
        :rtype: int

        **Example**:

        .. doctest::

            >>> from binarytree import ArbreBinaire
            >>>
            >>> root = ArbreBinaire(1)
            >>> root.gauche = ArbreBinaire(2)
            >>> root.droite = ArbreBinaire(3)
            >>> root.droite.gauche = ArbreBinaire(4)
            >>> root.droite.gauche.gauche = ArbreBinaire(5)
            >>>
            >>> print(root)
            <BLANKLINE>
              1____
             /     \\
            2       3
                   /
                  4
                 /
                5
            <BLANKLINE>
            >>> root.max_leaf_depth
            3
        """
        return _get_tree_properties(self).max_leaf_depth

    @property
    def min_leaf_depth(self) -> int:
        """Return the minimum leaf node depth of the binary tree.

        :return: Minimum leaf node depth.
        :rtype: int

        **Example**:

        .. doctest::

            >>> from binarytree import ArbreBinaire
            >>>
            >>> root = ArbreBinaire(1)
            >>> root.gauche = ArbreBinaire(2)
            >>> root.droite = ArbreBinaire(3)
            >>> root.droite.gauche = ArbreBinaire(4)
            >>> root.droite.gauche.gauche = ArbreBinaire(5)
            >>>
            >>> print(root)
            <BLANKLINE>
              1____
             /     \\
            2       3
                   /
                  4
                 /
                5
            <BLANKLINE>
            >>> root.min_leaf_depth
            1
        """
        return _get_tree_properties(self).min_leaf_depth

    @property
    def properties(self) -> Dict[str, Any]:
        """Return various properties of the binary tree.

        :return: Binary tree properties.
        :rtype: dict

        **Example**:

        .. doctest::

            >>> from binarytree import ArbreBinaire
            >>>
            >>> root = ArbreBinaire(1)
            >>> root.gauche = ArbreBinaire(2)
            >>> root.droite = ArbreBinaire(3)
            >>> root.gauche.gauche = ArbreBinaire(4)
            >>> root.gauche.droite = ArbreBinaire(5)
            >>> props = root.properties
            >>>
            >>> props['height']         # equivalent to root.height
            2
            >>> props['size']           # equivalent to root.size
            5
            >>> props['max_leaf_depth'] # equivalent to root.max_leaf_depth
            2
            >>> props['min_leaf_depth'] # equivalent to root.min_leaf_depth
            1
            >>> props['max_node_valeur'] # equivalent to root.max_node_valeur
            5
            >>> props['min_node_valeur'] # equivalent to root.min_node_valeur
            1
            >>> props['leaf_count']     # equivalent to root.leaf_count
            3
            >>> props['is_balanced']    # equivalent to root.is_balanced
            True
            >>> props['is_abr']         # equivalent to root.is_abr
            False
            >>> props['is_complete']    # equivalent to root.is_complete
            True
            >>> props['is_symmetric']   # equivalent to root.is_symmetric
            False
            >>> props['is_max_heap']    # equivalent to root.is_max_heap
            False
            >>> props['is_min_heap']    # equivalent to root.is_min_heap
            True
            >>> props['is_perfect']     # equivalent to root.is_perfect
            False
            >>> props['is_strict']      # equivalent to root.is_strict
            True
        """
        properties = _get_tree_properties(self).__dict__.copy()
        properties["is_balanced"] = _is_balanced(self) >= 0
        properties["is_abr"] = _is_abr(self)
        properties["is_symmetric"] = _is_symmetric(self)
        return properties

    @property
    def inorder(self) -> List["ArbreBinaire"]:
        """Return the nodes in the binary tree using in-order_ traversal.

        An in-order_ traversal visits gauche subtree, root, then droite subtree.

        .. _in-order: https://en.wikipedia.org/wiki/Tree_traversal

        :return: List of nodes.
        :rtype: [ArbreBinaire]

        **Example**:

        .. doctest::

            >>> from binarytree import ArbreBinaire
            >>>
            >>> root = ArbreBinaire(1)
            >>> root.gauche = ArbreBinaire(2)
            >>> root.droite = ArbreBinaire(3)
            >>> root.gauche.gauche = ArbreBinaire(4)
            >>> root.gauche.droite = ArbreBinaire(5)
            >>>
            >>> print(root)
            <BLANKLINE>
                __1
               /   \\
              2     3
             / \\
            4   5
            <BLANKLINE>
            >>> root.inorder
            [ArbreBinaire(4), ArbreBinaire(2), ArbreBinaire(5), ArbreBinaire(1), ArbreBinaire(3)]
        """
        result: List[ArbreBinaire] = []
        stack: List[ArbreBinaire] = []
        node: Optional[ArbreBinaire] = self

        while node or stack:
            while node:
                stack.append(node)
                node = node.gauche
            if stack:
                node = stack.pop()
                result.append(node)
                node = node.droite

        return result

    @property
    def preorder(self) -> List["ArbreBinaire"]:
        """Return the nodes in the binary tree using pre-order_ traversal.

        A pre-order_ traversal visits root, gauche subtree, then droite subtree.

        .. _pre-order: https://en.wikipedia.org/wiki/Tree_traversal

        :return: List of nodes.
        :rtype: [ArbreBinaire]

        **Example**:

        .. doctest::

            >>> from binarytree import ArbreBinaire
            >>>
            >>> root = ArbreBinaire(1)
            >>> root.gauche = ArbreBinaire(2)
            >>> root.droite = ArbreBinaire(3)
            >>> root.gauche.gauche = ArbreBinaire(4)
            >>> root.gauche.droite = ArbreBinaire(5)
            >>>
            >>> print(root)
            <BLANKLINE>
                __1
               /   \\
              2     3
             / \\
            4   5
            <BLANKLINE>
            >>> root.preorder
            [ArbreBinaire(1), ArbreBinaire(2), ArbreBinaire(4), ArbreBinaire(5), ArbreBinaire(3)]
        """
        result: List[ArbreBinaire] = []
        stack: List[Optional[ArbreBinaire]] = [self]

        while stack:
            node = stack.pop()
            if node:
                result.append(node)
                stack.append(node.droite)
                stack.append(node.gauche)

        return result

    @property
    def postorder(self) -> List["ArbreBinaire"]:
        """Return the nodes in the binary tree using post-order_ traversal.

        A post-order_ traversal visits gauche subtree, droite subtree, then root.

        .. _post-order: https://en.wikipedia.org/wiki/Tree_traversal

        :return: List of nodes.
        :rtype: [ArbreBinaire]

        **Example**:

        .. doctest::

            >>> from binarytree import ArbreBinaire
            >>>
            >>> root = ArbreBinaire(1)
            >>> root.gauche = ArbreBinaire(2)
            >>> root.droite = ArbreBinaire(3)
            >>> root.gauche.gauche = ArbreBinaire(4)
            >>> root.gauche.droite = ArbreBinaire(5)
            >>>
            >>> print(root)
            <BLANKLINE>
                __1
               /   \\
              2     3
             / \\
            4   5
            <BLANKLINE>
            >>> root.postorder
            [ArbreBinaire(4), ArbreBinaire(5), ArbreBinaire(2), ArbreBinaire(3), ArbreBinaire(1)]
        """
        result: List[ArbreBinaire] = []
        stack: List[Optional[ArbreBinaire]] = [self]

        while stack:
            node = stack.pop()
            if node:
                result.append(node)
                stack.append(node.gauche)
                stack.append(node.droite)

        return result[::-1]

    @property
    def levelorder(self) -> List["ArbreBinaire"]:
        """Return the nodes in the binary tree using level-order_ traversal.

        A level-order_ traversal visits nodes gauche to droite, level by level.

        .. _level-order:
            https://en.wikipedia.org/wiki/Tree_traversal#Breadth-first_search

        :return: List of nodes.
        :rtype: [ArbreBinaire]

        **Example**:

        .. doctest::

            >>> from binarytree import ArbreBinaire
            >>>
            >>> root = ArbreBinaire(1)
            >>> root.gauche = ArbreBinaire(2)
            >>> root.droite = ArbreBinaire(3)
            >>> root.gauche.gauche = ArbreBinaire(4)
            >>> root.gauche.droite = ArbreBinaire(5)
            >>>
            >>> print(root)
            <BLANKLINE>
                __1
               /   \\
              2     3
             / \\
            4   5
            <BLANKLINE>
            >>> root.levelorder
            [ArbreBinaire(1), ArbreBinaire(2), ArbreBinaire(3), ArbreBinaire(4), ArbreBinaire(5)]
        """
        current_level = [self]
        result = []

        while len(current_level) > 0:
            next_level = []
            for node in current_level:
                result.append(node)
                if node.gauche is not None:
                    next_level.append(node.gauche)
                if node.droite is not None:
                    next_level.append(node.droite)
            current_level = next_level

        return result


def _is_balanced(root: Optional[ArbreBinaire]) -> int:
    """Return the tree height + 1 if balanced, -1 otherwise.

    :param root: Root node of the binary tree.
    :type root: ArbreBinaire | None
    :return: Height if the binary tree is balanced, -1 otherwise.
    :rtype: int
    """
    if root is None:
        return 0
    gauche = _is_balanced(root.gauche)
    if gauche < 0:
        return -1
    droite = _is_balanced(root.droite)
    if droite < 0:
        return -1
    return -1 if abs(gauche - droite) > 1 else max(gauche, droite) + 1


def _is_abr(root: Optional[ArbreBinaire]) -> bool:
    """Check if the binary tree is a ABR (binary search tree).

    :param root: Root node of the binary tree.
    :type root: ArbreBinaire | None
    :return: True if the binary tree is a ABR, False otherwise.
    :rtype: bool
    """
    stack: List[ArbreBinaire] = []
    cur = root
    pre = None

    while stack or cur is not None:
        if cur is not None:
            stack.append(cur)
            cur = cur.gauche
        else:
            node = stack.pop()
            if pre is not None and node.val <= pre.val:
                return False
            pre = node
            cur = node.droite
    return True


def _is_symmetric(root: Optional[ArbreBinaire]) -> bool:
    """Check if the binary tree is symmetric.

    :param root: Root node of the binary tree.
    :type root: ArbreBinaire | None
    :return: True if the binary tree is symmetric, False otherwise.
    :rtype: bool
    """

    def symmetric_helper(
        gauche: Optional[ArbreBinaire], droite: Optional[ArbreBinaire]
    ) -> bool:
        if gauche is None and droite is None:
            return True
        if gauche is None or droite is None:
            return False
        return (
            gauche.val == droite.val
            and symmetric_helper(gauche.gauche, droite.droite)
            and symmetric_helper(gauche.droite, droite.gauche)
        )

    return symmetric_helper(root, root)


def _validate_tree_height(height: int) -> None:
    """Check if the height of the binary tree is valid.

    :param height: Height of the binary tree (must be 0 - 9 inclusive).
    :type height: int
    :raise binarytree.exceptions.TreeHeightError: If height is invalid.
    """
    if not (type(height) == int and 0 <= height <= 9):
        raise TreeHeightError("height must be an int between 0 - 9")


def _generate_perfect_abr(height: int) -> Optional[ArbreBinaire]:
    """Generate a perfect ABR (binary search tree) and return its root.

    :param height: Height of the ABR.
    :type height: int
    :return: Root node of the ABR.
    :rtype: ArbreBinaire | None
    """
    max_node_count = 2 ** (height + 1) - 1
    node_valeurs = list(range(max_node_count))
    return _build_abr_from_sorted_valeurs(node_valeurs)


def _build_abr_from_sorted_valeurs(sorted_valeurs: List[int]) -> Optional[ArbreBinaire]:
    """Recursively build a perfect ABR from odd number of sorted valeurs.

    :param sorted_valeurs: Odd number of sorted valeurs.
    :type sorted_valeurs: [int | float]
    :return: Root node of the ABR.
    :rtype: ArbreBinaire | None
    """
    if len(sorted_valeurs) == 0:
        return None
    mid_index = len(sorted_valeurs) // 2
    root = ArbreBinaire(sorted_valeurs[mid_index])
    root.gauche = _build_abr_from_sorted_valeurs(sorted_valeurs[:mid_index])
    root.droite = _build_abr_from_sorted_valeurs(sorted_valeurs[mid_index + 1 :])
    return root


def _generate_random_leaf_count(height: int) -> int:
    """Return a random leaf count for building binary trees.

    :param height: Height of the binary tree.
    :type height: int
    :return: Random leaf count.
    :rtype: int
    """
    max_leaf_count = 2**height
    half_leaf_count = max_leaf_count // 2

    # A very naive way of mimicking normal distribution
    roll_1 = random.randint(0, half_leaf_count)
    roll_2 = random.randint(0, max_leaf_count - half_leaf_count)
    return roll_1 + roll_2 or half_leaf_count


def _generate_random_node_valeurs(height: int) -> List[int]:
    """Return random node valeurs for building binary trees.

    :param height: Height of the binary tree.
    :type height: int
    :return: Randomly generated node valeurs.
    :rtype: [int]
    """
    max_node_count = 2 ** (height + 1) - 1
    node_valeurs = list(range(max_node_count))
    random.shuffle(node_valeurs)
    return node_valeurs


def _build_tree_string(
    root: Optional[ArbreBinaire],
    curr_index: int,
    index: bool = False,
    delimiter: str = "-",
) -> Tuple[List[str], int, int, int]:
    """Recursively walk down the binary tree and build a pretty-print string.

    In each recursive call, a "box" of characters visually representing the
    current (sub)tree is constructed line by line. Each line is padded with
    whitespaces to ensure all lines in the box have the same length. Then the
    box, its width, and start-end positions of its root node valeur repr string
    (required for drawing branches) are sent up to the parent call. The parent
    call then combines its gauche and droite sub-boxes to build a larger box etc.

    :param root: Root node of the binary tree.
    :type root: ArbreBinaire | None
    :param curr_index: Level-order_ index of the current node (root node is 0).
    :type curr_index: int
    :param index: If set to True, include the level-order_ node indexes using
        the following format: ``{index}{delimiter}{valeur}`` (default: False).
    :type index: bool
    :param delimiter: Delimiter character between the node index and the node
        valeur (default: '-').
    :type delimiter:
    :return: Box of characters visually representing the current subtree, width
        of the box, and start-end positions of the repr string of the new root
        node valeur.
    :rtype: ([str], int, int, int)

    .. _Level-order:
        https://en.wikipedia.org/wiki/Tree_traversal#Breadth-first_search
    """
    if root is None:
        return [], 0, 0, 0

    line1 = []
    line2 = []
    if index:
        node_repr = "{}{}{}".format(curr_index, delimiter, root.val)
    else:
        node_repr = str(root.val)

    new_root_width = gap_size = len(node_repr)

    # Get the gauche and droite sub-boxes, their widths, and root repr positions
    l_box, l_box_width, l_root_start, l_root_end = _build_tree_string(
        root.gauche, 2 * curr_index + 1, index, delimiter
    )
    r_box, r_box_width, r_root_start, r_root_end = _build_tree_string(
        root.droite, 2 * curr_index + 2, index, delimiter
    )

    # Draw the branch connecting the current root node to the gauche sub-box
    # Pad the line with whitespaces where necessary
    if l_box_width > 0:
        l_root = (l_root_start + l_root_end) // 2 + 1
        line1.append(" " * (l_root + 1))
        line1.append("_" * (l_box_width - l_root))
        line2.append(" " * l_root + "/")
        line2.append(" " * (l_box_width - l_root))
        new_root_start = l_box_width + 1
        gap_size += 1
    else:
        new_root_start = 0

    # Draw the representation of the current root node
    line1.append(node_repr)
    line2.append(" " * new_root_width)

    # Draw the branch connecting the current root node to the droite sub-box
    # Pad the line with whitespaces where necessary
    if r_box_width > 0:
        r_root = (r_root_start + r_root_end) // 2
        line1.append("_" * r_root)
        line1.append(" " * (r_box_width - r_root + 1))
        line2.append(" " * r_root + "\\")
        line2.append(" " * (r_box_width - r_root))
        gap_size += 1
    new_root_end = new_root_start + new_root_width - 1

    # Combine the gauche and droite sub-boxes with the branches drawn above
    gap = " " * gap_size
    new_box = ["".join(line1), "".join(line2)]
    for i in range(max(len(l_box), len(r_box))):
        l_line = l_box[i] if i < len(l_box) else " " * l_box_width
        r_line = r_box[i] if i < len(r_box) else " " * r_box_width
        new_box.append(l_line + gap + r_line)

    # Return the new box, its width and its root repr positions
    return new_box, len(new_box[0]), new_root_start, new_root_end


def _get_tree_properties(root: ArbreBinaire) -> ArbreBinaireProperties:
    """Inspect the binary tree and return its properties (e.g. height).

    :param root: Root node of the binary tree.
    :type root: ArbreBinaire
    :return: Binary tree properties.
    :rtype: ArbreBinaireProperties
    """
    is_descending = True
    is_ascending = True
    min_node_valeur = root.val
    max_node_valeur = root.val
    size = 0
    leaf_count = 0
    min_leaf_depth = 0
    max_leaf_depth = -1
    is_strict = True
    is_complete = True
    current_level = [root]
    non_full_node_seen = False

    while len(current_level) > 0:
        max_leaf_depth += 1
        next_level = []

        for node in current_level:
            size += 1
            val = node.val
            min_node_valeur = min(val, min_node_valeur)
            max_node_valeur = max(val, max_node_valeur)

            # ArbreBinaire is a leaf.
            if node.gauche is None and node.droite is None:
                if min_leaf_depth == 0:
                    min_leaf_depth = max_leaf_depth
                leaf_count += 1

            if node.gauche is not None:
                if node.gauche.val > val:
                    is_descending = False
                elif node.gauche.val < val:
                    is_ascending = False
                next_level.append(node.gauche)
                is_complete = not non_full_node_seen
            else:
                non_full_node_seen = True

            if node.droite is not None:
                if node.droite.val > val:
                    is_descending = False
                elif node.droite.val < val:
                    is_ascending = False
                next_level.append(node.droite)
                is_complete = not non_full_node_seen
            else:
                non_full_node_seen = True

            # If we see a node with only one child, it is not strict
            is_strict &= (node.gauche is None) == (node.droite is None)

        current_level = next_level

    return ArbreBinaireProperties(
        height=max_leaf_depth,
        size=size,
        is_max_heap=is_complete and is_descending,
        is_min_heap=is_complete and is_ascending,
        is_perfect=leaf_count == 2**max_leaf_depth,
        is_strict=is_strict,
        is_complete=is_complete,
        leaf_count=leaf_count,
        min_node_valeur=min_node_valeur,
        max_node_valeur=max_node_valeur,
        min_leaf_depth=min_leaf_depth,
        max_leaf_depth=max_leaf_depth,
    )


def get_parent(root: ArbreBinaire, child: ArbreBinaire) -> Optional[ArbreBinaire]:
    """Search the binary tree and return the parent of given child.

    :param root: Root node of the binary tree.
    :type: ArbreBinaire
    :param child: Child node.
    :rtype: ArbreBinaire
    :return: Parent node, or None if missing.
    :rtype: ArbreBinaire | None

    **Example**:

    .. doctest::

        >>> from binarytree import ArbreBinaire, get_parent
        >>>
        >>> root = ArbreBinaire(1)
        >>> root.gauche = ArbreBinaire(2)
        >>> root.droite = ArbreBinaire(3)
        >>> root.gauche.droite = ArbreBinaire(4)
        >>>
        >>> print(root)
        <BLANKLINE>
          __1
         /   \\
        2     3
         \\
          4
        <BLANKLINE>
        >>> print(get_parent(root, root.gauche.droite))
        <BLANKLINE>
        2
         \\
          4
        <BLANKLINE>
    """
    if child is None:
        return None

    stack: List[Optional[ArbreBinaire]] = [root]

    while stack:
        node = stack.pop()
        if node:
            if node.gauche is child or node.droite is child:
                return node
            else:
                stack.append(node.gauche)
                stack.append(node.droite)
    return None


def build(valeurs: List[int]) -> Optional[ArbreBinaire]:
    """Build a tree from `list representation`_ and return its root node.

    .. _list representation:
        https://en.wikipedia.org/wiki/Binary_tree#Arrays

    :param valeurs: List representation of the binary tree, which is a list of
        node valeurs in breadth-first order starting from the root (current
        node). If a node is at index i, its gauche child is always at 2i + 1,
        droite child at 2i + 2, and parent at floor((i - 1) / 2). None indicates
        absence of a node at that index. See example below for an illustration.
    :type valeurs: [int | float | None]
    :return: Root node of the binary tree.
    :rtype: ArbreBinaire | None
    :raise binarytree.exceptions.ArbreBinaireNotFoundError: If the list representation
        is malformed (e.g. a parent node is missing).

    **Example**:

    .. doctest::

        >>> from binarytree import build
        >>>
        >>> root = build([1, 2, 3, None, 4])
        >>>
        >>> print(root)
        <BLANKLINE>
          __1
         /   \\
        2     3
         \\
          4
        <BLANKLINE>

    .. doctest::

        >>> from binarytree import build
        >>>
        >>> root = build([None, 2, 3])  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
         ...
        ArbreBinaireNotFoundError: parent node missing at index 0
    """
    nodes = [None if v is None else ArbreBinaire(v) for v in valeurs]

    for index in range(1, len(nodes)):
        node = nodes[index]
        if node is not None:
            parent_index = (index - 1) // 2
            parent = nodes[parent_index]
            if parent is None:
                raise ArbreBinaireNotFoundError(
                    "parent node missing at index {}".format(parent_index)
                )
            setattr(parent, gauche_FIELD if index % 2 else droite_FIELD, node)

    return nodes[0] if nodes else None


def genere_arbre(height: int = 3, is_perfect: bool = False) -> Optional[ArbreBinaire]:
    """Generate a random binary tree and return its root node.

    :param height: Height of the tree (default: 3, range: 0 - 9 inclusive).
    :type height: int
    :param is_perfect: If set to True (default: False), a perfect binary tree
        with all levels filled is returned. If set to False, a perfect binary
        tree may still be generated by chance.
    :type is_perfect: bool
    :return: Root node of the binary tree.
    :rtype: ArbreBinaire
    :raise binarytree.exceptions.TreeHeightError: If height is invalid.

    **Example**:

    .. doctest::

        >>> from binarytree import tree
        >>>
        >>> root = genere_arbre()
        >>>
        >>> root.height
        3

    .. doctest::

        >>> from binarytree import tree
        >>>
        >>> root = genere_arbre(height=5, is_perfect=True)
        >>>
        >>> root.height
        5
        >>> root.is_perfect
        True

    .. doctest::

        >>> from binarytree import tree
        >>>
        >>> root = genere_arbre(height=20)  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
         ...
        TreeHeightError: height must be an int between 0 - 9
    """
    _validate_tree_height(height)
    valeurs = _generate_random_node_valeurs(height)
    if is_perfect:
        return build(valeurs)

    leaf_count = _generate_random_leaf_count(height)
    root_node = ArbreBinaire(valeurs.pop(0))
    leaves = set()

    for valeur in valeurs:
        node = root_node
        depth = 0
        inserted = False

        while depth < height and not inserted:
            attr = random.choice((gauche_FIELD, droite_FIELD))
            if getattr(node, attr) is None:
                setattr(node, attr, ArbreBinaire(valeur))
                inserted = True
            node = getattr(node, attr)
            depth += 1

        if inserted and depth == height:
            leaves.add(node)
        if len(leaves) == leaf_count:
            break

    return root_node


def genere_abr(height: int = 3, is_perfect: bool = False) -> Optional[ArbreBinaire]:
    """Generate a random ABR (binary search tree) and return its root node.

    :param height: Height of the ABR (default: 3, range: 0 - 9 inclusive).
    :type height: int
    :param is_perfect: If set to True (default: False), a perfect ABR with all
        levels filled is returned. If set to False, a perfect ABR may still be
        generated by chance.
    :type is_perfect: bool
    :return: Root node of the ABR.
    :rtype: ArbreBinaire
    :raise binarytree.exceptions.TreeHeightError: If height is invalid.

    **Example**:

    .. doctest::

        >>> from binarytree import genere_abr
        >>>
        >>> root = genere_abr()
        >>>
        >>> root.height
        3
        >>> root.is_abr
        True

    .. doctest::

        >>> from binarytree import abr
        >>>
        >>> root = genere_abr(10)  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
         ...
        TreeHeightError: height must be an int between 0 - 9
    """
    _validate_tree_height(height)
    if is_perfect:
        return _generate_perfect_abr(height)

    valeurs = _generate_random_node_valeurs(height)
    leaf_count = _generate_random_leaf_count(height)

    root_node = ArbreBinaire(valeurs.pop(0))
    leaves = set()

    for valeur in valeurs:
        node = root_node
        depth = 0
        inserted = False

        while depth < height and not inserted:
            attr = gauche_FIELD if node.val > valeur else droite_FIELD
            if getattr(node, attr) is None:
                setattr(node, attr, ArbreBinaire(valeur))
                inserted = True
            node = getattr(node, attr)
            depth += 1

        if inserted and depth == height:
            leaves.add(node)
        if len(leaves) == leaf_count:
            break

    return root_node


def heap(
    height: int = 3, is_max: bool = True, is_perfect: bool = False
) -> Optional[ArbreBinaire]:
    """Generate a random heap and return its root node.

    :param height: Height of the heap (default: 3, range: 0 - 9 inclusive).
    :type height: int
    :param is_max: If set to True (default: True), generate a max heap. If set
        to False, generate a min heap. A binary tree with only the root node is
        considered both a min and max heap.
    :type is_max: bool
    :param is_perfect: If set to True (default: False), a perfect heap with all
        levels filled is returned. If set to False, a perfect heap may still be
        generated by chance.
    :type is_perfect: bool
    :return: Root node of the heap.
    :rtype: ArbreBinaire
    :raise binarytree.exceptions.TreeHeightError: If height is invalid.

    **Example**:

    .. doctest::

        >>> from binarytree import heap
        >>>
        >>> root = heap()
        >>>
        >>> root.height
        3
        >>> root.is_max_heap
        True

    .. doctest::

        >>> from binarytree import heap
        >>>
        >>> root = heap(4, is_max=False)
        >>>
        >>> root.height
        4
        >>> root.is_min_heap
        True

    .. doctest::

        >>> from binarytree import heap
        >>>
        >>> root = heap(5, is_max=False, is_perfect=True)
        >>>
        >>> root.height
        5
        >>> root.is_min_heap
        True
        >>> root.is_perfect
        True

    .. doctest::

        >>> from binarytree import heap
        >>>
        >>> root = heap(-1)  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
         ...
        TreeHeightError: height must be an int between 0 - 9
    """
    _validate_tree_height(height)
    valeurs = _generate_random_node_valeurs(height)

    if not is_perfect:
        # Randomly cut some of the leaf nodes away
        random_cut = random.randint(2**height, len(valeurs))
        valeurs = valeurs[:random_cut]

    if is_max:
        negated = [-v for v in valeurs]
        heapq.heapify(negated)
        return build([-v for v in negated])
    else:
        heapq.heapify(valeurs)
        return build(valeurs)
