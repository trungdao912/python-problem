from enums import Session


class InvalidValueException(Exception):
    pass


class Step:
    def __init__(self, number_of_sessions: int, number_of_star: str):
        self.number_of_sessions = number_of_sessions
        self.number_of_star = number_of_star
        self.number_convert = Session.NUMBER_TO_TEXT_MAP
        self.string_convert = Session.TEXT_TO_NUMBER_MAP

    def make_steps(self):
        str = 'I completed {} sessions and I rated my expert {} stars'.format(
            self.number_of_sessions, self.number_of_star)
        splitted_string = str.split(' ')

        try:
            splitted_string[2] = self.number_convert[splitted_string[2]]
            splitted_string[-2] = self.string_convert[splitted_string[-2]]
        except KeyError:
            raise InvalidValueException("Out of index key")

        return ' '.join(splitted_string)


Step(10, 'five').make_steps()
