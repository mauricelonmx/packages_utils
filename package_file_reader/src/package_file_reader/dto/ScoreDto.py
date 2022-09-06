from package_file_reader.src.package_file_reader.dto.IHeadLine import IHeadLine

class ScoreDto(IHeadLine):
    """Class ScoreDto to handle all parameters for Score entity, asociated with indicadores
    Conventions xml:
           folioConsultaOtorgante -> granting_dossier
           claveOtorgante -> granting_key
           expedienteEncontrado -> file_found
           folioConsulta -> sheet_found
           nombreScore -> nameScore
           codigo -> code
           valor -> value
           razon1 -> razon1
           razon2 -> razon2
           razon3 -> razon3
           razon4 -> razon4
           error  -> error
           indicadores -> indicators        
    """    



    def __init__(self , granting_dossier : str, granting_key: str, file_found:str, 
                sheet_found: str, name_score: str, code: int, value: int, razon1 : str, razon2:str, 
                razon3:str, razon4:str , error:str, indicators: None) -> None:
        
        self.granting_dossier = granting_dossier
        self.granting_key = granting_key 
        self.file_found = file_found
        self.sheet_found = sheet_found
        self.name_score = name_score
        self.code = code
        self.value = value
        self.razon1 = razon1 
        self.razon2 = razon2
        self.razon3 =razon3
        self.razon4 =razon4
        self.error = error
        self.indicators = indicators         
    
        
     
       
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
     
    
    def get_name_score(self):
        """Method to get infortmacion about name_score
       Returns:
            str: return a value of name_score
        """      
        return self.name_score
    
    
    def get_code(self):
        """Method to get infortmacion about code
       Returns:
            str: return a value of code
        """      
        return self.code
   
    
    def get_value(self):
        """Method to get infortmacion about value
       Returns:
            str: return a value of value
        """      
        return self.value
          
    
    def get_razon1(self):
        """Method to get infortmacion about razon1
       Returns:
            str: return a value of razon1
        """      
        return self.razon1
    
       
    def get_razon2(self):
        """Method to get infortmacion about razon2
       Returns:
            str: return a value of razon2
        """      
        return self.razon2
       
       
    def get_razon3(self):
        """Method to get infortmacion about razon3
       Returns:
            str: return a value of razon3
        """      
        return self.razon3
       
       
    def get_razon4(self):
        """Method to get infortmacion about razon4
       Returns:
            str: return a value of razon4
        """      
        return self.razon4
       
       
    def get_error(self):
        """Method to get infortmacion about error
       Returns:
            str: return a value of error
        """      
        return self.error
       
    
    def get_indicators(self):
        """Method to get infortmacion about indicators
       Returns:
            str: return a value of indicators
        """      
        return self.indicators
 