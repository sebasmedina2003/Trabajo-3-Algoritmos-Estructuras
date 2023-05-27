class Categoria:
    def __init__(self, nombre:str, descripcion:str, status:str) -> None:
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__status = status
    
    def getNombre(self):
        return self.__nombre
    
    def getDescripcion(self):
        return self.__descripcion
    
    def getStatus(self):
        return self.__status
    
    def getListaAtributos(self):
        return [self.__nombre, self.__descripcion, self.__status]