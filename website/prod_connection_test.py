# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 11:19:50 2021

@author: GYu
"""


import pandas as pd
from sqlalchemy import create_engine   # pip install flask_sqlalchemy


url_1 = 'https://www.akleg.gov/basis/Bill/Range/32?session=&bill1=&bill2='
tables = pd.read_html(url_1,match="Bill", flavor='html5lib') 

print("There are : ",len(tables)," tables")
print("Take look at table 0")
# print(tables[0])

df_source = pd.DataFrame(tables[0])
df_source.to_excel(r'AL_bills_2021_source.xlsx')
#print(df_source)

url_2 = 'postgresql://gloria.yu:&|wIyn1I7Y5w@fn-atlantis-production.cjdtimdpf6hg.us-east-1.rds.amazonaws.com:5432/atlantis'
engine = create_engine(url_2, pool_size=50, echo=False)
engine.connect()

SQL_Query = pd.read_sql_query("select external_id from legislation.bills where locality = 'ak' and session = '20212022r'", engine)
df_prod = pd.DataFrame(SQL_Query)
# print(df_prod)
    

df_source.to_sql('AL_bills_2021_source', engine, if_exists='replace', index = False)
df_prod.to_sql('AL_bills_2021_prod', engine, if_exists='replace', index = False)

#result = engine.execute('SELECT count(*) FROM AL_bills_2021_source')
#for row in result:
#    print(row)
#result = engine.execute('SELECT * FROM AL_bills_2021_prod')
#result = engine.execute('select external_id, Bill from AL_bills_2021_source source join AL_bills_2021_prod prod on source.Bill = prod.external_id')
#result = engine.execute('select count(*) from AL_bills_2021_source source join AL_bills_2021_prod prod on source.Bill = prod.external_id')
# result = engine.execute('select external_id, Bill from AL_bills_2021_source source left join AL_bills_2021_prod prod on source.Bill = prod.external_id where external_id is null')

#for row in result:
#    print(row)

SQL_Query = pd.read_sql_query("select external_id, Bill from AL_bills_2021_source source left join AL_bills_2021_prod prod on source.Bill = prod.external_id where external_id is null", engine)

df_diff = pd.DataFrame(SQL_Query)
print(df_diff)

df_diff.to_excel(r'AL_bills_2021_diff.xlsx')