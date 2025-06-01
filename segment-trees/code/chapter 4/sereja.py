class Node:
    def __init__(self, c=None):
        # If no character is provided, initialize all counts to 0
        if c is None:
            self.open = self.close = self.pairs = 0
        else:
            # If the character is '(', increment open count
            self.open = 1 if c == '(' else 0
            # If the character is ')', increment close count
            self.close = 1 if c == ')' else 0
            # Initially, there are no pairs
            self.pairs = 0

def merge(L: Node, R: Node) -> Node:
    # Find the number of matching pairs between L's opens and R's closes
    match = min(L.open, R.close)
    res = Node()
    # Total pairs: pairs from L, pairs from R, plus new matches
    res.pairs = L.pairs + R.pairs + match
    # Remaining opens: opens from both sides minus those matched
    res.open = L.open + R.open - match
    # Remaining closes: closes from both sides minus those matched
    res.close = L.close + R.close - match
    return res