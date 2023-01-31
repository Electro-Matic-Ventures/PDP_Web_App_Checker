class SplitPartNumber:
    
    pdp: str
    type_: str
    certificate: str
    language: str
    voltage: str
    main_breaker: str
    small_breakers: str
    large_breakers: str
    isolation_transformer: str
    phase_transformer: str
    feed: str
    
    def __init__(
        self,
        pdp:str='',
        type_:str='',
        certificate:str='',
        language:str='',
        voltage:str='',
        main_breaker:str='',
        small_breakers:str='',
        large_breakers:str='',
        isolation_transformer:str='',
        phase_transformer:str='',
        feed:str=''
    ):
        self.pdp = pdp
        self.type_ = type_
        self.certificate = certificate
        self.language = language
        self.voltage = voltage
        self.main_breaker = main_breaker
        self.small_breakers = small_breakers
        self.large_breakers = large_breakers
        self.isolation_transformer = isolation_transformer
        self.phase_transformer = phase_transformer
        self.feed = feed
        return
    
    def get(self, property_name:str)-> str:
        return getattr(self, property_name)
    
    def set_(self, property_name:str, value:str)-> None:
        setattr(self, property_name, value)
        
    def split(self, part_number:str)-> None:
        indices = SplitPartNumber(
            pdp= '3',
            type_= '1',
            certificate = '1',
            language= '1',
            voltage= '1',
            main_breaker='1',
            small_breakers= '2',
            large_breakers= '1',
            isolation_transformer= '1',
            phase_transformer= '3',
            feed= '1'            
        )
        for key in indices.__dict__:
            value = int(indices.get(key))
            self.set_(key, part_number[:value])
            part_number = part_number[value:]
        return