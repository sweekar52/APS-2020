# gcd of a and b  
def gcd(a, b): 
  
    # Everything divides 0  
    if (a == 0):  
        return b;  
    if (b == 0):  
        return a;  
      
    # base case  
    if (a == b):  
        return a;  
      
    # a is greater  
    if (a > b):  
        return gcd(a - b, b);  
    return gcd(a, b - a);  
  
# Function to return the LCM  
# of three numbers 
def LCM(x, y, z): 
    ans = ((x * y) / (gcd(x, y))); 
    return ((z * ans) / (gcd(ans, z))); 
  
# Function to return the largest n-digit 
# number which is divisible by x, y and z 
def findDivisible(n, x, y, z): 
      
    # find the LCM 
    lcm = LCM(x, y, z); 
      
    # find largest n-digit number 
    largestNDigitNum = int(pow(10, n)) - 1; 
      
    remainder = largestNDigitNum % lcm; 
      
    # If largest number is the answer 
    if (remainder == 0): 
        return largestNDigitNum ; 
      
    # find closest smaller number 
    # divisible by LCM 
    largestNDigitNum -= remainder; 
      
    # if result is an n-digit number 
    if (largestNDigitNum >= int(pow(10, n - 1))): 
        return largestNDigitNum; 
    else: 
        return 0; 
  
# Driver code 
n = 2; x = 3;  
y = 4; z = 6; 
res = int(findDivisible(n, x, y, z)); 
  
# if the number is found 
if (res != 0): 
    print(res); 
else: 
    print("Not possible"); 