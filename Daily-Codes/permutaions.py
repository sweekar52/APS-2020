# Python3 program to print first n unique 
# permutations of the string using itertools 
from itertools import permutations 

# Function to print first n unique 
# permutation using itertools 
def nPermute(string, n): 

	# Convert the string to list and sort 
	# the characters in alphabetical order 
	strList = sorted(list(string)) 
	
	# Create an iterator 
	permList = permutations(strList) 

	# Keep iterating until we 
	# reach nth unique permutation 
	i = 0
	permSet = set() 
	tempStr = '' 
	
	while i < n: 
		tempStr = ''.join(permList.__next__()) 
		
		# Insert the string in the set 
		# if it is not already included 
		# and print it out. 
		if tempStr not in permSet: 
			permSet.add(tempStr) 
			print(tempStr) 
			i += 1
	
# Driver code 
if __name__ == "__main__": 

	string = "ababc"
	n = 10
	nPermute(string, n) 
