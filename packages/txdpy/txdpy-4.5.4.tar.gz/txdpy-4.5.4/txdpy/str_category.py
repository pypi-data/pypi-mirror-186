import re

#判断是否为纯数字
def is_num(s:str):
    if re.search('^([0-9\.]+)$',s):
        return True
    return False

#判断是否为纯小写字母
def is_Sletter(s:str):
    if re.search('^([a-z]+)$',s):
        return True
    return False

#判断是否为纯大写字母
def is_Bletter(s:str):
    if re.search('^([A-Z]+)$',s):
        return True
    return False

#判断是否为纯字母
def is_letter(s:str):
    if re.search('^([a-zA-Z]+)$',s):
        return True
    return False

#判断是否为纯数字和字母
def is_num_letter(s:str):
    if re.search('^([0-9a-zA-Z]+)$',s):
        return True
    return False

#判断是否为纯汉字
def is_chinese(s:str):
    if re.search('^([\u4e00-\u9fa5]+)$',s):
        return True
    return False