def greetings():
    print()
    print("      ------------      ")
    print("    Добро пожаловать    ")
    print("        в игру          ")
    print("    крестики-нолики! ")
    print("      ------------      ")
    print()
    print(" формат ввода клетки: x y     ")
    print(" х - номер строки ")
    print(" y - номер столбца")
    print()

def show():
    print(f"  | 0 | 1 | 2 | ")
    print("---------------")
    for i in range(3):
        row_info = " | ".join(field[i])
        print(f"{i} | {row_info} | ")
        print("---------------")

def ask():
    while True:
        cords = input("Ваш ход: ").split()

        if len(cords) != 2:
            print("Введите 2 координаты")
            continue

        x, y = cords

        if not(x.isdigit()) or not(y.isdigit()):
            print("Введите число")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Координаты вне диапазона! ")
            continue

        if field[x][y] != " ":
            print("Клетка занята!")
            continue

        return x, y

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
            print("-- Выиграл Х! -- ")
            return True
        if symbols == ["0", "0", "0"]:
            print("-- Выиграл '0'! -- ")
            return True

    return False

greetings()

field = [[" "] * 3 for i in range(3)]

num = 0
while True:
    num += 1

    show()

    if num % 2 == 1:
        print("Ход Х")
    else:
        print("Ход '0'")

    x, y = ask()

    if num % 2 == 1:
        field[x][y] = "Х"
    else:
        field[x][y] = "0"

    if win():
        break

    if num == 9:
        print("--Ничья--")
        break