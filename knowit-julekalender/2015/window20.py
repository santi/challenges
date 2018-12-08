__author__ = 'Santi'

"""
Gitt strengene S og T. Finn den korteste substrengen av S som inneholder alle bokstavene i T
(rekkefølge på bokstavene i substrengen er ikke relevant).

Eksempel:
S = ADOBECODECBFANETS
T = ABC
Så er den korteste substrengen som inneholder alle bokstavene i T CBFA
"""


T = "ABCDA"

S = "FJKAUNOJDCUTCRHBYDLXKEODVBWTYPTSHASQQFCPRMLDXIJMYPVOHBDUGSMBLMVUMMZYHULSUIZIMZTICQORLNTOVKVAMQTKHVR" \
    "IFMNTSLYGHEHFAHWWATLYAPEXTHEPKJUGDVWUDDPRQLUZMSZOJPSIKAIHLTONYXAULECXXKWFQOIKELWOHRVRUCXIAASKHMWTMA" \
    "JEWGEESLWRTQKVHRRCDYXNTLDSUPXMQTQDFAQAPYBGXPOLOCLFQNGNKPKOBHZWHRXAWAWJKMT" \
    "JSLDLNHMUGVVOPSAMRUJEYUOBPFNEHPZZCLPNZKWMTCXERPZRFKSXVEZTYCXFRHRGEITWHRRYPWSVAYBUHCERJXDCYAVICPTNBGIOD" \
    "LYLMEYLISEYNXNMCDPJJRCTLYNFMJZQNCLAGHUDVLYIGASGXSZYPZKLAWQUDVNTWGFFYFFSMQWUNUPZRJMTHACFELGHDZEJWFD" \
    "WVPYOZEVEJKQWHQAHOCIYWGVLPSHFESCGEUCJGYLGDWPIWIDWZZXRUFXERABQJOXZALQOCSAYBRHXQQGUDADYSORTYZQPWGMBLN" \
    "AQOFODSNXSZFURUNPMZGHTAJUJROIGMRKIZHSFUSKIZJJTLGOEEPBMIXISDHOAIFNFEKKSLEXSJLSGLCYYFEQBKIZZTQQXBQZAPXAA" \
    "IFQEIXELQEZGFEPCKFPGXULLAHXTSRXDEMKFKABUTAABSLNQBNMXNEPODPGAORYJXCHCGKECLJVRBPRLHORREEIZOBSHDSCETTTNFTS" \
    "MQPQIJBLKNZDMXOTRBNMTKHHCZQQMSLOAXJQKRHDGZVGITHYGVDXRTVBJEAHYBYRYKJAVXPOKHFFMEPHAGFOOPFNKQAUGYLVPWUJUPCU" \
    "GGIXGRAMELUTEPYILBIUOCKKUUBJROQFTXMZRLXBAMHSDTEKRRIKZUFNLGTQAEUINMBPYTWXULQNIIRXHHGQDPENXAJNWXULFBNKBRIN" \
    "UMTRBFWBYVNKNKDFR"


def check_zero_dict(d):
    zeroes = True
    for c in d.values():
        if c > 0:
            zeroes = False
    return zeroes


def make_dict(t):
    chars = {}
    for c in t:
        if chars.get(c):
            chars[c] += 1
        else:
            chars[c] = 1
    return chars


def find_shortest_subsequence(s, t):
    start_index = 0
    end_index = len(s)
    for i in range(len(s)):
        chars = make_dict(t)
        for j in range(i, len(s)):
            if chars.get(s[j]):
                chars[s[j]] -= 1
            if check_zero_dict(chars):
                if end_index - start_index > j + 1 - i:
                    print("FINISHED!", "The longest substring was", j + 1 - i, "long, and was", s[i:j+1], "from", i, "to", j + 1)
                    start_index = i
                    end_index = j + 1
                break
    return start_index, end_index, s[start_index:end_index]

print(find_shortest_subsequence(S, T))