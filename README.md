Usuario
=======
Trabajo Adicional
Taller de construcción de software
INFO175
Integrante:Juan Aarón Maldonado Imilán

Detalle del Programa:
El programa se llama Usuarios y tiene como finalidad mostrar usuarios que 
pertenecen a distintos grupos en una grilla. En el programa se podrá 
ingresar, eliminar usuarios, como también crear grupos y eliminarlos.
 
Funcionamiento del programa:

El archivo principal se llama Main.Principal.py, el cual al ejecutar se
podrá ver la ventana principal que muestra todos los usuarios de la base
de datos con distintos botones entre ellos tenemos:
-Nuevo Usuario que al presionarlo aparece una nueva ventana con un formulario
a rellenar, este fue creado a partir de 2 archivos llamados Ingreso.py y 
VentanaAgregar.py que corresponde al main de esta ventana.
-Editar usuarios que al presionarlo nos muestra un formulario que tiene la 
informacion de la fila seleccionada, fue creado en los archivos 
VentanaEdicion.py y Ingreso Edicion.py y se encuentra incompleto.
-Eliminar Usuario que al presionarlo te pide seleccionar una fila para poder 
eliminar algún usuario de la grilla, fue creado en el archivo MainPrincipal.py
-Crear Grupo que al presionarlo aparece una pequeña ventana para crear un grupo
que fue creada en CreacionGrupo.py CreaGrupo.py.
-Editar Grupo es un botón que no tiene ninguna función.
-Eliminar Grupo botón que al presionarlo aparece una ventana con los grupos
de la base de datos y que al seleccionar uno se eliminar el grupo con todos
los usuarios que estén en el, fue creado en VentanaEliminarGrupo.py y en 
EliminarGrupo.py
-Buscar botón que funciona en paralelo con el la caja de texto que al 
ingresar un nombre busca en la grilla su igual y nos da algunas sugerencias de 
lo que podemos estar buscando.
Por ultimo tenemos un archivo controller.py en los cuales estan creados los 
métodos que interactúan con la base de datos.

Observaciones:
Para poder ver los usuarios en la grilla se debe ejecutar en primer lugar
el archivo que crea la base de datos llamado BDUsuarios.py.
Para poder ver los usuarios ingresados se debe cerrar el programa y volver a 
ejecutar.
Para poder ingresar un nuevo usuario se debe cumplir con los campos obligatorios.
El password del usuario es guardada de acuerdo al algoritmo SHA512.
Al editar usuario se encuentra incompleto, ya que al ser ejecutado nos muestra los
campos a editar pero siempre edita el primer elemento de la grilla no el que fue
seleccionado.
