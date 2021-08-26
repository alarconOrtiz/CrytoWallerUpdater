import ConfigParser
import io

class ConfigHandler:
    def __init__(self):
        self.file_path_config = "config.ini"
        self.crypto_coins = {}
        self.excell_path  = "crytoWallet.ex" 
    
    def read_file():
        with open(self.file_path_config) as f:
            config_file = f.read()
            config = ConfigParser.RawConfigParser(allow_no_value=True)
            config.readfp(io.BytesIO(self.file_path_config))
            
            #read al coin in config file
            index_coin = 1
            next_coin = True
            while next_coin : 
                try:
                    coin = config.get('cryptocoin','coin{}'.format(index_coin))
                    self.crypto_coins.append( coin )
                    index_coin= index_coin + 1
                except
                    next_coin = False
            #read paths
                pass
    