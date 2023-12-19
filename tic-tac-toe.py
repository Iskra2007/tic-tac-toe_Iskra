list_all = [[-1, -1], [-1, 0], [-1, 1], [-1, 2], [-1, 3], [0, -1], [1, -1], [2, -1], [3, -1]]
wins_0 = 0
wins_x = 0
t = 0
board = [[' ', 0, 1, 2],
       [0, '-', '-', '-'],
       [1, '-', '-', '-'],
       [2, '-', '-', '-']]
for i in range(4):
    for j in range(4):
        print(board[i][j], end=' ')
    print()

def wins(count):
    global board
    global t
    if board[1][1] == count and board[1][2] == count and board[1][3] == count:
        print('выиграли ', count)
        return True
    elif board[2][1] == count and board[2][2] == count and board[2][3] == count:
        print('выиграли ', count)
        return True
    elif board[3][1] == count and board[3][2] == count and board[3][3] == count:
        print('выиграли ', count)
        return True
    elif board[1][1] == count and board[2][1] == count and board[3][1] == count:
        print('выиграли ', count)
        return True
    elif board[1][2] == count and board[2][2] == count and board[3][2] == count:
        print('выиграли ', count)
        return True
    elif board[1][3] == count and board[2][3] == count and board[3][3] == count:
        print('выиграли ', count)
        return True
    elif board[1][1] == count and board[2][2] == count and board[3][3] == count:
        print('выиграли ', count)
        return True
    elif board[1][3] == count and board[2][2] == count and board[3][1] == count:
        print('выиграли ', count)
        return True
    else:
        return False

while True:
    while True:
        print("введите место куда хотите поставить x:")
        position_xg = int(input('по гаризонтали:'))
        position_xv = int(input('по вертикали:'))
        listx = []
        listx += position_xg, position_xv
        if listx in list_all:
            print("это поле уже занято")
        else:
            list_all.append(listx)
            t += 1
            break


    for i in range(4):
        for j in range(4):
            board[position_xg + 1][position_xv + 1] = 'x'
            print(board[i][j], end=' ')
        print()

    if wins('x'):
        wins_x += 1
        print('Победы:')
        print(wins_x, ':', wins_0)
        exit1 = input('напишите "да", если хотите продолжить, "нет", если не хотите:')
        if exit1 == "да":
            list_all = [[-1, -1], [-1, 0], [-1, 1], [-1, 2], [-1, 3], [0, -1], [1, -1], [2, -1], [3, -1]]
            t = 0
            board = [[' ', 0, 1, 2],
                     [0, '-', '-', '-'],
                     [1, '-', '-', '-'],
                     [2, '-', '-', '-']]
            for i in range(4):
                for j in range(4):
                    print(board[i][j], end=' ')
                print()
            while True:
                print("введите место куда хотите поставить x:")
                position_xg = int(input('по гаризонтали:'))
                position_xv = int(input('по вертикали:'))
                listx = []
                listx += position_xg, position_xv
                if listx in list_all:
                    print("это поле уже занято")
                else:
                    list_all.append(listx)
                    t += 1
                    break

            for i in range(4):
                for j in range(4):
                    board[position_xg + 1][position_xv + 1] = 'x'
                    print(board[i][j], end=' ')
                print()
        else:
            break
    elif t == 5:
        print('Ничья')
        print('Победы:')
        print(wins_x, ':', wins_0)
        exit1 = input('напишите "да", если хотите продолжить, "нет", если не хотите:')
        if exit1 == "да":
            list_all = [[-1, -1], [-1, 0], [-1, 1], [-1, 2], [-1, 3], [0, -1], [1, -1], [2, -1], [3, -1]]
            t = 0
            board = [[' ', 0, 1, 2],
                     [0, '-', '-', '-'],
                     [1, '-', '-', '-'],
                     [2, '-', '-', '-']]
            for i in range(4):
                for j in range(4):
                    print(board[i][j], end=' ')
                print()
            while True:
                print("введите место куда хотите поставить x:")
                position_xg = int(input('по гаризонтали:'))
                position_xv = int(input('по вертикали:'))
                listx = []
                listx += position_xg, position_xv
                if listx in list_all:
                    print("это поле уже занято")
                else:
                    list_all.append(listx)
                    t += 1
                    break

            for i in range(4):
                for j in range(4):
                    board[position_xg + 1][position_xv + 1] = 'x'
                    print(board[i][j], end=' ')
                print()
        else:
            break

    while True:
        print("введите место куда хотите поставить 0:")
        position_0g = int(input('по гаризонтали:'))
        position_0v = int(input('по вертикали:'))
        listx = []
        listx += position_0g, position_0v
        if listx in list_all:
            print("это поле уже занято")
        else:
            list_all.append(listx)
            break

    for i in range(4):
        for j in range(4):
            board[position_0g + 1][position_0v + 1] = '0'
            print(board[i][j], end=' ')
        print()

    if wins('0'):
        wins_0 += 1
        print('Победы:')
        print(wins_x, ':', wins_0)
        exit1 = input('напишите "да", если хотите продолжить, "нет", если не хотите:')
        if exit1 == "да":
            list_all = [[-1, -1], [-1, 0], [-1, 1], [-1, 2], [-1, 3], [0, -1], [1, -1], [2, -1], [3, -1]]
            t = 0
            board = [[' ', 0, 1, 2],
                     [0, '-', '-', '-'],
                     [1, '-', '-', '-'],
                     [2, '-', '-', '-']]
            for i in range(4):
                for j in range(4):
                    print(board[i][j], end=' ')
                print()
        else:
            break
print('До свидания!!')


