from pytube import YouTube

#link = 'https://www.youtube.com/watch?v=hc_TJee9J_U'
link = 'https://www.youtube.com/watch?v=UHgY7LIiaSM'

yt = YouTube(link)

#stream = yt.streams.filter(only_audio=True, subtype='webm').first()
#stream.download('/home/david/Documents/Coding/Practicas-Python/YTDownloader', filename=f'{yt.title}.mp3')


yt.streams.get_highest_resolution().download('/home/david/Documents/Coding/Practicas-Python/YTDownloader')
