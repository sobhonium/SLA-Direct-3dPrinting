
import configparser

def prepend_defalt_section():
    '''.ini files from prusa printers hove no default
    section in them. temporary I want to add a [DEFALT] sectoin
    to them and use it with ConfigParserTool'''
    
    # must change change .ini files in scr folder:


    # config = configparser.ConfigParser()
    # config['DEFAULT']