import re

pattern = r"a\w.c" # r"a[a-c]c", r"a[^a-zA-Z]c" - диапазон (^ - это символ
# НЕ от всего выражения)
s = 'aa-caacabcbacbacbacbcabacbacacbbacbac' # abc. acc - подходят
match_obj = re.match(pattern, s)
print(match_obj)
all_inclusions = re.findall(pattern, s)
print(all_inclusions)