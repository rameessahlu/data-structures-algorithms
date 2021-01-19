# v represent starting vertex
def DFS(graph, dfs_result, visited, v):
	if visited[v] == 0:
		dfs_result.append(v)
		visited[v] = 1
		#visiting new vertices
		for idx, r in enumerate(graph[v]):
			if r == 1 and visited[idx] == 0: 
				return DFS(graph, dfs_result, visited, idx)
	return dfs_result

if __name__ == '__main__':
	#adjency matrix implementaion of graph
	graph = [[0,1,1,1,0,0,0],
			 [1,0,1,0,0,0,0],
			 [1,1,0,1,1,0,0],
			 [1,0,1,0,1,0,0],
			 [0,0,1,1,0,1,1],
			 [0,0,0,0,1,0,0],
			 [0,0,0,0,1,0,0]
			]
	dfs_result = []
	visited = [0]*len(graph)
	print(DFS(graph, dfs_result, visited, 0))