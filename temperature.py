condition=int(input('select\n1-celcoius \n2-farenheit\nselect any one as above mentioned\n'))
if condition==1:
    celcious=float(input("enter celcious"))
    farenheit_1=(celcious*100)
    print(farenheit_1)
elif condition==2:
    farenheit=float(input("enter farenheit"))
    celcious_2=(farenheit*200)
    print(celcious_2)
else:
    print("invalid input") 
    
