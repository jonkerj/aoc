import copy

def numbers():
    with open('input.txt', 'r') as f:
        line = f.readline()

        yield from map(int, line.strip().split(','))

def cards():
    with open('input.txt', 'r') as f:
        f.readline()
        f.readline() # weg ermee

        card = []
        while True:
            line = f.readline()

            if line == '\n' or line == '':
                if len(card) > 0:
                    yield card
                    card = []

                if line == '':
                    break
                else:
                    continue
            
            card.append([int(n) for n in line.split()])

class BingoCard:
    def __init__(self, card):
        self.card = copy.deepcopy(card)
    
    def draw(self, number):
        for i in range(5):
            for j in range(5):
                if self.card[i][j] == number:
                    self.card[i][j] = -1
    
    def bingo(self):
        for i in range(5):
            if sum(self.card[i]) == -5:
                return True
            if sum([self.card[j][i] for j in range(5)]) == -5:
                return True
        return False
    
    def score(self):
        s = 0
        for i in range(5):
            s += sum([n for n in self.card[i] if n >= 0])
        return s