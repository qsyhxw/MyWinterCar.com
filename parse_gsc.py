import pandas as pd

# Read all sheets
xl = pd.ExcelFile('mywintercar.com-Performance-on-Search-2026-02-05.xlsx')
print("Available sheets:", xl.sheet_names)

# Read the queries sheet (index 1, named '查询数')
df_queries = pd.read_excel(xl, sheet_name='查询数')
print("\n=== QUERIES SHEET ===")
print("Columns:", df_queries.columns.tolist())
print("Total rows:", len(df_queries))

# Rename columns to English
df_queries.columns = ['query', 'clicks', 'impressions', 'ctr', 'position']

# Sort by impressions descending
df_queries = df_queries.sort_values('impressions', ascending=False)

# Save to CSV for easy reading
df_queries.to_csv('gsc_queries.csv', index=False)
print("\nSaved to gsc_queries.csv")

# Print top 100 queries
print("\n=== TOP 100 QUERIES BY IMPRESSIONS ===")
print(df_queries.head(100).to_string(index=False))

# Read pages sheet if available
if '网页' in xl.sheet_names:
    df_pages = pd.read_excel(xl, sheet_name='网页')
    print("\n\n=== PAGES SHEET ===")
    print("Columns:", df_pages.columns.tolist())
    df_pages.to_csv('gsc_pages.csv', index=False)
    print(df_pages.to_string(index=False))
