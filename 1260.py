count_vertex, count_edge, start_at = map(int, input().split())
tree = []
visit = {}

# construct tree
for i in range(0, count_vertex):
    tree.append([])

for i in range(0, count_edge):
    f, t = map(int, input().split())
    f_idx = f - 1
    t_idx = t - 1
    
    # append child
    tree[f_idx].append(t_idx)
    tree[t_idx].append(f_idx)

visit_dfs = []

#print("Tree: {}".format(",".join(map(str, tree))))

# dfs
def dfs(c):
    #print("V: {}".format(c))
    visit[c] = True
    if not c + 1 in visit_dfs: # no duplicate
        visit_dfs.append(c + 1)

    #print("App3")
    for child in sorted(tree[c]):
        if not child in visit:
            dfs(child)

def bfs(c):
    bfs_result = []
    bfs_queue = []
    bfs_result.append(c + 1)
    bfs_queue.append(c)
    while len(bfs_queue) > 0: # repeat until len 0
        parent = bfs_queue.pop(0)
        for child in sorted(tree[parent]):
            #print("Tree Element for {}: {}".format(parent + 1, child + 1))
            if not child + 1 in bfs_result:
                bfs_result.append(child + 1)
                bfs_queue.append(child)
        #print("==============")
    return bfs_result

dfs(start_at - 1)

# bfs
bfs_result = bfs(start_at - 1)

print(" ".join(map(str, visit_dfs)))
print(" ".join(map(str, bfs_result)))