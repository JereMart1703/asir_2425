class Coche:
    def __init__(self, matricula : str,marca :str, 
                 modelo: str, color:str):
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.color = color


    # comparar por defecto por matricula
    def __eq__(self, other):
        return self.matricula == other.matricula

