arr = []
weights = []


def root(u):
    global arr, weights
    root = u
    while arr[root] != root:
        root = arr[root]
    return root


def union(u, v):
    global arr, weights
    rootU = root(u)
    rootV = root(v)

    if weights[rootV] > weights[rootU]:
        arr[rootU] = arr[rootV]
        weights[rootV] += weights[rootU]

    else:
        arr[rootV] = arr[rootU]
        weights[rootU] += weights[rootU]

def find(u, v):
    return root(u) == root(v)


def main():
    global arr, weights
    arr = [i for i in range(10)]
    weights = [1 for _ in range(10)]
    union(0, 1)
    print(arr)
    print(weights)

if __name__ == "__main__":
    main()