from package_file_reader.src.package_file_reader.dto.IHeadLine import IHeadLine

class NameDto(IHeadLine):
    """Class NameDto to handle all parameters for Name entity, asociated with Person
    Conventions xml:
           folioConsultaOtorgante -> granting_dossier
           claveOtorgante -> granting_key
           expedienteEncontrado -> file_found
           folioConsulta -> sheet_found
           ApellidoPaterno -> first_last_name
           ApellidoMaterno -> second_last_name
           ApellidoAdicional -> last_name_aditional
           Nombres -> name
           FechaNacimiento -> date_of_birth
           RFC -> rfc
           CURP -> curp
           Numero de seguridad Social -> security_social_number
            Nacionalidad -> citizenship
            Residencia -> residence
            EstadoCivil -> marital_status 
            Sexo -> genre
            ClaveElectorIFE -> key_electotal_ife
            NumeroDependientes -> dependants_number
            FechaDefuncion   -> decease_date     
    """    

    def __init__(self , granting_dossier : str, granting_key: str, file_found:str,      
                sheet_found: str, first_last_name: str,
                second_last_name : str, aditional_last_name : str,
                name : str, date_of_birth :str, rfc : str, curp : str, security_social_number: int,
                citizenship : str, residence :int, marital_status : str, genre : str,
                key_electotal_ife : str, dependants_number : int, decease_date: str
                ) -> None:
        
                self.granting_dossier = granting_dossier 
                self.granting_key = granting_key
                self.file_found = file_found      
                self.sheet_found = sheet_found  
                self.first_last_name= first_last_name
                self.second_last_name =second_last_name
                self.aditional_last_name = aditional_last_name
                self.name = name 
                self.date_of_birth= date_of_birth
                self.rfc =rfc
                self.curp = curp
                self.security_social_number=security_social_number
                self.citizenship =citizenship
                self.residence =residence
                self.marital_status =marital_status
                self.genre =genre
                self.key_electotal_ife =key_electotal_ife
                self.dependants_number =dependants_number
                self.decease_date=decease_date
                
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
     
    ####################################################
    def get_first_last_name(self):
        """Method to get infortmacion about first_last_name
       Returns:
            str: return a value of first_last_name
        """      
        return self.first_last_name
    
    
    def get_second_last_name(self):
        """Method to get infortmacion about second_last_name
       Returns:
            str: return a value of second_last_name
        """      
        return self.second_last_name
    

    def get_aditional_last_name(self):
        """Method to get infortmacion about aditional_last_name
       Returns:
            str: return a value of aditional_last_name
        """      
        return self.aditional_last_name
   
   
    def get_name(self):
        """Method to get infortmacion about name
       Returns:
            str: return a value of name
        """      
        return self.name
    
    
    def get_date_of_birth(self):
        """Method to get infortmacion about date_of_birth
       Returns:
            str: return a value of date_of_birth
        """      
        return self.date_of_birth
     
    
    
    def get_rfc(self):
        """Method to get infortmacion about rfc
       Returns:
            str: return a value of rfc
        """      
        return self.rfc


    def get_curp(self):
        """Method to get infortmacion about curp
       Returns:
            str: return a value of curp
        """      
        return self.curp
    
    
    def get_security_social_number(self):
        """Method to get infortmacion about security_social_number
       Returns:
            str: return a value of security_social_number
        """      
        return self.security_social_number
    
    
    
    def get_citizenship(self):
        """Method to get infortmacion about citizenship
       Returns:
            str: return a value of citizenship
        """      
        return self.citizenship
    
    
    
    def get_residence(self):
        """Method to get infortmacion about residence
       Returns:
            str: return a value of residence
        """      
        return self.residence
    
        
    def get_marital_status(self):
        """Method to get infortmacion about marital_status
       Returns:
            str: return a value of marital_status
        """      
        return self.marital_status
        
    
    def get_genre(self):
        """Method to get infortmacion about genre
       Returns:
            str: return a value of genre
        """      
        return self.genre
        
    
    def get_key_electotal_ife(self):
        """Method to get infortmacion about key_electotal_ife
       Returns:
            str: return a value of key_electotal_ife
        """      
        return self.key_electotal_ife
    
        
    def get_dependants_number(self):
        """Method to get infortmacion about dependants_number
       Returns:
            str: return a value of dependants_number
        """      
        return self.dependants_number
        
        
    def get_decease_date(self):
        """Method to get infortmacion about decease_date
       Returns:
            str: return a value of decease_date
        """      
        return self.decease_date
      