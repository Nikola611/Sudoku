import math,random


# creating the SudokuGenerator
class SudokuGenerator:

    def __init__(self, size, removed_cells):
      self.row_length = size
      self.removed_cells = removed_cells
      self.box_length = 3
      self.board = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]


    # returns the board
    def get_board(self):
      return self.board

    # prints the board
    def print_board(self, board):
      count = 0
      print("Here is the board")
      for f in range(0,9):
       for i in board[f]:
         count +=1
         print(i, end=" ")
         if count == 9:
           print("")
           count = 0 

    # Checks to see if number can go in specified row
    def valid_in_row(self, row, num):
      rowNum = self.board[row]
      if num in rowNum:
        return False
      else:
        return True
      
    # Checks to see if number can go in specified col
    def valid_in_col(self, col, num):
      colNum = []
      for i in range(9):
        colNum.append(self.board[i][col])
      if num in colNum:
        return False
      else:
        return True

    # Checks to see if number can go in box
    def valid_in_box(self, row_start, col_start, num):
      
      row = (row_start//3) * 3
      col = (col_start//3) * 3

      for i in range(row, row + 3):
        for j in range(col, col + 3):
          if self.board[i][j] == num:
            return False
      return True
      
    # checks if each row and 3x3 box is valid
    def is_valid(self, row, col, num):
      if self.valid_in_row(row, num) == False:
        return False
      elif self.valid_in_col(col,num) == False:
        return False
      elif self. valid_in_box(row, col, num) == False:
        return False
      else:
        return True

    # fills the box
    def fill_box(self, row_start, col_start):
      num = int()
      for i in range(row_start, row_start + 3):
        for j in range(col_start, col_start+ 3):
          while True:
            num = random.randrange(1, 10)
            if self.valid_in_box(i, j, num) == True:
              self.board[i][j] = num
              break

    # fills diagonal
    def fill_diagonal(self):
      self.fill_box(0,0)
      self.fill_box(3,3)
      self.fill_box(6,6)


    # Do not change***
    # fills the remaining spots on board, provided
    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True
        
        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    # Do not change****
    # fills all values, provided
    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    # removes the specified amount of cells from the board
    def remove_cells(self):
      count = self.removed_cells
      while count != 0:
        index = random.randrange(1,self.row_length*self.row_length)-1
        #print(index)
        i = index//9
        j = index%9
        if self.board[i][j] != 0:
          count -= 1
          self.board[i][j] = 0

        
# Do not change****
# generates the sudoku board, provided
def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board
