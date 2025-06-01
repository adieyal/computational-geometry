class Node:
    def __init__(self, s=None):
        # Initialize a list to store the count of each lowercase English letter (26 letters)
        self.count = [0] * 26
        if s is not None:
            # If a string is provided, count the occurrences of each character
            for c in s:
                # Increment the count for the corresponding character
                self.count[ord(c) - ord('a')] += 1

def merge(L: Node, R: Node) -> Node:
    # Create a new Node to store the merged result
    res = Node()
    for i in range(26):
        # Sum the counts of each letter from both nodes
        res.count[i] = L.count[i] + R.count[i]
    return res
