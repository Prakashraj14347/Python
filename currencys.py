print('select currency')
print('1 dollar to inr')
print('2 inr to dollar')
print('3 euro to inr')
print('4 inr to euro')
condition=int(input('select choice'))
if condition ==1:
    dollar=int(input("enter amount in dollars:"))
    inr_1=(dollar*75)
    print(inr_1)
elif condition==2:
    inr=int(input("enter amount in inr:"))
    dollar_1=(inr/75)
    print(dollar_1)
elif condition==3:
    euro=int(input("enter amount in euro: "))
    inr_2=(euro*100)
    print(inr_2)
elif condition==4:
    inr_3=int(input("enter amount in inr:"))
    EURO_1=(inr_3/100)
    print (EURO_1)
else: 
    print("invalid input")