import json
import requests



########### Thanks to https://www.github.com/Alexflipnote for this snippet of code (adapted from his python bot source code) ###########

def config(filename: str = "config"):
    """ Fetch default config file """
    try:
        with open(f"{filename}.json", encoding='utf8') as data:
            return json.load(data)
    except FileNotFoundError:
        raise FileNotFoundError(f"Could Not find {filename}.json")
        
        
def temp(filename: str = "temp"):
    """ Fetch default config file """
    try:
        with open(f"{filename}.json", encoding='utf8') as data:
            return json.load(data)
    except FileNotFoundError:
        raise FileNotFoundError(f"Could Not find {filename}.json")
        
        
        
 
