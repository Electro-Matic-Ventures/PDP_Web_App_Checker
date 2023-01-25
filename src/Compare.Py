from FileLocations import FileLocations
from WritePartNumber import WritePartNumber
from ExcelData import ExcelData
from WebAppData import WebAppData

class Compare:
    
    __file_locations: FileLocations
    __excel_data: ExcelData
    __web_app_data: WebAppData
    
    def __init__(self, file_locations:FileLocations):
        self.__file_locations = file_locations
        self.__write_pn_to_excel_file()
        return
    
    def __write_pn_to_excel_file(self)-> None:
        part_number = self.__get_pn_from_file_name()
        w = WritePartNumber(self.__file_locations.excel, part_number)
        return
    
    def __get_pn_from_file_name(self)-> str:
        split_path = self.__file_locations.web_app.split('/')
        file_name = split_path[-1]
        part_number = file_name[:file_name.find('_BOM')]
        return part_number
    
locations = FileLocations()
locations.excel = 'C:/users/jrmachado/downloads/Ford GVOSS PDP Configurator Sub Builds 2023 DESAI pricing 10-6-22 (1).xlsx'
locations.web_app = 'C:/users/jrmachado/downloads/PDPCC3D4150N15AT_BOM.csv'
c = Compare(locations)