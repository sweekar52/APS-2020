// C++ implementation of the above approach 
#include <bits/stdc++.h> 
using namespace std; 

const int MOD = (int)1e9 + 7; 

// A recursive function that generates all 
// the sequence and find GCD 
int calculate(int pos, int g, int n, int k) 
{ 

	// If we reach the sequence of length N 
	// g is the GCD of the sequence 
	if (pos == n) { 
		return g; 
	} 

	// Intialise answer to 0 
	int answer = 0; 

	// Placing all possible values at this 
	// position and recursively find the 
	// GCD of the sequence 
	for (int i = 1; i <= k; i++) { 

		// Take GCD of GCD calculated uptill 
		// now i.e. g with current element 
		answer = (answer % MOD 
				+ calculate(pos + 1, __gcd(g, i), n, k) % MOD); 

		// Take modulo to avoid overflow 
		answer %= MOD; 
	} 

	// Return the final answer 
	return answer; 
} 

// Function that finds the sum of GCD 
// of all the subsequence of N length 
int sumofGCD(int n, int k) 
{ 

	// Recursive function that generates 
	// the sequence and return the GCD 
	return calculate(0, 0, n, k); 
} 

// Driver Code 
int main() 
{ 
	int N = 3, K = 2; 

	// Function Call 
	cout << sumofGCD(N, K); 
	return 0; 
} 
