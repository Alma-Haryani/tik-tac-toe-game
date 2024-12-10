# Tic Tac Toe game in Python

# Game board
board = [' ' for _ in range(9)]

# Function to insert an X or O at a given position
def insertLetter(letter, pos):
    board[pos] = letter

# Function to check if a space is free
def spaceIsFree(pos):
    return board[pos] == ' '

# Function to print the game board
def printBoard(board):
    print()
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('-----------')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('-----------')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
    print()

# Function to check if the board is full
def isBoardFull(board):
    return board.count(' ') == 0

# Function to check for a win
def isWinner(bo, le):
    winningBoards = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for i in winningBoards:
        if bo[i[0]] == bo[i[1]] == bo[i[2]] == le:
            return True
    return False

# Function to handle player move
def playerMove():
    run = True
    while run:
        move = input('Please select a position to place an \'X\' (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move-1):
                    run = False
                    insertLetter('X', move-1)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')

# Function to handle computer move
def compMove():
    run = True
    while run:
        move = 0
        for i in ['O', 'X']:
            for j in range(0, 9):
                if board[j] == ' ':
                    board[j] = i
                    if isWinner(board, i):
                        move = j
                        run = False
                        break
                    board[j] = ' '
        if move == 0:
            possibleMoves = [i for i, letter in enumerate(board) if letter == ' ' and i not in [0, 2, 6, 8]]
            move = 0
            for let in ['O', 'X']:
                for i in possibleMoves:
                    boardCopy = board[:]
                    boardCopy[i] = let
                    if isWinner(boardCopy, let):
                        move = i
                        run = False
                        break
            if move == 0:
                cornersOpen = []
                for i in [0, 2, 6, 8]:
                    if board[i] == ' ':
                        cornersOpen.append(i)
                if len(cornersOpen) > 0:
                    move = selectRandom(cornersOpen)
                else:
                    edgesOpen = []
                    for i in [1, 3, 5, 7]:
                        if board[i] == ' ':
                            edgesOpen.append(i)
                    if len(edgesOpen) > 0:
                        move = selectRandom(edgesOpen)
        insertLetter('O', move)
        return move

# Function to select a random move
def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

# Main function
def main():
    print('Welcome to Tic Tac Toe!')
    printBoard(board)

    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print('Sorry, O\'s won this time!')
            break

        if not(isWinner(board, 'X')):
            move = compMove()
            if move == 0:
                print('')
            else:
                print('Computer placed an \'O\' in position', move + 1 , ':')
                printBoard(board)
        else:
            print('X\'s won this time! Good Job!')
            break

    if isBoardFull(board):
        print('Tie Game!')

# Run the game
main()