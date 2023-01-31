from SplitPartNumber import SplitPartNumber


class ConfigurePageAddresses:
    
    sheet_name: str
    cell_addresses: SplitPartNumber 
        
    def __init__(self, sheet_name:str, cell_addresses:SplitPartNumber):
        self.sheet_name = sheet_name
        self.cell_addresses = cell_addresses
        return