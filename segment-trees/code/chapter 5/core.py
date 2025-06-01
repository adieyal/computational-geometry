class SegmentTree:
    def __init__(self, size):
        self.n = size
        self.tree = [0] * (4 * size)
        self.lazy = [0] * (4 * size)

    def apply(self, node, l, r, add):
        self.tree[node] += add * (r - l + 1)
        self.lazy[node] += add

    def push(self, node, l, r):
        if self.lazy[node] != 0:
            mid = (l + r) // 2
            self.apply(node * 2, l, mid, self.lazy[node])
            self.apply(node * 2 + 1, mid + 1, r, self.lazy[node])
            self.lazy[node] = 0

    def update(self, node, l, r, ql, qr, add):
        if ql > r or qr < l:
            return
        if ql <= l and r <= qr:
            self.apply(node, l, r, add)
            return
        self.push(node, l, r)
        mid = (l + r) // 2
        self.update(node * 2, l, mid, ql, qr, add)
        self.update(node * 2 + 1, mid + 1, r, ql, qr, add)
        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]