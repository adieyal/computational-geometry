MAXNODES = (100000 + 100000) * 20
lchild = [0] * MAXNODES
rchild = [0] * MAXNODES
tree_val = [0] * MAXNODES
node_count = 0

def new_node():
    global node_count
    node_count += 1
    return node_count

def update(prev, l, r, pos, val):
    node = new_node()
    lchild[node] = lchild[prev]
    rchild[node] = rchild[prev]
    
    if l == r:
        tree_val[node] = val
    else:
        mid = (l + r) >> 1
        if pos <= mid:
            lchild[node] = update(lchild[prev], l, mid, pos, val)
        else:
            rchild[node] = update(rchild[prev], mid+1, r, pos, val)
        tree_val[node] = tree_val[lchild[node]] + tree_val[rchild[node]]
    return node