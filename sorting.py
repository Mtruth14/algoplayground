"""
Module d'implémentation des algorithmes de tri.
Contient les versions itératives de plusieurs algorithmes classiques.
"""

def bubble_sort(arr):
    """
    Trie un tableau en utilisant l'algorithme Bubble Sort.
    
    Principe : Compare et échange les éléments adjacents s'ils sont dans le mauvais ordre.
    Complexité temporelle : O(n²) dans le pire cas et en moyenne, O(n) dans le meilleur cas.
    Complexité spatiale : O(1) (tri en place).
    
    Args:
        arr (list): Liste d'éléments comparables à trier.
    
    Returns:
        list: Liste triée.
    """
    n = len(arr)
    for i in range(n):
        # Drapeau pour optimisation
        swapped = False
        
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Échange les éléments
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        # Si aucun échange n'a été fait, le tableau est déjà trié
        if not swapped:
            break
    
    return arr


def insertion_sort(arr):
    """
    Trie un tableau en utilisant l'algorithme Insertion Sort.
    
    Principe : Construit le tableau trié un élément à la fois en insérant
    chaque élément à sa position correcte.
    Complexité temporelle : O(n²) dans le pire cas et en moyenne, O(n) dans le meilleur cas.
    Complexité spatiale : O(1) (tri en place).
    
    Args:
        arr (list): Liste d'éléments comparables à trier.
    
    Returns:
        list: Liste triée.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Déplace les éléments plus grands que key vers la droite
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Insère key à la bonne position
        arr[j + 1] = key
    
    return arr


def quick_sort(arr):
    """
    Trie un tableau en utilisant l'algorithme Quick Sort (version itérative).
    
    Principe : Utilise une approche "diviser pour régner" avec un élément pivot.
    Complexité temporelle : O(n log n) en moyenne, O(n²) dans le pire cas.
    Complexité spatiale : O(log n) pour la pile d'appels (dans cette version itérative).
    
    Args:
        arr (list): Liste d'éléments comparables à trier.
    
    Returns:
        list: Liste triée.
    """
    if len(arr) <= 1:
        return arr
    
    # Utilisation d'une pile pour simuler la récursivité
    stack = [(0, len(arr) - 1)]
    
    while stack:
        low, high = stack.pop()
        
        if low < high:
            # Partitionnement
            pivot = arr[high]
            i = low - 1
            
            for j in range(low, high):
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            
            # Place le pivot à sa position finale
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            pivot_index = i + 1
            
            # Ajoute les sous-tableaux à traiter à la pile
            stack.append((low, pivot_index - 1))
            stack.append((pivot_index + 1, high))
    
    return arr