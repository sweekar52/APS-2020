def dfs(graph, source, visited):
  if(visited[source] == True):
    return
  
  visited[source] = True
  print(source)

  for v in range(len(graph[source])):
    if(not visited[v] and graph[source][v]):
      dfs(graph, v, visited)

def main():
  graph = [[0, 1, 1, 0, 1], [1, 0, 1, 0, 0], [1, 1, 0, 1, 0], [0, 0, 1, 0, 1], [1, 0, 0, 1, 0]]
  visited = [False for i in range(5)]
  dfs(graph,0,visited)

if __name__ == "__main__":
    main()