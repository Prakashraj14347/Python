print("***Temperature Coversion***")
print("1.Celsius to Fahrenheit \n2.Fahrenheit to Celsius")
selection = int(input())

def fahren(temp)    :
    converted = (temp*1.8) + 32
    return converted

def celsius(temp)    :
    converted = (temp - 32) * 0.6
    return converted


if(selection == 1):
    print("Enter the celsius value")
    temp = float(input())
    print("Celsius to Fahrenheit")
    print("The coverted temperature is ",fahren(temp),"°F")
elif(selection == 2):
    print("Enter the fahrenheit value")
    temp = float(input())
    print("Fahrenheit to Celsius")
    print("The coverted temperature is ",celsius(temp),"°C")
else:
    print("Please enter a valid input") 