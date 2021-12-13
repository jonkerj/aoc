import bingo

numbers = list(bingo.numbers())
cards = list(bingo.cards())

best = len(numbers)
for card in cards:
    b = bingo.BingoCard(card)

    assert not b.bingo()

    for n, number in enumerate(numbers[:best], 1):
        b.draw(number)
        if b.bingo():
            score = b.score() * number

            if n < best:
                best = n
                print(f'New best, {n} moves, score={score}')
