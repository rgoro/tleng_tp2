tokens = [
	'COMENTARIO',
	'NUMERO',
	'PALABRA',
	'COMA',
	'PUNTO',
	'NUMERAL',
	'BARRA',
	'IGUAL',
	'PAREN_L',
	'PAREN_R',
	'LLAVE_L',
	'LLAVE_R',
	'PUNTO_Y_COMA',

	'TEMPO',
	'COMPAS',
	'CONST'
]

def t_COMENTARIO(token):
	r"//.*"
	pass

def t_NUMERO(token):
	r"[1-9][0-9]*"
	token.value = int(token.value)
	return token

def t_PALABRA(token):
	r"\w+"
	token.value = token.value
	return token

def t_NEWLINE(token):
  r"\n+"
  token.lexer.lineno += len(token.value)


t_TEMPO = r"\#tempo"
t_COMPAS = r"\#compas"
t_CONST = r"const"
t_COMA = r","
t_PUNTO = r"\."
t_NUMERAL = r"\#"
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
