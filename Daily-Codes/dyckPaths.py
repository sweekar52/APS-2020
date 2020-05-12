
def generatePaths(n):
    global paths
    if n in paths:
        return paths[n]
    
    paths[n] = []

    for i in range(1, n+1):
        middle = generatePaths(i-1)
        ending = generatePaths(n-i)
        for m in middle:
            for e in ending:
                paths[n].append('X'+m+'Y'+e)

    return paths[n]

ip = int(input())

paths = {}
paths[0] = ['']
paths[1] = ['XY']

print(generatePaths(ip))