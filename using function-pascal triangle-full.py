num = int(input("Enter the number of rows:"))  
  
for n in range(1, num+1):  
    for m in range(0, num-n+1):  
        print(' ', end='')  
  
   # first element is always 1  
    B = 1  
    for m in range(1, n+1):  
  
      # first value in a line is always 1  
      print(' ', B, sep='', end='')  
  
      # using Binomial Coefficient  
      BC = B * (n - m) // m 
    print()  