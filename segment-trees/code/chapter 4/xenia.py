class Node:
    def __init__(self, value=0):
        # Store the value for this segment
        self.value = value

def merge(L: Node, R: Node, op: str) -> Node:
    # Merge two nodes using the specified operation ('or' or 'xor')
    # L, R: child nodes to merge
    # op: operation to use ('or' for bitwise OR, 'xor' for bitwise XOR)
    if op == 'or':
        # Bitwise OR of the two child values
        return Node(L.value | R.value)
    else:
        # Bitwise XOR of the two child values
        return Node(L.value ^ R.value)
