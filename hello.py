import polars as pl
from pathlib import Path
import sys

def main():
    path_to_sql = sys.argv[1]
    context = pl.SQLContext()
    sql_text = Path(path_to_sql).read_text()
    print(sql_text)
    print("---")
    df = context.execute(sql_text)
    print(df.collect())

main()
