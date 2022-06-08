from typing import Optional
from LeetPride import ListNode, make_node_list, append_node_list, list_nodes
from LeetPride import LeetPrideCore, completion_display
# from LeetPride import run_process  # commented out to pass in the method identifier to run with multiple Solutions


class SolutionNodeList:
    def get_intersection_node(self, head_a: ListNode, head_b: ListNode) -> Optional[ListNode]:
        if type(head_a) is list and type(head_b) is list:
            tail = make_node_list(head_a[2:])
            head_a = append_node_list(head_a[:2], tail)
            head_b = append_node_list(head_b[:3], tail)
        if head_a is None or head_b is None:
            return None
        pa = head_a
        pb = head_b
        while pa is not pb:
            pa = head_b if pa is None else pa.next
            pb = head_a if pb is None else pb.next
        return list_nodes(pa)[0]
        # return pa


def generate_tests():
    nl0 = make_node_list([8, 4, 5])
    nl1 = append_node_list([4, 1, ], nl0)
    nl2 = append_node_list([5, 6, 1, ], nl0)
    p_try = {'head_a': (nl1, list_nodes), 'head_b': (nl2, list_nodes)}
    p_try2 = {'head_a': nl1, 'head_b': nl2}
    nl_2_common = make_node_list([2, 4, ])
    p_test2 = {'head_a': (append_node_list([1, 9, 1, ], nl_2_common), list_nodes),
               'head_b': (append_node_list([3, ], nl_2_common), list_nodes)}

    return [('SolutionNodeList', None, True),
            ('get_intersection_node', [[4, 1, 8, 4, 5], [5, 6, 1, 8, 4, 5]], 8),
            ('get_intersection_node', p_try, 8),
            ('get_intersection_node', p_try2, 8),
            ('get_intersection_node', p_try, 10),  # Intentional Fail
            ('get_intersection_node', {'head_a': (nl1, list_nodes), 'head_b': (nl2, list_nodes)}, 8),
            ('get_intersection_node', p_test2, 2),
            ('get_intersection_node', p_test2, list_nodes(nl_2_common)[0]),
            ]


def lpcnl1_example_main() -> Optional[int] | None:
    tests_unified = generate_tests()
    lpc = LeetPrideCore(module=__name__)
    lpc.solution_hash_display(tests_unified=tests_unified)
    any_fail = lpc.run_tests(tests_unified)
    return completion_display(any_fail)


def main() -> Optional[int] | None:
    return lpcnl1_example_main()  # return run_process(generate_tests())


if __name__ == '__main__':
    exit(main())
