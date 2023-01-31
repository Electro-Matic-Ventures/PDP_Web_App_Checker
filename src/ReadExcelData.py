from pandas import DataFrame, read_excel
from openpyxl import load_workbook
from ReadBookAddresses import ReadBookAddresses


class ReadExcelData:
    
    __file_name: str
    __part_number: str
    __addresses: ReadBookAddresses
    data: DataFrame
    
    def __init__(self, file_name:str, part_number:str):
        self.__file_name = file_name
        self.__part_number = part_number
        self.__addresses = ReadBookAddresses()        
        self.data = self.__read()
        return
    
    def __read(self)-> DataFrame:
        work_book = load_workbook(self.__file_name)
        work_sheet = work_book[self.__addresses.cpdp_400.sheet_name]
        test = work_sheet["B2:C99"]
        data_frame = DataFrame()
        # data_frame = read_excel(
        #     io=self.__file_name,
        #     sheet_name=self.__addresses.cpdp_400.sheet_name,
        #     index_col=0
        # )
        # header = data_frame.iloc[1]
        # data_frame = data_frame.iloc[2:]
        # data_frame.columns = header
        return data_frame