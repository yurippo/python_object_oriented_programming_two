class FolhaDePagamento:
    @staticmethod
    def log():
        return f"Isso é um log qualquer"




#Métodos estáticos a outra forma de criar métodos ligados
# à classe é com a declaração @staticmethod. Veja acima

#Note que, no caso acima, não precisamos passar nenhum primeiro
# argumento fixo para o método estático. Nesse caso, não é possível
# acessar as informações da classe, porém o método estático é acessível
# a partir da classe e também da instância.

#Cuidados a tomar...
#Sempre que você usar métodos estáticos em classes que contém herança,
# observe se não está tentando acessar alguma informação da classe a partir
# do método estático, pois isso pode dar algumas dores de cabeça pra entender o motivo dos problemas.

#Alguns pythonistas não aconselham o uso do @staticmethod, já que poderia ser substituído por uma simples
# função no corpo do módulo. Outros mais puristas entendem que os métodos estáticos fazem sentido, sim,
# e que devem ser vistos como responsabilidade das classes.

