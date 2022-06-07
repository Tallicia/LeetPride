class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def print_nodes(head: ListNode, addresses: bool = False) -> list:
    out = []
    while head is not None:
        if addresses:
            out += [(head.val, str(head))]
        else:
            out += [head.val]
        head = head.next
    return out


def append_node_list(node: list, append: ListNode) -> ListNode | None:
    head = make_node_list(node)
    n = head
    while n.next:
        n = n.next
    n.next = append
    return head

def make_node_list(node: list) -> ListNode | None:
    if len(node) == 0:
        return None
    head = ListNode(node[0])
    tail = head
    for n in node[1:]:
        tail.next = ListNode(n)
        tail = tail.next
    return head


def make_node_lists(*nodes: list) -> ():
    ret = ()
    for n in nodes:
        ret = ret + (make_node_list(n),)
    return ret
