class Person:
    def __init__(self, name, fname, age, address, phone):
        self.name = name
        self.fname = fname
        self.age = age
        self.address = address
        self.phone = phone


class PersonArray:
    def __init__(self):
        self.persons = []
        self.size = 0

    def add_person(self, name, fname, age, address, phone):
        person = Person(name, fname, age, address, phone)
        self.persons.append(person)
        self.size += 1

    def remove_person(self, name, fname):
        for person in self.persons:
            if person.name == name and person.fname == fname:
                self.persons.remove(person)
                self.size -= 1

    def __str__(self):
        result = ""
        for person in self.persons:
            result = result + f"""
name: {person.name}
family name: {person.fname}
age: {person.age}
address: {person.address}
phone: {person.phone}
"""
        return result
