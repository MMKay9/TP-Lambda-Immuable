import time  # Importation du module time pour mesurer le temps d'exécution

# ========================
# Exercice 1 : Fonctions de base
# ========================

# Fonction qui calcule le carré d'un nombre
def square(x):
    return x ** 2

print(square(4))  # Test : devrait afficher 16


# Fonction qui applique la fonction carré à une liste de nombres
def square_list(numbers):
    return list(map(lambda x: x ** 2, numbers))

numbers = [1, 2, 3, 4, 5]
print(square_list(numbers))  # Test : devrait afficher [1, 4, 9, 16, 25]


# Fonction qui additionne deux nombres
def sum_two_numbers(a, b):
    return a + b

print(sum_two_numbers(3, 5))  # Test : devrait afficher 8


# Fonction qui calcule la somme des éléments d'une liste
def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

numbers = [1, 2, 3, 4, 5]
print(sum_list(numbers))  # Test : devrait afficher 15


# ========================
# Exercice 2 : Utilisation des clôtures
# ========================

# Fonction qui retourne une fonction multipliant un nombre par n
def create_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

double = create_multiplier(2)  # Création d'une fonction qui double un nombre
triple = create_multiplier(3)  # Création d'une fonction qui triple un nombre

# Tests
print(double(5))   # 10
print(double(7))   # 14
print(triple(4))   # 12
print(triple(6))   # 18


# ========================
# Exercice 3 : Manipulation des listes de mots
# ========================

# Liste de mots
words = ["Voiture", "Lego", "Fruit", "Ecole", "Arbre", "Epée", "Cheval", "Haricot"]

# Filtrer les mots qui commencent par 'a' (insensible à la casse)
filtered_words = list(filter(lambda word: word.lower().startswith('a'), words))

# Fonction qui compte les mots de plus de min_length caractères
def create_length_counter(min_length):
    def counter(word_list):
        return sum(1 for word in word_list if len(word) > min_length)
    return counter

count_long_words = create_length_counter(5)

# Tests
print(filtered_words)  # Devrait afficher les mots commençant par 'a'
print(count_long_words(words))  # Nombre de mots ayant plus de 5 caractères


# ========================
# Exercice 5 : Composition de fonctions
# ========================

# Fonction qui compose deux fonctions f et g : retourne f(g(x))
def compose(f, g):
    return lambda x: f(g(x))

# Définition de deux fonctions lambda
square = lambda x: x ** 2       # Élévation au carré
double = lambda x: x * 2        # Multiplication par 2

# Composition des fonctions
double_then_square = compose(square, double)  # (2x)^2
square_then_double = compose(double, square)  # 2(x^2)

# Tests
print(double_then_square(3))  # 36
print(square_then_double(3))  # 18
print(double_then_square(4))  # 64
print(square_then_double(4))  # 32


# ========================
# Exercice 6 : Filtrage et transformation
# ========================

# Fonction qui filtre et transforme une liste
def filterMap(filter_func, transform_func, lst):
    return [transform_func(x) for x in lst if filter_func(x)]

# Liste de mots avec certaines chaînes vides
words = ["hello", "", "world", "python", "", "lambda"]

# Définition des fonctions de filtrage et transformation
is_not_empty = lambda x: x != ""  # Supprime les chaînes vides
to_upper = lambda x: x.upper()    # Convertit en majuscules

# Application de filterMap
filtered_transformed_words = filterMap(is_not_empty, to_upper, words)

# Test
print(filtered_transformed_words)  # ['HELLO', 'WORLD', 'PYTHON', 'LAMBDA']


# ========================
# Exercice 7 : Mémorisation des résultats (Clôtures avancées)
# ========================

# Fonction de mémorisation qui stocke les résultats précédents
def memoize(func):
    cache = {}  # Dictionnaire pour stocker les résultats

    def memorized_func(n):
        if n in cache:
            return cache[n]  # Retourne la valeur si déjà calculée
        result = func(n)  # Sinon, calcule la valeur
        cache[n] = result  # Stocke la valeur pour les futurs appels
        return result

    return memorized_func

# Fonction factorielle récursive
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

# Fonction Fibonacci récursive
def fibonacci(n):
    return n if n <= 1 else fibonacci(n - 1) + fibonacci(n - 2)

# Mémorisation des fonctions
memoized_factorial = memoize(factorial)
memoized_fibonacci = memoize(fibonacci)

# Fonction pour mesurer le temps d'exécution
def measure_time(func, n):
    start_time = time.time()
    result = func(n)
    end_time = time.time()
    print(f"Résultat: {result}, Temps d'exécution: {end_time - start_time:.6f} sec")

# Tests
print("Factorielle de 10 :")
measure_time(memoized_factorial, 10)

print("\nFibonacci de 35 :")
measure_time(memoized_fibonacci, 35)

print("\nFibonacci de 35 (avec cache) :")
measure_time(memoized_fibonacci, 35)  # Devrait être beaucoup plus rapide !


# ========================
# Exercice 8 : Calcul de réductions
# ========================

# Fonction qui applique une réduction et retourne le montant total après réduction
def calculateDiscount(prices, discount_func):
    discounted_prices = list(map(discount_func, prices))
    return sum(discounted_prices)

# Liste des prix des produits
product_prices = [100, 200, 50, 75, 150]

# Fonction lambda pour appliquer une réduction de 20%
discount_20 = lambda price: price * 0.8  

# Calcul du montant total après réduction
total_after_discount = calculateDiscount(product_prices, discount_20)

# Affichage du résultat
print(f"Montant total après réduction : {total_after_discount:.2f}")  # 460.00
