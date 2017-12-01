# coding=utf-8
from board import Board
from player import Player
from artificial_intelligence import ArtificialIntelligence

def main():
    my_board = Board(8, 8, "O")                     # "O" : open space
    my_player = Player("B", my_board)               # "B" : black
    my_ai = ArtificialIntelligence("W", my_board)   # "W" : white

    # set up board before starting
    my_board.create_board()
    my_board.set_board(4, 3, my_player.color)
    my_board.set_board(3, 4, my_player.color)
    my_board.set_board(3, 3, my_ai.color)
    my_board.set_board(4, 4, my_ai.color)

    while True:

        if my_board.possible_choice(my_player.color) > 0:
            my_board.print_board()
            my_player.select_point()  # wait for player's input
        else:
            if not my_board.possible_choice(my_ai.color) > 0:
                my_board.game_set(my_player.color, my_ai.color)

        if my_board.possible_choice(my_ai.color) > 0:
            my_board.print_board()
            my_ai.ai_calculate()
        else:
            if not my_board.possible_choice(my_player.color) > 0:
                my_board.game_set(my_player.color, my_ai.color)


if __name__ == '__main__':
    main()

"""
A game of Othello

change loop index to something more recognizable than 'i's or 'j's,
unless those iterator names are meant to indicate the function of "loops".
(use 'i' or 'j' if the code for the loop is short)

ネーミング：
    module_name, 
    package_name, 
    ClassName, 
    method_name, 
    ExceptionName, 
    function_name, 
    GLOBAL_CONSTANT_NAME, 
    global_var_name, 
    instance_var_name, 
    function_parameter_name, 
    local_var_name.

    その他の例：
    Google Opensource formatting
    class names             : CamelCase
    variable names          : lower_separated
    constant names          : kConstantName
    macro names             : MACRO_NAME
    class member variables  : offset_
    modules                 : snake_case (== lower_separated)
    method names            : snake_case (== lower separated)

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

[制御フローを読みやすくする]
ガード節：関数の上部で単純な条件を先に処理するもの
if/elseブロックの並び順について：
    ・条件は否定形よりも肯定形を使う。
        例えば、if(!debug)ではなく、if(debug)を使う。
    ・単純な条件を先に書く。
        ifとelseが同じ画面に表示されるので見やすい。
    ・関心を引く条件や目立つ条件を先に書く。
"""
