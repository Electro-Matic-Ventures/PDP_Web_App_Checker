from ReadPageAddresses import ReadPageAddresses


class ReadBookAddresses:

    cpdp_400: ReadPageAddresses

    def __init__(self):
        self.cpdp_400 = self.__build_cpdp_400()
        return
    

    def __build_cpdp_400(self)-> ReadPageAddresses:
        cell_addresses = ['B','F']
        return ReadPageAddresses('400A CPDP', cell_addresses)       