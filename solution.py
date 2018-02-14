fi = open('./input.txt', 'r')
firstLine = fi.readline().split()
w = int(firstLine[0])
h = int(firstLine[1])
keys = []
for i in range(0,h):
    keys.append(fi.readline().split()[0])

langs = []
tempArray = []

for line in fi:
    if line.split()[0] == "%TEMPLATE-END%":
        langs.append(tempArray)
        tempArray = []
    else:
        if line.split()[0] != "%TEMPLATE-START%":
            tempArray.append(line)

templates = []

for i in range(0,3):
    templates.append("".join(langs[i][1:]))

sums = [0,0,0]

for i in range(0,3):
    preX = 0
    preY = 0
    for s in templates[i]:
        x = 0
        y = 0
        for k in keys:
            x = k.find(s)
            if x >= 0:
                x += 1
                y = keys.index(k) + 1
                if templates[i].index(s) != 0:
                    sums[i] += max(abs(x-preX), abs(y-preY))
                preX = x
                preY = y
                break

bestScore = min(sums)
bestLang = langs[sums.index(bestScore)][0]

fo = open('./output.txt', 'w')
fo.write(bestLang)
fo.write(str(bestScore))
