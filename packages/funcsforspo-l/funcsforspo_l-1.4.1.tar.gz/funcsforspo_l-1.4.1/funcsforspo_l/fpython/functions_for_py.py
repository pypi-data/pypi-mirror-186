"""
## Várias funções para ajudar no desenvolvimento de qualquer aplicação em Python

### Nesse módulo você achará desde funções simples, até funções complexas que levariam um bom tempo para desenvolve-las.
"""
from __future__ import annotations

################################## IMPORTS #############################################
from configparser import RawConfigParser
from datetime import datetime, date, timedelta
from fnmatch import fnmatch
from time import sleep
import os, sys, shutil, platform, re, logging, unicodedata, gc, requests, time, json, threading
import subprocess as sp
import zipfile
from rich import print
from numpy import unicode_
################################## IMPORTS #############################################

def remover_acentos(text:str, encoding:str='utf-8'):
	try:
		text = unicode_(text, encoding=encoding)
	except Exception:
		pass
	text = unicodedata.normalize('NFD', text).encode('ascii', 'ignore').decode("utf-8")
	return str(text)

def getsizefile(path_file:str, return_convet_bytes: bool=False):
    """
    Função retorna o valor da função os.path.getsize()
    
    Args:
        path_file (str): O caminho do arquivo relativo
        return_convet_bytes (str): Converte o valor de bits para  B = Byte K = Kilo M = Mega G = Giga T = Tera P = Peta
        
    """
    FILE_PATH_ABSOLUTE = os.path.getsize(os.path.abspath(path_file))
    if return_convet_bytes:
        return convert_bytes(FILE_PATH_ABSOLUTE)
    return FILE_PATH_ABSOLUTE

def executa_garbage_collector(generation :int=False) -> int:
    """
    Portuguese:
    
    Execute o coletor de lixo.

    Sem argumentos, execute uma coleção completa. O argumento opcional pode ser um inteiro especificando qual geração coletar. Um ValueError é gerado se o número de geração for inválido.

    O número de objetos inacessíveis é retornado.
    
    #################################
    
    English:
    
    Run the garbage collector.

    With no arguments, run a full collection. The optional argument may be an integer specifying which generation to collect. A ValueError is raised if the generation number is invalid.

    The number of unreachable objects is returned.
    """
    if generation:
        return gc.collect(generation)
    else:
        return gc.collect()


def verifica_se_esta_conectado_na_vpn(ping_host :str):
    PING_HOST = ping_host
    """O método verificará por ping se está conectado no ip da VPN"""

    faz_log('Verificando se VPN está ativa pelo IP enviado no config.ini')
    
    output = sp.getoutput(f'ping {PING_HOST} -n 1')  # -n 1 limita a saída
    if ('Esgotado o tempo' in output) or ('time out' in output):
        faz_log('VPN NÃO CONECTADA!', 'w')
    else:
        faz_log("VPN conectada com sucesso!")


def transforma_lista_em_string(lista :list):
    try:
        return ', '.join(lista)
    except TypeError:
        lista = [str(i) for i in lista]
        return ', '.join(lista)


def remove_extensao_de_str(arquivo :str, extensao_do_arquivo :str) -> str:
    """Remove a extensão de um nome de arquivo.
    

    Args:
        arquivo (str): arquivo com a extensão em seu nome -> file.xlsx
        extensao_do_arquivo (str): extensão que deseja remover

    Returns:
        str: Nome do arquivo sem a extensão.
    """
    replacement =  arquivo.replace(f'.{extensao_do_arquivo}', '')
    replacement =  replacement.replace(f'{extensao_do_arquivo}', '')
    return replacement


def reverse_iter(iteravel :str | tuple | list) -> str | tuple | list:
    """Retorna qualquer iterável ao reverso
    
    Use:
        Antes da utilização: '1234567890'
        Antes da utilização: (1,2,3,4,5,6,7,8,9,0)
        Antes da utilização: [1,2,3,4,5,6,7,8,9,0]
    
    
        Após a utilização: '0987654321'
        Após a utilização: (0,9,8,7,6,5,4,3,2,1)
        Após a utilização: [0,9,8,7,6,5,4,3,2,1]

    * By https://www.geeksforgeeks.org/python-reversing-tuple/#:~:text=Since%20tuples%20are%20immutable%2C%20there,all%20of%20the%20existing%20elements.

    Args:
        iteravel (str | tuple | list): Qualquer iterável para ter seu valor reverso

    Returns:
        str | tuple | list: iterável com seus valores reversos
    """
    return iteravel[::-1]


def pega_caminho_atual(print_value: bool=False) -> str: 
    """Retorna o caminho absoluto do diretório de execução atual do script Python 
    
    Args: 
        print_value (bool, optional): Printa e retorna o path. Defaults to False. 
    
    Returns: 
        str: retorna o caminho absoluto da execução atual do script Python 
    """ 
    if print_value: 
        print(os.getcwd()) 
        return os.getcwd() 
    else: 
        return os.getcwd()


def cria_dir_no_dir_de_trabalho_atual(dir: str, print_value: bool=False, criar_diretorio: bool=True) -> str:
    """Cria diretório no diretório de trabalho atual
    
    1 - Pega o caminho atual de execução do script 
    
    2 - Concatena o "dir" com o caminho atual de execução do script 
    
    3 - Cria o diretório novo no caminho atual (optional) 
    
    
    Args: dir (str): Diretório que poderá ser criado print_value (bool, optional): Printa na tela a saida do caminho com o diretório criado. Defaults to False. 
          cria_diretorio (bool, optional): Cria o diretório enviado no caminho em que o script está sendo utilizado. Defaults to False. 
          
    Returns: 
        str: Retorna o caminho do dir com o caminho absoluto 
    """
    current_path = pega_caminho_atual()
    path_new_dir = os.path.join(current_path, dir) 
    if print_value: 
        print(path_new_dir) 
        if criar_diretorio: 
            os.makedirs(path_new_dir, exist_ok=True)  # Se existir, não cria
            return (path_new_dir)
    else: 
        if criar_diretorio: 
            os.makedirs(path_new_dir, exist_ok=True) 
        return (path_new_dir)

def deleta_diretorio(path_dir: str, use_rmtree: bool=True) -> None:
    """Remove um diretório com ou sem arquivos internos

    Args:
        path_dir (str): caminho relativo do diretório
        use_rmtree (bool, optional): Deleta arquivos e outros diretórios dentro do diretório enviado. Defaults to True.
    """
    DIRECTORY = os.path.abspath(path_dir)
    if os.path.exists(DIRECTORY):
        if use_rmtree:
            shutil.rmtree(DIRECTORY)
            sleep(3)
        else:
            os.rmdir(DIRECTORY)
    else:
        ...


def deleta_arquivos_duplicados(path_dir :str, qtd_copyes :int) -> None:
    """Deleta arquivos que contenham (1), (2) até a quantidade desejada
    
    Use:
        >>> deleta_arquivos_duplicados('dir', 2)
         dir--|
         
                 |---File.txt -> This is not deleted!
                 
                 |---File (1).txt -> This is deleted!
                 
                 |---File (2).txt -> This is deleted!
                 
                 |---File (3).txt -> This is not deleted!
                
    

    Args:
        path_dir (str): Caminho do diretório, relativo
        qtd_copyes (int): quantidade de possíveis arquivos repetidos
    """
    path_downloads = os.path.abspath(path_dir)
    arquivos = os.listdir(path_downloads)
    if (len(arquivos) > 1):
        copyes = [f'({i})' for i in range(qtd_copyes)]
        print(copyes)
        for copye in copyes:
            for arquivo in arquivos:
                if (copye in arquivo):
                    print(f'deletando {path_downloads}\\{arquivo}')
                    os.remove(path_downloads+'\\'+arquivo)  


def arquivos_com_caminho_absoluto_do_arquivo(path_dir: str) -> tuple[str]:
    """Retorna uma tupla com vários caminhos dos arquivos e diretórios

    ### O script pegará esse caminho relativo, pegará o caminho absoluto dele e concatenará com os arquivo(s) e/ou diretório(s) encontrado(s)
    
    Args:
        path_dir (str): caminho relativo do diretório

    Returns:
        tuple[str]: Retorna uma tupla com os arquivos e/ou diretórios
    """
    return tuple(os.path.join(os.path.abspath(path_dir), arquivo) for arquivo in os.listdir(path_dir))


def config_read(path_config: str) -> dict:
    """Le o config e retorna um dict

    Returns:
        dict: retorna todas as configurações
    """
    configs = RawConfigParser()
    configs.read(path_config)
    config = {s: dict(configs.items(str(s))) for s in configs.sections()}  # retorna o config como dict
    return config


def terminal(command):
    os.system(command)


def data_e_hora_atual_como_string(format: str='%d/%m/%y %Hh %Mm %Ss') -> str:
    """Retorna data ou hora ou os dois como string

    Args:
        format (str, optional): Formato da hora e data (ou só da hora ou só da data se preferir). Defaults to '%d/%m/%y %Hh %Mm %Ss'.

    Returns:
        str: hora / data atual como string
    """
    return datetime.now().strftime(format)


def adiciona_data_no_caminho_do_arquivo(file_path: str, format: str='%d/%m/%y-%Hh-%Mm-%Ss') -> str:
    """Adiciona data no inicio do arquivo.

    Args:
        date (datetime.datetime): Objeto datetime
        file_path (str): caminho do arquivo

    Returns:
        str: Retorna o arquivo com 
    """
    if isinstance(format, str):
        sufixo = 0
        file_name = os.path.basename(file_path)
        file_path = os.path.dirname(file_path)
        file_name, file_extension = os.path.splitext(file_name)
        file_name = data_e_hora_atual_como_string(format) + ' ' + file_name
        resultado_path = os.path.join(
            file_path, file_name + file_extension)
        while os.path.exists(resultado_path):  # caso o arquivo exista, haverá sufixo
            sufixo += 1
            resultado_path = os.path.join(
                file_path, file_name + str(sufixo) + file_extension)
        return resultado_path
    else:
        raise TypeError('Envie uma string no parâmetro format_date')


def baixar_arquivo_via_link(link: str, file_path: str, directory :bool|str=False):
    """Faz o download de arquivos pelo link que deve vir com a extensão do arquivo.

    ### É necessário que o arquivo venha com a sua extensão no link; exemplo de uso abaixo:
    
    Use:
        download_file(link='https://filesamples.com/samples/document/xlsx/sample3.xlsx', file_path='myplan.xlsx', directory='donwloads/')

    Args:
        link (str): link do arquivo que será baixado (deve vir com a extensão)
        file_path (str): destino do arquivo que será baixado (deve vir com a extensão)
        directory (str | bool): diretório de destino (será criado caso não exista), caso não envie, o arquivo ficará no diretorio de download atual. Optional, Default is False
    """
    if directory:
        cria_dir_no_dir_de_trabalho_atual(directory)
        file_path = os.path.join(os.path.abspath(directory), file_path)
        
    r = requests.get(link, allow_redirects=True)
    try:
        with open(file_path, 'wb') as file:
            file.write(r.content)
            print(f'Download completo! -> {os.path.abspath(file_path)}')
    except Exception as e:
        print(f'Ocorreu um erro:\n{str(e)}')
    finally:
        del r
        gc.collect()


def hora_atual(segundos: bool=False) -> str:
    """Função retorna a hora atual no formato hh:mm ou hh:mm:ss com segundos ativado"""
    from datetime import datetime
    e = datetime.now()
    if segundos:
        return f'{e.hour}:{e.minute}:{e.second}'
    else:
        return f'{e.hour}:{e.minute}'


def times() -> str:
    """Função retorna o tempo do dia, por exemplo, Bom dia, Boa tarde e Boa noite

    Returns:
        str: Periodo do dia, por exemplo, Bom dia, Boa tarde e Boa noite
    """
    import datetime
    hora_atual = datetime.datetime.now()
    if (hora_atual.hour < 12):
        return 'Bom dia!'
    elif (12 <= hora_atual.hour < 18):
        return 'Boa tarde!'
    else:
        return 'Boa noite!'

def verifica_se_caminho_existe(path_file_or_dir: str) -> bool:
    if os.path.exists(path_file_or_dir):
        return True
    else:
        return False

def deixa_arquivos_ocultos_ou_nao(path_file_or_dir : str, oculto : bool) -> None:
    """Deixa arquivos ou diretórios ocultos ou não.

    
    Use:
        >>> deixa_arquivos_ocultos_ou_nao(r'dir\file.txt', False)
        file.txt -> visible
        >>> deixa_arquivos_ocultos_ou_nao(r'dir\file.txt', True)
        file.txt -> not visible

    Args:
        path_file_or_dir (str): Arquivo ou diretório que deseja ocultar ou deixar visível
        oculto (str): Deixa o arquivo ou diretório oculto
    """

    import ctypes
    from stat import FILE_ATTRIBUTE_ARCHIVE
    FILE_ATTRIBUTE_HIDDEN = 0x02

    if oculto:
        ctypes.windll.kernel32.SetFileAttributesW(path_file_or_dir, FILE_ATTRIBUTE_HIDDEN)
        print(f'O arquivo / diretório {path_file_or_dir} ESTÁ OCULTO!')
    else:
        ctypes.windll.kernel32.SetFileAttributesW(path_file_or_dir, FILE_ATTRIBUTE_ARCHIVE)
        print(f'O arquivo / diretório {path_file_or_dir} NÃO ESTÁ MAIS OCULTO!')
        
    # HIDDEN = OCULTO
    # ARCHIVE = Ñ OCULTO


def fazer_requirements_txt() -> None:
    """"""
    os.system("pip freeze > requirements.txt")


def limpa_terminal_e_cmd() -> None:
    """Essa função limpa o Terminal / CMD no Linux e no Windows"""
    
    os.system('cls' if os.name == 'nt' else 'clear')


def limpa_diretorio(dir:str):
    """Limpa diretório(s)
    
    Args:
        dir (str): Caminho do diretório para limpar.
    """
    DIR = os.path.abspath(dir)
    if os.path.exists(DIR):
        shutil.rmtree(DIR)
        os.makedirs(DIR)
    else:
        os.makedirs(DIR)


def print_bonito(string : str, efeito='=', quebra_ultima_linha : bool=True) -> str:
    """Faz um print com separadores
    

    Args:
        string (str): o que será mostrado
        
    
    Exemplo:
        print_bonito('Bem vindo')
    
            =============
            = Bem vindo =
            =============
    
    
    """
    try:
        if len(efeito) != 1:
            print('O EFEITO DEVE SER SOMENTE UMA STRING efeito="="\n'
                '=========\n'
                '== Bem ==\n'
                '=========\n')
            return
        else:
            ...
        
        if quebra_ultima_linha:
            print(efeito*2 + efeito*len(string) + efeito*4)
            print(efeito*2 + ' '+string+' ' + efeito*2)
            print(efeito*2 + efeito*len(string) + efeito*4)
            print('')
        else:
            print(efeito*2 + efeito*len(string) + efeito*4)
            print(efeito*2 + ' '+string+' ' + efeito*2)
            print(efeito*2 + efeito*len(string) + efeito*4)
    except TypeError:
        print('O tipo de string, tem que ser obviamente, string | texto')


def instalar_bibliotecas_globalmente() -> None:
    """
        Instalar bibliotecas
            * pandas
            * unidecode
            * openpyxl
            * pyinstaller==4.6
            * selenium
            * auto-py-to-exe.exe
            * webdriver-manager
            * xlsxwriter
    """
    print('Instalando essas bibliotecas:\n'
          ' *pandas\n'
          ' *unidecode\n'
          ' *openpyxl\n'
          ' *pyinstaller==4.6\n'
          ' *selenium\n'
          ' *auto-py-to-exe.exe\n'
          ' *webdriver-manager\n'
          ' *xlsxwriter\n')
    aceita = input('você quer essas bibliotecas mesmo?s/n\n >>> ')
    if aceita == 's':
        os.system("pip install pandas unidecode openpyxl pyinstaller==4.6 selenium auto-py-to-exe webdriver-manager xlsxwriter")
        print('\nPronto')
    if aceita == '':
        os.system("pip install pandas unidecode openpyxl pyinstaller==4.6 selenium auto-py-to-exe webdriver-manager xlsxwriter")
        print('\nPronto')
    if aceita == 'n':
        dependencias = input('Escreva as dependencias separadas por espaço\nEX: pandas selenium pyautogui\n>>> ')
        os.system(f'pip install {dependencias}')
        print('\nPronto')
        sleep(3)


def criar_ambiente_virtual(nome_da_venv: str) -> None:
    nome_da_venv = nome_da_venv.strip()
    nome_da_venv = nome_da_venv.replace('.', '')
    nome_da_venv = nome_da_venv.replace('/', '')
    nome_da_venv = nome_da_venv.replace(',', '')
    os.system(f'python -m venv {nome_da_venv}')
    print(f'Ambiente Virtual com o nome {nome_da_venv} foi criado com sucesso!')
    sleep(2)
    
def restart_program() -> None:
    os.execl(sys.executable, sys.executable, *sys.argv)


def print_colorido(string : str, color='default', bolder : bool=False) -> str:
    """Dê um print com saida do terminal colorida

    Args:
        string (str): string que você quer colorir na saida do terminal / cmd
        color (str, optional): cor que você deseja colorir a string. Defaults to 'default'.
        bolder (bool, optional): se você deseja deixar a string com negrito / bolder. Defaults to False.
        
    Color List:
        white;
        red;
        green;
        blue;
        cyan;
        magenta;
        yellow;
        black.
    """
    color.lower()
    
    win_version = platform.system()+' '+platform.release()
    
    if ('Windows 10' in win_version) or 'Windows 11' in win_version:
        if bolder == False:
            if color == 'default':  # white
                print(string)
            elif color == 'red':  # red
                print(f'\033[31m{string}\033[m')
            elif color == 'green':  # green
                print(f'\033[32m{string}\033[m')
            elif color == 'blue':  # blue
                print(f'\033[34m{string}\033[m')
            elif color == 'cyan':  # cyan
                print(f'\033[36m{string}\033[m')
            elif color == 'magenta':  # magenta
                print(f'\033[35m{string}\033[m')
            elif color == 'yellow':  # yellow
                print(f'\033[33m{string}\033[m')
            elif color == 'black':  # black
                print(f'\033[30m{string}\033[m')
            
        elif bolder == True:
            if color == 'default':  # white
                print(f'\033[1m{string}\033[m')
            elif color == 'red':  # red
                print(f'\033[1;31m{string}\033[m')
            elif color == 'green':  # green
                print(f'\033[1;32m{string}\033[m')
            elif color == 'blue':  # blue
                print(f'\033[1;34m{string}\033[m')
            elif color == 'cyan':  # cyan
                print(f'\033[1;36m{string}\033[m')
            elif color == 'magenta':  # magenta
                print(f'\033[1;35m{string}\033[m')
            elif color == 'yellow':  # yellow
                print(f'\033[1;33m{string}\033[m')
            elif color == 'black':  # black
                print(f'\033[1;30m{string}\033[m')
    else:
        print(string)


def input_color(color : str='default', bolder: bool=False, input_ini: str='>>>') -> None:
    """A cor do input da cor que você desejar

    Args:
        color (str, optional): cor do texto do input (não o que o user digitar). Defaults to 'default'.
        bolder (bool, optional): adiciona um negrito / bolder na fonte. Defaults to False.
        input_ini (str, optional): o que você deseja que seja a string de saida do input. Defaults to '>>>'.

    Returns:
        input: retorna o input para ser adicionada em uma var ou qualquer outra coisa
        
    Color List:
        white;
        red;
        green;
        blue;
        cyan;
        magenta;
        yellow;
        black.
    """

    if bolder == False:
        if color == 'default':  # white
            return input(f'{input_ini} ')
        elif color == 'red':  # red
            return input(f'\033[31m{input_ini}\033[m ')
        elif color == 'green':  # green
            return input(f'\033[32m{input_ini}\033[m ')
        elif color == 'blue':  # blue
            return input(f'\033[34m{input_ini}\033[m ')
        elif color == 'cyan':  # cyan
            return input(f'\033[36m{input_ini}\033[m ')
        elif color == 'magenta':  # magenta
            return input(f'\033[35m{input_ini}\033[m ')
        elif color == 'yellow':  # yellow
            return input(f'\033[33m{input_ini}\033[m ')
        elif color == 'black':  # black
            return input(f'\033[30m{input_ini}\033[m ')
        else:
            print('Isso não foi compreensivel. Veja a doc da função, as cores válidas')
    elif bolder == True:
        if color == 'default':  # white
            return input(f'\033[1m{input_ini}\033[m ')
        elif color == 'red':  # red
            return input(f'\033[1;31m{input_ini}\033[m ')
        elif color == 'green':  # green
            return input(f'\033[1;32m{input_ini}\033[m ')
        elif color == 'blue':  # blue
            return input(f'\033[1;34m{input_ini}\033[m ')
        elif color == 'cyan':  # cyan
            return input(f'\033[1;36m{input_ini}\033[m ')
        elif color == 'magenta':  # magenta
            return input(f'\033[1;35m{input_ini}\033[m ')
        elif color == 'yellow':  # yellow
            return input(f'\033[1;33m{input_ini}\033[m ')
        elif color == 'black':  # black
            return input(f'\033[1;30m{input_ini}\033[m ')
        else:
            print('Isso não foi compreensivel.\nVeja na doc da função (input_color), as cores válidas')
    else:
        print('Não entendi, veja a doc da função (input_color), para utiliza-lá corretamente')


def move_arquivos(path_origem: str, path_destino: str, extension: str) -> None:
    """Move arquivos para outra pasta

    Args:
        path_origem (str): caminho de origem
        path_destino (str): caminho de destino
        extension (str): Estensão do arquivo.
    """

    arquivos_da_pasta_origem = os.listdir(path_origem)
    arquivos = [path_origem + "\\" + f for f in arquivos_da_pasta_origem if extension in f]
    
    for arquivo in arquivos:
        try:
            shutil.move(arquivo, path_destino)
        except shutil.Error:
            shutil.move(arquivo, path_destino)
            os.remove(arquivo)


def pega_somente_numeros(string :str) -> str or int:
    """Função pega somente os números de qualquer string
    
    * remove inclusive . e ,
    
    Args:
        string (str): sua string com números e outros caracteres

    Returns:
        str: somente os números
    """
    if isinstance(string, (str)):
        r = re.compile(r'\D')
        return r.sub('', string)
    else:
        print('Por favor, envie uma string como essa -> "2122 asfs 245"')
        return


def remove_arquivo(file_path : str) -> None:
    os.remove(os.path.abspath(file_path))


def remove_diretorio(dir_path : str):
    """Remove diretórios recursivamente

    Args:
        dir_path (str): caminho do diretório a ser removido
    """
    shutil.rmtree(os.path.abspath(dir_path))


def ver_tamanho_de_objeto(objeto : object) -> int:
    """Veja o tamanho em bytes de um objeto

    Args:
        objeto (object): objeto a verificar o tamanho

    Returns:
        int: tamanho do objeto
    """
    print(sys.getsizeof(objeto))


def read_json(file_json: str, enconding: str='utf-8') -> dict:
    """Lê e retorna um dict de um arquivo json

    Args:
        file_json (str): File Json
        enconding (str, optional): Encoding. Defaults to 'utf-8'.

    Returns:
        dict: Dados do arquivo Json
    """
    return json.load(open(file_json, "r", encoding=enconding))


def convert_bytes(tamanho: int|float):
    """Converte os bytes para
    >>> B = Byte

    >>> K = Kilo

    >>> M = Mega

    >>> G = Giga

    >>> T = Tera

    >>> P = Peta

    
    ### Utiliza-se a base 1024 ao invés de 1000

    Use:
        >>> tamanho_do_arquivo_em_bytes = os.path.getsize(C:\\MeuArquivo.txt)
        >>> print(tamanho_do_arquivo_em_bytes)
        >>>> 3923 
        >>> print(convert_bytes(tamanho_do_arquivo))
        >>>> '3.83 K'

    Args:
        tamanho (int|float): Tamanho do arquivo em bytes, pode ser utilizado o os.path.getsize(file)

    Returns:
        str: Valor do tamanho em B; K; M; G; T; P -> 
    """
    base = 1024
    kilo = base # K
    mega = base ** 2 # M
    giga = base ** 3 # G
    tera = base ** 4 # T
    peta = base ** 5 # P
    
    # se o tamanho é menor que kilo (K) é Byte
    # se o tamanho é menor que mega (M) é Kb
    # se o tamanho é menor que giga (G) é MB e assim por diante
    
    if isinstance(tamanho, (int, float)):
        pass
    else:
        print('Tentando converter o valor do parâmetro tamanho...')
        try:
            tamanho = float(tamanho)
        except ValueError as e:
            if 'could not convert string to float' in str(e):
                print(f'Não foi possível converter o tamanho ++ {tamanho} ++ para float!')
                return 'ValueError'
    if tamanho < kilo:
        tamanho = tamanho
        texto = 'B'
    elif tamanho < mega:
        tamanho /= kilo
        texto = 'K'
    elif tamanho < giga:
        tamanho /= mega
        texto = 'M'
    elif tamanho < tera:
        tamanho /= giga
        texto = 'G'
    elif tamanho < peta:
        tamanho /= tera
        texto = 'T'
    else:
        tamanho /= peta
        texto = 'P'
        
    tamanho = round(tamanho, 2)
    
    return f'{tamanho} {texto}'.replace('.', ',')


def time_now() -> float:
    """time() -> floating point number

    Returns:
        float: Return the current time in seconds since the Epoch. Fractions of a second may be present if the system clock provides them.
    """
    return time.time()


def ultimo_dia_do_mes_atual(format: str='%d/%m/%Y'):
    """Retorna a data com o último dia do mês

    Args:
        format (str, optional): formato da data. Defaults to '%d/%m/%Y'.

    Use:
        >>> ultimo_dia_do_mes_atual(format='%d/%m/%Y')
        >>>> '31/10/2022'

    Returns:
        str: data no formato
    """
    from calendar import mdays
    from datetime import datetime
    
    mes_atual = int(datetime.now().strftime('%m'))
    
    ultimo_dia = mdays[mes_atual]
    mes_atual = datetime.now().month
    ano_atual = datetime.now().year
    
    format_ = datetime.strptime(f'{ultimo_dia}/{mes_atual}/{ano_atual}', '%d/%m/%Y')

    return format_.strftime(format)

def apagar_todos_os_pacotes_pip():
    """Deleta todos os pacotes do pip instalados no ambiente em que for executado

    Caso não funcione, execute isso no terminal: `pip list --format=freeze | %{$_.split('==')[0]} | %{If(($_ -eq "pip") -or ($_ -eq "setuptools") -or ($_ -eq "wheel")) {} Else {$_}} | %{pip uninstall $_ -y}`
    """
    os.system("""pip list --format=freeze | %{$_.split('==')[0]} | %{If(($_ -eq "pip") -or ($_ -eq "setuptools") -or ($_ -eq "wheel")) {} Else {$_}} | %{pip uninstall $_ -y}""")

def atualizar_todos_os_pacotes_pip():
    """Atualiza todos os pacotes pip no ambiente atual (PODE DEMORAR MUITO)

    Caso não funcione, execute isso no terminal: `pip freeze | %{$_.split('==')[0]} | %{pip install --upgrade $_}`
    """
    os.system("""pip freeze | %{$_.split('==')[0]} | %{pip install --upgrade $_}""")

def retorna_o_tempo_decorrido(init: float|int, end: float|int, format: bool=True):
    """Retorna a expressão de (end - init) / 60

    Args:
        init (float | int): tempo de inicio da funcao, classe ou bloco
        end (float | int): tempo de finalizacao da funcao, classe ou bloco
        format (bool, optional): se deseja formatar por exemplo para 0.10 ou não. Defaults to True.

    Use:
    >>> from time import time
    >>> 
    >>> init = time()
    >>> ... your code ...
    >>> end = time()
    >>> result = retorna_o_tempo_decorrido(init, end)
    >>> print(result) >>> 0.17

    Returns:
        float|int: Valor do tempo total de execução
    """
    result = (end - init) / 60
    if format:
        return f'{result:.2f}'
    else:
        return result
        

def save_json(old_json: dict, file_json: str, enconding: str="utf-8") -> None:
    """Salva o arquivo JSON com o dict enviado no parâmetro.

    Args:
        old_json (dict): dict antigo com os dados alterados
        file_json (str): arquivo que será alterado
        enconding (str, optional): enconding. Defaults to "utf-8".
    """
    with open(file_json, 'w', encoding=enconding) as f:
        json.dump(old_json, f)


def fecha():
    """Fecha programa Python
    """
    try:
        sys.exit()
    except Exception:
        try:
            quit()
        except NameError:
            pass


def retorna_home_user() -> str:
    """Expand ~ and ~user constructions. If user or $HOME is unknown, do nothing.
    
    Use:
        >>> home = retorna_home_user()
        >>> print(home) >>> C:\\Users\\myuser
    
    Returns:
        str: $HOME -> C:\\Users\\myuser
    """
    return os.path.expanduser("~")

    
def fecha_em_x_segundos(qtd_de_segundos_p_fechar:int) -> None:
    """Espera os segundos enviados para fechar o programa

    Args:
        qtd_de_segundos_p_fechar (int): segundos para fazer regresivamente para fechar o programa
    """
    faz_log(f'Saindo do robô em: {qtd_de_segundos_p_fechar} segundos...')
    for i in range(qtd_de_segundos_p_fechar):
        faz_log(str(qtd_de_segundos_p_fechar))
        qtd_de_segundos_p_fechar -= 1
        sleep(1)
    fecha()
    
    
def zip_dirs(folders:list|tuple, zip_filename:str) -> None:
    """Faz zip de vários diretórios, recursivamente.

    Args:
        folders (list|tuple): folders
        zip_filename (str): name_file_zip with ``nome do arquivo.zip``
        
    Use:
        >>> folders = ['folder1', 'folder_with_files2', 'folder3',]
        >>> zip_dirs(folders, 'myzip.zip')
    """
    zip_file = zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED)

    for folder in folders:
        for dirpath, dirnames, filenames in os.walk(folder):
            for filename in filenames:
                zip_file.write(
                    os.path.join(dirpath, filename),
                    os.path.relpath(os.path.join(dirpath, filename), os.path.join(folders[0], '../..')))

    zip_file.close()
    
    
def resource_path(relative_path) -> str:
    """ Get absolute path to resource, works for dev and for PyInstaller 
    
        SE QUISER ADICIONAR ALGO NO ROBÔ BASTA USAR ESSA FUNÇÃO PARA ADICIONAR O CAMINHO PARA O EXECUTÁVEL COLOCAR
        * PARA USAR DEVE COLOCAR ESSA FUNÇÃO NO MÓDULO POR CAUSA DO os.path.abspath(__file__) * 
    """
    base_path = getattr(
        sys,
        '_MEIPASS',
        os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)    


def faz_log(msg: str, level: str = 'i', color: None|str=None, format: None|str=None) -> None:
    """Faz log na pasta padrão (./logs/botLog.log)



    Args:
        msg (str): "Mensagem de Log"
        level (str): "Niveis de Log"
        color (None|str): Cores Rich; defaut is None
        format (None|str) Formatação Rich; defaut is None

    Levels:
        'i' or not passed = info and print

        'i*' = info log only

        'w' = warning
        
        'c*' = critical / Exception Error exc_info=True
        
        'c' = critical
        
        'e' = error

    Use:
    >>> faz_log('@@@@@@@@@@@@@@@@@@@', color='red')
    >>> faz_log('@@@@@@@@@@@@@@@@@@@', color='red', format='b')
    >>> faz_log('@ O SISTEMA CAIU! @', color='red on yellow b i s blink')
    >>> faz_log('@@@@@@@@@@@@@@@@@@@', color='green')
    >>> faz_log('@@@@@@@@@@@@@@@@@@@', color='green b i')

    Formatação Rich:
            Colors: https://rich.readthedocs.io/en/latest/appendix/colors.html
    """
    path_logs_dir = os.path.abspath('logs')
    path_logs_file = os.path.join(path_logs_dir, 'logs.log')

    if not os.path.exists(path_logs_dir):
        os.mkdir(path_logs_dir)
    else:
        pass

    if isinstance(msg, str):
        pass
    
    if isinstance(msg, (object)):
        msg = str(msg)    
    

    if isinstance(level, (str)):
        pass
    else:
        print('COLOQUE UMA STING NO PARAMETRO LEVEL!')

    if isinstance(msg, (str)) and isinstance(level, (str)):
        if level == 'i' or level == '' or level is None:
            logging.basicConfig(filename=path_logs_file,
                                encoding='utf-8',
                                filemode='w',
                                format='%(asctime)s - %(levelname)s - %(message)s',
                                level=logging.INFO
                                )
            if isinstance(color, str) and isinstance(format, str):
                print(f'[{format}][{color}]{msg}[/{color}][/{format}]')
            elif isinstance(color, str):
                print(f'[{color}]{msg}[/{color}]')
            else:
                print(msg)
            if r'\n' in msg:
                msg = msg.replace(r"\n", "")
            logging.info(msg)

        if level == 'i*':
            logging.basicConfig(filename=path_logs_file,
                                encoding='utf-8',
                                filemode='w',
                                format='%(asctime)s - %(levelname)s - %(message)s',
                                level=logging.INFO
                                )
            if r'\n' in msg:
                msg = msg.replace(r"\n", "")
            logging.info(msg)

        elif level == 'w':
            logging.basicConfig(filename=path_logs_file,
                                encoding='utf-8',
                                filemode='w',
                                format='%(asctime)s - %(levelname)s - %(message)s',
                                level=logging.WARNING
                                )
            logging.warning(msg)
            if isinstance(color, str) and isinstance(format, str):
                print(f'[{format}][{color}]{msg}[/{color}][/{format}]')
            elif isinstance(color, str):
                print(f'[{color}]{msg}[/{color}]')
            else:
                print(msg)

        elif level == 'e':
            logging.basicConfig(filename=path_logs_file,
                                encoding='utf-8',
                                filemode='w',
                                format='%(asctime)s - %(levelname)s - %(message)s',
                                level=logging.ERROR
                                )
            logging.error(msg)
            if isinstance(color, str) and isinstance(format, str):
                print(f'[{format}][{color}]{msg}[/{color}][/{format}]')
            elif isinstance(color, str):
                print(f'[{color}]{msg}[/{color}]')
            else:
                print(msg)

        elif level == 'c':
            logging.basicConfig(filename=path_logs_file,
                                encoding='utf-8',
                                filemode='w',
                                format='%(asctime)s - %(levelname)s - %(message)s',
                                level=logging.CRITICAL
                                )
            logging.critical(msg)
            if isinstance(color, str) and isinstance(format, str):
                print(f'[{format}][{color}]{msg}[/{color}][/{format}]')
            elif isinstance(color, str):
                print(f'[{color}]{msg}[/{color}]')
            else:
                print(msg)

        elif level == 'c*':
            logging.basicConfig(filename=path_logs_file,
                                encoding='utf-8',
                                filemode='w',
                                format='%(asctime)s - %(levelname)s - %(message)s',
                                level=logging.CRITICAL
                                )
            logging.critical(msg, exc_info=True)
            if isinstance(color, str) and isinstance(format, str):
                print(f'[{format}][{color}]{msg}[/{color}][/{format}]')
            elif isinstance(color, str):
                print(f'[{color}]{msg}[/{color}]')
            else:
                print(msg)
    

def retorna_data_e_hora_a_frente(dias_a_frente: int, sep: str='/') -> str:
    """Retorna a data e hora com dias a frente da data atual
    ex: 15/06/2002 18:31 -> dias_a_frente=3 -> 18/06/2002 18:31
    """
    hj = date.today()
    futuro = date.fromordinal(hj.toordinal() + dias_a_frente)  # hoje + 3# dias
    dia_futuro = futuro.strftime(f'%d{sep}%m{sep}%Y')
    hora_futuro = datetime.today().strftime('%H:%M')
    return f'{dia_futuro} {hora_futuro}'


def adiciona_no_inicio_de_string(string:str, add_in: str, print_exit: bool=False):
    """Adiciona uma string no inicio de uma outra string

    Args:
        string (str): String que deseja ter algo na frente
        add_in (str): A string que será adicionada na frente da string
        print_exit (bool, optional): Da um print no valor pronto. Defaults to False.

    Returns:
        _type_: _description_
    """
    if print_exit:
        print(add_in+string[:])
    return add_in+string[:]


def recupera_arquivos_xlsx_de_uma_pasta(dir: str) -> list[str]:
    """Retorna uma lista somente com os arquivos que contenham .xlsx

    Args:
        dir (str): Caminho relativo do diretório que tem o(s) arquivo(s) .xlsx

    Returns:
        list[str]: Lista com todos os arquivos .xlsx (com o caminho absoluto)
    """
    DIR_PATH = os.path.abspath(dir)
    FILES = os.listdir(DIR_PATH)
    FILES_XLSX = []
    for fil in FILES:
        if '.xlsx' in fil:
            FILES_XLSX.append(DIR_PATH + "\\" + fil)
    else:
        return tuple(FILES_XLSX)
    
def recupera_arquivos_com_extensao_especifica_em_uma_pasta(dir: str, extensao:str='.xlsx') -> list[str]:
    """Retorna uma lista somente com os arquivos que contenham .xlsx

    Args:
        dir (str): Caminho relativo do diretório que tem o(s) arquivo(s) .xlsx

    Returns:
        list[str]: Lista com todos os arquivos .xlsx (com o caminho absoluto)
    """
    DIR_PATH = os.path.abspath(dir)
    FILES = os.listdir(DIR_PATH)
    FILES_XLSX = []
    for fil in FILES:
        if extensao in fil:
            FILES_XLSX.append(DIR_PATH + "\\" + fil)
    else:
        return tuple(FILES_XLSX)


def cria_o_ultimo_diretorio_do_arquivo(path: str,  print_exit :bool=False):
    """Cria o ultimo diretório de um arquivo
    Ex: meudir1\meudir2\meudir3\meufile.txt
        create meudir1\meudir2\meudir3
    https://stackoverflow.com/questions/3925096/how-to-get-only-the-last-part-of-a-path-in-python

    Args:
        path (str): caminho absoluto ou relativo do diretório
    """
    
    PATH_ABS = os.path.abspath(path=path)
    if print_exit:
        print(os.path.basename(os.path.normpath(PATH_ABS)))
    arquivo_para_remover =  os.path.basename(os.path.normpath(PATH_ABS))
    PATH = path.replace(arquivo_para_remover, '')
    try:
        os.makedirs(PATH)
    except FileExistsError:
        print('Diretório já criado anteriormente...')


def retorna_data_a_frente_(dias_a_frente: int, sep: str='/') -> str:
    """Retorna a data e hora com dias a frente da data atual
    ex: 15/06/2002 -> dias_a_frente=3 -> 18/06/2002
    """
    hj = date.today()
    futuro = date.fromordinal(hj.toordinal() + dias_a_frente)  # hoje + 3# dias
    return futuro.strftime(f'%d{sep}%m{sep}%Y')



def procura_por_arquivos_e_retorna_sobre(dir: str, termo_de_procura: str, mostrar: str='all_path_file'):
    """Retorna um arquivo e retorna vários dados do arquivo
    #### Escolha as opções disponíveis:
    >>> mostrar='all_path_file' # mostra o caminho completo do arquivo
    >>> mostrar='file_name' # mostra o nome do arquivo (sem ext)
    >>> mostrar='file_name_with_ext' # mostra o nome do arquivo (com ext)
    >>> mostrar='ext_file' # mostra a extensão do arquivo (sem o nome)
    >>> mostrar='size_bytes' # mostra o tamanho do arquivo em bytes (os.path.getsize())
    >>> mostrar='size' # mostra o tamanho do arquivo convertido em B; K; M; G; T; P
    

    Args:
        dir (str): _description_
        termo_de_procura (str): _description_
        mostrar (str, optional): _description_. Defaults to 'all_path_file'.

    Returns:
        _type_: _description_
    """
    encontrou = 0
    for raiz, diretorios, arquivos in os.walk(dir):
        for arquivo in arquivos:
            if termo_de_procura in arquivo:
                try:
                    caminho_completo_do_arquivo = os.path.join(raiz, arquivo) # une a raiz com o nome do arq
                    nome_do_arquivo, extensao_do_arquivo = os.path.splitext(arquivo)
                    tamanho_do_arquivo_em_bytes = os.path.getsize(caminho_completo_do_arquivo)
                    encontrou += 1
                    if mostrar == 'all_path_file':
                        return caminho_completo_do_arquivo
                    elif mostrar == 'file_name':
                        return nome_do_arquivo
                    elif mostrar == 'file_name_with_ext':
                        return arquivo
                    elif mostrar == 'ext_file':
                        return extensao_do_arquivo
                    elif mostrar == 'size_bytes':
                        return tamanho_do_arquivo_em_bytes
                    elif mostrar == 'size':
                        return convert_bytes(tamanho_do_arquivo_em_bytes)
                except PermissionError as e:
                    print(f'Sem permissões... {e}')
                except FileNotFoundError as e:
                    print(f'Não encontrado... {e}')
                except Exception as e:
                    print(f'Erro desconhecido... {e}')
    else:
        if encontrou >= 1:
            ...
        else:
            print('Nenhum arquivo encontrado!')
            
            
def splitlines_text(text: str) -> list[str]:
    """Separa uma string com \\n
    
    Use:
        >>> string = "this is \\nstring example....\\nwow!!!"
        >>> print(string.splitlines())
        >>>> ['this is ', 'string example....', 'wow!!!']


    Args:
        text (str): string com \\n

    Returns:
        list[str]: lista com as strings separadas pelo \\n
    """
    return text.splitlines()


def executa_threading(function_for_execute, args:tuple|bool=False):
    """
    Função recebe uma outra função e os seus argumentos em uma tupla, ou não caso não tenha argumentos.
    
    ### Teste a sua função antes de colocar aqui! =)
    
    Essa é um pequeno resumo do que a classe Thread faz
    
    Args:
        function_for_execute (CALLABLE): Função que será executada em uma Threading
        args (tuple|False): Tupla com os argumentos, ou False se não tiver nenhum argumento.

    Use:
        >>> def cria_diretorio(dir_name="diretório"):
        >>>     try:
        >>>         os.mkdir(dir_name)
        >>>         print('diretorio_criado')
        >>>     except FileExistsError:
        >>>         pass
        >>> 
        >>> print('Não executou a Thread')
        >>> executa_threading(cria_diretorio, ('meu_diretório',))
        >>> print('Executou a Thread')

        >>>> Não executou a Thread
        >>>> diretorio_criado
        >>>> Executou a Thread
    """
    if args == False:
        x = threading.Thread(target=function_for_execute)
    else:
        x = threading.Thread(target=function_for_execute, args=args)
    x.start()
    
def suporte_para_paths_grandes(dos_path, encoding=None):
    """
    Função retorna um path que suporta até 32.760 caracteres
    
    https://stackoverflow.com/questions/36219317/pathname-too-long-to-open"""
    if (not isinstance(dos_path, str) and encoding is not None): 
        dos_path = dos_path.decode(encoding)
    path = os.path.abspath(dos_path)
    if path.startswith(u"\\\\"):
        return u"\\\\?\\UNC\\" + path[2:]
    return u"\\\\?\\" + path

def formata_para_real(valor:str|float, sigl:bool=False):
    """
    Função retorna o número float como real (BRL)
    
    É necessário enviar um valor que tenha , na última casa
    -> 13076,9 ou enviar um valor float

    Use:
        not sigl
        >>> formata_para_real(192213.12)
        >>>> 192.213,12
        
        sigl
        >>> formata_para_real(192213.12, True)
        >>>> R$ 192.213,12

    Args:
        valor (str|float): valor que quer converter como real
        sigl (bool): Coloca a sigla do real na frente
        
    Returns:
        str: valor formatado como real
    """
    if valor == '':
        return
    if isinstance(valor, float):
        pass
    else:
        try:
            valor = float(str(valor).replace(',', '.')) # converte valor para float
        except ValueError:
            if sigl:
                return 'R$ '+valor
            return valor
    valor = f'{valor:_.2f}'
    valor = valor.replace('.', ',').replace('_', '.')
    if sigl:
        return 'R$ '+valor
    return valor

def cria_diretorios_para_novo_projeto_python():
    """# ATENÇÃO, UTILIZAR SOMENTE UMA VEZ NO MOMENTO DA CRIAÇÃO DO NOVO PROJETO!"""
    faz_log('Criando pasta e arquivo de logs com esse log...')
    # cria diretório src
    cria_dir_no_dir_de_trabalho_atual('src')
    # cria subdiretorios do src
    os.makedirs('src\\app', exist_ok=True)
    
    # CRIA ARQUIVO PYTHON EM SRC\\APP
    with open('src\\app\\app.py', 'w', encoding='utf-8') as f:
        f.write("""from FuncsForSPO.fpython.functions_for_py import *
from FuncsForSPO.fselenium.functions_selenium import *
""")
    
    os.makedirs('src\\base', exist_ok=True)
    
    # CRIA ARQUIVO PYTHON EM src\\base
    with open('src\\base\\base.py', 'w', encoding='utf-8') as f:
        f.write("""from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import *
from webdriver_manager.chrome import ChromeDriverManager
from FuncsForSPO.fpython.functions_for_py import *
from FuncsForSPO.fselenium.functions_selenium import *
from FuncsForSPO.fregex.functions_re import *
from src.exceptions.exceptions import *
import pandas as pd
import json
import os

# -- GLOBAL -- #
URL_SUPORTE = f'https://api.whatsapp.com/send?phone=5511985640273'
CONFIG_PATH = os.path.abspath('configs\\config.json')
BASE = os.path.abspath('base')
JSON_CONFIG_DATA = read_json(CONFIG_PATH)
# -- GLOBAL -- #


class Bot:    
    def __init__(self, headless, download_files) -> None:
        # --- CHROME OPTIONS --- #
        self._options = ChromeOptions()
        
        if download_files:
            # --- PATH BASE DIR --- #
            self.__DOWNLOAD_DIR =  cria_dir_no_dir_de_trabalho_atual(dir='downloads', print_value=False, criar_diretorio=True)
            limpa_diretorio(self.__DOWNLOAD_DIR)
            self._SETTINGS_SAVE_AS_PDF = {
                        "recentDestinations": [
                            {
                                "id": "Save as PDF",
                                "origin": "local",
                                "account": ""
                            }
                        ],
                        "selectedDestinationId": "Save as PDF",
                        "version": 2,
                    }


            self._PROFILE = {'printing.print_preview_sticky_settings.appState': json.dumps(self._SETTINGS_SAVE_AS_PDF),
                    "savefile.default_directory":  f"{self.__DOWNLOAD_DIR}",
                    "download.default_directory":  f"{self.__DOWNLOAD_DIR}",
                    "download.prompt_for_download": False,
                    "download.directory_upgrade": True,
                    "profile.managed_default_content_settings.images": 2,
                    "safebrowsing.enabled": True}
                
            self._options.add_experimental_option('prefs', self._PROFILE)
        
        if headless == True:
            self._options.add_argument('--headless')
            
        self._options.add_experimental_option("excludeSwitches", ["enable-logging", "enable-automation"])
        self._options.add_experimental_option('useAutomationExtension', False)
            
        self._options.add_argument(f"--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36")
        self._options.add_argument("--disable-web-security")
        self._options.add_argument("--allow-running-insecure-content")
        self._options.add_argument("--disable-extensions")
        self._options.add_argument("--start-maximized")
        self._options.add_argument("--no-sandbox")
        self._options.add_argument("--disable-setuid-sandbox")
        self._options.add_argument("--disable-infobars")
        self._options.add_argument("--disable-webgl")
        self._options.add_argument("--disable-popup-blocking")
        self._options.add_argument('--disable-gpu')
        self._options.add_argument('--disable-software-rasterizer')
        self._options.add_argument('--no-proxy-server')
        self._options.add_argument("--proxy-server='direct://'")
        self._options.add_argument('--proxy-bypass-list=*')
        self._options.add_argument('--disable-dev-shm-usage')
        self._options.add_argument('--block-new-web-contents')
        self._options.add_argument('--incognito')
        self._options.add_argument('–disable-notifications')
        self._options.add_argument("--window-size=1920,1080")
        
        self.__service = Service(ChromeDriverManager().install())
        
        # create DRIVER
        self.DRIVER = Chrome(service=self.__service, options=self._options)
        self.WDW3 = WebDriverWait(self.DRIVER, timeout=3)
        self.WDW5 = WebDriverWait(self.DRIVER, timeout=5)
        self.WDW7 = WebDriverWait(self.DRIVER, timeout=7)
        self.WDW10 = WebDriverWait(self.DRIVER, timeout=10)
        self.WDW30 = WebDriverWait(self.DRIVER, timeout=30)
        self.WDW = self.WDW7

        self.DRIVER.maximize_window()
        return self.DRIVER

    def quit_web(self):
        self.DRIVER.quit()
""")
    
    os.makedirs('src\\database', exist_ok=True)

    # CRIA ARQUIVO PYTHON EM SRC\\database
    with open('src\\database\\database.py', 'w', encoding='utf-8') as f:
        f.write("""from FuncsForSPO.fpython.functions_for_py import *
from FuncsForSPO.fselenium.functions_selenium import *
""")

    
    os.makedirs('src\\exceptions', exist_ok=True)
    
    # CRIA ARQUIVO PYTHON EM SRC\\exceptions
    with open('src\\exceptions\\exceptions.py', 'w', encoding='utf-8') as f:
        f.write("""from FuncsForSPO.fexceptions.exceptions import *
""")


    # cria diretório bin
    cria_dir_no_dir_de_trabalho_atual('bin')
    
    # cria arquivo json
    with open('bin\\config.json', 'w', encoding='utf-8') as fjson:
        fjson.write("""{
    "CONFIG": {
        "STRING": "STRING",
        "INT": 1,
        "BOOL": true
        }
}""")

    # cria diretório base
    cria_dir_no_dir_de_trabalho_atual('base')

    # cria ambiente virtual
    if os.path.exists('venv'):
        print('Ambiente Virtual "venv" já criado')
        pass
    else:
        print('Criando Ambiente Virtual')
        os.system('python -m venv venv')
    print('Criado')
    
def retorna_a_menor_ou_maior_data(datas:list[str|datetime], maior:bool=True, format:str='%d/%m/%Y %H:%M', format_return:str='%d/%m/%Y %H:%M'):
    """
    ## Recebe e retorna a MAIOR ou a menor data de uma lista de datas
    
    ### caso a lista de datas seja datetime, ele não haverá conversão

    ### É necessário que todas as datas estejam no padrão do formato enviado no parâmetro format

    Args:
        datas (list[str | datetime]): Lista de datas
        maior (bool, optional): Se estiver como True, irá retornar a maior data, ou seja a data mais atual. Se estiver setada como False, retornará a manor data. Defaults to True.
        format (str, optional): Formato que as datas devem vir para alterar. Defaults to '%d/%m/%Y %H:%M'.
        format_return (str, optional): O formato que a data maior ou menor será retornada. Defaults to '%d/%m/%Y %H:%M'.

    Returns:
        _type_: _description_
    """
    datas_datetime = []
    
    for data in datas:
        if isinstance(data, datetime):
            datas_datetime.append(data)
        else:
            datas_datetime.append(datetime.strptime(data, format))
        
    if maior:
        return max(datas_datetime).strftime(format_return)
    else:
        return min(datas_datetime).strftime(format_return)


def verifica_se_baixou_o_arquivo(diretorio_de_download, palavra_chave):
    _LOCAL_DE_DOWNLOAD = os.path.abspath(diretorio_de_download)
    baixou = False
    while not baixou:
        lista_arquivos = os.listdir(_LOCAL_DE_DOWNLOAD)
        if len(lista_arquivos) == 0:
            sleep(2)
            baixou = False
            lista_arquivos = os.listdir(_LOCAL_DE_DOWNLOAD)
        else:
            for i in lista_arquivos:
                if '.crdownload' in i:
                    sleep(2)
                    lista_arquivos = os.listdir(_LOCAL_DE_DOWNLOAD)
                    baixou = False
                    continue
                if palavra_chave in i:
                    baixou = True
                    faz_log('Download concluido!')
                    return True
                else:
                    sleep(2)
                    lista_arquivos = os.listdir(_LOCAL_DE_DOWNLOAD)
                    baixou = False
                    
def data_com_dias_mais_ou_menos(data:datetime, dias:int=0, menos:bool=True, format_exit='%d/%m/%Y') -> str|datetime:
    """Função retorna a data enviada com dias a menos ou a mais dependendo da escolha

    Args:
        data (datetime): Data no padrão de classe datetime
        dias (int, optional): Dias a frente ou dias atrás. Defaults to 0.
        menos (bool, optional): Se quiser que veja dias atrás, deixar como True, como dia a frente, deixar como False. Defaults to True.
        format_exit (str, optional): Formato da data, caso envie None ou '' ou ainda False, ele retornará um objeto Datetime. Defaults to '%d/%m/%Y'.

    Returns:
        str|datetime: Data

    Use:
        >>> # Digamos que a data atual seja: 07/12/2022 ela retornará 05/12/2022 -> com o Format ligado
        >>> In [1]: retorna_data_com_dias_meses_anos_atras_ou_a_frente(datetime.now(), 2)
        >>> In [2]: type(retorna_data_com_dias_meses_anos_atras_ou_a_frente(datetime.now(), 2))
        >>> Out [1]: 05/12/2022
        >>> Out [2]: <class 'str'>



        >>> # Digamos que a data atual seja: 07/12/2022 ela retornará 05/12/2022 -> Com o Format não definido
        >>> In [1]: retorna_data_com_dias_meses_anos_atras_ou_a_frente(datetime.now(), 2, format_exit=None)
        >>> In [2]: type(retorna_data_com_dias_meses_anos_atras_ou_a_frente(datetime.now(), 2, format_exit=None))
        >>> Out [1]: 2022-12-05 11:01:37.476540
        >>> Out [2]: <class 'datetime.datetime'>
    """
    if menos:
        data = data - timedelta(days=dias)
        if (format_exit == '') or (format_exit is None) or (isinstance(format_exit, bool)):
            return data
        data_ = data.strftime(format_exit)
        return data_
    else:
        data = data + timedelta(days=dias)
        if (format_exit == '') or (format_exit is None) or (isinstance(format_exit, bool)):
            return data
        data_ = data.strftime(format_exit)
        return data_

def remove_pontos_e_barras(string):
    """Função remove esses elementos da string
    
    '.'
    
    '/'
    
    ','
    
    '-'
    
    '_'
    
    '='
    
    '|'
    
    '#'
    
    '`'
    
    '~'
    
    "'"
    
    '"'
    
    'string'.strip()
    #### Função já converte o argumento para str()

    Args:
        string (str): str com os caracteres

    Returns:
        str: Retorna string sem nenhum desses caracteres
    """
    string = str(string)
    string = string.replace('.','')
    string = string.replace('/', '')
    string = string.replace(',', '')
    string = string.replace('-', '')
    string = string.replace('_', '')
    string = string.replace('=', '')
    string = string.replace('|', '')
    string = string.replace('`', '')
    string = string.replace('~', '')
    string = string.replace("'", '')
    string = string.replace('"', '')
    string = string.replace('#', '')
    string = string.replace(';', '')
    string = string.replace(':', '')
    string = string.replace('@', '')
    string = string.replace('!', '')
    string = string.replace('(', '')
    string = string.replace(')', '')
    string = string.replace('$', '')
    string = string.replace('%', '')
    string = string.replace('+', '')
    string = string.replace('&', '')
    string = string.replace('^', '')
    string = string.replace('*', '')
    string = string.replace('{', '')
    string = string.replace('}', '')
    string = string.replace('[', '')
    string = string.replace(']', '')
    string = string.strip()
    return string

def remove_duplicados_na_lista(iteravel:list|tuple, convert_str:bool=False):
    """Remove duplicados de uma lista

    Args:
        iteravel (list | tuple): Lista ou tupla com valores duplicados
        convert_str (bool): Converte automaticamente caso encontre um valor int, float na lista que contenha str's (TypeError treatment)

    Returns:
        list
    """
    if isinstance(iteravel, tuple):
        iteravel = list(iteravel)
    try:
        return sorted(set(iteravel))
    except TypeError:
        if convert_str:
            iteravel = [str(i) for i in iteravel]
            return sorted(set(iteravel))
        else:
            return None

def data_amigavel_bonita(time: datetime|int=datetime.now()):
    """
    Obtenha um objeto datetime ou um carimbo de data/hora int() Epoch e retorne um
    string bonita como 'uma hora atrás', 'Ontem', '3 meses atrás',
    'agora', etc
    
    Get a datetime object or a int() Epoch timestamp and return a
    pretty string like 'an hour ago', 'Yesterday', '3 months ago',
    'just now', etc
    
    Referência: https://stackoverflow.com/questions/1551382/user-friendly-time-format-in-python

    Args:
        time (datetime | int, optional): data preferencialmente datetime class. Defaults to datetime.now().

    Returns:
        str: data como por exemplo em redes sociais, um dia atrás, etc...
    """
    
    from datetime import datetime
    now = datetime.now()
    if type(time) is int:
        diff = now - datetime.fromtimestamp(time)
    elif isinstance(time, datetime):
        diff = now - time
    elif not time:
        diff = 0
    second_diff = diff.seconds
    day_diff = diff.days

    if day_diff < 0:
        return ''

    if day_diff == 0:
        if second_diff < 10:
            return "Agora mesmo"
        if second_diff < 60:
            return str(second_diff) + " segundo(s) atrás"
        if second_diff < 120:
            return "A um minuto atrás"
        if second_diff < 3600:
            return str(second_diff // 60) + " minuto(s) atrás"
        if second_diff < 7200:
            return "A uma hora atrás"
        if second_diff < 86400:
            return str(second_diff // 3600) + " hora(s) atrás"
    if day_diff == 1:
        return "Ontem"
    if day_diff < 7:
        return str(day_diff) + " dia(s) atrás"
    if day_diff < 31:
        return str(day_diff // 7) + " semana(s) atrás"
    if day_diff < 365:
        return str(day_diff // 30) + " mese(s) atrás"
    return str(day_diff // 365) + " ano(s) atrás"

def recupera_arquivos_com_a_extensao_indicada(filtro='*.pdf') -> list:
        """Recupera todos os arquivos *.extension que existirem no diretório atual, inclusive em pastas

        Args:
            filtro (str, optional): filtro para pesquisa de tipos de arquivos. Defaults to '*.pdf'.
        """
        files_with_extension = []
        for path, subdirs, files in os.walk(pega_caminho_atual()):
            for file in files:
                file_path = os.path.join(path, file)
                if fnmatch(file, filtro):
                    files_with_extension.append(file_path)
                else:
                    pass
        else:
            return files_with_extension

def arquivo_com_caminho_absoluto(dir:str|list|tuple, filename:str) -> str:
    """Usa join para unir os caminhos enviados por ti para que funcionem em qualquer sistema operacional
    ele recupera o caminho absoluto do(s) diretorio(s) enviado e concatena com o arquivo enviado

    Args:
        dir (str|list|tuple, optional): Diretório ou diretórios que deseja unir.
        filename (str, optional): Arquivo que deseja usar.

    Returns:
        str: caminho com o caminho absoluto
        
    Use:
        >>> # With list/tuple
        >>> file_db = arquivo_com_caminho_absoluto(['bin', 'database'], 'database.db') # -> CAMINHO_ABS/bin/database/database.db
        >>>
        >>> # With string
        >>> file_db = arquivo_com_caminho_absoluto('bin', 'database.db') # -> CAMINHO_ABS/bin/database.db
    """
    if isinstance(dir, (tuple, list)):
        return os.path.join(os.path.abspath(dir[0]), *dir[1:], filename)
    else:
        return os.path.join(os.path.abspath(dir), filename)

# Deprecado #
# def remove_espacos_pontos_virgulas_de_um_int(numero: int, remove_2_ultimos_chars: bool=False) -> int:
#     """Remove espaços, pontos, virgulas e se quiser os 2 últimos caracteres

#     Args:
#         numero (int): número com todos os elementos que serão removidos
#         remove_2_ultimos_chars (bool, optional): remove os 2 últimos caracteres, por exemplo, 0,00 fica 0. Defaults to False.

#     Returns:
#         int: _description_
#     """
#     numero = str(numero)
#     numero = numero.replace(',', '')
#     numero = numero.replace('.', '')
#     numero = numero.strip()
#     if remove_2_ultimos_chars:
#         numero = numero[:-2]
#     return int(numero)


# Deprecado #

