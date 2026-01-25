# Sujet 50 

# Farhan et Ilhan


## Contexte et problème : 

1) Market making (bid/ask, spread, exécutions, inventaire)

Le market maker fournit de la liquidité en affichant en continu deux prix : un bid (prix d’achat) et un ask (prix de vente).  
La différence entre l’ask et le bid est le spread, qui représente la marge potentielle capturée si le market maker achète au bid puis revend à l’ask.

Lorsqu’un autre participant envoie un ordre “au marché”, il peut exécuter le bid (le market maker achète) ou l’ask (le market maker vend). Ces événements sont appelés des exécutions.  
Après chaque exécution, l’inventaire (position) du market maker évolue : il augmente après un achat et diminue après une vente.

Le profit ne provient pas uniquement du spread. Le PnL dépend également de la variation du prix du marché appliquée à l’inventaire détenu (mark-to-market).  
Si le prix évolue défavorablement par rapport à la position (par exemple, le market maker est long et le prix baisse), une perte est enregistrée.

Le market maker doit donc ajuster le niveau et l’asymétrie de ses prix afin de rester compétitif tout en maîtrisant son exposition au risque.  
En pratique, cela se traduit par un “skew” des quotes : lorsque l’inventaire devient trop élevé, l’ask est rendu plus attractif pour favoriser la vente, et le bid moins attractif pour limiter les achats.

Le problème est dynamique et stochastique : le marché évolue de manière aléatoire et les exécutions se produisent à des instants incertains.  
L’objectif est de proposer des prix compétitifs, capter le spread et contrôler le risque lié à l’inventaire.


2) Le trade-off “profit du spread” vs “risque d’inventaire”

Un spread large permet de capter une marge plus élevée par transaction, mais réduit la probabilité d’exécution, ce qui limite le volume de trades et donc le profit total.

À l’inverse, un spread serré augmente la fréquence des exécutions, mais réduit la marge par transaction et peut entraîner une accumulation rapide de l’inventaire.

Le principal risque provient de l’inventaire : plus la position |q| est élevée, plus le PnL devient sensible aux variations du prix du marché, ce qui crée une exposition directionnelle non désirée.

Le market maker doit donc parfois accepter une réduction du profit immédiat afin de diminuer son exposition au risque, en modifiant l’asymétrie de ses quotes, en imposant des contraintes d’inventaire (position maximale), en introduisant une contrainte de risque (proxy de VaR) ou en forçant une liquidation partielle ou totale de la position en fin d’horizon.

En résumé :
👉 maximiser le gain du spread pousse à coter agressif et être exécuté.
👉 minimiser le risque d’inventaire pousse à contrôler |q| via des quotes asymétriques, des contraintes (q max, VaR proxy), ou une liquidation.

