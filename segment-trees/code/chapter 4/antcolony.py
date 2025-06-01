from math import gcd

# Node class represents a segment with its GCD and the count of elements equal to the GCD
class Node:
    def __init__(self, strengths=None):
        # If no strengths are provided, or the list is empty, set GCD and count to 0
        if strengths is None or len(strengths) == 0:
            self.gcd = 0
            self.count = 0
        else:
            # Initialize GCD as the first element
            self.gcd = strengths[0]
            # Compute GCD of all elements in strengths
            for s in strengths[1:]:
                self.gcd = gcd(self.gcd, s)
            # Count how many elements are exactly equal to the GCD
            self.count = sum(1 for s in strengths if s == self.gcd)

# Merges two nodes into a new node representing their combined segment
def merge(L: Node, R: Node) -> Node:
    # Compute the GCD of the two segments
    g = gcd(L.gcd, R.gcd)
    count = 0
    # If left segment's GCD matches the combined GCD, add its count
    if L.gcd == g:
        count += L.count
    # If right segment's GCD matches the combined GCD, add its count
    if R.gcd == g:
        count += R.count
    # Create a new node with the combined GCD and count
    node = Node()
    node.gcd = g
    node.count = count
    return node