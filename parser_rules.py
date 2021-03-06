# -*- coding: utf-8 -*-

from lexer_rules import tokens

from expressions import *


def p_musilen(sub):
    'musileng : def_tempo def_compas constantes voces'
    sub[0] = Musileng(sub[1], sub[2], sub[3], sub[4])


def p_def_tempo(sub):
    'def_tempo : DEF_TEMPO DURACION num'
    if sub[3] <= 0:
        raise Exception('El #tempo (línea {0}) debe ser mayor a 0'.format(sub.lineno(1)))

    sub[0] = DefTempo(Duracion(sub[2]), sub[3])


def p_def_compas(sub):
    'def_compas : DEF_COMPAS num BARRA num'
    sub[0] = DefCompas(sub[2], sub[4])


def p_constantes(sub):
    '''constantes : empty
                  | constante PUNTO_Y_COMA constantes'''
    if len(sub) == 2:
        sub[0] = []
    else:
        sub[0] = sub[3]
        if sub[1][0] not in [x for (x, y) in sub[0]]:
            sub[0].insert(0, (sub[1][0], sub[1][1]))
        else:
            raise Exception("Constante {0} definida dos veces (línea {1})".format(sub[1][0], sub[1][2]))


def p_constante(sub):
    'constante : CONST CONSTANTE IGUAL num'
    sub[0] = (sub[2], sub[4], sub.lineno(1))


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
    sub[0] = Voz(sub[3], sub[6], sub.lineno(1))


def p_lista_compases(sub):
    '''lista_compases : compases
                      | repetir
                      | lista_compases compases
                      | lista_compases repetir'''
    if len(sub) == 2:
        sub[0] = sub[1]
    elif len(sub) == 3:
        sub[0] = sub[1] + sub[2]


def p_compases(sub):
    '''compases : compas LLAVE_R
                | compas LLAVE_R compases'''
    if len(sub) == 3:
        sub[0] = [sub[1]]
    else:
        sub[0] = sub[3]
        sub[0].insert(0, sub[1])


def p_repetir(sub):
    'repetir : REPETIR PAREN_L NUMERO PAREN_R LLAVE_L compases LLAVE_R'
    sub[0] = []
    if sub[3] < 1:
        raise Exception("Repetir con N < 1. Linea con error {0}. Valor del repetir {1}".format(sub.lineno(1), sub[3]))
    for i in range(sub[3]):
        sub[0] += sub[6]


def p_compas(sub):
    'compas : COMPAS LLAVE_L figuras'
    sub[0] = Compas(sub[3], sub.lineno(1))


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
    sub[0] = Nota(Altura(sub[3]), sub[5], Duracion(sub[7]), sub.lineno(1))


def p_silencio(sub):
    'silencio : SILENCIO PAREN_L DURACION PAREN_R'
    sub[0] = Silencio(Duracion(sub[3]), sub.lineno(1))


def p_var(sub):
    '''var : num
           | CONSTANTE'''
    sub[0] = sub[1]


def p_num(sub):
    'num : NUMERO'
    sub[0] = int(sub[1])


def p_empty(p):
    'empty :'
    pass


def p_error(sub):
    if sub is None:
        raise Exception("Fin de archivo inesperado. ¿No hay voces?")
    else:
        message = "Error de sintáxis en la línea {0}, no esperaba un token «{1}».".format(sub.lineno, sub.type)
        if sub.type == "DEF_COMPAS":
            message += "\nProbablemente faltó el #tempo."
        elif sub.type == "CONST":
            message += "\nProbablemente faltó o el #compas o el ; de una constante."
        elif sub.type == "LLAVE_R":
            message += "\nO falta un ; en una figura o hay algo (voz, repetir o compás) vacío."
        elif sub.type == "NOTA" or sub.type == "SILENCIO":
            message = "Error de sintáxis en la línea {0}, falta un ; en una figura.".format(sub.lineno)

        raise Exception(message)
