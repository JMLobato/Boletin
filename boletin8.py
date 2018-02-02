def pasar_a_segundos(h,m,s):
	total_seg=(h*3600)+(m*60)+s
	return total_seg

def calcular_coste(segundos,tarifa):
	total=segundos*tarifa #se multiplica los segundos por la tarifa
	return total

def convertir_a_euros(segundos,tarifa):
	cent=calcular_coste(segundos,tarifa)
	euros=cent/100
	premisa=False
	cent=""
	for elem in str(euros):
		if elem == ".":
			premisa=True
		if premisa==True:
			if elem != ".":
				cent=cent+elem
	return euros,int(cent)
