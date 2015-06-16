# -*- coding: utf-8 -*-
tokens = [
    # Caracteres sueltos
    'COMA',
#    'PUNTO',
#    'MENOS',
#    'MAS',
    'BARRA',
    'IGUAL',
    'PAREN_L',
    'PAREN_R',
    'LLAVE_L',
    'LLAVE_R',
    'PUNTO_Y_COMA',

    # palabras clave
    'DEF_TEMPO',
    'DEF_COMPAS',
    'VOZ',
    'CONST',
    'COMPAS',
    'NOTA',
    'SILENCIO',

    # Elementos musicales
    'ALTURA',
    'DURACION',

    # Varios
    'COMENTARIO',
    'NUMERO',
    'CONSTANTE',
]

t_DEF_TEMPO = r"\#tempo"
t_DEF_COMPAS = r"\#compas"

def t_COMENTARIO(token):
    r"//[^\n]*"
    pass

def t_NUMERO(token):
    r"[1-9][0-9]*"
    token.value = int(token.value)
    return token

# Estos cinco pensé que se podían definir como simples, pero no, si los
# definimos como «t_CONST = r"const"», se lexerean (?) como t_CONSTANTE.
# Además, las notas tienen que ir abajo, si no "silencio" se parsea como 
# "Altura(si) Constante(lencio)"
def t_CONST(token):
    r"const"
    return token

def t_VOZ(token):
    r"voz"
    return token

def t_COMPAS(token):
    r"compas"
    return token

def t_NOTA(token):
    r"nota"
    return token

def t_SILENCIO(token):
    r"silencio"
    return token

# Quizás sea un error incorporar los bemoles/sostenidos y los puntillos a
# estos dos tokens, se verá cuánto nos complica la vida.
def t_ALTURA(token):
    r"(do|re|mi|fa|sol|la|si)(-|\+)?"
    return token

def t_DURACION(token):
    r"(redonda|blanca|negra|corchea|semicorchea|fusa|semifusa)(\.)?"
    return token

def t_CONSTANTE(token):
    r"\w+"
    return token

def t_NEWLINE(token):
  r"\n+"
  token.lexer.lineno += len(token.value)

t_COMA = r","
#t_PUNTO = r"\."
#t_MENOS = r"-"
#t_MAS = r"\+"
t_BARRA = r"/"
t_IGUAL = r"="
t_PAREN_L = r"\("
t_PAREN_R = r"\)"
t_LLAVE_L = r"\{"
t_LLAVE_R = r"\}"
t_PUNTO_Y_COMA = r";"

t_ignore = " \t"

def t_error(token):
    message = "Token desconocido:"
    message += "\ntype:" + token.type
    message += "\nvalue:" + str(token.value)
    message += "\nline:" + str(token.lineno)
    message += "\nposition:" + str(token.lexpos)
    raise Exception(message)
