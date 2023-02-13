import sqlite3

conn=sqlite3.connect('tienda.db')
cursor_obj = conn.cursor()
cursor_obj.execute("DROP TABLE IF EXISTS USUARIOS")
table = """ CREATE TABLE USUARIOS (
            ID  INTEGER PRIMARY KEY AUTOINCREMENT,
            USUARIO VARCHAR(25),
            PASSWORD VARCHAR(255) NOT NULL,
            EMAIL VARCHAR(255) NOT NULL,
            FULLNAME VARCHAR(25) NOT NULL,
            SCORE INT,
            TIPOUSUARIO VARCHAR(25),
            VCOMPRADOLAR VARCHAR(25) NOT NULL
        ); """
cursor_obj.execute(table)
cursor_obj.execute("DROP TABLE IF EXISTS PRODUCTOS")
table = """ CREATE TABLE PRODUCTOS (
            ID  INTEGER PRIMARY KEY AUTOINCREMENT,
            NAMEPRODUCT VARCHAR(255) NOT NULL,
            PRICE VARCHAR(20) NOT NULL, 
            CATEGORIA VARCHAR(25) NOT NULL,
            STCOKACTUAL INT,
            CREACTION_PRODUCT TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UPDATE_PRODUCT TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ); """

### APORTE
#PREGUNTA 2
cursor_obj.execute(table)
cursor_obj.execute("DROP TABLE IF EXISTS INFO_T_CHANGES")

table=""" CREATE TABLE INFO_T_CHANGES (
            IDMOVIMIENTO  INTEGER PRIMARY KEY AUTOINCREMENT,
            V_VENTA FLOAT NOT NULL, 
            V_COMPRA FLOAT NOT NULL,    
            FECHA_INFORME TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
            CENTRO VARCHAR(25)

        ); """
#//////////////////////////////////////////////////////////////
#PREGUNTA 3
cursor_obj.execute(table)
cursor_obj.execute("DROP TABLE IF EXISTS HISTORIAL")

table=""" CREATE TABLE HISTORIAL (
            IDMOVIMIENTO  INTEGER PRIMARY KEY AUTOINCREMENT,
            USUARIO VARCHAR(25),    
            FECHA_COMPRA TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   
            VCOMPRASOL FLOAT NOT NULL,  
            VCOMPRADOLAR FLOAT NOT NULL,    
            PRODUCTOS INT NOT NULL,       
            TIPOUSUARIO VARCHAR(25)     
        ); """

cursor_obj.execute(table)
#PREGUNTA 2
insert="INSERT INTO INFORMACION_TASA_CAMBIOS(V_VENTA,V_COMPRA,FECHA_INFORME,CENTRO) VALUES('3.858','3.853','13/02/23','WESTERN UNION')"
#PREGUNTA 3
insert="INSERT INTO HISTORIAL(USUARIO,FECHA_COMPRA,VCOMPRASOL,VCOMPRADOLAR,PRODUCTOS,TIPOUSUARIO) VALUES('HECTOR','13/02/23','259','66.92','4','client')"
conn.execute(insert)
cursor_obj.execute(insert)

print('tabla lista')