from collections.abc import Sized  #outra abstract class

class MinhaListagem(Sized):
    def __init__(self,descricao,tamanho):
        self.descricao = descricao
        self.tamanho = tamanho

    def __str__(self):
        return self.descricao

    def __len__(self):
        return len(self.tamanho)


lista = MinhaListagem('Nova_Lista',3)
print(lista.descricao,lista.tamanho)

#o metodo __len__ que caracteriza a classe abstrata sized tem que ser implementado senao teremos um erro