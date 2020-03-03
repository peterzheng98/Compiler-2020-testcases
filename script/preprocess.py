#!/usr/bin/python

# examples
# //#include filename
# //#include filename TYPE:int

import argparse
import os
import sys


def include(filename, kv: dict):
    with open(filename, "r") as f:
        for line in f.readlines():
            for old, new in kv.items():
                line = line.replace(old, new)
            print(line, end="")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    args = parser.parse_args()
    directory, filename = os.path.split(args.input_file)
    os.chdir(directory)

    with open(filename) as f:
        for line in f.readlines():
            if not line.startswith("//#"):
                print(line, end="")
                continue
            if not line.startswith("//#include"):
                print("ignoring " + line, file=sys.stderr)
                continue
            args = line.split()
            args.pop(0)  # pop //#include
            filename = args[0].strip()
            kvs = [arg.strip().split(sep=":") for arg in args[1:]]
            kv = {k: v for k, v in kvs}
            include(filename, kv)


if __name__ == '__main__':
    main()
