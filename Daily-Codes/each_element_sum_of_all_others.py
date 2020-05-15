# Python 3 implementation 
# to find encrypted array 
# from the original array 

# Finds and prints the elements 
# of the encrypted array 
def findEncryptedArray(arr, n) : 
	sum = 0

	# total sum of elements 
	# of original array 
	for i in range(n) : 
		sum += arr[i] 

	# calculating and displaying 
	# elements of encrypted array 
	for i in range(n) : 
		print(sum - arr[i], end = " ") 
		
# Driver Code 
if __name__ == "__main__" : 

	arr = [ 5, 1, 3, 2, 4] 
	N = len(arr) 
	
	# function calling 
	findEncryptedArray(arr, N) 

# This code is contributed by ANKITRAI1 
