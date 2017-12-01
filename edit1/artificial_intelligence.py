# coding=utf-8
from player import Player


class ArtificialIntelligence(Player):
    def ai_calculate(self):
        # check the four-corners
        max_count = 0
        for i in range(2):  # （「ここはネストが深いので修正できる」＝＞検討中）
            for j in range(2):
                if self.my_board.board[i * (self.my_board.row - 1)][j * (self.my_board.col - 1)] == self.my_board.blank:  # noqa
                    count = self.my_board.count_up(i * (self.my_board.row - 1), j * (self.my_board.col - 1), self.color)  # noqa
                    if count > max_count:
                        max_count = count
                        self.row = i * (self.my_board.row - 1)
                        self.col = j * (self.my_board.col - 1)
        if max_count > 0:
            self.put_stone()
        else:
            # select to get highest return in that turn
            max_count = 0
            for i in range(self.my_board.row):
                for j in range(self.my_board.col):
                    if self.my_board.board[i][j] == self.my_board.blank:
                        count = self.my_board.count_up(i, j, self.color)
                        if count > max_count:
                            max_count = count
                            self.row = i
                            self.col = j
            if max_count > 0:
                self.put_stone()