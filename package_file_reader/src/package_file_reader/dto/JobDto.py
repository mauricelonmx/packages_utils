from package_file_reader.src.package_file_reader.dto.IHeadLine import IHeadLine

class JobDto(IHeadLine):
    """Class AddressDto to handle all parameters for Address entity, associated with Person
       Conventions xml:
       folioConsultaOtorgante -> granting_dossier
       claveOtorgante -> granting_key
       expedienteEncontrado -> file_found
       folioConsulta -> sheet_found
       nombreEmpresa -> company_name
       direccion -> company_address
       coloniaPoblacional -> colony
       delegacionMunicipio -> delegation
       ciudad -> city
       estado -> state
       CP  -> postal_code
       numeroTelefonico -> phone
       extension -> extension
       fax -> fax
       puesto -> position
       fechaContratacion -> date_hiring
       claveMoneda -> currency
       salariomensual -> fixed_salary
       fechaUltimoDiaEmpleo -> last_date_hiring
       fechaVerificacionEmpleo -> verification_date_hiring
       """    
 
    def __init__(self , granting_dossier : str, granting_key: str, file_found:str,  sheet_found: str, 
                 company_name : str, company_address : str,  colony : str, delegation : str,
                 city : str, state : str, postal_code : int, phone : int,
                 extension : int, fax : int, position : str, date_hiring: str,
                 currency : str, fixed_salary : int, last_date_hiring: str, verification_date_hiring: str) -> None :
        
        self.granting_dossier = granting_dossier 
        self.granting_key =granting_key
        self.file_found =file_found
        self.sheet_found = sheet_found  
        self.company_name = company_name
        self.company_address = company_address
        self.colony = colony
        self.delegation=delegation
        self.city = city
        self.state =state
        self.postal_code =postal_code
        self.phone = phone
        self.extension = extension
        self.fax = fax
        self.position = position
        self.date_hiring = date_hiring
        self.currency =currency
        self.fixed_salary = fixed_salary
        self.last_date_hiring =last_date_hiring
        self.verification_date_hiring = verification_date_hiring
    
        
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

   
      ###################
    def get_company_name(self):
        """Method to get infortmacion about company_name
        Returns:
            str: return a value of company_name
        """      
        return self.company_name    
  
    def get_company_address(self):
        """Method to get infortmacion about company_address
        Returns:
            str: return a value of company_address
        """      
        return self.company_address    
  
    def get_colony(self):
        """Method to get infortmacion about colony
        Returns:
            str: return a value of colony
        """      
        return self.company_address    
  
    
    def get_delegation(self):
        """Method to get infortmacion about delegation
        Returns:
            str: return a value of delegation
        """      
        return self.delegation    
  
    
    def get_city(self):
        """Method to get infortmacion about city
        Returns:
            str: return a value of city
        """      
        return self.city    
  
    
    def get_state(self):
        """Method to get infortmacion about state
        Returns:
            str: return a value of state
        """      
        return self.state    
  
  
    def get_postal_code(self):
        """Method to get infortmacion about postal_code
        Returns:
            str: return a value of postal_code
        """      
        return self.postal_code    
  
        
    def get_phone(self):
        """Method to get infortmacion about phone
        Returns:
            str: return a value of phone
        """      
        return self.phone    
      
    
    def get_extension(self):
        """Method to get infortmacion about extension
        Returns:
            str: return a value of extension
        """      
        return self.extension    
        
    
    def get_fax(self):
        """Method to get infortmacion about fax
        Returns:
            str: return a value of fax
        """      
        return self.fax    
    
    
    def get_position(self):
        """Method to get infortmacion about position
        Returns:
            str: return a value of position
        """      
        return self.position    

       
    def get_date_hiring(self):
        """Method to get infortmacion about date_hiring
        Returns:
            str: return a value of date_hiring
        """      
        return self.date_hiring    
   

    def get_currency(self):
        """Method to get infortmacion about currency
        Returns:
            str: return a value of currency
        """      
        return self.currency    


    def get_fixed_salary(self):
        """Method to get infortmacion about fixed_salary
        Returns:
            str: return a value of fixed_salary
        """      
        return self.fixed_salary    

    
    def get_last_date_hiring(self):
        """Method to get infortmacion about last_date_hiring
        Returns:
            str: return a value of last_date_hiring
        """      
        return self.last_date_hiring    

        
    def get_verification_date_hiring(self):
        """Method to get infortmacion about verification_date_hiring
        Returns:
            str: return a value of verification_date_hiring
        """      
        return self.verification_date_hiring    
    
     
    def __str__(self) -> str:
        return super().__dict__
        
        
        
        
        
        
        
        
