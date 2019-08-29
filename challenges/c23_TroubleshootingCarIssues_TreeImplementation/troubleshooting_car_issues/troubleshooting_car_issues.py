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
        next_node (obj): Object that tracks the last added node

    Methods:
        add_node:
        remove_node:
        find_empty_nodes:
        print_tree:
    """

    def __init__(self):
        self.root = None
        self.next_node = None

    def add_node(self, value, true_false):
        """Add a node to the tree"""
        if self.root is None:
            self.root = Node(value, None)
            self.next_node = self.root
        elif self.next_node is not None:
            if true_false:
                self.next_node.left = Node(value, self.next_node)
            else:
                self.next_node.right = Node(value, self.next_node)

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

    def find_empty_nodes(self, current_node=None):
        """Finds the next empty node in the tree

        Empty nodes are 'holes' in the tree where a node doesn't yet exist
        """
        print(f"Current Node: {current_node.value} -- Left Child: {current_node.left} -- Right Child: {current_node.right}")
        if current_node.left is None:
            return current_node.left

        self.find_empty_nodes(current_node.left)

        if current_node.right is None:
            return current_node.right

        self.find_empty_nodes(current_node.right)

        # return None


    def _find_empty_nodes_traverse_up(self):
        """Searches up the tree to find an empty node"""
        if self.next_node.left is None:
            return self.next_node.left

        if self.next_node.right is None:
            return self.next_node.right

        self.next_node = self.next_node.parent
        if self.next_node.parent is self.root:
            return self.root

        self._find_empty_nodes_traverse_up()

    def _find_empty_node_traverse_down(self, current_node):
        """Searches down the tree to find an empty node"""
        if current_node.left is None:
            return current_node.left

        if current_node.right is None:
            return current_node.right

        self._find_empty_node_traverse_down(current_node.left)
        self._find_empty_node_traverse_down(current_node.right)

    def set_next_node(self):
        """After adding a node, sets the last node to the new node"""
        if self.next_node.left and self.next_node.left.value:
            self.next_node = self.next_node.left
        elif self.next_node.right and self.next_node.right.value:
            self.next_node = self.next_node.right
        else:
            self.next_node = None

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
        if getattr(tree.next_node, left_right) is None:
            tree.add_node("** YOU ARE HERE **", left_right == "left")
            tree.print_tree()
            leaf_to_add = input(
                f"Add a [{left_right == 'left'}] prompt? " +
                "(Enter a blank string to skip or quit() to exit): "
            ).strip()
            if leaf_to_add == "quit()":
                tree.remove_node(getattr(tree.next_node, left_right))
                return "quit()"
            if leaf_to_add:
                getattr(tree.next_node, left_right).value = leaf_to_add
                leaf_created = True
            else:
                getattr(tree.next_node, left_right).value = None

    return leaf_created

def main():

    tree = initialize_tree()
    while True:
        leaf_created = add_leaf(tree)
        if leaf_created == "quit()":
            break
        tree.set_next_node()
        if tree.next_node is None:
            tree.next_node = tree.find_empty_nodes(tree.root)
            if tree.next_node is None:
                break

    print("\n\nFinal Decision Tree:")
    tree.print_tree()

    proceed = user_inputs.get_string_in_list(
        prompt="Ready to proceed? [Y/N]:",
        err_msg="Sorry, please enter a valid value.",
        allowed_vals=["y", "n"],
        case_sensitive=False
    ).lower()

    if proceed == "y":
        while True:
            print(tree.next_node.value)
            response = user_inputs.get_string_in_list(
                prompt="True or False? [T/F]:",
                err_msg="Sorry, please enter a valid value.",
                allowed_vals=["t", "f", "true", "false"],
                case_sensitive=False,
                exit_val="quit()"
            ).lower()[0]

            if response == "t":
                next_node = tree.walk(tree.next_node, "LEFT")
            elif response == "f":
                next_node = tree.walk(tree.next_node, "RIGHT")
            else:
                break

            if (next_node.left == next_node.right) and (next_node.left is None):
                print(next_node.value)
                break
    else:
        print("Goodbye.")
