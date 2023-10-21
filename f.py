import math

playlistRefresh = str(input()).split(" ")
durataionsInput = str(input()).split(" ")

durations = []
playlist = int(playlistRefresh[0])
refresh = int(playlistRefresh[1])

for dur in range(len(durataionsInput)):
    durations.append(durataionsInput[dur])

length = 0
adverts = []

for duration in durations:
    length += int(duration)

for start in durations:
    time = 0

    for following_songs in durations[:-1]:
        time += int(following_songs)
    
    adLength = math.floor(time / refresh)

    adverts.append(adLength)


output = ""
for ad in adverts:
    output += str(adverts[ad]) + " "

output = output[:-1]
print(output)