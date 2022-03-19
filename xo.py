# писал игру по видеоуроку с YouTube


board = list(range(1, 10))

wins_coord = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]


def draw_board():
    print('-------------')
    for i in range(3):
        print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
    print('-------------')


def take_input(player_token):
    while True:
        value = input('Куда поставить:' + player_token + ' ? ')
        if not (value in "123456789"):
            print("ошибочный ввод. повторите")
            continue
        value = int(value)
        if str(board[value - 1]) in 'XO':
            print('эта клетка уже занята')
            continue
        board[value - 1] = player_token
        break


def chek_wins():
    for each in wins_coord:
        if (board[each[0] - 1]) == (board[each[1] - 1]) == (board[each[2] - 1]):
            return board[each[1] - 1]
    else:
        return False


# в видео уроке как раз рассказали что else может так же работать с функцией for

def main():
    counter = 0
    while True:
        draw_board()
        if counter % 2 == 0:
            take_input('X')
        else:
            take_input('O')
        if counter > 3:
            winner = chek_wins()
            if winner:
                draw_board()
                print(winner, 'выиграл!')
                break
        counter += 1
        if counter > 8:
            draw_board()
            print('ничья!')
            break


main()
