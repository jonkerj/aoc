import bingo

numbers = list(bingo.numbers())
cards = list(bingo.cards())

worst = 0
for c, card in enumerate(cards, 1):
    b = bingo.BingoCard(card)

    assert not b.bingo()

    for n, number in enumerate(numbers, 1):
        b.draw(number)
        if b.bingo():
            
            if n > worst:
                score = b.score() * number
                worst = n
                print(f'New worst, card {c}: {n} moves, score={score}, board={b.card}')
            break
