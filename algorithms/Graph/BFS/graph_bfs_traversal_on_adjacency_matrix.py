class simple_queue:
	#a simple implementaion of queue using list
	def __init__(self):
		self.queue = []
	
	def enqueue(self, val):
		self.queue.append(val)
	
	def dequeue(self):
		return self.queue.pop(0)
	
	def is_empty(self):
		if len(self.queue) == 0:
			return True
		else:
			return False

# v represent starting vertex
def BFS(graph, v):
	bfs_result = []
	visited = [0]*len(graph)
	queue = simple_queue()
	
	bfs_result.append(v)
	queue.enqueue(v)
	visited[v] = 1
	#exploring all the vertices
	while not queue.is_empty():
		u = queue.dequeue()
		#visiting new vertices
		for idx, r in enumerate(graph[u]):
			if r == 1 and visited[idx] == 0: 
				queue.enqueue(idx)
				visited[idx] = 1
				bfs_result.append(idx)
	return bfs_result

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
	print(BFS(graph, 0))