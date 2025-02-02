############################################################################################
################################ Descripcion################################################
__author__ = "Jorge Cardona"
__copyright__ = "Copyright 2020, MACHINE LEARNING PROJECT"
__credits__ = "Jorge Cardona"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Jorge cardona "
__email__ = "https://github.com/JorgeCardona"
__status__ = "Production"
###############################################################################################
###############################################################################################
from CONFIGURATION.config import ALLOWED_SAVE_SERVICES, ALLOWED_EXTENTION_FILES, UPLOAD_FILES_DIRECTORY

from VALIDATIONS_AND_EXCEPTIONS.exceptions import Exceptions
from UTILS.save_files import Save
from flask import request
from CONFIGURATION.config import DATA_BASES_TYPES

class Validator(object):   

    def validate_upload_file(self, database_name:str, request:request):

        # obtiene la informacion de la base de datos solicitada
        database_type = self.allowed_databases(database_name)

        # valida si la base de datos es permitida en la aplicacion
        if(not database_type):
            
            # lanza la excepcion debido al fallo
            return [Exceptions().obtain_message(400.0), '', '']

        # obtiene el nombre de la key enviaada en la peticion
        key_name_service   = self.allowed_services(list(request.files))
 
        # valida que exista una key de servicio permitida 
        if(not key_name_service):
            
            # lanza la excepcion debido al fallo
            return [Exceptions().obtain_message(400.1), '', '']

        # obtiene la informacion del archivo adjuntado
        file_info = request.files[key_name_service]

        # obtiene el nombre del fichero adjuntado
        file_name  = file_info.filename if file_info else file_info

        # valida que se adjunto un archivo
        if (not file_name):

            # lanza la excepcion debido al fallo
            return [Exceptions().obtain_message(400.2),'','']

        # valida si la extension del archivo es valida para la carga de datos
        file_allowed = self.allowed_file(file_name)
        
        # valida que la extension del archivo cargado sea compatible con la plataforma
        if (not file_allowed):

            # lanza la excepcion debido al fallo
            return [Exceptions().obtain_message(74),'','']

        # retorna los valores obtenidos del archivo y la peticion del servicio
        return key_name_service, file_info, file_name

    # validqa que el nombre de la key enviada en la solicitud corresponda a ALLOWED_SAVE_SERVICES para guardar los datos
    def allowed_services(self, filename: list):

        # retorna el nombre de la key que se le puso al archivo al realizar  la peticion, si la key es valida
        return filename[0] if len(filename) > 0 and filename[0].upper() in ALLOWED_SAVE_SERVICES else []

    # valida que el archivo cuente con las extensiones permitidas
    def allowed_file(self, filename: str):
	    return '.' in filename and filename.rsplit('.', 1)[1].upper() in ALLOWED_EXTENTION_FILES


    # valida que la tecnologia de base de datos sea compatible con la aplicacion
    def allowed_databases(self, database_name: str):

        # retorna el valor del nombre de la abse de datos seleccionada
        return database_name.upper() if database_name != None and str(database_name.upper()) in DATA_BASES_TYPES else []