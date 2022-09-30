from collections.abc import MutableSequence


# Em outras linguagens, há a ideia de classes e métodos abstratos, que forçam as classes filhas a
# implementar alguns métodos.
#
# Para fazer o mesmo no Python, é possível usar classes abstratas, as chamadas ABC (A*bstract *Base Classes).
# Existem classes já prontas que ajudam nessa ideia.
#
# Para exemplificar, crie um novo arquivo com o nome testeAbc.py, para teste, com o seguinte conteúdo e execute-o:


class MinhaListinhaMutavel(MutableSequence):
    pass


# Você vai perceber que não acontece nada quando apenas este código é executado.
#
# 5) A classe MinhaListinhaMutavel herda de MutableSequence, ou seja, é desejável que o Python
# avise que tem que implementar todos os métodos abstratos de uma MutableSequence.
# Só que parece que não funcionou.
#
# Como Python é uma linguagem de tipagem dinâmica, não dá pra ter essa garantia
# só percorrendo o código de definição da classe. O que dá pra fazer é validar os métodos
# em tempo de instanciação. Adicione o código abaixo e teste novamente:


objetoValidado = MinhaListinhaMutavel()
print(objetoValidado)

# Agora dá um erro, dizendo que você esqueceu de implementar todos os métodos
# necessários para tornar a classe uma MutableSequence.
#
# Sempre que você quiser garantir a implementação de alguns métodos, pode recorrer às
# classes já existentes em collections.abc e outros pacotes também.

# Nesta aula, aprendemos sobre:
#
# Duck typing
# Python data (object) model
# Dunder methods
# Uso de ABCs