#string are immutable
a="!!!!jinal!!!!!!"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("jinal","swastik"))
print(a.split(" "))
capital="introduction tO jS"
print(capital.capitalize())

str1="welcome  to the console!!!"
print(len(str1))
print(len(str1.center(40)))
print(a.count("jinal"))

str1="welcome  to the console!!!"
print(str1.endswith("!!!"))

str1="welcome  to the console!!!"
print(str1.endswith("to",4,10))

str1="he's name is dan. he is an honest man."
print(str1.find("ishh"))
# print(str1.index("ishh"))

str1="welcometotheconsole"
print(str1.isalnum())
str1="welcome000"
print(str1.isalpha())

str1="hello worldL"
print(str1.islower())

str1="we wish you a merry christmas\n"
print(str1.isprintable())
str1="       "  #using spacebar
print(str1.isspace())
str2="  "  #using tab 
print(str1.isspace())

str1="world health organization"
print(str1.istitle())

str2="to kill a mocking bird"
print(str2.istitle())

str1="python is interpreted language "
print(str1.startswith("python"))

str1="Python is Interpreted Language "
print(str1.swapcase())

str1="he's name is dan. he is an honest man."
print(str1.title())


