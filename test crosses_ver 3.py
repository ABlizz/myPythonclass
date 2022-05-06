def win():
    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(field[i][j])
        if symbols == ["Х", "Х", "Х"]:
            print("Выиграл Х")
            return True

    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(field[j][i])
        if symbols == ["Х", "Х", "Х"]:
            print("Выиграл Х")
            return True

    symbols = []
    for i in range(3):
        symbols.append(field[i][i])
    if symbols == ["Х", "Х", "Х"]:
        print("Выиграл Х")
        return True

    symbols = []
    for i in range(3):
        symbols.append(field[i][2-i])
    if symbols == ["Х", "Х", "Х"]:
        print("Выиграл Х")
        return True

    return False


field = [
    ["0", " ", " "],
    ["0", " ", " "],
    ["0", " ", " "]
]


win()
