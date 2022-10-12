information = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": ["Amancio", "Ortega", "Gaona"],
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}
print(information)

information["number_stores"] = 2

print("Les clients de Zara sont ceux qui veulant faire des achats pour : ", information["type_of_clothes"])

information["country_creation"] = "Spain"

if information["international_competitors"] :
    information["international_competitors"].append("Desigual")

del information["creation_date"]

print(information["international_competitors"][-1])

print(information["major_color"]["US"])

print(len(information.keys()))

print(information.keys())

more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
}

information.update(more_on_zara)

print(information["number_stores"])
#une mise à jour va s'effectuer