import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Collect Stock Price Data
# Define the companies and time period
companies = {
    'Ormat Technologies': 'ORA',
    'Brookfield Renewable Partners L.P.': 'BEP',
    'NextEra Energy': 'NEE'
}

# Create a list to store the tickers
tickers_list = []

# Add the tickers of the selected companies into the list
for ticker in companies:
    tickers_list.append(companies[ticker])

# Dates the data are retrieve from
start_date = '2013-01-01'
end_date = '2023-12-31'

# Download data
data = yf.download(tickers_list, start=start_date, end=end_date)['Close']


                                # Step 2: Stock Price Analysis

# Find the maximum and minimum stock prices and their dates

# Creation of a dictionary in which the result of all companies will be stored
results = {}

# Loop through each company. Find the maximum and the id (date) of these maximums.
for company in data:
    max_price = data[company].max()
    max_date = data[company].idxmax()
    min_price = data[company].min()
    min_date = data[company].idxmin()

# Add  in the dictionary for each company with their statistics and add the results
    results[company] = {
        'Max Price': max_price,
        'Max Date': max_date,
        'Min Price': min_price,
        'Min Date': min_date
    }

# Print max and min prices
print("Stock Price Analysis:")
for company, stats in results.items():
    print(f"{company}: Max Price = {stats['Max Price']:.2f} on {stats['Max Date']}, "
          f"Min Price = {stats['Min Price']:.2f} on {stats['Min Date']}")


                                # Step 3: Cumulative Return Calculation

# Calculate cumulative returns
# Let's assume an investment of €1000
initial_investment = 1000
cumulative_returns = {}

# find the return if 1000 dollars were invested on each stock for a period of 10 years
for company in data.columns:
    start_price = data[company].iloc[0]
    end_price = data[company].iloc[-1]
    cumulative_return = (end_price - start_price) / start_price
    investment_value = initial_investment * (1 + cumulative_return)
    cumulative_returns[company] = {
        'Cumulative Return (%)': cumulative_return * 100,
        'Final Investment Value (€)': investment_value
    }

# Print cumulative returns
print("\nCumulative Returns:")
for company, stats in cumulative_returns.items():
    print(f"{company}: Return = {stats['Cumulative Return (%)']:.2f}%, "
          f"Final Investment = ${stats['Final Investment Value (€)']:.2f}")


                                # Step 4: Ecological Impact Comparison

# Data on companies to be compared
environmental_score = {
    'Company': ['ExxonMobil Corporation', 'Chevron Corporation', 'Peabody Energy Corporation',
                'Ormat Technologies', 'Brookfield Renewable Partners L.P.', 'NextEra Energy'],
    'Ticker': ['XOM', 'CVX', 'BTU', 'ORA', 'BEP', 'NEE'],
    'Environmental_Score': [33, 41, 30, 40, 57, 42],
    'Focus': ['No ESG Focus', 'No ESG Focus', 'No ESG Focus', 'ESG Focus', 'ESG Focus', 'ESG Focus']
}

# transform those data into a dataframe
df = pd.DataFrame(environmental_score)

# Separate data by focus
df_no_esg = df[df['Focus'] == 'No ESG Focus']
df_esg = df[df['Focus'] == 'ESG Focus']

# Bar plot of the environmental scores
plt.figure(figsize=(12, 6))
bar_width = 0.4

# x positions for both 'No ESG Focus' and 'ESG Focus' bars, centered around the tick positions
x_ticks = range(len(df))  # This will be the tick positions
x_no_esg = [x - bar_width / 2 for x in x_ticks[:len(df_no_esg)]]  # Offset to the left for 'No ESG Focus'
x_esg = [x + bar_width / 2 for x in x_ticks[len(df_no_esg):]]  # Offset to the right for 'ESG Focus'

# Bars
plt.bar(x_no_esg, df_no_esg['Environmental_Score'],
        width=bar_width, color='orange', label='No ESG Focus')
plt.bar(x_esg, df_esg['Environmental_Score'],
        width=bar_width, color='green', label='ESG Focus')

# Labels and title
plt.xlabel('Companies', fontsize=12)
plt.ylabel('Environmental Score', fontsize=12)
plt.title('Environmental Scores: ESG Focus vs No ESG Focus', fontsize=14)

# Set x-ticks and labels
plt.xticks(x_ticks, df['Company'].tolist(), rotation=45, ha='right')

plt.legend()

plt.tight_layout()
plt.show()

# Plot stock prices over time for stock analysis
data.plot(figsize=(12, 6), title='Stock Prices Over Time')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend(companies.keys())
plt.show()

