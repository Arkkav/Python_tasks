import json


def count_descendant(Vertex): # для класса Vertex возвращает всех потомков []
	ch = [Vertex]
	for i in js:
		if Vertex in i["parents"]:
			ch.append(i["name"])
			ch.extend(count_descendant(i["name"]))
	return ch


js = json.loads(input())
print(*sorted([i["name"] + ' : ' + str(len(set(count_descendant(i["name"])))) for i in js]), sep='\n')



# import json
#
# cls = {c['name']: c['parents'] for c in json.loads(input())}
#
# isbase = lambda b, d: b == d or any(isbase(b, c) for c in cls[d])
#
# for p in sorted(cls):
#     print(p, ':', len({c for c in cls if isbase(p, c)}))