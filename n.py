bottles = int(input()) # number of bottles
volumes = []
alphabet = "abcdefghijklmnopqrstuvwxyz"

for bottle in range(bottles):
    var = str(input())
    volumes.append(float(var[:-1]))
         
for vol in volumes:
    sum = ""
    newSum = ""

    sum = hash(vol)

    for char in str(sum):
        intchar = int(char)
        newSum += alphabet[intchar]

    print(newSum)