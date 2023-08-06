from __future__ import annotations

from ftplib import FTP, FTP_TLS
import ftplib
import os


def enviar_arquivo_via_ftp(host: str, user: str, passwd: str, filename_path_ftp: str, filename_path_upload: str):
    """Envia um arquivo via FTP
    ### Só é possível enviar arquivos, e um de cada vez.

    Args:
        host (str): Host do FTP
        user (str): Usuário do FTP
        passwd (str): Senha do FTP
        filename_path_ftp (str): Caminho do arquivo no FTP
        filename_path_upload (str): Caminho do arquivo no Computador
    """
    with FTP_TLS(host=host, user=user, passwd=passwd) as ftp:
        print('Acessando FTP_TLS')
        with open(filename_path_upload, "rb") as file:
            # use FTP's STOR command to upload the file
            ftp.storbinary(f"STOR {filename_path_ftp}", file)
            print('Upload concluido!')
            
            
def baixar_arquivo_via_ftp(host: str, user: str, passwd: str, filename_path_ftp: str, filename_path_download: str) -> None:
    """Faz o download de um arquivo via FTP

    Args:
        host (str): Host do FTP
        user (str): Usuário do FTP
        passwd (str): Senha do FTP
        filename_path_ftp (str): Caminho do arquivo para baixar (PATH FTP)
        filename_path_download (str): Caminho do Download
    """
    with FTP_TLS(host=host, user=user, passwd=passwd) as ftp:
        print('Acessando FTP_TLS')
        with open(filename_path_download, "wb") as file_:
            print('Fazendo download do arquivo...')
            ftp.retrbinary(f"RETR {filename_path_ftp}", file_.write,)
            print('Download concluido!')
            
def lista_todos_os_arquivos_ftp(host: str, user: str, passwd: str, dir: bool|str=False):
    """Lista os arquivos no dir ou na raiz

    Args:
        host (str): host
        user (str): user
        passwd (str): passwd
        dir (bool | str, optional): dir para listar. Defaults to False.

    Returns:
        _type_: _description_
    """
    ftp = FTP(host, user, passwd)
    if dir:
        ftp.cwd(dir)
    ftp.retrlines('LIST')
    ftp.quit()
            
            
def remover_diretorio_recursivamente_ftp(host, user, passwd, path):
    """Recursively delete a directory tree on a remote server.
    https://gist.github.com/artlogic/2632647
    """
    ftp = FTP(host, user, passwd)
    
    wd = ftp.pwd()

    try:
        names = ftp.nlst(path)
    except ftplib.all_errors as e:
        # some FTP servers complain when you try and list non-existent paths
        print('FtpRmTree: Could not remove {0}: {1}'.format(path, e))
        return

    for name in names:
        if os.path.split(name)[1] in ('.', '..'): 
            continue

        print('FtpRmTree: Checking {0}'.format(name))

        try:
            ftp.cwd(name)  # if we can cwd to it, it's a folder
            ftp.cwd(wd)  # don't try a nuke a folder we're in
            remover_diretorio_recursivamente_ftp(host, user, passwd, path)
        except ftplib.all_errors:
            ftp.delete(name)

    try:
        ftp.rmd(path)
    except ftplib.all_errors as e:
        print('FtpRmTree: Could not remove {0}: {1}'.format(path, e))
            
def cria_diretorio_no_ftp(host, user, passwd, dir: str, show_list: bool=False):
    """Cria um diretório no server ftp

    Args:
        host (str): host
        user (str): user
        passwd (str): passwd
        dir (str): diretório que será criado
        show_list (bool, optional): mostrar a lista de arquivos e diretorios, no final. Defaults to False.
    """
    ftp = FTP(host, user, passwd)
    try:
        ftp.mkd(dir)
    except ftplib.error_perm as e:
        print(f'Provavelmente já existe o diretório. {str(e)}')
    if show_list:
        ftp.retrlines('LIST')
    ftp.quit()
            
def alterar_permissao_de_arquivo_ftp(host: str, user: str, passwd: str, file_path_ftp: str, permission: str|int, force_permission: bool=False):
    """Altera a permissão em um arquivo ou pasta em um servidor FTP
    
    Permissões Disponiveis:
    
    #### 700
        Owner -> Ler; Gravar e Executar
        
        Group -> NOT ler; NOT gravar and NOT Executar
        
        Public -> NOT ler; NOT gravar and NOT Executar
        
    #### 770
        Owner -> Ler; Gravar e Executar
        
        Group -> Ler; Gravar e Executar
        
        Public -> NOT ler; NOT gravar and NOT Executar
        
    #### 777
        Owner -> Ler; Gravar e Executar
        
        Group -> Ler; Gravar e Executar
        
        Public -> Ler; Gravar e Executar
        
    #### 000
        Owner -> NOT ler; NOT gravar and NOT Executar
        
        Group -> NOT ler; NOT gravar and NOT Executar
        
        Public -> NOT ler; NOT gravar and NOT Executar

    Args:
        host (str): host ftp
        user (str): user ftp
        passwd (str): password ftp
        file_path_ftp (str): path_archive_ftp
        permission (str|int): permission
        force_permission (bool|int): force permission not predefined
    """
    with FTP_TLS(host=host, user=user, passwd=passwd) as ftp:
        print('Acessando FTP_TLS')
        try:
            if permission == '700' or permission == 700:
                ftp.sendcmd('SITE CHMOD 700 ' + file_path_ftp)
                print('Permissão 700 alterada com sucesso...')
                
            elif permission == '770' or permission == 770:
                ftp.sendcmd('SITE CHMOD 770 ' + file_path_ftp)
                print('Permissão 770 alterada com sucesso...')
                
            elif permission == '777' or permission == 777:
                ftp.sendcmd('SITE CHMOD 777 ' + file_path_ftp)
                print('Permissão 777 alterada com sucesso...')
            
            else:
                if force_permission:
                    print('Permissão não reconhecida...')
                else:
                    print('Permissão não reconhecida...\nNão haverá mudança forçada, para isso ative o parâmetro force_permission')
                
        except ftplib.error_perm as e:
            e = str(e)
            if 'No such file or directory' in e:
                print(f'Diretório ou arquivo não encontrado no servidor -> {file_path_ftp}')