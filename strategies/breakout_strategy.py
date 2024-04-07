import pandas as pd
from strategies.index import Strategy

class BreakoutStrategy(Strategy):
    def __init__(self, data, lookback_period):
        super().__init__(data)
        self.lookback_period = lookback_period

    def generate_signals(self):
        self.data['Support'] = self.data['Price'].rolling(window=self.lookback_period).min()
        self.data['Resistance'] = self.data['Price'].rolling(window=self.lookback_period).max()

        self.signals = pd.DataFrame(index=self.data.index)
        self.signals['Signal'] = 0

        # Generate buy signals for breakout above resistance
        self.signals['Signal'][self.data['Price'] > self.data['Resistance']] = 1

        # Generate sell signals for breakout below support
        self.signals['Signal'][self.data['Price'] < self.data['Support']] = -1