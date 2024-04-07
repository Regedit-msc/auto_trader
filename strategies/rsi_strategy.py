from strategies.index import Strategy
import pandas as pd
import talib

class RSIStrategy(Strategy):
    def __init__(self, data, period=14, overbought=70, oversold=30):
        super().__init__(data)
        self.period = period
        self.overbought = overbought
        self.oversold = oversold

    def generate_signals(self):
        self.data['RSI'] = talib.RSI(self.data['Price'], timeperiod=self.period)

        self.signals = pd.DataFrame(index=self.data.index)
        self.signals['Signal'] = 0

        # Generate buy signals for oversold conditions
        self.signals['Signal'][self.data['RSI'] < self.oversold] = 1

        # Generate sell signals for overbought conditions
        self.signals['Signal'][self.data['RSI'] > self.overbought] = -1