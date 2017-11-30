# coding=utf-8
import sys


class Board(object):
    board = []

    def __init__(self, row, col, blank):
        self.row   = row
        self.col   = col
        self.blank = blank

    def createBoard(self):
        for i in range(self.row):
            self.board.append([self.blank] * self.col)

    # used only in the set up process of the beginning of game
    # TODO: can be used thrugh out the game
    def setBoard(self, set_row, set_col, color):
        self.board[set_row][set_col] = color

    def printBoard(self):
        print ""
        for i in self.board:
            print("  ".join(i))
        print ""

    def possibleChoice(self, color):
        possibility = 0
        for ri in range(self.row):
            for ci in range(self.col):
                if self.board[ri][ci] == self.blank:
                    if self.countUp(ri, ci, color) > 0:
                        possibility += 1
        return possibility

    # print out results and end process
    def gameSet(self, player_color, ai_color):
        print("------------------")
        cnt_player = 0
        cnt_ai = 0
        for ri in range(self.row):
            for ci in range(self.col):
                if self.board[ri][ci] == player_color:
                    cnt_player += 1
                elif self.board[ri][ci] == ai_color:
                    cnt_ai += 1
        print("Player (Black): %d" % cnt_player)
        print("AI     (White): %d" % cnt_ai)
        if cnt_player > cnt_ai:
            print("Winner        : Player")
        elif cnt_player < cnt_ai:
            print("Winner        : AI")
        else:
            print("Draw")
        print("------------------")
        sys.exit()

    def countUp(self, row, col, color):
        count = 0
        # Hack: code not simple, modify code by using helper methods
        # down
        for i in range(row + 1, self.row):
            if self.board[i][col] == color:
                for ii in range(row + 1, i):
                    count += 1
                break
            elif self.board[i][col] == self.blank:
                break
        # right
        for i in range(col + 1, self.col):
            if self.board[row][i] == color:
                for ii in range(col + 1, i):
                    count += 1
                break
            elif self.board[row][i] == self.blank:
                break
        # up
        for i in range(row - 1, -1, -1):
            if self.board[i][col] == color:
                for ii in range(row-1, i, -1):
                    count += 1
                break
            elif self.board[i][col] == self.blank:
                break
        # left
        for i in range(col - 1, -1, -1):
            if self.board[row][i] == color:
                for ii in range(col - 1, i, -1):
                    count += 1
                break
            elif self.board[row][i] == self.blank:
                break
        # left-upper
        limit = min(row, col)
        for i in range(1, limit + 1):
            if self.board[row - i][col - i] == color:
                for ii in range(1, i):
                    count += 1
                break
            elif self.board[row - 1][col - 1] == self.blank:
                break
        # right-lower
        limit = min(self.row - row, self.col - col)
        for i in range(1, limit):
            if self.board[row + i][col + i] == color:
                for ii in range(1, i):
                    count += 1
                break
            elif self.board[row + i][col + i] == self.blank:
                break
        # left-lower
        limit = min(self.row - row, col + 1)
        for i in range(1, limit):
            if self.board[row + i][col - i] == color:
                for ii in range(1, i):
                    count += 1
                break
            elif self.board[row + i][col - i] == self.blank:
                break
        # right-upper
        limit = min(row + 1, self.col - col)
        for i in range(1, limit):
            if self.board[row - i][col + i] == color:
                for ii in range(1, i):
                    count += 1
                break
            elif self.board[row - i][col + i] == self.blank:
                break
        return count
