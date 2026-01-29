# Overview – Architecture et fonctionnement du projet

## Objectif du document

Ce document fournit une vue d’ensemble technique du projet **Optimisation d’exécution d’ordres par contraintes (TWAP / VWAP)**. Il décrit l’architecture globale, le pipeline de données et l’articulation entre les différentes stratégies implémentées (baselines, optimisation sous contraintes et apprentissage par renforcement).

---

## Vue globale

Le projet suit un pipeline commun à toutes les stratégies d’exécution :

1. Chargement ou génération des données de marché
2. Définition du volume total à exécuter et de l’horizon temporel
3. Application d’une stratégie d’exécution (TWAP, VWAP, CP-SAT ou RL)
4. Génération d’un planning d’exécution discret par tranche temporelle
5. Évaluation des performances (prix moyen, tracking error, impact proxy)

---

## Organisation du code

Le code est structuré de manière modulaire afin de séparer clairement :

* les stratégies d’exécution
* la gestion des données de marché
* les scripts d’exécution et de comparaison

### Structure principale

* `src/strategies/`

  * Implémente les différentes stratégies d’exécution
  * Chaque fichier correspond à une approche spécifique

* `src/data/`

  * Gestion du chargement et du prétraitement des données de marché

* `run_*.py`

  * Scripts d’entrée permettant d’exécuter une stratégie ou une comparaison
  * Ces scripts orchestrent les appels aux modules internes

---

## Données de marché

Les stratégies s’appuient sur des données de marché intraday (volumes et prix), chargées via le module `market_data.py`.

Ces données servent à :

* construire un profil de liquidité (VWAP)
* définir des contraintes réalistes de participation au marché
* simuler un environnement d’exécution

Dans certains cas (tests unitaires ou démonstrations), des données synthétiques peuvent être utilisées.

---

## Discrétisation temporelle

L’horizon d’exécution est discrétisé en **N tranches temporelles** (time buckets).

Pour chaque tranche :

* une quantité de volume est exécutée
* le volume de marché associé est connu (ou observé)

Toutes les stratégies produisent en sortie un vecteur :

```
q = (q₁, q₂, …, qₙ)
```

avec la contrainte :

```
∑ qᵢ = Q_total
```

---

## Stratégies implémentées

### TWAP (Time-Weighted Average Price)

La stratégie TWAP répartit le volume total uniformément sur l’ensemble des tranches temporelles.

Elle sert de baseline simple, sans prise en compte de la liquidité du marché.

---

### VWAP (Volume-Weighted Average Price)

La stratégie VWAP répartit le volume proportionnellement au volume de marché observé.

Elle permet un meilleur alignement avec la liquidité, mais suppose que le profil de volume est connu.

---

### Optimisation sous contraintes (CP-SAT)

Le problème d’exécution est formulé comme un problème d’optimisation sous contraintes.

Les volumes par tranche sont des variables de décision, soumises à :

* une contrainte de volume total
* des bornes par tranche
* des contraintes de participation au marché

La fonction objectif combine :

* un proxy d’impact de marché
* un terme de tracking error par rapport au VWAP

Le problème est résolu à l’aide du solveur **CP-SAT (OR-Tools)**.

---

### Apprentissage par renforcement (Reinforcement Learning)

L’exécution est modélisée comme un problème de décision séquentielle.

À chaque tranche temporelle, un agent décide de la quantité à exécuter en fonction :

* de l’état du marché
* du volume restant
* du temps restant

Contrairement aux approches précédentes, le RL ne suppose pas une connaissance parfaite du futur.

---

## Scripts d’exécution

Les scripts `run_*.py` permettent de :

* exécuter individuellement chaque stratégie
* comparer les résultats sur un même jeu de données
* tester le comportement sur données réelles

Ils constituent le point d’entrée principal du projet.


