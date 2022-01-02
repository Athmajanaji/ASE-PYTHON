a=int(input("Enter first number"))
if a%4==0 or a%400 and a%100!=0:
    print("leap year")
else:
    print("not a leap year")
