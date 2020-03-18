#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 21:03:30 2020

@author: orlando
"""

# content of test_sample.py
def inc(x):
    return x + 1


def test_answer_fail():
    assert inc(3) == 5

def test_answer_ok_1():
    assert inc(3) == 4
    
def test_answer_ok_1():
    x = inc(3)
    assert inc(x) == 5
    
def funcao_capitalize(nome):
    try:
        nome = nome.capitalize()
        return nome
    except:
        return None


def test_funcao_capitalize_fail():
    assert funcao_capitalize(3) == 'Oi mundo'
    
def test_funcao_capitalize_1_ok():
    assert funcao_capitalize('oi mundo') == 'Oi mundo'            
    
def test_funcao_capitalize_2_ok():
    assert funcao_capitalize([1,2,3]) == None