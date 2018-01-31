from boletin8 import convertir_a_euros
with open("comunicaciones.txt","r") as archivo:
	contenido= archivo.readlines().strip("\n")
for linea in contenido:
	if linea != "Tarifa 3":
		cosasdelinea=linea.split(":")
print(cosasdelinea)