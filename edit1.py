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

    # print out results
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
        # Hack: あまりキレイじゃない解決策。簡潔にまとめたい。
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


class Player(object):
    def __init__(self, color, my_board):
        self.color    = color
        self.my_board = my_board

    def selectPoint(self):
        self.row = int(input("row: "))
        self.col = int(input("col: "))
        self.putStone()

    def putStone(self):
        if self.row not in range(self.my_board.row)\
         or self.col not in range(self.my_board.col):
            print("invalid input (out of range)")
            self.selectPoint()
        elif self.my_board.board[self.row][self.col] == my_board.blank:
            if my_board.countUp(self.row, self.col, self.color) > 0:
                self.my_board.board[self.row][self.col] = self.color
            else:
                print("invalid input (unflippable)")
                self.selectPoint()
        else:
            print("invalid input (already taken)")
            self.selectPoint()
        self.flipStone()

    """
    # TODO: あとで手をつける
    # ヘルパーメソッドを使用して、助長な繰り返しを避ける。
    def flipStoneHelper(self, out_range_s, out_range_e, ...):
        for i in range(self.row + 1, my_board.row):
            if my_board.board[i][self.col] == self.color:
                for ii in range(self.row + 1, i):
                    my_board.board[ii][self.col] = self.color
                break
            elif my_board.board[i][self.col] == my_board.blank:
                return
    """

    def flipStone(self):
        # Hack: あまりキレイじゃない解決策。簡潔にまとめたい。
        # down
        for i in range(self.row + 1, my_board.row):
            if my_board.board[i][self.col] == self.color:
                for ii in range(self.row + 1, i):
                    my_board.board[ii][self.col] = self.color
                break
            elif my_board.board[i][self.col] == my_board.blank:
                break
        # right
        for i in range(self.col + 1, my_board.col):
            if my_board.board[self.row][i] == self.color:
                for ii in range(self.col + 1, i):
                    my_board.board[self.row][ii] = self.color
                break
            elif my_board.board[self.row][i] == my_board.blank:
                break
        # up
        for i in range(self.row - 1, -1, -1):
            if my_board.board[i][self.col] == self.color:
                for ii in range(self.row - 1, i, -1):
                    my_board.board[ii][self.col] = self.color
                break
            elif my_board.board[i][self.col] == my_board.blank:
                break
        # left
        for i in range(self.col - 1, -1, -1):
            if my_board.board[self.row][i] == self.color:
                for ii in range(self.col - 1, i, -1):
                    my_board.board[self.row][ii] = self.color
                break
            elif my_board.board[self.row][i] == my_board.blank:
                break
        # left-upper
        limit = min(self.row, self.col)
        for i in range(1, limit + 1):
            if my_board.board[self.row - i][self.col - i] == self.color:
                for ii in range(1, i):
                    my_board.board[self.row - ii][self.col - ii] = self.color
                break
            elif my_board.board[self.row - 1][self.col - 1] == my_board.blank:
                break
        # right-lower
        limit = min(my_board.row - self.row, my_board.col - self.col)
        for i in range(1, limit):
            if my_board.board[self.row + i][self.col + i] == self.color:
                for ii in range(1, i):
                    my_board.board[self.row + ii][self.col + ii] = self.color
                break
            elif my_board.board[self.row + i][self.col + i] == my_board.blank:
                break
        # left-lower
        limit = min(my_board.row - self.row, self.col + 1)
        for i in range(1, limit):
            if my_board.board[self.row + i][self.col - i] == self.color:
                for ii in range(1, i):
                    my_board.board[self.row + ii][self.col - ii] = self.color
                break
            elif my_board.board[self.row + i][self.col - i] == my_board.blank:
                break
        # right-upper
        limit = min(self.row + 1, my_board.col - self.col)
        for i in range(1, limit):
            if my_board.board[self.row - i][self.col + i] == self.color:
                for ii in range(1, i):
                    my_board.board[self.row - ii][self.col + ii] = self.color
                break
            elif my_board.board[self.row - i][self.col + i] == my_board.blank:
                break


class ArtificialIntelligence(Player):
    def aiCalculate(self):
        # check the four-corners
        max_count = 0
        for i in range(2):
            for j in range(2):
                if my_board.board[i * (my_board.row - 1)][j * (my_board.col - 1)] == my_board.blank:  # noqa
                    count = my_board.countUp(i * (my_board.row - 1), j * (my_board.col - 1), self.color)  # noqa
                    if count > max_count:
                        max_count = count
                        self.row = i * (my_board.row - 1)
                        self.col = j * (my_board.col - 1)
        if max_count > 0:
            self.putStone()
        else:
            # select point to get highest return in that turn
            max_count = 0
            for i in range(my_board.row):
                for j in range(my_board.col):
                    if my_board.board[i][j] == my_board.blank:
                        count = my_board.countUp(i, j, self.color)
                        if count > max_count:
                            max_count = count
                            self.row  = i
                            self.col  = j
            if max_count > 0:
                self.putStone()


my_board = Board(8, 8, "O")                     # "O" : open space
my_player = Player("B", my_board)               # "B" : black
my_ai = ArtificialIntelligence("W", my_board)   # "W" : white

# オセロ盤の初期設定
my_board.createBoard()
my_board.setBoard(4, 3, my_player.color)
my_board.setBoard(3, 4, my_player.color)
my_board.setBoard(3, 3, my_ai.color)
my_board.setBoard(4, 4, my_ai.color)

while True:

    if my_board.possibleChoice(my_player.color) > 0:
        my_board.printBoard()
        my_player.selectPoint()                 # ここでプレイヤーの入力を待つ
    else:
        if not my_board.possibleChoice(my_ai.color) > 0:
            my_board.gameSet(my_player.color, my_ai.color)

    if my_board.possibleChoice(my_ai.color) > 0:
        my_board.printBoard()
        my_ai.aiCalculate()
    else:
        if not my_board.possibleChoice(my_player.color) > 0:
            my_board.gameSet(my_player.color, my_ai.color)


"""
A game of Othello

change loop index to something more recognizable than 'i's or 'j's,
unless those iterator names are meant to indicate the function of loops.
(use 'i' or 'j' if the code for the loop is short)

Google Opensource formatting
class names             : CamelCase
variable names          : lower_separated
constant names          : kConstantName
macro names             : MACRO_NAME
class member variables  : offset_

JavaScript: The Good Parts by Douglas Crockford
Constructor : DatePicker()
functions   : pageHeight()

コードを美しくする
- 繰り返しを避ける => ヘルパーメソッドを追加する
- 縦整列を整えるために、空白を入れて調整する

コメント
・コメントするべきでは「ない」こと：
    コードからすぐに抽出できること
    ひどいコードを補う形の「補助的な」コメント。このようなときはコードを修正する。
・記録するべき自分の考え：
    DVDでいう「監督コメンタリー」のように、なぜこのようなコードになったのか
    コードの欠陥をTODO:やXXX:などの記法を使って示す
    定数の値にまつわる「背景」
・読み手の立場で考える：
    読み手の常識からかけ離れていることに関するコメント
    ファイルやクラスの全体像を示す

"