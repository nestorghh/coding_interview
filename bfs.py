# BFS implementation

graph={}
graph['a']=('b','c')
graph['b']=('a','d','e')
graph['c']=('a','d')
graph['d']=('b','c','e')
graph['e']=('b','d')


def bfs(graph,start):
	
	queue = [start]
	visited ={start:True}

	while queue:
		v = queue.pop(0)
		for n in graph[v]:
			if n not in visited:
				queue.append(n)
				visited[n]=True
	return visited

	
def bfs_distance(graph,start):
	queue = [start]
	level = {start:0}
	parent = {start:None}
	
	i=1

	while queue:
		v=queue.pop(0)
		for n in graph[v]:
			if n not in level:
				queue.append(n)
				level[n] = i
				parent[n] = v
		i+=1

	return level, parent
	



