"""
DIREITOS RESERVADOS / RIGHTS RESERVED / DERECHOS RESERVADOS

https://www.ilovepdf.com/compress_pdf

Esse robô envia o PDF para o site https://www.ilovepdf.com/compress_pdf
    e faz a compressão do arquivo PDF
    

"""
from __future__ import annotations
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from funcsforspo_l.fpython.functions_for_py import *
from funcsforspo_l.fselenium.functions_selenium import *
from funcsforspo_l.fexceptions.exceptions import FalhaAoRecuperarOcr, NivelDeCompressaoNaoPreenchido
import json
import os

class CompressPDF:    
    def __init__(self, file_pdf: str, compress_level: int=1, dir_exit: str='output', headless: bool=True, prints: bool=False, create_driver: bool=True) -> None:
        """Init

        Args:
            file_pdf (str): Caminho do arquivo
            dir_exit (str, optional): Local de saída do arquivo .PDF. Defaults to 'output'.
            compress_level (bool, optional): Nível de compressão. Defaults to 1.
            headless (bool, optional): executa como headless. Defaults to True.
            prints (bool, optional): Mostra os prints durante o processo
            create_driver (bool, optional): Cria um WebDriver. Defaults to True.
            
        Use:
            compress_level
                1- LESS COMPRESSION
                2- RECOMMENDED COMPRESSION
                3- EXTREME COMPRESSION
        """
        
        if isinstance(headless, (bool, int)):
            self.HEADLESS = headless
        else:
            print('Adicione True ou False para Headless')
        
        if isinstance(file_pdf, str):

            self.FILE_PDF = os.path.abspath(file_pdf)
            
            if prints:
                print(f'O tamanho do arquivo atual é: {convert_bytes(os.path.getsize(self.FILE_PDF))}')
                
            self.CONVERTER_VARIOS_ARQUIVOS = False
            self.MESCLAR_EM_UMA_LINHA = False
        else:
            print('Envie, uma string como caminho do parâmetro file_pdf')
            
        # --- CHROME OPTIONS --- #
        self._options = ChromeOptions()
        
        # --- PATH BASE DIR --- #
        self.COMPRESS_LEVEL = compress_level
        
        self.__DOWNLOAD_DIR =  cria_dir_no_dir_de_trabalho_atual(dir=dir_exit, print_value=False, criar_diretorio=True)
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
                "safebrowsing.enabled": True}
            
        self._options.add_experimental_option('prefs', self._PROFILE)
        
        self._options.add_experimental_option("excludeSwitches", ["enable-logging"])
        if self.HEADLESS:
            self._options.add_argument('--headless')
            
        # self._options.add_argument("--disable-web-security")
        # self._options.add_argument("--allow-running-insecure-content")
        # self._options.add_argument("--disable-extensions")
        # self._options.add_argument("--start-maximized")
        # self._options.add_argument("--no-sandbox")
        # self._options.add_argument("--disable-setuid-sandbox")
        # self._options.add_argument("--disable-infobars")
        # self._options.add_argument("--disable-webgl")
        # self._options.add_argument("--disable-popup-blocking")
        # self._options.add_argument('--disable-gpu')
        # self._options.add_argument('--disable-software-rasterizer')
        # self._options.add_argument('--no-proxy-server')
        # self._options.add_argument("--proxy-server='direct://'")
        # self._options.add_argument('--proxy-bypass-list=*')
        # self._options.add_argument('--disable-dev-shm-usage')
        # self._options.add_argument('--block-new-web-contents')
        # self._options.add_argument('--incognito')
        # self._options.add_argument('–disable-notifications')
        # self._options.add_argument('--suppress-message-center-popups')
        self._options.add_argument("--window-size=1920,1080")
        
        if create_driver:
            self.__service = Service(executable_path=ChromeDriverManager().install())
            self.DRIVER = Chrome(service=self.__service, options=self._options)
        else:
            self.DRIVER = Chrome(options=self._options)

        # - WebDriverWaits - #
        self.WDW3 = WebDriverWait(self.DRIVER, timeout=3)
        self.WDW7 = WebDriverWait(self.DRIVER, timeout=7)
        self.WDW30 = WebDriverWait(self.DRIVER, timeout=30)
        self.WDW60 = WebDriverWait(self.DRIVER, timeout=60)
        self.WDW180 = WebDriverWait(self.DRIVER, timeout=180)
        self.DRIVER.maximize_window()
    
    
        try:
            if prints:
                print('Acessando o site...')
            self.DRIVER.get('https://www.ilovepdf.com/compress_pdf')
            
            if prints:
                print('Enviando arquivo...')

            # Espera pelo elemento de enviar o arquivo
            espera_elemento(self.WDW3, (By.CSS_SELECTOR, '#uploader'))

            # Envia o arquivo
            sleep(2)
            self.DRIVER.find_element(By.CSS_SELECTOR, 'input[type="file"]').send_keys(self.FILE_PDF)
                
            if prints:
                print('Escolhendo o nível de compressão...')
            
            
            if self.COMPRESS_LEVEL == 1:
                espera_elemento_disponivel_e_clica(self.WDW30, (By.CSS_SELECTOR, 'li[data-value="low"]'))
            elif self.COMPRESS_LEVEL == 2:
                espera_elemento_disponivel_e_clica(self.WDW30, (By.CSS_SELECTOR, 'li[data-value="recommended"]'))
            elif self.COMPRESS_LEVEL == 3:
                espera_elemento_disponivel_e_clica(self.WDW30, (By.CSS_SELECTOR, 'li[data-value="extreme"]'))
            else:
                raise NivelDeCompressaoNaoPreenchido


            if prints:
                print('Clicando em Comprimir...')
            espera_elemento_disponivel_e_clica(self.WDW30, (By.CSS_SELECTOR, '#processTask'))

            verifica_se_baixou_o_arquivo(self.__DOWNLOAD_DIR, '.pdf')
            
            files = arquivos_com_caminho_absoluto_do_arquivo(self.__DOWNLOAD_DIR)
            
            if prints:
                print(f'O tamanho do arquivo FINAL é: {convert_bytes(os.path.getsize(files[-1]))}')

            
            if prints:
                print('Compressão finalizada!')

        except Exception as e:
            print('Ocorreu um erro!')
            faz_log('', 'c*')
            faz_log(self.DRIVER.page_source, 'i*')
            faz_log(self.DRIVER.get_screenshot_as_base64(), 'i*')
            print(str(e))
