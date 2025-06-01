# Prefix sum array
prefix = []

def build(arr):
    global prefix
    prefix = [0] * len(arr)
    prefix[0] = arr[0]
    for i in range(1, len(arr)):
        prefix[i] = prefix[i-1] + arr[i]

def query(l, r):
    return prefix[r] - (prefix[l-1] if l > 0 else 0)

# Usage example
arr = [1, 2, 3, 4, 5]
build(arr)
print(query(1, 3))  # Output: 9 (2+3+4)