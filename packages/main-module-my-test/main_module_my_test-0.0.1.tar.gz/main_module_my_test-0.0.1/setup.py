# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 22:01:43 2023

@author: Hernan_Lab
"""
from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Mi primer paquete de Python'
LONG_DESCRIPTION = 'Mi primer paquete de Python con una descripción ligeramente más larga'


# Configurando
setup(
       # el nombre debe coincidir con el nombre de la carpeta 	  
       #'modulomuysimple'
        name="main_module_my_test", 
        version=VERSION,
        author="Hernan Hernandez",
        author_email="<test@email.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # añade cualquier paquete adicional que debe ser
        #instalado junto con tu paquete. Ej: 'caer'
        
        keywords=['python', 'primer paquete'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)