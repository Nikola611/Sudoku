import pygame, sys
from constants import *
from cell import Cell
from sudoku_generator import SudokuGenerator

# global temp vars
x = 1
y = 1
yn = 0

# generates Sudoku
def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    global answerKey
    answerKey = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
    for s in range(9):
        for t in range(9):
            answerKey[s][t] = board[s][t]
    sudoku.remove_cells()
    board = sudoku.get_board()
    global boardTemp
    boardTemp = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
    for i in range(9):
        for j in range(9):
            boardTemp[i][j] = board[i][j]
    print(answerKey)
    print(board)
    return board

# Board class
class Board:
    def __init__(self, rows, cols, width, height, screen, difficulty):
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.board = generate_sudoku(9, difficulty) # Set to 30 for testing
        self.cells = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
        # New Variable self.origboard: Copy of self.board used by reset_to_original()
        #self.cells = [Cell(self.board[self.rows][self.cols], self.rows, self.cols, self.screen, CELL_WIDTH, CELL_HEIGHT)]
        for i in range(9):
            for j in range(9):
                self.cells[i][j] = (Cell(self.board[i][j], i, j, self.screen, 7, 7))



# creates the board
    def board_initialize(self):
        for i in range(9):
            for j in range(9):
                    self.cells[i][j].draw(i * 49, j * 49)
                    pygame.display.update()
        for i in range(1, 3):
            pygame.draw.line(self.screen, LINE_COLOR, (0, SQUARE_SIZE * i),
                             (WIDTH, SQUARE_SIZE * i), LINE_WIDTH)
            # draw vertical lines
        for i in range(1, 3):
            pygame.draw.line(self.screen, LINE_COLOR, (SQUARE_SIZE * i, 0),
                             (SQUARE_SIZE * i, HEIGHT), LINE_WIDTH)


# draws the board
    def draw(self):
        for i in range(9):
            for j in range(9):
                if boardTemp[i][j] != 0:
                    self.cells[i][j].draw(i*49,j*49)
                    pygame.display.update()
        for i in range(1, 3):
            pygame.draw.line(self.screen, LINE_COLOR, (0, SQUARE_SIZE * i),
                             (WIDTH, SQUARE_SIZE * i), LINE_WIDTH)
            # draw vertical lines
        for i in range(1, 3):
            pygame.draw.line(self.screen, LINE_COLOR, (SQUARE_SIZE * i, 0),
                             (SQUARE_SIZE * i, HEIGHT), LINE_WIDTH)

# draws the sketch cells of the board
    def draw_sketch(self):
        self.cells[x][y].draw_sketch(x*49,y*49)
        pygame.display.update()
        for i in range(1, 3):
            pygame.draw.line(self.screen, LINE_COLOR, (0, SQUARE_SIZE * i),
                             (WIDTH, SQUARE_SIZE * i), LINE_WIDTH)
            # draw vertical lines
        for i in range(1, 3):
            pygame.draw.line(self.screen, LINE_COLOR, (SQUARE_SIZE * i, 0),
                             (SQUARE_SIZE * i, HEIGHT), LINE_WIDTH)


# Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes.
# Draws every cell on this board.
# Adjusted From Video, [SQUARE_SIZE*(i*3)]
    def get_cord(self, pos):
        global x
        x = pos[0] // 49
        global y
        y = pos[1] // 49

# select function that creates board buttons, allows cells to be selected
    def select(self):
        global yn
        global y
        # button font
        buttonFont = pygame.font.Font(None, 40)

        # exit button
        exitText = buttonFont.render("Exit", 0, (255, 255, 255))
        exitSurface = pygame.Surface((exitText.get_size()[0] + 20, exitText.get_size()[1] + 20))
        exitSurface.fill(LINE_COLOR)
        exitSurface.blit(exitText, (10, 10))
        exitRectangle = exitSurface.get_rect(
            center=(WIDTH // 2 + 150, HEIGHT // 2 + 220))
        self.screen.blit(exitSurface, exitRectangle)

        # restart button
        restartText = buttonFont.render("Restart", 0, (255, 255, 255))
        restartSurface = pygame.Surface((restartText.get_size()[0] + 20, restartText.get_size()[1] + 20))
        restartSurface.fill(LINE_COLOR)
        restartSurface.blit(restartText, (10, 10))
        restartRectangle = restartSurface.get_rect(
            center=(WIDTH // 2, HEIGHT // 2 + 220))
        self.screen.blit(restartSurface, restartRectangle)

        # reset button
        resetText = buttonFont.render("Reset", 0, (255, 255, 255))
        resetSurface = pygame.Surface((resetText.get_size()[0] + 20, resetText.get_size()[1] + 20))
        resetSurface.fill(LINE_COLOR)
        resetSurface.blit(resetText, (10, 10))
        resetRectangle = resetSurface.get_rect(
            center=(WIDTH // 2 - 150, HEIGHT // 2 + 220))
        self.screen.blit(resetSurface, resetRectangle)

        # pygame event part of the program to update cells and button functionality
        for event in pygame.event.get():
            if yn == 1:
                if event.type == pygame.KEYUP:
                    # allows for key down
                    if event.key == pygame.K_1:
                        self.cells[x][y] = (Cell(1, x, y, self.screen, 7, 7))
                        self.board[x][y] = 1
                        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(x * 49, y * 49, 49, 49))
                        self.draw_sketch()
                    if event.key == pygame.K_2:
                        self.cells[x][y] = (Cell(2, x, y, self.screen, 7, 7))
                        self.board[x][y] = 2
                        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(x * 49, y * 49, 49, 49))
                        self.draw_sketch()
                    if event.key == pygame.K_3:
                        self.cells[x][y] = (Cell(3, x, y, self.screen, 7, 7))
                        self.board[x][y] = 3
                        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(x * 49, y * 49, 49, 49))
                        self.draw_sketch()
                    if event.key == pygame.K_4:
                        self.cells[x][y] = (Cell(4, x, y, self.screen, 7, 7))
                        self.board[x][y] = 4
                        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(x * 49, y * 49, 49, 49))
                        self.draw_sketch()
                    if event.key == pygame.K_5:
                        self.cells[x][y] = (Cell(5, x, y, self.screen, 7, 7))
                        self.board[x][y] = 5
                        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(x * 49, y * 49, 49, 49))
                        self.draw_sketch()
                    if event.key == pygame.K_6:
                        self.cells[x][y] = (Cell(6, x, y, self.screen, 7, 7))
                        self.board[x][y] = 6
                        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(x * 49, y * 49, 49, 49))
                        self.draw_sketch()
                    if event.key == pygame.K_7:
                        self.cells[x][y] = (Cell(7, x, y, self.screen, 7, 7))
                        self.board[x][y] = 7
                        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(x * 49, y * 49, 49, 49))
                        self.draw_sketch()
                    if event.key == pygame.K_8:
                        self.cells[x][y] = (Cell(8, x, y, self.screen, 7, 7))
                        self.board[x][y] = 8
                        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(x * 49, y * 49, 49, 49))
                        self.draw_sketch()
                    if event.key == pygame.K_9:
                        self.cells[x][y] = (Cell(9, x, y, self.screen, 7, 7))
                        self.board[x][y] = 9
                        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(x * 49, y * 49, 49, 49))
                        self.draw_sketch()
                    if event.key == pygame.K_BACKSPACE:
                        self.cells[x][y] = (Cell(0, x, y, self.screen, 7, 7))
                        self.board[x][y] = 0
                        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(x * 49, y * 49, 49, 49))
                        self.draw_sketch()

            # allows for system exit
            if event.type == pygame.QUIT:
                sys.exit()

            # allows for button functionality
            if event.type == pygame.MOUSEBUTTONDOWN:
                if y <= 8:
                        pygame.draw.rect(self.screen, (155, 155, 155), pygame.Rect(x * 49, y * 49, 49, 49), 2)
                        for i in range(1, 3):
                            pygame.draw.line(self.screen, LINE_COLOR, (0, SQUARE_SIZE * i),
                                             (WIDTH, SQUARE_SIZE * i), LINE_WIDTH)
                            # draw vertical lines
                        for i in range(1, 3):
                            pygame.draw.line(self.screen, LINE_COLOR, (SQUARE_SIZE * i, 0),
                                             (SQUARE_SIZE * i, HEIGHT), LINE_WIDTH)
                        pos = pygame.mouse.get_pos()
                        self.get_cord(pos)
                        if y <= 8:
                            if boardTemp[x][y] == 0:
                                pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(x*49, y*49, 49, 49), 2)
                                yn = 1
                            else:
                                yn = 0
                else:
                    y = 1

            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exitRectangle.collidepoint(event.pos):
                    sys.exit()
                if resetRectangle.collidepoint(event.pos):
                    self.reset_to_original()
                if restartRectangle.collidepoint(event.pos):
                    return -1
        pygame.display.update()
        return 0

    # gets the position of where the mouse button clicks are happening
    def click(self, x, y):
        for i in range(self.rows):
            for j in range(self.cols):
                if i == x and j == y:
                    return i, j

    # resets the board
    def reset_to_original(self):
        self.screen.fill(BG_COLOR)
        for i in range(9):
            for j in range(9):
                self.board[i][j] = boardTemp[i][j]
                self.cells[i][j] = (Cell(self.board[i][j], i, j, self.screen, 7, 7))
        self.board_initialize()

    # checks if board is full
    def is_full(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return True
        return False


    # checks to see if board inputted by user is correct
    def check_answer(self):
        if answerKey == self.board:
            return True
        else:
            return False

# main function
if __name__ ==  '__main__':
    while True:
        pygame.init()
        x = 0
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        screen.fill(BG_COLOR)
        pygame.display.set_caption("Sudoku")

        board = Board(9, 9, WIDTH, HEIGHT, screen, difficulty=30)
        board.board_initialize()
        while x == 0:
            x = board.select()
            if board.is_full() == False:
                    board.check_answer()
            pygame.display.update()

