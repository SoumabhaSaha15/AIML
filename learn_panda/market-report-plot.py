import matplotlib.pyplot as plt
import pandas as pd
data = {'Date': ['10-01-16', '10-02-16', '10-03-16', '10-04-16', '10-05-16', '10-06-16', '10-07-16'],
        'Open': [770.25, 776.030029, 774.25, 776.030029, 779.3541998, 776.306698, 779.659973],
        'High': [776.075902, 778.730022, 776.065702, 771.710022, 782.073407, 782.46398, 783.23],
        'Low': [769.5, 780.890015, 766.5, 772.890015, 775.650024, 775.539978,781.356],
        'Close': [675.23, 796.429993, 972.549798, 576.429993, 676.469971, 850.859985, 382.368]}

df = pd.DataFrame(data)
print(df)

# a) Line Chart
plt.figure(figsize=(5,3))
plt.plot(df['Date'], df['Open'], label='Open', color='blue')
plt.plot(df['Date'], df['High'], label='High', color='green')
plt.plot(df['Date'], df['Low'], label='Low', color='red')
plt.plot(df['Date'], df['Close'], label='Close', color='purple')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Stock Prices Over Time')
plt.legend()
plt.show()

# b) Bar Graph
plt.figure(figsize=(5, 3))
plt.bar(df['Date'], df['Close'], label='Close', color='orange')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.title('Closing Stock Prices')
plt.legend()
plt.show()

# c) Histogram - Assuming we want to see distribution of closing prices
plt.figure(figsize=(5, 3))
plt.hist(df['Close'], bins=7, label='Close', color='gray', edgecolor='black')
plt.xlabel('Closing Price')
plt.ylabel('Frequency')
plt.title('Distribution of Closing Prices')
plt.legend()
plt.show()







