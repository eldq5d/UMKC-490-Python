# Write a python program to create and airline booking reservation system.


class Person:
    """A class representing a person"""

    lastname = ''
    firstname = ''

    def __init__(self, firstname, lastname):
        Person.firstname = firstname
        Person.lastname = lastname

    def get_info(self):
        return self.firstname, self.lastname


# inheritance
class Passenger(Person):
    """A subclass of person, representing passengers"""
    # __SSN represents a private data class
    def __init__(self, firstname, lastname, boardingNumber, __SSN):
        Person.__init__(self, firstname, lastname)
        self.boardingNumber = boardingNumber
        self.__SSN = __SSN

    def get_passenger(self):
        return Person.firstname, Person.lastname, self.boardingNumber, self.__SSN


class Employee(Person):
    """A subclass of person, representing employees"""

    def __init__(self, firstname, lastname, employeeNumber):
        Person.__init__(self, firstname, lastname)
        self.empNum = employeeNumber

    def get_employee(self):
        return Person.firstname, Person.lastname, self.empNum


class Flight:
    """A class representing flights"""

    airline = ''
    fltNumber = ''
    status = ''

    def __init__(self, fltNumber, airline, status):
        Flight.fltNumber = fltNumber
        Flight.airline = airline
        Flight.status = status

    def get_airline(self):
        return self.fltNumber, self.airline, self.status


# multiple inheritance demonstrated here
class Baggage(Person, Flight):
    """A sub-class of passenger, representing person baggage on flight"""

    def __init__(self, firstname, lastname, fltNumber, airline, status, numberOfBags, itemNumber):
        Person.__init__(self, firstname, lastname)
        Flight.__init__(self, fltNumber, airline, status)
        self.numberOfBags = numberOfBags
        self.itemNumber = itemNumber

    def get_baggage(self):
        return (Person.firstname, Person.lastname, Flight.fltNumber, Flight.airline,
                Flight.status, self.numberOfBags, self.itemNumber)

a = Person(Person.firstname, Person.lastname)
b = Passenger(Person.firstname, Person.lastname, "C12", "123-45-6789")
c = Employee(Person.firstname, Person.lastname, "07132")
d = Flight(Flight.fltNumber, Flight.airline, Flight.status)
e = Baggage("Emma", "Davis", "AA9172", "American Airlines", "Delayed", 1, "0024")

print(a.get_info())
print(e.get_baggage())
