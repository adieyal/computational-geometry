# Query the sum in the range [q_L, q_R] in the segment tree
def query(node_idx, seg_L, seg_R, q_L, q_R):
    # Case 1: No overlap between current segment and query range
    if seg_R < q_L or seg_L > q_R:
        return 0  # Identity for sum

    # Case 2: Total overlap (current segment is completely inside query range)
    if q_L <= seg_L and seg_R <= q_R:
        return tree[node_idx]

    # Case 3: Partial overlap (need to check both children)
    mid = seg_L + (seg_R - seg_L) // 2  # Find the midpoint of the segment

    # Query the left child
    left_sum = query(2 * node_idx + 1, seg_L, mid, q_L, q_R)

    # Query the right child
    right_sum = query(2 * node_idx + 2, mid + 1, seg_R, q_L, q_R)

    # Combine the results from both children
    return left_sum + right_sum

# Example initial call:
# result = query(0, 0, N - 1, queryL, queryR)
