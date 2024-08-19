# -*- coding: utf-8 -*-
"""Копия блокнота "Untitled0.ipynb"

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1MUGZHWmfujRzx8DtF8U_AaVv_t_lhvLE
"""

pip install pyspark

from pyspark.sql import SparkSession
from datetime import date
import pandas as pd
import random
spark = SparkSession.builder \
    .appName("example") \
    .getOrCreate()
data_cols = {'date':[],'userID':[], 'product':[], 'count': [], 'price': []}
product_list = ['Ручка','Карандаш','Линейка','Тетрадь','Блокнот']
start_date = date.today().replace(day=1, month=1).toordinal()
end_date = date.today().toordinal()
for i in range(0, 1000):
  data_cols['date'].append(date.fromordinal(random.randint(start_date, end_date)))
  data_cols['userID'].append(random.randint(0, 100))
  data_cols['product'].append(product_list[random.randint(0, len(product_list)-1)])
  data_cols['count'].append(random.randint(1, 100))
  data_cols['price'].append(random.randint(10, 2000))
data_frame = pd.DataFrame(data_cols)
cols = ['date', 'userID', 'product', 'count', 'price']
order_dframe = spark.createDataFrame(data_frame, schema=cols)
order_dframe.show()
order_dframe.write.csv('order.csv')