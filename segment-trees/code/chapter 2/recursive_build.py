# Input array
A = [0] * MAXN
# Segment tree
tree = [0] * (4 * MAXN)

def build(node, start, end):
    if start == end:
        # Leaf node
        tree[node] = A[start]
    else:
        mid = start + (end - start) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2

        build(left_child, start, mid)
        build(right_child, mid + 1, end)

        # Merge children
        tree[node] = tree[left_child] + tree[right_child]

# Example Usage
build(0, 0, N-1)