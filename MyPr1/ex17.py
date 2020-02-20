import requests

r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/699991.txt')
b = r.text.strip()
while b[0:2] !='We':
    r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/' + b)
    b = r.text.strip()
    print(b)

