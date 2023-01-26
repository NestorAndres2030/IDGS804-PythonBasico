def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


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
        print(f"Que tipo de operacion matematica deseas realizar con {a} y {b}\n\
1 para sumar\n\
2 para restar\n\
3 para multiplicar\n\
4 para dividir\n\
5 para salir:")
        opcion=input()
        if opcion== 1:
            print(f"Resultado es:{suma(a,b)}")
        if opcion==2:
            print(f"Resultado es:{resta(a,b)}")
        if opcion==3:
            print(f"Resultado es:{mul(a,b)}")
        if opcion==4:
            print(f"Resultado es:{div(a,b)}")
        if opcion==5:
            break
        input("Presione cualquier tecla")
        os.system("cls")
a,b=pedirNumeros()
menu(a,b)