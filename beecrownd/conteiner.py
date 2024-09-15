container = input().split()
container = list(map(int, container))
navio = input().split()
navio = list(map(int, navio))
dimensao = 1
ok = 0

for i in range(0,3):
	if container[i] > navio[i]:
		ok = 1
	
if ok == 0:		
	for c in range(0,3):		
		dimensao *= navio[c]//container[c]
	
	print(dimensao)

else:
	print(0)