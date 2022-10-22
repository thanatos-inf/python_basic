# Создать загрузчик видео с YouTube (в видео и аудио версиях)

import pytube
from pytube import YouTube

vid = YouTube('https://www.youtube.com/watch?v=w8iTD4CaHCk&list=RDw8iTD4CaHCk&start_radio=1&ab_channel=AvrilLavigneVEVO')

# url_vid = input('Введите ссылку для скачивания видеоролика: ')
# vid = YouTube(url_vid)

print('Название: ', vid.title)
print('Количество просмотров: ', vid.views)
print('Длительность: ', vid.length, 'seconds')
print('Описание: ', vid.description)


streams = vid.streams

video_720 = streams.filter(res='720p').desc().first()
audio_best = streams.filter(only_audio=True).desc().first()

video_720.download()
audio_best.download()