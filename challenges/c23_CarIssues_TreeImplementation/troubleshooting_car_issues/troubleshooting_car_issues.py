"""
Defines a class that helps troubleshooting common car issues
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from util_functions.utils import user_inputs


class Node():
    """Represents a node in a tree object

    Attributes:
        left (obj): Left child node
        right (obj): Right child node
        value (str): Value for the node, assumed to be a string
        parent (obj): Parent node
    """
    def __init__(self, value, parent):
        self.left = None
        self.right = None
        self.value = value
        self.parent = parent

class DecisionTree():
    """Represents a True/False decision tree.

    True values are inserted as the left child node and False values are inserted as the right
        child node.

    Attributes:
        root (obj): Node representing the root of the tree
        last_node (obj): Object that tracks the last added node

    Methods:
        add_node:
        remove_node:
        find_empty_nodes:
        print_tree:
    """

    def __init__(self):
        self.root = None
        self.last_node = None

    def add_node(self, value, true_false):
        """Add a node to the tree"""
        if self.root is None:
            self.root = Node(value, None)
            self.last_node = self.root
        elif self.last_node is not None:
            if true_false:
                self.last_node.left = Node(value, self.last_node)
            else:
                self.last_node.right = Node(value, self.last_node)

    def print_tree(self):
        """Prints an ascii representation of the tree"""
        print(self._print_tree(self.root))

    def _print_tree(self, node, level=0):
        """
        Should print a tree representation

        Each parent node will have the possibility of two nodes beneath it
        Leafs will be designated with ">>"
        """
        if node is None:
            return

        current_level = level
        level += 1
        output = f"{node.value}"
        if node.left and (node.left.value is not None):
            connector = "├─" if node.left.value is not None else "└─"
            output += (
                "\n" + "│  " * current_level + f"{connector}" +
                f" (T): {self._print_tree(node.left, level)}"
            )

        if node.right and (node.right.value is not None):
            output += (
                f"\n{'│  ' * current_level}└─ (F): {self._print_tree(node.right, level)}"
            )

        if node.left or node.right:
            return output

        # return  "  ** " + output + " **"
        return output

    def walk(self, current_node, direction):
        """Walks through the tree one step at a time"""
        if self.root is not None:
            if direction == "LEFT":
                if current_node.left is None:
                    return current_node.value
                return current_node.left

            if current_node.right is None:
                return current_node.value
            return current_node.right

    def remove_node(self, node):
        """Removes a node from the tree"""
        self._remove_node(node)
        return "Deleted"

    def _remove_node(self, node):
        """Supporting code for removing node from the tree"""
        # Need to delete references to the node first, then delete the node
        # If the node has children, they need to be deleted as well
        if node.parent.left == node:
            node.parent.left = None

        if node.parent.right == node:
            node.parent.right = None

        if node.left is not None:
            self._remove_node(node.left)

        if node.right is not None:
            self._remove_node(node.right)

        del node

    def find_empty_nodes(self):
        """Finds the next empty node in the tree

        Empty nodes are 'holes' in the tree where a node doesn't yet exist
        """
        next_node_up = self._find_empty_nodes_traverse_up()


    def _find_empty_nodes_traverse_up(self):
        """Searches up the tree to find an empty node"""
        if self.last_node.left is None:
            return self.last_node.left

        if self.last_node.right is None:
            return self.last_node.right

        self.last_node = self.last_node.parent
        if self.last_node.parent is self.root:
            return None
        else:
            self._find_empty_nodes_traverse_up()

    def _find_empty_nodes_traverse_down(self):
        """Searches down the tree to find an empty node"""
        if self.last_node.left is None:
            return self.last_node.left

        if self.last_node.right is None:
            return self.last_node.right

        if (self.last_node.left is not None) and (self.last_node.left.value is not None):
            self.last_node = self.last_node.left
            self._find_empty_nodes_traverse_down()

        if (self.last_node.right is not None) and (self.last_node.right.value is not None):
            self.last_node = self.last_node.right
            self._find_empty_nodes_traverse_down()

        self.last_node = self.last_node.parent
        self._find_empty_nodes_traverse_down()

    def set_last_node(self):
        """After adding a node, sets the last node to the new node"""
        if self.last_node.left and self.last_node.left.value:
            self.last_node = self.last_node.left
        elif self.last_node.right and self.last_node.right.value:
            self.last_node = self.last_node.right
        elif self.last_node is None:
            return
        else:
            self.last_node = self.last_node.parent

def initialize_tree():
    """Function to start up a DecisionTree class object with a root value"""
    tree = DecisionTree()
    if tree.root is None:
        node_value = input("What is the root value? ")
        tree.add_node(node_value, None)
    return tree

def add_leaf(tree):
    """Function that adds leaf nodes to the tree"""
    leaf_created = False
    for left_right in ["left", "right"]:
        if getattr(tree.last_node, left_right) is None:
            tree.add_node("** YOU ARE HERE **", left_right == "left")
            tree.print_tree()
            leaf_to_add = input(
                f"Add a [{left_right == 'left'}] prompt? " +
                "(Enter a blank string to skip or quit() to exit): "
            ).strip()
            if leaf_to_add and leaf_to_add != "quit()":
                getattr(tree.last_node, left_right).value = leaf_to_add
                leaf_created = True
            else:
                getattr(tree.last_node, left_right).value = None
            if leaf_to_add == "quit()":
                return "quit()"

    return leaf_created

def main():

    tree = initialize_tree()
    while True:
        leaf_created = add_leaf(tree)
        if leaf_created == "quit()":
            break
        tree.set_last_node()

    print("\n\nFinal Decision Tree:")
    tree.print_tree()
