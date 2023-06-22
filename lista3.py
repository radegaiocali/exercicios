# 1- Classe Bola: Crie uma classe que modele uma bola:
# a) Atributos: Cor, circunferência, material
# b) Métodos: trocaCor e mostraCor

class bola:
    def __init__(self, cor, circunferencia, material):
        self.cor= cor
        self.circunferencia= circunferencia
        self.material= material
    def trocaCor (self,cor):
        self.cor= cor

    def mostraCor (self):
        return self.cor
     
bolaA= bola('rosa', 10 ,'fibra')
print(bolaA.mostraCor())
bolaA.trocaCor('cinza')
print(bolaA.mostraCor())
print()

# 2- Classe Quadrado: Crie uma classe que modele um quadrado:
#Atributos: Tamanho do lado
#Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Quadrado:
     def __init__(self, lado):
        self.lado= lado
    
     def mudaValor (self,valor):
        self.valor= valor

     def mostraValor (self):
        return self.valor

     def calculoArea (self):
        return self.lado*self.lado

qA= Quadrado(24)

print(qA.calculoArea())
print()

# 3- Classe Retangulo: Crie uma classe que modele um retangulo:
#a. Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
#b. Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
#c. Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois, 
# deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.

class Retangulo():
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def trocarValorbase(self, base):
        self.nova__base = base

    def trocarValoraltura(self, altura):
        self.nova__altura = altura

    def retornaValorbase(self):
        return self.base

    def calculoArea(self):
        return self.base*self.altura

    def calculoPerimetro(self):
        return self.base+self.base+self.altura+self.altura

bas= int(input('Informe o valor da base do retangulo'))
alt= int(input('Informe o valor da altura do retangulo'))
r1= Retangulo(bas,alt)
print('A área é: ', r1.calculoArea())
print('O perímetro é: ', r1.calculoPerimetro())
print()

#4- Classe Pessoa: Crie uma classe que modele uma pessoa:
#a) Atributos: nome, idade, peso e altura
#b) Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela
# menor que 21 anos, ela deve crescer 0,5 cm.
class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome= nome
        self.idade= idade
        self.peso= peso
        self.altura= altura

    def envelhecer (self,anos):
        self.idade +=anos
        if self.idade <21:
           self.cresce(anos)

    def crescer (self, anos):
        if self.idade <21:
           self.altura += 0.5 * anos

    def engordar (self, peso):
        self.peso += peso

    def emagrecer (self, peso):
        self.peso -= peso

    def altura (self):
        self.altura += altura

y= Pessoa("Aline", 16, 68, 1.68)
print(y.nome)
print(y.idade)
print(y.peso)
print(y.altura)

#5- Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. 
#A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo. 
#Os métodos são os seguintes: alterarNome, depósito e saque; 
#No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatório

class ContaCorrente:
 def __init__(self, num_conta, nome_correntista, saldo):
     self.num_conta= num_conta
     self.nome_correntista= nome_correntista  
     self.saldo= saldo  
     

def alterarNome (self, novo_nome):
     self.nome_correntista= novo_nome

def depositou (self,inseriu_dinheiro):
    self.saldo+= inseriu_dinheiro

def saque (self, retirou_dinheiro):
    self.saldo-= retirou_dinheiro

usuario1= ContaCorrente(2750, 'Joao', 50)
print(usuario1.saldo)


 # 6- Classe TV: Faça um programa que simule um televisor criando-o como um objeto. O usuário deve ser capaz de informar 
 # o número do canal e aumentar ou diminuir o volume. 
#Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.


class Tv:
    def __init__(self, polegadas, marca):
        self.polegadas= polegadas
        self.marca= marca
        self.canal(0)
        self.vol_min= 0
        self.vol_max= 60
        self.volume= volume


    def trocarCanal (self):
        if (canal>0) and (canal<=100):
            self.canal= canal


    def aumentarVol (self):
        if self.vol_min < self.volume <= self.vol_max:
            self.volume+= 1

    def diminuirVol (self):
        if self.volume >0:
            self.volume-= 1

tv= Tv(50, LG)
canal= input("informe o canal que deseja assitir")



    


    


