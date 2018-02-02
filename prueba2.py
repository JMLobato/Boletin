from boletin8 import convertir_a_euros,pasar_a_segundos
with open("comunicaciones.txt","r") as archivo:
	tarifa= archivo.readline()
	contenido= archivo.readlines()
lista=[]
for linea in contenido:
	tiempos=linea.strip("\n").split(":")
	lista.append(tiempos)
for tiempo in lista[1:]:
	euros,cent=convertir_a_euros(pasar_a_segundos(int(tiempo[0]),int(tiempo[1]),int(tiempo[2])),3)
	print("Esta comunicacion ha costado %d euros y %d centimos"%(euros,cent))