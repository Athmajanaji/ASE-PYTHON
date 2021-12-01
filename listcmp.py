s=0
s1=0
l=input("Enter List Of numbers")
l1=list(map(int,l.split(",")))
len1=len(l1)
print(len1)
#print(l1)
t=input("Enter List Of numbers")
l2=list(map(int,t.split(",")))
len2=len(l2)
print(len2)
if(len2==len1):
    print("Lists are of Same Length")
else:
    print("Lists are of different length")
for i in range(0,len1):
    s=l1[i]+s
for i in range(0,len2):
    s1=l2[i]+s1
if(s1==s):
    print("Sum OF Lists are Equal")
else:
    print("Sum of Lists are different")
#if(len1==len2):
for i in range(0,len1):
    for j in range(0,len2):
            if(l1[i]==l2[j]):
                print(l1[i])
            else:
                a=1

if(a==1):
    print("Lists Have different Elements")
    
s1=set(l1)
s2=set(l2)

print(s1)

    
