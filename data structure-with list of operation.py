a=["apple","banana","lemon"]
b=["carrot","raddish","onion"]
c=[13,7,5]
d=[14.09,19.83,24.05]
e=[14, 19, 11, 3, 13, 7, 17, 5, 2]
f=['T.nagar','Technology','Besant']



# APPEND (add a single element to the end of the list)
a.extend(["jackfriut"])
print(a)
b.extend(["brinjal"])
print(b)
c.extend(["25"])
print(c)
d.extend(["23.98"])
print(d)

# REPLACE
a[0]="green apple"
print(a)
b[1]="tomato"
print(b)
c[2]="28"
print(c)
d[0]="89.98"
print(d)

# INSERT
a.insert(2,"strawberry")
print(a) 
b.insert(0,"tomato")
print(b)
c.insert(2,"89")
print(c)
d.insert(2,"85.104")
print(d)

# DELETE
del a[0]
print(a)
del b[0]
print(b)
del c[2]
print(c)
del d[3]
print(d)

# POP
a.pop(0)
print(a)
b.pop(2)
print(b)
c.pop(1)
print(c)
d.pop(2)
print(d)

#SORT
e.sort()
print(e)

#REVERSE
reversed_list = f[::-1]
print(reversed_list)

#FLOAT to INTEGER
d= int(14.09)
print(d)

#COMBINE
print(a, b,c,d,e,f)