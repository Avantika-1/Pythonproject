fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020
car["color"] = "red"
print(car)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":

        continue

print(x)

for x in range (6):
  print(x)

class Person:
     def __init__(self, fname):
         self.firstname = fname

    def printname(self):
        print(self.firstname)

class Student(Person):
  pass

x = Student("Mike")
x.printname()

import keyword
print(keyword.kwlist)
