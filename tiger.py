#! /usr/bin/env python
#
# Do not modify

from optparse import OptionParser
from parser.parser import parse
import sys

parser = OptionParser()
parser.add_option("-d", "--dump",
                  help="dump input file to output",
                  action="store_true", default=False,
                  dest="dump")
parser.add_option("-e", "--eval",
                  help="evaluate input file to output",
                  action="store_true", default=False,
                  dest="eval")
parser.usage = """%prog [options] [file]"""
parser.description = "Compile a Tiger program (or standard input)"

(options, args) = parser.parse_args()

if len(args) > 1:
    parser.print_help(file=sys.stderr)
    sys.exit(1)

fd = open(args[0]) if args else sys.stdin
content = fd.read()
fd.close()

tree = parse(content)

if options.dump:
    from parser.dumper import Dumper
    print(tree.accept(Dumper()))

if options.eval:
    from ast.evaluator import Evaluator
    print("Evaluating: %s" % tree.accept(Evaluator()))