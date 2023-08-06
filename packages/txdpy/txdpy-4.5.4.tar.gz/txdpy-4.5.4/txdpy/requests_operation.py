from lxml import etree
from .list_processing import si

def headers_dict(headers_raw):
    if headers_raw is None:
        return None
    headers_raw=headers_raw.strip()
    if headers_raw.startswith(':'):
        print('\033[1;33m提示：requests请求头中键名前的冒号需要删除，格式化headers中已删除！\033[0m')
    headers = headers_raw.splitlines()
    headers_tuples = [header.strip().lstrip(':').split(":", 1) for header in headers]

    result_dict = {}
    for header_item in headers_tuples:
        if not len(header_item) == 2:
            continue

        item_key = header_item[0].strip()
        item_value = header_item[1].strip()
        result_dict[item_key] = item_value

    return result_dict

def param_dict(param_raw):
    if param_raw is None:
        return None
    params = param_raw.splitlines()
    param_tuples = [param.strip().split(":", 1) for param in params]

    result_dict = {}
    for param_item in param_tuples:
        if not len(param_item) == 2:
            continue

        item_key = param_item[0].strip()
        item_value = param_item[1].strip()
        result_dict[item_key] = item_value

    return result_dict

def webptablesl(res,xpath,i=0):
    """
    :param res: url响应的html(例如response.text)
    :param xpath: 表格xpath(例如//table[1])
    :param i: 多个表格索引
    :return: 拆分后的表格数据，以列表返回
    """
    tree=etree.HTML(res)
    tables = tree.xpath(xpath)
    if tables:
        table = tables[i]
    else:
        return []
    trs = table.xpath('.//tr')

    #提取表格合并信息
    al=[]
    for tr in trs:
        l=[]
        tds=tr.xpath('./td|th')
        for td in tds:
            td_text=''.join(si(td.xpath('.//text()')))
            colspan=td.xpath('./@colspan')
            colspan =int(colspan[0]) if colspan else 1
            rowspan=td.xpath('./@rowspan')
            rowspan = int(rowspan[0]) if rowspan else 1
            l.append({td_text:(colspan,rowspan)})
        al.append(l)

    new_al=[]
    for n in range(len(al)):
        new_al.append([])

    #处理横向合并
    a=0
    for l in al:
        new_l=new_al[a]
        i=0
        for d in l:
            for key, value in d.items():
                for c in range(value[0]):
                    new_l.insert(i,key)
                    i+=1
            i+=1
        new_al.pop(a)
        new_al.insert(a,new_l)
        a+=1

    #处理纵向合并
    a=0
    for l in al:
        for d in l:
            for key, value in d.items():
                if value[1]>1:
                    for r in range(1,value[1]):
                        i = new_al[a + r - 1].index(key)
                        new_l=new_al[a+r]
                        new_l.insert(i, key)
                        new_al.pop(a+r)
                        new_al.insert(a+r, new_l)
        a+=1
        
    return new_al