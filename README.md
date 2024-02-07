# README

## Introduction
Ce référentiel contient du code pour définir une grammaire hors contexte et implémenter des procédures d'analyse pour un langage simple. Le langage comprend un ensemble de symboles non terminaux (*VN*) et une table d'analyse (*TA*) pour faciliter l'analyse syntaxique. Le code fourni comprend des fonctions pour analyser les chaînes d'entrée selon les règles de grammaire définies.

## Grammaire hors contexte
La grammaire est définie avec les symboles non terminaux suivants :
- `<Programme>`
- `<liste_declarations>`
- `<une_declaration>`
- `<liste_instructions>`
- `<une_instruction>`
- `<type>`
- `<affectation>`
- `<test>`
- `<condition>`
- `<operateur>`

## Table d'analyse (*TA*)
La table d'analyse (*TA*) est implémentée sous forme de dictionnaires imbriqués pour faciliter l'analyse selon les règles de grammaire. Elle associe les symboles terminaux aux règles de production correspondantes.

## Structure du code
Le code se compose des composants principaux suivants :

1. **Définition de VN et TA** : 
   - *VN* : Ensemble de symboles non terminaux.
   - *TA* : Table d'analyse associant les symboles terminaux aux règles de production.

2. **Fonctions d'analyse** :
   - `empiler_regle(pile, regle)` : Fonction pour pousser une règle sur la pile.
   - `analyse(chaine)` : Fonction pour effectuer une analyse sur les chaînes d'entrée selon les règles de grammaire.

3. **Entrée et sortie** :
   - Une entrée utilisateur est demandée pour fournir la chaîne à analyser.
   - Les résultats de l'analyse, y compris les règles de réduction appliquées, sont affichés à l'utilisateur.

## Utilisation
Pour utiliser ce code, suivez ces étapes :
1. Clonez le référentiel sur votre machine locale.
2. Exécutez le script Python contenant le code.
3. Suivez les instructions à l'écran pour entrer la chaîne à analyser.
4. Visualisez les résultats de l'analyse affichés dans la console.

## Exemple
Voici un exemple d'utilisation du code :
1. Clonez le référentiel :
   ```bash
   git clone https://github.com/votre-nom-utilisateur/votre-repository.git
2. Naviguez jusqu'au répertoire du référentiel :
     ```bash
   cd your-repository
3. Exécutez le script Python :
   ```bash
   python Mini_C_Compiler.py

## Contribution
Les contributions à ce projet sont les bienvenues. Vous pouvez contribuer en :

Soumettant des rapports de bogues ou des demandes de fonctionnalités via le suivi des problèmes.
Proposant des améliorations de code ou de nouvelles fonctionnalités via des demandes de tirage.
