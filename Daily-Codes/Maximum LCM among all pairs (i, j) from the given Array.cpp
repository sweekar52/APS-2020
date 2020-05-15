// C++ implementation to find the maximum 
// LCM of pairs in an array 

#include <bits/stdc++.h> 
using namespace std; 

// Function comparing all LCM pairs 
int maxLcmOfPairs(int arr[], int n) 
{ 
	// To store the highest LCM 
	int maxLCM = -1; 

	// To generate all pairs from array 
	for (int i = 0; i < n; i++) { 
		for (int j = i + 1; j < n; j++) { 

			// Find LCM of the pair 
			// Update the maxLCM if this is 
			// greater than its existing value 
			maxLCM = max(maxLCM, 
						(arr[i] * arr[j]) 
							/ __gcd(arr[i], arr[j])); 
		} 
	} 

	// Return the highest value of LCM 
	return maxLCM; 
} 

// Driver code 
int main() 
{ 
	int arr[] = { 17, 3, 8, 6 }; 
	int n = sizeof(arr) / sizeof(arr[0]); 

	cout << maxLcmOfPairs(arr, n); 

	return 0; 
} 
