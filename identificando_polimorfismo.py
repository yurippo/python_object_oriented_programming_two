class Relatorio:
    def gera_relatorio(self):
        print('Relatório geral')

class RelatorioUsuarios(Relatorio):
    def gera_relatorio(self):
        print('Relatório dos usuários')

class RelatorioCustos(Relatorio):
    def gera_relatorio(self):
        print('Relatório de custos')

relatorio1 = RelatorioUsuarios()
relatorio2 = RelatorioCustos()
relatorio3 = RelatorioUsuarios()
relatorio4 = RelatorioUsuarios()

relatorios = [relatorio1, relatorio2, relatorio3, relatorio4]
for rel in relatorios:
    rel.gera_relatorio()


#Usando polimorfismo, consigo gerar relatórios de qualquer tipo, usando o código abaixo:
#Em que trecho do código ocorre o polimorfismo?
#
# for rel in relatorios:
#     rel.gera_relatorio()

#Correto, neste momento não importa qual é a classe do relatório.
