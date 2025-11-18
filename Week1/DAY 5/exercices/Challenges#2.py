# Draw the following pattern using for loops:
""" 
  *
 ***
*****"""

lines = 3
for i in range(lines):
    # spaces decreasing
    for j in range(lines - i - 1):
        print(" ", end="")
    # stars increasing by 2
    for k in range(2 * i + 1):
        print("*", end="")
    print()  # nouvelle ligne

lines = 5
for i in range(lines):
    for j in range(lines - i - 1):
        print(" ", end="")
    for k in range(i + 1):
        print("*", end="")
    print()

lines = 5
# partie croissante
for i in range(lines):
    print("*" * (i + 1))

# partie décroissante
for i in range(lines, 0, -1):
    print(" " * (lines - i) + "*" * i)

# exercice 2 :

my_list = [2, 24, 12, 354, 233]  # tri par sélection
for i in range(len(my_list) - 1):  # i va de 0 à 3
    minimum = i   # on suppose que le minimum est à l'indice i
    for j in range( i + 1, len(my_list)): # deuxieme boucle pour trouver le minimum
        if(my_list[j] < my_list[minimum]): # comparer les éléments
            minimum = j # mettre à jour l'indice du minimum
            if(minimum != i): # échanger les éléments
                my_list[i], my_list[minimum] = my_list[minimum], my_list[i] # echange
print(my_list) # [2, 12, 24, 233, 354]
