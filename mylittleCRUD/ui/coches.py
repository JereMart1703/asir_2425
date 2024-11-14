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
            cochesServicios.crearCoche()
        elif (opcion == "2"):
            cochesServicios.listar_coches()
        elif (opcion == "3"):
            cochesServicios.buscarCoche()
        elif (opcion == "4"):
            cochesServicios.borrarCoche()
        elif (opcion == "5"):
            break
        else:
            print("Opcion incorrecta")








