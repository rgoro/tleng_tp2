# -*- coding: utf-8 -*-

tokens = [
	# Caracteres sueltos
	'COMA',
	'LLAVE_L',
	'LLAVE_R',

	'NUMERO',
]

def t_NUMERO(token):
	r"[1-9][0-9]*"
	token.value = int(token.value)
	return token

t_ignore = " \t"

t_COMA = r","
t_LLAVE_L = r"\["
t_LLAVE_R = r"\]"

def t_NEWLINE(token):
  r"\n+"
  token.lexer.lineno += len(token.value)

def t_error(token):
    message = "Token desconocido:"
    message += "\ntype:" + token.type
    message += "\nvalue:" + str(token.value)
    message += "\nline:" + str(token.lineno)
    message += "\nposition:" + str(token.lexpos)
    raise Exception(message)
