# -*- coding: utf-8 -*-
# @Time    : 2026/2/7 下午3:59
# @Author  : Monarch
# @File    : 情景模拟数据导入数据库.py
# @Software: PyCharm

import os
import json
import pandas as pd
from sqlalchemy import create_engine, types
import numpy as np

os.chdir(r'D:\Study_tool\Tomcat\webapps\anyi\api\jsonData')


df = pd.read_json('anyi_qjmn4.json')
df['flyPosition'] = df['flyPosition'].apply(json.dumps)
df['features'] = df['features'].apply(json.dumps)
df['type'] = '4'

host = "127.0.0.1"
pwd = "123456"
port = 3306
sql_name = "root"
database = "anyiVR"
conn = create_engine(f'mysql+pymysql://{sql_name}:{pwd}@{host}:{port}/{database}')

object_type = types.JSON
# Scenario simulation
df.to_sql('scenario', conn,
          if_exists='append',
          index=False,
          dtype={
              'flyPosition': object_type,
              'features': object_type,
              'content': types.Text
          })




