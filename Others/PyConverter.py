#!/usr/bin/env python
#-*-coding:UTF-8-*-

import argparse

parser = argparse.ArgumentParser(description="")
parser.add_argument("Data", type=str, metavar="Data", help="Data to convert, must be an integer.")
parser.add_argument("Key", type=str, metavar="Key", help="Integer convert to b = Binary, x = Hexa or o = Octal.")

args = parser.parse_args()

# Colors
green = "\033[1:32m"
warning ="\033[1:33m" 
default = "\033[0m" 

try:
    if args.Key == "x" or args.Key == "X":
        print green + args.Data + default + " -> " + green + "{0:x}".format(int(args.Data)) + default
    elif args.Key == "b" or args.Key == "B":
        print green + args.Data + default + " -> " + green + "{0:b}".format(int(args.Data)) + default
    elif args.Key == "o" or args.Key == "O":
        print green + args.Data + default + " -> " + green + "{0:o}".format(int(args.Data)) + default
    else:
        print warning + "[Error] Impossible to convert your datas with this key." + default
except ValueError as e:
    print warning + "[ValueError] The data must be integer." + default

