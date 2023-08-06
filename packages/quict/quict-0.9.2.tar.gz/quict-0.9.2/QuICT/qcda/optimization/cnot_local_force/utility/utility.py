class path(object):
    """ record the path of bfs

    Attribute:
        father_node(int): father in bfs
        CX_tuple(tuple<int, int>): the way father access to son
    """

    def __init__(self, father_node, control, target):
        """ initial method

        father_node(int): the order of father_node
        control(int): the control bit of CX
        target(int): the target bit of CX
        """
        self.father_node = father_node
        self.CX_tuple = (control, target)


def apply_cx(state, control, target, n):
    """ apply cnot gate to the state

    Args:
        state(int): the state represent the matrix
        control(int): the control index for the cx gate
        target(int): the target index for the cx gate
        n(int): number of qubits in the matrix
    Returns:
        int: the new state after applying the gate
    """

    control_col: int = n * control
    target_col: int = n * target

    for i in range(n):
        if state & (1 << (control_col + i)):
            state ^= (1 << (target_col + i))
    return state


def count(nn):
    ans = 1
    for i in range(nn):
        ans *= ((1 << nn) - (1 << i))
    return ans


def generate_layer(n):
    """ generate combination layer for n qubits(n in [2, 5])

    Args:
        n(int): the qubits of layer, in [2, 5]
    Returns:
        list<list<tuple<int, int>>>: the list of layers
    """
    layers = []

    # single layer
    for i in range(n):
        for j in range(n):
            if i != j:
                layers.append([(i, j)])

    # double layer
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    if i != j and i != k and i != l and j != k and j != l and k != l:
                        layers.append([(i, j), (k, l)])

    return layers
