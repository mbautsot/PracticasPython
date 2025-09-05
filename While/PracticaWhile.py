print('PlayListRatings')
print('='*70)

print('=' * 70)
i = 0  # Inicializa l indice
PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
while i < len(PlayListRatings):
    rating = PlayListRatings[i]
    if rating < 6:
        break
    print(rating)
    i += 1

print('='*70)
squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i = 0
while (i < len(squares) and squares[i] == 'orange'):
    new_squares.append(squares[i])
    i += 1
print(new_squares)
print('='*70)