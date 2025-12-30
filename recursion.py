"""
Module d'implémentation des algorithmes récursifs.
Contient des fonctions récursives classiques et des algorithmes de tri/réecherche récursifs.
"""

def factorial(n):
    """
    Calcule la factorielle d'un nombre n (n!).
    
    Principe : n! = n * (n-1) * ... * 1, avec 0! = 1.
    Complexité temporelle : O(n).
    Complexité spatiale : O(n) à cause de la pile d'appels.
    
    Args:
        n (int): Nombre entier non négatif.
    
    Returns:
        int: Factorielle de n.
    
    Raises:
        ValueError: Si n est négatif.
    """
    if n < 0:
        raise ValueError("La factorielle n'est définie que pour les nombres non négatifs.")
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    """
    Calcule le n-ième terme de la suite de Fibonacci.
    
    Principe : F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2).
    Complexité temporelle : O(2^n) (exponentielle).
    Complexité spatiale : O(n) à cause de la pile d'appels.
    
    Args:
        n (int): Position dans la suite de Fibonacci (n ≥ 0).
    
    Returns:
        int: Le n-ième terme de la suite de Fibonacci.
    """
    if n < 0:
        raise ValueError("n doit être un entier non négatif")
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def array_sum(arr):
    """
    Calcule la somme des éléments d'un tableau de manière récursive.
    
    Principe : Somme du premier élément et de la somme du reste du tableau.
    Complexité temporelle : O(n).
    Complexité spatiale : O(n) à cause de la pile d'appels.
    
    Args:
        arr (list): Liste de nombres.
    
    Returns:
        int/float: Somme des éléments.
    """
    if not arr:
        return 0
    return arr[0] + array_sum(arr[1:])


def recursive_binary_search(arr, target, left=0, right=None):
    """
    Recherche un élément dans un tableau TRIÉ en utilisant l'algorithme de recherche binaire récursif.
    
    Principe : Divise récursivement l'intervalle de recherche par deux.
    Complexité temporelle : O(log n).
    Complexité spatiale : O(log n) à cause de la pile d'appels.
    
    Args:
        arr (list): Liste TRIÉE dans laquelle rechercher.
        target: Élément à rechercher.
        left (int): Index de début de la recherche (utilisé pour la récursivité).
        right (int): Index de fin de la recherche (utilisé pour la récursivité).
    
    Returns:
        int: Index de l'élément trouvé, ou -1 si non trouvé.
    """
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = left + (right - left) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return recursive_binary_search(arr, target, mid + 1, right)
    else:
        return recursive_binary_search(arr, target, left, mid - 1)


def merge_sort(arr):
    """
    Trie un tableau en utilisant l'algorithme Merge Sort (récursif).
    
    Principe : Divise le tableau en deux moitiés, trie chaque moitié récursivement,
    puis fusionne les deux moitiés triées.
    Complexité temporelle : O(n log n) dans tous les cas.
    Complexité spatiale : O(n) pour le tableau temporaire.
    
    Args:
        arr (list): Liste d'éléments comparables à trier.
    
    Returns:
        list: Liste triée.
    """
    if len(arr) <= 1:
        return arr
    
    # Division
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Appels récursifs
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    
    # Fusion
    return _merge(left_sorted, right_sorted)


def _merge(left, right):
    """
    Fusionne deux listes triées en une seule liste triée.
    
    Args:
        left (list): Première liste triée.
        right (list): Deuxième liste triée.
    
    Returns:
        list: Liste fusionnée et triée.
    """
    merged = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    # Ajoute les éléments restants
    merged.extend(left[i:])
    merged.extend(right[j:])
    
    return merged