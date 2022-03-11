
from random import randint


board = [' ' for x in range(10)]

def insertLetter(letter, pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == ' '

def printBoard(board):
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

def isWinner(bo, le):
    return ((bo[1] == le and bo[2] == le and bo[3] == le)
    or (bo[4] == le and bo[5] == le and bo[6] == le)
    or (bo[7] == le and bo[8] == le and bo[9] == le)
    or (bo[1] == le and bo[4] == le and bo[7] == le)
    or (bo[2] == le and bo[5] == le and bo[8] == le)
    or (bo[3] == le and bo[6] == le and bo[9] == le)
    or (bo[1] == le and bo[5] == le and bo[9] == le)
    or (bo[3] == le and bo[5] == le and bo[7] == le))


def playerMove():
    while True:
        move = int(input("What is your move? Pick a number between 1 and 9."))
        if move in range(1, 10):
            if spaceIsFree(move):
                insertLetter("x", move)
                printBoard(board)
                return
            else: print("Pick a space that is free!")
        else: print("Your number wasn't between 1 and 9!")


def compMove():
    while True:
        move = randint(1, 9)
        if spaceIsFree(move):
            insertLetter("o", move)
            printBoard(board)
            return

def isBoardFull(board):
    return ' ' not in board[1:9]

def main():
    while not isBoardFull(board):
        playerMove()
        if not isBoardFull(board):
            compMove()
        if isWinner(board, "x"):
            print("Player Wins!!! :)")
            return
        elif isWinner(board, "o"):
            print("Computer Wins :(")
            return
    print("Neither player won :/")
    return

main()