# diplom_work
Задание к итоговой работе:
Возможна такая ситуация, что мы хотим показать друзьям фотографии из социальных сетей, но соц. сети могут быть недоступны по каким-либо причинам. Давайте защитимся от такого.
Нужно написать программу для резервного копирования фотографий с профиля (аватарок) пользователя VK в облачное хранилище Яндекс.Диск.
Для названий фотографий использовать количество лайков, если количество лайков одинаково, то добавить дату загрузки.
Информацию по сохраненным фотографиям сохранить в json-файл.

Задача:
Нужно написать программу, которая будет:

Получать фотографии с профиля. Для этого нужно использовать метод photos.get.
Сохранять фотографии максимального размера (ширина/высота в пикселях) на Я.Диске.
Для имени фотографий использовать количество лайков.
Сохранять информацию по фотографиям в json-файл с результатами.
Обратите внимание: токен для ВК можно получить выполнив инструкцию.

Входные данные:
Пользователь вводит:

id пользователя VK;
токен с Полигона Яндекс.Диска. Важно: Токен публиковать в github не нужно!
Выходные данные:
json-файл с информацией по файлу:
1
2
3
4
    [{
    "file_name": "34.jpg",
    "size": "z"
    }]
Измененный Я.Диск, куда добавились фотографии.
Обязательные требования к программе:
Использовать REST API Я.Диска и ключ, полученный с полигона.
Для загруженных фотографий нужно создать свою папку.
Сохранять указанное количество фотографий(по умолчанию 5) наибольшего размера (ширина/высота в пикселях) на Я.Диске
Сделать прогресс-бар или логирование для отслеживания процесса программы.
Код программы должен удовлетворять PEP8.
У программы должен быть свой отдельный репозиторий.
Все зависимости должны быть указаны в файле requiremеnts.txt.​
