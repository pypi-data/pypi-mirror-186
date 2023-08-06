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

class HtmlToPdf:    
    def __init__(self, file_pdf: str, code_html: str, dir_exit: str='output', headless: bool=True, prints: bool=False, create_driver: bool=True) -> None:
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

        else:
            print('Envie, uma string como caminho do parâmetro file_pdf')
            
        # --- CHROME OPTIONS --- #
        self._options = ChromeOptions()
        
        # --- PATH BASE DIR --- #
        self.CODE_HTML = code_html
        
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
            self.DRIVER.get('https://www.i2pdf.com/pt/html-to-pdf')
            
            with open('file_html.html', 'w', encoding='utf-8') as f:
                f.write(self.CODE_HTML)
            
            
            if prints:
                print('Enviando arquivo...')

            self.DRIVER.find_element(By.CSS_SELECTOR, 'input[type="file"][name="customFileInput"]').send_keys(os.path.abspath('file_html.html'))
            sleep(2)
        

            espera_elemento_disponivel_e_clica(self.WDW30, (By.CSS_SELECTOR, 'button[class="html_to_pdf btn btn-primary glow mr-1 "]'))

            espera_elemento_disponivel_e_clica(self.WDW60, (By.CSS_SELECTOR, 'a[href*="file"]'))
            verifica_se_baixou_o_arquivo(self.__DOWNLOAD_DIR, '.pdf')
            
            files = arquivos_com_caminho_absoluto_do_arquivo(self.__DOWNLOAD_DIR)
            file = files[0]
            os.replace(file, self.FILE_PDF)
            os.remove('file_html.html')
            
            if prints:
                print('Conversão finalizada!')

        except Exception as e:
            print('Ocorreu um erro!')
            faz_log('', 'c*')
            faz_log(self.DRIVER.page_source, 'i*')
            faz_log(self.DRIVER.get_screenshot_as_base64(), 'i*')
            print(str(e))
