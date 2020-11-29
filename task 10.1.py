# Кто самый умный супергерой? Есть API по информации о супергероях.
# Нужно определить кто самый умный(intelligence) из трех супергероев- Hulk,
# Captain America, Thanos. Для определения id нужно использовать
# метод /search/name

import requests

my_dict = {}
name_list = ["Hulk", "Captain America", "Thanos"]
for name in name_list:
    response = requests.get(
            f"https://superheroapi.com/api/2619421814940190/search/{name}")
    if response.status_code != 200:
        raise Exception("всё очень плохо")
    posts = response.json()["results"]    
    for i in posts:
        if i["name"] == name:
            for power, vol in i["powerstats"].items():
                if power == "intelligence":                    
                    my_dict[name] = int(vol)

max_powerstats = max(my_dict, key=my_dict.get)

print(f"Самый умный герой {max_powerstats}")
