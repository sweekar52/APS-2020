def findNumbers(n) : 
  
    # Append 'F' (N - 1) times  
    ans = 'F'*(n - 1);  
  
    # Append 'E' for an even number  
    even = ans + 'E';  
  
    # Append 'F' for an odd number  
    odd = ans + 'F';  
  
    print("Even: " , even);  
    print( "Odd: " , odd);  
  
# Driver code  
if __name__ == "__main__" : 
  
    n = 2;  
  
    findNumbers(n);  