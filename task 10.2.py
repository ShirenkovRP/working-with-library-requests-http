# У Яндекс.Диска есть очень удобное и простое API. Для описания всех его методов
# существует Полигон. Нужно написать программу, которая принимает на вход путь до
# файла на компьютере и сохраняет на Яндекс.Диск с таким же именем.
# Все ответы приходят в формате json;
# Загрузка файла по ссылке происходит с помощью метода put и передачи туда данных;
# Токен можно получить кликнув на полигоне на кнопку "Получить OAuth-токен".

import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        HEADERS = {"Authorization": f"OAuth {self.token}"}
        file_name = file_path.split("\\")[-1]
        """Метод загруджает файл file_path на яндекс диск"""
        resp1 = requests.get(
                "https://cloud-api.yandex.net/v1/disk/resources/upload",
                params={"path": file_name, "overwrite": "true"},
                headers=HEADERS
                )
        resp1.raise_for_status()
        d = resp1.json()
        href = d["href"]
        with open(file_path, "rb") as f:
            resp2 = requests.put(href, files={"file": f})
        resp2.raise_for_status()
        return 'Вернуть ответ об успешной загрузке'


if __name__ == '__main__':  
    uploader = YaUploader('<Your Yandex Disk token>')
    result = uploader.upload(r"C:\Users\Ширенков Роман\Pictures\i30.jpg")
    print(result)
