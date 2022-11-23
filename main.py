import requests
from pprint import pprint
import json
import datetime

token = "TOKEN "
URL = 'https://api.vk.com/method/account.getProfileInfo'
params = {
    'access_token': token,
    'v': '5.131'
}
res_1 = requests.get(URL, params=params)
pprint(res_1.json())
res_2 = res_1.json()
personal_id = str(res_2['response']['id'])
# print(res_2)

URL = 'https://api.vk.com/method/photos.get'
params = {
    'owner_id': f'{personal_id}',
    'album_id': 'wall',
    'extended': 1,
    'photo_sizes': 1,
    'access_token': token,
    'v': '5.131'
}
res = requests.get(URL, params=params)
result = res.json()
foto_list = result['response']['items']
# print(result)

def time_convert(time_unix):
    time_bc = datetime.datetime.fromtimestamp(time_unix)
    str_time = time_bc.strftime('%Y-%m-%d time %H-%M-%S')
    return str_time


# ссылка на максимальный файл.
def geting_fotos_links(list_of_size):
    links_of_foto = ''
    max_size_foto = 0
    for any_foto in list_of_size:
        if any_foto['height'] > max_size_foto:
            max_size_foto = any_foto['height']
            links_of_foto = any_foto['url']
    return links_of_foto


# Получаем размеры файла
def geting_max_size_foto(list_of_size):
    size_of_foto = ''
    max_size_foto = 0
    for any_foto in list_of_size:
        if any_foto['height'] > max_size_foto:
            max_size_foto = any_foto['height']
            max_size_foto_2 = any_foto['width']
            size_of_foto = f'h={max_size_foto} X  w={max_size_foto_2}'
    return size_of_foto


# Получаем название файла.
def making_info_for_foto(any_foto):
    count_likes = any_foto['likes']['count']
    date_foto = any_foto['date']
    name_of_file = f'{count_likes} {date_foto}'
    size_of_file = geting_max_size_foto(any_foto['sizes'])
    any_foto_info = {"file_name": name_of_file, "size": size_of_file}
    return any_foto_info


result_for_every_foto = []
some_fotos_links = []
for foto_in_list in foto_list:
    result_for_every_foto.append(making_info_for_foto(foto_in_list))
    some_fotos_links.append(geting_fotos_links(foto_in_list['sizes']))

pprint(result_for_every_foto)  # печать файла с результатами
pprint(some_fotos_links)  # печать ссылок фото


class YaUploader:  # Класс записи объекта на диск яндекса
    def __init__(self, token_ya: str):
        self.token_ya = token_yandex

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token_ya)
        }

    def get_upload_file(self, file_link, disk_file_path):
        headers = self.get_headers()
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        params = {"url": file_link, "path": disk_file_path, "overwrite": False}
        r = requests.post(url=upload_url, params=params, headers=headers)
        res = r.json()
        pprint(res)


token_ya = 'token_yandex'
putloader = YaUploader(token_ya)
index = 0
name_foto = ''
for one_foto in some_fotos_links:  # запись фото на яндекс диск
    n_foto = one_foto
    name_foto = result_for_every_foto[index]['file_name']
    path_yandex = f'/photo/{name_foto}'
    putloader.get_upload_file(n_foto, path_yandex)
    index += 1

with open('result_file.json', 'w') as f:  # Запись результа в корневой каталог файла .
    json.dump(result_for_every_foto, f, indent=2)
