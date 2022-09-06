from package_file_reader.src.package_file_reader.reader import xml_to_dict
import unittest
import respuesta_1
import respuesta_2
import respuesta_3
import respuesta_4
import json
import xmltodict


class Test_FileReader(unittest.TestCase):
    

    #Method to setup structs
    def setUp(self):
        self.resp_1 = respuesta_1
        self.resp_2 = respuesta_2
        self.resp_3 = respuesta_3
        self.resp_4 = respuesta_4
        

    #Method to find keys in a dict
    def find_keys(self, data, key_to_extract):
        return {key: data[key] for key in data.keys() & key_to_extract} 


    #Method to  extract main keys from xml
    def extract_main_headers(self, data: None):
        key_to_extract = {'Respuesta'}
        respuesta = self.find_keys(data, key_to_extract)
        key_to_extract = {'Personas'}
        personas = self.find_keys(respuesta['Respuesta'], key_to_extract)
        key_to_extract = {'Persona'}
        persona = self.find_keys(personas['Personas'], key_to_extract)
        return persona


    #Method to  generate dict_keys to compare
    def dict_to_compare(self, key_to_compare:None):
        return  dict.fromkeys(key_to_compare, 0)
        
    #Method to convert dict to json    
    def dict_to_json(self, data : dict):
        return json.dumps(data)
    
    
    
    ######################################################################################
    #Test de respuesta_1
    def test_1_xml_to_dict_validate_keys_persona(self):
        r1 = xml_to_dict(self.resp_1.data)
        response = self.extract_main_headers(r1)
        self.assertEquals( response.keys() , self.dict_to_compare({'Persona'}).keys())      
        

    def test_1_xml_to_dict_validate_keys_encabezado(self):
        r1 = xml_to_dict(self.resp_1.data)
        response = self.extract_main_headers(r1)
        key_to_extract = {'Encabezado'}
        values_extracted = self.find_keys(response['Persona'] , key_to_extract)
        self.assertEquals(values_extracted.keys(), self.dict_to_compare({'Encabezado'}).keys())      
       
        
    def test_1_xml_to_dict_validate_values_encabezado(self):
        r1 = xml_to_dict(self.resp_1.data)
        response = self.extract_main_headers(r1)
        key_to_extract = {'Encabezado'}
        values_extracted = self.find_keys(response['Persona'] , key_to_extract)
        dict_to_compare = {'Encabezado': {'FolioConsultaOtorgante': '11334148', 'ClaveOtorgante': '0000091008', 'ExpedienteEncontrado': '1', 'FolioConsulta': '775269017'}}
        self.assertEquals(values_extracted , dict_to_compare )
        
    
    def test_1_xml_to_dict_validate_count_domicilios(self):
        r1 = xml_to_dict(self.resp_1.data)
        response = self.extract_main_headers(r1)
        key_to_extract = {'Domicilios'}
        values_extracted = self.find_keys(response['Persona'] , key_to_extract)
        key_to_extract = {'Domicilio'}
        values_extracted = self.find_keys(values_extracted['Domicilios'] , key_to_extract)
        self.assertEquals(len(values_extracted['Domicilio']) , 3)
       

    def test_1_xml_to_dict_validate_items_domicilios(self):
        r1 = xml_to_dict(self.resp_1.data)
        response = self.extract_main_headers(r1)
        key_to_extract = {'Domicilios'}
        values_extracted = self.find_keys(response['Persona'] , key_to_extract)
        key_to_extract = {'Domicilio'}
        values_extracted = self.find_keys(values_extracted['Domicilios'] , key_to_extract)
        self.assertTrue(isinstance(list(values_extracted.items()) ,list))
       

    def test_1_xml_to_dict_validate_values_domicilios(self):
        r1 = xml_to_dict(self.resp_1.data)
        response = self.extract_main_headers(r1)
        key_to_extract = {'Domicilios'}
        values_extracted = self.find_keys(response['Persona'] , key_to_extract)
        key_to_extract = {'Domicilio'}
        values_extracted = self.find_keys(values_extracted['Domicilios'] , key_to_extract)
        dict_to_compare = {'Direccion': 'NVA AMP POR LA VIA', 'ColoniaPoblacion': 'querendaro estacion', 'DelegacionMunicipio': 'ZINAPECUARO', 'Ciudad': 'ZINAPECUARO', 'Estado': 'MICH', 'CP': '58940', 'FechaResidencia': '2021-05-16', 'NumeroTelefono': None, 'TipoDomicilio': None, 'TipoAsentamiento': None, 'FechaRegistroDomicilio': '2021-05-16'}
        self.assertEquals(values_extracted['Domicilio'][0] , dict_to_compare )
   
   
    def test_1_xml_to_dict_validate_empleos(self):
        r1 = xml_to_dict(self.resp_1.data)
        response = self.extract_main_headers(r1)
        key_to_extract = {'Empleos'}
        values_extracted = self.find_keys(response['Persona'] , key_to_extract)
        dict_to_compare = {'Empleos': None }
        self.assertEquals(values_extracted, dict_to_compare )
        
   
    def test_1_xml_to_dict_validate_mensajes(self):
        r1 = xml_to_dict(self.resp_1.data)
        response = self.extract_main_headers(r1)
        key_to_extract = {'Mensajes'}
        values_extracted = self.find_keys(response['Persona'] , key_to_extract)
        key_to_extract = {'Mensaje'}
        values_extracted = self.find_keys( values_extracted['Mensajes'] , key_to_extract)
        self.assertEquals(int(values_extracted['Mensaje']['TipoMensaje']),  2 )
        self.assertEquals(int(values_extracted['Mensaje']['Leyenda']) , 1 )
    
    
    def test_1_xml_to_dict_validate_cuentas(self):
        r1 = xml_to_dict(self.resp_1.data)
        response = self.extract_main_headers(r1)
        key_to_extract = {'Cuentas'}
        values_extracted = self.find_keys(response['Persona'] , key_to_extract)
        dict_to_compare = {'Cuentas': None }
        self.assertEquals(values_extracted, dict_to_compare )
        
    
    def test_1_xml_to_dict_validate_consultas_efectuadas(self):
        r1 = xml_to_dict(self.resp_1.data)
        response = self.extract_main_headers(r1)
        key_to_extract = {'ConsultasEfectuadas'}
        values_extracted = self.find_keys(response['Persona'] , key_to_extract)
        key_to_extract = {'ConsultaEfectuada'}
        values_extracted = self.find_keys(values_extracted['ConsultasEfectuadas'] , key_to_extract)
        self.assertTrue(len(values_extracted['ConsultaEfectuada']) == 4)
       
       
    def test_1_xml_to_dict_when_xml_is_empty(self):
        with self.assertRaises(Exception):
            data=""
            r1 = xml_to_dict(data)
                
    def test_1_xml_to_dict_when_xml_is_none(self):
        with self.assertRaises(Exception):
            data=None
            r1 = xml_to_dict(data)
    
    ######################################################################################
    #Test de respuesta_2 esquema con errores solo cumple 1 test
    def test_2_xml_to_dict_validate_keys_persona(self):
        with self.assertRaises(Exception):
            r1 = xml_to_dict(self.resp_2.data)
            response = self.extract_main_headers(r1)
        
    ######################################################################################
    #Test de respuesta_3
    def test_3_xml_to_dict_validate_keys_persona(self):
        r1 = xml_to_dict(self.resp_3.data)
        response = self.extract_main_headers(r1)
        self.assertEquals( response.keys(), self.dict_to_compare({'Persona'}).keys())      
    
    def test_3_xml_to_dict_validate_keys_encabezado(self):
        r1 = xml_to_dict(self.resp_3.data)
        response = self.extract_main_headers(r1)
        key_to_extract = {'Encabezado'}
        values_extracted = self.find_keys(response['Persona'] , key_to_extract)
        self.assertEquals(values_extracted.keys(), self.dict_to_compare({'Encabezado'}).keys())      
    
    
    def test_3_xml_to_dict_validate_count_domicilios(self):
        r1 = xml_to_dict(self.resp_3.data)
        response = self.extract_main_headers(r1)
        key_to_extract = {'Domicilios'}
        values_extracted = self.find_keys(response['Persona'] , key_to_extract)
        key_to_extract = {'Domicilio'}
        values_extracted = self.find_keys(values_extracted['Domicilios'] , key_to_extract)
        self.assertEquals(len(values_extracted['Domicilio']) , 2)
    
    
    def test_3_xml_to_dict_validate_items_domicilios(self):
        r1 = xml_to_dict(self.resp_3.data)
        response = self.extract_main_headers(r1)
        key_to_extract = {'Domicilios'}
        values_extracted = self.find_keys(response['Persona'] , key_to_extract)
        key_to_extract = {'Domicilio'}
        values_extracted = self.find_keys(values_extracted['Domicilios'] , key_to_extract)
        self.assertTrue(isinstance(list(values_extracted.items()), list))
    
    
    def test_3_xml_to_dict_validate_values_domicilios(self):
        r1 = xml_to_dict(self.resp_3.data)
        response = self.extract_main_headers(r1)
        key_to_extract = {'Domicilios'}
        values_extracted = self.find_keys(response['Persona'] , key_to_extract)
        key_to_extract = {'Domicilio'}
        values_extracted = self.find_keys(values_extracted['Domicilios'] , key_to_extract)
        dict_to_compare = {'Direccion': 'NVA AMP POR LA VIA', 'ColoniaPoblacion': 'querendaro estacion', 'DelegacionMunicipio': 'ZINAPECUARO', 'Ciudad': 'ZINAPECUARO', 'Estado': 'MICH', 'CP': '58940', 'FechaResidencia': '2021-05-16', 'NumeroTelefono': None, 'TipoDomicilio': None, 'TipoAsentamiento': None, 'FechaRegistroDomicilio': '2021-05-16'}
        self.assertNotEquals(values_extracted['Domicilio'][0] , dict_to_compare )

    
    def test_3_xml_to_dict_validate_empleos(self):
        r1 = xml_to_dict(self.resp_3.data)
        response = self.extract_main_headers(r1)
        key_to_extract = {'Empleos'}
        values_extracted = self.find_keys(response['Persona'] , key_to_extract)
        dict_to_compare = {'Empleos': None }
        self.assertEquals(values_extracted, dict_to_compare )
   
   
    def test_3_xml_to_dict_validate_mensajes(self):
        r1 = xml_to_dict(self.resp_3.data)
        response = self.extract_main_headers(r1)
        key_to_extract = {'Mensajes'}
        values_extracted = self.find_keys(response['Persona'] , key_to_extract)
        key_to_extract = {'Mensaje'}
        values_extracted = self.find_keys( values_extracted['Mensajes'] , key_to_extract)
        self.assertNotEquals(int(values_extracted['Mensaje']['TipoMensaje']) , 99 )
        self.assertNotEquals(int(values_extracted['Mensaje']['Leyenda']) , 45 )
    
    
    def test_3_xml_to_dict_validate_cuentas(self):
        r1 = xml_to_dict(self.resp_3.data)
        response = self.extract_main_headers(r1)
        key_to_extract = {'Cuentas'}
        values_extracted = self.find_keys(response['Persona'] , key_to_extract)
        dict_to_compare = {'Cuentas': None }
        self.assertEquals(values_extracted, dict_to_compare )


    def test_3_xml_to_dict_validate_consultas_efectuadas(self):
        r1 = xml_to_dict(self.resp_3.data)
        response = self.extract_main_headers(r1)
        key_to_extract = {'ConsultasEfectuadas'}
        values_extracted = self.find_keys(response['Persona'] , key_to_extract)
        key_to_extract = {'ConsultaEfectuada'}
        values_extracted = self.find_keys(values_extracted['ConsultasEfectuadas'] , key_to_extract)
        self.assertTrue(isinstance(list(values_extracted.items()), list))
        self.assertTrue( len( list(values_extracted.items())) == 1)

    
    def test_3_xml_to_dict_when_xml_is_empty(self):
        with self.assertRaises(Exception):
            data=""
            r1 = xml_to_dict(data)
                
    def test_3_xml_to_dict_when_xml_is_none(self):
        with self.assertRaises(Exception):
            data=None
            r1 = xml_to_dict(data)
        
    def test_3_xml_to_dict_when_xml_is_dict_empty(self):
        with self.assertRaises(Exception):
            data={}
            r1 = xml_to_dict(data)
        
    def test_3_xml_to_dict_when_xml_tag_broken(self):
        with self.assertRaises(Exception):
            data='''
                <Brokentag>
                    <ConsultaEfectuada>
                        <FechaConsulta>2020-04-16</FechaConsulta>
                        <ClaveOtorgante/>
                        <NombreOtorgante>BANCO MUISCA</NombreOtorgante>
                        <TelefonoOtorgante>17207988</TelefonoOtorgante>
                        <TipoCredito>F</TipoCredito>
                        <ClaveUnidadMonetaria>MX</ClaveUnidadMonetaria>
                        <ImporteCredito>0</ImporteCredito>
                        <TipoResponsabilidad/>
                    </ConsultaEfectuada>
                </ConsultasEfectuadas>'''
            r1 = xml_to_dict(data)
    
    
    ######################################################################################
    #Test de respuesta_4
    
    def test_4_xml_to_dict_validate_values_encabezado(self):
        r1 = xml_to_dict(self.resp_4.data)
        response = self.extract_main_headers(r1)
        key_to_extract = {'Encabezado'}
        values_extracted = self.find_keys(response['Persona'] , key_to_extract)
        dict_to_compare = {'Encabezado': {'FolioConsultaOtorgante': '113341499', 'ClaveOtorgante': '0000099008', 'ExpedienteEncontrado': '1', 'FolioConsulta': '7752687017'}}
        self.assertNotEquals(values_extracted , dict_to_compare )
 
    
    def test_4_xml_to_dict_validate_count_domicilios(self):
        r1 = xml_to_dict(self.resp_4.data)
        response = self.extract_main_headers(r1)
        key_to_extract = {'Domicilios'}
        values_extracted = self.find_keys(response['Persona'] , key_to_extract)
        key_to_extract = {'Domicilio'}
        values_extracted = self.find_keys(values_extracted['Domicilios'] , key_to_extract)
        self.assertNotEquals(len(values_extracted['Domicilio']) , 4)
    
    
    def test_4_xml_to_dict_validate_list_domicilios(self):
        r1 = xml_to_dict(self.resp_4.data)
        response = self.extract_main_headers(r1)
        key_to_extract = {'Domicilios'}
        values_extracted = self.find_keys(response['Persona'] , key_to_extract)
        key_to_extract = {'Domicilio'}
        values_extracted = self.find_keys(values_extracted['Domicilios'] , key_to_extract)
        self.assertTrue(isinstance(list(values_extracted.items()), list))

    
    def test_4_xml_to_dict_validate_items_domicilios(self):
        r1 = xml_to_dict(self.resp_4.data)
        response = self.extract_main_headers(r1)
        key_to_extract = {'Domicilios'}
        values_extracted = self.find_keys(response['Persona'] , key_to_extract)
        key_to_extract = {'Domicilio'}
        values_extracted = self.find_keys(values_extracted['Domicilios'] , key_to_extract)
        self.assertTrue(len(list(values_extracted['Domicilio'])) == 3) 

    
    def test_4_xml_to_dict_validate_values_domicilios(self):
        r1 = xml_to_dict(self.resp_4.data)
        response = self.extract_main_headers(r1)
        key_to_extract = {'Domicilios'}
        values_extracted = self.find_keys(response['Persona'] , key_to_extract)
        key_to_extract = {'Domicilio'}
        values_extracted = self.find_keys(values_extracted['Domicilios'] , key_to_extract)
        dict_to_compare = {'Direccion': 'XXXX VIA', 'ColoniaPoblacion': 'estacion', 'DelegacionMunicipio': 'ZINAPECUARO', 'Ciudad': 'X', 'Estado': 'X', 'CP': '4', 'FechaResidencia': '2021-05-16', 'NumeroTelefono': None, 'TipoDomicilio': None, 'TipoAsentamiento': None, 'FechaRegistroDomicilio': '2021-05-16'}
        self.assertNotEquals(values_extracted['Domicilio'][2] , dict_to_compare )
    

    def test_4_xml_to_dict_validate_empleos(self):
        r1 = xml_to_dict(self.resp_4.data)
        response = self.extract_main_headers(r1)
        key_to_extract = {'Empleos'}
        values_extracted = self.find_keys(response['Persona'] , key_to_extract)
        dict_to_compare = {'Empleos': None }
        self.assertEquals(values_extracted, dict_to_compare )
   
    
    def test_4_xml_to_dict_validate_mensajes(self):
        r1 = xml_to_dict(self.resp_4.data)
        response = self.extract_main_headers(r1)
        key_to_extract = {'Mensajes'}
        values_extracted = self.find_keys(response['Persona'] , key_to_extract)
        key_to_extract = {'Mensaje'}
        values_extracted = self.find_keys( values_extracted['Mensajes'] , key_to_extract)
        self.assertEquals(int(values_extracted['Mensaje']['TipoMensaje']) , 20 )
        self.assertEquals(int(values_extracted['Mensaje']['Leyenda']) , 11 )

    
    def test_4_xml_to_dict_validate_cuentas(self):
        r1 = xml_to_dict(self.resp_4.data)
        response = self.extract_main_headers(r1)
        key_to_extract = {'Cuentas'}
        values_extracted = self.find_keys(response['Persona'] , key_to_extract)
        dict_to_compare = {'Cuentas': None }
        self.assertNotEquals(values_extracted, dict_to_compare )

    
    def test_4_xml_to_dict_validate_count_cuentas(self):
        r1 = xml_to_dict(self.resp_4.data)
        response = self.extract_main_headers(r1)
        key_to_extract = {'Cuentas'}
        values_extracted = self.find_keys(response['Persona'] , key_to_extract)
        key_to_extract = {'Cuenta'}
        values_extracted = self.find_keys(values_extracted['Cuentas'] , key_to_extract)
        self.assertTrue(len(list(values_extracted['Cuenta'])) == 12) 


    def test_4_xml_to_dict_compare_cuentas(self):
        r1 = xml_to_dict(self.resp_4.data)
        response = self.extract_main_headers(r1)
        key_to_extract = {'Cuentas'}
        values_extracted = self.find_keys(response['Persona'] , key_to_extract)
        key_to_extract = {'Cuenta'}
        values_extracted = self.find_keys(values_extracted['Cuentas'] , key_to_extract)
        account_0 = values_extracted['Cuenta'][0]
        account_1 = values_extracted['Cuenta'][1]
        account_10 = values_extracted['Cuenta'][10]
               
        self.assertNotEquals(account_0['CreditoMaximo'] , account_1['CreditoMaximo']) 
        self.assertNotEquals(account_0['ValorActivoValuacion'] , account_1['ValorActivoValuacion']) 
        self.assertEquals(account_0['ClaveOtorgante'] , account_1['ClaveOtorgante']) 
        self.assertNotEquals(account_0['NombreOtorgante'] , account_1['CreditoMaximo']) 
        self.assertNotEquals(account_0['TipoResponsabilidad'] , account_1['CreditoMaximo']) 
        self.assertEquals(account_0['TipoCuenta'] , account_1['TipoCuenta']) 
        self.assertNotEquals(account_0['ClaveUnidadMonetaria'] , account_1['CreditoMaximo']) 
        self.assertEquals(account_0['NumeroPagos'] , account_1['NumeroPagos']) 
        self.assertEquals(account_0['FrecuenciaPagos'] , account_1['FrecuenciaPagos']) 
        self.assertEquals(account_0['MontoPagar'] , account_1['MontoPagar']) 
        self.assertEquals(account_0['Garantia'] , account_1['Garantia']) 
        self.assertEquals(account_0['PagoActual'] , account_1['PagoActual']) 
        self.assertEquals(account_0['FechaPeorAtraso'] , account_1['FechaPeorAtraso']) 
        self.assertEquals(account_0['TotalPagosReportados'] , account_1['TotalPagosReportados']) 
        self.assertNotEquals(account_10['LimiteCredito'] , account_1['LimiteCredito']) 
        self.assertEquals(account_10['SaldoVencidoPeorAtraso'] , account_1['SaldoVencidoPeorAtraso']) 
        
    def test_4_xml_to_dict_validate_consultas_efectuadas(self):
        r1 = xml_to_dict(self.resp_4.data)
        response = self.extract_main_headers(r1)
        key_to_extract = {'ConsultasEfectuadas'}
        values_extracted = self.find_keys(response['Persona'] , key_to_extract)
        key_to_extract = {'ConsultaEfectuada'}
        values_extracted = self.find_keys(values_extracted['ConsultasEfectuadas'] , key_to_extract)
        self.assertTrue(isinstance(list(values_extracted.items()), list))
        self.assertTrue( len(values_extracted['ConsultaEfectuada'])  == 12)
        
    def test_4_xml_to_dict_when_xml_is_empty(self):
        with self.assertRaises(Exception):
            data=""
            r1 = xml_to_dict(data)
                
    def test_4_xml_to_dict_when_xml_is_none(self):
        with self.assertRaises(Exception):
            data=None
            r1 = xml_to_dict(data)
    
    
    
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Test_FileReader))
    runner = unittest.TextTestRunner()
    runner.run(suite)
    # unittest.main()
