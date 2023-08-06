'''
Module containing utilities for generating, manipulating and verifing
Danish CPR-numbers.

This includes a HTTP server that generates CPR-numbers on demand.
'''

import argparse

from .generator import CPRGenerator
from .server import CPRGeneratorServer


def _get_parser():
    parser = argparse.ArgumentParser(
        prog='cpr-gen',
        description="An Unofficial tool for generating Danish CPR-numbers.")
    parser.add_argument('-n', '--numbers', dest='numbers', type=int, default=1)
    parser.add_argument('--hyphen', dest='hyphen', type=bool, default=False)
    parser.add_argument('-m', '--modulus11', dest='mod11', type=bool, default=True)

    return parser


def main_generator():
    parser = _get_parser()
    args = parser.parse_args()

    generator = CPRGenerator()
    cpr_numbers = generator.generate_iter(n=args.numbers,
                                          hyphen=args.hyphen,
                                          mod11=args.mod11)

    for cpr_number in cpr_numbers:
        print(cpr_number)


def main_server():
    server = CPRGeneratorServer()
    server.run()


if __name__ == '__main__':
    main_generator()
