# 4) No Sistema Operacional Linux, o comando para realizar uma operação de ping com 10
# iterações é ping -4 -c 10 <servidor> e no Sistema Operacional Windows, o comando para a
# mesma função é ping -4 -n 10 <servidor>. Fazer uma aplicação Java que rode 3 Threads, sendo
# que a Thread deve identificar o SO para rodar o comando certo, fazendo operação de ping para
# os servidores UOL (www.uol.com.br), Terra (www.terra.com.br) e Google (www.google.com.br).
# Cada thread deve ler a saída do ping imprimindo, a cada iteração, o nome do servidor (usar
# fixo: UOL, Terra ou Google) e o tempo daquela iteração. Ao fim, deve-se exibir o nome do
# servidor (usar fixo: UOL, Terra ou Google) e o tempo médio obtido pela operação. Outros
# Sistemas Operacionais devem ser descartados.



import subprocess
import platform
import multiprocessing

def acessar(requisicao):
	alvo: str = ""
	buffer = requisicao.stdout.readline().decode("utf-8", errors="ignore")
	while buffer != "":
		if "avg" in buffer or "Average" in buffer or (", " in buffer and "ms" in buffer):
			alvo = buffer
			return alvo
		buffer = requisicao.stdout.readline().decode("utf-8", errors="ignore")
	return "erro ao executar o comando"

def media_linux(conteudo):
	media = conteudo.split(" = ")
	media = media[1].split("/")
	media = media[1]
	return media + "ms"
def media_windows(conteudo):
	media = conteudo.split(", ")
	media = media[2].split(" = ")
	media = media[1]
	return media

def ping(site, url):
	comando = ["ping", "-4", "-c", "10", url]
	if(platform.system() == "Linux"):
		resposta = subprocess.Popen(comando, stdout=subprocess.PIPE)
		conteudo = acessar(resposta)
		tempo = media_linux(conteudo)
		print(f"\n{site}\n{tempo}")
	elif(platform.system() == "Windows"):
		comando = ["ping", "-4", "-n", 10, url]
		resposta = subprocess.Popen(comando, stdout=subprocess.PIPE)
		conteudo = acessar(resposta)
		tempo = media_windows(conteudo)
		print(f"\n{site}\n{tempo}")
	else:
		print("Sistema operacional não compatível com a aplciacao")

def main():
	urls = [
		"www.google.com",
		"www.terra.com.br",
		"www.uol.com.br"
		]

	sites= [
		"Google",
		"UOL",
		"Terra"
		]
	parametros = [0] * 3 

	for i in range(3):
		parametros[i] = (sites[i], urls[i])
		#ping(sites[i], urls[i]) #testa linear
	with multiprocessing.Pool(processes=3) as p:
		p.starmap(ping, parametros)

if __name__ == "__main__":
	main()
