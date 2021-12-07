#
class Person:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def getName(self):
        return self.firstName + ' ' + self.lastName

class Employee(Person):

    def setWorkDetail(self, department, position):
        self.department = department
        self.position = position

    def getWorkDetail(self):
        return self.position + ', ' + self.department

emp1 = Employee('Mladen', 'Solomun')
emp1.setWorkDetail('Software Engineer', 'C++ programmer')

print('Name: ' + emp1.getName())
print('Work: ' + emp1.getWorkDetail())

emp2 = Employee('John', 'Askew')
emp2.setWorkDetail('Sound Engineer', 'Musical acoustics')

print('Name: ' + emp2.getName())
print('Work: ' + emp2.getWorkDetail())