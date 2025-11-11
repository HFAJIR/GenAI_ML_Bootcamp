import random

# Génération des données
list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
target_number = 3728
# --- Solution optimisée ---
seen = set()  
pairs = set()  

for num in list_of_numbers:
    complement = target_number - num
    if complement in seen:
        # on trie la paire pour éviter les doublons dans l'autre sens
        pair = tuple(sorted((num, complement)))
        pairs.add(pair)
    seen.add(num)
print(f"Nombre de paires trouvées : {len(pairs)}\n")
for a, b in pairs:
    print(f"{a} et {b} somment à {target_number}")
