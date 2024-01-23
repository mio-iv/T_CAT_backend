import T_CAT.consts as consts

def create_message(input_message, add_message):
    """
    input_message, add_messageを、一つの文にする。
    例：
    input_message: 空は何で青いの？
    add_message: 幼児向けに易しく答えて

    input_message: いい加減にしてよ、めっちゃ迷惑！
    add_message:この文をオブラートに包んだ表現に変えて
    """
    return  f"{str(consts.MAX_TOKENS)}文字以内で" + add_message + "「" + input_message + "」"
