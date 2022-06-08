from LP_Examples.LPC_Class_Pride import lpccp_example_main
from LP_Examples.LPC_Class_Mix import lpccm_example_main
from LP_Examples.LPC_Method_1_Stub import lpcm1_example_main
from LP_Examples.LPC_NodeList_1 import lpcnl1_example_main

def main() -> int:
    res_max = 0
    res_max = max(lpccm_example_main(), res_max)
    res_max = max(lpccp_example_main(), res_max)
    res_max = max(lpcnl1_example_main(), res_max)
    res_max = max(lpcm1_example_main(), res_max)
    return res_max


if __name__ == '__main__':
    exit(main())
