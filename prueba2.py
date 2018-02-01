from boletin8 import convertir_a_euros
with open("comunicaciones.txt","r") as archivo:
	contenido= archivo.readlines()
lista=[]
for linea in contenido:
	if linea != "Tarifa 3":
		tiempos=linea.strip("\n").split(":")
		lista.append(tiempos)
print(lista)
for tiempo in lista[1:]:
	comunicacion=convertir_a_euros(tiempo[0],tiempo[1],tiempo[2],3)
	print("Esta comunicacion ha costado %d euros y %d centimos"%(euros,cent))
