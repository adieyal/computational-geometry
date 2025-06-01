class Node:
    def __init__(self, c=None):
        # If no character is provided, initialize all counts and lengths to 0
        if c is None:
            self.cnt4 = self.cnt7 = 0  # Count of '4's and '7's
            self.lnds = self.lnds_rev = 0  # LNDS and reversed LNDS
        else:
            # If a character is provided, set counts based on whether it's '4' or '7'
            self.cnt4 = 1 if c == '4' else 0  # 1 if c is '4', else 0
            self.cnt7 = 1 if c == '7' else 0  # 1 if c is '7', else 0
            self.lnds = 1  # A single character is always a subsequence of length 1
            self.lnds_rev = 1  # Same for reversed order

    def flip(self):
        # Swap the counts of '4' and '7', and also swap LNDS and its reverse
        # This simulates flipping all '4's to '7's and vice versa in a segment
        self.cnt4, self.cnt7 = self.cnt7, self.cnt4
        self.lnds, self.lnds_rev = self.lnds_rev, self.lnds

def merge(L: Node, R: Node) -> Node:
    # Merge two nodes (segments) to form a new node representing their union
    res = Node()
    # Total count of '4's and '7's is the sum from both segments
    res.cnt4 = L.cnt4 + R.cnt4
    res.cnt7 = L.cnt7 + R.cnt7
    # LNDS: Longest Non-Decreasing Subsequence
    # Option 1: Take LNDS from left and all '7's from right
    # Option 2: Take all '4's from left and LNDS from right
    res.lnds = max(L.lnds + R.cnt7, L.cnt4 + R.lnds)
    # LNDS in reversed order: Longest Non-Increasing Subsequence
    # Option 1: Take reversed LNDS from left and all '4's from right
    # Option 2: Take all '7's from left and reversed LNDS from right
    res.lnds_rev = max(L.lnds_rev + R.cnt4, L.cnt7 + R.lnds_rev)
    return res
