# Print debug information for a query on the segment tree
def debug_query(node, start, end, l, r, depth=0):
    indent = ' ' * (depth * 2)
    print(f"{indent}Node {node} [{start},{end}] ", end='')
    if r < start or end < l:
        print("NO OVERLAP")
    elif l <= start and end <= r:
        print(f"COMPLETE: {tree[node]}")
    else:
        print("PARTIAL")
        mid = start + (end - start) // 2
        debug_query(2 * node + 1, start, mid, l, r, depth + 1)
        debug_query(2 * node + 2, mid + 1, end, l, r, depth + 1)

# Example usage:
debug_query(0, 0, N - 1, l, r)