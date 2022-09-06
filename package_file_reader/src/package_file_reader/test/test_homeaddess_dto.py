import unittest
from package_file_reader.src.package_file_reader.dto.HomeAddressDto import HomeAddressDto 
from package_file_reader.src.package_file_reader.dto.IHeadLine import IHeadLine



class Test_HomeAddress(unittest.TestCase):
    #Conventions:
    #       folioConsultaOtorgante -> granting_dossier
    #       claveOtorgante -> granting_key
    #       expedienteEncontrado -> file_found
    #       folioConsulta -> sheet_found
    #       Direccion -> address
    #       ColoniaPoblacion -> colony
    #       DelegacionMunicipio -> delegation
    #       Ciudad -> city
    #       Estado -> state
    #       CP -> postal_code
    #       FechaResidencia -> residence_date
    #       NumeroTelefono -> phone
    #       TipoDomicilio -> type_address
    #       TipoAsentamiento -> type_colony
    #       FechaRegistroDomicilio -> date_regiter_address
    #       TipoAltaDomicilio -> type_membership_address
    #       NumeroOtorgantesCarga -> number_granting_charge
    #       NumeroOtorgantesConsulta -> number_granting_consultation
    #       IDDomicilio -> id_home_address
       
    
    #Method to setup structs
    def setUp(self):
        self.homeaddress_dto_1 = HomeAddressDto('333333', '6666666', '1', '675269017', 
                                                'AV CTO EJIDO COLECTIVO', 
                                                'barr plateros', 
                                                'CHIMALHUACAN', 
                                                'CHIMALHUACAN',
                                                'MEX' , 
                                                56356, '2021-05-16', 
                                                1111111111, 'N', 
                                                'ZZ', '2021-05-16',
                                                0, 3, 3 , 1  )
        
        self.homeaddress_dto_2 = HomeAddressDto('333333', '6666666', '1', '675269017', 
                                                'AV CTO EJIDO COLECTIVO', 
                                                'barr plateros', 
                                                'CHIMALHUACAN', 
                                                'CHIMALHUACAN',
                                                'MEX' , 
                                                56356, '2021-05-16', 
                                                None, 'N', 
                                                'ZZ', '2021-05-16',
                                                None, None, None , None  )
        
    #Test 1
    def test_granting_dossier(self):
        self.assertEqual(self.homeaddress_dto_1.get_granting_dossier(), '333333')
        self.assertEqual(self.homeaddress_dto_1.granting_dossier, '333333')
        self.assertTrue(isinstance( self.homeaddress_dto_1.granting_dossier , str))
       
    #Test 2
    def test_granting_key(self):
        self.assertEqual(self.homeaddress_dto_1.get_granting_key(), '6666666')
        self.assertEqual(self.homeaddress_dto_1.granting_key, '6666666')
        self.assertTrue(isinstance( self.homeaddress_dto_1.granting_key , str))
       
     
    #Test 3
    def test_file_found(self):
        self.assertEqual(self.homeaddress_dto_1.get_file_found(), '1')
        self.assertEqual(self.homeaddress_dto_1.file_found, '1')
    
    #Test 4
    def test_sheet_found(self):
        self.assertEqual(self.homeaddress_dto_1.get_sheet_found(), '675269017')
        self.assertEqual(self.homeaddress_dto_1.sheet_found, '675269017')
    
    
    
    #Test 5 ##############################################
    def test_address(self):
        self.assertEqual(self.homeaddress_dto_1.get_address(), 'AV CTO EJIDO COLECTIVO')
        self.assertEqual(self.homeaddress_dto_1.address, 'AV CTO EJIDO COLECTIVO')
        self.assertTrue(isinstance(self.homeaddress_dto_1.address, str))
    
   #Test 6
    def test_colony(self):
        self.assertEqual(self.homeaddress_dto_1.get_colony(), 'barr plateros')
        self.assertEqual(self.homeaddress_dto_1.colony, 'barr plateros')
        self.assertTrue(isinstance(self.homeaddress_dto_1.address, str))
   
   #Test 7
    def test_delegation(self):
        self.assertEqual(self.homeaddress_dto_1.get_delegation(), 'CHIMALHUACAN')
        self.assertEqual(self.homeaddress_dto_1.delegation, 'CHIMALHUACAN')
        self.assertTrue(isinstance(self.homeaddress_dto_1.delegation, str))
    
    
    #Test 8
    def test_city(self):
        self.assertEqual(self.homeaddress_dto_1.get_city(), 'CHIMALHUACAN')
        self.assertEqual(self.homeaddress_dto_1.city, 'CHIMALHUACAN')
    
    #Test 9
    def test_state(self):
        self.assertEqual(self.homeaddress_dto_1.get_state(), 'MEX')
        self.assertEqual(self.homeaddress_dto_1.state, 'MEX')
        self.assertTrue(len(self.homeaddress_dto_1.state) == 3)
        
    #Test 9
    def test_postal_code(self):
        self.assertEqual(self.homeaddress_dto_1.get_postal_code(), 56356)
        self.assertEqual(self.homeaddress_dto_1.postal_code, 56356)
        self.assertTrue(isinstance(self.homeaddress_dto_1.postal_code,int ))
        self.assertTrue(len(str(self.homeaddress_dto_1.postal_code))==5 )
        
        
    
    #Test 10
    def test_residence_date(self):
        self.assertEqual(self.homeaddress_dto_1.get_residence_date(), '2021-05-16')
        self.assertEqual(self.homeaddress_dto_1.residence_date, '2021-05-16')
    
    
    #Test 11
    def test_phone(self):
        self.assertEqual(self.homeaddress_dto_1.get_phone(), 1111111111)
        self.assertEqual(self.homeaddress_dto_1.phone, 1111111111)
    
    
    #Test 12
    def test_id_home_address(self):
        self.assertEqual(self.homeaddress_dto_1.get_id_home_address(), 1)
        self.assertEqual(self.homeaddress_dto_1.id_home_address, 1)
        
 
    #Test 13
    def test_number_granting_consultation(self):
        self.assertEqual(self.homeaddress_dto_1.get_number_granting_charge(), 3)
        self.assertEqual(self.homeaddress_dto_1.number_granting_charge, 3)
        self.assertAlmostEqual(len(str(self.homeaddress_dto_1.number_granting_charge)),1 )
        
        
    #################      
    
    #Test 14
    def test_id_home_address_when_is_none(self):
        self.assertIsNone(self.homeaddress_dto_2.id_home_address)
    
    
    #Test 14
    def test_number_granting_charge_when_is_none(self):
           self.assertIsNone(self.homeaddress_dto_2.number_granting_charge)
    
    
    #Test 14
    def test_type_membership_address_when_is_none(self):
           self.assertIsNone(self.homeaddress_dto_2.type_membership_address)
          
    
        
    #Test 15
    def test_indicator_is_instance_of_iheadline(self):
        self.assertTrue(isinstance(self.homeaddress_dto_2, IHeadLine))  
              