import os


   

def pedirNumeros():
    a=int(input("Ingresa el valor de a:"))
    b=int(input("Ingresa el valor de b:"))
    os.system("cls")
    return a,b
def suma(a,b):
    return a+b
def resta(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def menu(a,b):



    while True:
        print(f"Eligue la Operacion que quieres hacer  {a} y {b}\n\
s para sumar\n\
r para restar\n\
m para multiplicar\n\
d para dividir\n\
x para salir:")
        opcion=input()
        if opcion=='s':
            print(f"Resultado es:{suma(a,b)}")
        if opcion=='r':
            print(f"Resultado es:{resta(a,b)}")
        if opcion=='m':
            print(f"Resultado es:{mul(a,b)}")
        if opcion=='d':
            print(f"Resultado es:{div(a,b)}")
        if opcion=='x':
            break
        input("Presione cualquier tecla")
        os.system("cls")


if __name__ =='__main__': # para llamar funciones de otro documento sin que se ejecute todo solo lo que pedi 
    a,b=pedirNumeros()
    menu(a,b)