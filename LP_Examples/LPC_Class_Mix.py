from LeetPride.Core import *


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.dp = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]

        # calculate prefix sum
        for r in range(len(self.dp) - 1):
            for c in range(len(self.dp[0]) - 1):
                self.dp[r + 1][c + 1] = matrix[r][c] + self.dp[r][c + 1] + self.dp[r + 1][c] - self.dp[r][c]

    @timeit
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2 + 1][col2 + 1] - self.dp[row1][col2 + 1] - self.dp[row2 + 1][col1] + self.dp[row1][col1]


class Other:
    def __init__(self):
        self.__repr__ = 'Love'
        pass

    def derp(self, pride: str = 'Lover') -> str:
        return 'LGBTQ ' + pride


def generate_tests():
    tests_unified = []
    #  \/\/\/\/\/\/\/\/\/\/ Set tests in these sections \/\/\/\/\/\/\/\/\/\/ #
    tests = (['NumMatrix', 'sumRegion', 'sumRegion', 'sumRegion', 'sumRegion'],
             [[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]],
              [2, 1, 4, 3],
              [1, 1, 2, 2],
              [1, 2, 2, 4],
              [0, 0, 1, 1],
              ])
    expected_test_results = [True, 8, 11, 12, 15, ]
    #  ^^^^^^^^^^^^^^^^^^^^ Set tests in these sections ^^^^^^^^^^^^^^^^^^^^ #
    tests_unified += list(zip(tests[0], tests[1], expected_test_results))  # This line should remain

    #  \/\/\/\/\/\/\/\/\/\/ Set tests in these sections \/\/\/\/\/\/\/\/\/\/ #
    tests = (['NumMatrix', 'sumRegion', ],
             [[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]],
              [0, 0, 1, 1],
              ])
    expected_test_results = [True, 14, ]  # Intentionally Failing Test
    #  ^^^^^^^^^^^^^^^^^^^^ Set tests in these sections ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ #
    tests_unified += list(zip(tests[0], tests[1], expected_test_results))

    #  \/\/\/\/\/\/\/\/\/\/ Set tests in these sections \/\/\/\/\/\/\/\/\/\/ #
    tests = (['Other', 'derp', ],  # Switching to another class and methods for testing
             [(),
              'Lover forever!',
              ])
    expected_test_results = [True, 'LGBTQ Lover forever!', ]
    #  ^^^^^^^^^^^^^^^^^^^^ Set tests in these sections ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ #
    tests_unified += list(zip(tests[0], tests[1], expected_test_results))

    #  \/\/\/\/\/\/\/\/\/\/ Set tests in these sections \/\/\/\/\/\/\/\/\/\/ #
    tests = (['NumMatrix', 'sumRegion', 'sumRegion', 'sumRegion', 'sumRegion', ],
             [[[[0, 0], [1, 1]]],
              [0, 0, 1, 1],
              [0, 0, 0, 0],
              [0, 1, 0, 1],
              [0, 1, 1, 1],
              ])
    expected_test_results = [True, 2, 0, 0, 1, ]
    #  ^^^^^^^^^^^^^^^^^^^^ Set tests in these sections ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ #
    tests_unified += list(zip(tests[0], tests[1], expected_test_results))

    return tests_unified


def lpccm_example_main() -> Optional[int] | None:
    tests_unified = generate_tests()
    lpc = LeetPrideCore(module=__name__)
    lpc.solution_hash_display(tests_unified=tests_unified)
    any_fail = lpc.run_tests(tests_unified)
    return completion_display(any_fail)

def main() -> Optional[int] | None:
    # solution_hash_display([['main']])
    # solution_hash_display([['fail test on purpose and exit']])
    return lpccm_example_main()

if __name__ == '__main__':  # most of this relevant only for large recursion situations or concurrency needs
    # sys.setrecursionlimit(5000)
    # threading.stack_size(200000000)
    # thread = threading.Thread(target=main())
    # thread.start()
    exit(main())
