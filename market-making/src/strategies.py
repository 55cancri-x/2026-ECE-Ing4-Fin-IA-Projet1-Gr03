from dataclasses import dataclass

@dataclass
class StrategyOutput:
    bid: float
    ask: float

class StrategieSpreadFixe:
    def __init__(self, spread: float):
        self.spread = float(spread)

    def quote(self, S: float, q: int) -> StrategyOutput:
        bid = S - self.spread / 2.0
        ask = S + self.spread / 2.0
        return StrategyOutput(bid=bid, ask=ask)

class StrategieSkewInventaire:
    """
    Stratégie inspirée Avellaneda-Stoikov / Guéant (version simplifiée) :
    - Un spread 'de base'
    - Un skew proportionnel à l'inventaire q pour pousser à revenir vers 0
    """
    def __init__(self, base_spread: float, gamma: float):
        self.base_spread = float(base_spread)
        self.gamma = float(gamma)

    def quote(self, S: float, q: int) -> StrategyOutput:
        # skew: si q>0 (long), on veut vendre => on baisse ask et on baisse aussi bid
        # (donc on décale les deux quotes vers le bas)
        skew = self.gamma * q

        bid = S - self.base_spread / 2.0 - skew
        ask = S + self.base_spread / 2.0 - skew
        return StrategyOutput(bid=bid, ask=ask)

