def build_iterative(A):
    N = len(A)
    tree_size = 1
    while tree_size < N:
        tree_size *= 2

    # Initialize the tree with zeros (identity for sum)
    tree = [0] * (2 * tree_size)

    # Copy input to leaves
    for i in range(N):
        tree[tree_size + i] = A[i]

    # Fill remaining leaves with identity (already zero)
    # for i in range(N, tree_size):
    #     tree[tree_size + i] = 0  # Not needed, already zero

    # Build internal nodes bottom-up
    for i in range(tree_size - 1, 0, -1):
        tree[i] = tree[2 * i] + tree[2 * i + 1]

    return tree

# Example usage
A = [1, 2, 3, 4]
tree = build_iterative(A)
print(tree)
