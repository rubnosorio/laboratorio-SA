import requests
import json
from requests.auth import HTTPBasicAuth
from zeep import Client
from requests import Session
from zeep.transports import Transport


# Funcion que permite listar los contactos de la aplicacion
def listar_Contactos(cliente_id, cliente_pass):
	#Recursos necesarios para realizar la peticion
	
	session = Session()
	session.auth = HTTPBasicAuth(cliente_id, cliente_pass)
	cliente = Client('https://api.softwareavanzado.world/index.php?webserviceClient=administrator&webserviceVersion=1.0.0&option=contact&api=soap&wsdl', 
		transport=Transport(session=session))
	lista = cliente.service.readList(limit=0)
	print(lista)

# Funcion que permite crear los 10 clientes solicitados, segun las instrucciones
def crear_Contactos(cliente_id, cliente_pass):
	session = Session()
	session.auth = HTTPBasicAuth(cliente_id, cliente_pass)
	cliente = Client('https://api.softwareavanzado.world/index.php?webserviceClient=administrator&webserviceVersion=1.0.0&option=contact&api=soap&wsdl', 
		transport=Transport(session=session))

	print('*************** Start Crear contactos ***************')
	#numero de contactos 
	NContactos = 0
	while NContactos < 10:
		nombre = "201403703_SOAP_No_" + str(NContactos)
		# Haciendo peticion al servidor
		response = cliente.service.create(nombre, NContactos, '*', '' )
		print(response)
		# Update contador
		NContactos+=1

	print('*************** End Crear contactos ***************')


# main, de la aplicacion
if __name__ == '__main__':

	cliente_id = 'sa'
	cliente_pass = 'usac'
	# Menu de opciones de la aplicacion
	opcion = 0
	while opcion != 3:
		opcion = int(input("Que desea hacer:\n" + 
						"1. Listar\n" + 
						"2. Crear\n" + 
						"3. Salir\n"
						"R: "))
		if opcion == 1:
			# Llamar a la funcion que lista los contactos
			listar_Contactos(cliente_id, cliente_pass)
		elif opcion == 2:
			# Llamar a la funcion que crea los 10 contactos
			crear_Contactos(cliente_id, cliente_pass)

		# Salir de la aplicacion
		print("Exit")
