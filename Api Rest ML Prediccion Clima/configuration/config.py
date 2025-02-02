###############################################################################################################
################################ Meatadata Footbar Description ################################################
__author__ = "Jorge Cardona"
__copyright__ = "Copyright 2020, Machine Learning Projects"
__credits__ = "Jorge Cardona"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Jorge Cardona"
__email__ = "https://github.com/JorgeCardona"
__status__ = "Production"
###############################################################################################################
###############################################################################################################

import pathlib
import os
os.chdir('..')

# directorios donde se guarda la informacion de la API
ROOT_DIRECTORY = str(pathlib.Path(__file__).parent.absolute()) 
FILES_DIRECTORY = ROOT_DIRECTORY + '/modelos'
MODLES_DIRECTORY = ROOT_DIRECTORY + '/modelos entrenados'
MAX_CONTENT_LENGTH  = 16 * 1024 * 1024

# son los clasificadores que se van a usar en el analisis
CLASIFICADORES2    = ['DT','LR']  

CLASIFICADORES    = ['MLP','GB','NB','KNN','RF','DT','LR']  
ARCHIVOS_PERMITIDOS = set(['csv', 'xlsx', 'xls'])

# credenciales de la base de datos
URL_CONEXION     = "mongodb://localhost:27017/"
NOMBRE_BD        = 'db'
NOMBRE_COLECCION = 'clima'    
NOMBRE_COLECCION_CLASIFICADOR = 'mejor_clasificador'
NOMBRE_COLECCION_PREDICCION = 'datos_prediccion'

# configuraciones de los modelos
CANTIDAD_DE_VALIDACIONES = 10
PORCENTAJE_ENTRENAMIENTO = 0.3
PRECISION = 2
LIMITE_BINARIZACION = 24.99
NOMBRE_COLUMNA_BINARIZADA = 'HumedadBinarizadaPrediccion'
COLUMNA_DECISION = 'relative_humidity_3pm' 
TOTAL_DIMENSIONES_PCA = 7


print('ROOT_DIRECTORY', ROOT_DIRECTORY)
print('FILES_DIRECTORY', FILES_DIRECTORY)
print('MODLES_DIRECTORY', MODLES_DIRECTORY)