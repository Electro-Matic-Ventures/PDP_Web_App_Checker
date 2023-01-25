from openpyxl import load_workbook
from SplitPartNumber import SplitPartNumber
from WorkBookAddresses import WorkbookAddresses


class WritePartNumber:
    
    __file_name: str
    __split_part_number: SplitPartNumber
    __addresses: WorkbookAddresses
    
    def __init__(self, file_name:str, part_number:str):
        self.__split_part_number = self.__split_part_number(part_number)
        self.__addresses = WorkbookAddresses()
        self.__file_name = file_name
        self.__write()
        return
    
    def __write(self)-> None:
        work_book = load_workbook(self.__file_name)
        work_sheet = work_book[self.__addresses.cpdp_400.sheet_name]
        for key in self.__split_part_number.__dict__:
            value = self.__split_part_number.get(key)
            address = self.__addresses.cpdp_400.cell_addresses.get(key)
            work_sheet[address] = value
        work_book.save(self.__file_name)
        return
    
    def __split_part_number(self, part_number:str)-> SplitPartNumber:
        split_pn = SplitPartNumber()
        split_pn.split(part_number)
        return split_pn