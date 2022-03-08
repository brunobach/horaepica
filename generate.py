
# importing modules
from youtube_transcript_api import YouTubeTranscriptApi
import json
from os.path import exists

erros = []

def generate_subtitles(video_id):
    try:
        srt = YouTubeTranscriptApi.get_transcript(video_id, ['pt', 'pt-BR'])
        with open('./subtitles/' + video_id + '.txt', "w") as f:
            for i in srt:
                f.write("{}\n".format(i))
        print('video concluido: ' + video_id + '\n')
    except:
        print('Não foi possivel gerar: ' + video_id + '\n')
        erros.append({"video": video_id})
        with open('erros.json', 'w') as json_file:
            json.dump(erros, json_file, indent=4)

def check_subtitles(video_id):
    if exists('./subtitles/' + video_id + '.txt'):
        print('video ja existe: ' + video_id + '\n')
    else:
        generate_subtitles(video_id)

file = open('videos.json', "r")
data = json.loads(file.read())

for idx, video in enumerate(data):
    print(str(idx) + ': video em processamento: ' + video['videoId'] + '\n' + video['title']['runs'][0]['text'] + '\n' )
    check_subtitles(video['videoId'])

file.close()

