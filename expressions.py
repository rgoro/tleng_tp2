# -*- coding: utf-8 -*-

class Numero(object):
    def __init__(self, valor):
        self.valor = valor

    def __repr__(self):
        return str(self.valor)

class Duracion(object):
    def __init__(self, valor):
        self.puntillo = '.' in valor
        self.valor = valor.strip('.')

    def __repr__(self):
        return self.valor + ("." if self.puntillo else "")

class Altura(object):
    def __init__(self, valor):
        self.sostenido = '+' in valor
        self.bemol = '-' in valor
        self.valor = valor.strip('+-')

    def __repr__(self):
        return self.valor + ("+" if self.sostenido else ("-" if self.bemol else ""))

class DefTempo(object):
    def __init__(self, duracion, valor):
        self.duracion = duracion
        self.valor = valor

    def __repr__(self):
        return "tempo: " + self.duracion + " = " + self.valor


# FIXME lo llamo duracion, pero ahí va un número, no un objeto Duracion
class DefCompas(object):
    def __init__(self, tiempos, duracion):
        self.tiempos = tiempos
        self.duracion = duracion

    def __repr__(self):
        return "compas: " + self.tiempos + "/" + self.duracion

class Constante(object):
    def __init__(self, label, valor):
        self.valor = (label, valor)

    def __repr__(self):
        return str(self.valor)

class Compas(object):
    def __init__(self, figuras):
        self.figuras = figuras
    
    def __repr__(self):
        return str(self.figuras)

#Uso herencia por instinto de programador, no estoy seguro si la voy a necesitar.
class Figura(object):
    pass

class Nota(Figura):
    def __init__(self, altura, octava, duracion):
        self.altura = altura
        self.octava = octava
        self.duracion = duracion

    def __repr__(self):
        return "Nota: <" + self.altura + " -- " + self.octava + " -- " + self.duracion + ">"

class Silencio(Figura):
    def __init__(self, duracion):
        self.duracion = duracion

    def __repr__(self):
        return "Silencio: <" + self.duracion + ">"

class Voz(object):
    def __init(self, instrumento, compases):
        self.instrumento = instrumento
        self.compases = compases

    def __repr__(self):
        return str(self.instrumento) + ": " + str(self.compases)

class MusiLen(object):
    def __init__(self, def_tempo, def_compas, constantes, voces):
        self.def_tempo = def_tempo
        self.def_compas = def_compas
        self.constantes = constantes
        self.voces = voces

    def __repr__(self):
        return "Musilen {\n\t" + str(self.def_tempo) + "\n\t" + str(self.def_compas) + "\n\t" + self.constantes + "\n\t" + self.voces + "\n}"

