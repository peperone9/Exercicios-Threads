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
