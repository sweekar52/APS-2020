# Find the small string at that index in the array of 
# small strings is contained in the big string 

# Helper Function to the Finding bigString 
def isInBigStringHelper(bigString,smallString,startIdx): 
	
	# Initialize leftBigIdx and rightBigIdx and leftSmallIdx variables 
	leftBigIdx = startIdx 
	rightBigIdx = startIdx + len(smallString) - 1
	leftSmallIdx = 0
	rightSmallIdx = len(smallString) - 1

	# Iterate until leftBigIdx variable reaches less 
	# than or equal to rightBigIdx 
	while (leftBigIdx <= rightBigIdx): 
		
		# Check if bigString[leftBigIdx] is not equal 
		# to smallString[leftSmallIdx] or Check if 
		# bigString[rightBigIdx] is not equal to 
		# smallString[rightSmallIdx] than return false 
		# otherwise increment leftBigIdx and leftSmallIdx 
		# decrement rightBigIdx and rightSmallIdx 
		if (bigString[leftBigIdx] != smallString[leftSmallIdx] or
			bigString[rightBigIdx] != smallString[rightSmallIdx]): 
			return False

		leftBigIdx += 1
		rightBigIdx -= 1
		leftSmallIdx += 1
		rightSmallIdx -= 1
	return True

# Function to the bigString 
def isInBigString(bigString, smallString): 
	
	# iterate in the bigString 
	for i in range(len(bigString)): 
		
		# Check if length of smallString + i is greater than 
		# the length of bigString 
		if (i + len(smallString) > len(bigString)): 
			break

		# call the function isInBigStringHelper 
		if (isInBigStringHelper(bigString, smallString, i)): 
			return True
	return False

# Function to the multiStringSearch 
def multiStringSearch(bigString, smallStrings): 
	solution = [] 

	# iterate in the smallString 
	for smallString in smallStrings: 
		# calling the isInBigString Function 
		solution.append(isInBigString(bigString, smallString)) 
	return solution 

# Driver code 
if __name__ == '__main__': 
	# initialize string 
	str1 = "this is a big string"

	# initialize vector string 

	substr = ["this", "yo", "is", "a","bigger", "string", "kappa"] 

	# Function call 
	ans = multiStringSearch(str1, substr) 

	# Print answers 
	for i in range(len(ans)): 
		# Check if ans[i] is equal to 1 
		# then Print true otherwise print false 
		if (ans[i] == 1): 
			print("true",end = " ") 
		else: 
			print("false",end = " ") 

# This code is contributed by Bhupendra_Singh 
