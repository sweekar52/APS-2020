# Python3 program to find 
# Sum of GCD over all subarrays. 

# Utility function to calculate 
# sum of gcd of all sub-arrays. 
def findGCDSum(n, a): 
	GCDSum = 0; 
	tempGCD = 0; 
	for i in range(n): 
		
		# Fixing the starting index of a subarray 
		for j in range(i, n): 
			
			# Fixing the ending index of a subarray 
			tempGCD = 0; 
			for k in range(i, j + 1): 
				
				# Finding the GCD of this subarray 
				tempGCD = __gcd(tempGCD, a[k]); 
				
			# Adding this GCD in our sum 
			GCDSum += tempGCD; 

	return GCDSum; 

def __gcd(a, b): 
	return a if(b == 0 ) else __gcd(b, a % b);	 

# Driver Code 
if __name__ == '__main__': 
	n = 5; 
	a = [1, 2, 3, 4, 5]; 
	totalSum = findGCDSum(n, a); 
	print(totalSum); 

# This code is contributed by PrinciRaj1992 
