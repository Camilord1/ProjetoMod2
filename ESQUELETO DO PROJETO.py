import pandas as pd
from datetime import datetime


def menu():
    print('='*60)
    print('\n Olá, bem vindo(a) a pesquisa sobre o Mercado Tech no Brasil! \n')
    print('='*60)
    print('lembre-se de utilizar as opções válidas')
    nome = input('Insira seu nome: ')
    idade = input('Insira sua idade: ')
    genero = input('Insira seu gênero: ')
    
menu()

class Pessoa():
    def __init__(self, idade, nome, genero):
        self.idade = idade
        self._nome = nome
        self.genero = genero

    def setNome(self, nomePessoa):
        self._nome = nomePessoa
    
    def getNome(self):
        return self._nome

class Entrevista(Pessoa):
    def __init__(self, idade, nome, genero, perg01, perg02, perg03, perg04):
        Pessoa.__init__(self,idade,nome,genero)
        self.perg01 = perg01
        self.perg02 = perg02
        self.perg03 = perg03
        self.perg04 = perg04

    def resgatarDadosEntrevista(self):
        return f'O nome do candidato(a) {self.getNome()}, idade {self.idade}, gênero {self.genero} e as repostas {self.perg01}, {self.perg02}, {self.perg03} e {self.perg04}'

""" Variáveis globais
"""
condicao = True # Variavel usada no laço para sair do while quando digitar 00
data_atual = datetime.now().strftime('%Y-%m-%d %H:%M') # Variável que armazena a data e hora atual formatada
respostas = [] # Lista que armazena todas as respostas

while condicao:
    
    escolha_idade = int(input('Digite sua idade: '))

    if escolha_idade == 00:

        print('\nFinalizando as entrevistas. \nObrigado pela atenção!\n')
        condicao = False

    elif escolha_idade != 00:

        nome_entrevistado = input('Informe seu nome: ')
        escolha_genero = input('Informe seu gênero: \n[1] F \n[2] M \n[3] Outro\n= ')

        perg01 = input('Você sabia que o mercado de tecnologia no Brasil abre mais de 500 mil vagas por ano? \n[1] Sim\n[2] Não\n[3] Não sei responder\n= ')
        perg02 = input('Você trabalha ou conhece alguém que trabalhe com tecnologia? \n[1] Sim\n[2] Não\n[3] Não sei responder\n= ')
        perg03 = input('Você acredita que o mercado de trabalho tecnológico é diversificado (mulheres, LGBTQIA+, PCD, idade)? \n[1] Sim\n[2] Não\n[3] Não sei responder\n= ')
        perg04 = input('Você acredita que em seis meses um profissional pode estar capacitado para trabalhar nessa área? \n[1] Sim\n[2] Não\n[3] Não sei responder\n= ')
        
        objeto_pesquisa = Entrevista(escolha_idade, nome_entrevistado, escolha_genero, perg01, perg02, perg03, perg04)
        print(objeto_pesquisa.resgatarDadosEntrevista())

        respostas.append([escolha_idade, escolha_genero, perg01, perg02, perg03, perg04, data_atual])

    else:
        print('Ocorreu algum problema!')

print('Lista das respostas da pesquisa: ',respostas)


df = pd.DataFrame(respostas)
df.to_csv('teste.csv')
print(df.head())