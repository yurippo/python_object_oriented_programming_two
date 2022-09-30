class Programa:

    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self,novo_nome):
        self._nome = novo_nome.title()

    @property
    def like(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    def __str__(self):
        return (f'{self._nome} - {self.ano}: {self._likes} Likes')


class Filme(Programa): #heranca em python eu passo a classe mae como parametro dessa forma
    #python ate suporta heranca multipla mas estamos usando so uma classe para nao complicar muito
    #quando fazemos a heraanca herdamos todas as funcionalidades da classe mae metodos atributos,
    #mas tambem tenho o conceito de extender a classe mae agregar mais a classe mae
    

    def __init__(self, nome, ano, duracao):
        super().__init__(nome,ano) #esse trecho cria um objeto com os parametros da classe mae
        self.duracao = duracao

#nao precisei implementar os getters, setters properties que vem da classe mae

    def retorna_cadastro_diferenciado(self):
        pass

    def __str__(self):
        return (f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes')

class Serie(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome,ano) #o super sobrescreve aqui o init da classe mae
        self.temporadas = temporadas #estou usando o self aqui para adicionar mais um atributo mis alguma cisa a classe

#nao precisei implementar os getters, setters properties que vem da classe mae

    def __str__(self): #criei o thunder method que e o imprime de forma pythonica retorna o objeto em forma de string
        return (f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} Likes')


class Playlist:
    def __init__(self,nome,programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self,item): #euto repassando o meu item para a lista de programas interna esse metodo eh um thunder metodo do python data model
       return self._programas[item]
   #metodo magico do Python Magic Method Of Python Undercore front and back Duck Typing

    @property
    def listagem(self):
        return self._programas


    def __len__(self): #thunder magic method metodo magico do python
     return len(self._programas)




vingadores = Filme('vingadores - guerra infinita',2018,160)
atlanta = Serie('atlanta', 2018, 2)

tmep = Filme('Todo mundo em pânico',1999, 100)
demolidor = Serie('Demolidor',2016,2)


vingadores.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like()
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()

filmes_e_series = [vingadores,atlanta, demolidor,tmep]

playlist_fim_de_semana = Playlist('fim de semana',filmes_e_series)

print(f'Tamanho da playlist: {len(playlist_fim_de_semana.listagem)}')

print(vingadores in playlist_fim_de_semana)

len(playlist_fim_de_semana)

for programa in playlist_fim_de_semana:
    print(programa)

print(f'Ta ou nao ta?! {demolidor in playlist_fim_de_semana}')




#É quando não importa a classe sendo usada,
# contanto que esta classe herde de uma superclasse específica.
#Correto. Um código que espera uma superclasse, pode receber qualquer
# classe filha, reduzindo a quantidade de ifs às vezes, pois não precisamos
# mais verificar o tipo da classe.


#Herança
#Generalização/especialização
#Método super()

#
# Polimorfismo
# Relacionamento é um
# Representação textual de um objeto