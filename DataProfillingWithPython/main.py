import pandas_profiling
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    'mssql+pyodbc://'
    '@./sakila?' # username:pwd@server:port/database
    'driver=ODBC+Driver+17+for+SQL+Server'
    )

df = pd.read_sql(
      'SELECT * FROM actor',
  engine)

print(df.head(10))

hourse_price_report=pandas_profiling.ProfileReport(df)

hourse_price_report.to_file('table_report.html')
