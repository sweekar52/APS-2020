# Python3 implementation of the above approach 

# Function to find power of 
# a number. 
def power(a, b) : 

	result = 1; 
	while (b > 0) : 
		if (b % 2 == 1) : 
			result = result * a; 
		a = a * a; 
		b = b // 2; 
	
	return result; 

# Function to find 
# factorial of a number. 
def factorial(n) : 

	fact = 1; 
	for i in range(1, n + 1) : 
		fact = fact * i; 
	
	return fact; 

# Function to print no of arrays 
def findNoOfArrays(a, n) : 

	# c variable counts the no of pairs 
	sum = 0; c = 0; 

	# Map to store the frequency 
	# of each element 
	mp = dict.fromkeys(a, 0); 

	for i in range(2 * n) : 
		mp[a[i]] += 1; 

		# Sum of all elements of the array 
		sum = sum + a[i]; 

	# Variable to check if it is 
	# possible to make any array 
	isArrayPossible = True; 
	ans = factorial(n - 1); 

	# First element of suffix array 
	# and the last element of prefix array 
	s1 = sum // (n + 1); 

	# Check if the element exists in the map 
	if (mp[s1] >= 2) : 
		mp[s1] = mp[s1] - 2; 
		
	else : 
		isArrayPossible = False; 
	
	if (isArrayPossible) : 
		for first,second in mp.items() : 
			
			# If elements of any pair are equal 
			# and their frequency is not divisible by 2 
			# update the isArrayPossible variable 
			# to false and break through the loop 
			if (first == s1 - first) : 
				if (mp[first] % 2 != 0) : 
					isArrayPossible = False; 
					break; 

			# If elements of any pair are not equal 
			# and their frequency is not same 
			# update the isArrayPossible variable 
			# to false and break through the loop 
			if (first != s1 - first) : 
				if s1 - first in mp : 
					if (mp[first] != mp[s1 - first]) : 
						isArrayPossible = False; 
						break; 
			
			# Check if frequency is greater than zero 
			if (second > 0) : 
				if (first != s1 - first) : 

					# update the count of pairs 
					c = c + second; 

					# Multiply the answer by 
					# 2^(frequency of pairs) since 
					# the elements of the pair are 
					# not the same in this condition 
					ans = ans * power(2, second); 

					# Divide the answer by the factorial 
					# of no of similar pairs 
					ans = ans / factorial(second); 

					# Make frequency of both these elements 0 
					mp[first] = 0; 
					mp[s1 - first] = 0; 
				
				if (first == s1 - first) : 

					# Update the count of pairs 
					c = c + second // 2; 

					# Divide the answer by the factorial 
					# of no. of similar pairs 
					ans = ans // factorial(second // 2); 

					# Make frequency of this element 0 
					mp[first] = 0; 

	# Check if it is possible to make the 
	# array and there are n-1 pairs 
	# whose sum will be equal to s1 
	if (c < n - 1 or isArrayPossible == False) : 
		print("0"); 
	else: 
		print(ans); 

# Driver code 
if __name__ == "__main__" : 

	arr1 = [ 5, 2, 3, 5 ]; 
	n1 = len(arr1); 

	# Function calling 
	findNoOfArrays(arr1, n1 // 2); 

	arr2 = [ -1, -1, -1, 0, 1, 0, 
				1, 0, 1, 0, 0, 0 ]; 
	n2 = len(arr2); 
	findNoOfArrays(arr2, n2 // 2); 
	
# This code is contributed by AnkitRai01 
