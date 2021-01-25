import argparse
import shutil
import time

import pyaa
from pyaa.utils.formatting import (
    extract_aa,
    animation_with_2,
)

PUSHEEN = [
    '   ▐▀▄       ▄▀▌   ▄▄▄▄▄▄▄              ',
    '   ▌▒▒▀▄▄▄▄▄▀▒▒▐▄▀▀▒██▒██▒▀▀▄           ',
    '  ▐▒▒▒▒▀▒▀▒▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀▄         ',
    '  ▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▒▒▒▒▒▒▒▒▒▒▒▒▀▄       ',
    '▀█▒▒▒█▌▒▒█▒▒▐█▒▒▒▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌      ',
    '▀▌▒▒▒▒▒▒▀▒▀▒▒▒▒▒▒▀▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐   ▄▄ ',
    '▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌▄█▒█ ',
    '▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒█▀  ',
    '▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▀    ',
    '▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌     ',
    ' ▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐      ',
    ' ▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌      ',
    '  ▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐       ',
    '  ▐▄▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▌       ',
    '    ▀▄▄▀▀▀▀▀▄▄▀▀▀▀▀▀▀▄▄▀▀▀▀▀▄▄▀         ',
]

PUSHEEN_SWING = [
    '   ▐▀▄       ▄▀▌   ▄▄▄▄▄▄▄              ',
    '   ▌▒▒▀▄▄▄▄▄▀▒▒▐▄▀▀▒██▒██▒▀▀▄           ',
    '  ▐▒▒▒▒▀▒▀▒▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀▄         ',
    '  ▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▒▒▒▒▒▒▒▒▒▒▒▒▀▄       ',
    '▀█▒▒▒█▌▒▒█▒▒▐█▒▒▒▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌      ',
    '▀▌▒▒▒▒▒▒▀▒▀▒▒▒▒▒▒▀▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐      ',
    '▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐     ',
    '▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐▄    ',
    '▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▐▄  ',
    '▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌▀▌▒█ ',
    ' ▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐   ▀▀ ',
    ' ▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌      ',
    '  ▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐       ',
    '  ▐▄▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▌       ',
    '    ▀▀▄▄▀▀▀▄▄▀▀▀▀▀▀▀▀▀▀▄▄▀▀▀▀▄▄▀        ',
]

SIZE_TERMINAL_COLUMNS = shutil.get_terminal_size().columns
SIZE_AA_COLUMNS = len(PUSHEEN[0])
SIZE_AA_ROWS = len(PUSHEEN)


def parse():
    usage = 'pusheen [--run] [--time TIME] [--percentage PERCENTAGE]'
    parser = argparse.ArgumentParser(usage=usage)
    parser.add_argument(
        '-v',
        '--version',
        help='print product version and exit',
        action='version',
        version=pyaa.__version__,
    )
    parser.add_argument(
        '-r',
        '--run',
        action='store_true',
        help='pusheen will run',
    )
    parser.add_argument(
        '-t',
        '--time',
        type=float,
        default=0.04,
        help='set sleep time',
    )
    parser.add_argument(
        '-p',
        '--percentage',
        type=int,
        default=45,
        choices=range(0, 100+1),
        help='set percentage of distance (0 to 100)',
    )
    args = parser.parse_args()
    return args


def main():
    args = parse()
    if args.run:
        args.time = 0.01
        for i in range(SIZE_TERMINAL_COLUMNS+SIZE_AA_COLUMNS):
            swing_pusheen = animation_with_2(i, 10, PUSHEEN, PUSHEEN_SWING)
            if i < SIZE_AA_COLUMNS:
                extracted_aa = extract_aa(i, swing_pusheen, from_left=True)
            elif i <= SIZE_TERMINAL_COLUMNS:
                extracted_aa = swing_pusheen
            else:
                extracted_aa = extract_aa(SIZE_TERMINAL_COLUMNS-i, swing_pusheen, from_left=False)
            for line in extracted_aa:
                print(' '*(SIZE_TERMINAL_COLUMNS-i)+line+' '*(i-SIZE_AA_COLUMNS))
            time.sleep(args.time)
            print('\033[{n}F'.format(n=SIZE_AA_ROWS+1))

    else:
        SIZE_TERMINAL_COLUMNS_TMP = int(SIZE_TERMINAL_COLUMNS*args.percentage/100)
        if SIZE_TERMINAL_COLUMNS_TMP < SIZE_AA_COLUMNS:
            for i in range(SIZE_TERMINAL_COLUMNS_TMP*2):
                swing_pusheen = animation_with_2(i, 10, PUSHEEN, PUSHEEN_SWING)
                if i < SIZE_TERMINAL_COLUMNS_TMP:
                    extracted_aa = extract_aa(i, swing_pusheen, from_left=True)
                    for line in extracted_aa:
                        print(' '*((SIZE_TERMINAL_COLUMNS-SIZE_TERMINAL_COLUMNS_TMP)+SIZE_TERMINAL_COLUMNS_TMP-i)+line)
                else:
                    extracted_aa = extract_aa(SIZE_TERMINAL_COLUMNS_TMP*2-i, swing_pusheen, from_left=True)
                    for line in extracted_aa:
                        print(' '*((SIZE_TERMINAL_COLUMNS-SIZE_TERMINAL_COLUMNS_TMP)+i-SIZE_TERMINAL_COLUMNS_TMP)+line)
                time.sleep(args.time)
                print('\033[{n}F'.format(n=SIZE_AA_ROWS+1))

        else:
            for i in range(SIZE_TERMINAL_COLUMNS_TMP*2):
                swing_pusheen = animation_with_2(i, 10, PUSHEEN, PUSHEEN_SWING)
                if i < SIZE_AA_COLUMNS:
                    extracted_aa = extract_aa(i, swing_pusheen, from_left=True)
                    for line in extracted_aa:
                        print(
                            ' '*((SIZE_TERMINAL_COLUMNS-SIZE_TERMINAL_COLUMNS_TMP)+SIZE_TERMINAL_COLUMNS_TMP-i) +
                            line+' '*(i-SIZE_AA_COLUMNS))
                elif i <= SIZE_TERMINAL_COLUMNS_TMP:
                    extracted_aa = swing_pusheen
                    for line in extracted_aa:
                        print(
                            ' '*((SIZE_TERMINAL_COLUMNS-SIZE_TERMINAL_COLUMNS_TMP)+SIZE_TERMINAL_COLUMNS_TMP-i) +
                            line+' '*(i-SIZE_AA_COLUMNS))
                elif i <= SIZE_TERMINAL_COLUMNS_TMP*2-SIZE_AA_COLUMNS:
                    extracted_aa = swing_pusheen
                    for line in extracted_aa:
                        print(
                            ' '*((SIZE_TERMINAL_COLUMNS-SIZE_TERMINAL_COLUMNS_TMP)+i-SIZE_TERMINAL_COLUMNS_TMP) +
                            line+' '*(SIZE_AA_COLUMNS-i))
                else:
                    extracted_aa = extract_aa(SIZE_TERMINAL_COLUMNS_TMP*2-i, swing_pusheen, from_left=True)
                    for line in extracted_aa:
                        print(
                            ' '*((SIZE_TERMINAL_COLUMNS-SIZE_TERMINAL_COLUMNS_TMP)+i-SIZE_TERMINAL_COLUMNS_TMP) +
                            line+' '*(SIZE_AA_COLUMNS-i))
                time.sleep(args.time)
                print('\033[{n}F'.format(n=SIZE_AA_ROWS+1))
