
from domain.modelo.coche import Coche
from data.db import coches


class CochesServicios:

    def listar_coches(self):
        return coches
    
    def crear_coche(self, coche: Coche):
        coches.append(coche)

    def borra_coche(self, matricula: str):
        ## buscar coche por matricula
        for coche in coches:
            if coche.matricula == matricula:
                coches.remove(coche)
    
    def cambiar_coche(self, matricula: str):
        ## buscar coche por matricula
        for coche in coches:
            if coche.matricula == matricula:
                coche.color = "AAAAAA"
        return None

