import numpy as np
import pygame
import math

ROWS = 3
COLUMNS = 3

white=(255,255,255)
black=(0,0,0)
height=600
width=600

size=(width, height)

def mark(row,col,player):
    board[row][col] = player

def is_valid_mark(row,col):
    return board[row][col]== 0

def is_board_full():
    for c in range(COLUMNS):
        for r in range(ROWS):
            if board[r][c] == 0:
                return False
    return True

def draw_lines():
    pygame.draw.line(window, black, (200,0), (200,600), 10)
    pygame.draw.line(window, black, (400,0), (400,600), 10)
    pygame.draw.line(window, black, (0,200), (600,200), 10)
    pygame.draw.line(window, black, (0,400), (600,400), 10)

def is_winning_move(player):
    if player == 1:
        announcement = "Player 1 won"
    else:
        announcement = "Player 2 won"
    for r in range(ROWS):
        if board[r][0] == player and board[r][1] == player and board[r][2] == player:
            print(announcement)
            return True
    for c in range(COLUMNS):
        if board[0][c] == player and board[1][c] == player and board[2][c] == player:
            print(announcement)
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
            print(announcement)
            return True
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
            print(announcement)
            return True

board = np.zeros((ROWS,COLUMNS))
game_over = False
Turn = 0

pygame.init()
window = pygame.display.set_mode(size)
pygame.display.set_caption("Tic-Tac-Toe")
window.fill(white)
draw_lines()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if Turn % 2 == 0:
                #player 1
                row = math.floor(event.pos[1]/200)
                col = math.floor(event.pos[0]/200)
                if is_valid_mark(row,col):
                    mark(row,col,1)
                    if is_winning_move(1):
                        game_over = True
                else:
                    Turn -=1
            else:
                #player 2
                row = math.floor(event.pos[1]/200)
                col = math.floor(event.pos[0]/200)
                if is_valid_mark(row,col):
                    mark(row,col,2)
                    if is_winning_move(2):
                        game_over = True
                else:
                    Turn -=1

            Turn +=1
            print(board)
            # Draw the marks on the board
            for r in range(ROWS):
                for c in range(COLUMNS):
                    if board[r][c] == 1:
                        pygame.draw.line(window, black, (c*200 + 50, r*200 + 50), (c*200 + 150, r*200 + 150), 5)
                        pygame.draw.line(window, black, (c*200 + 150, r*200 + 50), (c*200 + 50, r*200 + 150), 5)
                    elif board[r][c] == 2:
                        pygame.draw.circle(window, black, (c*200 + 100, r*200 + 100), 50, 5)

            pygame.display.update()

    if game_over == True:
        print("game over")
