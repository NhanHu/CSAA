class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def prinstname(self):
        print(self.firstname, self.lastname)
    

class Student(Person):
  def __init__(self, fname, lname, name):
    Person.__init__(self, fname, lname)
    self.name = name
  def printname(self):
        print(self.firstname, self.lastname, self.name)

x = Student("Mike", "Olsen", "Name")
x.prinstname()
