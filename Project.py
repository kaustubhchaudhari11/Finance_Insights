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
print("Printing The PROFIT RATIOS: \n",ratios_df)



file_path = r"C:\Users\kaust\Desktop\Finance Project\venv\Ferrari Financials.xlsx"
sheet_name = 'Balance Sheet'


Balance_sheet_df = pd.read_excel(file_path, sheet_name=sheet_name, header=1)

Balance_sheet_df.set_index(Balance_sheet_df.columns[0], inplace=True)

for col in Balance_sheet_df.columns:
    Balance_sheet_df[col] = pd.to_numeric(Balance_sheet_df[col].astype(str).str.replace(',', ''), errors='coerce')

# Calculate the ratios
current_ratio = Balance_sheet_df.loc['Current Assets'] / Balance_sheet_df.loc['Current Liabilities']
quick_ratio = (Balance_sheet_df.loc['Cash And Cash Equivalents'] + 
               Balance_sheet_df.loc['Other Short Term Investments'] + 
               Balance_sheet_df.loc['Receivables']) / Balance_sheet_df.loc['Current Liabilities']
debt_to_equity_ratio = Balance_sheet_df.loc['Total Liabilities Net Minority Interest'] / Balance_sheet_df.loc['Stockholders\' Equity']

# Create a new DataFrame for ratios with the correct column names from the balance sheet
ratios_df = pd.DataFrame({
    'Current Ratio': current_ratio,
    'Quick Ratio': quick_ratio,
    'Debt-to-Equity Ratio': debt_to_equity_ratio
}, index=Balance_sheet_df.columns)

ratios_df = ratios_df.T

print(ratios_df)




# Now we will calculating other ratios ->
file_path = r"C:\Users\kaust\Desktop\Finance Project\venv\Ferrari Financials.xlsx"
cash_flow_sheet = 'Cash Flow'
balance_sheet = 'Balance Sheet'

# Reading the Cash Flow sheet
cash_flow_df = pd.read_excel(file_path, sheet_name=cash_flow_sheet, header=1)
cash_flow_df.set_index(cash_flow_df.columns[0], inplace=True)
for col in cash_flow_df.columns:
    cash_flow_df[col] = pd.to_numeric(cash_flow_df[col].astype(str).str.replace(',', ''), errors='coerce')

# Reading the Balance Sheet
balance_sheet_df = pd.read_excel(file_path, sheet_name=balance_sheet, header=1)
balance_sheet_df.set_index(balance_sheet_df.columns[0], inplace=True)
for col in balance_sheet_df.columns:
    balance_sheet_df[col] = pd.to_numeric(balance_sheet_df[col].astype(str).str.replace(',', ''), errors='coerce')

# Dates for the last four years
years = ['12/30/2023', '12/30/2022', '12/30/2021', '12/30/2020']

# Initialize a dictionary to store the ratios
ratios = {'Year': [], 'Operating Cash Flow Ratio': [], 'Free Cash Flow': []}

# Calculate the ratios for each year
for year in years:
    current_liabilities = balance_sheet_df.loc['Current Liabilities', year]
    operating_cash_flow = cash_flow_df.loc['Operating Cash Flow', year]
    capital_expenditure = cash_flow_df.loc['Capital Expenditure', year]
    operating_cash_flow_ratio = operating_cash_flow / current_liabilities
    free_cash_flow = operating_cash_flow + capital_expenditure

    # Store the results
    ratios['Year'].append(year)
    ratios['Operating Cash Flow Ratio'].append(operating_cash_flow_ratio)
    ratios['Free Cash Flow'].append(free_cash_flow)

# Convert the results dictionary to a DataFrame for better visualization
ratios_df = pd.DataFrame(ratios)

print(ratios_df)