import re

#提取汉字
def get_chinese(s:str):
    """
    :param s: 提取的字符串
    :return: 返回提取结果列表
    """
    return re.findall('([\u4e00-\u9fa5]+)',s)

#提取字母
def get_letter(s:str):
    """
    :param s: 提取的字符串
    :return: 返回提取结果列表
    """
    return re.findall('([a-zA-Z]+)',s)

#提取大写字母
def get_Bletter(s:str):
    """
    :param s: 提取的字符串
    :return: 返回提取结果列表
    """
    return re.findall('([A-Z]+)',s)

#提取小写字母
def get_Sletter(s:str):
    """
    :param s: 提取的字符串
    :return: 返回提取结果列表
    """
    return re.findall('([a-z]+)',s)

#提取数字
def get_num(s:str):
    """
    :param s: 提取的字符串
    :return: 返回提取结果列表
    """
    return re.findall('([0-9]+)',s)

#提取数字或字母或数字和字母
def get_num_letter(s:str):
    """
    :param s: 提取的字符串
    :return: 返回提取结果列表
    """
    return re.findall('([0-9a-zA-Z]+)',s)

#自定义提取
def get_middle(s:str,front:str,after:str,contain=True):
    """
    :param front: 开头字符串
    :param after: 结尾字符串
    :param s: 查找字符串
    :param contain: 是否包含开头和末尾的字符串
    :return: 返回提取结果列表
    """
    if contain:
        return re.findall(f'({front}.*?{after})',s)
    else:
        return re.findall(f'{front}(.*?){after}',s)