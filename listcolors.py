
s1=input("enter the first set of colours  : ")
s2=input("enter the second set of colours : ")
s1=set(s1.split(" "))
s2=set(s2.split(" "))
s3=s1.difference(s2)
print(s3)
