import requests
import json
from utils import default
import os










class CSGO():
  def __init__(self):
    self.version = 'v2.0'
    config = default.config()
    print("Catching pesky bugs")
    self.key = config["TRNKEY"]
    
    if self.key == "":
      self.key = input("Please Enter A Valid API Key to Continue")        # This checks to see if the API key was entered into the config.json file
    else:                                                                         # If not you will have to enter it manually.
      self.key = self.key
 
    with open('temp.json', "r") as f:
      print("fucking bugs")
      fl = json.load(f)
      self.id = f1['SteamID']
      
    

    
    
    
      
        
        
      
    self.url = f'https://public-api.tracker.gg/v2/csgo/standard/profile/steam/{self.id}'
    self.headers = {                            # headers
    "Accept": "application/json",
    "Accept-Encoding": "gzip",
    "TRN-Api-Key": self.key
}
    
  def main(self, filename = 'parseddata.json'):  
    resp = requests.get(self.url, headers=self.headers) #Calling the headers
    rcode = resp.status_code
    rcode = 200     #If HTTP code is not 200, you will not have access to the API server, simple.
    while True:       #May aswell use a while loop to not crash the code when a Non-200 HTTP code flags up
      try:
        print(resp.status_code)
        break
      except exception as e:
        print(e)
        continue
      else:
        print(resp.status_code)
        continue
      
             
    data = resp.text
    parsed = json.loads(data)
    
   
    if 'data' not in parsed:
      raise ValueError('Either the account has no avaliable CSGO data OR the Steam account owner has set its privacy to private')
      

    else:
      prefix = parsed["data"]["segments"][0]["stats"]

    
      # Misc 
    tp = parsed["data"]["segments"][0]["stats"]["timePlayed"]["displayValue"]
    dmg = parsed["data"]["segments"][0]["stats"]["damage"]["displayValue"]
    m = parsed["data"]["segments"][0]["stats"]["moneyEarned"]["displayValue"]
    score = parsed["data"]["segments"][0]["stats"]["score"]["displayValue"]
    GamePlayed = prefix["matchesPlayed"]["displayValue"]
    
    # Kill related
    kd = parsed["data"]["segments"][0]["stats"]["kd"]["displayValue"]     # Actual values
    kills = parsed["data"]["segments"][0]["stats"]["kills"]["displayValue"]
    shot_acc = prefix["shotsAccuracy"]["displayValue"]
    
    #Death related
    death = parsed["data"]["segments"][0]["stats"]["deaths"]["displayValue"]
    
    
    
   
    # Meta Game Info
    MVP = prefix["mvp"]["displayValue"]
    Win = prefix["wins"]["displayValue"]
    loss = prefix["losses"]["displayValue"]
    bombp = prefix["bombsPlanted"]["displayValue"]
    bombd = prefix["bombsDefused"]["displayValue"]
    rplayed = prefix["roundsPlayed"]["displayValue"]
    rwon = prefix["roundsWon"]["displayValue"]
    HSPcT = prefix["headshotPct"]["displayValue"]
    
    
    
    types =  {
     
      "killRelated": [ 
         {
          "kill": kills,
          "ratio": kd,
          "shotacc": shot_acc,
          "SteamID": self.id
          
          }             ],
    
        "miscData": [
          {
          "timePlayed": tp,
          "damageGiven": dmg,
          "moneyEarned": m,
          "score": score,
          "gamePlayed": GamePlayed       
          } ],
      "metaData": [
        {
          "MvP": MVP,
          "Wins": Win,
          "Losses": loss,
          "BombsPlanted": bombp,
          "BombsDefused": bombd,
          "RoundsPlayed": rplayed,
          "RoundsWon": rwon, 
          "HeadshotPercentage": HSPcT
          
        }
      ]
      
}
    
    with open(filename, 'w') as t:
      json.dump(types, t, sort_keys=True, indent = 4)   
    os.system('python flasktest.py')
    
    
              
    
    
    
if __name__ == '__main__':
  c = CSGO()
  c.main()
  