# coding=utf-8
import operator
__author__ = 'vemund'

"""
Gitt en liste med positive heltall, finn det største tallet det er mulig å lage ved å sette sammen
alle tallene i lista i valgfri rekkefølge.

Eksempel 1: [3, 30, 34, 5, 9] => 9534330
Eksempel 2: [128,12] => 12812
Eksempel 3: [824,938,1399,5607,6973,5703,9609,4398,8247] => 9609938824824769735703560743981399

"""


class Number(object):

    def __init__(self, number, index):
        self.number = str(number)
        self.index = index

    def __len__(self):
        return len(self.number)

    def __getitem__(self, item):
        return self.number[item]


numbers = [2907, 6165, 6129, 3468, 2040, 4331, 7935, 5683, 6004, 9694, 8092, 188, 5796, 1184, 8873, 3200, 1981, 9556, 9981, 1387, 7802, 8387, 9970, 7326, 5372, 28, 628, 3408, 6, 3425, 3071, 6021, 9989, 5077, 824, 938, 1399, 5607, 6973, 5703, 9609, 4398, 8247, 5164, 2026, 4, 4468, 9524, 8, 9227, 8969, 1746, 5593]
text_numbers = []*len(numbers)
for i in range(len(numbers)):
    num = Number(numbers[i], i)
    text_numbers.append(num)

longest_number = len(text_numbers[0])
for num in text_numbers:
    if len(num) > longest_number:
        longest_number = len(num)

for i in range(len(text_numbers)):
    if len(text_numbers[i]) < longest_number:
        text_numbers[i].number += "9" * (longest_number - len(text_numbers[i]))

text_numbers.sort(cmp=(lambda a, b: int(b.number + a.number) - int(a.number + b.number)))

for num in text_numbers:
    print numbers[num.index]

number = ""
for i in range(len(text_numbers)):
    number+= str(numbers[text_numbers[i].index])
print number

print "99899981997096949609955695249389227889698873838782482478092793578027326669736286165612960216004579657035683560755935372516450774446843984331346834253408320030712907282040202619811881746139913871184" \
   == "99899981997096949609955695249389227896988873838782482478092793578027326697366286165612960216004579657035683560755935372516450774468443984331346834253408320030712907282040202619811881746139913871184"
