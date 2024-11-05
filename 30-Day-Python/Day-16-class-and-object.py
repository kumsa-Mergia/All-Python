
class Person:
  name = "Harry"
  occupation = "Software Developer"
  networth = 10
  def info(self):
    print(f"{self.name} is a {self.occupation}")


a = Person()
b = Person()
c = Person()

a.name = "solomon"
a.occupation = "Accountant"

b.name = "Makda"
b.occupation = "HR"

# print(a.name, a.occupation)
a.info()
b.info()
c.info()
