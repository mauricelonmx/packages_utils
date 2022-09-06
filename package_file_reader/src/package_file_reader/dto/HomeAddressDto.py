from package_file_reader.src.package_file_reader.dto.IHeadLine import IHeadLine

class HomeAddressDto(IHeadLine):
    """Class AddressDto to handle all parameters for Address entity, associated with Person
       Conventions xml:
       folioConsultaOtorgante -> granting_dossier
       claveOtorgante -> granting_key
       expedienteEncontrado -> file_found
       folioConsulta -> sheet_found
       Direccion -> address
       ColoniaPoblacion -> colony
       DelegacionMunicipio -> deletagion
       Ciudad -> city
       Estado -> state
       CP -> postal_code
       FechaResidencia -> residence_date
       NumeroTelefono -> phone
       TipoDomicilio -> type_address
       TipoAsentamiento -> type_colony
       FechaRegistroDomicilio -> date_regiter_address
       TipoAltaDomicilio -> type_membership_address
       NumeroOtorgantesCarga -> number_granting_charge
       NumeroOtorgantesConsulta -> number_granting_consultation
       IDDomicilio -> id_home_address
    """    
 
    def __init__(self , granting_dossier : str, granting_key: str, file_found:str,  sheet_found: str, address: str, 
                 colony: str, delegation: str, city : str, state : str, postal_code : int, residence_date: str , phone : int, 
                type_address : str , type_colony : int, date_register_address: str, type_membership_address : int, 
                number_granting_charge :int, number_granting_consultation : int, id_home_address : int ) -> None :
        
        self.granting_dossier = granting_dossier 
        self.granting_key =granting_key
        self.file_found =file_found
        self.sheet_found = sheet_found  
        self.address = address 
        self.colony = colony
        self.delegation = delegation
        self.city = city 
        self.state = state
        self.postal_code = postal_code
        self.residence_date = residence_date
        self.phone = phone
        self.type_address = type_address
        self.type_colony = type_colony
        self.date_register_address = date_register_address
        self.type_membership_address = type_membership_address
        self.number_granting_charge = number_granting_charge
        self.number_granting_consultation = number_granting_consultation
        self.id_home_address = id_home_address

        
       
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


    def get_address(self):
        """Method to get infortmacion about address
        Returns:
            str: return a value of address
        """        
        return self.address

    def get_colony(self):
        """Method to get infortmacion about colony
        Returns:
            str: return a value of colony
        """        
        return self.colony

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
            str: return a value of  state
        """      
        return self.state

    def get_postal_code(self):
        """Method to get infortmacion about postal_code
        Returns:
            str: return a value of  postal_code
        """      
        return self.postal_code


    def get_residence_date(self):
        """Method to get infortmacion about residence_date
        Returns:
            str: return a value of  residence_date
        """      
        return self.residence_date


    def get_phone(self):
        """Method to get infortmacion about phone
        Returns:
            str: return a value of  phone
        """      
        return self.phone


    def get_type_address(self):
        """Method to get infortmacion about type_address
        Returns:
            str: return a value of  type_address
        """      
        return self.type_address


    def get_type_colony(self):
        """Method to get infortmacion about type_colony
        Returns:
            str: return a value of  type_colony
        """      
        return self.type_colony

    def get_date_register_address(self):
        """Method to get infortmacion about date_register_address
        Returns:
            str: return a value of  date_register_address
        """      
        return self.date_register_address

    def get_type_membership_address(self):
        """Method to get infortmacion about type_membership_address
        Returns:
            str: return a value of type_membership_address
        """      
        return self.type_membership_address


    def get_number_granting_charge(self):
        """Method to get infortmacion about number_granting_charge
        Returns:
            str: return a value of  number_granting_charge
        """      
        return self.number_granting_charge


    def get_number_granting_consultation(self):
        """Method to get infortmacion about number_granting_consultation
        Returns:
            str: return a value of  number_granting_consultation
        """      
        return self.number_granting_consultation


    def get_id_home_address(self):
        """Method to get infortmacion about id_home_address
        Returns:
            str: return a value of  id_home_address
        """      
        return self.id_home_address
