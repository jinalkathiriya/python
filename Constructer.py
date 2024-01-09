class Person:

  def __init__(self, name, occ):
    print("Hey I am a person")
    self.name = name
    self.occ = occ

  def info(self):
    print(f"{self.name} is a {self.occ}")


a = Person("Jinal", "Developer")
b = Person("swastik", "HR") 
a.info()
b.info()
# print(a.name)
# a.name = "swastik"
# a.occ = "HR"
# a.info()
