a= [1,2,3,4,5]
found=0
n=int(input("enter a number"))
print ("enter n number")
for i in range (0,n):
    a[i]=int(input())
key=int(input("enter key to be searched !"))
for i in range (0,n):
    if key ==a[i]:
        print ("key found")
        found +=1
    else:
        continue
    if found ==0:
        print ("key not found")
         