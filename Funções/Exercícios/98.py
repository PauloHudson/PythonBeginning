#faca um programa que tenha uma funcao chamada contador()
#que receba tres parametros: inicio, fim e passo
# e reakuze a contagem
# seu programa tem que realizar tres contagens atraves da funcao criada
#a de 1 ate 10, de 1 em 1
#b de 10 áte 0, de 2 em 2 
#c uma contagem personalizada. 
from time import sleep

def linha():
    print('=-=' * 10)
#inicio #fim #passo

def contador(inicio, fim, passo): 
    if passo == 0:
        passo = 1
    if passo < 0:
        passo = abs(passo)
    if inicio > fim:
        passo = -passo
        fim -= 2
    print(f'Contador de {inicio} até {fim} de {passo} em {passo}')
    for c in range(inicio, fim, passo):
        print(c, end=' ', flush=True)
        sleep(0.3)
    print()
        
linha()
contador(1, 10, 1)
linha()
contador(10, 0, 2)
print('=-=' * 10)
contador(int(input('Digite o ínicio: ')), int(input('Ditite o fim: ')), int(input('Digite o passo: ')))