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



