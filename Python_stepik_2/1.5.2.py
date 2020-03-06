class Buffer:
	def __init__(self):
		# конструктор без аргументов
		self.current_part = []

	def add(self, *a):
		# добавить следующую часть последовательности
		self.current_part += a
		n = len(self.current_part) // 5
		if n > 0:
			for i in range(n):
				print(sum(self.current_part[: 5]))
				self.current_part = self.current_part[5:]

	def get_current_part(self):
		# вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были
		# добавлены
		return self.current_part

buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part() # вернуть [1, 2, 3]
buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
buf.get_current_part() # вернуть [6]
buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
buf.get_current_part() # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
buf.get_current_part() # вернуть [1]

# class Buffer:
#     def __init__(self):
#         self.part = []
#
#     def add(self, *a):
#         for i in a:
#             self.part.append(i)
#             if len(self.part) == 5:
#                 print(sum(self.part))
#                 self.part.clear()
#
#     def get_current_part(self):
#         return self.part