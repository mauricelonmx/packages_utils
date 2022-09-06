import unittest
from package_file_reader.src.package_file_reader.dto.MessageDto import MessageDto 
from package_file_reader.src.package_file_reader.dto.IHeadLine import IHeadLine


class Test_Message(unittest.TestCase):
    
    #Conventions:
    #       folioConsultaOtorgante -> granting_dossier
    #       claveOtorgante -> granting_key
    #       expedienteEncontrado -> file_found
    #       folioConsulta -> sheet_found
    #       tipoMensaje -> type_message
    #      leyenda -> caption
    
    #Method to setup structs
    def setUp(self):
        self.message_dto = MessageDto('11334148', '0000091008', '1', '775269017', 1, '2')
    
    #Test 1
    def test_granting_dossier(self):
        self.assertEqual(self.message_dto.get_granting_dossier(), '11334148')
        self.assertEqual(self.message_dto.granting_dossier, '11334148')
        self.assertTrue(isinstance( self.message_dto.granting_dossier , str))
       
        
    #Test 2
    def test_granting_key(self):
        self.assertEqual(self.message_dto.get_granting_key(), '0000091008')
        self.assertEqual(self.message_dto.granting_key, '0000091008')
        self.assertTrue(isinstance( self.message_dto.granting_key , str))
       
     
    #Test 3
    def test_file_found(self):
        self.assertEqual(self.message_dto.get_file_found(), '1')
        self.assertEqual(self.message_dto.file_found, '1')
    
    #Test 4
    def test_sheet_found(self):
        self.assertEqual(self.message_dto.get_sheet_found(), '775269017')
        self.assertEqual(self.message_dto.sheet_found, '775269017')
    
    
    #Test 5
    def test_type_message(self):
        self.assertEqual(self.message_dto.get_type_message(), 1)
        self.assertEqual(self.message_dto.type_message, 1)
        self.assertTrue(isinstance( self.message_dto.type_message , int))
        
    
    
    #Test 6
    def test_caption(self):
        self.assertEqual(self.message_dto.get_caption(), '2')
        self.assertEqual(self.message_dto.caption, '2')
        self.assertTrue(isinstance( self.message_dto.caption , str))
    
    #Test 7    
    def test_issubclass_of_iheadline(self):
        self.assertTrue(issubclass(MessageDto, IHeadLine))
        self.assertTrue(isinstance(self.message_dto, IHeadLine))  