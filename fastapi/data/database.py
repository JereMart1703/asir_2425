import mysql.connector 


# db = list()
database = mysql.connector.connect( # LLAMAMOS AL FUNCION CONNECT PARA CONECTARNOS
    host ='localhost',
    port = 3306,
    ssl_disabled = True,
    user ='root', #USUARIO QUE USAMOS NOSOTROS
    password ='clase', #CONTRASEÑA CON LA QUE NOS CONECTAMOS
    database='demo'
) 