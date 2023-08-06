'''
HTTP Server implemented using Flask for generating
Danish CPR-numbers on demand.
'''

from functools import reduce
from markupsafe import escape
from flask import Flask

from .generator import CPRGenerator

__all__ = ['CPRGeneratorServer']

app = Flask('cpr-gen')


@app.route('/')
def handle_default():
    generator = CPRGenerator()
    cpr_number = generator.generate()
    return f'{escape(cpr_number)}'


@app.route('/hyphen')
def handle_hyphen():
    generator = CPRGenerator()
    cpr_number = generator.generate(hyphen=True)
    return f'{escape(cpr_number)}'


@app.route('/no-mod11')
def handle_no_mod11():
    generator = CPRGenerator()
    cpr_number = generator.generate(mod11=False)
    return f'{escape(cpr_number)}'


@app.route('/no-mod11/hyphen')
def handle_no_mod11_hyphen():
    generator = CPRGenerator()
    cpr_number = generator.generate(mod11=False,
                                    hyphen=True)
    return f'{escape(cpr_number)}'


@app.route('/<int:numbers>')
def handle_numbers(numbers):
    generator = CPRGenerator()
    cpr_numbers = generator.generate_iter(n=numbers)
    return reduce(lambda a, b: a + ', ' + b,
                  [escape(str(number))
                   for number in cpr_numbers])


@app.route('/hyphen/<int:numbers>')
def handle_hyphen_numbers(numbers):
    generator = CPRGenerator()
    cpr_numbers = generator.generate_iter(n=numbers,
                                          hyphen=True)
    return reduce(lambda a, b: a + ', ' + b,
                  [escape(str(number))
                   for number in cpr_numbers])


@app.route('/no-mod11/<int:numbers>')
def handle_no_mod11_numbers(numbers):
    generator = CPRGenerator()
    cpr_numbers = generator.generate_iter(n=numbers,
                                          mod11=False)
    return reduce(lambda a, b: a + ', ' + b,
                  [escape(str(number))
                   for number in cpr_numbers])


@app.route('/no-mod11/hyphen/<int:numbers>')
def handle_no_mod11_hyphen_numbers(numbers):
    generator = CPRGenerator()
    cpr_numbers = generator.generate_iter(n=numbers,
                                          hyphen=True,
                                          mod11=False)
    return reduce(lambda a, b: a + ', ' + b,
                  [escape(str(number))
                   for number in cpr_numbers])


class CPRGeneratorServer:

    def run(self):
        app.run()
