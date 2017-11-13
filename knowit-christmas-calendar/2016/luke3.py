import re

friends = {}

def increment_friend(friend):
    if friends.get(friend, False):
        pass
    else:
        friends[friend] = []

with open('luke3.input') as f:
    for line in f.readlines():
        statement = re.sub(' +', ' ', line.strip()).split(' '))
        if statement[0] == 'friends':
