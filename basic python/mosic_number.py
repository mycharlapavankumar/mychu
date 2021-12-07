n=int(input('enter'))    
i=0
ans = 1
  
    # Iterate from 2 to the number 
for i in range(2,n+1): 
      # If i is the factor of n 
    if (n % i == 0 and n > 0): 
            count = 0
  
            # Find the count where i^count 
            # is a factor of n 
            while (n % i == 0): 
  
                # Divide the number by i 
                n //= i 
  
                # Increase the count 
                count+=1
              
  
            # Multiply the answer with 
            # count and i 
            ans *= count * i 
print(ans)
