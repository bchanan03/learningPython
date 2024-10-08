class InterceptingValidator:
    def __init__(self, input):
        self._validator = None
        self._input = input

    def set_validator(self, validator):
        self._validator = validator

    def validate(self):
        return self._validator.validate(self._input)


class NumberValidator:
    """Checks if the input is a number or not """

    def validate(self, input):
        int_or_not = True
        try:
            user_input = int(input)
            print("Your input " + str(user_input) + " is an integer!")
        except ValueError:
            print("Your input " + input + " is not an integer!")
            int_or_not = False

        return int_or_not


def check_input(ival):
    number_validator = InterceptingValidator(ival)
    number_validator.set_validator(NumberValidator())
    return number_validator.validate()


if __name__ == "__main__":
    check_input('1234')