ROW = 7
COL = 5

def print_board(board):
    for line in board:
        print()
        for object in line:
            print ("%c" %object, end = "")
    print()
def gravity(player, board, i):
    for j in range(ROW):
        if board[j][player[i]] == '-':
            gravity = j
    return gravity;
def controlwinner(board, player):
    players = {'X': 'G1', 'O': 'G2'}
    #control rows
    for i in range (ROW):
        for j in range(COL-3):
            if board[i][j]==board[i][j+1]==board[i][j+2]==board[i][j+3]==player:
                print(player, "Is the winner")
                return True
    #control columns
    for i in range (ROW-3):
        for j in range(COL):
            if board[i][j]==board[i+1][j]==board[i+2][j]==board[i+3][j]==player:
                print(player, "Is the winner")
                return True
    #control diagonals
    for i in range(3,ROW):
        for j in range (0,2):
            if board[i][j+0]==board[i-1][j+1]==board[i-2][j+2]==board[i-3][j+3]==player:
                print(players[player], "Is the winner")
                return True
    for i in range(0, 3):
        for j in range (COL-4, 0, -1):
            if board[i+1][j]==board[i+1][j+1]==board[i+2][j+2]==board[i+3][j+3]==player:
                print(player, "Is the winner")
                return True

    return False

def moves(player1,player2, board):
    players = {'G1': 'X', 'G2':'O'}
    print(players)
    for i in range (len(player1)):
        lowest = gravity(player1, board, i)
        print("G1:", player1[i])
        board[lowest][player1[i]] = 'X'
        print_board(board)
        if(controlwinner(board, players['G1'])):
             exit(1)
        lowest = gravity(player2, board, i)
        board[lowest][player2[i]] = 'O'
        print("G2:", player2[i])
        print_board(board)
        if(controlwinner(board, players['G2'])):
            exit(2)


def main():
    player1 = list()
    player2 = list()
    board = [['-' for i in range(COL)] for j in range(ROW)]


    try:
        with open("moves.txt", 'r', encoding="UTF-8") as file:
            for line in file:
                (player, move) = line.split()
                if (player=='G1'):
                    player1.append(int(move))
                elif (player == 'G2'):
                    player2.append(int(move))

    except OSError:
        print("Error")

    moves(player1, player2, board)


if __name__ == "__main__":
    main()
