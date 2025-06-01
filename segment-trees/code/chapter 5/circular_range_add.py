def circular_range_add(L, R, val):
    # Adds 'val' to all elements in the circular range [L, R]
    # If L <= R, the range does not wrap around the end of the array
    if L <= R:
        range_add(L, R, val)
    else:
        # If L > R, the range wraps around the end of the array
        # So, add 'val' to [L, N-1] and [0, R]
        range_add(L, N - 1, val)
        range_add(0, R, val)

def circular_range_query(L, R):
    # Returns the sum (or result) over the circular range [L, R]
    # If L <= R, the range does not wrap around the end of the array
    if L <= R:
        return range_query(L, R)
    else:
        # If L > R, the range wraps around the end of the array
        # So, query [L, N-1] and [0, R] and sum the results
        return range_query(L, N - 1) + range_query(0, R)