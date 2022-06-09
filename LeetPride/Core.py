import os.path
import sys  # import threading
from typing import Optional, List
from time import time
from functools import wraps
from colorama import Fore, Back, Style
from pystyle import Colorate, Colors, Box
import inspect  # from hashlib import md5
from zlib import adler32  # , crc32


def timeit(f):
    @wraps(f)
    def timing(*args, **kw):
        t1 = time()
        res = f(*args, **kw)
        t2 = time()
        dur = t2 - t1
        print(Fore.YELLOW + 'Duration :', '%0.9f' % dur + Style.RESET_ALL, end=' ')
        return res
    return timing


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs, flush=True)


def str_style(s: str, sp: int = 1, hvd: str = 'd', box: Optional[str] = None, col: list = Colors.rainbow) -> str:
    f, res = Colorate.Horizontal, ''
    if hvd.lower() == 'v':
        f = Colorate.Vertical
    elif hvd.lower() == 'd':
        f = Colorate.Diagonal
    elif hvd.lower() == 'b':
        f = Colorate.DiagonalBackwards
    elif hvd.lower() == 'e':
        f = Colorate.Error
    if box is None or box is False:
        res = f(col, s, speed=sp)
    elif box == 'Lines':
        res = f(col, Box.Lines(s), speed=sp)
    elif box == 'Box':
        res = f(col, Box.DoubleCube(s), speed=sp)
    return res + Style.RESET_ALL


def completion_display(any_fail):
    if any_fail:
        print(str_style('\nDone !! Oh NOEZ !!', col=Colors.red_to_yellow))
        s_fail = str(any_fail) + ' Test(s) Failed ' + 'x' * min(50, any_fail * 5) + '!!'
        s = str_style(s_fail, col=Colors.red_to_purple)
        eprint(s)
    else:
        print(str_style('\nDone !! Yay !!', col=Colors.blue_to_green))
        print(Fore.GREEN + '!! Without any failures -- Woot! Woot!' + Style.RESET_ALL)
    return any_fail


def run_process(tests_unified: List, params: Optional[dict] = None, module: str = '__main__') -> int:
    time_all = False
    if params:
        if 'time_all' in params.keys() and params['time_all']:
            time_all = True
        if 'module' in params.keys():
            module = params['module']
    lpc = LeetPrideCore(time_all=time_all, module=module)
    lpc.solution_hash_display(tests_unified=tests_unified)
    any_fail = lpc.run_tests(tests_unified)
    return completion_display(any_fail)


class LeetPrideCore:
    def __init__(self, time_all: Optional[bool] = False, module: str = '__main__'):
        self.test_module = module
        self.test_class = None
        self.time_all = time_all
        self.timing_set = {}

    def solution_hash_display(self, tests_unified: Optional[List] = None, sol_name: str = None):
        finds = []
        if sol_name:
            finds += [sol_name]
        else:
            for t in tests_unified:
                chk = t[0][0][0]
                if type(chk) is str and chk.isupper():
                    finds += [t[0]]
        finds = sorted(set(finds))
        for sol_name in finds:
            # module = __import__(self.test_module + '.' + sol_name)
            module = __import__(self.test_module)
            # module = self.test_module
            file = os.path.basename(inspect.getfile(module))
            # print(f'{self.test_module=}')
            # print(f'{module=}')
            sol_class = getattr(module, sol_name)
            sol_source, sol_members = file + '\n' + sol_name + '\n', ''
            try:
                for m in inspect.getmembers(sol_class):
                    if m[0].startswith('__') and m[0] != '__init__':  # and m[0] != '__init_subclass__':
                        continue
                    s_m = 'sol_class.' + m[0]
                    s_inst = eval(s_m)
                    if inspect.isfunction(s_inst) or inspect.ismethod(s_inst):
                        eval_s = 'inspect.getsource(s_inst)'  # sol.__hash__()
                        x = eval(eval_s)
                        sol_source += x + '\n\n'
                    else:
                        x = eval(s_m)
                        s_type = str(type(x))
                        if s_type != "<class 'wrapper_descriptor'>":
                            sol_members += '    member: ' + s_m + ' : ' + s_type + '\n'
                sol_source += sol_members
                print(str_style(sol_source[:-1], box='Box', hvd='v', sp=5))
                sol_hash = adler32(sol_source.encode())
                sol_hex = str(hex(sol_hash).split('x')[-1])
                print(str_style('Solution Adler-32 : ' + str(sol_hash) + ' || ' + sol_hex + ' v0.69'))
            except NameError:
                print(Colorate.Error('Invalid or No Class ' + sol_name + ' or Solution Defined'))

    def run_tests(self, tests_unified: List):
        fail, any_fail, res, test_len, pr_col, eval_s, tc = False, 0, [], 400, '', '', None
        for t in tests_unified:
            pr_col += str(t)[:test_len] + '\n'
        print(str_style(pr_col, sp=2, hvd='d'))
        for tt in tests_unified:
            if tt[0][0][0].isupper():
                test_class_name = tt[0]  # Class Instantiate in first test entry
                print(str_style('\n' + '-' * 10 + ' Instantiating: '
                                + test_class_name, hvd='h', sp=4, col=Colors.yellow_to_green))
                p, params = tt[1], None
                if p:
                    if type(p) is str:
                        params = "'" + p + "'"
                    else:
                        params = str(p)[1: -1]
                self.set_test_class(test_class_name, params)
                out = test_class_name + ' is successfully instantiated'
                out += (' : ' + params) if params else '.'
                print(str_style(out, hvd='h'))
                res += [(True, eval_s)]
            else:
                any_fail, r0 = self.test_print(any_fail, test_len, tt)
                res += [(r0, eval_s)]
        return any_fail

    def set_test_class(self, test_class_name='Solution', params=None):
        module = __import__(self.test_module)
        sol_class = getattr(module, test_class_name)
        if sol_class and params:
            eval_s = 'sol_class(' + params + ')'
        else:
            eval_s = 'sol_class()'
        self.test_class = eval(eval_s)

    def test_print(self, any_fail, test_len, test_and_result):
        method_name = str(test_and_result[0])
        p, params, param_display_list = test_and_result[1], None, None
        if p:
            if type(p) is str:
                params = "'" + p + "'"
            elif type(p) is dict:
                params = p
            elif type(p) is list:
                params = str(p)[1: -1]
        print(str_style(' :Testing: ' + '-' * 60 + ' :Testing: ', hvd='d', sp=1, col=Colors.purple_to_red))
        i, fail, param_list = test_and_result[1], False, []
        if params:
            if type(params) is dict:
                params_check = [x for x in params.values()]
                if type(params_check[0]) is tuple:
                    param_list = [p[0] for p in params.values()]
                    param_display_list = [p[1] for p in params.values()]
                else:
                    param_list = [p for p in params.values()]
                eval_s = 'self.test_class.' + method_name + '(*param_list)'
            else:
                eval_s = 'self.test_class.' + method_name + '(' + params + ')'
        else:
            eval_s = 'self.test_class.' + method_name + '()'
        print(str_style(f'{self.test_class.__class__.__name__}.{method_name}'), end='')
        if param_display_list is not None:
            params = []
            for p in zip(param_display_list, param_list):
                params += [p[0](p[1])]
        print('(' + Fore.MAGENTA + str(params)[:test_len] + Style.RESET_ALL + ')')
        if self.time_all:
            src = inspect.getsource(eval('self.test_class.' + method_name))
            if '@timeit' in src or 'self.test_class.' + method_name in self.timing_set.keys():
                print(str_style('timeit on ', col=Colors.red_to_yellow), end='')
            else:
                self.timing_set['self.test_class.' + method_name] = 'TimingOn'
                setattr(self.test_class, method_name, timeit(eval('self.test_class.' + method_name)))
            r0 = eval(eval_s)
        else:
            r0 = eval(eval_s)
        expected_result = test_and_result[2]
        good = r0 == expected_result
        if not good:
            fail = True
            any_fail += 1
        if not fail:
            print(Fore.GREEN + Style.BRIGHT + 'Good! - ' + Style.RESET_ALL, end='')
            p_col = Fore.GREEN
        else:
            print(Fore.RED + Style.BRIGHT + Back.YELLOW + 'FAIL TEST - ' + Style.RESET_ALL, end='')
            p_col = Fore.RED + Back.YELLOW + Style.BRIGHT
        print(Fore.CYAN + 'Test: ', Colorate.Horizontal(Colors.rainbow, str(test_and_result)[:test_len]),
              Fore.GREEN + 'Result: ' + p_col + "'" + str(r0) + "'" + Style.RESET_ALL, Fore.GREEN
              + '?=', Fore.LIGHTYELLOW_EX + "'" + str(expected_result) + "'" + Fore.RESET)
        return any_fail, r0

# if __name__ == '__main__':  # most of this relevant only for large recursion situations
#     # sys.setrecursionlimit(5000)
#     # threading.stack_size(200000000)
#     # thread = threading.Thread(target=main())
#     # thread.start()
#     exit(main())
