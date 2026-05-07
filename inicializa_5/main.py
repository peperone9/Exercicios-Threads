import multiprocessing
from time import sleep

def imprime_thread(id):
    sleep(0.5)
    print(f"Thread #{id}")
    
    
    
def main():
    qnt= 5 #quantidade de threads criadas
    params = [0] * qnt
    for i in range(0,qnt):
        params[i]= i
    with multiprocessing.Pool(processes=qnt) as pool:
        pool.map(imprime_thread, params)
    

if __name__== "__main__":
    main()
