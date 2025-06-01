# N_orig: original array size
# N_tree: smallest power of 2 >= N_orig
# tree array size is 2 * N_tree, 1-indexed (tree[1] is the root)
tree = [0] * (2 * MAX_N_TREE)  # Replace MAX_N_TREE with your value
N_tree = ...  # Set this to the smallest power of 2 >= N_orig

def iterative_update(p, value):
    # Move to the leaf position in the tree
    p += N_tree
    # Set the value at the leaf
    tree[p] = value
    # Move up to the root, updating parents
    while p > 1:
        p //= 2  # Go to parent node
        # Update parent by merging its two children
        tree[p] = tree[2 * p] + tree[2 * p + 1]

def iterative_query(l, r):
    # Initialize result with the identity for sum
    res = 0
    # Move l and r to the leaf positions
    l += N_tree
    r += N_tree
    # Loop until the two pointers meet
    while l < r:
        # If l is a right child, include its value and move to next
        if l % 2 == 1:
            res += tree[l]
            l += 1
        # If r is a right child, move left and include its value
        if r % 2 == 1:
            r -= 1
            res += tree[r]
        # Move both pointers up to their parents
        l //= 2
        r //= 2
    # Return the final result
    return res