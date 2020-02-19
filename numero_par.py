#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def numero_par(numeros):
    for numero in numeros:
        if numero % 2 == 0:
            print(numero)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# numero_par(numeros)

"""
Crie uma função que recebe uma string e 
retorne a mesma string formtatada com "|"
e letras maiusculas

Exemplo
Orlando => |O|R|L|A|N|D|O|
Ana     => |A|N|A|
"""

def converte_nome(nome):
    try:
        return '|'+'|'.join(nome.upper())+'|'
    except:
        return ''
    
    
'''
    novo_nome = '|'
    nome = nome.upper()
    for letra in nome:
        novo_nome += letra
        novo_nome += '|'
    return novo_nome
'''



assert(converte_nome('Ana') == '|A|N|A|')
assert(converte_nome('Orlando') == '|O|R|L|A|N|D|O|')
assert(converte_nome([1,2,3]) == '')
assert(converte_nome((1,2,3)) == '')





