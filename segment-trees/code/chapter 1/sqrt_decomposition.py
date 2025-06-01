import math

def build_sqrt_decomposition(arr):
    n = len(arr)
    block_size = int(math.sqrt(n))
    num_blocks = (n + block_size - 1) // block_size
    block = [0] * num_blocks
    for i in range(n):
        block[i // block_size] += arr[i]
    # Return all necessary data as a tuple
    return arr, block, block_size

def query_sqrt_decomposition(arr, block, block_size, l, r):
    n = len(arr)
    sum_ = 0
    while l <= r:
        if l % block_size == 0 and l + block_size - 1 <= r:
            sum_ += block[l // block_size]
            l += block_size
        else:
            sum_ += arr[l]
            l += 1
    return sum_

# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr_data = build_sqrt_decomposition(arr)
print(query_sqrt_decomposition(*arr_data, 2, 6))  # Output: 25