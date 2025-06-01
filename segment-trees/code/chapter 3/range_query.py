# Query the sum in the range [l, r] in the segment tree
def query(node, start, end, l, r):
    # No overlap
    if r < start or end < l:
        return 0  # Identity for sum

    # Complete overlap
    if l <= start and end <= r:
        return tree[node]

    # Partial overlap
    mid = start + (end - start) // 2
    left_child = 2 * node + 1
    right_child = 2 * node + 2

    left_sum = query(left_child, start, mid, l, r)
    right_sum = query(right_child, mid + 1, end, l, r)

    return left_sum + right_sum

# Example usage:
result = query(0, 0, N - 1, query_left, query_right)
