from datetime import datetime
import sqlite3



conn = sqlite3.connect('data.db')
c = conn.cursor()


def create_table():
  global name , coin , price # Retrieve global variable name
  c.execute('CREATE TABLE IF NOT EXISTS RecordONE (number REAL, Coin TEXT, price FLOAT)') # DB execution

def data_entry(co,pr):
  now = datetime.now()
  t_time = now.strftime("%H:%M:%S")
  c.execute("INSERT INTO RecordONE (number ,Coin ,price ) VALUES(?, ?, ?)", (t_time, co, pr))# Execute
  # Save changes to DB
  conn.commit()

# Close connection
#https://sqlite.org/cli.html
def dat_query():
  sql_result=c.execute("SELECT * FROM RecordONE ORDER BY ROWID ASC LIMIT 20")
  actual_result = sql_result.fetchall()
  print(actual_result)