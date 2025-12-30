"""
Module d'implémentation des algorithmes de recherche.
Contient les versions itératives des algorithmes de recherche.
"""

def linear_search(arr, target):
    """
    Recherche un élément dans un tableau en utilisant l'algorithme de recherche linéaire.
    
    Principe : Parcours séquentiel de tous les éléments jusqu'à trouver la cible.
    Complexité temporelle : O(n) dans le pire cas, O(1) dans le meilleur cas.
    Complexité spatiale : O(1).
    
    Args:
        arr (list): Liste dans laquelle rechercher.
        target: Élément à rechercher.
    
    Returns:
        int: Index de l'élément trouvé, ou -1 si non trouvé.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def binary_search(arr, target):
    """
    Recherche un élément dans un tableau TRIÉ en utilisant l'algorithme de recherche binaire (itératif).
    
    Principe : Divise récursivement l'intervalle de recherche par deux.
    Complexité temporelle : O(log n).
    Complexité spatiale : O(1) (version itérative).
    
    Args:
        arr (list): Liste TRIÉE dans laquelle rechercher.
        target: Élément à rechercher.
    
    Returns:
        int: Index de l'élément trouvé, ou -1 si non trouvé.
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1