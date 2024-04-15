from sympy import symbols, Or, And, Not
from sympy.logic.boolalg import SOPform
import itertools

expression = input("Entrez la fonction booléenne en utilisant les opérateurs logiques (& pour ET, | pour OU, ~ pour NON, ^ pour OU EXCLUSIF): ")
variables = input("Entrez les noms des variables séparés par des espaces: ").split()
table_verite(fonction, variables)

def get_minterms(expression):
    minterms = []
    n = len(expression)
    for i in range(2 ** n):
        if expression[i] == '1':
            minterms.append(format(i, '0' + str(n) + 'b'))
    return minterms


def minimize_boolean_function(expression):
    variables = symbols(' '.join(set(expression)))
    minterms = get_minterms(expression)
    simplified_expression = SOPform(variables, minterms)
    return simplified_expression

def boolean_string_to_logic_expression(boolean_string):
    variables = symbols(' '.join(set(boolean_string)))
    expression = ''
    for i, char in enumerate(boolean_string):
        if char == '1':
            expression += f"And({variables[i]})"
        elif char == '0':
            expression += f"And(Not({variables[i]}))"
    return expression[4:]  


#boolean_string = input("Entrez la fonction booléenne (utilisez '1' pour True et '0' pour False): ")


logic_expression = boolean_string_to_logic_expression(boolean_string)

minimized_expression = minimize_boolean_function(logic_expression)

print("Fonction minimisée:", minimized_expression)
