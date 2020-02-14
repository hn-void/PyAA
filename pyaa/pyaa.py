import argparse
import shutil
import time

import pyaa


python_aa = [
    " _____       _   _                 ",
    "|  __ \     | | | |                ",
    "| |__) |   _| |_| |__   ___  _ __  ",
    "|  ___/ | | | __| '_ \ / _ \| '_ \ ",
    "| |   | |_| | |_| | | | (_) | | | |",
    "|_|    \__, |\__|_| |_|\___/|_| |_|",
    "        __/ |                      ",
    "       |___/                       ",
]

SIZE_TERMINAL_COLUMNS = shutil.get_terminal_size().columns
SIZE_AA_COLUMNS = len(python_aa[0])
SIZE_AA_ROWS = len(python_aa)


def parse():
    usage = 'pyaa [--time TIME] [--red] [--green] [--blue]'
    parser = argparse.ArgumentParser(usage=usage)
    parser.add_argument(
        '-v',
        '--version',
        help='print product version and exit',
        action='version',
        version=pyaa.__version__)
    parser.add_argument(
        '-t',
        '--time',
        type=float,
        default=0.04,
        help='set sleep time(sec)')
    parser.add_argument(
        '-r',
        '--red',
        action='store_true',
        help='change font color to red')
    parser.add_argument(
        '-g',
        '--green',
        action='store_true',
        help='change font color to green')
    parser.add_argument(
        '-b',
        '--blue',
        action='store_true',
        help='change font color to blue')
    args = parser.parse_args()
    return args


def extract_aa(num, aa_list, from_left=True):
    extracted_aa = []
    for aa in aa_list:
        if from_left:
            extracted_aa.append(aa[:num])
        else:
            if num == 0:
                extracted_aa.append('')
            else:
                extracted_aa.append(aa[-num:])
    return extracted_aa


def main():
    args = parse()
    if args.red:
        print('\033[31m', end='')
    elif args.green:
        print('\033[32m', end='')
    elif args.blue:
        print('\033[34m', end='')

    for i in range(SIZE_TERMINAL_COLUMNS+SIZE_AA_COLUMNS):

        if i < SIZE_AA_COLUMNS:
            extracted_aa = extract_aa(i, python_aa, from_left=False)
        elif i <= SIZE_TERMINAL_COLUMNS:
            extracted_aa = python_aa
        else:
            extracted_aa = extract_aa(SIZE_TERMINAL_COLUMNS-i, python_aa)
        for line in extracted_aa:
            print(' '*(i-SIZE_AA_COLUMNS)+line+' '*(SIZE_TERMINAL_COLUMNS-i))

        time.sleep(args.time)
        print('\033[{n}F'.format(n=SIZE_AA_ROWS+1))
