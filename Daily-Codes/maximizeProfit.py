# Python3 implementation of the approach 

# Function to return the maximized profit 
def maxProfit(seats, k, n) : 

	# Push all the vacant seats 
	# in a priority queue 
	pq = []; 
	for i in range(k) : 
		pq.append(seats[i]); 
	
	# for maintaining the property of max heap 
	pq.sort(reverse = True); 
	
	# To store the maximized profit 
	profit = 0; 

	# To count the people that 
	# have been sold a ticket 
	c = 0; 
	while (c < n) : 
		
		# for maintaining the property of max heap 
		pq.sort(reverse = True); 
		
		# Get the maximimum number of 
		# vacant seats for any row 
		top = pq[0]; 
		
		# Remove it from the queue 
		pq.pop(0); 
		
		# If there are no vacant seats 
		if (top == 0) : 
			break; 
			
		# Update the profit 
		profit = profit + top; 
		
		# Push the updated status of the 
		# vacant seats in the current row 
		pq.append(top - 1); 
		
		# Update the count of persons 
		c += 1; 
	
	return profit; 

# Driver code 
if __name__ == "__main__" : 

	seats = [ 2, 3, 4, 5, 1 ]; 
	k = len(seats); 
	n = 6; 

	print(maxProfit(seats, k, n)); 

# This code is contributed by AnkitRai01 
