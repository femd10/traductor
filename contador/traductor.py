
from binario import Binario
from octal import Octal
from hexa import Hexa
from contador import Contador
import time
class Traductor():
    def __init__(self):
        self.binario= Binario()
        self.octal= Octal()
        self.hexa= Hexa()
        self.contador= Contador()
        
    def avanzar(self):
        time.sleep(1)
        self.binario.avanzar()
        self.octal.avanzar()
        self.hexa.avanzar()