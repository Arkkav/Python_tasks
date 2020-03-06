n = int(input())
Vertex = {} # вершина : множество прямых предков


def get_direct_ancestor(a, vertex): # возвращает множество всех предков

	stack = []
	for i in vertex[a]:
		stack.append(i)
		if i:
			stack.extend(get_direct_ancestor(i, vertex))
	return set(stack)


for i in range(n):
	VertexBuff = input().split()
	Vertex[VertexBuff[0]] = set()
	if len(VertexBuff) != 1:
		[Vertex[VertexBuff[0]].add(i) for i in VertexBuff[2:]]
q = int(input())
ex = [input() for i in range(q)]
re = []
for i in range(len(ex) - 1, 0, -1):
	if ex[i] not in Vertex:
		continue
	anc = get_direct_ancestor(ex[i], Vertex)
	for j in range(i):
		if ex[i] in re:
			continue
		if ex[j] == ex[i] or ex[j] in anc:
			re.append(ex[i])
for i in range(len(re) - 1, -1, -1):
	print(re[i])

# 	что это за генератор?
# def checkdup(d):
#     return cls[d] is None or any(map(checkdup, cls[d]))
#
# cls = {d: set(b[1:]) for _ in range(int(input())) for d, *b in [input().split()]}
#
# for _ in range(int(input())):
#     c = input()
#     if checkdup(c):
#         print(c)
#     cls[c] = None


# # код преподавателя
# n = int(input())
# classes = {}
# for i in range(n):
#     line = input()
#     parts = line.split(" : ")
#     cls = parts[0]
#     if len(parts) == 1:
#         classes[cls] = []
#     else:
#         classes[cls] = parts[1].split(" ")
#
#
# def check(src, dest):
#     if src == dest:
#         return True
#     return any([check(child, dest) for child in classes[src]])
#
#
# m = int(input())
# used = []
#
# for i in range(m):
#     cls = input()
#     if any([check(cls, used_one) for used_one in used]):
#         print(cls)
#     used.append(cls)