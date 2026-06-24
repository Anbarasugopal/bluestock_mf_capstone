from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("sqlite:///bluestock_mf.db")

for table in [
    "dim_fund",
    "fact_nav",
    "fact_transactions",
    "fact_performance"
]:
    count = pd.read_sql(
        f"SELECT COUNT(*) as cnt FROM {table}",
        engine
    )

    print(table)
    print(count)