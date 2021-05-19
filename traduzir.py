#Importar
import urllib.request
import zipfile
import shutil
import os
#Arquivos
pasta = os.getcwd()+'/'
fonte = 'fonte.txt'
baixar = 'baixar.txt'
#Baixar os mods
f = open(baixar,'r')
textoFonte = f.read()
textoFonte = textoFonte.replace('\n','').split('*')
tamanho = len(textoFonte) - 1
x = 0
while x<tamanho:
	linha = textoFonte[x].split('|')
	url = linha[0]
	nomeMod = linha[1]
	nomePasta = linha[2]
	print('Instalando: '+nomeMod)
	#Baixar os mod
	urllib.request.urlretrieve(url, pasta+nomeMod+'.zip')
	#Extrair os mod
	with zipfile.ZipFile(nomeMod+'.zip',"r") as zip_ref:
	    zip_ref.extractall(pasta)
	shutil.move(pasta+nomePasta, pasta+nomeMod)
	os.remove(pasta+nomeMod+'.zip')
	x+=1
#Traduzir os arquivos dos mods
f = open(fonte,'r')
textoFonte = f.read()
textoFonte = textoFonte.replace('\n','').split('*')
tamanho = len(textoFonte) - 1
x = 0
while x<tamanho:
	linha = textoFonte[x].split('|')
	arquivo = pasta + linha[0]
	textoOriginal = linha[1]
	textoNovo = linha[2]
	#Lendo o arquivo
	ler = open(arquivo,'r')
	conteudoArquivo = ler.read()
	conteudoArquivo = conteudoArquivo.replace(textoOriginal,textoNovo)
	ler.close()
	#Escrevendo a resposta
	escrever = open(arquivo,'w')
	escrever.write(conteudoArquivo)
	escrever.close()
	x+=1
#print(textoFonte)
#print(tamanho)
f.close()
