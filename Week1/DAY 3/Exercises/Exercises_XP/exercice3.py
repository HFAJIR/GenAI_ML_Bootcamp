
# 1. Create the brand dictionary
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red", 
        "US": ["pink", "green"]
    }
}

# 2. Change the number of stores to 2
brand["number_stores"] = 2
# 3. Print a sentence describing Zara's clients
print(f"Zara's clients are {', '.join(brand['type_of_clothes'])}.")
# 4. Add a key for country creation with the value "Spain"
brand["country_creation"] = "Spain"
# 5. Check if international_competitors exists and add "Desigual"
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
# 6. Delete the creation_date key
brand.pop("creation_date")
# 7. Print the last international competitor
print("Last international competitor:", brand["international_competitors"][-1])
# 8. Print the major colors in the US
print("Major colors in the US:", ', '.join(brand["major_color"]["US"]))
# 9. Print the number of keys in the dictionary
print("Number of keys in the brand dictionary:", len(brand))
# 10. Print the keys of the dictionary  
print("Keys in the brand dictionary:", list(brand.keys()))

print("___"*10)

print(brand)