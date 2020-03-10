# -*- coding: utf-8 -*-
"""
Projeto 7 a 1 ( em Python )

Created on Tue Mar 10 07:04:48 2020

@author: Orlando Saraiva Jr
"""

import collections

Figurinha = collections.namedtuple('Figurinha',['numero','legenda'])

album = []
repetidas = []


def comprar_figurinha(numero, legenda):
    nova_figurinha = Figurinha(numero, legenda)
    if nova_figurinha in album:
        repetidas.append(Figurinha(numero, legenda))
    else:
        album.append(Figurinha(numero, legenda))

def main():
    opcao = 0
    while opcao is not 3:
        print('''
            MENU:
    
            [1] - Cadastrar nova figurinha
            [2] - Verificar figurinhas presentes
            [3] - Sair
        ''')
        opcao = int(input('Escolha uma opção: '))
        if opcao == 1:
            numero = int(input('Digite o número da figurinha '))
            legenda = input('Digite o nome do jogador ')
            comprar_figurinha(numero, legenda)
        if opcao == 2:
            print('Controle de repetidas')
            print(repetidas)
            print('Album de figurinhas')
            print(album)
  
if __name__== "__main__":
  main()
