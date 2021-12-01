a=input("Enter a number")
l=a.split(",")
b=list(map(int,l))
c=len(b)
for i in range(0,c):
    if b[i]>100:
        b[i]="over"
print(b)
