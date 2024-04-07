from strategies.index import Strategy
import pandas as pd
import talib

class MACDStrategy(Strategy):
    def __init__(self, data, fast_period=12, slow_period=26, signal_period=9):
        super().__init__(data)
        self.fast_period = fast_period
        self.slow_period = slow_period
        self.signal_period = signal_period

    def generate_signals(self):
        macd, signal, _ = talib.MACD(self.data['Price'], fastperiod=self.fast_period, slowperiod=self.slow_period, signalperiod=self.signal_period)

        self.signals = pd.DataFrame(index=self.data.index)
        self.signals['Signal'] = 0

        # Generate buy signals for MACD line crossing above signal line
        self.signals['Signal'][macd > signal] = 1

        # Generate sell signals for MACD line crossing below signal line
        self.signals['Signal'][macd < signal] = -1