from rich.progress import track
import string
import random


def up_n_low(str: str):
    """
    字符串大小写全排列
    """
    res = [""]
    for i in track(str):
        if not i.isalpha():
            for j in range(len(res)):
                res[j] += i
        else:
            for k in range(len(res)):
                tmp = res[k]
                res[k] += i.lower()
                res.append(tmp + i.upper())
    return res


def random_string(length: int):
    """
    生成随机字符串
    字符集：大小写字母和数字
    注：5 位及以上的随机字符串很难重复
    """
    while 1:
        charset = string.ascii_letters + string.digits
        char_list = random.choices(charset, k=length)
        chars = ''.join(char_list)
        # 不能以数字开头
        if chars[0] not in string.digits:
            return chars


if __name__ == '__main__':
    count = 1
    l = []
    while 1:
        r = random_string(5)
        if r in l:
            print(count)
            break
        count += 1
        l.append(r)
