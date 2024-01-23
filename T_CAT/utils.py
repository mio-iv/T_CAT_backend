def create_message(input_message, add_message):
    """
    input_message, add_messageを、一つの文にする。
    input_message: 明日の天気は？
    add_message: 小学生むけに答えて

    input_message: いい加減にしてよ、めっちゃ迷惑！
    add_message:この文をオブラートに包んだ表現に変えて
    """
    return add_message + "「" + input_message + "」"
