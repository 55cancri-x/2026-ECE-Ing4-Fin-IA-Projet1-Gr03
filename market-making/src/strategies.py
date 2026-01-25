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
        half = self.base_spread / 2.0
        skew = self.gamma * q

        # On définit directement les distances au mid
        delta_b = max(0.0, half + skew)   # q>0 => delta_b augmente => bid plus bas => moins d'achats
        delta_a = max(0.0, half - skew)   # q>0 => delta_a diminue => ask plus proche => plus de ventes

        bid = S - delta_b
        ask = S + delta_a
        return StrategyOutput(bid=bid, ask=ask)

