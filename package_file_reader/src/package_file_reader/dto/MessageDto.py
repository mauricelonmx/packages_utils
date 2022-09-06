from package_file_reader.src.package_file_reader.dto.IHeadLine import IHeadLine

class MessageDto(IHeadLine):
    """Class Message to handle all parameters for Message entity
    Conventions xml:
           folioConsultaOtorgante -> granting_dossier
           claveOtorgante -> granting_key
           expedienteEncontrado -> file_found
           folioConsulta -> sheet_found
           tipoMensaje -> type_message
           leyenda -> caption
    """    



    def __init__(self , granting_dossier : str, granting_key: str, file_found:str, 
                sheet_found: str, type_message: int, caption : str) -> None:
        
        self.granting_dossier = granting_dossier
        self.granting_key = granting_key 
        self.file_found = file_found
        self.sheet_found = sheet_found
        self.type_message = type_message
        self.caption = caption
        
     
       
    def get_granting_dossier(self):
        """Method to get infortmacion about granting_dossier
        Returns:
            str: return a value of granting_dossier
        """        
        return self.granting_dossier
     
     
    def get_granting_key(self):
        """Method to get infortmacion about granting_key
        Returns:
            str: return a value of granting_key
        """      
        return self.granting_key
    
    
    def get_file_found(self):
        """Method to get infortmacion about file_found
        Returns:
            str: return a value of file_found
        """      
        return self.file_found
    
    
    def get_sheet_found(self):
        """Method to get infortmacion about sheet_found
       Returns:
            str: return a value of sheet_found
        """      
        return self.sheet_found
     
    
    def get_type_message(self):
        """Method to get infortmacion about type_message
        Returns:
            str: return a value of type_message
        """      
        return self.type_message
     
    
    def get_caption(self):
        """Method to get infortmacion about caption
        Returns:
            str: return a value of leyenda
        """        
        return self.caption
    
       