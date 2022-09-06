import unittest
from package_file_reader.src.package_file_reader.dto.NameDto import NameDto 
from package_file_reader.src.package_file_reader.dto.IHeadLine import IHeadLine


class Test_Name(unittest.TestCase):
    
    #Conventions xml:
    #     folioConsultaOtorgante -> granting_dossier
    #     claveOtorgante -> granting_key
    #     expedienteEncontrado -> file_found
    #     folioConsulta -> sheet_found
    
    #     ApellidoPaterno -> last_name_one
    #     ApellidoMaterno -> last_name_two
    #     ApellidoAdicional -> last_name_aditional
    #     Nombres -> name
    #     FechaNacimiento -> date_of_birth
    #     RFC -> rfc
    #     CURP -> curp
    #     Numero de seguridad Social -> security_social_number
    #     Nacionalidad -> citizenship
    #     Residencia -> residence
    #     EstadoCivil -> marital_status 
    #     Sexo -> genre
    #     ClaveElectorIFE -> key_electotal_ife
    #     NumeroDependientes -> dependants_number
    #     FechaDefuncion   -> decease_date   
    
     #Method to setup structs
    def setUp(self):
        self.name_dto_1 = NameDto('333333', '6666666', '1', '675269017', 
                                  'Gutierrez' , 'Perez', None, 'Mauricio', '2000-10-01', 'PASA881122',
                                  None, 100200300, 'MX', 1, 'D', 'M', None, 0, None
                                  )
        self.name_dto_2 = None
        
    
    #Test 1
    def test_granting_dossier(self):
        self.assertEqual(self.name_dto_1.get_granting_dossier(), '333333')
        self.assertEqual(self.name_dto_1.granting_dossier, '333333')
        self.assertTrue(isinstance( self.name_dto_1.granting_dossier , str))
       
        
    #Test 2
    def test_granting_key(self):
        self.assertEqual(self.name_dto_1.get_granting_key(), '6666666')
        self.assertEqual(self.name_dto_1.granting_key, '6666666')
        self.assertTrue(isinstance( self.name_dto_1.granting_key , str))
       
     
    #Test 3
    def test_file_found(self):
        self.assertEqual(self.name_dto_1.get_file_found(), '1')
        self.assertEqual(self.name_dto_1.file_found, '1')
    
    #Test 4
    def test_sheet_found(self):
        self.assertEqual(self.name_dto_1.get_sheet_found(), '675269017')
        self.assertEqual(self.name_dto_1.sheet_found, '675269017')
       
    #################################################   
    #Test 5
    def test_first_last_name(self):
        self.assertEqual(self.name_dto_1.get_first_last_name(), 'Gutierrez')
        self.assertEqual(self.name_dto_1.first_last_name, 'Gutierrez')   
        
    #Test 5 
    def test_second_last_name(self):
        print(self.name_dto_1.get_second_last_name())
        self.assertEqual(self.name_dto_1.get_second_last_name(), 'Perez')
        self.assertEqual(self.name_dto_1.second_last_name, 'Perez')       
        
    #Test 6
    def test_aditional_last_name(self):
        self.assertEqual(self.name_dto_1.get_aditional_last_name(), None)
        self.assertEqual(self.name_dto_1.aditional_last_name, None)  
        self.assertIsNone(self.name_dto_1.aditional_last_name)  
                 
    
    #Test 7
    def test_name(self):
        self.assertEqual(self.name_dto_1.get_name(), 'Mauricio')
        self.assertEqual(self.name_dto_1.name, 'Mauricio')  
        self.assertIsNotNone(self.name_dto_1.name)  
        self.assertTrue(isinstance( self.name_dto_1.name, str) )  
        
                
    #Test 8
    def test_date_of_birth(self):
        self.assertEqual(self.name_dto_1.get_date_of_birth(), '2000-10-01')
        self.assertEqual(self.name_dto_1.date_of_birth, '2000-10-01')  
        self.assertIsNotNone(self.name_dto_1.date_of_birth)  
        self.assertEquals(len(str(self.name_dto_1.date_of_birth)),10 )  
        
                 
    #Test 9
    def test_rfc(self):
        self.assertEqual(self.name_dto_1.get_rfc(), 'PASA881122')
        self.assertEqual(self.name_dto_1.rfc, 'PASA881122')  
        self.assertTrue(len(str(self.name_dto_1.rfc))<=13 )  


    #Test 10
    def test_curp(self):
        self.assertEqual(self.name_dto_1.get_curp(), None)
        self.assertEqual(self.name_dto_1.curp, None)  
        self.assertIsNone(self.name_dto_1.curp)  

    
    #Test 10
    def test_security_social_number(self):
        self.assertEqual(self.name_dto_1.get_security_social_number(), 100200300)
        self.assertEqual(self.name_dto_1.security_social_number, 100200300)  
        self.assertIsInstance(self.name_dto_1.security_social_number, int)  
        self.assertTrue(len(str(self.name_dto_1.security_social_number))<=11 )  
    
    
    #Test 10
    def test_citizenship(self):
        self.assertEqual(self.name_dto_1.get_citizenship(), 'MX')
        self.assertEqual(self.name_dto_1.citizenship, 'MX')  
        self.assertIsInstance(self.name_dto_1.citizenship,str)  
    
    
    #Test 10
    def test_residence(self):
        self.assertEqual(self.name_dto_1.get_residence(), 1)
        self.assertEqual(self.name_dto_1.residence, 1)  
        self.assertIsInstance(self.name_dto_1.residence, int)  
    
    #Test 10
    def test_marital_status(self):
        self.assertEqual(self.name_dto_1.get_marital_status(), 'D')
        self.assertEqual(self.name_dto_1.marital_status, 'D' ) 
        self.assertTrue(isinstance( self.name_dto_1.marital_status, str) )  
        self.assertTrue(len(str(self.name_dto_1.marital_status))==1 )  
        
    #Test 11
    def test_indicator_is_none(self):
        self.assertIsNone(self.name_dto_2)  
           
    
    
    #Test 10
    def test_genre(self):
        self.assertEqual(self.name_dto_1.get_genre(), 'M')
        self.assertEqual(self.name_dto_1.genre, 'M')  
        self.assertTrue(isinstance( self.name_dto_1.genre, str) )  
        self.assertTrue(len(str(self.name_dto_1.genre))==1 )   
   
   
   #Test 10
    def test_key_electotal_ife(self):
        self.assertEqual(self.name_dto_1.get_key_electotal_ife(), None)
        self.assertEqual(self.name_dto_1.key_electotal_ife, None)  
       
   #Test 10
    def test_dependants_number(self):
        self.assertEqual(self.name_dto_1.get_dependants_number(), 0)
        self.assertEqual(self.name_dto_1.dependants_number, 0)  
        
   #Test 10
    def test_decease_date(self):
        self.assertEqual(self.name_dto_1.get_decease_date(), None)
        self.assertEqual(self.name_dto_1.decease_date, None)  
    
    
    #Test 12
    def test_indicator_is_instance_of_iheadline(self):
        self.assertTrue(isinstance(self.name_dto_1, IHeadLine))      
   
   
    
                