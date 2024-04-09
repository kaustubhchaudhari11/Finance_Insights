import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression


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

Profit_ferrari_ratios_df = pd.DataFrame.from_dict(ratios, orient='index')
print("Printing The PROFIT RATIOS: \n",Profit_ferrari_ratios_df)



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

Ferrari_Liquidity_ratios_df = ratios_df.T

print(Ferrari_Liquidity_ratios_df)




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
    capital_expenditure = cash_flow_df.loc['Capital Expenditure', year]
    operating_cash_flow = cash_flow_df.loc['Operating Cash Flow', year]
    operating_cash_flow_ratio = operating_cash_flow / current_liabilities
    free_cash_flow = operating_cash_flow + capital_expenditure

    # Store the results
    ratios['Year'].append(year)
    ratios['Operating Cash Flow Ratio'].append(operating_cash_flow_ratio)
    ratios['Free Cash Flow'].append(free_cash_flow)

# Convert the results dictionary to a DataFrame for better visualization
Ferrari_cash_flow_ratios_df = pd.DataFrame(ratios)
print(Ferrari_cash_flow_ratios_df)





# New ratios for Mercedes Financials ->
file_path = r'C:\Users\kaust\Desktop\Finance Project\venv\Mercedes Benz Financials.xlsx'

# Load the Excel file
df = pd.read_excel(file_path, header=1)

# Set the first column as the index for financial metrics
df.rename(columns={df.columns[0]: 'Financial Metric'}, inplace=True)
df.set_index('Financial Metric', inplace=True)

# Clean the column names and convert the data to numeric, ignoring non-numeric values
df.columns = df.columns.str.strip()
df = df.apply(pd.to_numeric, errors='coerce')

# Dictionary to hold the financial ratios
ratios = {}

# Loop through each year (column) to calculate the base ratios
for year in df.columns:
    total_revenue = df.at['Total Revenue', year]
    gross_profit = df.at['Gross Profit', year]
    operating_income = df.at['Operating Income', year]
    net_income = df.at['Net Income', year]
    
    # Calculate and store the financial ratios
    ratios[year] = {
        'Revenue Growth Rate %': None,  # Placeholder, to be calculated in the next step
        'Gross Profit Margin %': (gross_profit / total_revenue) * 100 if total_revenue else None,
        'Operating Profit Margin %': (operating_income / total_revenue) * 100 if total_revenue else None,
        'Net Profit Margin %': (net_income / total_revenue) * 100 if total_revenue else None,
    }

# Calculate the Revenue Growth Rate % for each year, starting from the second one
for i, year in enumerate(df.columns[1:], start=1):  # Start from the second column
    current_year_revenue = df.at['Total Revenue', year]
    previous_year = df.columns[i - 1]  # Correctly gets the previous year
    previous_year_revenue = df.at['Total Revenue', previous_year]
    
    # Ensure there's previous year revenue to calculate the growth rate
    if previous_year_revenue and not pd.isnull(previous_year_revenue):
        growth_rate = ((current_year_revenue - previous_year_revenue) / previous_year_revenue) * 100
        ratios[year]['Revenue Growth Rate %'] = growth_rate

# Convert the ratios dictionary to a DataFrame for display
Mercedes_profit_ratios_df = pd.DataFrame.from_dict(ratios, orient='index')

# Print the calculated financial ratios for Mercedes-Benz
print("Printing The PROFIT RATIOS for Mercedes-Benz: \n", Mercedes_profit_ratios_df)


#Now RATIO For MERCEDES BALANCE SHEET

file_path = r"C:\Users\kaust\Desktop\Finance Project\venv\Mercedes Benz Financials.xlsx"
sheet_name = 'Balance Sheet'  # Adjust the sheet name if necessary

# Load the balance sheet data from the Excel file
balance_sheet_df = pd.read_excel(file_path, sheet_name=sheet_name, header=1)

# Set the first column as the index
balance_sheet_df.set_index(balance_sheet_df.columns[0], inplace=True)

# Clean and convert all columns to numeric, removing commas
for col in balance_sheet_df.columns:
    balance_sheet_df[col] = pd.to_numeric(balance_sheet_df[col].astype(str).str.replace(',', ''), errors='coerce')

# Calculate the balance sheet ratios
current_ratio = balance_sheet_df.loc['Current Assets'] / balance_sheet_df.loc['Current Liabilities']
quick_ratio = (balance_sheet_df.loc['Cash And Cash Equivalents'] + 
               balance_sheet_df.loc['Other Short Term Investments']) / balance_sheet_df.loc['Current Liabilities']
debt_to_equity_ratio = balance_sheet_df.loc['Total Liabilities Net Minority Interest'] / balance_sheet_df.loc['Stockholders\' Equity']

# Create a new DataFrame for the calculated ratios
ratios_df = pd.DataFrame({
    'Current Ratio': current_ratio,
    'Quick Ratio': quick_ratio,
    'Debt-to-Equity Ratio': debt_to_equity_ratio
}, index=balance_sheet_df.columns)

# Transpose the DataFrame for better readability
Mercedes_liquidity_ratios_df = ratios_df.T
print(Mercedes_liquidity_ratios_df)


file_path = r'C:\Users\kaust\Desktop\Finance Project\venv\Mercedes Benz Financials.xlsx'

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
    capital_expenditure = cash_flow_df.loc['Capital Expenditure', year]
    operating_cash_flow = cash_flow_df.loc['Operating Cash Flow', year]
    operating_cash_flow_ratio = operating_cash_flow / current_liabilities
    free_cash_flow = operating_cash_flow + capital_expenditure

    # Store the results
    ratios['Year'].append(year)
    ratios['Operating Cash Flow Ratio'].append(operating_cash_flow_ratio)
    ratios['Free Cash Flow'].append(free_cash_flow)

# Convert the results dictionary to a DataFrame for better visualization
Mercedes_Cash_flow_ratios_df = pd.DataFrame(ratios)

print(Mercedes_Cash_flow_ratios_df)
#-----Mercedes-DONE











porsche_file_path = 'C:\\Users\\kaust\\Desktop\\Finance Project\\venv\\Porsche Financials.xlsx'
sheet_name = 'Income Statement'  # This might be different for Porsche

# Load the data
df = pd.read_excel(porsche_file_path, sheet_name=sheet_name, header=1)

# Set the first column as the index for financial metrics
df.rename(columns={df.columns[0]: 'Financial Metric'}, inplace=True)
df.set_index('Financial Metric', inplace=True)

# Clean the column names and convert the data to numeric, ignoring non-numeric values
df.columns = df.columns.str.strip()
df = df.apply(pd.to_numeric, errors='coerce')


# Calculate the ratios for Porsche Profit Ratios ->
ratios = {}

for year in df.columns:
    total_revenue = df.at['Total Revenue', year]
    gross_profit = df.at['Gross Profit', year]
    operating_income = df.at['Operating Income', year]
    net_income = df.at['Net Income', year]
    
    # Calculate the ratios
    ratios[year] = {
        'Revenue Growth Rate %': None,  # Placeholder, to be calculated in the next step
        'Gross Profit Margin %': (gross_profit / total_revenue) * 100 if total_revenue else None,
        'Operating Profit Margin %': (operating_income / total_revenue) * 100 if total_revenue else None,
        'Net Profit Margin %': (net_income / total_revenue) * 100 if total_revenue else None,
    }

# Calculate the Revenue Growth Rate % for each year, starting from the second one
for i, year in enumerate(df.columns[1:], start=1):  # Start from the second column
    current_year_revenue = df.at['Total Revenue', year]
    previous_year = df.columns[i - 1]
    previous_year_revenue = df.at['Total Revenue', previous_year]
    
    if previous_year_revenue and not pd.isnull(previous_year_revenue):
        growth_rate = ((current_year_revenue - previous_year_revenue) / previous_year_revenue) * 100
        ratios[year]['Revenue Growth Rate %'] = growth_rate

# Convert the ratios dictionary to a DataFrame for display
Porche_Profit_ratios_df = pd.DataFrame.from_dict(ratios, orient='index')
print("PROFT PORSCHE RATIO",Porche_Profit_ratios_df)



file_path = r"C:\Users\kaust\Desktop\Finance Project\venv\Porsche Financials.xlsx"
sheet_name = 'Balance Sheet'  # Ensure this matches the sheet name in your file

# Load the balance sheet data
balance_sheet_df = pd.read_excel(file_path, sheet_name=sheet_name, header=1)

# Set the first column as the index
balance_sheet_df.set_index(balance_sheet_df.columns[0], inplace=True)

# Convert all columns to numeric, handling commas and non-numeric values
for col in balance_sheet_df.columns:
    balance_sheet_df[col] = pd.to_numeric(balance_sheet_df[col].astype(str).str.replace(',', ''), errors='coerce')

current_ratio = balance_sheet_df.loc['Current Assets'] / balance_sheet_df.loc['Current Liabilities']
quick_ratio = (balance_sheet_df.loc['Cash And Cash Equivalents'] + 
               balance_sheet_df.loc['Other Short Term Investments']) / balance_sheet_df.loc['Current Liabilities']
debt_to_equity_ratio = balance_sheet_df.loc['Total Liabilities Net Minority Interest'] / balance_sheet_df.loc['Stockholders\' Equity']

# Create a DataFrame for the calculated ratios
ratios_df = pd.DataFrame({
    'Current Ratio': current_ratio,
    'Quick Ratio': quick_ratio,
    'Debt-to-Equity Ratio': debt_to_equity_ratio
}, index=balance_sheet_df.columns)

# Transpose the DataFrame for better readability
Porche_Liquidity_ratios_df = ratios_df.T
print("PORSCHE LIQUIDITY RATIO",Porche_Liquidity_ratios_df)




file_path = r'C:\Users\kaust\Desktop\Finance Project\venv\Porsche Financials.xlsx'

# Define sheet names
cash_flow_sheet = 'Cash Flow'
balance_sheet = 'Balance Sheet'

# Reading the Cash Flow sheet from the Porsche Financials
cash_flow_df = pd.read_excel(file_path, sheet_name=cash_flow_sheet, header=1)
cash_flow_df.set_index(cash_flow_df.columns[0], inplace=True)
for col in cash_flow_df.columns:
    cash_flow_df[col] = pd.to_numeric(cash_flow_df[col].astype(str).str.replace(',', ''), errors='coerce')

# Reading the Balance Sheet from the Porsche Financials
balance_sheet_df = pd.read_excel(file_path, sheet_name=balance_sheet, header=1)
balance_sheet_df.set_index(balance_sheet_df.columns[0], inplace=True)
for col in balance_sheet_df.columns:
    balance_sheet_df[col] = pd.to_numeric(balance_sheet_df[col].astype(str).str.replace(',', ''), errors='coerce')

# Define the dates for the last four years
years = ['12/30/2023', '12/30/2022', '12/30/2021', '12/30/2020']

# Initialize a dictionary to store the calculated ratios
ratios = {'Year': [], 'Operating Cash Flow Ratio': [], 'Free Cash Flow': []}

# Fill NaN values in the cash flow DataFrame with 0
cash_flow_df.fillna(0, inplace=True)

# Calculate the ratios for each of the specified years
for year in years:
    current_liabilities = balance_sheet_df.loc['Current Liabilities', year]
    capital_expenditure = cash_flow_df.loc['Capital Expenditure', year]
    operating_cash_flow = cash_flow_df.loc['Operating Cash Flow', year]
    
    # Calculate the operating cash flow ratio
    operating_cash_flow_ratio = operating_cash_flow / current_liabilities if current_liabilities else None
    
    # Calculate the free cash flow
    free_cash_flow = operating_cash_flow + capital_expenditure if capital_expenditure or operating_cash_flow else None

    # Store the results for each year
    ratios['Year'].append(year)
    ratios['Operating Cash Flow Ratio'].append(operating_cash_flow_ratio)
    ratios['Free Cash Flow'].append(free_cash_flow)

# Convert the ratios dictionary into a DataFrame for visualization
Porsche_Cash_flow_ratios_df = pd.DataFrame(ratios)

# Print the calculated cash flow ratios for Porsche
print("Porsche Cash Flow Ratios:\n", Porsche_Cash_flow_ratios_df)



all_ratios_df = pd.concat([Profit_ferrari_ratios_df,Ferrari_Liquidity_ratios_df,Ferrari_cash_flow_ratios_df ,Mercedes_profit_ratios_df,Mercedes_liquidity_ratios_df,Mercedes_Cash_flow_ratios_df,Porche_Profit_ratios_df,Porche_Liquidity_ratios_df,Porsche_Cash_flow_ratios_df], axis=1)
print(all_ratios_df)

#---------------------------------------------------------------
ferrari_data = {
    "Date": ["12/30/2023", "12/30/2022", "12/30/2021", "12/30/2020"],
    "Revenue Growth Rate %": [None, -14.654449, -16.178978, -18.991434],
    "Gross Profit Margin %": [49.819033, 48.011365, 51.283900, 51.259354],
    "Operating Profit Margin %": [26.988151, 23.967539, 25.020335, 21.098246],
    "Net Profit Margin %": [20.971815, 18.303582, 19.451829, 17.568032],
    "Current Ratio": [3.558503, 3.728553, 3.392456, 3.891109],
    "Quick Ratio": [2.604355, 2.947262, 2.774133, 3.202797],
    "Debt-to-Equity Ratio": [1.627204, 1.991369, 2.108932, 2.505533],
    "Operating Cash Flow Ratio": [1.532526, 1.323823, 1.293685, 1.060369],
    "Free Cash Flow": [847727.0, 598721.0, 545583.0, 129215.0]
}

# Mercedes's financial data
mercedes_data = {
    "Date": ["12/30/2023", "12/30/2022", "12/30/2021", "12/30/2020"],
    "Revenue Growth Rate %": [None, -2.089180, -10.748115, -9.048270],
    "Gross Profit Margin %": [22.437964, 22.677430, 22.910085, 16.576065],
    "Operating Profit Margin %": [11.435993, 11.921316, 11.185051, 4.673258],
    "Net Profit Margin %": [9.307653, 9.666238, 17.182377, 2.978370],
    "Current Ratio": [1.262004, 1.163694, 1.173983, 1.154846],
    "Quick Ratio": [0.271162, 0.275534, 0.340622, 0.285054],
    "Debt-to-Equity Ratio": [1.854641, 2.030966, 2.594321, 3.682408],
    "Operating Cash Flow Ratio": [0.175534, 0.191102, 0.280000, 0.223747],
    "Free Cash Flow": [6257000.0, 9995000.0, 17229000.0, 13772000.0]
}

# Porsche's financial data
porsche_data = {
    "Date": ["12/30/2023", "12/30/2022", "12/30/2021", "12/30/2020"],
    "Revenue Growth Rate %": [None, -0.128511, -14.871324, -42.949687],
    "Gross Profit Margin %": [None, None, None, 103.48221],
    "Operating Profit Margin %": [99.375803, 99.227941, 99.093068, 98.448145],
    "Net Profit Margin %": [93.556086, 100.955882, 98.596415, 99.280848],
    "Current Ratio": [7.518248, 0.190930, 6.442953, 6.066667],
    "Quick Ratio": [7.408759, 0.111751, 4.308725, 5.742857],
    "Debt-to-Equity Ratio": [0.127101, 0.141410, 0.007963, 0.008457],
    "Operating Cash Flow Ratio": [13.671533, 0.198196, 4.919463, 7.361905],
    "Free Cash Flow": [1873000.0, 791000.0, 733000.0, 771000.0]
}

# Convert to DataFrame and set the 'Date' column as the index, then add a prefix
ferrari_df = pd.DataFrame(ferrari_data).set_index("Date").add_prefix("Ferrari_")
mercedes_df = pd.DataFrame(mercedes_data).set_index("Date").add_prefix("Mercedes_")
porsche_df = pd.DataFrame(porsche_data).set_index("Date").add_prefix("Porsche_")

# Concatenating all dataframes
all_data_df = pd.concat([ferrari_df, mercedes_df, porsche_df], axis=1)

# Plotting
fig, axs = plt.subplots(9, 1, figsize=(14, 36))

metrics = [
    "Revenue Growth Rate %",
    "Gross Profit Margin %",
    "Operating Profit Margin %",
    "Net Profit Margin %",
    "Current Ratio",
    "Quick Ratio",
    "Debt-to-Equity Ratio",
    "Operating Cash Flow Ratio",
    "Free Cash Flow"
]

def plot_metric(metric_name, data_df, title_prefix):
    plt.figure(figsize=(10, 6))
    for company_prefix in ['Ferrari_', 'Mercedes_', 'Porsche_']:
        if company_prefix + metric_name in data_df.columns:
            plt.plot(data_df.index, data_df[company_prefix + metric_name], label=company_prefix[:-1], marker='o')
    plt.title(f'{title_prefix}: {metric_name}')
    plt.ylabel(metric_name)
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# List of metrics to plot
metrics = [
    "Revenue Growth Rate %",
    "Gross Profit Margin %",
    "Operating Profit Margin %",
    "Net Profit Margin %",
    "Current Ratio",
    "Quick Ratio",
    "Debt-to-Equity Ratio",
    "Operating Cash Flow Ratio",
    "Free Cash Flow"
]

# Plot each metric separately
for metric in metrics:
    plot_metric(metric, all_data_df, "Financial Metric Comparison")

# Assuming all_data_df is your DataFrame containing the financial metrics for Ferrari and Mercedes
# Extend the index for plotting forecasted values
extended_years = ['12/30/2020', '12/30/2021', '12/30/2022', '12/30/2023', '2024', '2025']
forecast_years = np.array([4, 5]).reshape(-1, 1)  # Years for forecasting
years = np.array([0, 1, 2, 3]).reshape(-1, 1)  # Original dataset years

# List of metrics to forecast
metrics = [
    "Revenue Growth Rate %",
    "Gross Profit Margin %",
    "Operating Profit Margin %",
    "Net Profit Margin %",
    "Current Ratio",
    "Quick Ratio",
    "Debt-to-Equity Ratio",
    "Operating Cash Flow Ratio",
    "Free Cash Flow"
]

# Function to forecast a metric using linear regression
def forecast_metric(metric_name, df):
    # Prepare data
    ferrari_metric = df[f'Ferrari_{metric_name}'].dropna().values.reshape(-1, 1)
    mercedes_metric = df[f'Mercedes_{metric_name}'].dropna().values.reshape(-1, 1)
    
    # Linear regression for Ferrari
    lr_ferrari = LinearRegression().fit(years[:len(ferrari_metric)], ferrari_metric)
    ferrari_forecast = lr_ferrari.predict(forecast_years)
    
    # Linear regression for Mercedes
    lr_mercedes = LinearRegression().fit(years[:len(mercedes_metric)], mercedes_metric)
    mercedes_forecast = lr_mercedes.predict(forecast_years)
    
    return ferrari_forecast.flatten(), mercedes_forecast.flatten()

# Function to plot actual and forecasted metrics
def plot_forecasted_metric(metric_name, df):
    ferrari_forecast, mercedes_forecast = forecast_metric(metric_name, df)
    ferrari_actual_and_forecast = np.append(df[f'Ferrari_{metric_name}'], ferrari_forecast)
    mercedes_actual_and_forecast = np.append(df[f'Mercedes_{metric_name}'], mercedes_forecast)
    
    plt.figure(figsize=(10, 6))
    plt.plot(extended_years, ferrari_actual_and_forecast, label='Ferrari Actual', marker='o', linestyle='-')
    plt.plot(extended_years, mercedes_actual_and_forecast, label='Mercedes Actual', marker='o', linestyle='-')
    plt.plot(extended_years[-2:], ferrari_forecast, label='Ferrari Forecast', marker='o', linestyle='--', color='orange')
    plt.plot(extended_years[-2:], mercedes_forecast, label='Mercedes Forecast', marker='o', linestyle='--', color='green')
    plt.title(f'{metric_name} with Forecasted Values (2024-2025)')
    plt.xlabel('Year')
    plt.ylabel(metric_name)
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.show()

# Example: Forecast and plot "Current Ratio"
for metric in metrics:
    plot_forecasted_metric(metric, all_data_df)