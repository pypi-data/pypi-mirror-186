"""
DIREITOS RESERVADOS / RIGHTS RESERVED / DERECHOS RESERVADOS

https://www.ilovepdf.com/pt/jpg_para_pdf

Esse robô envia as imagens para o site https://www.ilovepdf.com/pt/jpg_para_pdf
    e faz a conversão para um arquivo PDF
    

"""
from __future__ import annotations
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from funcsforspo_l.fpython.functions_for_py import limpa_diretorio, arquivos_com_caminho_absoluto_do_arquivo
from funcsforspo_l.fselenium.functions_selenium import cria_dir_no_dir_de_trabalho_atual, espera_elemento, sleep, espera_elemento_disponivel_e_clica,faz_log,verifica_se_baixou_o_arquivo
from funcsforspo_l.fexceptions.exceptions import ErroNoConversorException, ErroNoConversorImagesException
import json
import os


class __ConvertImgToPdf:    
    def __init__(self, images_path: list[str]|str, pdf_name:str='Ilovepdf.pdf', retrat: bool=True, margin: str='NoMargin', output_dir: str='output', headless: bool=True, prints: bool=False, create_driver: bool=True) -> None:
        """
        ## DIREITOS RESERVADOS / RIGHTS RESERVED / DERECHOS RESERVADOS

        ### https://www.ilovepdf.com/pt/jpg_para_pdf
        
        ## Faz a conversão de Imagens para um único pdf. 
        
        ### Só é possível enviar até 20 imagens para o pdf, caso contrário, será necessário acessar o IlovePDF manualmente e converter com sua conta premium

        Args:
            images_path (list[str] | str): Imagens com caminhos relativos, até vinte (20)
            pdf_name (str, optional): Nome do documento com .pdf no final. Defaults to 'Ilovepdf.pdf'.
            retrat (bool, optional): Se deseja em formato retrato ou não. Defaults to True.
            margin (str, optional): Se deseja adicioanar margem, nomargin para deixar sem margem, low para pequena margem e big para grande margem. Defaults to 'NoMargin'.
            output_dir (str, optional): diretório de saída do arquivo. Defaults to 'output'.
            headless (bool, optional): se deseja executar com o navegador aberto ou não. Defaults to True.
            prints (bool, optional): se deseja ver as saídas de execução. Defaults to False.
            create_driver (bool, optional): cria o driver. Defaults to True.
        """
        
        
        if isinstance(headless, bool):
            self.HEADLESS = headless
        else:
            raise ErroNoConversorException('Adicione True ou False para "headless"')
        
        if isinstance(pdf_name, str) and ('.pdf' in pdf_name.lower()):
            self.PATH_NAME = pdf_name
        else:
            raise ErroNoConversorException('Adicione o nome do arquivo com .pdf e que seja do tipo str')
        
        try:
            if isinstance(images_path, str):
                self.IMGS = os.path.abspath(images_path)
            elif isinstance(images_path, list):
                if len(images_path) > 20:
                    raise ErroNoConversorImagesException('Não é possível enviar mais que 20 imagens, para isso é necessário o plano premium do IlovePDF')
                self.IMGS = [os.path.abspath(image) for image in images_path]
            else:
                raise ErroNoConversorImagesException('Não é da instância list ou str')
        except Exception:
            raise ErroNoConversorImagesException('Erro ao recuperar o abspath das imagens')
        
        if isinstance(retrat, bool):
            self.RETRATO = True if retrat else False
        else:
            raise ErroNoConversorException('Adicione True ou False para "retrat"')
            
        self.MARGIN = margin
                
        if (self.MARGIN.lower() == 'nomargin') or (self.MARGIN.lower() == 'low') or (self.MARGIN.lower() == 'big'):
            pass
        else:
            raise ErroNoConversorException('Adicione "nomargin" para nenhuma margem, "low" para uma margem pequena ou "big" para margem grande')
            
        
        # --- CHROME OPTIONS --- #
        self._options = ChromeOptions()
        
        # --- PATH BASE DIR --- #
        self.__DOWNLOAD_DIR =  cria_dir_no_dir_de_trabalho_atual(dir=output_dir, print_value=False, criar_diretorio=True)
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
            self.DRIVER.get('https://www.ilovepdf.com/pt/jpg_para_pdf')
            
            # Espera pelo elemento de enviar o arquivo
            espera_elemento(self.WDW3, (By.CSS_SELECTOR, '#uploader'))

            sleep(2)
            
            if prints:
                print('Enviando arquivo(s)...')

            if isinstance(self.IMGS, str):
                self.DRIVER.find_element(By.CSS_SELECTOR, 'input[type="file"]').send_keys(self.IMGS)
            elif isinstance(self.IMGS, list):
                for i in self.IMGS:
                    self.DRIVER.find_element(By.CSS_SELECTOR, 'input[type="file"]').send_keys(i)
            
            if prints:
                print('Escolhendo o retrato...')
            if not self.RETRATO:
                espera_elemento_disponivel_e_clica(self.WDW30, (By.CSS_SELECTOR, 'li[data-name="orientation"][data-value="landscape"]'))
            
            if prints:
                print('Escolhendo a margem...')
            if self.MARGIN.lower() == 'nomargin':
                pass
            elif self.MARGIN.lower() == 'low':
                espera_elemento_disponivel_e_clica(self.WDW30, (By.CSS_SELECTOR, 'li[data-name="margin"][data-value="20"]'))
            elif self.MARGIN.lower() == 'big':
                espera_elemento_disponivel_e_clica(self.WDW30, (By.CSS_SELECTOR, 'li[data-name="margin"][data-value="40"]'))            
            
            if prints:
                print('Clicando em processar...')
            espera_elemento_disponivel_e_clica(self.WDW30, (By.CSS_SELECTOR, '#processTask'))

            if prints:
                print('Esperando o arquivo ser baixado...')

            verifica_se_baixou_o_arquivo(self.__DOWNLOAD_DIR, '.pdf')

            if prints:
                print('Finalizado, download concluido!')
                
            if prints:
                print(f'Alterando o nome do documento para {self.PATH_NAME}...')
            files = arquivos_com_caminho_absoluto_do_arquivo(self.__DOWNLOAD_DIR)
            file_pdf = files[0]
            os.rename(file_pdf, os.path.join(os.path.dirname(file_pdf), self.PATH_NAME))
        except Exception as e:
            print('Ocorreu um erro!')
            faz_log('', 'c*')
            faz_log(self.DRIVER.page_source, 'i*')
            faz_log(self.DRIVER.get_screenshot_as_base64(), 'i*')
            print(str(e))
            
def convert_img_to_pdf(images_path: list[str]|str, pdf_name:str='Ilovepdf.pdf', retrat: bool=True, margin: str='NoMargin', output_dir: str='output', headless: bool=True, prints: bool=False, create_driver: bool=True):
    """
        ## DIREITOS RESERVADOS / RIGHTS RESERVED / DERECHOS RESERVADOS

        ### https://www.ilovepdf.com/pt/jpg_para_pdf
        
        ## Faz a conversão de Imagens para um único pdf. 
        
        ### Só é possível enviar até 20 imagens para o pdf, caso contrário, será necessário acessar o IlovePDF manualmente e converter com sua conta premium

        Args:
            images_path (list[str] | str): Imagens com caminhos relativos, até vinte (20)
            pdf_name (str, optional): Nome do documento com .pdf no final. Defaults to 'Ilovepdf.pdf'.
            retrat (bool, optional): Se deseja em formato retrato ou não. Defaults to True.
            margin (str, optional): Se deseja adicioanar margem, nomargin para deixar sem margem, low para pequena margem e big para grande margem. Defaults to 'NoMargin'.
            output_dir (str, optional): diretório de saída do arquivo. Defaults to 'output'.
            headless (bool, optional): se deseja executar com o navegador aberto ou não. Defaults to True.
            prints (bool, optional): se deseja ver as saídas de execução. Defaults to False.
            create_driver (bool, optional): cria o driver. Defaults to True.
        
    Use:
    >>> convert_img_to_pdf(
    >>> [
    >>>    r'imgs\myimage1 (1).png',
    >>>    r'imgs\myimage2.png',
    >>>    r'imgs\myimage3.png',
    >>>    r'imgs\myimage4.png',
    >>>    r'imgs\myimage5.png',
    >>>    r'imgs\myimage6.png',
    >>>    r'imgs\myimage7.png',
    >>>    r'imgs\myimage8.png',
    >>>    r'imgs\myimage10.png'
    >>> ],
    >>> pdf_name='meupdf.pdf', retrat=True, margin='big', output_dir='exit', headless=True, prints=True, create_driver=True)
    """
    __ConvertImgToPdf(images_path=images_path, pdf_name=pdf_name, retrat=retrat, margin=margin,output_dir=output_dir, headless=headless, prints=prints, create_driver=create_driver)