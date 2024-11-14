
from domain.modelo.coche import Coche
from data.db import coches


class CochesServicios:

    def crearCoche(self):
        matricula = input("Introduce la matricula: ")
        marca = input("Introduce la marca: ")
        modelo = input("Introduce el modelo: ")
        color = input("Introduce el color: ")
        coche = Coche(matricula, marca, modelo, color)
        coches.append(coche)

    def borrarCoche(self):
        matricula = input("Introduce la matricula: ")
        coche_borrar = Coche(matricula, "", "", "")
        coches.remove(coche_borrar)
        coches.pop(coches.index(coche_borrar))
        for coche in coches:
            if (coche.matricula == matricula):
                coches.remove(coche)
        for indice,coche in enumerate(coches):
            if (coche.matricula == matricula):
                coches.pop(indice)
                break
        coches.remove(self.buscarCocheParaBorrar(matricula))


    def buscarCocheParaBorrar(self,matricula : str) -> Coche:
        for coche in coches:
            if (coche.matricula == matricula):
                return coche
        return None

        
    def actualizarCoche(self):
        matricula = input("Introduce la matricula: ")
        modelo = input("Introduce el modelo: ")
       
        for coche in coches:
            if (coche.matricula == matricula):
                coche.modelo = modelo
          


    def buscarCoche(self):
        matricula = input("Introduce la matricula: ")
        for coche  in coches:
            if (coche.matricula == matricula):
                print(coche.matricula, coche.marca, coche.modelo, coche.color)
                break
        else:
            print("No se ha encontrado el coche")

    def listar_coches(self):
        for coche in coches:
            print(coche.matricula,coche.marca,coche.modelo, coche.marca)

