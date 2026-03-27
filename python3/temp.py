# -*- coding: utf-8 -*-
# @Time    : 2023/3/18 14:25
# @Author  : Monarch
# @File    : temp.py
# @Software: PyChar

import os
import pandas as pd
from sqlalchemy import create_engine


os.chdir(r'D:\Study_tool\Tomcat\webapps\anyi\api\jsonData')


df = pd.read_json('anyi_yqjy.json')


host = "127.0.0.1"
pwd = "123456"
port = 3306
sql_name = "root"
database = "anyiVR"
conn = create_engine(f'mysql+pymysql://{sql_name}:{pwd}@{host}:{port}/{database}')

df.to_sql('park_rt', conn, if_exists='replace', index=False)
