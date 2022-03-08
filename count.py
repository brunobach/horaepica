import json
from os.path import exists


ocurrences = []
substring = "bagatela"


def get_counts(filename, name):
    ocurrences_str = 0
    lines = []
    with open(filename) as f:
        line = f.readline()
        while line:
            line = f.readline()
            total_occurrences = line.count(substring)
            if total_occurrences > 0:
                lines.append({"minutos": line})
            ocurrences_str += total_occurrences
    
    if ocurrences_str > 0:
        ocurrences.append({"name": name, "video": filename, "bagatela": ocurrences_str, "encontrado": lines })
        with open('bagatela_ok.json', 'w') as json_file:
            json.dump(ocurrences, json_file, indent=4)

def check_subtitles(video_id, name):
    file = './subtitles/' + video_id + '.txt'
    if exists(file):
        get_counts(file, name)
    else:
        print('video nao existe: ' + video_id + '\n')

file = open('videos.json', "r")
data = json.loads(file.read())

for idx, video in enumerate(data):
    print(str(idx) + ': video em processamento: ' + video['videoId'] + '\n' + video['title']['runs'][0]['text'] + '\n' )
    check_subtitles(video['videoId'], video['title']['runs'][0]['text'])