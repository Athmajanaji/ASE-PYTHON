a=input("Enter a string :")
b=a[0]
b=b.lower()
a= a.replace(b,'$')    
print(b+a[1:])
