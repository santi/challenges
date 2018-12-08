


"""
input = [1, 1, 2, 3, 4, 5, 7, 6, 6, 7, 8]
output = [1, 1, 2, 3, 4, 5, 6, 6, 7, 8]
answer = 10
"""
input = []
with open('input-vekksort.txt') as f:
    lines = f.readlines()
    for line in lines:
        input.append(int(line))

print('Got input')

prev_max_len = [(0, 0)]


for i in range(len(input)):
    current_number = input[i]
    #print(f"current number is {current_number}")
    longest = 1
    for max, len in prev_max_len:
        #print(f"Looking at {prev} {max} {len}")
        if current_number >= max:
            #print("current number is less than max")
            if len >= longest:
                #print(f"The current longest chain is {longest}, which is shorter than {longest}")
                longest = len + 1
    #print(f'saving prev_max_len as: {(i, current_number, longest)}')
    prev_max_len.append((current_number, longest))
    if i % 100000 == 0:
        print(i)
#print(input)
#print(prev_max_len)

longest = 0
for max, len in prev_max_len:
    if len > longest:
        longest = len

print(len)
