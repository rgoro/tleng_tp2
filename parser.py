#!/usr/bin/python
# -*- coding: utf-8 -*-
import lexer_rules
import parser_rules

from sys import argv, exit

from ply.lex import lex
from ply.yacc import yacc

if __name__ == "__main__":
    if len(argv) != 2:
        print "Parametros invalidos."
        print "Uso:"
        print "  parser.py archivo_entrada"
        exit(1)

    input_file = open(argv[1], "r")
    text = input_file.read()
    input_file.close()

    lexer = lex(module=lexer_rules)
    parser = yacc(module=parser_rules)

    try:
        algo = parser.parse(text, lexer)
        midicomp = algo.get_midicomp()
        print midicomp
    except Exception as e:
        print e.message
        exit(1)
