import simplecrypt

with open(r"C:\Users\arkka\Desktop\encrypted.bin", "rb") as inp:
	encrypted = inp.read()
	with open(r"C:\Users\arkka\Desktop\passwords.txt", "r") as pas:
		a = pas.read().strip().split('\n')
		for i in a:
			s = simplecrypt.decrypt(i, encrypted)
			print(s)



