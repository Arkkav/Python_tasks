namespaces = {'global': None} # словарь пространств - пространство : родитель
vars = {'global': set()} # словарь переменных - пространство, множество переменных
def create(par1, par2):
	# create <namespace> <parent> –  создать новое пространство
	# имен с именем <namespace> внутри пространства <parent>
	namespaces[par1] = par2
def add(par1, par2):
	# add <namespace> <var> – добавить в пространство <namespace> переменную <var>
	if par1 in vars:
		vars[par1].add(par2)
	else:
		vars[par1] = set()
		vars[par1].add(par2)
def get(par1, par2):
	# get <namespace> <var> – получить имя пространства,
	# из которого будет взята переменная <var> при запросе и
	# з пространства <namespace>, или None, если такого пространства не существует
	global namespaces
	global vars
	if par1 == None:
		return None
	elif par1 in vars.keys():
		if par2 in vars[par1]:
			return par1
		else:
			par1 = namespaces[par1]
			return get(par1, par2)
	else:
		par1 = namespaces[par1]
		return get(par1, par2)
s = ''
n = int(input())
for i in range(n):
	cmd, par1, par2 = input().split()
	if cmd == 'create':
		create(par1, par2)
	elif cmd == 'add':
		add(par1, par2)
	else:
		s += str(get(par1, par2)) + '\n'
print(s)





