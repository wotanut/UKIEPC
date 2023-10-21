couriers = int(input())
strengths_input = str(input())
strengths = strengths_input.split(" ")
l = []

for i in range(len(strengths)):
    l.append(int(strengths[i]))

medians = []
teams = couriers // 3


l.sort(reverse=True)
for team in range(teams):
    l.pop()

isSkip = False

l.reverse()

for median in l:
    if isSkip or len(medians) == teams:
        isSkip = False
    else:
        medians.append(median)
        isSkip = True

sum = 0

for _ in medians:
    sum += int(_)

print(sum)