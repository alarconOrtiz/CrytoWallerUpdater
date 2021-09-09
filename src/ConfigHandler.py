import configparser
import io

class ConfigHandler:
    def __init__(self):
        self.file_path_config = "config.ini"
        self.crypto_coins = list()
        self.excell_path  = "Cartera.xlsx" 
    
    def read_INI_coins(self):
        config = configparser.ConfigParser()
        config.read(self.file_path_config)
            
        #read al coin in config file
        index_coin = 1
        next_coin = True
        while next_coin : 
            try:
                coin = config.get('coins','coin{}'.format(index_coin))
                self.crypto_coins.append( coin )
                index_coin= index_coin + 1
            except Exception as e:
                if(type(e) == configparser.NoOptionError ):
                    next_coin = False
                else:
                    raise e
            