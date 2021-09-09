#!/Users/alarcon/opt/anaconda3/bin/python3
from pycoingecko import CoinGeckoAPI
from ConfigHandler import ConfigHandler
import openpyxl

def main():
    #Getting the config information from a config file
    config = ConfigHandler()
    config.read_INI_coins()
    print(".......... Parameters ...............")
    print("Path: {}  ".format(config.file_path_config))
    print("Coins: {} ".format(config.crypto_coins))
    print("excell: {}".format(config.excell_path))
    print(".....................................")

    cg = CoinGeckoAPI()
    data = cg.get_price(ids = config.crypto_coins , vs_currencies='eur')
    
    print(">>> loading excell book")
    excel_document = openpyxl.load_workbook(config.excell_path)
    sheet = excel_document.get_sheet_by_name('Cartera')

    print("")
    print("List values ...........................")
    for coin in config.crypto_coins:
        print (str(coin)+' : '+str(data[str(coin).lower()]['eur']))
        multiple_cells = sheet['K2':'R2']
        for row in multiple_cells:
            for cell in row:
                if (str(cell.value).lower() == (str(coin).lower())):
                    sheet[cell.column_letter+'3'].value = data[str(coin).lower()]['eur']
                    print(cell.value+' >> UPDATED')
                    break
        #        else:
        #            if(cnt_coin == config.crypto_coins.count())

        
    


    excel_document.save(config.excell_path)

if __name__ == "__main__":
    main()
