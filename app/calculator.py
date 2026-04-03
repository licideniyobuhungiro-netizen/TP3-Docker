# calculator.py

def addition(a, b):
    """Retourne la somme de deux nombres"""
    return a + b

def multiplication(a, b):
    """Retourne le produit de deux nombres"""
    return a * b

# Section de test (s'exécute uniquement si on lance ce fichier)
if __name__ == "__main__":
    print("--- Test de la calculatrice ---")
    x, y = 10, 5
    print(f"{x} + {y} = {addition(x, y)}")
    print(f"{x} * {y} = {multiplication(x, y)}")