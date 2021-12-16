import math

class Node:
    def __init__(self, version):
        self.version = version

    def get_value(self):
        return NotImplementedError
    
    def get_version(self):
        return NotImplementedError

class Literal(Node):
    def __init__(self, version, value):
        super().__init__(version)
        self.value = value
    
    def get_value(self):
        return self.value
    
    def get_version(self):
        return self.version

class Operator(Node):
    def __init__(self, version, fn):
        super().__init__(version)
        self.children = []
        self.fn = fn
    
    def add_child(self, child):
        self.children.append(child)
    
    def get_value(self):
        return self.fn([c.get_value() for c in self.children])
    
    def get_version(self):
        return self.version + sum([c.get_version() for c in self.children])

class BITSParser:
    def __init__(self, s):
        self.bits = bin(int(line, 16))[2:].zfill(4*len(s))
        self.cursor = 0
    
    def remaining(self):
        return max(0, len(self.bits)-self.cursor)
    
    def get_bits(self, size):
        assert self.remaining() >= size, "Not enough bits available"
        r = self.bits[self.cursor:(self.cursor+size)]
        self.cursor += size
        return r

    def get_int(self, size):
        return int(self.get_bits(size), 2)
    
    def parse_literal(self):
        keep_reading = True
        b = ''
        while keep_reading:
            if self.get_bits(1) == '0':
                keep_reading = False
            b += self.get_bits(4)
        return int(b, 2)

    def parse_packet(self):
        version = self.get_int(3)
        type = self.get_int(3)
        if type==0x04:
            return Literal(version, self.parse_literal())
        else:  # operator
            if type == 0:
                fn = sum
            elif type == 1:
                fn = math.prod
            elif type == 2:
                fn = min
            elif type == 3:
                fn = max
            elif type == 5:
                fn = lambda x: 1 if x[0] > x[1] else 0
            elif type == 6:
                fn = lambda x: 1 if x[0] < x[1] else 0
            elif type == 7:
                fn = lambda x: 1 if x[0] == x[1] else 0
            node = Operator(version, fn)
            if self.get_bits(1) == '0':
                length = self.get_int(15)
                stop = self.cursor + length
                while self.cursor < stop:
                    node.add_child(self.parse_packet())
            else:
                subpackets = self.get_int(11)
                for _ in range(subpackets):
                    node.add_child(self.parse_packet())
            return node

with open('input.txt', 'r') as f:
    for line in f.read().splitlines():
        b = BITSParser(line)
        root = b.parse_packet()
        print(f'answer1: {root.get_version()}')
        print(f'answer2: {root.get_value()}')