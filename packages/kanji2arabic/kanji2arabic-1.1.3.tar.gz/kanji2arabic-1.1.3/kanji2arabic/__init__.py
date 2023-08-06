import kanjize

__kurai_list = "十,百,千,万,億,兆,京".split(",")
__kanji_arabic_dic = {"一": "1", "二": "2", "三": "3", "四": "4", "五": "5", "六": "6", "七": "7", "八": "8", "九": "9", "〇": "0"}
__arabic_kanji_dic = {"1": "一", "2": "二", "3": "三", "4": "四", "5": "五", "6": "六", "7": "七", "8": "八", "9": "九", "0": "〇"}


def __is_renban(txt: str) -> bool:
    """
    連番の漢数字か ex. 一二三: True, 百二十三: False

    Args:
        txt(str):変換する漢数字

    Returns:
        True:連番, False:漢数字
    """
    for kurai in __kurai_list:
        if kurai in txt:
            return False
    return True


def kanji2number_string(txt: str) -> str:
    """
    漢数字の文字列をアラビア数字のテキストに変換する

    Args:
        txt(str):漢数字文字列

    Returns:
        str:アラビア数字文字列

    """
    if __is_renban(txt):
        ret = ""
        for c in txt:
            ret += __kanji_arabic_dic[c]
        return ret
    else:
        return str(kanjize.kanji2number(txt))


def number2kanji_string(txt: str) -> str:
    """
    アラビア数字のテキストを漢字に変換する 例:123 -> 一二三

    Args:
        txt(str):アラビア数字文字列

    Returns:
        str:漢数字文字列

    """
    ret = ""
    for c in txt:
        ret += __arabic_kanji_dic[c]
    return ret

