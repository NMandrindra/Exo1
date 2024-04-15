import itertools

def evaluer_expression(expression, valeurs):
    """Évalue une expression logique avec les valeurs données."""
    return eval(expression, valeurs)

def generer_table_verite(expression, variables):
    """Génère le tableau de vérité pour une expression logique donnée."""
    n = len(variables)
    combinaisons = list(itertools.product([0, 1], repeat=n))
    table_verite = []

    for comb in combinaisons:
        valeurs = dict(zip(variables, comb))
        resultat = evaluer_expression(expression, valeurs)
        table_verite.append(list(comb) + [resultat])

    return table_verite

def obtenir_fonctions_booleanes(table_verite, variables):
    """Calcule les formes canoniques de la fonction."""
    mintermes = [ligne[:-1] for ligne in table_verite if ligne[-1]]
    maxtermes = [ligne[:-1] for ligne in table_verite if not ligne[-1]]
    
    expressions_mintermes = []
    for minterme in mintermes:
        expressions = []
        for i, var in enumerate(variables):
            if minterme[i]:
                expressions.append(var)
            else:
                expressions.append(f"{var}̄")
        expressions_mintermes.append("".join(expressions))
    
    expressions_maxtermes = []
    for maxterme in maxtermes:
        expressions = []
        for i, var in enumerate(variables):
            if maxterme[i]:
                expressions.append(f"{var}̄")
            else:
                expressions.append(var)
        expressions_maxtermes.append("+".join(expressions))
    
    return expressions_mintermes, expressions_maxtermes

def obtenir_deuxieme_forme_canonique(expressions_mintermes, expressions_maxtermes):
    """Calcule la deuxième forme canonique de la fonction."""
    deuxieme_forme_canonique = []
    for minterme in expressions_mintermes:
        for maxterme in expressions_maxtermes:
            expression = f"({minterme}) or ({maxterme})"
            deuxieme_forme_canonique.append(expression)
    return deuxieme_forme_canonique

def main():
    expression = input("Entrez la fonction booléenne en utilisant les opérateurs logiques (& pour ET, | pour OU, ~ pour NON, ^ pour OU EXCLUSIF): ")
    variables = sorted(set([c for c in expression if c.isalpha()]))
    
    table_verite = generer_table_verite(expression, variables)
    
    # Affichage du tableau de vérité sous forme de matrice
    print("  Tableau de vérité :")
    entetes = variables + [expression]
    print("  "+" | ".join(entetes))
    print("_" * (len(entetes) **2 +4))
    for ligne in table_verite:
        print("  "+" | ".join(str(item) for item in ligne))

    # Calcul de la première forme canonique
    expressions_mintermes, expressions_maxtermes = obtenir_fonctions_booleanes(table_verite, variables)
    print("\nPremière forme canonique (somme de mintermes) :")
    print("("+")+(".join(expressions_mintermes)+")")
 

    # Calcul de la deuxième forme canonique
    deuxieme_forme_canonique = obtenir_deuxieme_forme_canonique(expressions_mintermes, expressions_maxtermes)
    print("\nDeuxième forme canonique (produit des maxtermes):")
    print("(" + ") (".join(expressions_maxtermes)+")")

if __name__ == "__main__":
    main()
