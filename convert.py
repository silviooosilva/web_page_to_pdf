import colorama
import pdfcrowd
import os
import platform
from time import sleep
import shutil


def creatdir(nome_dir: str):
    if os.path.isdir(nome_dir):
        print(f'{colorama.Fore.GREEN}OS ARQUIVOS SERÃO GUARDADOS EM "arquivosConvertidos"\nVERIFIQUE A PASTA NO FINAL DA OPERAÇÃO PARA ENCONTRAR OS FICHEIROS..')
        sleep(5)
        # os.system(c)
    else:
        os.mkdir(nome_dir)
        print(f'{colorama.Fore.GREEN}OS ARQUIVOS SERÃO GUARDADOS EM "arquivosConvertidos"\nVERIFIQUE A PASTA NO FINAL DA OPERAÇÃO PARA ENCONTRAR OS FICHEIROS..')
        sleep(5)
        # os.system(c)

def convert(endereco_site, nome_arquivo, diretorio):
    print(f'\n[*] POR FAVOR AGUARDE, O ARQUIVO {nome_arquivo}.pdf ESTA A SER REPRODUZIDO!\n...')
    api = pdfcrowd.HtmlToPdfClient("demo", "ce544b6ea52a5621fb9d55f8b542d14d")
    try:
        if 'https://' in endereco_site:
            api.convertUrlToFile(endereco_site, f'{nome_arquivo}.pdf')
        else:
            api.convertUrlToFile('https://' + endereco_site, f'{nome_arquivo}.pdf')
        shutil.move(f'{nome_arquivo}.pdf', diretorio)
        print('-' * 30)
        print(f'{colorama.Fore.GREEN}CONVERSÃO FEITA COM SUCESSO')
    except:
        print(f'\n{colorama.Fore.RED}ACONTECEU UM ERRO NÃO PROGRAMÁVEL!\nTENTE NOVAMENTE OU VERIFIQUE A SUA CONEXÃO A INTERNET..')
