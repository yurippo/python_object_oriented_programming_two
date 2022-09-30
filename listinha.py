class Listinha:

    def __init__(self,items):
        self.items = items

    def __iter__(self):
        return self.items.__iter__()

    def __len__(self):
        return(len(self.items))
#sem o def __len__ implementado nao da pra chamar o len(meu_objeto)


meu_objeto = Listinha([1,2,4])

contador = 0

for item in meu_objeto:
    contador += 1

if len(meu_objeto) == contador:
    print('Sao iguais!')
else:
    print('Nao sao iguais!')