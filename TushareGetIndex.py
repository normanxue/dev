import tushare as ts
import pandas as pd 

pro = ts.pro_api('7847c5bfbb1c51936a0670c6a9c93fd6b535f2650a39576a297a86ee')  

#提取沪深300指数2018年9月成分和权重
df = pro.index_weight(index_code='399300.SZ', start_date='20180901', end_date='20180930')
print(df.head(5))  