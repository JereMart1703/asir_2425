from domain.modelo.coche import Coche
from domain.servicios.cochesServicios import CochesServicios

def main():
    cochesServicios : CochesServicios = CochesServicios()
    while True:
        print(" 1. Crear coche")
        print(" 2. Listar coches")
        print(" 3. Buscar coche")
        print(" 4. Borrar coche")
        print(" 5. Salir")
        opcion = input("Introduce una opcion: ")
        if (opcion == "1"):
            matricula :str = input("dime la matricula")
            color :str = input("dime el color")
            marca :str = input("dime la marca")
            modelo :str = input("dime el modelo")
            coche_nuevo : Coche = Coche(matricula, marca, modelo, color)
            cochesServicios.crear_coche(coche_nuevo)
            print("Coche creado")           
        elif (opcion == "2"):
            coches : list[Coche] = cochesServicios.listar_coches()
            for coche in coches:
                print(coche)
        elif (opcion == "3"):
            print("TODO")
        elif (opcion == "4"):
            matricula :str = input("dime la matricula")
            cochesServicios.cambiar_coche(matricula)
        elif (opcion == "5"):
            break
        else:
            print("Opcion incorrecta")








