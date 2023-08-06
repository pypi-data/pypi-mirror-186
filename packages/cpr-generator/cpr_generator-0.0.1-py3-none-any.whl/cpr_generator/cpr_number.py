'''
'''


class CPRNumber:
    '''
    Structure representing a Danish CPR-number (personnummer).
    '''

    def __init__(self, day: int, month: int, year: int, control_cipher: str):
        self._day = day
        self._month = month
        self._year = year
        self._control_cipher = control_cipher
