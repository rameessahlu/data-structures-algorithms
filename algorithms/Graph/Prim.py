MAX = 999
MIN = -999

#Using Prim's algorithm for finding minimum spanning tree problem
def findSpanningTree(graph):
    near=[MAX]*len(graph)
    result = []
    visited = []
    
    iteration = 0
    cond = True
    while(cond):
        smallest = 0
        if iteration == 0:
            #finds the smallest edge with the lowest weight to the zeroth vertex
            for c in range(0, len(graph[0])):
                if graph[0][c] < graph[0][smallest]:
                    smallest = c
            result.append([1,smallest+1])
            #marking selected vertices for result with MIN in near[]
            near[0] = MIN
            near[smallest] = MIN
            visited.append(0)
            visited.append(smallest)
        else:
            #finds the nearest vertex with the lowest weighted edge to each visited vertices and mark it in the near[]
            for n in range(0, len(near)):
                if near[n] == MIN:
                    continue
                else:
                    smallest = 0
                    for v in visited:
                        if graph[n][v] < graph[n][smallest]:
                            smallest = v
                        near[n] = smallest
            #finds the smallest edge from the all the shortest edges found and marked in near[]
            last_smallest = None
            for n in range(0,len(near)):
                if near[n] == MIN:
                    continue
                if last_smallest == None:
                    last_smallest = (n, near[n])
                if graph[n][near[n]] < graph[last_smallest[0]][last_smallest[1]]:
                    last_smallest = (n,near[n])
            result.append([last_smallest[0]+1,near[last_smallest[0]]+1])
            visited.append(last_smallest[0])
            visited.append(near[last_smallest[0]])
            if(near[last_smallest[0]] < len(near)):
                near[last_smallest[0]] = MIN
            if(near[last_smallest[0]] < len(near) and near[last_smallest[0]]>=0):
                near[near[last_smallest[0]]] = MIN
        iteration+=1
        #stops when no. of edges equals (vertices-1)/iteration
        if iteration == len(graph)-1:
            cond = False
    return result
            
if __name__ == '__main__':
    #adjency matrix representation of weighted graph
    graph = [
                [MAX,25,MAX,MAX,MAX,5,MAX], #1
                [25,MAX,12,MAX,MAX,MAX,10], #2
                [MAX,12,MAX,8,MAX,MAX,MAX], #3
                [MAX,MAX,8,MAX,16,MAX,14],  #4
                [MAX,MAX,MAX,16,MAX,20,18], #5
                [5,MAX,MAX,MAX,20,MAX,MAX], #6
                [MAX,10,MAX,14,18,MAX,MAX]  #7
            ]
    print(findSpanningTree(graph))