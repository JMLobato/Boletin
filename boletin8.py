def pasar_a_segundos(h,m,s):
	total_seg=(h*3600)+(m*60)+s
	return total_seg

def calcular_coste(h,m,s):
	total=(pasar_a_segundos(h,m,s))*100 #si 1 euro son X segundos, el calculo en cent se realizará multiplicando esos segundos por 100
	return total

def convertir_a_euros(h,m,s):
cent=calcular_coste(h,m,s)
total=(cent/100)%100
