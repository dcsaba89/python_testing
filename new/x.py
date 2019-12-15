import numpy as np
# import pandas as pd
import sys
ARGS = sys.argv[1:]


def ranger(n):
    if str(n).isnumeric():
        i = 0
        a = []
        while i < 2*n:
            if i % 2 == 0:
                a.append(np.int(i/2))
                i += 1
            else:
                i -= 1
            i += 1
        return np.array(a)
    else:
        raise ValueError("Pass exactly one integer argument")


def main(args):
    arg = args[0]
    r = ranger(arg)
    print(r)

    return 0


# main(ARGS)
