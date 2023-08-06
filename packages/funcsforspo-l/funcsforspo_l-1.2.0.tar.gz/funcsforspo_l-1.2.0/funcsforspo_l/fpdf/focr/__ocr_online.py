"""
DIREITOS RESERVADOS / RIGHTS RESERVED / DERECHOS RESERVADOS

https://online2pdf.com/pt/converter-pdf-para-txt-com-ocr

Esse robô envia o PDF para o site https://online2pdf.com/pt/converter-pdf-para-txt-com-ocr
    e recupera um arquivo txt com o ocr
    

"""
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from funcsforspo_l.fpython.functions_for_py import *
from funcsforspo_l.fselenium.functions_selenium import *
from funcsforspo_l.fexceptions.exceptions import FalhaAoRecuperarOcr
import json
import os

class GetTextPDF:    
    def __init__(self, file_pdf: str, dir_exit: str='output', get_text_into_code: bool=True, headless: bool=True, prints: bool=False, create_driver: bool=True) -> str:
        """Init

        Args:
            file_pdf (str): Caminho do arquivo
            dir_exit (str, optional): Local de saída do arquivo TXT. Defaults to 'output'.
            headless (bool, optional): executa como headless. Defaults to True.
            get_text_into_code (bool, optional): Retorna o texto do pdf no código. Defaults to True.
            create_driver (bool, optional): Cria um driver. Defaults to True.
        """
        if isinstance(headless, (bool, int)):
            self.HEADLESS = headless
        else:
            print('Adicione True ou False para Headless')
        
        if isinstance(file_pdf, str):
            self.FILE_PDF = os.path.abspath(file_pdf)
            self.CONVERTER_VARIOS_ARQUIVOS = False
            self.MESCLAR_EM_UMA_LINHA = False
        else:
            print('Envie, uma string como caminho do parâmetro file_pdf')
            
        # --- CHROME OPTIONS --- #
        self._options = ChromeOptions()
        
        # --- PATH BASE DIR --- #
        self.get_text_into_code = get_text_into_code
        
        if get_text_into_code:
            self.__DOWNLOAD_DIR = cria_dir_no_dir_de_trabalho_atual('tempdir')
        else:
            self.__DOWNLOAD_DIR =  cria_dir_no_dir_de_trabalho_atual(dir=dir_exit, print_value=False, criar_diretorio=True)
            
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
        self._options.add_argument('--suppress-message-center-popups')
        
        if create_driver:
            self.__service = Service(executable_path=ChromeDriverManager().install())
            self.DRIVER = Chrome(service=self.__service, options=self._options)
        else:
            self.DRIVER = Chrome(options=self._options)

        # - WebDriverWaits - #
        self.WDW3 = WebDriverWait(self.DRIVER, timeout=3)
        self.WDW30 = WebDriverWait(self.DRIVER, timeout=30)
        self.WDW60 = WebDriverWait(self.DRIVER, timeout=60)
        self.WDW180 = WebDriverWait(self.DRIVER, timeout=180)
        self.DRIVER.maximize_window()
    
    
        try:
            if prints:
                print('Acessando o site...')
            self.DRIVER.get('https://online2pdf.com/pt/converter-pdf-para-txt-com-ocr')
            
            if prints:
                print('Convertendo arquivo...')

            # Espera pelo elemento de enviar o arquivo
            self.WDW3.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#input_file0')))

            # Envia o arquivo
            self.DRIVER.find_element(By.CSS_SELECTOR, '#input_file0').send_keys(self.FILE_PDF)
                
            # Clica em OCR Profundo
            espera_elemento_disponivel_e_clica(self.WDW3, (By.CSS_SELECTOR, '#export_fullocr_box > label'))

            # Clica em Converter
            espera_elemento_disponivel_e_clica(self.WDW3, (By.CSS_SELECTOR, 'button[class="convert_button"]'))

            if prints:
                print('Carregando, por favor espere, essa parte deve demorar um pouco...')
            
            # espera o elemento de completo
            espera_elemento(self.WDW180, (By.CSS_SELECTOR, '#completed_window'))

            def verifica_se_baixou(path_dir):
                """Verifica se baixou algum arquivo na pasta
                Args:
                    path_dir (str): path do diretório
                """
                wait = True
                while(wait):
                    path_dir_abs = os.path.abspath(path_dir)
                    for fname in os.listdir(path_dir_abs):
                        if '.crdownload' in fname or len(os.listdir(path_dir_abs)) == 0:
                            continue
                        else:
                            wait=False
                            sleep(3)
                            if prints:
                                print('OCR Concluido!')
            verifica_se_baixou(self.__DOWNLOAD_DIR)            
        except Exception as e:
            print('Ocorreu um erro!')
            print(str(e))
            

            
    def recupera_texto(self) -> str:
        if self.get_text_into_code:
            try:
                file_txts = arquivos_com_caminho_absoluto_do_arquivo(self.__DOWNLOAD_DIR)
                file_txt = file_txts[-1]
                text = None
                with open(file_txt, mode='r', encoding='utf-16-le') as f:
                    text = f.read()
                shutil.rmtree(self.__DOWNLOAD_DIR)
                return text
            except IndexError:
                raise FalhaAoRecuperarOcr('Ocorreu um erro na recuperação que causou um IndexError, provavelmente não baixou o arquivo.')