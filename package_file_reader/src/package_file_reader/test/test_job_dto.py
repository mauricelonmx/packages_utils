import unittest
from package_file_reader.src.package_file_reader.dto.JobDto import JobDto 
from package_file_reader.src.package_file_reader.dto.IHeadLine import IHeadLine



class Test_Job(unittest.TestCase):
    #Conventions:
    #   folioConsultaOtorgante -> granting_dossier
    #   claveOtorgante -> granting_key
    #   expedienteEncontrado -> file_found
    #   folioConsulta -> sheet_found
    #   nombreEmpresa -> company_name
    
    #   direccion -> company_address
    #   coloniaPoblacional -> colony
    #   delegacionMunicipio -> delegation
    #   ciudad -> city
    #   estado -> state
    #   CP  -> postal_code
    #   numeroTelefonico -> phone
    
    #   extension -> extension
    #   fax -> fax
    #   puesto -> position
    #   fechaContratacion -> date_hiring
    #   claveMoneda -> currency
    #   salariomensual -> fixed_salary
    #   fechaUltimoDiaEmpleo -> last_date_hiring
    #   fechaVerificacionEmpleo -> verification_date_hiring
              
    
    #Method to setup structs
    
                 
                 
    def setUp(self):
        self.job_dto_1 = JobDto('333333', '6666666', '1', '675269017', 
                                'GLOBANT', 
                                'AV PUERTO MADERO 234', 
                                'GRAN BUENOS AIRES', 
                                'GRAN BUENOS AIRES', 
                                'CIUDAD CAPITAL',
                                'CABA' , 
                                111111999,
                                999,
                                911,
                                22222222,
                                'Gerente Account',
                                '2020-08-09',
                                'US',
                                1500,
                                '1998-01-12', 
                                '2020-02-15'
                                )
        
      #Test 1
    def test_granting_dossier(self):
        self.assertEqual(self.job_dto_1.get_granting_dossier(), '333333')
        self.assertEqual(self.job_dto_1.granting_dossier, '333333')
        self.assertTrue(isinstance( self.job_dto_1.granting_dossier , str))
       
    #Test 2
    def test_granting_key(self):
        self.assertEqual(self.job_dto_1.get_granting_key(), '6666666')
        self.assertEqual(self.job_dto_1.granting_key, '6666666')
        self.assertTrue(isinstance( self.job_dto_1.granting_key , str))
       
     
    #Test 3
    def test_file_found(self):
        self.assertEqual(self.job_dto_1.get_file_found(), '1')
        self.assertEqual(self.job_dto_1.file_found, '1')
    
    #Test 4
    def test_sheet_found(self):
        self.assertEqual(self.job_dto_1.get_sheet_found(), '675269017')
        self.assertEqual(self.job_dto_1.sheet_found, '675269017')
    
    #Test 5 ###############
    def test_company_name(self):
        self.assertTrue(self.job_dto_1.get_company_name()=='GLOBANT')
        self.assertEqual(self.job_dto_1.company_name ,'GLOBANT')
     
     
    #   direccion -> company_address
    #   coloniaPoblacional -> colony
    #   delegacionMunicipio -> delegation
    #   ciudad -> city
    #   estado -> state
    #   CP  -> postal_code
    #   numeroTelefonico -> phone
     
        
    #Test 6
    def test_company_address(self):
        self.assertTrue(self.job_dto_1.get_company_address()=='AV PUERTO MADERO 234')
        self.assertEqual(self.job_dto_1.company_address ,'AV PUERTO MADERO 234')
        self.assertTrue(isinstance( self.job_dto_1.company_address, str) )
        
       
    #Test 7
    def test_colony(self):
        self.assertEquals(self.job_dto_1.colony ,'GRAN BUENOS AIRES')
        self.assertTrue(isinstance( self.job_dto_1.colony, str) )
        self.assertTrue(self.job_dto_1.colony=='GRAN BUENOS AIRES')
        
    #Test 8
    def test_delegation(self):
        self.assertTrue(self.job_dto_1.get_delegation()=='GRAN BUENOS AIRES')
        self.assertEqual(self.job_dto_1.delegation ,'GRAN BUENOS AIRES')
    
    
    #Test 9
    def test_city(self):
        self.assertTrue(self.job_dto_1.get_city()=='CIUDAD CAPITAL')
        self.assertEqual(self.job_dto_1.city ,'CIUDAD CAPITAL')
        
    #Test 10
    def test_state(self):
        self.assertTrue(self.job_dto_1.get_state()=='CABA')
        self.assertEqual(self.job_dto_1.state ,'CABA')
        self.assertNotEquals(self.job_dto_1.state ,'CABAs')
        
    
    #Test 11
    def test_postal_code(self):
        self.assertTrue(self.job_dto_1.get_postal_code()==111111999)
        self.assertEqual(self.job_dto_1.postal_code ,111111999)
        self.assertTrue(isinstance( self.job_dto_1.postal_code, int) )
        
        
     
    #Test 12
    def test_phone(self):
        self.assertTrue(self.job_dto_1.get_phone()==999)
        self.assertEqual(self.job_dto_1.phone ,999)
    
   
    #Test 13
    def test_extension(self):
       self.assertTrue(self.job_dto_1.get_extension()==911)
       self.assertEqual(self.job_dto_1.extension ,911)
       self.assertTrue(len(str(self.job_dto_1.extension))==3 )
       
       
    #Test 14
    def test_position(self):
       self.assertTrue(self.job_dto_1.get_position()=='Gerente Account')
       self.assertEqual(self.job_dto_1.position ,'Gerente Account')
       self.assertTrue(isinstance(self.job_dto_1.position,str)) 
    

    #Test 15
    def test_currency(self):
       self.assertTrue(self.job_dto_1.get_currency()=='US')
       self.assertEqual(self.job_dto_1.currency ,'US')
       self.assertTrue(isinstance(self.job_dto_1.currency,str)) 
    
    #Test 15
    def test_fixed_salary(self):
        self.assertTrue(self.job_dto_1.get_fixed_salary()==1500)
        self.assertEqual(self.job_dto_1.fixed_salary ,1500)
        self.assertTrue(isinstance(self.job_dto_1.fixed_salary,int)) 
     
        
    #Test 15
    def test_verification_date_hiring(self):
        self.assertTrue(self.job_dto_1.get_verification_date_hiring()=='2020-02-15')
        self.assertEqual(self.job_dto_1.verification_date_hiring ,'2020-02-15')
        self.assertTrue(isinstance(self.job_dto_1.verification_date_hiring,str)) 

     