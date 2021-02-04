import platform
import colorama
from convert import convert, creatdir

# ativando o colorama, ferramenta que
# facilita a coloração do terminal
colorama.init(autoreset=True)

if "windows" in platform.system().lower():
    c = 'cls'
else:
    c = 'clear'
# os.system(c)
diretorio = './arquivosConvertidos'


def banner():
    print(f"""{colorama.Fore.CYAN}
\t\t--------------------------------
\t\t|  CONVERSOR HTML TO PDF v1.1  |
\t\t--------------------------------
""")



if __name__ == '__main__':
    try:
        creatdir(diretorio)
        banner()
        site = str(input('DIGITE A URL DO SITE:\n> '))
        nome = str(input('DIGITE O NOME COM QUE QUER GUARDAR O PDF:\n> '))
        convert(site, nome, diretorio)
    except Exception as erro:
        pass
    finally:
        print(f'\n{colorama.Fore.YELLOW}By: SÍLVIO SILVA')