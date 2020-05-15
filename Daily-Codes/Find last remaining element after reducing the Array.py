# Python3 program to find the value of the 
# reduced Array by reducing the array 
# based on the given conditions 

# Function to find the value of the 
# reduced Array by reducing the array 
# based on the given conditions 
def find_value(a, n, k): 

	# Variable to store the sum 
	sum = 0

	# For loop to iterate through the 
	# given array and find the sum 
	for i in range(n): 
		sum += a[i] 

	# Return the required value 
	return sum % k 

# Driver code 
if __name__ == "__main__": 
	n, k = 5, 3; 
	a = [12, 4, 13, 0, 5]; 
	print(find_value(a, n, k)) 
