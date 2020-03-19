# Есть файл, в котором содержаться слова разделённые пробелом.
# Например: "abba com mother bill mother com abba dog abba mother com".
# Нужно найти и вывести тройку слов, которые чаще всего встречаются вместе (порядок не имеет значения).
# То есть в моём примере тройки слов это "abba com mother", "com mother bill", "mother bill mother" и т.д.
# Тут правильным ответом должно быть "abba com mother" (частота — 3 раза).
# https://habr.com/en/post/439576/

s = "abba com mother bill mother com abba dog abba mother com".split()
a = []
d = dict()
max_i = 0
max_s = ''
for i in range(1,len(s)-1):
	b = sorted([s[i - 1], s[i], s[i + 1]])
	a.append(b)
	c = str(b)
	if b in a:
		if c in d:
			d[c] += 1
		else:
			d[c] = 1
		if d[c] > max_i:
			max_i = d[c]
			max_s = s[i - 1] + ' ' + s[i] + ' ' + s[i + 1]

print(d)
print(max_s)