def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

a=int(input("Enter a Number"))
f=fact(a)
print("Factorial = ",f)

        
