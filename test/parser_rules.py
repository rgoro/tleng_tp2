# -*- coding: utf-8 -*-

from lexer_rules import tokens

from expressions import Number


def p_lista(subexpressions):
    'lista : LLAVE_L numeros LLAVE_R'
    subexpressions[0] = subexpressions[2]
    subexpressions[0].reverse()


def p_numeros_numero(subexpressions):
    'numeros : NUMERO'
    subexpressions[0] = [Number(subexpressions[1])]

def p_numeros_coma(subexpressions):
    'numeros : NUMERO COMA numeros'
    subexpressions[0] = subexpressions[3]
    subexpressions[0].append(Number(subexpressions[1]))


def p_error(subexpressions):
    raise Exception("Syntax error.")
