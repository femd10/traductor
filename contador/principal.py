from traductor import Traductor

t=Traductor()

n=int(input("ingrese el numero a contar: "))
s=int(input("ingrese el sistema a contar en digitos: "))
input("\nPresione enter para iniciar el conteo...")
for i in range(n+1):
    if s==2:
        print(bin(t.binario.valor)[2:])
    elif s==8:
        print(oct(t.octal.valor)[2:])
    elif s==16:
        print(hex(t.hexa.valor))
    elif s==10:
        print(t.contador.valor)
    
    
    t.avanzar()
print("\t ／l、\n\t（ﾟ､ ｡７\n\t⠀l、ﾞ~ヽ\n\t じし(_, )ノ\n")