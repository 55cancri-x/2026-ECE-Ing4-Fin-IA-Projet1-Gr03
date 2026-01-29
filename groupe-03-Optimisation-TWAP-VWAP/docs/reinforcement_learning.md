# Reinforcement Learning

L’apprentissage par renforcement permet de modéliser l’exécution d’un ordre comme un processus décisionnel séquentiel.  
Un agent interagit avec un environnement de marché simulé et apprend progressivement une politique d’exécution optimale.

Contrairement à l’optimisation sous contraintes, cette approche ne nécessite pas de connaître à l’avance le profil de liquidité global.

## Environnement

Le temps est discrétisé en N tranches.  
À chaque instant t, l’agent choisit un volume à exécuter sous contrainte de liquidité.

## État

s_t = (t, q_remaining)

t : indice temporel  
q_remaining : volume restant à exécuter (discrétisé)

## Actions

a_t = fraction du volume maximum autorisé à l’instant t :

a_t ∈ {0, 0.25, 0.5, 0.75, 1.0} · cap_t

## Récompense

r_t = − [ λ_impact · a_t² + λ_track · (a_t − x_tᵛʷᵃᵖ)² ]

Une pénalité terminale est ajoutée si le volume total n’est pas exécuté en fin d’épisode.

## Algorithme

Q-learning tabulaire avec politique ε-greedy :

Q(s, a) ← (1 − α) Q(s, a) + α [ r + γ maxₐ Q(s', a) ]

## Sortie

Une politique d’exécution apprise, testée en rollout greedy.
