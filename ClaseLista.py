from CLaseNode import Nodo
from zope.interface import implementer
from Interface import Interface
from ClaseAparato import Aparato
from Interface import  Interface
from ClaseLavarropa import  Lavaropa
from ClaseHeladera import  Heladera
from ClaseTelevisor import  Televisor
@implementer(Interface)
class Lista:
    __comienzo=None
    __actual=None
    __indice=0
    __tope=0
    def __init__(self):
        self.__comienzo=None
        self.__actual=None
    def __iter__(self):
        return self
    def __next__(self):
        if self.__indice==self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            dato = self.__actual.getDato()
            self.__actual=self.__actual.getSiguiente()
            return dato
    def agregarAparato(self, aparato):
        nodo = Nodo(aparato)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo=nodo
        self.__actual=nodo
        self.__tope+=1
    def getTope(self):
        return self.__tope
    def getcabeza(self):
        return self.__comienzo

    def agregarElemento(self,elemeto):
        nodo = Nodo(elemeto)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo=nodo
        self.__actual=nodo
        self.__tope +=1
        print('Elemento agregado')

    def insertarElemento(self,elemento,posicion):
        if isinstance(elemento, Aparato):
            aux = self.__comienzo
            i = 0
            encontro = False
            ant = aux
            if posicion > 0 and posicion <= self.__tope:
                if i == posicion - 1:
                    if aux == None:
                        self.agregarElemento(elemento)
                    else:
                        nodo = Nodo(elemento)
                        nodo.setSiguiente(aux)
                        aux.setSiguiente(aux.getSiguiente())
                        self.__comienzo = nodo
                        self.__actual = nodo
                        self.__tope += 1
                else:
                    while aux != None and not encontro:
                        if i == posicion - 1:
                            encontro = True
                            nodo = Nodo(elemento)
                            ant.setSiguiente(nodo)
                            nodo.setSiguiente(aux)
                            self.__tope += 1
                            print('Elemento agregado en la posicion {}!'.format(posicion))
                        else:
                            ant = aux
                            aux = aux.getSiguiente()
                            i += 1
            else:
                print('ERROR: posicion ingresada invalida!')

    def mostrarElemento(self, posicion):
            aux = self.__comienzo
            bandera = True
            i = 1
            if posicion > 0 and posicion <= self.__tope:
                while aux != None and bandera:
                    if posicion  == i:
                        dato = aux.getDato()
                        bandera = False
                    else:
                        aux = aux.getSiguiente()
                        i += 1
            if bandera == True:
                print('Posicion no encontrada')
            else:
                if isinstance(dato,Televisor):
                    print('Es un televisor')
                elif isinstance(dato,Heladera):
                    print('Es una Heladera')
                elif isinstance(dato,Lavaropa):
                    print('Es un lavaropa')