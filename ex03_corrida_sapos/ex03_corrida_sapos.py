# 3 - Fazer uma aplicação de uma corrida de sapos, com 5 Threads, cada Thread controlando 1 sapo. 
# Deve haver um tamanho máximo para cada pulo do sapo (em centímetros) e a distância máxima para que os sapos percorram. 
# A cada salto, um sapo pode dar um salto de 0 até o tamanho máximo do salto (valor aleatório entre 1 e 5 cm.). Após dar um salto,
# a Thread, para cada sapo, deve mostrar no console, qual foi o tamanho do salto e quanto o sapo percorreu. Assim que o 
# sapo percorrer a distância máxima, a Thread deve apresentar que o sapo chegou. 
# Dica: O exercício deve ser resolvido todo em console, ou seja, como se estivesse sendo narrado.

import multiprocessing
import random
import time

def corrida(sapo, distancia):
	percurso: int = 0 #posição atual do sapo
	pulo: int #tamanho do pulo

	while percurso < distancia:
		pulo = random.randint(0,5)
		percurso += pulo
		if pulo != 0:
			print(f"Sapo {sapo} pula {pulo}cm !! percorrendo {percurso}cm")
		else:
			print(f"Sapo {sapo} ficou parado!!")
		time.sleep(0.5)
	print(f"\t=== -----> SAPO {sapo} TERMINOU A CORRIDA !! <----- ===")

def main():
	distancia: int #distancia do sapo até a linha de chegada
	distancia = 20

	qnt: int = 5 #quantidade de sapos na corrida
	sapos = [(0,0)] * qnt
	for i in range(qnt):
		sapos[i] = (i + 1, 20)

	print(f"----> INICIO DA CORRIDA DE {distancia}CMs <----")
	#inicia corrida
	with multiprocessing.Pool(processes=5) as p:
		p.starmap(corrida, sapos)

if __name__ == "__main__":
	main()
