#!/Users/alarcon/opt/anaconda3/bin/python3
from ConfigHandler import ConfigHandler


def main():
    #Getting the config information from a config file
    config = ConfigHandler();
    config.read_file()
    print("Parameters.....")
    print("Path: {} ".format(config.file_path_config))
    print("Coin: {} ".format(config.crypto_coins))
    print("excell: {}".format(config.excell_path))


if __name__ == "__main__":
    main()
