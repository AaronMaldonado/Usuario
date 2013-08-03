# -*- coding: utf-8 -*-

import os
import sqlite3

def create_db(db_name):
	conn=sqlite3.connect(db_name)
	c=conn.cursor()
	query="""CREATE TABLE grupos(id_grupo integer PRIMARY KEY AUTOINCREMENT,
				     nombre text)"""
	c.execute(query)


	query1="""CREATE TABLE usuarios(id_usuario integer PRIMARY KEY 
				       AUTOINCREMENT,username text,
				       password text,nombres text,
				       apellidos text,email text,
				       fecha_nacimiento date,fk_id_grupo integer,
			           FOREIGN KEY (fk_id_grupo) REFERENCES 
                       grupos (id_grupo))"""
	c.execute(query1)


if __name__ == "__main__":
    db_name = 'base.db'
    if not os.path.exists(db_name):
        create_db(db_name)
        
    conn = sqlite3.connect(db_name)
    c = conn.cursor()


    query = "INSERT INTO grupos (id_grupo,nombre) VALUES (?,?)"
    
    v1 =[0,"Manager"]
    v2 =[1,"Administrador"]
    v3 =[2,"Supervisor"]
    v4 =[3,"Moderador"]
    v5 =[4,"Invitado"]
    c.execute("INSERT INTO grupos VALUES(?,?)",v1)
    c.execute("INSERT INTO grupos VALUES(?,?)",v2)
    c.execute("INSERT INTO grupos VALUES(?,?)",v3)
    c.execute("INSERT INTO grupos VALUES(?,?)",v4)
    c.execute("INSERT INTO grupos VALUES(?,?)",v5)
    conn.commit()
    
    
    query="INSERT INTO usuarios(id_usuario, username, password,nombres,apellidos,email,fecha_nacimiento,fk_id_grupo) VALUES(?,?,?,?,?,?,?,?)"
    u1=["5","Daguir","perla","Aaron","Maldonado Imilan","leo_1189@hotmail.com","12-08-1989","0"]
    u2=["6","Anubis","dark","John","Stark Tully","dark_12@gmail.com","23-07-1992","1"]
    u3=["7","Gandalf","comarca","Olorin","Gallego Montes","elblanco@hotmail.com","10-04-1900","2"]
    u4=["8","Pandita","panda","Valeria","Asencio Uribe","gvaleriau@msn.com","02-11-1989","3"]
    u5=["9","Alquimist","noche","Marco","Orellana Sandoval","blan@hotmail.com","03-12-1974","4"]
    u6=["10","Inani","sos","Carolina","Ramirez Lopez","qarito.blezz@gmail.com","10-10-1989","0"]
    u7=["11","Proyecto","platino","Patricia","bello Parra","proyectox.@gmail.com","19-09-1989","1"]
    u8=["12","klau","cartas","Claudia Antonia","Navarro Galindo","klau@hotmail.com","06-10-1989","2"]
    u9=["13","Negro","gato","Jamie","Lannister ","jamie@hotmail.com","30-05-1980","3"]
    u10=["14","Payo","payo","Esteban","Mancilla Alvarado","payo@gmail.com","01-03-1987","4"]
    u11=["15","Huevo","huevo","Laura Maria","Carmona Perez","hit@hotmail.com","23-06-1985","0"]
    u12=["16","Sparta","sparta","Mateo","Vera Diaz","sparta@hotmail.com","19-07-1979","1"]
    u13=["17","Sauron","sauron","Darren","Criss Colfed","darren@gmail.com","17-01-1984","2"]
    u14=["18","Voldi","Voldi","Harry","Potter","harry@hotmail.com","31-07-1989","3"]
    u15=["19","Matrix","matrix","Neo","Montana Salas","matrix@msn.com","06-05-1977","4"]
    
    
    c.execute("INSERT INTO usuarios VALUES (?,?,?,?,?,?,?,?)",u1)
    c.execute("INSERT INTO usuarios VALUES (?,?,?,?,?,?,?,?)",u2)		
    c.execute("INSERT INTO usuarios VALUES (?,?,?,?,?,?,?,?)",u3)	
    c.execute("INSERT INTO usuarios VALUES (?,?,?,?,?,?,?,?)",u4)		
    c.execute("INSERT INTO usuarios VALUES (?,?,?,?,?,?,?,?)",u5)
    c.execute("INSERT INTO usuarios VALUES (?,?,?,?,?,?,?,?)",u6)
    c.execute("INSERT INTO usuarios VALUES (?,?,?,?,?,?,?,?)",u7)
    c.execute("INSERT INTO usuarios VALUES (?,?,?,?,?,?,?,?)",u8)
    c.execute("INSERT INTO usuarios VALUES (?,?,?,?,?,?,?,?)",u9)
    c.execute("INSERT INTO usuarios VALUES (?,?,?,?,?,?,?,?)",u10)
    c.execute("INSERT INTO usuarios VALUES (?,?,?,?,?,?,?,?)",u11)
    c.execute("INSERT INTO usuarios VALUES (?,?,?,?,?,?,?,?)",u12)
    c.execute("INSERT INTO usuarios VALUES (?,?,?,?,?,?,?,?)",u13)
    c.execute("INSERT INTO usuarios VALUES (?,?,?,?,?,?,?,?)",u14)
    c.execute("INSERT INTO usuarios VALUES (?,?,?,?,?,?,?,?)",u15)
	
	
    conn.commit()
