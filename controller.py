#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3

def connect():
    con = sqlite3.connect('base.db')
    con.row_factory = sqlite3.Row
    return con

#obtener usuarios
def get_usuarios():
    con = connect()
    c = con.cursor()
    query = """SELECT g.nombre ,u.username, u.nombres, u.apellidos, u.email, u.fecha_nacimiento FROM usuarios u, grupos g WHERE u.fk_id_grupo = g.id_grupo"""
    result = c.execute(query)
    usuarios = result.fetchall()
    con.close()
    return usuarios
  
def get_grupos():
    con = connect()
    c = con.cursor()
    query = "SELECT id_grupo, nombre FROM grupos"
    result = c.execute(query)
    grupos = result.fetchall()
    con.close()
    return grupos
        
#eliminar usuario 
def delete(id_usuario):
    exito = False
    con = connect()
    c = con.cursor()
    query = "DELETE FROM usuarios  WHERE username = ?"
    try:
        resultado = c.execute(query, [id_usuario])
        con.commit()
        exito = True
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    con.close()
    return exito


def agregar(id_grupo,username,password,nombres,apellidos,email,fecha_nacimiento):
	exito=False
	con=connect()
	c=con.cursor()
	query="INSERT INTO usuarios(id_usuario, username, password,nombres,apellidos,email,fecha_nacimiento,fk_id_grupo) VALUES(?,?,?,?,?,?,?,?)"
	try:
		result=c.execute(query,["id_usuario",username,password,nombres,apellidos,email,fecha_nacimiento,id_grupo])
		con.commit()
		exito=True
		msgBox=QtGui.QMessageBox()
		msgBox.setText("El usuario fue agregado.")
		msgBox.exec_()
	except sqlite3.Error as e:
		exito=True
		print "Error:", e.args[0]
	con.close()
	return exito
		
