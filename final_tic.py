board  = ['' for x in range(10)]

def insertLetter(letter,pos):
    board[pos] = letter


def spaceisFree(pos):
    return board[pos] == ' '

def printBoard(board):
    # "board" is a list of 10 strings representing the board (ignore index 0)
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def isWinner(bo,le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

def playerMove():
    run = True
    while run:
        move = int(input('Please select a position to place an X (1-9):'))
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceisFree(move):
                    run = False
                    insertLetter('X',move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number no strings!')

def compMove():

    #Algo has 3  steps
    #1 is there a move that the AI can do that results in it winning if so take that move and WIN
    #2 if we cant win, find a move that the player can make that will win them the game in the next turn
    # Block that move by moving into that position
    #3 If the AI cant win in the next move and the player cant win find a corner to move to  if the center is not taken
    #take the center else take the edges

    #any empty squares left in the board
    #this is a for loop in one line so what enumerate does it takes all the indices and values in our list
    # e.g 0-' ' 1-X 2-O
    #if the letter is blank and the index is not 0 and this will generate a list of all the positions that we can move into
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0 # result for Tie Game if we havent found a move to win

    # Make a copy of the board and check every position see if it is a winning move

    for let in ['O', 'X']: # check if O is going to win and then X is going to win
        for i in possibleMoves:
            boardCopy = board[:] # make a clone and create a new space in memory for them, lists are mutable
            boardCopy[i] = let # make a copy and place our letter into an empty space
            if isWinner(boardCopy, let): # check if it is a winning move
                move = i #the empty space that is a winning move
                return move
        # After running for O check if the player is going to win and then block their move by checking if there is a winnign move available

    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)

    return move



def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]

def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def main():
    global board
    print("Hari and Patrick Welcome you to Tic Tac Toe")
    printBoard(board)
    while not(isBoardFull(board)):
        if not isWinner(board,'O'): #Computer is Os and Human is Xs
            playerMove()
            printBoard(board)
        else:
            print('Sorry the AI has Won,you suck')
            break;
        if not isWinner(board,'X'): #Computer is Os and Human is Xs
            move = compMove()
            if move == 0: # Computer move doesnt work as the board is full
                print('Tie Game')
            else:
                insertLetter('O',move)
                print('The AI has placed an O in position',move,':')
                printBoard(board)
        else:
            print( ' Player won this time! Good Job!')
            break;
    if isBoardFull(board):
        print('Draw Game!')

    while True:
        answer = input('Do you want to play again? (Y/N)')
        if answer.lower() == 'y' or answer.lower == 'yes':
            board = [' ' for x in range(10)]
            print('-----------------------------------')
            main()
        else:
            break







main()
