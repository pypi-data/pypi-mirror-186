from .pytmysql import PyMySQL
import xlrd

def excel_into_mysql(file:str,host:str, password:str, database:str,bm:str,th_a=1,stat:int=0,port:int=3306, user:str='root',auto_add_key:bool=True):
    """
    :param file: 文件路径
    :param host: mysql地址
    :param password: mysql密码
    :param database: mysql数据库名称
    :param bm: 数据库表名称
    :param th_a: 插入数据表表头，可传入excel对应行或列表
    :param stat: 插入数据库数据行，有默认规则，可自定义
    :param port: mysql端口号
    :param user: mysql用户名
    :param auto_add_key: 是否自动添加表头字段
    :return:
    """
    data = xlrd.open_workbook(file)
    table = data.sheets()[0]  #通过工作表索引顺序获取
    nrows = table.nrows #有效行数
    ncols = table.ncols #有效列数
    data=[]
    for r in range(nrows):
        l=[]
        for c in range(ncols):
            l.append(table.cell_value(r, c))
        data.append(l)
    mysql = PyMySQL(host=host,port=3306, user='root', password=password, database=database,auto_add_key=auto_add_key)
    th=[]
    if type(th_a) is int:
        th=data[th_a-1]
        stat=th_a
    elif type(th) is list:
        th = th_a
    for v in data[stat:]:
        mysql.insert_into(bm,th,v)
    mysql.close()