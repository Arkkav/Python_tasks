import re

resp = ''
link_pattern = re.compile(r'(.*)?')
url = link_pattern.findall(resp)