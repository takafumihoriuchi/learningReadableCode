# coding=utf-8
class Player(object):
    def __init__(self, color, my_board):
        self.color    = color  # noqa
        self.my_board = my_board

    def select_point(self):
        self.row = int(input("row: "))
        self.col = int(input("col: "))
        self.put_stone()

    def put_stone(self):
        # re-input : out of range
        if self.row not in range(self.my_board.row)\
         or self.col not in range(self.my_board.col):
            print("invalid input (out of range)")
            self.select_point()
            return
        # re-input : already taken
        if self.my_board.board[self.row][self.col] != self.my_board.blank:
            print("invalid input (already taken)")
            self.select_point()
            return
        # re-input : open space, can't flip any of opponent's stone
        if self.my_board.count_up(self.row, self.col, self.color) == 0:
            print("invalid input (unflippable)")
            self.select_point()
            return
        # valid input
        self.my_board.board[self.row][self.col] = self.color
        self.flip_stone()

    """
    # TODO: in the middle of implementing a helper code for 'flip_stone()'
    def flip_stone_helper(self, out_range_s, out_range_e, ...):
        for i in range(self.row + 1, my_board.row):
            if my_board.board[i][self.col] == self.color:
                for ii in range(self.row + 1, i):
                    my_board.board[ii][self.col] = self.color
                break
            elif my_board.board[i][self.col] == my_board.blank:
                return
    """

    def flip_stone(self):
        # Hack: code not simple, modify code by using helper methods
        # down
        for i in range(self.row + 1, self.my_board.row):
            if self.my_board.board[i][self.col] == self.color:
                for ii in range(self.row + 1, i):
                    self.my_board.board[ii][self.col] = self.color
                break
            elif self.my_board.board[i][self.col] == self.my_board.blank:
                break
        # right
        for i in range(self.col + 1, self.my_board.col):
            if self.my_board.board[self.row][i] == self.color:
                for ii in range(self.col + 1, i):
                    self.my_board.board[self.row][ii] = self.color
                break
            elif self.my_board.board[self.row][i] == self.my_board.blank:
                break
        # up
        for i in range(self.row - 1, -1, -1):
            if self.my_board.board[i][self.col] == self.color:
                for ii in range(self.row - 1, i, -1):
                    self.my_board.board[ii][self.col] = self.color
                break
            elif self.my_board.board[i][self.col] == self.my_board.blank:
                break
        # left
        for i in range(self.col - 1, -1, -1):
            if self.my_board.board[self.row][i] == self.color:
                for ii in range(self.col - 1, i, -1):
                    self.my_board.board[self.row][ii] = self.color
                break
            elif self.my_board.board[self.row][i] == self.my_board.blank:
                break
        # left-upper
        limit = min(self.row, self.col)
        for i in range(1, limit + 1):
            if self.my_board.board[self.row - i][self.col - i] == self.color:
                for ii in range(1, i):
                    self.my_board.board[self.row - ii][self.col - ii] = self.color
                break
            elif self.my_board.board[self.row - 1][self.col - 1] == self.my_board.blank:
                break
        # right-lower
        limit = min(self.my_board.row - self.row, self.my_board.col - self.col)
        for i in range(1, limit):
            if self.my_board.board[self.row + i][self.col + i] == self.color:
                for ii in range(1, i):
                    self.my_board.board[self.row + ii][self.col + ii] = self.color
                break
            elif self.my_board.board[self.row + i][self.col + i] == self.my_board.blank:
                break
        # left-lower
        limit = min(self.my_board.row - self.row, self.col + 1)
        for i in range(1, limit):
            if self.my_board.board[self.row + i][self.col - i] == self.color:
                for ii in range(1, i):
                    self.my_board.board[self.row + ii][self.col - ii] = self.color
                break
            elif self.my_board.board[self.row + i][self.col - i] == self.my_board.blank:
                break
        # right-upper
        limit = min(self.row + 1, self.my_board.col - self.col)
        for i in range(1, limit):
            if self.my_board.board[self.row - i][self.col + i] == self.color:
                for ii in range(1, i):
                    self.my_board.board[self.row - ii][self.col + ii] = self.color
                break
            elif self.my_board.board[self.row - i][self.col + i] == self.my_board.blank:
                break
