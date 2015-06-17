# -*- coding: utf-8 -*-

from lexer_rules import tokens

from expressions import *

def p_musilen(sub):
    'musilen : def_tempo def_compas constantes voces'
    sub[0] = MusiLen(sub[1], sub[2], sub[3], sub[4])

def p_def_tempo(sub):
    'def_tempo : DEF_TEMPO DURACION num'
    sub[0] = DefTempo(Duracion(sub[2]), sub[3])

def p_def_compas(sub):
    'def_compas : DEF_COMPAS num BARRA num'
    sub[0] = DefCompas(Numero(sub[2]), sub[4])

def p_constantes(sub):
    '''constantes : constante PUNTO_Y_COMA
                  | constante PUNTO_Y_COMA constantes'''
    if len(sub) == 3:
        sub[0] = [sub[1]]
    else:
        sub[0] = sub[3]
        sub[0].insert(0, sub[1])

def p_constante(sub):
    'constante : CONST label IGUAL num'
    sub[0] = Constante(sub[2], sub[4])

def p_voces(sub):
    '''voces : voz LLAVE_R
             | voz LLAVE_R voces'''
    if len(sub) == 3:
        sub[0] = [sub[1]]
    else:
        sub[0] = sub[3]
        sub[0].insert(0, sub[1])

def p_voz(sub):
    'voz : VOZ PAREN_L var PAREN_R LLAVE_L lista_compases'
    sub[0] = Voz(sub[3], sub[6])

                      #| lista_compases compases
                      #| lista_compases repetir'''
def p_lista_compases(sub):
    '''lista_compases : compases
                      | repetir'''
    if len(sub) == 2:
        sub[0] = sub[1]
    elif len(sub) == 3:
        sub[0] = sub[1] + sub[2]
    else:
        sub[0] = sub[1] + sub[3] + sub[5]

def p_compases(sub):
    '''compases : compas LLAVE_R
                | compas LLAVE_R compases'''
    if len(sub) == 3:
        sub[0] = [sub[1]]
    else:
        sub[0] = sub[3]
        sub[0].insert(0, sub[1])

def p_repetir(sub):
    'repetir : REPETIR PAREN_L NUMERO PAREN_R LLAVE_L compases'
    sub[0] = []
    for i in range(int(sub[3])):
        sub[0] += sub[6]

def p_compas(sub):
    'compas : COMPAS LLAVE_L figuras'
    sub[0] = Compas(sub[3])

def p_figuras(sub): 
    '''figuras : figura PUNTO_Y_COMA
               | figura PUNTO_Y_COMA figuras'''
    if len(sub) == 3:
        sub[0] = [sub[1]]
    else:
        sub[0] = sub[3]
        sub[0].insert(0, sub[1])
    
def p_figura(sub):
    '''figura : nota
              | silencio'''
    sub[0] = sub[1]

def p_nota(sub):
    'nota : NOTA PAREN_L ALTURA COMA var COMA DURACION PAREN_R'
    sub[0] = Nota(Altura(sub[3]), sub[5], Duracion(sub[7]))
    
def p_silencio(sub):
    'silencio : SILENCIO PAREN_L DURACION PAREN_R'
    sub[0] = Silencio(Duracion(sub[3]))

def p_var(sub):
    '''var : num
           | label'''
    sub[0] = sub[1]

def p_num(sub):
    'num : NUMERO'
    sub[0] = int(sub[1])

def p_label(sub):
    'label : CONSTANTE'
    sub[0] = sub[1]

#def p_error(sub):
#    raise Exception("Syntax error.")

