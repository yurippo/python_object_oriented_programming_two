class Funcionario:
    prefixo = "Instrutor"

    @classmethod
    def info(cls):
        return f"Esse é um {cls.prefixo}"

   
#Perceba que, ao invés de self, passamos cls para o método,
# já que neste caso sempre recebemos uma instância da classe
# como primeiro argumento. O nome cls é uma convenção, assim como self.





#Métodos de classe
#São métodos declarados com @classmethod.
# Quando criamos um método de classe, temos acesso
# aos atributos da classe. Da mesma forma com os atributos de classe,
# podemos acessar estes métodos de dentro dos métodos de instância, a
# partir de __class__, se desejarmos:


#Para saber mais: Métodos estáticos e de classe

#Da mesma forma que temos alguns atributos diretamente da
# classe, e que são acessíveis sem necessidade de criar uma instância,
# conseguimos também criar métodos ligados à classe.

#Há duas formas de criar estes métodos: