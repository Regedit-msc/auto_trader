
from strategies.index import Strategy
import pandas as pd

class MovingAverageStrategy(Strategy):
    def __init__(self, data, short_window, long_window):
        super().__init__(data)
        self.short_window = short_window
        self.long_window = long_window

    def generate_signals(self):
        self.data['Short_MA'] = self.data['Price'].rolling(window=self.short_window).mean()
        self.data['Long_MA'] = self.data['Price'].rolling(window=self.long_window).mean()

        self.signals = pd.DataFrame(index=self.data.index)
        self.signals['Signal'] = 0
        self.signals['Signal'][self.data['Short_MA'] > self.data['Long_MA']] = 1  # Buy signal
        self.signals['Signal'][self.data['Short_MA'] < self.data['Long_MA']] = -1  # Sell signal