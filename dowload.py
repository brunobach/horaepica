from __future__ import unicode_literals
import youtube_dl
import json

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '192'
    }],
    'postprocessor_args': [
        '-ar', '16000'
    ],
    'prefer_ffmpeg': True,
    'keepvideo': True,
    'outtmpl': './generated/audio/%(id)s.%(ext)s'
}

def download(url):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


file = open('./generated/erros.json', "r")
data = json.loads(file.read())

for idx, video in enumerate(data):
    print(str(idx) + ': video em processamento: ' + video['video'] + '\n')
    url = 'https://www.youtube.com/watch?v=' + video['video']
    download(url)