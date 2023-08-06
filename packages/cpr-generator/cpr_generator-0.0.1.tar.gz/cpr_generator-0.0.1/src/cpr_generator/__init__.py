'''
'''

from .generator import CPRGenerator


def main():
    generator = CPRGenerator
    cpr_number = generator.generate()
    print(cpr_number)


if __name__ == '__main__':
    main()
