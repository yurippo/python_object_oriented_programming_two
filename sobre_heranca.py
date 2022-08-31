class Veiculo:

    def abastecer(self, litros):
        pass

class Carro(Veiculo):
        pass

class Moto(Veiculo):
        pass

#Desta forma, o método abastecer é herdado pelas classes Moto e Carro ;)

#Tenho 2 classes que têm comportamentos iguais:
#Utilizando herança, como posso fazer para remover esta duplicação?