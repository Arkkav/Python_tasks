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
# print(Vertex)

q = int(input())
Answers = ''
for i in range(q):
	Ancestor, Descendant = input().split()
	if Ancestor not in Vertex or Descendant not in Vertex:
		Answers += 'No\n'
		continue
	anc = get_direct_ancestor(Descendant, Vertex)
	# print(Descendant + ' ' + str(anc))
	if Ancestor in anc or Ancestor == Descendant:
		Answers += 'Yes\n'
	elif Ancestor not in anc:
		Answers += 'No\n'
	else:
		Answers += 'No\n'
print(Answers)

# Так себе код, но интересно применение map и lambda
# n = int(input())
#
# parents = {}
# for _ in range(n):
#     a = input().split()
#     parents[a[0]] = [] if len(a) == 1 else a[2:]
#
# def is_parent(child, parent):
#     return child == parent or any(map(lambda p: is_parent(p, parent), parents[child]))
#
# q = int(input())
# for _ in range(q):
#     a, b = input().split()
#     print("Yes" if is_parent(b, a) else "No")


# # Вот еще неплохое решение
# def test(parent, child):
#     if parent == child or parent in base[child]:
#         return 'Yes'
#     for i in base[child]:
#         if test(parent, i) == 'Yes':
#             return 'Yes'
#     return 'No'
#
# base = {}
# for com in [input().split(' ') for i in range(int(input()))]:
#     base[com[0]] = com[2:len(com)]
# for com in [input().split(' ') for i in range(int(input()))]:
#     print (test(com[0], com[1]))
