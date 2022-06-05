from typing import Optional
from LeetPride import run_process


class Pride:
    def __init__(self, pride: str):
        self.love = pride

    def loving(self, pride: str = '!!!') -> str:
        return 'LGBTQ Lover ' + self.love + pride


def generate_tests():
    #  \/\/\/\/\/\/\/\/\/\/ Set tests in these sections \/\/\/\/\/\/\/\/\/\/ #
    tests = (['Pride', 'loving', ],
             ['forever !',
              None,
              ])
    expected_test_results = [True, 'LGBTQ Lover forever !!!!', ]
    #  ^^^^^^^^^^^^^^^^^^^^ Set tests in these sections ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ #

    return list(zip(tests[0], tests[1], expected_test_results))


def lpccp_example_main() -> Optional[int] | None:
    return run_process(generate_tests(), params={'module': __name__})


def main() -> Optional[int] | None:
    return lpccp_example_main()


if __name__ == '__main__':  # most of this relevant only for large recursion situations or concurrency needs
    exit(main())
