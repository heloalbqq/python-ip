#pessoa = {"nome":"helo", "idade":"19", "genero":"feminino"}
#nome = pessoa['nome']
#print(nome)

dados = [
    {"nome":"isa", "idade":18},
    {"nome":"helo", "idade":19}
]
for pessoa in dados:
    idade = pessoa["idade"]
    print(idade)