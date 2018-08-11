class Person:
    num_of_person = 0

    def __init__(self, fname, lname, address):
        self.fnamae = fname
        self.lname = lname
        self.address = address
        self.email = fname + '.' + lname + '@company.com'
        Person.num_of_person += 1

    def get_fullname(self):
        return '{} {}'.format(self.fnamae, self.lname)

    @classmethod
    def set_person_name(cls, num_of_person):
        cls.num_of_person = num_of_person


class Employee(Person):
    pass


Employee.set_person_name(100)

p1 = Employee('Budi', 'Anduk', 'Kota Garut')
p2 = Employee('Wati', 'Gehu', 'Kota Bogor')

#Print Employeeeee
print(Employee.num_of_person)
