from datetime import datetime
maintenant = datetime.now()
date_actuelle = maintenant.date()
print("Date actuelle :", date_actuelle)
next_year = date_actuelle.year + 1

print("Next year :", next_year)

intial_date = datetime(next_year, 1, 1).date()

print("Initial date of next year :", intial_date)

difference = intial_date - date_actuelle

print("difference :", difference.days, "jours")