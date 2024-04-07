from Producto import Producto
class Tienda:
    
    def __init__(self):
        self.__producto1 = Producto("Papeleria", "lapiz", 550.0, 30, 9)
        self.dineroEnCaja = 0

    def getProducto1(self):
        return self.__producto1
    
    def __init__(self):
        self.__producto2 = Producto("Papeleria", "Borrador", 300.0, 15, 5)

    def getProducto2(self):
        return self.__producto2 

    def __init__(self):
        self.__producto3 = Producto("Supermercado", "Cafe",5600.00, 20,10)
        self.dineroEnCaja = 0

    def getProducto3(self):
        return self.__producto3
    
    def __init__(self):
        self.__producto4 = Producto("Drogueria", "Desinfectante", 3200.0, 12, 11)
        self.dineroEnCaja = 0

    def getProducto4(self):
        return self.__producto4
    
#Vender una cierta cantidad del producto cuyo nombre es igual al recibido como parametro. El metodo retorna el numero de unidades efectivamente vendidas 
#Suponga que el nombre que se recibe como parametro corresponde a uno de los productos de la tienda. Utilice el metodo vender de la clase producto como parte de su solucion 

    def venderProducto(self, nombreProducto, cantidad):
        if cantidad <= self.__cantidadBodega:
            self.__cantidadUnidadesVendidas += cantidad
            self.__cantidadBodega -= cantidad 
        #if self.__producto1 <= 30:
            #self.__getCantidadBodega -= cantidad
        elif cantidad <= 30:
            return "El producto fue vendido exitosamente"
        
    #Calcular el numero de productos de papeleria que se venden en la tienda 
        
    def cuantosPapeleria(self):
        productosPapeleria = (self.__producto1, self.__producto2)
        cantidadVendida += (productoCantidadVendida for producto in productosPapeleria)
        return cantidadVendida 
    
    ################################### TAREA ############################################

    def darPrecioProducto(self, producto):
        valorProducto = 1 and <4:
        if self.pNumeroProducto == self.__producto1:
            return "El precio del producto1 es:"

        elif self.pNumeroProducto == self.__producto2:
            return "El precio del producto2 es:"
        
        elif self.pNumeroProducto == self.__producto3:
            return "El precio del producto3 es:"
        
        elif self.pNumeroProducto == self.__producto4:
            return "El precio del producto4 es:"
        

    def cuantosPapeleria(self):
        productosPapeleria = (self.__producto1, self.__producto2)
        cantidadVendida += (producto.CantidadVendida for producto in productosPapeleria)
        return cantidadVendida
    