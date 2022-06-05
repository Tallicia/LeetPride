from LeetPrideCore import *


class Solution:
    # @timeit
    def method1(self, nums: List[int], target: int) -> List[int | None]:
        return [nums[target]]


def generate_tests():
    test_result = [(([2, 8, 11, 15], 0),
                    [2])]

    ops, init_params, funcs = ['Solution'], [], ['method1']
    tests_unified = [(ops[0], init_params, True)]
    for tr in test_result:
        for f in funcs:
            ops += [f]
            tests_unified += [(f, tr[0], tr[1])]
    return tests_unified


def main() -> Optional[int] | None:
    tests_unified = generate_tests()
    lpc = LeetPrideCore(time_all=True)
    lpc.solution_hash_display(tests_unified)
    any_fail = lpc.run_tests(tests_unified)
    return completion_display(any_fail)


if __name__ == '__main__':  # most of this relevant only for large recursion situations or concurrency needs
    exit(main())