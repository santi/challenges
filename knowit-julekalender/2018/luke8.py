
def parse_doll(line):
    doll = line.split(',')
    return (doll[0], int(doll[1]))

dolls = sorted(list(map(parse_doll, open('luke8.txt').readlines())), key=lambda doll: doll[1])

for doll in dolls:
    print(doll)

max_dolls = 0
prev_doll = (None, 0)
for doll in dolls:
    if doll[0] == prev_doll[0] or doll[1] == prev_doll[1]:
        continue
    else:
        print(f"add doll {doll} to collection.")
        max_dolls += 1
        prev_doll = doll
print(max_dolls)