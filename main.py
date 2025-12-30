"""
Module principal du CLI AlgoPlayground.
Fournit une interface interactive pour tester les algorithmes.
"""

import random
import time
import sys

# Import des modules d'algorithmes
from sorting import bubble_sort, insertion_sort, quick_sort
from searching import linear_search, binary_search
from recursion import factorial, fibonacci, array_sum, recursive_binary_search, merge_sort


def generate_random_list(size, min_val=0, max_val=100):
    """
    Génère une liste de nombres aléatoires.
    
    Args:
        size (int): Taille de la liste.
        min_val (int): Valeur minimale.
        max_val (int): Valeur maximale.
    
    Returns:
        list: Liste de nombres aléatoires.
    """
    return [random.randint(min_val, max_val) for _ in range(size)]


def display_menu():
    """
    Affiche le menu principal du programme.
    """
    print("\n" + "="*50)
    print("           ALGO PLAYGROUND - MENU PRINCIPAL")
    print("="*50)
    print("1. Algorithmes de Tri")
    print("2. Algorithmes de Recherche")
    print("3. Algorithmes Récursifs")
    print("4. Comparaison de performances")
    print("5. Quitter")
    print("="*50)


def display_sorting_menu():
    """
    Affiche le menu des algorithmes de tri.
    """
    print("\n" + "-"*40)
    print("           ALGORITHMES DE TRI")
    print("-"*40)
    print("1. Bubble Sort")
    print("2. Insertion Sort")
    print("3. Quick Sort (itératif)")
    print("4. Merge Sort (récursif)")
    print("5. Retour au menu principal")
    print("-"*40)


def display_searching_menu():
    """
    Affiche le menu des algorithmes de recherche.
    """
    print("\n" + "-"*40)
    print("        ALGORITHMES DE RECHERCHE")
    print("-"*40)
    print("1. Recherche Linéaire")
    print("2. Recherche Binaire (itératif)")
    print("3. Recherche Binaire (récursif)")
    print("4. Retour au menu principal")
    print("-"*40)


def display_recursion_menu():
    """
    Affiche le menu des algorithmes récursifs.
    """
    print("\n" + "-"*40)
    print("        ALGORITHMES RÉCURSIFS")
    print("-"*40)
    print("1. Factorielle")
    print("2. Suite de Fibonacci")
    print("3. Somme d'un tableau")
    print("4. Retour au menu principal")
    print("-"*40)


def test_sorting_algorithm():
    """
    Interface pour tester les algorithmes de tri.
    """
    display_sorting_menu()
    
    while True:
        try:
            choice = int(input("\nChoisissez un algorithme (1-5): "))
            
            if choice == 5:
                return
            
            if choice not in [1, 2, 3, 4]:
                print("Choix invalide. Veuillez choisir entre 1 et 5.")
                continue
            
            # Génération de la liste
            try:
                size = int(input("Taille de la liste (ex: 10): "))
                if size <= 0:
                    print("La taille doit être positive.")
                    continue
            except ValueError:
                print("Veuillez entrer un nombre entier valide.")
                continue
            
            original_list = generate_random_list(size)
            print(f"\nListe originale : {original_list}")
            
            # Copie de la liste pour le tri
            list_to_sort = original_list.copy()
            
            # Exécution de l'algorithme avec mesure du temps
            start_time = time.time()
            
            if choice == 1:
                sorted_list = bubble_sort(list_to_sort)
                algo_name = "Bubble Sort"
            elif choice == 2:
                sorted_list = insertion_sort(list_to_sort)
                algo_name = "Insertion Sort"
            elif choice == 3:
                sorted_list = quick_sort(list_to_sort)
                algo_name = "Quick Sort"
            elif choice == 4:
                sorted_list = merge_sort(list_to_sort)
                algo_name = "Merge Sort"
            
            end_time = time.time()
            
            # Affichage des résultats
            print(f"\nAlgorithme utilisé : {algo_name}")
            print(f"Liste triée : {sorted_list}")
            print(f"Temps d'exécution : {end_time - start_time:.6f} secondes")
            
            # Vérification que la liste est bien triée
            is_sorted = all(sorted_list[i] <= sorted_list[i+1] for i in range(len(sorted_list)-1))
            print(f"Liste correctement triée : {'Oui' if is_sorted else 'Non'}")
            
        except ValueError:
            print("Veuillez entrer un nombre valide.")
        except Exception as e:
            print(f"Une erreur est survenue : {e}")


def test_searching_algorithm():
    """
    Interface pour tester les algorithmes de recherche.
    """
    display_searching_menu()
    
    while True:
        try:
            choice = int(input("\nChoisissez un algorithme (1-4): "))
            
            if choice == 4:
                return
            
            if choice not in [1, 2, 3]:
                print("Choix invalide. Veuillez choisir entre 1 et 4.")
                continue
            
            # Génération et tri de la liste (si nécessaire pour la recherche binaire)
            try:
                size = int(input("Taille de la liste (ex: 10): "))
                if size <= 0:
                    print("La taille doit être positive.")
                    continue
            except ValueError:
                print("Veuillez entrer un nombre entier valide.")
                continue
            
            original_list = generate_random_list(size)
            
            if choice in [2, 3]:  # Recherche binaire nécessite une liste triée
                original_list.sort()
                print(f"\nListe triée : {original_list}")
            else:
                print(f"\nListe : {original_list}")
            
            # Choix de la valeur à rechercher
            try:
                target = int(input("Valeur à rechercher : "))
            except ValueError:
                print("Veuillez entrer un nombre valide.")
                continue
            
            # Exécution de l'algorithme avec mesure du temps
            start_time = time.time()
            
            if choice == 1:
                result = linear_search(original_list, target)
                algo_name = "Recherche Linéaire"
            elif choice == 2:
                result = binary_search(original_list, target)
                algo_name = "Recherche Binaire (itératif)"
            elif choice == 3:
                result = recursive_binary_search(original_list, target)
                algo_name = "Recherche Binaire (récursif)"
            
            end_time = time.time()
            
            # Affichage des résultats
            print(f"\nAlgorithme utilisé : {algo_name}")
            print(f"Valeur recherchée : {target}")
            if result != -1:
                print(f"Résultat : Trouvé à l'index {result}")
                print(f"Vérification : original_list[{result}] = {original_list[result]}")
            else:
                print(f"Résultat : Non trouvé")
            print(f"Temps d'exécution : {end_time - start_time:.6f} secondes")
            
        except ValueError:
            print("Veuillez entrer un nombre valide.")
        except Exception as e:
            print(f"Une erreur est survenue : {e}")


def test_recursion_algorithm():
    """
    Interface pour tester les algorithmes récursifs.
    """
    display_recursion_menu()
    
    while True:
        try:
            choice = int(input("\nChoisissez un algorithme (1-4): "))
            
            if choice == 4:
                return
            
            if choice not in [1, 2, 3]:
                print("Choix invalide. Veuillez choisir entre 1 et 4.")
                continue
            
            if choice == 1:  # Factorielle
                try:
                    n = int(input("Entrez un nombre entier non négatif : "))
                    if n < 0:
                        print("La factorielle n'est définie que pour les nombres non négatifs.")
                        continue
                    
                    start_time = time.time()
                    result = factorial(n)
                    end_time = time.time()
                    
                    print(f"\nAlgorithme : Factorielle")
                    print(f"Entrée : {n}")
                    print(f"Résultat : {n}! = {result}")
                    print(f"Temps d'exécution : {end_time - start_time:.6f} secondes")
                    
                except ValueError as e:
                    print(f"Erreur : {e}")
                except RecursionError:
                    print("Erreur : Profondeur de récursion dépassée. Essayez avec un nombre plus petit.")
            
            elif choice == 2:  # Fibonacci
                try:
                    n = int(input("Entrez la position dans la suite de Fibonacci (n ≥ 0) : "))
                    if n < 0:
                        print("n doit être un entier non négatif.")
                        continue
                    
                    start_time = time.time()
                    result = fibonacci(n)
                    end_time = time.time()
                    
                    print(f"\nAlgorithme : Suite de Fibonacci")
                    print(f"Entrée : position {n}")
                    print(f"Résultat : F({n}) = {result}")
                    print(f"Temps d'exécution : {end_time - start_time:.6f} secondes")
                    
                    # Avertissement pour les grandes valeurs de n
                    if n > 35:
                        print("\n⚠️  Attention : L'algorithme récursif de Fibonacci a une complexité exponentielle.")
                        print("   Pour n > 35, les temps d'exécution peuvent devenir très longs.")
                    
                except ValueError as e:
                    print(f"Erreur : {e}")
                except RecursionError:
                    print("Erreur : Profondeur de récursion dépassée. Essayez avec un nombre plus petit.")
            
            elif choice == 3:  # Somme d'un tableau
                try:
                    size = int(input("Taille du tableau (ex: 10) : "))
                    if size <= 0:
                        print("La taille doit être positive.")
                        continue
                    
                    arr = generate_random_list(size, 1, 100)
                    print(f"\nTableau généré : {arr}")
                    
                    start_time = time.time()
                    result = array_sum(arr)
                    end_time = time.time()
                    
                    # Vérification avec la fonction sum() de Python
                    verification = sum(arr)
                    
                    print(f"\nAlgorithme : Somme récursive d'un tableau")
                    print(f"Tableau : {arr}")
                    print(f"Résultat récursif : {result}")
                    print(f"Vérification (sum()) : {verification}")
                    print(f"Correspondance : {'Oui' if result == verification else 'Non'}")
                    print(f"Temps d'exécution : {end_time - start_time:.6f} secondes")
                    
                except ValueError:
                    print("Veuillez entrer un nombre valide.")
                except RecursionError:
                    print("Erreur : Profondeur de récursion dépassée. Essayez avec une taille plus petite.")
            
        except ValueError:
            print("Veuillez entrer un nombre valide.")
        except Exception as e:
            print(f"Une erreur est survenue : {e}")


def compare_performances():
    """
    Compare les performances des différents algorithmes de tri.
    """
    print("\n" + "="*60)
    print("          COMPARAISON DES PERFORMANCES DE TRI")
    print("="*60)
    
    try:
        size = int(input("Taille de la liste pour la comparaison (ex: 100) : "))
        if size <= 0:
            print("La taille doit être positive.")
            return
    except ValueError:
        print("Veuillez entrer un nombre entier valide.")
        return
    
    # Génération de la liste
    print(f"\nGénération d'une liste de {size} éléments aléatoires...")
    original_list = generate_random_list(size, 0, 10000)
    
    # Liste des algorithmes à comparer
    algorithms = [
        ("Bubble Sort", bubble_sort),
        ("Insertion Sort", insertion_sort),
        ("Quick Sort", quick_sort),
        ("Merge Sort", merge_sort),
    ]
    
    print(f"\nComparaison en cours...")
    print("-"*60)
    print(f"{'Algorithme':<20} {'Temps (s)':<15} {'Liste triée?'}")
    print("-"*60)
    
    results = []
    
    for algo_name, algo_func in algorithms:
        # Copie de la liste pour chaque algorithme
        list_copy = original_list.copy()
        
        # Mesure du temps d'exécution
        start_time = time.time()
        sorted_list = algo_func(list_copy)
        end_time = time.time()
        
        execution_time = end_time - start_time
        
        # Vérification que la liste est bien triée
        is_sorted = all(sorted_list[i] <= sorted_list[i+1] for i in range(len(sorted_list)-1))
        
        results.append((algo_name, execution_time, is_sorted))
        
        print(f"{algo_name:<20} {execution_time:<15.6f} {'Oui' if is_sorted else 'Non'}")
    
    print("-"*60)
    
    # Trouver l'algorithme le plus rapide
    fastest = min(results, key=lambda x: x[1])
    print(f"\n🎯 L'algorithme le plus rapide est '{fastest[0]}' avec {fastest[1]:.6f} secondes")
    
    # Avertissement pour les grandes tailles avec Bubble Sort
    if size > 1000:
        bubble_time = next(r[1] for r in results if r[0] == "Bubble Sort")
        print(f"\n⚠️  Note : Bubble Sort devient très lent pour n > 1000")
        print(f"   Temps Bubble Sort: {bubble_time:.3f}s vs Quick Sort: {fastest[1]:.6f}s")


def main():
    """
    Fonction principale du programme.
    """
    print("="*60)
    print("       BIENVENUE DANS ALGO PLAYGROUND")
    print("="*60)
    print("Une boîte à outils pour expérimenter avec les algorithmes")
    print("Version 1.0 - Développé en Python")
    
    while True:
        display_menu()
        
        try:
            choice = int(input("\nChoisissez une option (1-5): "))
            
            if choice == 1:
                test_sorting_algorithm()
            elif choice == 2:
                test_searching_algorithm()
            elif choice == 3:
                test_recursion_algorithm()
            elif choice == 4:
                compare_performances()
            elif choice == 5:
                print("\nMerci d'avoir utilisé AlgoPlayground ! À bientôt !")
                sys.exit(0)
            else:
                print("Choix invalide. Veuillez choisir entre 1 et 5.")
                
        except ValueError:
            print("Veuillez entrer un nombre valide.")
        except KeyboardInterrupt:
            print("\n\nInterruption par l'utilisateur. Au revoir !")
            sys.exit(0)
        except Exception as e:
            print(f"Une erreur inattendue est survenue : {e}")


if __name__ == "__main__":
    main()