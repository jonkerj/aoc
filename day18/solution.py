import input
import math

class Node:
    def __init__(self, parent):
        self.parent = parent
    
    def root(self):
        if self.parent is None:
            return self
        return self.parent.root()
    
    def reduce(self):
        n = self.find(lambda x: isinstance(x, Pair) and x.level() >= 4)
        if n is not None:
            explode(self.root(), n)  # would have liked to do this OO
            self.reduce()  # bohica
        n = self.find(lambda x: isinstance(x, Literal) and x.value >= 10)
        if n is not None:
            n.split()
            self.reduce()
    
    def level(self):
        if self.parent is None:
            return 0
        else:
            return self.parent.level() + 1

    def add(self, other):
        result = Pair(None, None, None)
        result.left = self.clone(result)
        result.right = other.clone(result)
        result.reduce()
        return result
    
class Literal(Node):
    def __init__(self, parent, value):
        super().__init__(parent)
        self.value = value
    
    def __str__(self):
        return str(self.value)
    
    def flatten(self):
        return [self]
    
    def split(self):
        pair = Pair(self.parent, None, None)
        pair.left = Literal(pair, math.floor(self.value/2))
        pair.right = Literal(pair, math.ceil(self.value/2))
        if self.parent.left == self:
            self.parent.left = pair
        else:
            self.parent.right = pair
    
    def find(self, fn):
        if fn(self):
            return self
        return None

    def magnitude(self):
        return self.value
    
    def clone(self, newparent):
        return Literal(newparent, self.value)

class Pair(Node):
    def __init__(self, parent, left, right):
        super().__init__(parent)
        self.left = left
        self.right = right
    
    def __str__(self):
        return f'[{self.left},{self.right}]'
    
    def flatten(self):
        return self.left.flatten() + self.right.flatten()
    
    def find(self, fn):
        if fn(self):
            return self
        r = self.left.find(fn)
        if r is not None:
            return r
        r = self.right.find(fn)
        if r is not None:
            return r
        return None

    def magnitude(self):
        return 3 * self.left.magnitude() + 2 * self.right.magnitude()

    def clone(self, newparent):
        p = Pair(newparent, None, None)
        p.left = self.left.clone(p)
        p.right = self.right.clone(p)
        return p

def sfn_factory(input, parent):
    if isinstance(input, list):
        assert len(input) == 2
        pair = Pair(parent, None, None)
        pair.left = sfn_factory(input[0], pair)
        pair.right = sfn_factory(input[1], pair)
        return pair
    else:
        return Literal(parent, input)

# tried to do it recursively, but becomes messy real quick
def explode(root, node):
    # node should be a Pair with two Literal children
    assert isinstance(node, Pair)
    assert isinstance(node.left, Literal)
    assert isinstance(node.right, Literal)

    # search for a node with identical children, as Pairs do not appear in the flattened list
    flat = root.flatten()
    idx = -1
    for i, item in enumerate(flat):
        if item == node.left and flat[i+1] == node.right: # whugh, but it works
            idx = i
            break
    
    assert idx >= 0  # we should be able to find 'node' in the flattened list

    # at this point, idx is the index of the leftmost literal of the pair
    # that means that (given within bounds):
    # idx -1 is the left neighbor
    # idx +1 is the sibling (which is going to explode)
    # idx +2 is the right neighbor

    if idx > 0:  # it's not the leftmost
        lefty = flat[idx-1]
        lefty.value += node.left.value
    if idx < len(flat)-2:  # it's not the rightmost
        righty = flat[idx+2]
        righty.value += node.right.value
    
    # kaboom
    if node.parent.right == node:
        node.parent.right = Literal(node.parent, 0)
    else:
        node.parent.left = Literal(node.parent, 0)


inputs = list(map(lambda a: sfn_factory(a, None), input.numbers))

root = inputs[0]

for to_add in inputs[1:]:
    root = root.add(to_add)

print(root.magnitude())

highest = 0
for a in range(len(inputs)):
    for b in range(len(inputs)):
        if a == b:
            continue
        m = inputs[a].add(inputs[b]).magnitude()
        if m > highest:
            highest = m
print(highest)