#include "bits/stdc++.h" 
using namespace std; 

constexpr static int MAXSIZE = 1000; 
constexpr static int INF 
	= numeric_limits<int>::max(); 

// Segment Tree array 
int64_t tree[MAXSIZE]; 

// Lazy Update array 
int64_t lazy[MAXSIZE]; 

// This tuple will hold tree state 
// the stacks 
using QueryAdaptor 
	= tuple<int64_t, 
			int64_t, 
			int64_t>; 

// Build our segment tree 
void build_tree(int64_t* arr, 
				int64_t arr_size) 
{ 
	// Stack will use to update 
	// the tree value 
	stack<QueryAdaptor> st; 

	// Emplace the root of the tree 
	st.emplace(1, 0, arr_size - 1); 

	// Repeat until empty 
	while (!st.empty()) { 

		// Take the indexes at the 
		// top of the stack 
		int64_t currnode, curra, currb; 

		// value at the top of the 
		// stack 
		tie(currnode, curra, currb) = st.top(); 

		// Pop the value from the 
		// stack 
		st.pop(); 

		// Flag with INF ranges are merged 
		if (curra == INF && currb == INF) { 
			tree[currnode] = tree[currnode * 2] 
							+ tree[currnode * 2 + 1]; 
		} 

		// Leaf node 
		else if (curra == currb) { 
			tree[currnode] = arr[curra]; 
		} 

		else { 

			// Insert flag node inverse 
			// order of evaluation 
			st.emplace(currnode, INF, INF); 

			int64_t mid = (curra + currb) / 2; 

			// Push children 
			st.emplace(currnode * 2, 
					curra, mid); 
			st.emplace(currnode * 2 + 1, 
					mid + 1, currb); 
		} 
	} 
} 

// A utility function that propagates 
// updates lazily down the tree 
inline void push_down(int64_t node, 
					int64_t a, 
					int64_t b) 
{ 
	if (lazy[node] != 0) { 
		tree[node] += lazy[node] * (b - a + 1); 

		if (a != b) { 
			lazy[2 * node] += lazy[node]; 
			lazy[2 * node + 1] += lazy[node]; 
		} 

		lazy[node] = 0; 
	} 
} 

// Iterative Range_Update function to 
// add val to all elements in the 
// range i-j (inclusive) 
void update_tree(int64_t arr_size, 
				int64_t i, 
				int64_t j, 
				int64_t val) 
{ 

	// Intialize the stack 
	stack<QueryAdaptor> st; 

	// Emplace the root of the tree 
	st.emplace(1, 0, arr_size - 1); 

	// Work until empty 
	while (!st.empty()) { 

		// Take the indexes at the 
		// top of the stack 
		int64_t currnode, curra, currb; 
		tie(currnode, curra, currb) = st.top(); 
		st.pop(); 

		// Flag with INF ranges are merged 
		if (curra == INF && currb == INF) { 
			tree[currnode] = tree[currnode * 2] 
							+ tree[currnode * 2 + 1]; 
		} 

		// Traverse the previous updates 
		// down the tree 
		else { 
			push_down(currnode, curra, currb); 

			// No overlap condition 
			if (curra > currb || curra > j 
				|| currb < i) { 
				continue; 
			} 

			// Total overlap condition 
			else if (curra >= i && currb <= j) { 
				// Update lazy array 
				tree[currnode] += val * (currb - curra + 1); 

				if (curra != currb) { 
					lazy[currnode * 2] += val; 
					lazy[currnode * 2 + 1] += val; 
				} 
			} 

			// Partial Overlap 
			else { 
				// Insert flag node inverse 
				// order of evaluation 
				st.emplace(currnode, INF, INF); 

				int64_t mid = (curra + currb) / 2; 

				// Push children 
				st.emplace(currnode * 2, 
						curra, mid); 
				st.emplace(currnode * 2 + 1, 
						mid + 1, currb); 
			} 
		} 
	} 
} 

// A function that find the sum of 
// all elements in the range i-j 
int64_t query(int64_t arr_size, 
			int64_t i, 
			int64_t j) 
{ 
	// Intialize stack 
	stack<QueryAdaptor> st; 

	// Emplace root of the tree 
	st.emplace(1, 0, arr_size - 1); 

	int64_t result = 0; 

	while (!st.empty()) { 

		// Take the indexes at the 
		// top of the stack 
		int64_t currnode, curra, currb; 
		tie(currnode, curra, currb) = st.top(); 
		st.pop(); 

		// Traverse the previous updates 
		// down the tree 
		push_down(currnode, curra, currb); 

		// No overlap 
		if (curra > currb || curra > j 
			|| currb < i) { 
			continue; 
		} 

		// Total Overlap 
		else if (curra >= i && currb <= j) { 
			result += tree[currnode]; 
		} 

		// Partial Overlap 
		else { 
			std::int64_t mid = (curra + currb) / 2; 

			// Push children 
			st.emplace(currnode * 2, 
					curra, mid); 
			st.emplace(currnode * 2 + 1, 
					mid + 1, currb); 
		} 
	} 

	return result; 
} 

// Driver Code 
int main() 
{ 
	// Initialize our trees with 0 
	memset(tree, 0, sizeof(int64_t) * MAXSIZE); 
	memset(lazy, 0, sizeof(int64_t) * MAXSIZE); 

	int64_t arr[] = { 1, 3, 5, 7, 9, 11 }; 
	int n = sizeof(arr) / sizeof(arr[0]); 

	// Build segment tree from given array 
	build_tree(arr, n); 

	// Print sum of values in array 
	// from index 1 to 3 
	cout << "Sum of values in given range = "
		<< query(n, 1, 3) 
		<< endl; 

	// Add 10 to all nodes at indexes 
	// from 1 to 5 
	update_tree(n, 1, 5, 10); 

	// Find sum after the value is updated 
	cout << "Updated sum of values in given range = "
		<< query(n, 1, 3) 
		<< endl; 

	return 0; 
} 
