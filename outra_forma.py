class Filme:

    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self,novo_nome):
        self.__nome = novo_nome.title()

    @property
    def like(self):
        return self.__likes

    def dar_like(self):
        self.__likes += 1


class Serie:

    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self,novo_nome):
        self.__nome = novo_nome

    @property
    def likes(self):
        return self.__likes
    def dar_like(self):
        self.__likes += 1


vingadores = Filme('vingadores - guerra infinita',2018,160)

#Filme(nome='vingadores', ano=2018, duracao=160)

#Ou

"Filme: Vingadores de 2018 - 160 min"
#
# A primeira deixa bem claro como funciona o objeto. Normalmente,
# a segunda forma ilustra o que um usuário final ficaria satisfeito em ver.
#
# A ideia da primeira versão é remover ambiguidade e permite, por exemplo, recriar
# o objeto, já que está mostrando todas as informações.
#
# Outro exemplo, se chamarmos o repr de um objeto do tipo list, podemos ter uma ideia
# do que é esperado quando criarmos o nosso próprio com __repr__:

lista = [1,2,4,5]

print(repr(lista))
#
# Se pegarmos o resultado do print, conseguimos recriar o objeto lista.



vingadores.dar_like()

print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duracao: {vingadores.duracao} - Likes: {vingadores.like}')

atlanta = Serie('atlanta', 2018, 2)
atlanta.nome = 'atlanta de glover'

atlanta.dar_like()
atlanta.dar_like()

print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas} - Likes: {atlanta.likes}')


#
# Nós vimos como usar __str__ para representar um objeto como string de forma legível.
#
# Falamos sobre uma outra forma de representação, ela pode ajudar bastante se precisarmos
# encontrar um erro, ou debugar o código.
#
# Assim como o __str__, existe outro método especial chamado __repr__, que é usado para
# mostrar uma representação que ajude no debug ou log de um código.
#
# Por exemplo, se você quiser entender como funciona seu objeto, ou se está válido,
# e imprimir o seu valor string, qual resultado abaixo facilita sua vida?