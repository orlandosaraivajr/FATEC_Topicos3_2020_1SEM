#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Baralho como sequencia de cartas
Extraido do capítulo 1 do livro "Python Fluente"
"""

import collections

Card = collections.namedtuple('Card',['rank','suit'])

class Baralho:
    ranks = [str(n) for n in range(2,11)] +list('JQKA')
    suits = 'espada ouros copa paus'.split()
    
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
    
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]


baralho = Baralho()

from random import choice
carta_escolhida = choice(baralho)