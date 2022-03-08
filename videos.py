import scrapetube

videos = scrapetube.get_channel("UC8A2EsWhIWV1T0jdG51eYLw")

with open("videos.txt", "w") as f:
    for i in videos:
        f.write("{}\n".format(i))