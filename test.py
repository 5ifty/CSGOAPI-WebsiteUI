import json


a = input("Enter ID")
astr = str(a)
b = input("Enter user")
bstr = str(b)


def dumpfile(data, filename = "tes.json"):
  with open(filename,'w') as f:
        json.dump(data, f, indent=4)
      
      
with open("tes.json") as json_file:
  data = json.load(json_file)

  x = data['info']
  y = {
    "SteamID": astr,
    "Preffered_Allias": bstr
    }

  x.append(y)
  
  
  



dumpfile(data)