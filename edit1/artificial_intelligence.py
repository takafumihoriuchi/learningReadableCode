# coding=utf-8
from player import Player


class ArtificialIntelligence(Player):
    def ai_calculate(self):
        # check the four-corners
        max_count = 0
        interate_corner = 2
        for i in range(interate_corner):
            for j in range(interate_corner):
                row_length_idx = i * (self.my_board.row - 1)
                col_length_idx = j * (self.my_board.col - 1)
                if self.my_board.board[row_length_idx][col_length_idx] != self.my_board.blank:  # noqa
                    continue
                count = self.my_board.count_up(row_length_idx, col_length_idx, self.color)  # noqa
                if count > max_count:
                    max_count = count
                    self.row = row_length_idx
                    self.col = col_length_idx
        if max_count > 0:
            self.put_stone()
            return
        # select to get highest return in that turn
        max_count = 0
        for i in range(self.my_board.row):
            for j in range(self.my_board.col):
                if self.my_board.board[i][j] != self.my_board.blank:
                    continue
                count = self.my_board.count_up(i, j, self.color)
                if count > max_count:
                    max_count = count
                    self.row = i
                    self.col = j
        if max_count > 0:
            self.put_stone()
