__author__ = "Enrique Rodriguez"
__version__ = "1.0.0"
__maintainer__ = "Enrique Rodriguez"
__email__ = "rodriguez.enrique.pr@gmail.com"
__status__ = "Production"


import re
import os
import sys
import argparse
from .sql_minifier import SQLMinifier


def read_from_file(path):
    if not os.path.exists(path):
        stderr(f"The file '{path}' was not found.")
        sys.exit(1)
    fd = open(path)
    sql = fd.read()
    fd.close()
    return sql


def stderr(s):
    sys.stderr.write(f"Error: {s}\n")


def stdout(s):
    sys.stdout.write(s+"\n")


def main():
    parser = argparse.ArgumentParser(
        prog='SQLMin',
        description='Shrinks SQL into a single line',
        epilog='Disclaimer: %(prog)s assumes that the given sql syntax is correct and compiles successfully.'
    )

    parser.add_argument('sql', help='an sql query string')
    parser.add_argument('-f', '--file', help='set the sql parameter as a path to a file',
                        action=argparse.BooleanOptionalAction)

    args = parser.parse_args()
    sql = args.sql
    if args.file:
        sql = read_from_file(os.path.expanduser(args.sql))
    
    minifier = SQLMinifier()
    stdout(minifier.minify(sql))


if __name__ == "__main__":
    main()
