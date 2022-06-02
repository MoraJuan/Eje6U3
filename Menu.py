
from Manejador import  Manejador
from ClaseLavarropa import Lavaropa
from ClaseObj import  Object
class Menu:
    opcion=None
    
    def __init__(self):
        self.__opcion=0
    def mostrarmenu(self):
        jsonF = Object()
        Aparatos = Manejador()
        diccionario = jsonF.leerJSONArchivo('aparatoselectronicos.json')
        Aparatos = jsonF.decodificarDiccionario(diccionario)

        while self.__opcion!=-1:
            print('[1] Inssertar aparato en posicion especifica')
            print('[2] Agrega a coleccion')
            print('[3] Motrar')
            print('[4] Mostar ')
            print('[5] Mostrar')
            print('[6] Mostrar')
            print('[7] Almacenar')
            self.__opcion=input('\nIngrese numero: ')
            if self.__opcion=='1':
                pos = int(input('Ingresar posicion donde insertara el elemento '))
                aparato = Aparatos.crearaparato()
                Aparatos.insertarElemento(aparato,pos)
            elif self.__opcion=='2':
                aparato = Aparatos.crearaparato()
                Aparatos.agregarElemento(aparato)
            elif self.__opcion=='3':
                posicion = int(input('Ingresar posicion '))
                Aparatos.mostrarElemento(posicion)
            elif self.__opcion=='4':
                Aparatos.Aparatosphillips()
            elif self.__opcion=='5':
                Aparatos.marcalavaropas()
            elif self.__opcion=='6':
                Aparatos.mostrarDatos()
            elif self.__opcion=='7':
                listaJSON = Aparatos.guardarJSON()
                jsonF.guardarJSONArchivo(listaJSON, 'Aparato.json')
                print('Archivo guardado')
               