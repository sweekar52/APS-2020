visited = []
count = []
edgeList = []

def bfs(s):
    global visited, count, edgeList
    q = []
    q.append(s)
    visited[s] = True
    count[s] = 0
    while len(q) != 0:
        ele = q.pop(0)
        for node in edgeList[ele]:
            if(not(visited[node])):
                q.append(node)
                count[node] = count[ele] + 1
                visited[node] = True

def main():
    global visited, count, edgeList
    q = int(input())
    while q:
        q -= 1
        n, m = map(int, input().split())
        edgeList = [[]for _ in range(n)]
        visited = [ False for _ in range(n) ]
        count = [ -1 for _ in range(n) ]
        for _ in range(m):
            u, v = map(int, input().split())
            u -= 1
            v -= 1
            edgeList[u].append(v)
            edgeList[v].append(u)

        s = int(input())
        s -= 1
        bfs(s)
        for num in count:
            if(num!=0 and num!=-1):
                print(num*6, end=' ')
            elif(num==-1):
                print(num, end=' ')
        print()

if __name__ == "__main__":
    main()