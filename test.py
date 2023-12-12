print("""Operations:
      
      *************
      1- Addition
      2- Subtraction
      3- Multiplication
      4- Division
      *************
      
      """)

while(True):
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))

    select = input("Select Operation: ")

    if select == "1":
        print("Result: ".format(a,b), a+b)
    elif select == "2":
        print("Result: ".format(a,b), a-b)
    elif select == "3":
        print("Result: ".format(a,b), a*b)
    elif select == "4":
        print("Result: ".format(a,b), a/b)
    else:
        print("Invalid Operation")
        break