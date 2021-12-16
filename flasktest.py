from flask import Flask, render_template, Markup, request, url_for, redirect
import json
import requests
import sys
from utils import default
from flask_classful import FlaskView, route
from flask.logging import default_handler
import os







sys.path.append('/')

app = Flask(__name__, template_folder='templates', static_folder='static')




def page_not_found(e):
  return render_template('404.html'), 404     # error handler



class Flasky(FlaskView):
  

  
  
  @route('/', methods=['GET', 'post'])
  def index_post(self):
    text = request.form.get('text','')
    
    jsontext = {
      "SteamID": f"{text}"
    }
    with open('temp.json', 'w') as zxy:
      xyz = json.dump(jsontext, zxy)
      
      
      os.system('python index.py')
      
    
      return render_template('input.html')
      
    
    



  @route('/test')
  def tests(self, filename = 'parseddata.json'):
    
      with open(filename) as json_filez:
        dataz = json.load(json_filez)
        for i in dataz["killRelated"]:
          idz = i["SteamID"]
          pkills = i["kill"]
          pshotsacc = i["shotacc"]
          ratio = i["ratio"]
        for x in dataz["miscData"]:
          timeplayed = x["timePlayed"]
          dg = x["damageGiven"]
          moneyearnt = x["moneyEarned"]
          score = x["score"]
          gamesp = x["gamePlayed"]
          
        for z in dataz["metaData"]:
          planted = z["BombsPlanted"]
          defused = z["BombsDefused"]
          wins = z["Wins"]
          mvp = z["MvP"]
          HSPC = z["HeadshotPercentage"]
          RoundsPlayed = z["RoundsPlayed"]
          RoundsWon = z["RoundsWon"]
          loss = z["Losses"]
          
          
        
          
          
        
      
      
     
    
      

      return render_template('index.html', exit=idz, kills=pkills, 
                             kds=ratio, shoota=pshotsacc, tp=timeplayed, 
                             dg=dg, gp=gamesp, MoneyEarned=moneyearnt,score=score, 
                             planted=planted, defused=defused, mvp=mvp, 
                             hs=HSPC, roundsplayed=RoundsPlayed, roundswon=RoundsWon,
                             loss=loss                         
                            )



  @route('/contact')
  def contact(self):
    return f"Contact Page Debug" 
  
  





Flasky.register(app,route_base = '/')
app.register_error_handler(404, page_not_found)
app.logger.removeHandler(default_handler)


if __name__ == "__main__":
  app.run(debug='True', host='0.0.0.0', port=3000)