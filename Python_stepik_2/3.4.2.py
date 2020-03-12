import re
import requests

html_file = input()
# html_file = 'http://pastebin.com/raw/7543p0ns'

link_pattern = re.compile(r'<a[^>]*?href=(?:\'|\")(?:https://|http://|ftp://|)(.*?)[\"|\'|/|:]')
resp = requests.get(html_file).text
url = link_pattern.findall(resp)
url2 = []
for i in url:
	if not i.startswith(".."):
		url2.append(i)
url2 = sorted(list(set(url2)))
# url = sorted(url)
# url = set(url)
# match_object = re.search(pattern, line)
print(*url2, sep='\n')

# import re
# import requests
#
# resp = requests.get(input()).text
# sites = set()
# for site in re.findall(r'<a.*?href=".*?:\/\/((?:\w|-)+(?:\.(?:\w|-)+)+)', resp):
#     sites.add(site)
#
# for site in sorted(sites):
#     print(site)

# import requests, re
# urls = set(re.findall(r"(?:.*)?(?:<a(?:.*)? href=[\"\'])(?:\w+://)?(\w[\w\.-]*)", requests.get(input()).text))
#
# print('\n'.join(sorted(urls)))