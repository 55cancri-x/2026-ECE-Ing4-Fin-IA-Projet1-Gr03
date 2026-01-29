# Constrained Optimization (CP-SAT)

Cette approche formule l’exécution d’un ordre comme un problème d’optimisation sous contraintes.  
L’objectif est de répartir un volume total à exécuter sur plusieurs tranches de temps tout en respectant les limites de liquidité du marché et en minimisant un coût global.

Le modèle est résolu à l’aide du solveur CP-SAT de Google OR-Tools, qui permet de gérer des variables entières, des contraintes strictes et une fonction objectif quadratique.

## Variables

x_t ∈ ℕ⁺ : volume exécuté à l’instant t

## Données

Q : volume total à exécuter  
V_t : volume de marché observé à l’instant t  
α : taux de participation maximal autorisé  

## Contraintes

Somme des volumes exécutés égale au volume total :

∑ₜ x_t = Q

Borne de liquidité par tranche :

0 ≤ x_t ≤ α · V_t

## Cible VWAP

x_tᵛʷᵃᵖ = Q · V_t / ∑ₖ V_k

## Fonction objectif

min ∑ₜ [ λ_impact · x_t² + λ_track · (x_t − x_tᵛʷᵃᵖ)² ]

Cette fonction modélise le compromis entre impact de marché (volumes trop concentrés) et suivi du benchmark VWAP.

## Sortie

Un planning d’exécution optimal (x₁, x₂, …, x_N).
