#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3

#conecta con la base de datos
def connect():
    con = sqlite3.connect('base.db')
    con.row_factory = sqlite3.Row
    return con

#obtiene los campos de la base de datos
def get_usuarios():
    con = connect()
    c = con.cursor()
    query = """SELECT g.nombre ,u.id_usuario,u.username, u.nombres, u.apellidos, u.email, u.fecha_nacimiento FROM usuarios u, grupos g WHERE u.fk_id_grupo = g.id_grupo"""
    result = c.execute(query)
    usuarios = result.fetchall()
    con.close()
    return usuarios
    
#Obtiene todos los grupos de la base de datos
def get_grupos():
    con = connect()
    c = con.cursor()
    query = "SELECT id_grupo , nombre FROM grupos"
    result = c.execute(query)
    grupos = result.fetchall()
    con.close()
    return grupos
        
#eliminar usuario 
def delete(id_usuario):
    exito = False
    con = connect()
    c = con.cursor()
    query = "DELETE FROM usuarios  WHERE id_usuario = ?"
    try:
        resultado = c.execute(query, [id_usuario])
        con.commit()
        exito = True
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    con.close()
    return exito

#elimina grupos de la base de datos
def delete_grupo(nombre):
    exito = False
    con = connect()
    c = con.cursor()
    query = "DELETE FROM grupos WHERE nombre = ?"
    try:
        resultado = c.execute(query, [nombre])
        con.commit()
        exito = True
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    con.close()
    return exito
    
##Agrega usuarios a la base de datos 
def agregar(username,password,nombres,apellidos,email,fecha_nacimiento,id_grupo):
    exito=False
    con=connect()
    c=con.cursor()
    query="INSERT INTO usuarios(username, password,nombres,apellidos,email,fecha_nacimiento,fk_id_grupo) VALUES(?,?,?,?,?,?,?)"
    try:
        result=c.execute(query,[username,password,nombres,apellidos,email,fecha_nacimiento,id_grupo])
        con.commit()
        exito=True
    except sqlite3.Error as e:
        exito=True
        print "Error:", e.args[0]
    con.close()
    return exito

#crea nuevos grupos en la base de datos
def crear(nombre):
    exito=False
    con=connect()
    c=con.cursor()
    query="INSERT INTO grupos(nombre) VALUES (?)"
    try:
        result=c.execute(query,[nombre])
        con.commit()
        exito=True
    except squite3.Error as e:
        exito=True
        print "Error:", e.args[0]
    con.close()
    return exito
	
#busca usuarios en la base de datos
def buscar_usuario(word):
    con = connect()
    c= con.cursor()
    query = """SELECT g.nombre ,u.id_usuario,u.username, u.nombres, u.apellidos, u.email, u.fecha_nacimiento  FROM usuarios u, grupos g WHERE u.fk_id_grupo =g.id_grupo AND (u.username LIKE '%'||?||'%' OR u.nombres LIKE '%'||?||'%' OR u.apellidos LIKE '%'||?||'%' OR u.email LIKE '%'||?||'%' OR u.fecha_nacimiento LIKE '%'||?||'%' OR g.nombre LIKE '%'||?||'%' )"""
    result = c.execute(query,[word,word,word,word,word,word])
    usuarios = result.fetchall()
    con.close()
    return usuarios


def editar(username,password,nombres,apellidos,email,fecha_nacimiento,id_grupo):
    exito=False
    con=connect()
    c=con.cursor()
    query="""UPDATE usuarios SET username=?, password=?,nombres=?, apellidos=?,email=?,fecha_nacimiento=? WHERE fk_id_grupo=?"""
    try:
	result=c.execute(query,[username,password,nombres,apellidos,email,fecha_nacimiento,id_grupo])
        con.commit()
        exito=True
    except squile3.Error as e:
	exito=False
	print "Error:", e.args[0]
    con.close()
    return exito
