playlist = [
{"title": "Bohemian Rhapsody", "duration": "5:55"},
{"title": "Hotel California", "duration": "6:30"},
{"title": "Stairway to Heaven", "duration": "8:02"},
{"title": "Imagine", "duration": "3:07"},
{"title": "Smells Like Teen Spirit", "duration": "5:01"},
{"title": "Billie Jean", "duration": "4:54"},
{"title": "Hey Jude", "duration": "7:11"},
{"title": "Like a Rolling Stone", "duration": "6:13"},
]

max = -1
max_s = ""
max_d = ""
min = 9999
min_s = ""
min_d = ""
total = 0

for i in playlist:
    dur = i["duration"]
    rdur = int(dur[0]) * 60 + int(dur[2]) * 10 + int(dur[3])
    if rdur > max:
        max = rdur
        max_s = i["title"]
        max_d = dur
    if rdur < min:
        min = rdur
        min_s = i["title"]
        min_d = dur
    total += rdur


print (f"Duracion total: {total // 60}m {total % 60}s")
print (f'Cancion mas larga: "{max_s}" ({max_d})')
print (f'Cancion mas corta: "{min_s}" ({min_d})')

