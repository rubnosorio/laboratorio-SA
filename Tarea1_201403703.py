import requests
import json

# Funcion que permite listar los contactos de la aplicacion
def listar_Contactos():
	#Recursos necesarios para realizar la peticion
	url = 'https://api.softwareavanzado.world/index.php?webserviceClient=administrator&webserviceVersion=1.0.0&option=contact&api=hal'
	headers = { 'Content-Type': 'application/json'}
	args = { 'list[limit]': '0'}
	# Haciendo peticion al servidor
	response = requests.get(url, params=args, headers = headers)

	# Empezar a listar los contactos existentes
	print('*************** Start Listar ***************')
	if response.status_code == 200:
		response_json = response.json() #La variable response_json Es un diccionario
		
		# Se obtiene la lista de contactos
		contactos = response_json['_embedded']['item']

		if contactos:

			# Por cada contacto se imprime su id y su nombre
			for contacto in contactos:
				id_ = contacto['id']
				nombre = contacto['name']

				# Generando cadena de salida por cada contacto encontrado
				contacto_data = "ID: {0}, Name: {1}"
				print(contacto_data.format(id_, nombre))

	print('*************** End Listar ***************')


# Funcion que permite crear los 10 clientes solicitados, segun las instrucciones
def crear_Contactos():
	#Recursos necesarios para realizar la peticion
	url = 'https://api.softwareavanzado.world/index.php?webserviceClient=administrator&webserviceVersion=1.0.0&option=contact&api=hal'
	headers = { 'Content-Type': 'application/json'}
	args = { 'list[limit]': 0}
	# Empezar a crear los contactos
	print('*************** Start Crear contactos ***************')
	#numero de contactos 
	NContactos = 0
	while NContactos < 10:
		nombre = "201403703_No_" + str(NContactos)
		payload = { "name": nombre, "catid": NContactos }

		# Haciendo peticion al servidor
		response = requests.post(url, params = args, json=payload, headers = headers)

		if response.status_code == 201:
			# Generando cadena de salida por cada contacto creado				
			print(payload)

		# Update contador
		NContactos+=1

	print('*************** End Crear contactos ***************')


# main, de la aplicacion
if __name__ == '__main__':

	# Obtener el token de autenticacion para utilizar las funciones posteriores
	#access_token = GetToken('client_credentials', 'annelice119@gmail.com', '201403819')

	# Si se logra obtener el token, ingresar al menu de opciones
	if 1==1:

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
				listar_Contactos()
			elif opcion == 2:
				# Llamar a la funcion que crea los 10 contactos
				crear_Contactos()

		# Salir de la aplicacion
		print("Exit")
