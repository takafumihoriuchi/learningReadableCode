# coding=utf-8
from Board import Board
from Player import Player
from ArtificialIntelligence import ArtificialIntelligence

my_board = Board(8, 8, "O")                     # "O" : open space
my_player = Player("B", my_board)               # "B" : black
my_ai = ArtificialIntelligence("W", my_board)   # "W" : white

# set up board before starting
my_board.createBoard()
my_board.setBoard(4, 3, my_player.color)
my_board.setBoard(3, 4, my_player.color)
my_board.setBoard(3, 3, my_ai.color)
my_board.setBoard(4, 4, my_ai.color)

while True:

    if my_board.possibleChoice(my_player.color) > 0:
        my_board.printBoard()
        my_player.selectPoint()  # wait for player's input
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
"""
