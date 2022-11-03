thiscar = {
    "brand": "bmw",
    "model": "car",
    "color": ["red", "blue", "pink"],
    "year": 2022
}
print(type(thiscar))
print()
# to print the dictionary
print(thiscar)
print()
# To access and change the value
thiscar["model"] = "cycle"
print(thiscar)
#for loop through the dictionary

for model in thiscar:
    print(thiscar[model])