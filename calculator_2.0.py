# 1) calculator_2.0.py

import math

class Calculator:
    def __init__(self):
        # 2-a) Initialisation du dictionnaire avec les opérations de base
        self.operations = {
            '+': self.add,
            '-': self.subtract,
            '*': self.multiply,
            '/': self.divide
        }
    
    # 2-b) Méthodes pour les opérations de base
    def add(self, x, y):
        return x + y
    
    def subtract(self, x, y):
        return x - y
    
    def multiply(self, x, y):
        return x * y
    
    def divide(self, x, y):
        if y == 0:
            raise ValueError("Erreur: Division par zéro.")
        return x / y
    
    # 2-c) Méthode pour ajouter une nouvelle opération
    def add_operation(self, symbol, function):
        self.operations[symbol] = function

    # 2-d) Méthode pour effectuer le calcul
    def calculate(self, num1, operation, num2=None):
        # Vérification des types d'entrée
        if not isinstance(num1, (int, float)):
            raise TypeError("Erreur: Le premier nombre doit être un entier ou un flottant.")
        
        if operation not in self.operations:
            raise ValueError(f"Erreur: L'opération '{operation}' n'est pas valide.")
        
        # Si l'opération nécessite un second nombre (comme +, -, *, /)
        if num2 is not None:
            if not isinstance(num2, (int, float)):
                raise TypeError("Erreur: Le deuxième nombre doit être un entier ou un flottant.")
            return self.operations[operation](num1, num2)
        
        # Si l'opération est une fonction unitaire (comme racine carrée ou logarithme ou exponentielle)
        else:
            if operation == 'sqrt':
                return self.sqrt(num1)
            elif operation == 'log':
                return self.log(num1)
            elif operation == '**':
                return self.exponentiation(num1)

    # 3) Fonctions avancées
    def sqrt(self, x):
        if x < 0:
            raise ValueError("Erreur: La racine carrée d'un nombre négatif n'est pas définie.")
        return math.sqrt(x)

    def log(self, x):
        if x <= 0:
            raise ValueError("Erreur: Le logarithme d'un nombre non positif n'est pas défini.")
        return math.log(x)

    def exponentiation(self, base, exponent):
        if not isinstance(exponent, (int, float)):
            raise TypeError("Erreur: L'exposant doit être un entier ou un flottant.")
        return base ** exponent

# 4) Programme principal
if __name__ == "__main__":
    calc = Calculator()
    
    # Ajout des opérations avancées à la calculatrice
    calc.add_operation('sqrt', calc.sqrt)
    calc.add_operation('log', calc.log)
    calc.add_operation('**', calc.exponentiation)

    while True:
        try:
            print("\nOptions d'opération : +, -, *, /, sqrt (racine carrée), log (logarithme), ** (exponentiation)")
            operation = input("Entrez l'opération (ou 'q' pour quitter) : ")
            
            if operation.lower() == 'q':
                print("Merci d'avoir utilisé la calculatrice. Au revoir!")
                break
            
            num1 = float(input("Entrez le premier nombre : "))
            
            if operation in ['+', '-', '*', '/']:
                num2 = float(input("Entrez le deuxième nombre : "))
                result = calc.calculate(num1, operation, num2)
                print(f"Résultat : {result}")
            elif operation == '**':
                exponent = float(input("Entrez l'exposant : "))
                result = calc.calculate(num1, operation, exponent)
                print(f"Résultat : {result}")
            else:
                result = calc.calculate(num1, operation)
                print(f"Résultat : {result}")

        except Exception as e:
            print(e)
