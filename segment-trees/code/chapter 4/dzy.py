class Node:
    def __init__(self, left=None, right=None):
        # The sum of the segment this node represents
        self.sum = 0
        # The range [l, r) this node covers (optional, for clarity)
        self.left = left
        self.right = right
        # Lazy propagation: store the first two Fibonacci numbers to be added
        # to this segment (for range updates)
        self.lazy_fib1 = 0  # F_1 to be added at leftmost position
        self.lazy_fib2 = 0  # F_2 to be added at leftmost+1 position

def merge(L: Node, R: Node) -> Node:
    # Create a new node representing the merged segment
    res = Node()
    # The sum is just the sum of the left and right children
    res.sum = (L.sum + R.sum) % (10**9 + 9)
    # No need to merge lazy values here; they are handled during propagation
    return res
