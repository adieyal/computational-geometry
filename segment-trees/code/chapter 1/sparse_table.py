# Sparse Table for Range Minimum Query (RMQ)
import math

st = []
log = []

def build(arr):
    global st, log
    n = len(arr)
    k = int(math.log2(n)) + 1
    st = [[0] * k for _ in range(n)]
    log = [0] * (n + 1)
    for i in range(2, n + 1):
        log[i] = log[i // 2] + 1
    for i in range(n):
        st[i][0] = arr[i]
    for j in range(1, k):
        for i in range(n - (1 << j) + 1):
            st[i][j] = min(st[i][j-1], st[i + (1 << (j-1))][j-1])

def query(l, r):
    # Returns min in arr[l..r] (inclusive)
    global st, log
    j = log[r - l + 1]
    return min(st[l][j], st[r - (1 << j) + 1][j])

# Usage example
arr = [1, 3, 2, 7, 9, 11, 3, 5, 6]
build(arr)
print(query(2, 5))  # Output: 2 (min of [2,7,9,11])
print(query(3, 8))  # Output: 3 (min of [7,9,11,3,5,6])
