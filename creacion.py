import sqlite3
conn = sqlite3.connect('facturacion.db')
c = conn.cursor()

#Tabla
c.execute('''CREATE TABLE domicilio
             (id integer primary key asc, direccion text, telefono real, administrador text)''')
c.execute('''CREATE TABLE administrador
             (id integer primary key asc, telefono real, direccion text)''')
c.execute('''CREATE TABLE cliente
             (id integer primary key asc, nombre text, nit text, telefono text, direccion text)''')
c.execute('''CREATE TABLE cuenta
             (id integer primary key asc, cliente integer, foreign key(cliente) references cliente(id))''')
c.execute('''CREATE TABLE producto
             (id integer primary key asc, cantidad real, precio real, nombre text)''')
c.execute('''CREATE TABLE productoscuenta
             (id integer primary key asc, cantidad real, cuenta integer, producto integer, foreign key(cuenta) references cuenta(id), foreign key(producto) references producto(id))''')
# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()