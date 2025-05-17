from configparser import ConfigParser

def load_config(filename='database.ini', section='postgresql'):
    """Load configuration from a file."""
    parser = ConfigParser()
    parser.read(filename)
    
    db_config = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db_config[item[0]] = item[1]
    else:
        raise Exception(f'Section {section} not found in the {filename} file')
    
    return db_config

if __name__ == '__main__':
    config = load_config()
    print(config)
# This script loads database configuration from a .ini file.
# It uses the ConfigParser module to read the file and extract the necessary parameters.