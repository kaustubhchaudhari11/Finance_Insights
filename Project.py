import pandas as pd



ferrari_financials = pd.read_excel(r"C:\Users\kaust\Desktop\Finance Project\venv\Ferrari Financials.xlsx")
mercedes_benz_financials = pd.read_excel(r"C:\Users\kaust\Desktop\Finance Project\venv\Mercedes Benz Financials.xlsx")
porsche_financials = pd.read_excel(r"C:\Users\kaust\Desktop\Finance Project\venv\Porsche Financials.xlsx")
volvo_financials = pd.read_excel(r"C:\Users\kaust\Desktop\Finance Project\venv\Volvo Financials.xlsx")




import pandas as pd

df = pd.read_excel(r"C:\Users\kaust\Desktop\Finance Project\venv\Ferrari Financials.xlsx")

df.set_index('Income Statement', inplace=True)

for col in df.columns:
    df[col] = pd.to_numeric(df[col].replace(',', ''), errors='coerce')

financial_ratios = {}

file_path = r'C:\Users\kaust\Desktop\Finance Project\venv\Ferrari Financials.xlsx'

df = pd.read_excel(file_path, header=1)

df.index.name = 'Financial Metric'

df.rename(columns={df.columns[0]: 'Financial Metric'}, inplace=True)
df.set_index('Financial Metric', inplace=True)

df.columns = df.columns.str.strip()

df = df.apply(pd.to_numeric, errors='coerce')

ratios = {}

for year in df.columns:
    total_revenue = df.at['Total Revenue', year]
    gross_profit = df.at['Gross Profit', year]
    operating_income = df.at['Operating Income', year]
    net_income = df.at['Net Income', year]
    
    # Calculate the ratios
    ratios[year] = {
        'Revenue Growth Rate %': None,  
        'Gross Profit Margin %': (gross_profit / total_revenue) * 100 if total_revenue else None,
        'Operating Profit Margin %': (operating_income / total_revenue) * 100 if total_revenue else None,
        'Net Profit Margin %': (net_income / total_revenue) * 100 if total_revenue else None,
    }


for i, year in enumerate(df.columns):
    if i > 0:  
        current_year_revenue = df.at['Total Revenue', year]
        previous_year = df.columns[i - 1]
        previous_year_revenue = df.at['Total Revenue', previous_year]
        
        if previous_year_revenue and not pd.isnull(previous_year_revenue):
            growth_rate = ((current_year_revenue - previous_year_revenue) / previous_year_revenue) * 100
            ratios[year]['Revenue Growth Rate %'] = growth_rate

ratios_df = pd.DataFrame.from_dict(ratios, orient='index')
# print("Printing The PROFIT RATIOS: \n",ratios_df)



#  Now Calculating the Balance sheet ratios ->
file_path = r"C:\Users\kaust\Desktop\Finance Project\venv\Ferrari Financials.xlsx"
sheet_name = 'Balance Sheet'


# Balance_sheet_df = pd.read_excel(file_path, sheet_name=sheet_name)
Balance_sheet_df = pd.read_excel(file_path, sheet_name=sheet_name, header=0)

# Balance_sheet_df.set_index('Balance Sheet', inplace=True)
Balance_sheet_df.set_index(Balance_sheet_df.columns[0], inplace=True)

# print(Balance_sheet_df)

for col in Balance_sheet_df.columns:
    # Using to_numeric with errors='coerce' will replace non-numeric values with NaN
    # Assuming that the first column after the index is the date header, we start conversion from the second column
    Balance_sheet_df[col] = pd.to_numeric(Balance_sheet_df[col].astype(str).str.replace(',', ''), errors='coerce')

# Print the dataframe to verify the result
print(Balance_sheet_df)
