# Data Pipeline

Les données de marché sont utilisées pour construire des profils de liquidité réalistes servant de base aux stratégies VWAP, CP et RL.

Dans ce projet, les données sont récupérées sous forme de snapshots intraday.

## Source

Yahoo Finance (via l’API yfinance)

## Données utilisées

Prix de clôture intraday  
Volumes échangés par intervalle de temps

## Prétraitement

– Sélection d’une fenêtre intraday  
– Agrégation des volumes par tranche de temps  
– Normalisation des volumes si nécessaire  

## Rôle dans le projet

Les volumes servent :
– de référence pour la stratégie VWAP  
– de contraintes de liquidité pour l’optimisation CP  
– de dynamique de l’environnement pour le RL  

Aucune information future n’est utilisée dans les stratégies en ligne.
