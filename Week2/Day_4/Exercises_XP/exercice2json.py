
import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

# Étape 1: Charger la chaîne JSON en dictionnaire Python
data = json.loads(sampleJson)

# Étape 2: Accéder à la clé "salary"
salary = data["company"]["employee"]["payable"]["salary"]
print("Salary:", salary)

# Étape 3: Ajouter la clé "birth_date" à l'intérieur de "employee"
data["company"]["employee"]["birth_date"] = "1990-05-15"  
print("Modified JSON:", data)

# Étape 4: Sauvegarder le JSON modifié dans un fichier
with open("modified_employee.json", "w") as file:
    json.dump(data, file, indent=4)

print("Modified JSON saved to 'modified_employee.json'")