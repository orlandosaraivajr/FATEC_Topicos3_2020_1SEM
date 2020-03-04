#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def elementos_repetidos(lista_com_elementos):
    return list(set(lista_com_elementos))


assert elementos_repetidos([1, 2, 1, 1, 1, 3]) == [1,2,3]


elementos_duplicados = [(1,2),(1,2),(2,2),(1,2),(3,2)]

# Set
elementos_campo1 = [1,2,3,4,5,6,7,8,9,11,13,15]
elementos_campo2 = [11,13,15,21,22,24,25,28]

campo1 = set(elementos_campo1)
campo2 = set(elementos_campo2)

campo1.intersection(campo2)
campo1.union(campo2)
campo2.union(campo1)
campo1.difference(campo2)

1 in campo1
1 in campo2

#Dicionário
dicionario = {}
dicionario['fatec'] = "Araras"
dicionario['Orlando'] = ['Orlando','Saraiva']
dicionario[1] = [1,[3,4,5,6],3,4]

dicionario[1] # Vai dar certo
dicionario[2] # Vai dar ruim
dicionario.keys()
dicionario.values()

import json

r = {'is_claimed': 'True', 'rating': 3.5}
r = json.dumps(r)
loaded_r = json.loads(r)
loaded_r['rating'] #Output 3.5
type(r) #Output str
type(loaded_r) #Output dict
