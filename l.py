import math

ones = str(input()).split(" ")
twos = str(input()).split(" ")

# Ones
h1 = int(ones[0])
d1 = int(ones[1])
t1 = int(ones[2])

# Twos
h2 = int(twos[0])
d2 = int(twos[1])
t2 = int(twos[2])

hitsNeededFor1 = h1 / d2
hitsNeededFor2 = h2 / d1

hitsNeededFor1 = math.ceil(hitsNeededFor1)
hitsNeededFor2 = math.ceil(hitsNeededFor2)

timeFor1ToDie = (hitsNeededFor1 -1) * t2
timeFor2ToDie = (hitsNeededFor2 -1) * t1

if timeFor1ToDie > timeFor2ToDie:
    print("player one")
elif timeFor1ToDie < timeFor2ToDie:
    print("player two")
else:
    print("draw")