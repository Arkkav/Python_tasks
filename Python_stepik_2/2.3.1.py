# class Iterformultifilter:


class multifilter:
    def judge_half(pos, neg):
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
        return pos >= neg

    def judge_any(pos, neg):
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
        return pos >= 1

    def judge_all(pos, neg):
        # допускает элемент, если его допускают все функции (neg == 0)
        return neg == 0

    def __init__(self, iterable, *funcs, judge=judge_any):
        # iterable - исходная последовательность
        # funcs - допускающие функции
        # judge - решающая функция
        self.i = 0
        self.judge = judge
        self.funcs = funcs
        self.iterable = iterable
        self.k = len(self.iterable)

    def __iter__(self):
        # возвращает итератор по результирующей последовательности
        return self

    def __next__(self):
        while self.i < self.k:
            pos = 0
            neg = 0
            for _ in self.funcs:
                if _(self.iterable[self.i]):
                    pos += 1
                else:
                    neg += 1
            self.i += 1
            if self.judge(pos, neg):
                return self.iterable[self.i - 1]
        raise StopIteration







def mul2(x):
    return x % 2 == 0

def mul3(x):
    return x % 3 == 0

def mul5(x):
    return x % 5 == 0

a = [i for i in range(31)]  # [0, 1, 2, ... , 30]
b = multifilter(a, mul2, mul3, mul5)
print(list(b))
print(list(b))
# [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]


# print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))
# # [0, 6, 10, 12, 15, 18, 20, 24, 30]
#
# print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))
# # [0, 30]


# # с применением генератора в одной строке
# class multifilter:
#     judge_half = lambda fx: sum(fx) >= len(fx) / 2
#     judge_any = lambda fx: any(fx)
#     judge_all = lambda fx: all(fx)
#
#     def __init__(self, iterable, *funcs, judge=judge_any):
#         self.iterable = iterable
#         self.funcs = funcs
#         self.judge = judge
#
#     def __iter__(self):
#         return (x for x in self.iterable if self.judge([f(x) for f in self.funcs]))


# собственное решение через yield (вместо __next__)
#
# логика работы прописана в итераторе объекта __iter__
# где пробегаемся по элементам исходной последовательности
# просеиваем элемент через функции-фильтры
# и если выбранная функция judge дала добро
# то yield`им этот элемент
#
#
#

# # решение с yield в iter
# class multifilter:
#     def judge_half(pos, neg):
#         return pos >= neg  # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
#
#     def judge_any(pos, neg):
#         return pos >= 1  # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
#
#     def judge_all(pos, neg):
#         return neg == 0  # допускает элемент, если его допускают все функции (neg == 0)
#
#     def __init__(self, iterable, *funcs, judge=judge_any):
#         self.lst = iterable  # iterable - исходная последовательность
#         self.funcs = funcs   # funcs - допускающие функции
#         self.judge = judge   # judge - решающая функция
#
#     def __iter__(self):
#         for el in self.lst:
#             pos, neg = 0, 0
#             for f in self.funcs:
#                 pass
#                 if f(el):
#                     pos += 1
#                 else:
#                     neg += 1
#             if self.judge(pos, neg):
#                 yield el