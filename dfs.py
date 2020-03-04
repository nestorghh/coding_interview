#def dfs(graph, start):
#	parents={start:None}
#	return dfs_visit(graph,start,parents)

#def dfs_visit(graph, start, parents):
#	for n in graph[start]:
#		if n not in parents:
#			parents[n]=start
#			dfs_visit(graph,n, parents)



# dfs for graphs represented as an adjacency list.

graph={} 
graph['a']=('b','c') 
graph['b']=('a','d','e') 
graph['c']=('a','d') 
graph['d']=('b','c','e')
graph['e']=('b','d') 

def dfs(graph, start):
	visited={}
	stack=[]
	stack.append(start)
	

	while stack:
		s=stack[-1]
		stack.pop()

		if s not in visited:
			visited[s]=True

		for n in graph[s]:
			if n not in visited:
				stack.append(n)
	return visited

# 




