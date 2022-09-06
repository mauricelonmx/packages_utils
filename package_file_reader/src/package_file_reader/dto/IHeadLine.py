import abc

class IHeadLine(metaclass=abc.ABCMeta):
    """Interface IHeadLineDto using __subclasshook__
    Conventions xml:
           folioConsultaOtorgante -> granting_dossier
           claveOtorgante -> granting_key
           expedienteEncontrado -> file_found
           folioConsulta -> sheet_found
    """    
       
    @abc.abstractmethod
    def get_granting_dossier(self):
        pass
    
    @abc.abstractmethod
    def get_granting_key(self):
        pass
    
    @abc.abstractmethod
    def get_file_found(self):
        pass
    
    @abc.abstractmethod
    def get_sheet_found(self):
        pass   