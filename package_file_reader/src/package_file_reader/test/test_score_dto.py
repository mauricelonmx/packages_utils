import unittest
from package_file_reader.src.package_file_reader.dto.ScoreDto import ScoreDto 
from package_file_reader.src.package_file_reader.dto.IHeadLine import IHeadLine


class Test_Score(unittest.TestCase):
    
    #Conventions:
    #folioConsultaOtorgante -> granting_dossier
    #claveOtorgante -> granting_key
    #expedienteEncontrado -> file_found
    #folioConsulta -> sheet_found
    #nombreScore -> name_score
    #codigo -> code
    #valor -> value
    #razon1 -> razon1
    #razon2 -> razon2
    #razon3 -> razon3
    #razon4 -> razon4
    #error  -> error
    #indicadores -> indicators     
    
    #Method to setup structs
    def setUp(self):
        self.score_dto_1 = ScoreDto('333333', '6666666', '1', '675269017', 'name score', 123456, 1111, 
                                    'razon 1', 'razon 2', 'razon 3', 'razon 4', '0', 'indicadores')
        self.score_dto_2 = ScoreDto('333333', '6666666', '1', '675269017', 'name score', None, None, 
                                    'razon 1', 'razon 2', 'razon 3', 'razon 4', None, None)
        self.score_dto_3 = None
        
        self.score_dto_4 = ScoreDto('333333', '6666666', '1', '675269017', 'name score', 123456, 1111, 
                                    24234234, None, None, 'razon 4', 1, 2342342424)
        
        
    #Test 1
    def test_granting_dossier(self):
        self.assertEqual(self.score_dto_1.get_granting_dossier(), '333333')
        self.assertEqual(self.score_dto_1.granting_dossier, '333333')
        self.assertTrue(isinstance( self.score_dto_1.granting_dossier , str))
       
        
    #Test 2
    def test_granting_key(self):
        self.assertEqual(self.score_dto_1.get_granting_key(), '6666666')
        self.assertEqual(self.score_dto_1.granting_key, '6666666')
        self.assertTrue(isinstance( self.score_dto_1.granting_key , str))
       
     
    #Test 3
    def test_file_found(self):
        self.assertEqual(self.score_dto_1.get_file_found(), '1')
        self.assertEqual(self.score_dto_1.file_found, '1')
    
    #Test 4
    def test_sheet_found(self):
        self.assertEqual(self.score_dto_1.get_sheet_found(), '675269017')
        self.assertEqual(self.score_dto_1.sheet_found, '675269017')
    
    
    #Test 5    
    def test_issubclass_of_iheadline(self):
        self.assertTrue(issubclass(ScoreDto, IHeadLine))
        
   
    #Test 6
    def test_name_score(self):
        self.assertIsNotNone(self.score_dto_1.get_name_score()) 
        self.assertIsNotNone(self.score_dto_1.name_score)
        self.assertEqual(self.score_dto_1.name_score, 'name score')
        self.assertTrue( isinstance(self.score_dto_1.name_score, str)   )
        
      
    
    #Test 7
    def test_code(self):
        self.assertIsNotNone(self.score_dto_1.get_value()) 
        self.assertIsNotNone(self.score_dto_1.value)
        self.assertEqual(self.score_dto_1.value, 1111)
        self.assertTrue( isinstance(self.score_dto_1.value, int)   )
    
    #Test 8
    def test_value(self):
        self.assertIsNotNone(self.score_dto_1.get_code()) 
        self.assertIsNotNone(self.score_dto_1.code)
        self.assertEqual(self.score_dto_1.code, 123456)
        self.assertTrue( isinstance(self.score_dto_1.code, int)   )
        
   
   #Test 9
    def test_razons(self):
        self.assertIsNotNone(self.score_dto_1.get_razon1())
        self.assertIsNotNone(self.score_dto_1.get_razon2())
        self.assertIsNotNone(self.score_dto_1.get_razon3())
        self.assertIsNotNone(self.score_dto_1.get_razon4())
        
        self.assertIsNotNone(self.score_dto_1.razon1)
        self.assertIsNotNone(self.score_dto_1.razon2)
        self.assertIsNotNone(self.score_dto_1.razon3)
        self.assertIsNotNone(self.score_dto_1.razon4)
         
        self.assertEqual(self.score_dto_1.razon1, 'razon 1')
        self.assertEqual(self.score_dto_1.razon2, 'razon 2')
        self.assertEqual(self.score_dto_1.razon3, 'razon 3')
        self.assertEqual(self.score_dto_1.razon4, 'razon 4')
        
        self.assertTrue( isinstance(self.score_dto_1.razon1, str)   )
        self.assertTrue( isinstance(self.score_dto_1.razon2, str)   )
        self.assertTrue( isinstance(self.score_dto_1.razon3, str)   )
        self.assertTrue( isinstance(self.score_dto_1.razon4, str)   )
    
    #Test 10
    def test_error(self):
        self.assertIsNotNone(self.score_dto_1.get_error())
        self.assertIsNotNone(self.score_dto_1.error)
        self.assertEquals(self.score_dto_1.error,'0')
        self.assertTrue( isinstance(self.score_dto_1.error, str)   )
        
    #Test 11
    def test_indicators(self):
        self.assertIsNotNone(self.score_dto_1.get_indicators())
        self.assertIsNotNone(self.score_dto_1.indicators)
        self.assertNotEquals(self.score_dto_1.indicators,'01212121')
        self.assertTrue( isinstance(self.score_dto_1.indicators, str)   )
    
    ##############################################################################
    
    #Test 11
    def test_when_code_is_none(self):
        self.assertIsNone(self.score_dto_2.get_code()) 
    
    #Test 12
    def test_when_code_is_none(self):
        self.assertIsNone(self.score_dto_2.get_code()) 
        self.assertFalse(isinstance(self.score_dto_2.code, int) )    

    #Test 13
    def test_when_value_is_none(self):
        self.assertIsNone(self.score_dto_2.value) 
        self.assertFalse(isinstance(self.score_dto_2.value, int) )    
    
    #Test 14
    def test_when_error_is_none(self):
        self.assertIsNone(self.score_dto_2.error) 
        self.assertFalse(isinstance(self.score_dto_2.error, int) )    
    
    #Test 15
    def test_when_indicators_is_none(self):
        self.assertIsNone(self.score_dto_2.indicators) 
        self.assertFalse(isinstance(self.score_dto_2.indicators, int) )    

    #Test 16
    def test_indicator_is_none(self):
        self.assertIsNone(self.score_dto_3)  
        
    #Test 17
    def test_raise_exception_in_failed_parameters_error(self):
        with self.assertRaises(Exception):
            self.assertFalse( isinstance(self.score_dto_4.error, int) )
     
    #Test 18
    def test_raise_exception_in_failed_parameters_indicators(self):
        with self.assertRaises(Exception):
            self.assertFalse( isinstance(self.score_dto_4.indicators, int) )    
            
    #Test 19
    def test_raise_exception_in_failed_parameters_razon1(self):
        with self.assertRaises(Exception):
            self.assertFalse( isinstance(self.score_dto_4.razon1, int) )            