import configparser

class Config(object):
    __module__       = 'aes-service/config.py'
    __author__       = 'Rob Mitchell'
    __maintainer__   = 'Rob Mitchell'
    __email__        = 'rlmitchell@gmail.com'
    __version__      = '1.0.0'
    __version_date__ = '2020.06.06.1559ct'
    __status__       = 'personal use release'

    parser = None

    @staticmethod
    def get_parser( file_path ):
        if Config.parser is None:
            Config.parser = configparser.ConfigParser()
            Config.parser.read( file_path )
        return Config.parser

