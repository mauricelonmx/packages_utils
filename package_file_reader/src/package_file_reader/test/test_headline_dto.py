import unittest
from package_file_reader.src.package_file_reader.dto.HeadLineDto import HeadLineDto
from package_file_reader.src.package_file_reader.dto.IHeadLine import IHeadLine



class Test_HeadLine(unittest.TestCase):
    #Conventions:
    #       folioConsultaOtorgante -> granting_dossier
    #       claveOtorgante -> granting_key
    #       expedienteEncontrado -> file_found
    #       folioConsulta -> sheet_found
    #       tipoMensaje -> type_message
    #      leyenda -> caption
    
    #Method to setup structs
    def setUp(self):
        self.headLine_dto = HeadLineDto('11334148', '0000091008', '1', '775269017')
    
    #Test 1
    def test_granting_dossier(self):
        self.assertEqual(self.headLine_dto.get_granting_dossier(), '11334148')
        self.assertEqual(self.headLine_dto.granting_dossier, '11334148')
        self.assertTrue(isinstance( self.headLine_dto.granting_dossier , str))
       
    #Test 2
    def test_granting_key(self):
        self.assertEqual(self.headLine_dto.get_granting_key(), '0000091008')
        self.assertEqual(self.headLine_dto.granting_key, '0000091008')
        self.assertTrue(isinstance( self.headLine_dto.granting_key , str))
       
     
    #Test 3
    def test_file_found(self):
        self.assertEqual(self.headLine_dto.get_file_found(), '1')
        self.assertEqual(self.headLine_dto.file_found, '1')
    
    #Test 4
    def test_sheet_found(self):
        self.assertEqual(self.headLine_dto.get_sheet_found(), '775269017')
        self.assertEqual(self.headLine_dto.sheet_found, '775269017')
    
    #Test 5
    def test_issubclass_of_iheadline(self):
        self.assertTrue(issubclass(HeadLineDto, IHeadLine))
        self.assertTrue(isinstance(self.headLine_dto, IHeadLine))