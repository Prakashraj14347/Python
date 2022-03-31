# file using normal 
f = open("C:/Besant tech/python/open and write 1.txt", "w")
f.write("hi all! welcome too!\n")
f.close()

f = open("C:/Besant tech/python/open and write 1.txt", "a")
f.write("BESANT TECHNOLOGY-tnagar!")
f.close()

# file using try and finally
try:
    f = open("C:/Besant tech/python/open and write 3.txt", "w")
    f.write("i love python!\n")
finally:
    f.close()
try:
    f = open("C:/Besant tech/python/open and write 3.txt", "a")
    f.write("i love programming!")
finally:
    f.close()
    
    
# file using with 
    
with open("C:/Besant tech/python/open and write 4.txt", "w") as f:
    f.write("another type of reader\n")
    f.close()
    
    
with open("C:/Besant tech/python/open and write 4.txt", "a") as f:
    f.write("with use of many contents")
    f.close()
    
        
