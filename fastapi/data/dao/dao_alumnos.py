from data.modelo.alumno import Alumno

class DaoAlumnos:
    
    def get_all(self,db) -> list[Alumno]:
        cursor = db.cursor()
    
        cursor.execute("SELECT * FROM alumnos")

        equipos_en_db = cursor.fetchall()
        equipos : list[Alumno]= list()
        for equipo in equipos_en_db:
            equipos.append(Alumno(equipo[0], equipo[1]))

        cursor.close()
        
        return equipos