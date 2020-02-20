a, b, c, d = input(), input(), input(), input()
g = {}
for i in range(len(a)):
    g[a[i]] = b[i]

def cypher(a, d):
    b = ''
    for i in range(len(a)):
        b += d[a[i]]
    return b
def uncode(d):
    uncode = {}
    for key, value in d.items():
        uncode[value] = key
    return uncode
print(cypher(c, g))
print(cypher(d, uncode(g)))