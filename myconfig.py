from configparser import ConfigParser   # Python2中是from ConfigParser import ConfigParser
conf = ConfigParser()  # 需要实例化一个ConfigParser对象
conf.read('config.ini')  # 需要添加上config.ini的路径，不需要open打开，直接给文件路径就读取，也可以指定encoding='utf-8'
api_token = conf['tushare']['api_token']  # 读取user段的name变量的值，字符串格式
# print(api_token)  # 打印出来看看是否读取成功
# ConfigParser doesn't actually need an explicit close() as it doesn't maintain any open file handles
# after read() completes its operation