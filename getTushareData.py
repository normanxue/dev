import tushare as ts
import pandas as pd 
pro = ts.pro_api('')  

df = pro.daily(ts_code='000001.SZ,600000.SH', start_date='20180701', end_date='20180718')
print(df.head(5))

print("行情获取成功")
data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
print(data.head(5))
print("股票获取成功")