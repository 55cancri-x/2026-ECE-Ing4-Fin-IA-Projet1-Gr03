from dataclasses import dataclass

@dataclass(frozen=True)
class Parametres:
    # Horizon et pas de temps
    T: int = 1000          # nombre de pas
    dt: float = 1.0

    # Prix (mid-price) : random walk discret
    S0: float = 100.0
    sigma: float = 0.2     # volatilité par pas

    # Arrivées d'ordres : intensité dépendante du spread
    lambda0: float = 1.2   # intensité "de base" (plus grand => plus d'exécutions)
    k: float = 1.5         # sensibilité au spread (plus grand => moins d'exécutions quand spread augmente)

    # Inventaire
    q_max: int = 10        # contrainte simple : |q| <= q_max

    # Coûts (optionnel mais utile)
    fee_per_trade: float = 0.0  # tu peux mettre 0.001 etc. si vous voulez

    # Reproductibilité
    seed: int = 42


