import requests
import re


def url_in(in_wich, look_for):
	res = requests.get(in_wich)
	_lst = re.findall(r"<a href=\"([^\"]*)", res.text)
	for i in _lst:
		if look_for in i:
			return _lst, True
	return _lst, False


a = input().strip()
b = input().strip()

lst, _bool = url_in(a, b)
lists = ''
s = 'No'
for i in lst:
	lists, _bool = url_in(i, b)
	if _bool :
		s = 'Yes'
		break
print(s)



# import re
# import requests
#
# start_url = input()
# end_url = input()
#
# found = False
#
# link_pattern = re.compile(r'<a[^>]*?href="(.*?)"[^>]*?>')
#
# resp = requests.get(start_url).text
# for url in link_pattern.findall(resp):
# 	cur_resp = requests.get(url).text
# 	if end_url in link_pattern.findall(cur_resp):
# 		found = True
# 		break
#
# print("Yes" if found else "No")