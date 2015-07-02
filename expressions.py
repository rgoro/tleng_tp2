# -*- coding: utf-8 -*-

from math import ceil

CLICKS_POR_PULSO = 384

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

    def get_clicks(self, clicks_por_redonda):
        f = self.get_valor_tempo()
        clicks = int(clicks_por_redonda / f)
        if self.puntillo:
            clicks = int(clicks * 1.5)

        return clicks

    def __repr__(self):
        return self.valor + (" con puntillo" if self.puntillo else "")

class Altura(object):
    def __init__(self, valor):
        self.sostenido = '+' in valor
        self.bemol = '-' in valor
        self.valor = valor.strip('+-')

    def get_nota_americana(self):
        return self.get_nota() + self.get_modificador()

    def get_nota(self):
        if self.valor == "do":
            return "c"
        elif self.valor == "re":
            return "d"
        elif self.valor == "mi":
            return "e"
        elif self.valor == "fa":
            return "f"
        elif self.valor == "sol":
            return "g"
        elif self.valor == "la":
            return "a"
        elif self.valor == "si":
            return "b"

    def get_modificador(self):
        if self.sostenido:
            return "+"
        elif self.bemol:
            return "-"
        else:
            return ""

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
        return str(self.tiempos) + "/" + str(self.duracion)


#Uso herencia por instinto de programador, no estoy seguro si la voy a necesitar.
class Figura(object):
    def get_pulsos(self, pulso_inicial, clicks_inicial, clicks_por_redonda):
        clicks_total = clicks_inicial + self.duracion.get_clicks(clicks_por_redonda)
        pulso = pulso_inicial + int(ceil(clicks_total / CLICKS_POR_PULSO))
        clicks = clicks_total % CLICKS_POR_PULSO

        return (int(pulso), int(clicks))

class Nota(Figura):
    def __init__(self, altura, octava, duracion):
        self.altura = altura
        self.octava = octava
        self.duracion = duracion

    def get_nota(self):
        return self.altura.get_nota_americana() + str(self.octava)

    def get_midicomp(self, canal, compas, pulso_inicial, click_inicial, cpr, pulsos_por_compas):
        (pulso_final, click_final) = self.get_pulsos(pulso_inicial, click_inicial, cpr)
        midicomp = str(compas).zfill(3) + ":" + str(pulso_inicial).zfill(2) + ":" + str(click_inicial).zfill(3)
        midicomp += " On  ch=" + canal + " note=" + self.get_nota() + "  vol=70\n"
        
        if pulso_final < pulsos_por_compas:
            midicomp += str(compas).zfill(3) + ":" + str(pulso_final).zfill(2) + ":" + str(click_final).zfill(3)
        else:
            midicomp += str(compas + 1).zfill(3) + ":00:000"

        midicomp += " Off ch=" + canal + " note=" + self.get_nota() + "  vol=0\n"

        return (midicomp, pulso_final, click_final)

    def __repr__(self):
        return "Nota: <" + str(self.altura) + " -- " + str(self.octava) + " -- " + str(self.duracion) + ">"

class Silencio(Figura):
    def __init__(self, duracion):
        self.duracion = duracion

    #FIXME Testear que ignorar los pulsos por compas no joda la vida acá.
    def get_midicomp(self, canal, compas, pulso_inicial, clicks_inicial, cpr, ppc):
        (pulso_final, clicks_final) = self.get_pulsos(pulso_inicial, clicks_inicial, cpr)
        midicomp = ""

        return (midicomp, pulso_final, clicks_final)

    def __repr__(self):
        return "Silencio: <" + str(self.duracion) + ">"

class Compas(object):
    def __init__(self, figuras):
        self.figuras = figuras

    def validar(self, nro_voz, nro_compas, def_compas):
        suma_duraciones = 0
        for f in self.figuras:
            duracion = f.duracion.get_valor_tempo()
            if f.duracion.puntillo:
                #print suma_duraciones, "+= 1 /", duracion
                suma_duraciones += 1.0/duracion
                #print suma_duraciones, "+= 1 /", duracion * 0.5
                suma_duraciones += 1.0/duracion * 0.5
            else:
                #print suma_duraciones, "+= 1 /", duracion
                suma_duraciones += 1.0/duracion

        #print suma_duraciones, "?", def_compas.tiempos, "/", def_compas.duracion, "=",  1.0*def_compas.tiempos / def_compas.duracion
        if suma_duraciones < 1.0*def_compas.tiempos / def_compas.duracion:
            raise Exception("Voz {0} incorrecta: el compás {1} es demasiado corto.".format(nro_voz, nro_compas))
        elif suma_duraciones > 1.0*def_compas.tiempos / def_compas.duracion:
            raise Exception("Voz {0} incorrecta: el compás {1} es demasiado largo.".format(nro_voz, nro_compas))
        else:
            return True

    def get_midicomp(self, canal, nro_compas, clicks_por_redonda, pulsos_por_compas):
        pulso = 0
        clicks = 0
        midicomp = ""
        for f in self.figuras:
            (midicomp_figura, pulso, clicks) = f.get_midicomp(canal, nro_compas, pulso, clicks, clicks_por_redonda, pulsos_por_compas)
            midicomp += midicomp_figura

        return midicomp
    
    def __repr__(self):
        return str(self.figuras)

class Voz(object):
    def __init__(self, instrumento, compases):
        self.instrumento = instrumento
        self.compases = compases

    def validar(self, nro_voz, def_compas):
        i = 1
        for c in self.compases:
            c.validar(nro_voz, i, def_compas)
            i += 1

    def get_midicomp(self, id, clicks_por_redonda, pulsos_por_compas):
        midicomp = "MTrk\n"
        midicomp += "000:00:000 Meta TrkName \"Voz " + id + "\"\n"
        midicomp += "000:00:000 ProgCh ch=" + id + " prog=" + str(self.instrumento) + "\n"

        compas = 0
        for c in self.compases:
            midicomp += c.get_midicomp(id, compas, clicks_por_redonda, pulsos_por_compas)
            compas += 1

        midicomp += str(compas).zfill(3) + ":00:000 Meta TrkEnd\n"
        midicomp += "TrkEnd\n"

        return midicomp

    def __repr__(self):
        return str(self.instrumento) + ": " + str(self.compases)

class MusiLen(object):
    def __init__(self, def_tempo, def_compas, constantes, voces):
        self.def_tempo = def_tempo
        self.def_compas = def_compas
        self.constantes = dict(constantes)
        self.voces = voces
        if not self.validar_voces():
            raise Exception("Voces inconsistentes (aunque tendrían que lanzar su propia excepción).")

    def validar_voces(self):
        i = 1
        for v in self.voces:
            v.validar(i, self.def_compas)
            i += 1

        return True

    def get_midicomp(self):
        self.reemplazar_constantes()
        midicomp = self.get_header()
        clicks_por_redonda = CLICKS_POR_PULSO*self.def_compas.duracion
        i = 1
        for voz in self.voces:
            midicomp += voz.get_midicomp(str(i), clicks_por_redonda, self.def_compas.tiempos)
            i += 1

        return midicomp

    def reemplazar_constantes(self):
        for voz in self.voces:
            if voz.instrumento in self.constantes.keys():
                voz.instrumento = self.constantes[voz.instrumento]

            for compas in voz.compases:
                for figura in compas.figuras:
                    if type(figura) == Nota and figura.octava in self.constantes.keys():
                        figura.octava = self.constantes[figura.octava]

            
    def get_header(self):
        header = "MFile 1 " + str(len(self.voces) + 1) + " " + str(CLICKS_POR_PULSO) + "\n"
        header += "MTrk\n"
        header += "000:00:000 Tempo " + str(self.def_tempo.get_tempo_midi()) + "\n"
        header += "000:00:000 TimeSig " + str(self.def_compas) + " 24 8\n"
        header += "000:00:000 Meta TrkEnd\n"
        header += "TrkEnd\n"

        return header

    def __repr__(self):
        return "Musilen {\n\t" + str(self.def_tempo) + "\n\t" + str(self.def_compas) + "\n\t" + str(self.constantes) + "\n\t" + str(self.voces) + "\n}"

