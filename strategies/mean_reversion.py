
from strategies.index import Strategy
import pandas as pd


class MeanReversionStrategy(Strategy):
    def __init__(self, data, lookback_period, threshold):
        super().__init__(data)
        self.lookback_period = lookback_period
        self.threshold = threshold

    def generate_signals(self):
        self.data['Rolling_Mean'] = self.data['Price'].rolling(window=self.lookback_period).mean()
        self.data['Rolling_Std'] = self.data['Price'].rolling(window=self.lookback_period).std()

        self.signals = pd.DataFrame(index=self.data.index)
        self.signals['Signal'] = 0
        self.signals['Signal'][self.data['Price'] < (self.data['Rolling_Mean'] - self.threshold * self.data['Rolling_Std'])] = 1  # Buy signal
        self.signals['Signal'][self.data['Price'] > (self.data['Rolling_Mean'] + self.threshold * self.data['Rolling_Std'])] = -1  # Sell signal

    