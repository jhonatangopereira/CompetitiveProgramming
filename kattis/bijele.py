# Bijele

# 1 king, 1 queen, 2 rooks, 2 bishops, 2 knights, 8 pawns
expected_pieces = [1, 1, 2, 2, 2, 8]
chess_pieces = list(map(int, input().split())) # [1 2 3 4 5 6]

# mapping the difference between expected pieces and the input pieces
result = [expected_pieces[i] - chess_pieces[i] for i in range(len(chess_pieces))]
print(*result, sep=" ")
