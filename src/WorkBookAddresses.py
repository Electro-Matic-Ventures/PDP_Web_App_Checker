from SplitPartNumber import SplitPartNumber
from WorkbookAddress import WorkbookAddress

class WorkbookAddresses:
    
    cpdp_400: WorkbookAddress
    
    def __init__(self):
        self.cpdp_400 = self.__build_cpdp_400()
        return
    
    def __build_cpdp_400(self)-> WorkbookAddress:
        cell_addresses = SplitPartNumber(
            pdp='B1',
            type_='C1',
            certificate='D1',
            language='E1',
            voltage='F1',
            main_breaker='G1',
            small_breakers='H1',
            large_breakers='J1',
            isolation_transformer='L1',
            phase_transformer='N1',
            feed='P1'
        )
        return WorkbookAddress('400A CPDP Config', cell_addresses)       