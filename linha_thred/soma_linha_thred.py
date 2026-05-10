#2) Fazer uma aplicação que, na main, inicialize uma variável id, inteira e inicialize 5 variáveis
#   inteiras para valores, crie um vetor de parâmetros, com o id como primeiro parâmetro e um
#   vetor com os 5 valores recebidos. As variáveis que recebem os valores devem receber, cada
#   uma delas, um valor aleatório de 1 a 100. Esses parâmetros devem ser preenchidos para 3
#   chamadas de Threads. Faça 3 chamadas de Threads, passando os parâmetros e, cada Thread,
#   deve calcular a soma de cada linha (Cada iteração do laço, para a soma deve ser seguido por
#   um sleep de 0.2 segundos), ao final, deve-se imprimir a identificação da linha e o resultado da
#   soma.


import multiprocessing
from time import sleep
from random import randint

def main():
    params = [(0,0)] * 3
    for i in range(0,3):
        id: int = i + 1
        v1: int = randint(1,100)
        v2: int = randint(1,100)
        v3: int = randint(1,100)
        v4: int = randint(1,100)
        v5: int = randint(1,100)
        params[i] = (id, [v1,v2,v3,v4,v5])
            #processamento(id, [v1,v2,v3,v4,v5]) #COMPARA SEQUENCIAL COM PARALELO
     
    with multiprocessing.Pool(processes=3) as pool:
        pool.starmap(processamento, params)

   
        
    
def processamento(id, numeros):
    soma = 0
    for i in range(0,5):
        soma += numeros[i]
        print(f"SOMANDO... Linha{id} {numeros} -> {soma} ")
        sleep(0.2)
        


    print(f"\nSOMA FINAL: Linha{id} {numeros} -> {soma}")

if __name__ == "__main__":
    main()
