import pdfcrowd
import os
import shutil
import platform
from time import sleep
import colorama

# ativando o colorama, ferramenta que
# facilita a coloração do terminal
colorama.init(autoreset=True)

if "windows" in platform.system().lower():
    c = 'cls'
else:
    c = 'clear'
# os.system(c)
diretorio = './arquivosConvertidos'


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


def banner():
    print(f"""{colorama.Fore.CYAN}
\t\t--------------------------------
\t\t|  CONVERSOR HTML TO PDF v1.1  |
\t\t--------------------------------
""")


def main(endereco_site, nome_arquivo):
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
    except Exception as e:
        print(f'\n{colorama.Fore.RED}ACONTECEU UM ERRO NÃO PROGRAMÁVEL!\nTENTE NOVAMENTE OU VERIFIQUE A SUA CONEXÃO A INTERNET..')


if __name__ == '__main__':
    try:
        creatdir(diretorio)
        banner()
        site = str(input('DIGITE A URL DO SITE:\n> '))
        nome = str(input('DIGITE O NOME COM QUE QUER GUARDAR O PDF:\n> '))
        main(site, nome)
    except Exception as erro:
        pass
    finally:
        print(f'\n{colorama.Fore.YELLOW}By: SÍLVIO SILVA')
