import json
file = open("pokemon_full.json")
str_json = file.read()
L = len(str_json)
print("Общее количество символов в файле равно", L)
file.close()

file = open("pokemon_full.json")
str_correct = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" # Создаем строку символов, которые мы будем считать.
lines = file.readlines()
f = ""
counter = 0
for line in lines:
    f += line
for i in f:
    if i in str_correct: # Если символ содержится в str_correct, то считаем его.
        counter += 1
print("Общее количесто символов без пробелов и знаков препинания равно", counter)
file.close()

data = json.loads(str_json) # Чтобы преобразовать строки json в объекты Python, используем функцию json.loads()
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
