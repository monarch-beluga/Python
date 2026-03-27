# -*- coding: utf-8 -*-
# @Time    : 2026/2/7 下午3:30
# @Author  : Monarch
# @File    : 应急空间数据导入数据库.py
# @Software: PyCharm


import os
import pandas as pd
from sqlalchemy import create_engine
import numpy as np

os.chdir(r'D:\Study_tool\Tomcat\webapps\anyi\api\jsonData')

host = "127.0.0.1"
pwd = "123456"
port = 3306
sql_name = "root"
database = "anyiVR"
# conn = pymysql.connect(host=host, password=pwd, port=port, user=sql_name, db=database)
conn = create_engine(f'mysql+pymysql://{sql_name}:{pwd}@{host}:{port}/{database}')

df = pd.read_json('anyi_yjkj.json')

df.rename(columns={'type': 'type_num', '类型': 'type', '备注': 'remark'}, inplace=True)
df.drop('范围数据（管道等提供）', axis=1, inplace=True)
df.drop('speed', axis=1, inplace=True)

mask = df['id'].isna()
start_value = df['id'].max() if df['id'].notna().any() else 0
df.loc[mask, 'id'] = np.arange(start_value + 1, start_value + 1 + mask.sum())

df['id'] = df['id'].astype(int)
df['type_num'] = df['type_num'].astype(int)

df.to_sql('space', conn, if_exists='replace', index=False)



