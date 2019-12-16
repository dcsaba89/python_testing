import numpy as np
# import pandas as pd
import sys
ARGS = sys.argv[1:]


def ranger(n):
    if str(n).isnumeric():
        return range(np.int(n))
    else:
        raise ValueError("Pass exactly one integer argument")


def main(args):
    arg = args[0]
    r = ranger(arg)
    print(r)

    return 0


# main(ARGS)
