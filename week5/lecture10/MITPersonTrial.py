# -*- coding: utf-8 -*-
"""
Created on Wed May 18 08:10:59 2016

@author: ericgrimson
"""
from week5.lecture10.PersonTrial import Person


class MITPerson(Person):
    nextIdNum = 0  # next ID number to assign

    def __init__(self, name):
        Person.__init__(self, name)  # initialize Person attributes
        # new MITPerson attribute: a unique ID number
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1

    def getIdNum(self):
        return self.idNum

    # sorting MIT people uses their ID number, not name!
    def __lt__(self, other):
        return self.idNum < other.idNum

    def speak(self, utterance):
        return (self.getLastName() + " says: " + utterance)

    def __str__(self):
        """return self's name"""
        return "Name {}, id {}, age {}".format(self.name, self.getIdNum(), self.getAge())


# example usage

m3 = MITPerson('Mark Zuckerberg')
Person.setBirthday(m3, 5, 14, 1984)
m2 = MITPerson('Drew Houston')
Person.setBirthday(m2, 3, 4, 1983)
m1 = MITPerson('Bill Gates')
Person.setBirthday(m1, 10, 28, 1955)

MITPersonList = [m1, m2, m3]

for e in MITPersonList:
    print(e)

print()
# default sort based on idNum
MITPersonList.sort()
print("-> Default sort based on idNum")
for e in MITPersonList:
    print(e)

print()
# sort based on lastName
MITPersonList = sorted(MITPersonList, key=lambda e: e.lastName)
print("-> sort based on last name")
for e in MITPersonList:
    print(e)


# sort based on age
def age_sort(person):
    return person.getAge()

print()
MITPersonList = sorted(MITPersonList, key=age_sort)
print("-> sort based on age")
for e in MITPersonList:
    print(e)

# p1 = MITPerson('Eric')
# p2 = MITPerson('John')
# p3 = MITPerson('John')
# p4 = Person('John')

# p1<p2
# p1<p4

# p4<p1
