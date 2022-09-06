from package_file_reader.src.package_file_reader.dto.IHeadLine import IHeadLine

class HeadLineDto(IHeadLine):
    """Class HeadLineDto to handle  HeadLine
    Conventions xml:
           folioConsultaOtorgante -> granting_dossier
           claveOtorgante -> granting_key
           expedienteEncontrado -> file_found
           folioConsulta -> sheet_found
    """    
    def __init__(self , granting_dossier : str, granting_key: str, file_found:str, sheet_found: str) -> None:
        
        self.granting_dossier = granting_dossier
        self.granting_key = granting_key 
        self.file_found = file_found
        self.sheet_found = sheet_found
        
        
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
       