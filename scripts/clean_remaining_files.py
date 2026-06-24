import pandas as pd

files = {
    "01_fund_master.csv": "clean_fund_master.csv",
    "03_aum_by_fund_house.csv": "clean_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv": "clean_monthly_sip_inflows.csv",
    "05_category_inflows.csv": "clean_category_inflows.csv",
    "06_industry_folio_count.csv": "clean_industry_folio_count.csv",
    "09_portfolio_holdings.csv": "clean_portfolio_holdings.csv",
    "10_benchmark_indices.csv": "clean_benchmark_indices.csv"
}

for raw_file, clean_file in files.items():

    print(f"Cleaning {raw_file}")

    df = pd.read_csv(f"data/raw/{raw_file}")

    # Remove duplicates
    df = df.drop_duplicates()

    # Remove completely empty rows
    df = df.dropna(how="all")

    # Remove extra spaces from text columns
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].astype(str).str.strip()

    df.to_csv(
        f"data/processed/{clean_file}",
        index=False
    )

    print(f"Saved -> {clean_file}")

print("All files cleaned successfully")