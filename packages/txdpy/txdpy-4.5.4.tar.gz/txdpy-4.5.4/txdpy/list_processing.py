def si(ls: list, s: str = None):
    """
    :param ls: 需要处理的列表
    :param s: 移除字符串头尾指定的字符（默认为空格或换行符）或字符序列
    :return: 移除元素某些字符的列表
    """
    if s:
        return [l.strip(s) for l in ls]
    return [l.strip() for l in ls]


def rl(ls: list, s1: str, s2: str):
    """
        :param ls: 需要处理的列表
        :param s1: 需要被替换的字符串
        :param s2: 替换完成的字符串
        :return: 替换元素字符后的列表
        """
    try:
        return [l.replace(s1, s2) for l in ls]
    except:
        return eval(str(ls).replace(s1,s2))


# 查找列表重复元素
def liduel(li: list):
    """
    :param li: 列表
    :return: 返回重复元素
    """
    tr_c = li
    tr_c = str(tr_c)
    tr_c = eval(tr_c)
    zwzf = '！已提取索引！'
    if zwzf in tr_c:
        zwzf = zwzf[::-1]
    dic = {}
    for td in tr_c:
        idx = tr_c.index(td)
        if td in dic:
            dic[td] = dic[td] + [idx]
        else:
            dic[td] = [idx]
        tr_c[idx] = zwzf
    repeat_es = []
    for key, value in dic.items():
        if len(value) > 1:
            repeat_es.append({'重复元素': key, '出现次数': len(value), '元素索引': value})

    return repeat_es

def list_dupl(list):
    """
    :param list:
    :return: 返回去重后的列表
    """
    new_list=[]
    for l in list:
        if l not in new_list:
            new_list.append(l)
    return new_list

