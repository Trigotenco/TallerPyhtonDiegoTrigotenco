import configparser
import sys

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config.ini')

    if ('Maximus' in config and 'basedatos' in config['Maximus'] and 'usuario' in config['Maximus'] and 'contrasennia' in config['Maximus']):

        bd = config['Maximus']['basedatos']
        user = config['Maximus']['usuario']
        password = config['Maximus']['contrasennia']

        print(f"Usuario: {user}")
        print(f"Contrasennia: {password}")
        print("-" * 30)

