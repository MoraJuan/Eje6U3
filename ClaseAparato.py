from abc import abstractmethod
from abc import ABC
import json
from pathlib import Path
class Aparato(ABC):
    __marca = None
    __modelo = None
    __color = None
    __pais =  None
    __precio = None

    def __init__(self,marca,modelo,color,pais,precio):
        self.__marca = marca
        self.__modelo = modelo
        self.__color = color
        self.__pais = pais
        self.__precio =  precio

    def getmarca(self):
        return self.__marca
    def getmodelo(self):
        return self.__modelo
    def getcolor(self):
        return self.__color
    def getpais(self):
        return self.__pais
    def getprecio(self):
        return self.__precio

