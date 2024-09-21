from random import randint

# director class
class Director:
    def __init__(self, builder):
        self._builder = builder

    def construct(self):
        self._builder.generate_id()
        self._builder.account_type()
        self._builder.clearance()

    def get_student_account(self):
        return self._builder.get_student_account()


# student account builder class
class StudentAccountBuilder:
    def __init__(self):
        self._student_account = None

    # generate random id with n digits
    def _random_id_with_n_digits(self, n):
        range_start = 10**(n-1)
        range_end = (10**n)-1
        return randint(range_start, range_end)

    def generate_id(self): pass
    def account_type(self): pass
    def clearance(self): pass

    def get_student_account(self):
        return self._student_account

# student account class
class StudentAccount:
    def __init__(self, student_type):
        self.student_type = student_type
        self.account_id = None
        self.clearance = None

    def __str__(self):
        return f"Student ID: {self.student_id} | Account Type: {self.account_type} | Clearance: {self.clearance}"


class NetanyaAccademicCollegeBuilder(StudentAccountBuilder):
    def __init__(self):
        super().__init__()
        self._student_account = StudentAccount('Netanya Accademic College')

    def generate_id(self):
        self._student_account.student_id = self._random_id_with_n_digits(5)

    def account_type(self):
        self._student_account.account_type = 'Netanya Accademic College account'

    def clearance(self):
        self._student_account.clearance = 'Netanya Accademic College clearance'


if __name__ == "__main__":
    netanya_accademic_college_builder = NetanyaAccademicCollegeBuilder()
    director = Director(netanya_accademic_college_builder)
    director.construct()
    student_account = director.get_student_account()
    print(student_account)