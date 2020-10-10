# Python code for simpson's 1 / 3 rule    
# Function for approximate integral 
def simpsons_( ll, ul, n ): 
  
    # Calculating the value of h 
    h = (ul - ll) / n
  
    # List for storing value of y 
    y = [3.1, 4.4, 6.4, 6.6, 5.9, 5.6, 5.1, 4.9, 4.6]
    
    # Calculating result 
    res = 0
    i = 0
    while i<= n: 
        if i == 0 or i == n: 
            res+= y[i] 
        elif i % 2 != 0: 
            res+= 4 * y[i] 
        else: 
            res+= 2 * y[i] 
        i+= 1
    res = res * (h / 3) 
    return res 
      
# Driver code
# Lower limit and upper limit
lower_limit = 1 
upper_limit = 9  

# Number of sub intervals
n = 8 

print ("The approximate total profit of the beverage company over nine-month" 
       "period is ", "%.4f" % simpsons_(lower_limit, upper_limit, n), 
       "in thousand of dollars. ") 


