from ClaseAparato import Aparato
import json
from pathlib import Path
class Televisor(Aparato):
    __tipopantalla =None
    __pulgadas = None
    __TipoDefinicion= None
    __Conexion = bool


    def __init__(self, marca, modelo, color, pais, precio,tipo,pulgadas,definicion,conexion):
        super().__init__(marca, modelo, color, pais, precio)
        self.__tipopantalla = tipo
        self.__pulgadas = pulgadas
        self.__TipoDefinicion = definicion
        if conexion == "True":
            self.__Conexion = True
        else:
            self.__Conexion = False

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                marca=self.getmarca(),
                modelo=self.getmodelo(),
                color=self.getcolor(),
                pais=self.getpais(),
                precio=self.getprecio(),
                tipo=self.__tipopantalla,
                pulgadas=self.__pulgadas,
                definicion=self.__TipoDefinicion,
                conexion=self.__Conexion
            )
        )
        return d

    def ImporteVenta(self):
        importe = 0
        if self.__TipoDefinicion == "SD":
            importe = (int(self.getprecio()) /100) + int(self.getprecio())
        elif self.__TipoDefinicion == "HD":
            importe = ((int(self.getprecio()) *2) / 100) + int(self.getprecio())
        elif self.__TipoDefinicion == "FULL HD":
            importe = ((int(self.getprecio()) * 3) / 100) + int(self.getprecio())
        if self.__Conexion == True:
            importe +=  ((int(self.getprecio()) * 10) / 100)
        return  importe

    def __str__(self):
        s = str(self.getmarca()) + '   ' + str(self.getpais()) + '   ' + str(self.ImporteVenta())
        return 