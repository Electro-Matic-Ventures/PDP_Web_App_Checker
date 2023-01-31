from FileLocations import FileLocations
from WritePartNumber import WritePartNumber
from ReadExcelData import ReadExcelData
from pandas import DataFrame

class Compare:
    
    __file_locations: FileLocations
    __part_number: str
    __excel_data: DataFrame
    __web_app_data: DataFrame
    
    def __init__(self, file_locations:FileLocations):
        self.__file_locations = file_locations
        self.__part_number = self.__get_pn_from_file_name()
        self.__write_pn_to_excel_file()
        self.__excel_data = self.__get_excel_data()
        return
    
    def __write_pn_to_excel_file(self)-> None:
        WritePartNumber(self.__file_locations.excel, self.__part_number)
        return
    
    def __get_excel_data(self)-> DataFrame:
        return ReadExcelData(self.__file_locations.excel, self.__part_number).data
    
    def __get_pn_from_file_name(self)-> str:
        split_path = self.__file_locations.web_app.split('/')
        file_name = split_path[-1]
        part_number = file_name[:file_name.find('_BOM')]
        return part_number
    