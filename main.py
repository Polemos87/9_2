import requests
import os

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        headers = {
            'accept': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }
        url = requests.get("https://cloud-api.yandex.net:443/v1/disk/resources/upload", params={f'path': {name_file}}, headers=headers)
        upload_url = url.json()["href"]
        requests.put(upload_url, headers=headers, files={'file': open(file_path, "rb")})

if __name__ == '__main__':
    token = ''
    uploader = YaUploader(token)
    file_path = input("Введите путь:")

    with open(file_path) as file:
        name_file = os.path.basename(file_path)

    uploader.upload(file_path)

