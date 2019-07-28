board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
turn_num = 1


def dis_board():
    print(board[0] + '|' + board[1] + '|' + board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8])


def handle_turn(count):
    if count % 2 == 0:
        return "O"
    else:
        return "X"


def play_game():
    enter = int(input('enter the position you want to select'))
    if 0 < enter < 10:
        global turn_num
        if board[enter - 1] == '-':
            board[enter - 1] = handle_turn(turn_num)
            dis_board()
            turn_num = turn_num + 1
        else:
            print("position is already filled select some other position")
            play_game()
    else:
        print("entered position is wrong please enter the position between 1-9")
        play_game()


def check_winner():
    row1 = board[0:3]
    row2 = board[3:6]
    row3 = board[6:10]
    col1 = board[0:7:3]
    col2 = board[1:8:3]
    col3 = board[2:9:3]
    dig1 = board[0::4]
    dig2 = board[2:7:2]

    def element_match(row):
        v1 = row[0]
        match = True
        for z in row:
            if v1 != z or v1 == '-':
                match = False
        return match
    winner = [None] * 8
    winner[0] = element_match(row1)
    winner[1] = element_match(row2)
    winner[2] = element_match(row3)
    winner[3] = element_match(col1)
    winner[4] = element_match(col2)
    winner[5] = element_match(col3)
    winner[6] = element_match(dig1)
    winner[7] = element_match(dig2)
    for i in winner:
        if i:
            print("!!!!!Hurrray you have WON!!!!!")
            break
    if turn_num == 10 and i == False:
        print("oops..... its a tie......Better luck Next Time!!!!!")
    elif turn_num != 10 and i == False:
        finalize_win()

def finalize_win():
    enter = int(input('enter the position you want to select'))
    if 0 < enter < 10:
        if board[enter - 1] == '-':
            global turn_num
            board[enter - 1] = handle_turn(turn_num)
            dis_board()
            turn_num = turn_num + 1
        else:
            print("position is already filled select some other position")
            finalize_win()
    else:
        print("entered position is wrong please enter the position between 1-9")
        finalize_win()
    if 5 < turn_num <= 11 :
        check_winner()


def main():
    dis_board()
    for j in range(6):
        if turn_num <= 5:
            play_game()
        elif 6 <= turn_num < 10:
            check_winner()


main()
