from package_file_reader.src.package_file_reader.dto.IHeadLine import IHeadLine

class IndicatorDto(IHeadLine):
    """Class IndicatorDto to handle all parameters for Indicator entity, associated with ScoreDto
    Conventions xml:
           folioConsultaOtorgante -> granting_dossier
           claveOtorgante -> granting_key
           expedienteEncontrado -> file_found
           folioConsulta -> sheet_found
           descriptionInd -> description_ind
           valorInd -> value_ind
    """    



    def __init__(self , granting_dossier : str, granting_key: str, file_found:str, 
                sheet_found: str, description_ind : str, value_ind: int) -> None:
        
        self.granting_dossier = granting_dossier
        self.granting_key = granting_key 
        self.file_found = file_found
        self.sheet_found = sheet_found
        self.description_ind = description_ind,
        self.value_ind = value_ind
        
     
       
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
     
    
    def get_description_ind(self):
        """Method to get infortmacion about description_ind
        Returns:
            str: return a value of description_ind
        """        
        return self.description_ind
    
    
    
    def get_value_ind(self):
        """Method to get infortmacion about value_ind
        Returns:
            str: return a value of value_ind
        """        
        return self.value_ind
       
