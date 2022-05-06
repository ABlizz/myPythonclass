def win():
    win_coord = [((0, 0), (0, 1), (0, 2)),
                 ((1, 0), (1, 1), (1, 2)),
                 ((2, 0), (2, 1), (2, 2)),
                 ((0, 2), (1, 1), (2, 0)),
                 ((0, 0), (1, 1), (2, 2)),
                 ((0, 0), (1, 0), (2, 0)),
                 ((0, 1), (1, 1), (2, 1)),
                 ((0, 2), (1, 2), (2, 2))]
    for coord in win_coord:
        symbols = []

        for c in coord:
            symbols.append(field[c[0]][c[1]])

        if symbols == ["Х", "Х", "Х"]:
            print("Выиграл Х")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0 ")
            return True
    return False

field = [
    ["0", " ", " "],
    [" ", "0", " "],
    [" ", " ", "0"]
]

print(win())