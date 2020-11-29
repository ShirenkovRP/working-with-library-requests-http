# Самый важный сайт для программистов это stackoverflow. И у него тоже есть API
# Нужно написать программу, которая выводит все вопросы за последние два дня и
# содержит тэг 'Python'. Для этого задания токен не требуется.

import requests


resp = requests.get("https://api.stackexchange.com/2.2/questions",
                    {"fromdate": "1606435200",
                        "todate": "1606608000",
                        "order": "desc",
                        "sort": "activity",
                        "tagged": "python",
                        "site": "stackoverflow"}
                    )

resp.raise_for_status()
posts = resp.json()["items"]
for ques in posts:
    print(ques["title"])
