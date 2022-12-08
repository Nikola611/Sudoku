from sudoku_generator import SudokuGenerator
from constants import *
from board import Board
import pygame, sys

#creating the main menu
def create_main_menu():
    # Font
    titleFont = pygame.font.Font(None, 60)
    buttonFont = pygame.font.Font(None, 40)
    subTitleFont = pygame.font.Font(None, 50)

    # Background
    screen.fill(BG_COLOR)

    # Title
    titleSurface = titleFont.render("Welcome To Sudoku", 0, LINE_COLOR)
    titleRectangle = titleSurface.get_rect(
      center =(WIDTH // 2, HEIGHT // 2- 150))
    screen.blit(titleSurface, titleRectangle)
    subTitleSurface = subTitleFont.render("Select Game Mode", 0, LINE_COLOR)
    subTitleRectangle = subTitleSurface.get_rect(
        center =(WIDTH // 2, HEIGHT // 2 -60))
    screen.blit(subTitleSurface, subTitleRectangle)

    # Button Font
    easyText = buttonFont.render("Easy", 0, (255, 255, 255))
    mediumText = buttonFont.render("Medium", 0, (255, 255, 255))
    hardText = buttonFont.render("Hard", 0, (255, 255, 255))

    # Button background
    easySurface = pygame.Surface((easyText.get_size()[0]+20, easyText.get_size()[1] + 20))
    easySurface.fill(LINE_COLOR)
    easySurface.blit(easyText, (10, 10))
    mediumSurface = pygame.Surface((mediumText.get_size()[0]+20, mediumText.get_size()[1] + 20))
    mediumSurface.fill(LINE_COLOR)
    mediumSurface.blit(mediumText, (10, 10))
    hardSurface = pygame.Surface((hardText.get_size()[0] + 20, hardText.get_size()[1] + 20))
    hardSurface.fill(LINE_COLOR)
    hardSurface.blit(hardText, (10, 10))
    # Button
    easyRectangle = easySurface.get_rect(
        center=(WIDTH // 2 - 150, HEIGHT // 2 + 80))
    mediumRectangle = mediumSurface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 80))
    hardRectangle = hardSurface.get_rect(
        center=(WIDTH // 2 + 150, HEIGHT // 2 + 80))

    screen.blit(easySurface, easyRectangle)
    screen.blit(mediumSurface, mediumRectangle)
    screen.blit(hardSurface, hardRectangle)

    # Makes it so that the user MUST do something
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if easyRectangle.collidepoint(event.pos):
                return 1
            elif mediumRectangle.collidepoint(event.pos):
                return 40
            elif hardRectangle.collidepoint(event.pos):
                return 50
      pygame.display.update()

def create_game_over(game_over):
    # Font
    game_overFont = pygame.font.Font(None, 40)
    buttonFont = pygame.font.Font(None, 40)

    # Screen color
    screen.fill(BG_COLOR)

    # get text
    if game_over != False:
        text = 'Game Won!'
    else:
        text = 'Game Over :('

    game_overSurf = game_overFont.render(text, 0, LINE_COLOR)
    game_overRect = game_overSurf.get_rect(
        center = (WIDTH// 2, HEIGHT // 2 - 100)
    )
    screen.blit(game_overSurf, game_overRect)

    if game_over != False:
        exitText = buttonFont.render("Exit", 0, (255, 255, 255))
        exitSurface = pygame.Surface((exitText.get_size()[0] + 20, exitText.get_size()[1] + 20))
        exitSurface.fill(LINE_COLOR)
        exitSurface.blit(exitText, (10, 10))
        exitRectangle = exitSurface.get_rect(
            center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(exitSurface, exitRectangle)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if exitRectangle.collidepoint(event.pos):
                        sys.exit()
            pygame.display.update()
    else:
        try_againText = buttonFont.render("Try Again?", 0, (255, 255, 255))
        try_againSurface = pygame.Surface((try_againText.get_size()[0] + 20, try_againText.get_size()[1] + 20))
        try_againSurface.fill(LINE_COLOR)
        try_againSurface.blit(try_againText, (10, 10))
        try_againRectangle = try_againSurface.get_rect(
            center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(try_againSurface, try_againRectangle)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if try_againRectangle.collidepoint(event.pos):
                        return -1
            pygame.display.update()


def create_board():
    screen.fill(BG_COLOR)
    board.board_initialize()
    pygame.display.update()
#creating the main function
if __name__ == '__main__':
    while True:
        x = 0
        game_over = False
        winner = 0

        pygame.init()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Sudoku")

        global board
        board = Board(9, 9, WIDTH, HEIGHT, screen, create_main_menu())
        create_board()
        while x == 0:
            x = board.select()
            if board.is_full() == False:
                x = create_game_over(board.check_answer())


    #create_game_over()

'''
  screen.fill(BG_COLOR)
  board = Board(WIDTH, HEIGHT, screen, difficulty='easy')
  board.draw()
'''

