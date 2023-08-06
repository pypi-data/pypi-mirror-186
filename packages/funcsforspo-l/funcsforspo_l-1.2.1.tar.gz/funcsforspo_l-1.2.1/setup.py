import os
from setuptools import setup

version = '1.2.1'

with open("README.md", "r", encoding='utf-8') as fh:
    readme = fh.read()
    setup(
        name='funcsforspo_l',
        version=version,
        url='https://github.com/githubpaycon/funcsforspo_l',
        license='MIT License',
        author='Gabriel Lopes de Souza',
        long_description=readme,
        long_description_content_type="text/markdown",
        author_email='githubpaycon@gmail.com',
        keywords='Funções Para Melhorar Desenvolvimento de Robôs com Selenium - Linux',
        description=u'Funções Para Melhorar Desenvolvimento de Robôs com Selenium - Linux',
        
        packages= [
            os.path.join('funcsforspo_l', 'femails'),
            os.path.join('funcsforspo_l', 'fexceptions'),
            os.path.join('funcsforspo_l', 'fftp'),
            os.path.join('funcsforspo_l', 'fpdf'),
            os.path.join('funcsforspo_l', 'fpdf', 'focr'),
            os.path.join('funcsforspo_l', 'fpdf', 'fcompress'),
            os.path.join('funcsforspo_l', 'fpdf', 'fimgpdf'),
            os.path.join('funcsforspo_l', 'fpdf', 'fhtml_to_pdf'),
            os.path.join('funcsforspo_l', 'fopenpyxl'),
            os.path.join('funcsforspo_l', 'fpysimplegui'),
            os.path.join('funcsforspo_l', 'fpython'),
            os.path.join('funcsforspo_l', 'fpython'),
            os.path.join('funcsforspo_l', 'fregex'),
            os.path.join('funcsforspo_l', 'fselenium'),
            os.path.join('funcsforspo_l', 'fsqlite'),
        ],
        
        install_requires= [
            'selenium',
            'bs4',
            'requests',
            'html5lib',
            'openpyxl',
            'webdriver-manager',
            'requests',
            'pretty_html_table',
            'PySimpleGUI',
            'wget',
            'rich==12.6.0',
        ],
        )
