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


class Serie(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome,ano) #o super sobrescreve aqui o init da classe mae
        self.temporadas = temporadas #estou usando o self aqui para adicionar mais um atributo mis alguma cisa a classe

#nao precisei implementar os getters, setters properties que vem da classe mae

vingadores = Filme('vingadores - guerra infinita',2018,160)

vingadores.dar_like()

print(f'{vingadores.nome} - {vingadores.duracao}: {vingadores.like}')

atlanta = Serie('atlanta', 2018, 2)

atlanta.dar_like()
atlanta.dar_like()

#print(f'{atlanta.nome} - {atlanta.ano} - {atlanta.temporadas}: {atlanta.likes}')

filmes_e_series = [vingadores,atlanta]

for programa in filmes_e_series:
    detalhes = programa.duracao if hasattr(programa, "duracao") else programa.temporadas
    print(f'{programa.nome} - {detalhes} D -  {programa.ano} ')


#É quando não importa a classe sendo usada,
# contanto que esta classe herde de uma superclasse específica.
#Correto. Um código que espera uma superclasse, pode receber qualquer
# classe filha, reduzindo a quantidade de ifs às vezes, pois não precisamos
# mais verificar o tipo da classe.


#Herança
#Generalização/especialização
#Método super()
