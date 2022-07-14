from LeetPride import str_style
from LP_Examples.LPC_Class_Pride import lpccp_example_main
from LP_Examples.LPC_Class_Mix import lpccm_example_main
from LP_Examples.LPC_Method_1 import lpcm1_example_main
from LP_Examples.LPC_NodeList_1 import lpcnl1_example_main
from LP_Examples.LPC_Method_Multiple import lpcmm_example_main
from LP_Examples.LPC_TreeNode_1 import lpctn1_example_main


def run_all_examples() -> int:
    res_max = 0
    funcs = [lpccm_example_main, lpccp_example_main, lpcnl1_example_main,
             lpcm1_example_main, lpcmm_example_main, lpctn1_example_main,
             ]
    func_str = ''
    for f in funcs:
        func_str += ''.join('    ' + str(f.__name__) + '     \n')
    func_cnt = str(len(funcs))
    func_out = 'Running ' + func_cnt + ' Examples:\n' + func_str
    print(str_style(func_out, sp=7, hvd='v', box='Box'))
    for f in funcs:
        res_max = max(f(), res_max)
    func_out = 'Completed ' + func_cnt + ' Examples:\n' + func_str
    print(str_style(func_out, sp=7, hvd='v', box='Box'))
    return res_max


def main() -> int:
    return run_all_examples()


if __name__ == '__main__':
    exit(main())
