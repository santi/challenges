__author__ = 'Santi'


file = open("words.txt","r")
data = file.readlines()
file.close()

for word in range(len(data)):
    data[word] = data[word].lower().strip()
    foo = []
    for bokstav in data[word]:
        foo.append(bokstav)
    foo = sorted(foo)
    data[word] = str(foo)



data = sorted(data)


teller = {}
for ord in data:
    if ord in teller:
        teller[ord] += 1
    else:
        teller[ord] = 1


max = 0
maxKey = ""
for key in teller:
    if teller[key] > max:
        max = teller[key]
        maxKey = key
print(maxKey)
