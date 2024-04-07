from enum import enum 
class Tipo(Enum):

    '''-------------------------------------
    #Enumeracion para los tipos de productos
    ----------------------------------------'''

    Papeleria = 1
    Supermercado = 2
    Drogueria = 3

class Producto: 
    __Subsidio = True
    __Calidad = 'A'

    '''-------------------------------------
    #Constantes
    ----------------------------------------'''

    __Iva_Papeleria = 0.16
    __IvaSupermercado = 0.04
    __IvaDrogueria = 0.12

    '''-------------------------------------
    #Metodos
    ----------------------------------------'''

    def __init__(self, tipo, pNombre, pValorUnitario, pCantidadBodega, pCantidadMinima):
        self.__tipo = tipo 
        self.__nombre = pNombre
        self.__valorUnitario = pValorUnitario
        self.__cantidadBodega = pCantidadBodega
        self.__cantidadMinima = pCantidadMinima
        self.__cantidadUnidadesVendidas = 0

    def getNombre(self):
        return self.__nombre
        
    def  getTipo(self):
        return self.__tipo
        
    def getValorUnitario(self):
        return self.__ValorUnitario 
        
    def getCantidaMinima(self):
        return self.__cantidadMinima
        
    def setCantidadUnidadesVendidas(self, cantidadUnidadesvendidas):
        self.__cantidadUnidadesVendidas = cantidadUnidadesvendidas

    def setCantidadBodega(self, cantidadBodega):
        self.__cantidadBodega = cantidadBodega

    def Vender ( self,cantidad):
        if cantidad <= self.__cantidadBodega:
            self.__cantidadUnidadesVendidas += cantidad
            self.__cantidadBodega -= cantidad 
            
        else:
                print ( "Cantidad no disponible")

    def sufiCantidad(self, cantidad):
            #Forma1

        if cantidad <= self.__cantidadBodega:
            return True
        else: 
            return False
            
            #Forma2

        haySudiciente = False 
        if cantidad <= self.__cantidadBodega:
            haySuficiente = True
            return haySuficiente
            
            #Forma3

            return cantidad <= self.__cantidadBodega
        
    def Dariva(self):
        if self.__tipo == "PAPELERIA":
            return self.__IvaPapeleria
        elif self.__tipo == "DROGUERIA":
            return self.__IvaDrogueria
        elif self.tipo == "SUPERMERCADO":
            return self.__IvaSupermercado
        else:
            print("Categoria de producto no existe")

#Aumentar el valor unitario utilizando la siguiente politica
#Si el producto cuesta menos de  1000, aumentar el 1%, si cuesta entre 1000 y 5000 aumentar el 2%, si cuesta mas de  5000 aumentar el 3%

    def subirValorUnitario(self):
        if self.__valorUnitario > 1000:
        elif self.__valorunitario += valorUnitario*0.01:
            return self.__valorUnitario
        elif self.__valorUnitario > 5000 < 1000:
            self.__valorUnitario += self.__valorUnitario*0.02
            return self.__valorUnitario
        elif self.__valorUnitario > 5000:
            self.__valorUnitario += self.__valorUnitario*0.03
            return self.__valorUnitario
        
    
#Recibir un pedido solo si en la bodega se tiene menos unidades de las indicadas  en el tope minimo, en el caso contrario el metodo no debe hacer nada

    def hacerPedido(self):
        if self.__cantidadBodega < self.__cantidadMinima:
            return True
        else: False

#Modificar el precio del producto utilizando la siguiente politica 
#si el producto es de dogueria o papeleria debe disminuir 10%, si es de supermercado debe aumentar un 5%

    def cambiarValorunitario(self):
        if self.__productoPapeleria -= self.__productoPapeleria/0.1:
            return self.actualizarvalorUnitario
        elif self.__productoDrogueria -= self.__productoDrogueria/0.1:
            return self.actualizarValorUnitario
        elif self.__productoSupermercado -= self.__productoSupermercado/0.5:
            return self.actualizarValorUnitario
        

        #################################### TAREA #############################

    def nombreTipoProducto(self, papeleria):
        if tipo == Tipo.Papeleria:
            return "El tipo del producto es de papeleria"
        
    def nombreTipoProducto(self, drogueria):
        if tipo == Tipo.Drogueria:
            return "El tipo del producto es de drogueria"
            
    def nombreTipoProducto(self, Supermercado):
        if tipo == Tipo.Supermercado:
             return "El tipo del producto es de supermercado"

    def aumentarValorUnitario(self):
         if self.__productoPapeleria += self.__productoPapeleria*0.2:
            return "Se aumento el valor unitario correctamente"
        elif self.__productoDrogueria += self.__productoDrogueria*0.1:
            return "Se aumento el valor unitario correctamente"
        elif self.__productoSupermercado += self.__productoSupermercado*0.3:
            return "Se aumento el valor unitario correctamente"
        
        
                    