from Examples.LPC_Class_Pride import *


def main() -> Optional[int] | None:
    tests_unified = generate_tests()
    lpc = LeetPrideCore(time_all=True)
    lpc.solution_hash_display(tests_unified)
    any_fail = lpc.run_tests(tests_unified)
    return completion_display(any_fail)


if __name__ == '__main__':  # most of this relevant only for large recursion situations or concurrency needs
    exit(main())
