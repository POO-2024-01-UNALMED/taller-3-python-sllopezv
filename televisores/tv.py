class TV:
    _numTV = 0
    
    def __init__(self, marca, estado):
        self._marca = marca
        self._estado = estado
        self._canal = 1
        self._volumen = 1
        self._precio = 500
        TV._numTV += 1
        
    # Getters
    def getMarca(self):
        return self._marca
    
    def getCanal(self):
        return self._canal
    
    def getVolumen(self):
        return self._volumen
    
    def getPrecio(self):
        return self._precio
    
    def getEstado(self):
        return self._estado
    
    def getControl(self):
        return self._control
    
    # Setters
    def setMarca(self, marca):
        self._marca = marca
        
    def setEstado(self, estado):
        self._estado = estado
        
    def setCanal(self, canal):
        if self._estado == True and canal >= 1 and canal <= 120:
            self._canal = canal
    
    def setVolumen(self, volumen):
        if self._estado == True and volumen >= 0 and volumen <= 7:
            self._volumen = volumen
            
    def setPrecio(self, precio):
        self._precio = precio
        
    def setControl(self, control):
        self._control = control
        
    # Metodos tv
    def turnOn(self):
        self._estado = True
        
    def turnOff(self):
        self._estado = False
        
    # Métodos canales
    def canalUp(self):
        if self._estado == True and self._canal < 120:
            self._canal += 1
            
    def canalDown(self):
        if self._estado == True and self._canal > 1:
            self._canal -= 1
            
    # Métodos volumen
    def volumenUp(self):
        if self._estado == True and self._volumen < 7:
            self._volumen += 1
            
    def volumenDown(self):
        if self._estado == True and self._volumen > 0:
            self._volumen -= 1
            
    # Método estático
    @classmethod
    def getNumTV(cls):
        return cls._numTV
    
    @classmethod
    def setNumTV(cls, numTV):
        cls._numTV = numTV


    