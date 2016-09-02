import sqlite3


def crear_cliente(nombre, nit, telefono, direccion):
	conn = sqlite3.connect('facturacion.db')
	c = conn.cursor()
	c.execute(
		'''INSERT INTO cliente (nombre, nit, telefono, direccion)
			VALUES ('%(nombre)s', '%(nit)s', '%(telefono)s', '%(direccion)s')''' % {
			'nombre': nombre,
			'nit': nit,
			'telefono': telefono,
			'direccion': direccion
		}
	)

	conn.commit()
	conn.close()


def leer_clientes():
	conn = sqlite3.connect('facturacion.db')
	c = conn.cursor()

	clientes = []
	for row in c.execute('SELECT * FROM cliente'):
		clientes.append(row)

	conn.close()

	return clientes

