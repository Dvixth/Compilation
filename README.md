#Analyseur Syntaxique
Ce programme implémente un analyseur syntaxique pour une grammaire formelle définie. L'analyseur vérifie la syntaxe d'une chaîne d'entrée conformément aux règles de la grammaire spécifiée. Voici une brève description des éléments du code :

#Définition des Symboles
Le programme utilise des symboles non-terminaux (VN) pour définir la structure de la grammaire. Les symboles non-terminaux sont les éléments qui peuvent être remplacés par des terminaux ou d'autres symboles non-terminaux selon les règles de production.

Table d'Analyse
Une table d'analyse (TA) est mise en œuvre à l'aide de dictionnaires imbriqués. Cette table est utilisée pour déterminer les règles de production appropriées lors de l'analyse de la chaîne d'entrée.

Fonctions Principales
empiler_regle(pile, regle): Empile une règle sur la pile.
analyse(chaine): Effectue l'analyse syntaxique de la chaîne d'entrée en suivant les règles de la grammaire.
Utilisation
Le programme demande à l'utilisateur de saisir une chaîne à analyser, en séparant les symboles terminaux par des espaces et en ajoutant le symbole de fin de chaîne $ à la fin. Ensuite, il affiche si la chaîne est acceptée ou s'il y a une erreur de syntaxe. De plus, il affiche l'ensemble des règles utilisées pendant l'analyse.

Exemple d'utilisation
Voici un exemple d'utilisation :

L'utilisateur saisit une chaîne à analyser.
Le programme analyse la chaîne et indique si elle est acceptée ou non.
Il affiche également les règles utilisées pendant l'analyse.
Assurez-vous que la chaîne d'entrée est conforme à la grammaire définie pour obtenir des résultats précis.
