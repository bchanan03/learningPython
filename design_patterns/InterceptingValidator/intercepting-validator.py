class InterceptingValidator:
    def __init__(self, validator):
        self.validator = validator

    def validate(self, data):
        if not self.validator.validate(data):
            print("Validation failed")
            return False
        print("Validation succeeded")
        return True


class NumbersValidator:
    def validate(self, data):
        return all(map(lambda x: x.isnumeric(), data))


class LettersValidator:
    def validate(self, data):
        return all(map(lambda x: x.isalpha(), data))


class PasswordValidator:
    def validate(self, data):
        return len(data) >= 8

def check_input(ival):
    # Your code goes here
    return None

if __name__ == "__main__":
    numbersVlidator = InterceptingValidator(NumbersValidator())
    numbersVlidator.validate("1234")
    numbersVlidator.validate("abcd")
    numbersVlidator.validate("1234abcd")

