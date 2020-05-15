// C++ program to Find count of 
// Subarrays whose product can be 
// represented as the difference between 
// two different numbers 

#include <bits/stdc++.h> 
using namespace std; 

// Function to print number of subarrays 
void numberOfSubarrays(int arr[], int n) 
{ 

	vector<pair<int, int> > next(n); 
	vector<pair<int, int> > next_to_next(n); 

	int f = -1; 
	int s = -1; 

	for (int i = n - 1; i >= 0; i--) { 
		next[i].first = arr[i]; 

		next_to_next[i].first = arr[i]; 

		// check if number is divisible by 2 
		if (arr[i] % 2 == 0) { 
			s = f; 
			f = i; 
		} 

		// Store the position 
		// of the next element 
		next[i].second = f; 

		// Store the position of 
		// next to next element 
		// which is multiple of 2 
		next_to_next[i].second = s; 
	} 

	int total = 0; 

	for (int i = 0; i < n; i++) { 
		int calculate; 

		// Check if the element is divisible 
		// is divisible by 4 
		if (next[i].first % 4 == 0) { 
			calculate = n - i; 

			total += calculate; 
		} 

		// Check if current element 
		// is an odd number 
		else if (next[i].first & 1 == 1) { 

			if (next[i].second == -1) { 
				calculate = n - i; 

				total += calculate; 
			} 

			else { 

				// check if after the current element 
				// only 1 element exist which is a 
				// multiple of only 2 but not 4 
				if (next_to_next[i].second == -1 
				&& next[next[i].second].first % 4 != 0) 

				{ 
					calculate = next[i].second - i; 
					total += calculate; 
				} 

				// Check if after the current element an element exist 
				// which is multiple of only 2 and not 4 and after that 
				// an element also exist which is multiple of 2 
				else if (next_to_next[i].second != -1 
						&& next[next[i].second].first % 4 != 0) { 
					calculate = n - i; 
					total += calculate; 
					total -= next_to_next[i].second - next[i].second; 
				} 

				// All subarrays can be formed by current element 
				else { 
					calculate = n - i; 
					total = total + calculate; 
				} 
			} 
		} 

		// Condition for an even number 
		else { 

			// Check if next element does not 
			// exist which is multiple of 2 
			if (next_to_next[i].second == -1) 
				total = total; 

			// Check if next element exist 
			// which is multiple of 2 
			else { 
				calculate = n - i; 
				total += calculate; 
				total = total - next_to_next[i].second + i; 
			} 
		} 
	} 

	// Print the output 
	cout << total << "\n"; 
} 

// Driver Code 
int main() 
{ 
	// array initialisation 
	int arr[] = { 2, 5, 6 }; 

	int size = sizeof(arr) / sizeof(arr[0]); 

	numberOfSubarrays(arr, size); 

	return 0; 
} 
