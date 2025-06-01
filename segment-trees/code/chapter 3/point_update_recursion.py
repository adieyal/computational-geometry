# Update the value at index upd_idx in the array to new_val
def update(node_idx, seg_L, seg_R, upd_idx, new_val):
    # If this node is a leaf (covers a single element)
    if seg_L == seg_R:
        # Update the value at the leaf node
        tree[node_idx] = new_val
        return

    # Calculate the midpoint of the current segment
    mid = seg_L + (seg_R - seg_L) // 2

    # If the update index is in the left child
    if upd_idx <= mid:
        update(2 * node_idx + 1, seg_L, mid, upd_idx, new_val)
    # If the update index is in the right child
    else:
        update(2 * node_idx + 2, mid + 1, seg_R, upd_idx, new_val)

    # After updating the child, update the current node's value
    tree[node_idx] = tree[2 * node_idx + 1] + tree[2 * node_idx + 2]

# Example initial call:
# update(0, 0, N - 1, p, b)
