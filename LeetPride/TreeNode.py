from typing import List


class TreeNode:
    def __init__(self, val: object = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insert_tree_node(temp: TreeNode, data: object):
    """
    :param temp:
    :param data:
    :return: No Return, updates temp TreeNode in place
    """
    queue = [temp]
    while len(queue):
        temp = queue[0]
        queue.pop(0)
        if not temp.left:
            temp.left = TreeNode(data)
            break
        else:
            queue.append(temp.left)
        if not temp.right:
            temp.right = TreeNode(data)
            break
        else:
            queue.append(temp.right)


def make_tree(elements):
    if not elements:
        return TreeNode()
    tree = TreeNode(elements[0])
    for element in elements[1:]:
        insert_tree_node(tree, element)
    return tree


def print_tree(head: TreeNode) -> list:
    """
    Print Tree in in-order order traversal
    """
    # in order list generation
    out = []
    if head is not None:
        out += print_tree(head.left)
        if head.val is not None:
            out += [head.val]
        out += print_tree(head.right)
    return out


def print_tree_pre(head: TreeNode) -> list:
    """
    Print Tree in pre-order order traversal
    """
    out = []
    if head is not None:
        if head.val is not None:
            out += [head.val]
        out += print_tree_pre(head.left)
        out += print_tree_pre(head.right)
    return out


def print_level_order(root) -> List[int]:
    out = []
    h = height(root)
    for i in range(1, h + 1):
        out += print_current_level(root, i)
    return out


def print_current_level(root, level) -> List[int | None]:
    out = []
    if root is None:
        return [None]
    if level == 1:
        out += [root.val]
    elif level > 1:
        out += print_current_level(root.left, level - 1)
        out += print_current_level(root.right, level - 1)
    return out


def height(node):
    if node is None:
        return 0
    else:  # Compute the height of each subtree
        l_height = height(node.left)
        r_height = height(node.right)
        return max(l_height + 1, r_height + 1)
