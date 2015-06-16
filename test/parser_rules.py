# -*- coding: utf-8 -*-

from lexer_rules import tokens

from expressions import Number


def p_listas(subexpressions):
    '''listas : lista PUNTO_Y_COMA
              | lista PUNTO_Y_COMA listas'''
    if len(subexpressions) == 3:
        subexpressions[0] = [subexpressions[1]]
    else:
        subexpressions[0] = subexpressions[3]
        subexpressions[0].append(subexpressions[1])

def p_lista(subexpressions):
    'lista : LLAVE_L numeros LLAVE_R'
    subexpressions[0] = subexpressions[2]
    subexpressions[0].reverse()


def p_numeros(subexpressions):
    '''numeros : num
               | num COMA numeros'''
    if len(subexpressions) == 2:
        subexpressions[0] = [subexpressions[1]]
    else:
        subexpressions[0] = subexpressions[3]
        subexpressions[0].append(subexpressions[1])

def p_num(subexpressions):
    'num : PAREN_L NUMERO PAREN_R'
    subexpressions[0] = Number(subexpressions[2])

def p_error(subexpressions):
    raise Exception("Syntax error.")
