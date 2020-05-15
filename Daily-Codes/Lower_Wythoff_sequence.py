
from math import sqrt, floor 
  
# Function to print the first n terms  
# of the lower Wythoff sequence  
def lowerWythoff(n) :  
  
    # Calculate value of phi  
    phi = (1 + sqrt(5)) / 2;  
  
    # Find the numbers  
    for i in range(1, n + 1) : 
  
        # a(n) = floor(n * phi)  
        ans = floor(i * phi);  
  
        # Print the nth numbers  
        print(ans,end="");  
  
        if (i != n) : 
            print( ", ",end = "");  
  
# Driver code  
if __name__ == "__main__" :  
  
    n = 5;  
    lowerWythoff(n); 