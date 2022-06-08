from typing import List, Optional
from LeetPride import LeetPrideCore, completion_display, timeit


class MultipleApproaches:
    def bigger(self, a: str = 'bigger', x: int = 3) -> str:
        return 'Do it !!' + a * x

    @timeit
    def faster(self, a: str = 'faster', x: int = 1) -> str:
        return 'Do it !!' + a * x

    def stronger(self, a: str = 'faster', x: int = 5) -> str:
        return 'Do it !!' + a * x

def generate_tests():
    test_result = [[['BIGGER', 2], 'Do it !!BIGGERBIGGER']]
    test_result += [[['BIGGER', 2], 'Do it !!BIGGERBIGGER']]
    test_result += [[['faster', 1], 'Do it !!faster']]
    test_result += [[['BIGGER', ], 'Do it !!BIGGERBIGGER']]

    ops, init_params, funcs = ['MultipleApproaches'], [], ['bigger', 'faster', 'stronger']
    tests_unified = [(ops[0], init_params, True)]
    for tr in test_result:
        for f in funcs:
            ops += [f]
            tests_unified += [(f, tr[0], tr[1])]
    return tests_unified


def lpcmm_example_main() -> Optional[int] | None:
    tests_unified = generate_tests()
    lpc = LeetPrideCore(module=__name__)
    lpc.solution_hash_display(tests_unified=tests_unified)
    any_fail = lpc.run_tests(tests_unified)
    return completion_display(any_fail)


def main() -> Optional[int] | None:
    return lpcmm_example_main()


if __name__ == '__main__':  # most of this relevant only for large recursion situations or concurrency needs
    exit(main())
