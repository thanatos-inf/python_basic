import pytube
from pytube import YouTube

vid = YouTube('https://www.youtube.com/watch?v=w8iTD4CaHCk&list=RDw8iTD4CaHCk&start_radio=1&ab_channel=AvrilLavigneVEVO')

print('Title: ', vid.title)
print('Views: ', vid.views)
print('Length: ', vid.length, 'seconds')
print('Description: ', vid.description)
print('Ratings: ', vid.rating)

yt = YouTube('https://www.youtube.com/watch?v=w8iTD4CaHCk&list=RDw8iTD4CaHCk&start_radio=1&ab_channel=AvrilLavigneVEVO')
streams = yt.streams

video_480 = streams.filter(res='480p').desc().first()
audio_best = streams.filter(only_audio=True).desc().first()

video_480.download()
audio_best.download()
