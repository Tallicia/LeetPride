from LeetPride import run_process, timeit, TreeNode, make_tree, LeetPrideCore, completion_display
from typing import List, Optional


class SolutionTreeNode:
    @timeit
    def right_side_view(self, root: Optional[TreeNode]) -> List[int] | None:
        if not root:
            return root
        results = []

        def level_order(node, res, level) -> None:
            if not node:
                return
            if len(res) == level:
                res.append(node.val)
            level_order(node.right, res, level + 1)
            level_order(node.left, res, level + 1)
        level_order(root, results, 0)
        return results


def generate_tests():
    funcs = ['right_side_view', ]
    tests = [('SolutionTreeNode', None, True)]
    cases = [({'node': make_tree([1, 2, 3, None, 5, None, 4])}, [1, 3, 4]),
             ({'node': make_tree([1, None, 3])}, [1, 3]),
            ]
    for f in funcs:
        for c in cases:
            # print(list_level_order(c[0][0]))
            tests += [(f, c[0], c[1])]  # first is inputs, second is expected result
    return tests


def lpctn1_example_main() -> Optional[int] | None:
    tests_unified = generate_tests()
    lpc = LeetPrideCore(module=__name__)
    lpc.solution_hash_display(tests_unified=tests_unified)
    any_fail = lpc.run_tests(tests_unified)
    return completion_display(any_fail)


def main() -> Optional[int] | None:
    return lpctn1_example_main()


def main() -> int:
    t = generate_tests()
    print(t)
    return run_process(generate_tests())


if __name__ == '__main__':
    exit(main())

'''
199. Binary Tree Right Side View
Medium

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you
 can see ordered from top to bottom.


Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:
Input: root = [1,null,3]
Output: [1,3]

Example 3:
Input: root = []
Output: []

Constraints:
    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100
'''