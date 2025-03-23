import pandas as pd
from backtesting import Backtest, Strategy

# Load data
df = pd.read_csv('btc_usdt_data.csv')

# Rename columns if necessary
df.rename(columns={
    'open': 'Open',
    'high': 'High',
    'low': 'Low',
    'close': 'Close',
    'volume': 'Volume',
    'timestamp': 'Timestamp'
}, inplace=True)

# Ensure timestamp is in datetime format and set as index
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df.set_index('Timestamp', inplace=True)

# Define Strategy
class MACD_SMA_Strategy(Strategy):
    sma_period = 20  
    macd_short = 12  
    macd_long = 26   
    macd_signal = 9  
    
    def init(self):
        self.sma = self.I(lambda x: pd.Series(x).rolling(self.sma_period).mean(), self.data.Close)
        self.macd, self.signal = self.I(self.macd_func, self.data.Close, self.macd_short, self.macd_long, self.macd_signal)
        
    def macd_func(self, close, short, long, signal):
        close_series = pd.Series(close)
        macd_line = close_series.ewm(span=short, adjust=False).mean() - close_series.ewm(span=long, adjust=False).mean()
        signal_line = macd_line.ewm(span=signal, adjust=False).mean()
        return macd_line, signal_line
    
    def next(self):
        risk_per_trade = 0.01  # 1% of available cash
        cash = self.equity  # Available balance
        position_size = (cash * risk_per_trade) / self.data.Close[-1]  # Convert cash to BTC units

        if self.macd[-1] > self.signal[-1] and self.data.Close[-1] > self.sma[-1]:
            if not self.position:
                self.buy(size=position_size)
        elif self.macd[-1] < self.signal[-1] and self.data.Close[-1] < self.sma[-1]:
            if self.position:
                self.sell(size=self.position.size)  # Close entire position


# Backtest with 100x leverage
def backtest():
    bt = Backtest(df, MACD_SMA_Strategy, cash=1000000, commission=0.002, margin=0.01)  # 100x leverage
    stats = bt.run()
    print(stats)
    bt.plot()

backtest()
