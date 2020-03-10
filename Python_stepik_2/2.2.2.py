import simplecrypt

with open("encrypted.bin", "rb") as inp, open("passwords.txt", "r") as pas:
	encrypted = inp.read()
	# a = pas.read().strip().split('\n')
	for i in pas:
		a = i.strip()
		try:
			s = simplecrypt.decrypt(a, encrypted)
		except simplecrypt.DecryptionException:
			print('Error')
		else:
			print(a)
			print(s)


