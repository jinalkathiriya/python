# Default Arguments
def name(fname, mname = "Jinal", lname = "swastik"):
    print("Hello,", fname, mname, lname)
name("jinu")


# Keyword Arguments
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name(mname = "jinal", lname = "jitubhai", fname = "kathiriya")


# Variable length Arguments
# Arbitrary Arguments:
def name(*name):
    print("Hello,", name[0], name[1], name[2])

name("piyyu", "vraj", "swastik")
# Keyword Arbitrary Arguments:
def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname = "jinal", lname = "jitubhai", fname = "kathiriya")


# Required Arguments
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name("Peter", "Ego", "Quill")


def name(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname

print(name("James", "Buchanan", "Barnes"))