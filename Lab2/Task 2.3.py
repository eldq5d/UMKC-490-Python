# Write a python program to create the following management system.
# 1. Airline Booking Reservation System (classes for Flight,Person,Employee,Passenger etc.)
#
# Prerequisites:
# Your code should have at least five classes.
# Your code should have _init_ constructor in all the classes
# Your code should show inheritance at least once
# Your code should have one super call
# Use of self is required
# Use at least one private data member in your code
# Use multiple Inheritance at least once
# Create instances of all classes and show the relationship between them
# Your submission code should point out where all these things are present


class Person:
    """A class representing a person"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return self.name, self.age


class Passenger(Person):
    """A subclass of person, representing passengers"""

    def __init__(self, boardingNumber, __SSN, age, name):
        Person.__init__(self, age, name)
        self.boardingNumber = boardingNumber
        self.__SSN = __SSN

    def get_passenger(self):
        return self.name, self.age, self.boardingNumber, self.__SSN


class Employee(Person):
    """A subclass of person, representing employees"""

    def __init__(self, name, age, employeeNumber):
        Person.__init__(self, name, age)
        self.empNum = employeeNumber

    def get_employee(self):
        return self.name, self.age, self.empNum


class Flight:
    """A class representing flights"""

    def __init__(self, fltNumber, airline, status):
        self.fltNumber = fltNumber
        self.airline = airline
        self.status = status

    def get_airline(self):
        return self.fltNumber, self.airline, self.status


class Baggage(Person, Flight):
    """A sub-class of passenger, representing passenger baggage on flight"""

    def __init__(self, name, age, fltNumber, airline, status, numberOfBags, itemNumber):
        Person.__init__(self, name, age)
        Flight.__init__(self, fltNumber, airline, status)
        self.numberOfBags = numberOfBags
        self.itemNumber = itemNumber

    def get_baggage(self):
        return self.name, self.age, self.fltNumber, self.airline, self.status, self.numberOfBags, self.itemNumber

a = Person("Emma", 25)
b = Passenger("Emma", 25, "C12", "123-45-6789")
c = Employee("Jeanie", 51, "07132")
d = Flight("AA9172", "American", "Delayed")
e = Baggage("Emma", 25, "C12", "American", "On-time", 1, "0024")

print(a.get_info())
print(b.get_passenger())
print(c.get_employee())
print(d.get_airline())
print(e.get_baggage())
