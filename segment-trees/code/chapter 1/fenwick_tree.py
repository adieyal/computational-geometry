# Fenwick Tree (Binary Indexed Tree) implementation

fenwick = []

def build(arr):
    global fenwick
    n = len(arr)
    fenwick = [0] * (n + 1)
    for i in range(n):
        update(i, arr[i])

def update(index, delta):
    # Adds delta to element at index
    global fenwick
    i = index + 1
    while i < len(fenwick):
        fenwick[i] += delta
        i += i & -i

def query(r):
    # Returns prefix sum from 0 to r (inclusive)
    global fenwick
    res = 0
    i = r + 1
    while i > 0:
        res += fenwick[i]
        i -= i & -i
    return res

def range_query(l, r):
    # Returns sum from l to r (inclusive)
    return query(r) - (query(l - 1) if l > 0 else 0)

# Usage example
arr = [1, 2, 3, 4, 5]
build(arr)
print(range_query(1, 3))  # Output: 9 (2+3+4)
update(2, 2)  # arr[2] += 2, arr becomes [1,2,5,4,5]
print(range_query(1, 3))  # Output: 11 (2+5+4)
