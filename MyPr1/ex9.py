def update_dictionary(d, key, value):
    a = []
    if key in d:
        a = d[key]
        a.append(value)
        d[key] = a
    elif 2 * key in d:
        a = d[2 * key]
        a.append(value)
        d[2 * key] = a
    else:
        a.append(value)
        d[2 * key] = a

d = {}
x = {}
print(update_dictionary(x, 0, -5)) # None
print(x) # {0: [-5]}  (0*0=2)
update_dictionary(x, 1, -1)
print(x) # {0: [-5], 2: [-1]} (тк индекса 1 нет создаем key*2=2)
update_dictionary(x, 2, -2)
print(x) # {0: [-5], 2: [-1, -2]} (тк индекс 2 есть добавляем -2 в него)
update_dictionary(x, 3, -3)
print(x) # 0: [-5], 2: [-1, -2], 6: [-3]}
# print(update_dictionary(d, 1, -1))  # None
# print(d)                            # {2: [-1]}
# update_dictionary(d, 2, -2)
# print(d)                            # {2: [-1, -2]}
# update_dictionary(d, 1, -3)
# print(d)                            # {2: [-1, -2, -3]}