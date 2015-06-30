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

    def get_valor_tempo(self):
        if self.valor == "redonda":
            return 1
        elif self.valor == "blanca":
            return 2
        elif self.valor == "negra":
            return 4
        elif self.valor == "corchea":
            return 8
        elif self.valor == "semicorchea":
            return 16
        elif self.valor == "fusa":
            return 32
        elif self.valor == "semifusa":
            return 64

    def __repr__(self):
        return self.valor + (" con puntillo" if self.puntillo else "")

class Altura(object):
    def __init__(self, valor):
        self.sostenido = '+' in valor
        self.bemol = '-' in valor
        self.valor = valor.strip('+-')

    def __repr__(self):
        return self.valor + (" sostenido" if self.sostenido else (" bemol" if self.bemol else ""))

class DefTempo(object):
    def __init__(self, duracion, valor):
        self.duracion = duracion
        self.valor = valor

    def get_tempo_midi(self):
        return (1000000 * 60 * self.duracion.get_valor_tempo())/(4 * self.valor)

    def __repr__(self):
        return "tempo: " + str(self.duracion) + " = " + str(self.valor)


# FIXME lo llamo duracion, pero ahí va un número, no un objeto Duracion
class DefCompas(object):
    def __init__(self, tiempos, duracion):
        self.tiempos = tiempos
        self.duracion = duracion

    def __repr__(self):
        return "compas: " + str(self.tiempos) + "/" + str(self.duracion)

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
        return "Nota: <" + str(self.altura) + " -- " + str(self.octava) + " -- " + str(self.duracion) + ">"

class Silencio(Figura):
    def __init__(self, duracion):
        self.duracion = duracion

    def __repr__(self):
        return "Silencio: <" + str(self.duracion) + ">"

class Voz(object):
    def __init__(self, instrumento, compases):
        self.instrumento = instrumento
        self.compases = compases

    def __repr__(self):
        return str(self.instrumento) + ": " + str(self.compases)

class MusiLen(object):
    def __init__(self, def_tempo, def_compas, constantes, voces):
        self.def_tempo = def_tempo
        self.def_compas = def_compas
        self.constantes = dict(constantes)
        self.voces = voces

    def reemplazar_constantes(self):
        for voz in self.voces:
            if voz.instrumento in self.constantes.keys():
                voz.instrumento = self.constantes[voz.instrumento]

            for compas in voz.compases:
                for figura in compas.figuras:
                    if type(figura) == Nota and figura.octava in self.constantes.keys():
                        figura.octava = self.constantes[figura.octava]

            
    def get_header(self):
        header = "MFile1 " + str(len(self.voces)) + "384\n\n"
        header += "Mtrk\n"
        header += "000:00:000 TimeSig " + str(self.def_compas) + " 24 8\n"
        header += "000:00:000 Tempo " + str(self.def_tempo.get_tempo_midi()) + "\n"
        header += "000:00:000 Meta TrkEnd\n"
        header += "TrkEnd\n"

        return header

    def __repr__(self):
        return "Musilen {\n\t" + str(self.def_tempo) + "\n\t" + str(self.def_compas) + "\n\t" + str(self.constantes) + "\n\t" + str(self.voces) + "\n}"

