# from LP_Examples.LPC_Class_Pride import lpccp_example_main
from LP_Examples.LPC_Class_Mix import lpccm_example_main
from LP_Examples.LPC_Method_1_Stub import lpcm1_example_main

def main() -> int:
    return lpcm1_example_main()

    # tests_unified = generate_tests()
    # lpc = LeetPrideCore(time_all=True)
    # lpc.solution_hash_display(tests_unified)
    # any_fail = lpc.run_tests(tests_unified)
    # return completion_display(any_fail)


if __name__ == '__main__':  # most of this relevant only for large recursion situations or concurrency needs
    exit(main())
