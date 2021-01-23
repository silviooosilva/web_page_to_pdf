import pdfcrowd 
import os
import shutil
import platform
from time import sleep
if("windows" in platform.system().lower()):
    c = 'cls'
else:
    c = 'clear'
os.system(c)
dir = './arquivosConversor'
def creatdir(dir):
    if os.path.isdir(dir):
         print('\033[1;32mVERIFIQUE A PASTA arquivosConversor PARA ENCONTRAR OS FICHEIROS\033[m') 
         sleep(3)
         os.system(c)
    else:
        os.mkdir(dir)
        print('\033[1;32mVERIFIQUE A PASTA arquivosConversor PARA ENCONTRAR OS FICHEIROS\033[m')
        sleep(3)
        os.system(c)
creatdir(dir)  
def banner():
    print('-'*30)
    print('CONVERSOR HTML TO PDF 1.0') 
    print('-'*30) 
def main(site, nome):
    api = pdfcrowd.HtmlToPdfClient("demo", "ce544b6ea52a5621fb9d55f8b542d14d")
    try:
        if site not in 'https://':
            api.convertUrlToFile('https://'+site, nome+'.pdf')
        else:
            api.convertUrlToFile(site, nome+'.pdf')
        shutil.move(nome+'.pdf',dir) 
        print('-'*30)
        print('\033[1;32mCONVERSÃO FEITA COM SUCESSO\033[m') 
    except:
        print('\033[1;31m\nACONTECEU UM ERRO NÃO PROGRAMÁVEL!\nTENTE NOVAMENTE OU VERIFIQUE A SUA CONEXÃO A INTERNET\033[m')
banner()
site = str(input('DIGITE A URL DO SITE: '))
nome = str(input('DIGITE O NOME QUE QUER NO PDF: '))
main(site, nome)
print('\n\033[1;33mBy: SÍLVIO SILVA \033[m') 