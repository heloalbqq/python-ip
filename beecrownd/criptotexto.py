teste = int(input())
for i in range(0,teste):
	txt = input()
	mensagem = []
	for c in txt:
		if c.islower():
			mensagem.append(c)
		else:
			continue
		
	for c in mensagem[::-1]:
		print(c,end="")
		
	print()