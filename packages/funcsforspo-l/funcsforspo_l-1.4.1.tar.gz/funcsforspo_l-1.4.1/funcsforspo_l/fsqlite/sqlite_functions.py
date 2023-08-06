from __future__ import annotations
from sqlite3 import Cursor, Connection
import sqlite3
import os
import shutil

def deletar_tabela_sqlite(cur, table_name) -> None:
    """Deleta uma tabela específica pelo nome dela

    Args:
        cur (_type_): Cursor SQLite3
        table_name (str): Nome da tabela a ser deletada
    """
    cur.execute(f'''DROP TABLE {table_name}''')
    
def select_all_from_table(cur, table):
    """SELECT * FROM table

    Args:
        cur (Cursor): Cursor do SQLite
        table (Tabela): Tabela do banco de dados
    """
    
    cur.execute('SELECT * FROM ?', (table))
    
def faz_backup_do_banco(path_database: str, dir_backup: str) -> None:
    """Faz backup do banco de dados
    ## Enviar caminho relativo do db

    Args:
        path_database (str): caminho do banco de dados
        dir_backup (str): diretorio do banco de dados
    """
    
    PATH_DATABASE = os.path.abspath(path_database)
    DIR_BACKUP = os.path.abspath(dir_backup)
    PATH_DATABASE_BACKUP = DIR_BACKUP +'\\'+ path_database
    
    if os.path.exists(PATH_DATABASE):
        if os.path.exists(DIR_BACKUP):
            shutil.copy2(PATH_DATABASE, PATH_DATABASE_BACKUP)
        else:
            os.makedirs(DIR_BACKUP)
            shutil.copy2(PATH_DATABASE, PATH_DATABASE_BACKUP)
            

def connect_db(db_file: str) -> Cursor | Connection:
    """Retorna o cursor e a conexão do banco

    Args:
        db_file (str): caminho do banco de dados

    Returns:
        Cursor | Connection: Cursor and Connection SQLite3
    """
    con = sqlite3.connect(os.path.abspath(db_file))
    cur = con.cursor()
    return cur, con