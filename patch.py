#Importar
import urllib.request
import zipfile
import shutil
import os
#Definir as vars de pastas
pasta = os.getcwd()+'/'
pasta_bin = pasta+'bin/'
pasta_Mod = pasta+'Mod/'
#Baixar os arquivos de config
urllib.request.urlretrieve('https://raw.githubusercontent.com/riqueenz/Free-CAD-config/main/enzweiler.system.cfg', pasta+'enzweiler.system.cfg')
urllib.request.urlretrieve('https://raw.githubusercontent.com/riqueenz/Free-CAD-config/main/enzweiler.user.cfg', pasta+'enzweiler.user.cfg')
os.remove(pasta+'RunFreeCAD.bat')
urllib.request.urlretrieve('https://raw.githubusercontent.com/riqueenz/Free-CAD-config/main/RunFreeCAD.bat', pasta+'RunFreeCAD.bat')
urllib.request.urlretrieve('https://raw.githubusercontent.com/riqueenz/Free-CAD-config/main/fonte.txt', pasta+'fonte.txt')
urllib.request.urlretrieve('https://raw.githubusercontent.com/riqueenz/Free-CAD-config/main/baixar.txt', pasta+'baixar.txt')
urllib.request.urlretrieve('https://raw.githubusercontent.com/riqueenz/Free-CAD-config/main/macros.txt', pasta+'macros.txt')
#Arquivos
fonte = 'fonte.txt'
baixar = 'baixar.txt'
macros = 'macros.txt'
#Baixar as macros
if not os.path.exists(pasta_bin+'/macros/'):
    os.makedirs(pasta_bin+'/macros/')
f = open(macros,'r')
textoFonte = f.read()
textoFonte = textoFonte.replace('\n','').split('*')
tamanho = len(textoFonte) - 1
x = 0
while x<tamanho:
	linha = textoFonte[x].split('|')
	url = linha[0]
	nome_macro = linha[1]
	print('Instalando macro : '+nome_macro)
	#Baixar as macros
	urllib.request.urlretrieve(url, pasta_bin+'/macros/'+nome_macro)
	x+=1
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
	nomepasta_Mod = linha[2]
	print('Instalando: '+nomeMod)
	#Baixar os mod
	urllib.request.urlretrieve(url, pasta_Mod+nomeMod+'.zip')
	#Extrair os mod
	with zipfile.ZipFile(pasta_Mod+nomeMod+'.zip',"r") as zip_ref:
	    zip_ref.extractall(pasta_Mod)
	shutil.move(pasta_Mod+nomepasta_Mod, pasta_Mod+nomeMod)
	os.remove(pasta_Mod+nomeMod+'.zip')
	x+=1
#Traduzir os arquivos dos mods
f = open(fonte,'r')
textoFonte = f.read()
textoFonte = textoFonte.replace('\n','').split('*')
tamanho = len(textoFonte) - 1
x = 0
while x<tamanho:
	linha = textoFonte[x].split('|')
	arquivo = pasta_Mod + linha[0]
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
