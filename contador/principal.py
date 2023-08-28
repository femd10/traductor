from traductor import Traductor

t=Traductor()

n=int(input("ingrese el numero a contar: "))
s=int(input("ingrese el sistema a contar en digitos: "))
input("\nPresione enter para iniciar el conteo...")
for i in range(n):
    if s==2:
        print(bin(t.contador.valor)[2:])
    elif s==8:
        print(oct(t.contador.valor)[2:])
    elif s==16:
        print(hex(t.contador.valor))
    elif s==10:
        print(t.contador.valor)
    