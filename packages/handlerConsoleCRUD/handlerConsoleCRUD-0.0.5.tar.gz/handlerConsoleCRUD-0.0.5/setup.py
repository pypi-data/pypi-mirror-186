import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

VERSION = '0.0.5' #Muy importante, deberéis ir cambiando la versión de vuestra librería según incluyáis nuevas funcionalidades
PACKAGE_NAME = 'handlerConsoleCRUD' #Debe coincidir con el nombre de la carpeta 
AUTHOR = 'Carlos Soto De Dios' 
AUTHOR_EMAIL = '1106419@est.intec.edu.do' 
URL = 'https://github.com/EstCarlos' 

LICENSE = 'MIT' #Tipo de licencia
DESCRIPTION = 'Librería QUE TE PERMITE DEFINIR LOS CAMPOS DE TU CRUD ' #Descripción corta
LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding='utf-8') #Referencia al documento README con una descripción más elaborada
LONG_DESC_TYPE = "text/markdown"


setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    license=LICENSE,
    packages=find_packages(),
    include_package_data=True
)