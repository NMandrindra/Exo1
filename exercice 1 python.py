import itertools

def table_verite(fonction, variables):
    valeurs_variables = list(itertools.product([0, 1], repeat=len(variables))) 
   
  
    print((),' | '.join(variables) + ' | ' + fonction)
    print('_' * (len(variables) ** 2+10))   
    for valeurs in valeurs_variables:
        valeurs_str = [str(valeur) for valeur in valeurs]
        resultat = eval(fonction, dict(zip(variables, valeurs)))
        
        if resultat == 0:
            print((),' | '.join(valeurs_str) + ' | ' + str(int(resultat)),'|','   f')
        else:
            print((),' | '.join(valeurs_str) + ' | ' + str(int(resultat)),'|','   v')   
            
       #  for variable in variables :
         #	h == [variable if valeur_str == 1 else Not(variable) for variable]
       	#  k == [variable if valeur_str == 0 else Not(variable) for variable]
       
     #  if resultat ==1:
       #  prime_implicants = (And(*h))
      # elif resulat == 0:
             # prime_implicants = (Or(*k))      
            
fonction = input("Entrez la fonction booléenne en utilisant les opérateurs logiques (& pour ET, | pour OU, ~ pour NON, ^ pour OU EXCLUSIF): ")
variables = input("Entrez les noms des variables séparés par des espaces: ").split()
table_verite(fonction, variables)

print('      ')
print('     première forme canonique =') #print(Or(prime_implicants))
print('      ')
print('    deuxième forme canonique =') #print(And(prime_implicants))
