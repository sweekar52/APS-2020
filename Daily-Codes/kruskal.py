arr = []
weights = []
edgeList = []


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
    global arr, weights, edgeList
    nNodes, nEdges = map(int, input().split())
    arr = [i for i in range(nNodes)]
    weights = [1 for _ in range(nNodes)]

    for _ in range(nEdges):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        edgeList.append((u, v, w))

    edgeList.sort(key=lambda x: x[2])
    # print(edgeList)

    weightSum = 0
    for edge in edgeList:
        if not find(edge[0], edge[1]):
            union(edge[0], edge[1])
            weightSum += edge[2]

    print(weightSum)


if __name__ == "__main__":
    main()