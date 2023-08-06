'''
This module contains utilities for generating and
verifying Danish CPR-numbers according to the rules
specified by the Danish 'Det Centrale Personregister'
https://cpr.dk/media/12066/personnummeret-i-cpr.pdf

Note: This software is a community project and is NOT
officially issued by the Danish Authorities, and thus
may contain bugs.
'''

from datetime import date
from random import seed, randint, choice

__all__ = ['CPRGenerator']


class CPRGenerator:
    '''
    Utility for generating a Danish CPR-number (personnummer).
    '''

    def __init__(self, rand_seed=None):
        if rand_seed:
            seed(rand_seed)

    def _is_leap_year(self, year: int) -> bool:
        '''
        Checks whether a given year is a leap year.
        '''
        if year < 0:
            raise ValueError("Year cannot be negative.")

        if year % 400 == 0:
            return True
        if year % 100 == 0:
            return False
        if year % 4 == 0:
            return True

        return False

    def _generate_loebenummer(self, year: int) -> tuple[int, int, int]:
        '''
        Generates the seventh, eighth and ninth numbers
        in a Danish CPR-number according to the rules based
        on the year in which a person is born.
        This number is called "Løbenummer" is Danish.
        '''
        if not (1900 <= year <= 2057):
            raise ValueError("Year must be between 1900 and 2057 (inclusive).")

        seven = 0
        eight = 0
        nine = 0

        match year:
            case year if year <= 1936:
                seven = randint(0, 3)
                eight = randint(0, 9)
                nine = randint(0, 9)
            case year if 1937 <= year <= 1999:
                seven = choice([0, 1, 2, 3, 4, 9])
                eight = randint(0, 9)
                nine = randint(0, 9)
            case year if 2000 <= year <= 2036:
                seven = randint(4, 9)
                eight = randint(0, 9)
                nine = randint(0, 9)
            case year if year >= 2037:
                seven = randint(5, 8)
                eight = randint(0, 9)
                nine = randint(0, 9)

        return seven, eight, nine

    def _generate_control_ciphers(self,
                                  day: int,
                                  month: int,
                                  year: int,
                                  mod11: bool = True) -> str:
        '''
        Generates the last four ciphers in a Danish CPR-number.
        The generation is based on the birthday of the person.
        By default the numbers is generated such that it satisfies
        the modulus-11 control condition, but this can be turned of
        by setting the `mod11` parameter to `False`.
        '''
        if mod11:
            rest = 1
            while rest == 1:
                seven, eight, nine = self._generate_loebenummer(year)

                one = day // 10
                two = day % 10
                three = month // 10
                four = month % 10

                year = year % 100

                five = year // 10
                six = year % 10

                # Calculate the control rest according to specification.
                rest = sum([
                    one * 4,
                    two * 3,
                    three * 2,
                    four * 7,
                    five * 6,
                    six * 5,
                    seven * 4,
                    eight * 3,
                    nine * 2,
                ]) % 11

            ten = 11 - rest
            return str(seven) + str(eight) + str(nine) + str(ten)
        else:
            # Modulus 11 doesn't matter so just gimme four random digits.
            def rand():
                return randint(0, 9)

            return str(rand()) + str(rand()) + str(rand()) + str(rand())

    def generate(self, hyphen: bool = False, mod11: bool = True) -> str:
        '''
        Randomly generates a Danish CPR-number for a hypothetical citizen
        born between 1900 and the current year.
        The number may be generated with or without a hyphen between
        the 6th and 7th digit using the `hyphen` parameter.

        By default the numbers is generated such that it satisfies the
        modulus-11 control condition for persons born between 1900 and 2007,
        but this can be turned off by setting the `mod11` parameter to `False`.
        '''
        month = randint(1, 12)
        current_year = date.today().year

        year = randint(1900, current_year)

        # If born in 2007 or later, don't enforce modulus-11.
        if year >= 2007:
            mod11 = False

        # Select a random, valid day according to the Gregorian Calendar.
        match month:
            case 1 | 3 | 5 | 7 | 8 | 10 | 12:
                day = randint(1, 31)
            case 4 | 6 | 9 | 11:
                day = randint(1, 30)
            case 2:
                if self._is_leap_year(year):
                    day = randint(1, 29)
                else:
                    day = randint(1, 28)

        # Generate the four last digits.
        control_cipher = self._generate_control_ciphers(day, month, year, mod11)

        # Remove the millenium and century.
        year = year % 100

        # Format the first six digits.
        year = '0' + str(year) if year < 10 else str(year)
        day = '0' + str(day) if day < 10 else str(day)
        month = '0' + str(month) if month < 10 else str(month)

        if hyphen:
            return day + month + year + '-' + control_cipher
        else:
            return day + month + year + control_cipher
