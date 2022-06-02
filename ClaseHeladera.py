from ClaseAparato import Aparato
import json
from pathlib import Path
class Heladera(Aparato):
    __capacidad = None
    __freezer = bool
    __ciclica = bool

    def __init__(self, marca, modelo, color, pais, precio,capacidad,freezer,ciclicla):
        super().__init__(marca, modelo, color, pais, precio)
        self.__capacidad = capacidad
        if freezer == "True":
            self.__freezer = True
        else:
            self.__freezer = False
        if ciclicla == "True":
         self.__ciclica = True
        else:
            self.__ciclica = False

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                marca=self.getmarca(),
                modelo=self.getmodelo(),
                color=self.getcolor(),
                pais=self.getpais(),
                precio=self.getprecio(),
                capacidad=self.__capacidad,
                freezer=self.__freezer,
                ciclica=self.__ciclica
            )
        )
        return d

    def ImporteVenta(self):
        importe = 0
        if self.__freezer == None:
            importe = (int(self.getprecio()) /100) + int(self.getprecio())
        else:
            importe = ((int(self.getprecio()) *5) / 100) + int(self.getprecio())
        if self.__ciclica == True:
            importe += ((int(self.getprecio()) *10) / 100)
        return importe
    def __str__(self):
        s = str(self.getmarca()) + '   ' + str(self.getpais()) + '   ' + str(self.ImporteVenta())
        return s