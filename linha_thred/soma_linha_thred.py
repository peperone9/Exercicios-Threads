import multiprocessing
from time import sleep
from random import randint

def main():
    params = [(0,0)] * 3
    for i in range(0,3):
        id: int = i + 1
        v1: int = randint(1,100000000)
        v2: int = randint(1,100000000)
        v3: int = randint(1,100000000)
        v4: int = randint(1,100000000)
        v5: int = randint(1,100000000)
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
