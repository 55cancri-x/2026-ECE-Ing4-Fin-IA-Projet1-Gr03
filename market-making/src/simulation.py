import numpy as np
from dataclasses import dataclass
from typing import Tuple

from .parametres import Parametres

@dataclass
class Etat:
    t: int
    S: float
    q: int
    cash: float

class SimulateurMarche:
    """
    Simulateur minimal pour market making :
    - Le midprice S suit un random walk discret
    - Des ordres au marché arrivent avec une intensité lam(spread)
    - Si exécution : on trade au bid (achat) ou au ask (vente) avec prob 1/2
    - Contrainte inventaire : |q| <= q_max
    """
    def __init__(self, p: Parametres):
        self.p = p
        self.rng = np.random.default_rng(p.seed)
        self.reset()

    def reset(self) -> Etat:
        self.etat = Etat(t=0, S=float(self.p.S0), q=0, cash=0.0)
        return self.etat

    def _evol_prix(self) -> None:
        self.etat.S += self.p.sigma * self.rng.standard_normal()

    def _intensite(self, spread: float) -> float:
        # Intensité décroissante avec le spread : lam = lambda0 * exp(-k * spread)
        spread = max(spread, 1e-9)  # éviter valeurs <=0
        return self.p.lambda0 * np.exp(-self.p.k * spread)

    def step(self, bid: float, ask: float) -> Tuple[Etat, float, bool]:
        """
        Effectue un pas :
        - Met à jour le prix
        - Simule une exécution éventuelle
        Retourne: (etat, pnl_mtm, executed)
        """
        if ask <= bid:
            raise ValueError(f"Quotes invalides: ask ({ask}) doit être > bid ({bid}).")

        # 1) mise à jour prix
        self._evol_prix()

        # 2) exécution ?
        spread = ask - bid
        lam = self._intensite(spread)
        proba_exec = min(1.0, lam * self.p.dt)

        executed = False

        if self.rng.random() < proba_exec:
            executed = True

            # achat au bid (50%) ou vente à l'ask (50%)
            if self.rng.random() < 0.5:
                # exécution au bid => on ACHÈTE (q += 1)
                if self.etat.q < self.p.q_max:
                    self.etat.q += 1
                    self.etat.cash -= bid
                    self.etat.cash -= self.p.fee_per_trade
            else:
                # exécution à l'ask => on VEND (q -= 1)
                if self.etat.q > -self.p.q_max:
                    self.etat.q -= 1
                    self.etat.cash += ask
                    self.etat.cash -= self.p.fee_per_trade

        # 3) temps + pnl
        self.etat.t += 1
        pnl = self.etat.cash + self.etat.q * self.etat.S

        return self.etat, pnl, executed

