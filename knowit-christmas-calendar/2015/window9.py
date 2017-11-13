__author__ = 'vemund'

n = 142453146368
liste = []
#print "".join(map(chr, map(lambda n: n + 65, lambda liste, number: liste.append(number%26) if number != 0 else liste(liste, number//26))))[::-1]
print (lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v))))(lambda f: (lambda i: 1 if (i == 0) else i * f(i - 1)))(10)
while n:
    n, rest = divmod(n - 1, 26)
    liste.append(chr(rest + 65))
print "".join(liste).upper()[::-1]

print




