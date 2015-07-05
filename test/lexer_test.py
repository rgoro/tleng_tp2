#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from unittest import TestCase

from ply.lex import lex

import lexer_rules

class TestLexer(TestCase):
    def setUp(self):
        self.lexer = lex(module=lexer_rules)

    def test_def_tempo(self):
        text = "#tempo"
        self.lexer.input(text)
        token = self.lexer.token()
        self.assertEqual(token.type, "DEF_TEMPO")

    def test_def_compas(self):
        text = "#compas"
        self.lexer.input(text)
        token = self.lexer.token()
        self.assertEqual(token.type, "DEF_COMPAS")

    def test_comentario(self):
        text = "//compas"
        self.lexer.input(text)
        token = self.lexer.token()
        self.assertEqual(token, None)

    def test_compas_y_comentario(self):
        text = "#compas //fruta"
        self.lexer.input(text)
        token = self.lexer.token()
        self.assertEqual(token.type, "DEF_COMPAS")
        token = self.lexer.token()
        self.assertEqual(token, None)

    def test_cuatro_numeros(self):
        text = "0 1 10 00"
        self.lexer.input(text)

        token = self.lexer.token()
        self.assertEqual(token.type, "NUMERO")
        self.assertEqual(token.value, 0)
        token = self.lexer.token()
        self.assertEqual(token.type, "NUMERO")
        self.assertEqual(token.value, 1)
        token = self.lexer.token()
        self.assertEqual(token.type, "NUMERO")
        self.assertEqual(token.value, 10)
        token = self.lexer.token()
        self.assertEqual(token.type, "NUMERO")
        self.assertEqual(token.value, 0)

    def test_palabras_claves(self):
        text = "const voz compas nota silencio repetir"
        self.lexer.input(text)

        token = self.lexer.token()
        self.assertEqual(token.type, "CONST")
        token = self.lexer.token()
        self.assertEqual(token.type, "VOZ")
        token = self.lexer.token()
        self.assertEqual(token.type, "COMPAS")
        token = self.lexer.token()
        self.assertEqual(token.type, "NOTA")
        token = self.lexer.token()
        self.assertEqual(token.type, "SILENCIO")
        token = self.lexer.token()
        self.assertEqual(token.type, "REPETIR")

    def test_duraciones(self):
        text = "redonda blanca negra corchea semicorchea fusa semifusa"
        text += " redonda. blanca. negra. corchea. semicorchea. fusa. semifusa."
        self.lexer.input(text)

        token = self.lexer.token()
        self.assertEqual(token.type, "DURACION")
        self.assertEqual(token.value, "redonda")
        token = self.lexer.token()
        self.assertEqual(token.type, "DURACION")
        self.assertEqual(token.value, "blanca")
        token = self.lexer.token()
        self.assertEqual(token.type, "DURACION")
        self.assertEqual(token.value, "negra")
        token = self.lexer.token()
        self.assertEqual(token.type, "DURACION")
        self.assertEqual(token.value, "corchea")
        token = self.lexer.token()
        self.assertEqual(token.type, "DURACION")
        self.assertEqual(token.value, "semicorchea")
        token = self.lexer.token()
        self.assertEqual(token.type, "DURACION")
        self.assertEqual(token.value, "fusa")
        token = self.lexer.token()
        self.assertEqual(token.type, "DURACION")
        self.assertEqual(token.value, "semifusa")
        token = self.lexer.token()
        self.assertEqual(token.type, "DURACION")
        self.assertEqual(token.value, "redonda.")
        token = self.lexer.token()
        self.assertEqual(token.type, "DURACION")
        self.assertEqual(token.value, "blanca.")
        token = self.lexer.token()
        self.assertEqual(token.type, "DURACION")
        self.assertEqual(token.value, "negra.")
        token = self.lexer.token()
        self.assertEqual(token.type, "DURACION")
        self.assertEqual(token.value, "corchea.")
        token = self.lexer.token()
        self.assertEqual(token.type, "DURACION")
        self.assertEqual(token.value, "semicorchea.")
        token = self.lexer.token()
        self.assertEqual(token.type, "DURACION")
        self.assertEqual(token.value, "fusa.")
        token = self.lexer.token()
        self.assertEqual(token.type, "DURACION")
        self.assertEqual(token.value, "semifusa.")

    def test_alturas(self):
        text = "do re mi fa sol la si"
        text += "do- re- mi- fa- sol- la- si-"
        text += "do+ re+ mi+ fa+ sol+ la+ si+"
        self.lexer.input(text)

        token = self.lexer.token()
        self.assertEqual(token.type, "ALTURA")
        self.assertEqual(token.value, "do")
        token = self.lexer.token()
        self.assertEqual(token.type, "ALTURA")
        self.assertEqual(token.value, "re")
        token = self.lexer.token()
        self.assertEqual(token.type, "ALTURA")
        self.assertEqual(token.value, "mi")
        token = self.lexer.token()
        self.assertEqual(token.type, "ALTURA")
        self.assertEqual(token.value, "fa")
        token = self.lexer.token()
        self.assertEqual(token.type, "ALTURA")
        self.assertEqual(token.value, "sol")
        token = self.lexer.token()
        self.assertEqual(token.type, "ALTURA")
        self.assertEqual(token.value, "la")
        token = self.lexer.token()
        self.assertEqual(token.type, "ALTURA")
        self.assertEqual(token.value, "si")
        token = self.lexer.token()
        self.assertEqual(token.type, "ALTURA")
        self.assertEqual(token.value, "do-")
        token = self.lexer.token()
        self.assertEqual(token.type, "ALTURA")
        self.assertEqual(token.value, "re-")
        token = self.lexer.token()
        self.assertEqual(token.type, "ALTURA")
        self.assertEqual(token.value, "mi-")
        token = self.lexer.token()
        self.assertEqual(token.type, "ALTURA")
        self.assertEqual(token.value, "fa-")
        token = self.lexer.token()
        self.assertEqual(token.type, "ALTURA")
        self.assertEqual(token.value, "sol-")
        token = self.lexer.token()
        self.assertEqual(token.type, "ALTURA")
        self.assertEqual(token.value, "la-")
        token = self.lexer.token()
        self.assertEqual(token.type, "ALTURA")
        self.assertEqual(token.value, "si-")
        token = self.lexer.token()
        self.assertEqual(token.type, "ALTURA")
        self.assertEqual(token.value, "do+")
        token = self.lexer.token()
        self.assertEqual(token.type, "ALTURA")
        self.assertEqual(token.value, "re+")
        token = self.lexer.token()
        self.assertEqual(token.type, "ALTURA")
        self.assertEqual(token.value, "mi+")
        token = self.lexer.token()
        self.assertEqual(token.type, "ALTURA")
        self.assertEqual(token.value, "fa+")
        token = self.lexer.token()
        self.assertEqual(token.type, "ALTURA")
        self.assertEqual(token.value, "sol+")
        token = self.lexer.token()
        self.assertEqual(token.type, "ALTURA")
        self.assertEqual(token.value, "la+")
        token = self.lexer.token()
        self.assertEqual(token.type, "ALTURA")
        self.assertEqual(token.value, "si+")
    
    def test_constante(self):
        text = "alguna cosa"
        self.lexer.input(text)

        token = self.lexer.token()
        self.assertEqual(token.type, "CONSTANTE")
        self.assertEqual(token.value, "alguna")
        token = self.lexer.token()
        self.assertEqual(token.type, "CONSTANTE")
        self.assertEqual(token.value, "cosa")

    def test_constante_incluyendo_nota(self):
        text = "lalonde"
        self.lexer.input(text)

        token = self.lexer.token()
        self.assertEqual(token.type, "ALTURA")
        self.assertEqual(token.value, "la")
        token = self.lexer.token()
        self.assertEqual(token.type, "CONSTANTE")
        self.assertEqual(token.value, "londe")

if __name__ == '__main__':
    unittest.main()
