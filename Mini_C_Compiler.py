# Définition de VN et TA

#Un set qui nous permet de définir les symbole non Terminaux 
VN = { 
    '<Programme>', '<liste_declarations>', '<une_declaration>',
    '<liste_instructions>', '<une_instruction>', '<type>',
    '<affectation>', '<test>', '<condition>', '<operateur>'
}

#Deux dictionnaires imbriqués qui nous permettent de mettre en oeuvre une table d'analyse pour notre grammaire 
#la faculté avec les dictionnaire c'est leur strucutre <clé, valeur> pour notre cas on a : 
#Dictionaire 1 : <Clé=Symbole Terminale,Valeur=Le symbole reconnu et la règle qui le,produit <Clé=Symbole Terminal, Valeur = Règle>>
TA = {
    '<Programme>': {'main(){': 'main(){ <liste_declarations> <liste_instructions> } $'},
    '<liste_declarations>': {'int': '<une_declaration> <liste_declarations>', 'float': '<une_declaration> <liste_declarations>', '}': '$', 'id': '$', 'if': '$'},
    '<une_declaration>': {'int': '<type> id', 'float': '<type> id'},
    '<liste_instructions>': {'id': '<une_instruction> <liste_instructions>', 'if': '<une_instruction> <liste_instructions>', '}': '$'},
    '<une_instruction>': {'id': '<affectation> ', 'if': '<test>'},
    '<type>': {'int': 'int', 'float': 'float'},
    '<affectation>': {'id': 'id = nombre'},
    '<test>': {'if': 'if <condition> <une_instruction> else <une_instruction>'},
    '<condition>': {'id': 'id <operateur> nombre '},
    '<operateur>': {'<': '<', '>': '>', '=': '='}
}

# Fonction pour empiler une règle sur la pile qui a deux paramètre un tableau et une chaine
def empiler_regle(pile, regle): 
     # Diviser la règle en symboles individuels tel que regle c'est une chaine de caractère spérée par des espace 
     #la fonction split() dévise chaque mot avec un espace entre les deux 
    regle = regle.split() 
    #parcour de la chaine regle a l'envers 
    for symbole in reversed(regle):
    #ajoute du symbole dans la pile 
        pile.append(symbole)
    #cette fonction opère cette partie de l'algorithme présenté lors du cours :     

#initialisation d'un tableau vide pour sauvegarder les règles utilisé lors de l'analyse 
regles_reduites = []

# Fonction pour effectuer l'analyse qui prend en paramètre la chaine
def analyse(chaine):
    
    pile = ['<Programme> $']  # Initialisation de la pile avec l'axiome et le symbole $ 
    i = 0  # Indice pour parcourir la chaîne d'entrée

    while True:
        sommet_pile = pile[-1]
        sommet_pile = sommet_pile.split()[0]#Sommet_pile prend le premier symbole terminal ou non 
        
        if sommet_pile in VN: #si le sommet de la pile est un VN
            symbole_courant = chaine[i] if i < len(chaine) else '$' #initlaisation d'un symbole courant ( les condition font en sorte 
            #que si la position du symbole est = a la langueur de la chaine c.a.d qu'on est arrivé a la fin de la chaine et que c'est automatiquement le symbole courant )
            
            if sommet_pile in TA and symbole_courant in TA[sommet_pile]:#cette codition vérifie dans TA si il existe une règle de 
                #production entre le symbole courant avec le sommet de pile 
                regle = TA[sommet_pile][symbole_courant] # initialisation de la pile 
                if regle == '$':  # Si la réduction est de la forme VN -> $
                    regles_reduites.append(f"{sommet_pile} -> {regle}") #emplier la règle dans la tableau  
                    print(regles_reduites[i])                    
                    pile.pop()  # Ignore la réduction qui donne le vide car elle dépile pas la chaine 
                else:
                    regles_reduites.append(f"{sommet_pile} -> {regle}") 
                    pile.pop()  # Dépiler le symbole non terminal
                    empiler_regle(pile, regle)  # Empiler la règle inversée
                continue
            else:
                print("Erreur de syntaxe") 
                break
        else:
            if sommet_pile == '$': # si le sommet de pile est vide 
                if chaine[i] == '$':#et le symbole de la chaine courant est vide 
                    print("Chaîne acceptée")
                    break
                else:
                    print("Erreur de syntaxe")
                    break
            elif sommet_pile == chaine[i]:
                pile.pop()  # Dépiler la pile
                i += 1
            else:
                print("Erreur de syntaxe")
                break

# Chaîne à analyser
chaine_a_analyser =input("Entrez votre chaine a analysé en séparant les symbole terminaux avec des espaces et en ajoutant $ a la fin : ")

# Appel de la fonction d'analyse
analyse(chaine_a_analyser.split())

#Les règles 
print("Ensemble des règles utilisé sont : ")
for regle in regles_reduites:
    print(regle)


