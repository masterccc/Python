#!/usr/bin/env python
#-*-coding:UTF-8-*-

import argparse

def display(first_color, letter, data):
	return green + data + default + " -> " + green + ("{0:"+letter+"}").format(int(data)) + default

parser = argparse.ArgumentParser(description="")
parser.add_argument("Data", type=str, metavar="Data", help="Data to convert, must be an integer.")
parser.add_argument("Key", type=str, metavar="Key", help="Integer convert to b = Binary, x = Hexa or o = Octal.")

args = parser.parse_args()
# Colors
green = "\033[1:32m"
warning ="\033[1:33m" 
default = "\033[0m" 

error_msg = warning + "[Error] Impossible to convert your datas with this key." + default

tformat = args.Key.lower()

try:
	print display(green, tformat, args.Data) if (tformat in ["x","b","o"]) else error_msg
except ValueError as e:
    print warning + "[ValueError] The data must be integer." + default

