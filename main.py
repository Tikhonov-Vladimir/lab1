import json

file = open("pokemon_full.json")
str_json = file.read()
len_str = len(str_json)
print("Общее количество символов в файле равно", len_str)
file.close()

file = open("pokemon_full.json")
counter = 0
for i in str_json:
    if i.isalnum() is True:
        counter += 1
print("Общее количесто символов без пробелов и знаков препинания равно", counter)
file.close()

data = json.loads(str_json)
max_desc = 0
poke_name = ""
for profile in data:
    desc = profile["description"]
    if len(desc) > max_desc:
        max_desc = len(desc)
        poke_name = profile["name"]
print("У покемона", poke_name, "наиболее длинное описание")

max_words = 0
abilities = ""
for profile in data:
    for skills in profile["abilities"]:
        if len(skills.split()) > max_words:
            max_words = len(skills.split())
            abilities = skills
print("Умение", abilities, "содержит больше всего слов")
