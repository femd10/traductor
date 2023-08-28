
from binario import Binario
from octal import Octal
from hexa import Hexa
from contador import Contador
class Traductor():
    def __init__(self):
        self.binario= Binario()
        self.octal= Octal()
        self.hexa= Hexa()
        self.contador= Contador()
    def avanzar(self):
    
        self.contador.avanzar()
       