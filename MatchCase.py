x=int(input("Enter the value of x: "))
# x is the variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")

    # case with if-condition
    # case 4 if x % 2 == 0:
        # print("x%2==0 and case is 4")

    #Empty case with if-conditon
    # case _ if x<10:
        # print("x is <10")

    case 4:
        print("case is 4")

    case _ if x!=90:
        print(x, "is not 90")
    case _ if x!=80:
        print(x, "is not 80")
    case _:
        print(x)