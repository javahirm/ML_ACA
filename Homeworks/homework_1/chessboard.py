py = int(input("Y coordinate: "))
px = int(input("X coordinate: "))
possible_moves = [(py + 2, px + 1), (py + 2, px - 1),
                  (py + 1, px + 2), (py + 1, px - 2),
                  (py - 2, px - 1), (py - 1, px - 2),
                  (py - 1, px + 2), (py - 2, px + 1)]
print(possible_moves)
