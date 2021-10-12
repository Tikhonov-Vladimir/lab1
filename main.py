import json

file = open("pokemon_full.json")
str_pokemon = file.read()
len_str = len(str_pokemon)
print("Общее количество символов в файле равно", len_str)
file.close()

counter = 0
for symbol in str_pokemon:
    if symbol.isalnum():
        counter += 1
print("Общее количесто символов без пробелов и знаков препинания равно", counter)

objects = json.loads(str_pokemon)
max_desc = 0
poke_name = ""
for profile in objects:
    desc = profile["description"]
    if len(desc) > max_desc:
        max_desc = len(desc)
        poke_name = profile["name"]
print("У покемона", poke_name, "наиболее длинное описание")

max_words = 0
abilities = ""
for profile in objects:
    for skills in profile["abilities"]:
        if len(skills.split()) > max_words:
            max_words = len(skills.split())
            abilities = skills
print("Умение", abilities, "содержит больше всего слов")
