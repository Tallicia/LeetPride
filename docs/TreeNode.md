# TreeNode support

LeetPride includes class TreeNode and helper functions for
setting up and displaying TreeNodes for human-readable use and 
test verification.

Helper functions will make creating tests and verifying tests 
using list representation of TreeNodes much easier and quicker.  

>
>```
>from LeetPride import run_process, TreeNode, insert_tree_node, make_tree, list_tree, list_tree_pre, list_level_order, list_current_level, height   
>```
>will quickly make available standard ListNode class
>>
>>      class TreeNode:
>>          def __init__(self, val: object = 0, left=None, right=None):
>>          self.val = val
>>          self.left = left
>>          self.right = right

```
def insert_tree_node(node: TreeNode, data: object):
    """
    :param node: A TreeNode
    :param data: THe data to assign to the TreeNode once placed in position
    :return: No Return, updates temp TreeNode in place

    Insert data to be placed in tree
    """
    queue = [node]
    while len(queue):
        node = queue[0]
        queue.pop(0)
        if not node.left:
            node.left = TreeNode(data)
            break
        else:
            queue.append(node.left)
        if not node.right:
            node.right = TreeNode(data)
            break
        else:
            queue.append(node.right)
```
```
def make_tree(elements):
    """
    create Tree from elements, usually a list.
    """
    if not elements:
        return TreeNode()
    tree = TreeNode(elements[0])
    for element in elements[1:]:
        insert_tree_node(tree, element)
    return tree
```
```
def list_tree(head: TreeNode) -> list:
    """
    list Tree in in-order order traversal
    """
    # in order list generation
    out = []
    if head is not None:
        out += list_tree(head.left)
        if head.val is not None:
            out += [head.val]
        out += list_tree(head.right)
    return out
```
```
def list_tree_pre(head: TreeNode) -> list:
    """
    list Tree in pre-order order traversal
    """
    out = []
    if head is not None:
        if head.val is not None:
            out += [head.val]
        out += list_tree_pre(head.left)
        out += list_tree_pre(head.right)
    return out
```
```
def list_level_order(root) -> List[int]:
    """
    list Tree in level order
    """
    out = []
    h = height(root)
    for i in range(1, h + 1):
        out += list_current_level(root, i)
    return out
```
```
def list_current_level(root, level) -> List[int | None]:
    """
    list of the current level
    """
    out = []
    if root is None:
        return [None]
    if level == 1:
        out += [root.val]
    elif level > 1:
        out += list_current_level(root.left, level - 1)
        out += list_current_level(root.right, level - 1)
    return out
```
```
def height(node):
    """
    list height of Tree at given Node
    """
    if node is None:
        return 0
    else:  # Compute the height of each subtree
        l_height = height(node.left)
        r_height = height(node.right)
        return max(l_height + 1, r_height + 1)
```
