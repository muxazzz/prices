import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
start_date = "2020-03-01"
end_date = "2020-03-15"
aapl = yf.download("YNDX DSKY.ME", start=start_date, end=end_date)
close=aapl["Close"]
empty={'date': ['Volume'], 'col2':['Volume']}
df = pd.DataFrame(data=empty)
volume=aapl["Volume"]
printer1 = close.append(df)
printer = printer1.append(volume)
printer1.plot()
plt.show
plt.savefig('my_plot.png')
printer.to_csv (r'/Users/mikhailpuchkov/Desktop/miexport_dataframe.csv', index = True, header=True)
