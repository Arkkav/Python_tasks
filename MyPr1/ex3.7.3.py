a = int(input())
b = set()
[b.add(*input().lower().split('\n')) for i in range(a)]
c = int(input())
d = set()
for i in range(c):
    g = input().lower().split(' ')
    [d.add(i) for i in g]
[print(i) for i in d if i not in b]

# # # формируем множество известных слов на основании построчного ввода
# # dic = {input().lower() for _ in range(int(input()))}
# #
# # # заводим пустое множество для приема текста
# wrd = set()
#
# # т.к. текст построчно подается, а также в каждой строке несколько слов,
# # то каждую строку превращаем во множество и добавляем в единое множество wrd
# for _ in range(int(input())):
#     wrd |= {i.lower() for i in input().split()}
#
# # на вывод отправляем результат вычитания словарного множества dic
# # из текстового множества wrd; впереди ставим *, чтобы раскрыть поэлементно
# print(*(wrd-dic), sep="\n")


# words = set(input().lower() for i in range(int(input())))
# text = set(('\n'.join(input().lower() for i in range(int(input())))).split())
# print('\n'.join(text - words))