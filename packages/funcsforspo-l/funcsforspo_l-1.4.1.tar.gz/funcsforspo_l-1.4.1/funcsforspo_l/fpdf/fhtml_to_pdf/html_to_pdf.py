"""
DIREITOS RESERVADOS / RIGHTS RESERVED / DERECHOS RESERVADOS

https://www.ilovepdf.com/compress_pdf

Esse robô envia o PDF para o site https://www.ilovepdf.com/compress_pdf e faz a compressão do arquivo PDF
        
"""
from __future__ import annotations
from funcsforspo_l.fpdf.fhtml_to_pdf.__html_to_pdf import HtmlToPdf

def comprimir_pdf(file_pdf: str, code_html: str, dir_exit: str='output', headless: bool=True, prints: bool=False, create_driver: bool=True) -> None:
    """Comprimir seu PDF
    
    DIREITOS RESERVADOS / RIGHTS RESERVED / DERECHOS RESERVADOS

    https://www.ilovepdf.com/compress_pdf

    Esse robô envia o PDF para o site https://www.ilovepdf.com/compress_pdf e faz a compressão do arquivo PDF

    Args:
        file_pdf (str): Seu arquivo PDF
        compress_level (int, optional): Nível de Compressão do PDF. Defaults to 1.
        dir_exit (str, optional): Diretório de Saída. Defaults to 'output'.
        headless (bool, optional): Headless. Defaults to True.
        prints (bool, optional): Print andamento da compressão. Defaults to False.
        create_driver (bool, optional): Cria WebDriver. Defaults to True.
        
        
    Use:
        >>> from FuncsForSPO.fpdf.fcompress.compress import comprimir_pdf
        
        >>> comprimir_pdf('meupdf.pdf', 1)
        or
        >>> comprimir_pdf('meupdf.pdf', 2)
        or
        >>> comprimir_pdf('meupdf.pdf', 3)
    """
    
    HtmlToPdf(file_pdf=file_pdf, code_html=code_html, dir_exit=dir_exit, headless=headless, prints=prints, create_driver=create_driver)
