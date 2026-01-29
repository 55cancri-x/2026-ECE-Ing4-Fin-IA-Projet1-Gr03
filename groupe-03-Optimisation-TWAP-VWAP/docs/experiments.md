# Experiments

Cette section décrit les expériences menées pour comparer les différentes stratégies d’exécution.

## Stratégies comparées

– TWAP  
– VWAP  
– Optimisation sous contraintes (CP-SAT)  
– Agent de reinforcement learning  

## Scénarios

– Profils de volumes synthétiques  
– Profils de volumes intraday réels  

## Métriques d’évaluation

Impact de marché (proxy quadratique) :

Impact = ∑ₜ x_t²

Erreur de tracking VWAP :

Tracking = ∑ₜ (x_t − x_tᵛʷᵃᵖ)²

## Analyse

Les résultats mettent en évidence :
– la simplicité mais la rigidité de TWAP  
– l’alignement marché de VWAP  
– le compromis optimal impact / tracking du modèle CP  
– la capacité adaptative du RL dans un cadre en ligne  

Les expériences confirment la cohérence des modèles et leurs limites respectives.
