import requests
import json
# import sqlite3
# from sqlite3 import Error
#
#
# def create_connection(path):
#     connection = None
#     try:
#         connection = sqlite3.connect(path)
#         print("Connection to SQLite DB successful")
#     except Error as e:
#         print(f"The error '{e}' occurred")
#
#     return connection
#
#
# connection = create_connection(r"C:\Users\arkka\PycharmProjects\Python_tasks\Python_stepik_2\sm_app.sqlite")
# c = connection.cursor()
# c.execute('''CREATE TABLE stocks
#              (name text, date text)''')


client_id = '...'
client_secret = '...'
# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
				  data={"client_id": 'edb1081cc97bfe18a1e2',
						"client_secret": 'cdc884c2e9ea1c25cd0de823fa721545'})

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]
# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}
# инициируем запрос с заголовком
s = '''4f5f64c13b555230ac000004
503649d96cb8020002000dd0
519258cc9e628509c40000d7
56d6f872139b2166eb000ade
4e96f7705554c900010027db
4f552b2e3b55524170000003
511d5a7994326bf7f10005c6
53fb955e72616951aa090000
545bef0b72616949b5310700
53d8b30672616913c7e40200
551bc2ca7261692b55981300
4f86f41a24907b0001000d46
515b34a9223afaab8f000905
4e9314fd57d697000100133c
55255e8d7261695ba22f0300
'''.split()
lst = dict()
for i in s:
	r = requests.get("https://api.artsy.net/api/artists/" + i, headers=headers)
	j = json.loads(r.text)
	lst[j['sortable_name']] = int(j['birthday'])
lst = sorted(lst.items(), key=lambda x: (x[1], x[0]))  # 2-а аргумента работают как в sort by в SQL
print(*[i[0] for i in lst], sep='\n')