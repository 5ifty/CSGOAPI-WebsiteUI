import json
import re


def parsing(filename = "tes.json"):
  with open(filename) as file:
    data = json.load(file)
    
    
    
    
  Allias = input("Please type in the Preffered Allias you entered before (caps sensitive): ")
  for i in data:
    if i['Preffered_Allias'] == Allias:
      print(i['SteamID'])
      print(i['Preffered_Allias'])
      break
      
    else:
      continue
    
     
    
    
    
    
    
parsing()