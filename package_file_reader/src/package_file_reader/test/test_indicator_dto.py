from typing import Tuple
import unittest
from package_file_reader.src.package_file_reader.dto.IndicatorDto import IndicatorDto 
from package_file_reader.src.package_file_reader.dto.IHeadLine import IHeadLine


class Test_Indicator(unittest.TestCase):
    
    #Conventions:
    #       folioConsultaOtorgante -> granting_dossier
    #       claveOtorgante -> granting_key
    #       expedienteEncontrado -> file_found
    #       folioConsulta -> sheet_found
    #       descriptionInd -> description_ind
    #       valorInd -> value_ind
    
    #Method to setup structs
    def setUp(self):
        self.indicator_dto_1 = IndicatorDto('333333', '6666666', '1', '675269017', 'Testde indicador', 123456)
        self.indicator_dto_2 = IndicatorDto('333333', '6666666', '1', '675269017',None , None)
        self.indicator_dto_3 = None
        self.indicator_dto_4 = IndicatorDto('333333', '6666666', '1', '675269017',11111 , 'testetsttest')
        
        
        
        

    #Test 1
    def test_granting_dossier(self):
        self.assertEqual(self.indicator_dto_1.get_granting_dossier(), '333333')
        self.assertEqual(self.indicator_dto_1.granting_dossier, '333333')
        self.assertTrue(isinstance( self.indicator_dto_1.granting_dossier , str))
       
        
    #Test 2
    def test_granting_key(self):
        self.assertEqual(self.indicator_dto_1.get_granting_key(), '6666666')
        self.assertEqual(self.indicator_dto_1.granting_key, '6666666')
        self.assertTrue(isinstance( self.indicator_dto_1.granting_key , str))
       
     
    #Test 3
    def test_file_found(self):
        self.assertEqual(self.indicator_dto_1.get_file_found(), '1')
        self.assertEqual(self.indicator_dto_1.file_found, '1')
    
    #Test 4
    def test_sheet_found(self):
        self.assertEqual(self.indicator_dto_1.get_sheet_found(), '675269017')
        self.assertEqual(self.indicator_dto_1.sheet_found, '675269017')
    
    
    #Test 5    
    def test_issubclass_of_iheadline(self):
        self.assertTrue(issubclass(IndicatorDto, IHeadLine))
        
    
    #Test 6
    def test_when_indicator_value_ind_is_none(self):
        self.assertIsNone(self.indicator_dto_2.get_value_ind())
        self.assertIsNone(self.indicator_dto_2.value_ind)
   
    #Test 7 launch exception when value is None
    def test_raise_exception_indicator_description_ind_is_none(self):
       with self.assertRaises(Exception):
           self.assertIsNone(self.indicator_dto_2.get_description_ind())
           self.assertIsNone(self.indicator_dto_2.description_ind)
      
    #Test 8 launch exception when value is None
    def test_raise_exception_indicator_value_ind_is_none(self):
        with self.assertRaises(Exception):
            self.assertIsNotNone(self.indicator_dto_2.get_value_ind())
            self.assertIsNotNone(self.indicator_dto_2.value_ind)

    #Test 9
    def test_raise_exception_in_failed_parameters_value_ind(self):
        self.assertFalse( isinstance(self.indicator_dto_4.value_ind, int) )
    
    #Test 10
    def test_raise_exception_in_failed_parameters_description_ind(self):
        self.assertFalse( isinstance(self.indicator_dto_4.description_ind, str) )
    

    #Test 11
    def test_indicator_is_none(self):
        self.assertIsNone(self.indicator_dto_3)  
        
     
    #Test 12
    def test_indicator_is_instance_of_iheadline(self):
        self.assertTrue(isinstance(self.indicator_dto_1, IHeadLine))  
          