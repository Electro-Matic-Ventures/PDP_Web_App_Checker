class ReadPageAddresses:
    
    sheet_name: str
    cell_addresses: list 
        
    def __init__(self, sheet_name:str, cell_addresses:list):
        self.sheet_name = sheet_name
        self.cell_addresses = cell_addresses
        return