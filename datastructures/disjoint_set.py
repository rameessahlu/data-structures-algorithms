graph = [(1,2), (3,4), (5,6), (7,8), (2,4,), (2,5), (1,3), (6,8), (5,9)]
set_members = 8

def calculate_union():
    pass

# find parent
def find_set_for_child(disjoint_set, p, c, parents_top_parent):
    if disjoint_set[c-1] == -1:
        disjoint_set[c-1] = p
    else:
        if disjoint_set[c-1] > 0:
            return find_set_for_child(disjoint_set, p, disjoint_set[c-1], parents_top_parent)
        else:
            if disjoint_set[parents_top_parent] < disjoint_set[c-1]:
                disjoint_set[c-1] = parents_top_parent+1
    return c-1

def find_set_for_parent(disjoint_set, p, partOfTheSet):
    if disjoint_set[p-1] < 0 or p-1 == 0: #itself is a parent
        if partOfTheSet:
            disjoint_set[p-1] -= 1
        else:
            disjoint_set[p-1] -= 2
        return p-1
    else:
        return find_set_for_parent(disjoint_set, disjoint_set[p-1], False)

#array representation
def find_cycle(graph):
    disjoint_set = [-1] * set_members
    #represent array in graph
    c = -1
    for g in graph:
        parents_top_parent = find_set_for_parent(disjoint_set, g[0], True)
        #if c ==3:
        #    print(parents_top_parent)
        childs_top_parent = find_set_for_child(disjoint_set, g[0], g[1], parents_top_parent)
        if childs_top_parent == parents_top_parent:
            print('Found cycle @ {}!'.format(g))
            return
    print(disjoint_set)
    
find_cycle(graph)