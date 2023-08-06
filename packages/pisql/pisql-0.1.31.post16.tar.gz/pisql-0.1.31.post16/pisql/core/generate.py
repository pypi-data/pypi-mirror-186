import re
import uuid
import pandas as pd
from .isql import iSQL, init_isql
from unidecode import unidecode as udc

isql = init_isql()

def get_columns_fmt(df, word_len=3):
    pattern = r"\%|\&|\*|\(|\)|\[|\]|\{|\}|\;|\:|\,|\.|\/|\<|\>|\?|\!|\||\`|\~|\-|\=|\_|\+| |\'"
    
    columns = []
    for col in df.columns:
        base = "_".join([ udc(word) for word in re.split(pattern, col) if len(word) >= 2 ]).upper()
        if len(base) > 30:
            stripcol = [ udc(word[:word_len]) for word in re.split(pattern, col) if len(word) >= 2 ]
            stripcol = '_'.join(stripcol).upper()
            if len(stripcol) > 30:
                stripcol = stripcol[:30]
            columns.append(stripcol)
        else:
            
            columns.append(base)
            
    return columns

def genInsertSql(df, table_name):
    columns = get_columns_fmt(df)
    drop = f"DROP TABLE {table_name} \nGO\n"
    create_table = f"CREATE TABLE {table_name} (" + ", ".join([ f"{col} VARCHAR(255)" for col in columns ]) + ") \nGO\n"
    left_sql_line = f"INSERT INTO {table_name} ("
    left_sql_line += ", ".join(columns)
    left_sql_line += ") VALUES ("
    right_sql_line = ")\n"
    records = df.to_records(index=False)
    sql = drop + create_table
    for record in records:
        sql += left_sql_line
        sql += ", ".join([ f"""'{udc(item).replace("'"," ")}'""" if isinstance(item, str) else f'"{item}"' for item in record ])
        sql += right_sql_line
    return sql

def execInsertSql(df, table_name):
    query = genInsertSql(df, 'MY_NEW_TABLE_NAME')
    file = "query-"+str(uuid.uuid4())+".sql"
    open(file, 'w+').write(query)
    isql.run_sql_file(file, preprocess=False)
    os.remove(file)