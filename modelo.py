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

vingadores.dar_like()

print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duracao: {vingadores.duracao} - Likes: {vingadores.like}')

atlanta = Serie('atlanta', 2018, 2)
atlanta.nome = 'atlanta de glover'

atlanta.dar_like()
atlanta.dar_like()

print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas} - Likes: {atlanta.likes}')


# Nesta aula, aprendemos sobre a construção de objetos e classes, utilizando encapsulamento. Vimos:
#
# Criação da classe
# Definição de métodos assessores
# @property
# name
# Até a próxima aula!