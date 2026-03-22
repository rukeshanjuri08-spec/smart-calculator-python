import math

while True:
    print("\n---calculator---")
    print("1.add")
    print("2.subtract")
    print("3.multiply")
    print("4.divide")
    print("5.modulus")
    print("6.exit")
    choice=input("enter choice:")
    if choice=="6":
     print("exiting...")
     break

    a=float(input("enater first number:"))
    b=float(input("enter second number:"))

    if choice =="1":
     print("result:",a+b)
    
    elif choice =="2":
     print("result:",a-b)
    
    elif choice =="3":
     print("result:",a*b)
    
    elif choice =="4":
      if b == 0:
       print("cannot divide by zero")
      else:
       print("result:", a/b)
    
    elif choice =="5":
       print("result:",a%b)

    else:
       print("invalid choise")
