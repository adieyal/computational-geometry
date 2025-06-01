class FlipLazyTree:
    def __init__(self, size):
        # Segment tree arrays are sized to 4 * size to safely cover all nodes
        # count1[node] stores the number of 1s in the segment represented by 'node'
        self.count1 = [0] * (4 * size)
        # lazy_flip[node] is True if the segment needs to be flipped (lazy propagation marker)
        self.lazy_flip = [False] * (4 * size)

    def apply_flip(self, node, length):
        # Flips the count of 1s in the segment: number of 1s becomes number of 0s and vice versa
        self.count1[node] = length - self.count1[node]
        # Toggle the lazy flip marker for this node
        self.lazy_flip[node] = not self.lazy_flip[node]

    def push(self, node, l, r):
        # Propagates the flip operation to the children if there is a pending flip
        if self.lazy_flip[node]:
            mid = (l + r) // 2
            # Apply flip to the left child (node*2) for its segment length (mid - l + 1)
            self.apply_flip(node * 2, mid - l + 1)
            # Apply flip to the right child (node*2 + 1) for its segment length (r - mid)
            self.apply_flip(node * 2 + 1, r - mid)
            # Clear the lazy flip marker for the current node after pushing down
            self.lazy_flip[node] = False