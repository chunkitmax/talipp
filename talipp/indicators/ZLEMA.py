from typing import Any, List, Optional

from talipp.indicators.EMA import EMA
from talipp.indicators.Indicator import Indicator


class ZLEMA(Indicator):
  """
  Zero Lag Exponential Moving Average
  """
  def __init__(self, period: int, input_values: Optional[List[float]] = None):
    super().__init__()

    self.period = period
    self.ema1 = EMA(period)
    self.ema2 = EMA(period)

    self.initialize(input_values, None)

  def _calculate_new_value(self) -> Any:
    self.ema1.add_input_value(self.input_values[-1])
    if len(self.ema1) == 0:
      return None
    self.ema2.add_input_value(self.ema1[-1])
    if len(self.ema2) == 0:
      return None
    return self.ema1[-1] + self.ema1[-1] - self.ema2[-1]
