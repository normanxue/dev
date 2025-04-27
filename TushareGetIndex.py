import tushare as ts
import pandas as pd 
import myconfig # 读取配置文件
pro = ts.pro_api(myconfig.api_token)  
#提取沪深300指数2018年9月成分和权重
df = pro.index_weight(index_code='399300.SZ', start_date='20180901', end_date='20180930')
print(df.head(5))  