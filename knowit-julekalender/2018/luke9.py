# encoding: utf-8
import json
import hashlib

def md5(hash, char):
    msg = hash + char
    msg = msg.encode()
    hasher = hashlib.md5()
    hasher.update(msg)
    return hasher.hexdigest()

with open('luke9.json') as f:
    messages = json.load(f)
print(len(messages))
init = md5('julekalender', '')
seed = md5(init, 'u')
print(seed)
letters = []
for _ in range(len(messages)):
    for msg in messages:
        code =md5(init, msg['ch'])
        if code == msg['hash']:
            init = code
            letters.append(msg['ch'])
            break

print(''.join(letters))
            
