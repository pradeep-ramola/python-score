import requests
import pyttsx3
import json
from datetime import datetime
engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speak(audio):
        engine.say(audio)
        engine.runAndWait()
    
class ScoreGet:
    
    def __init__(self):
        self.url_matches=" https://cricapi.com/api/matches/"
        self.get_score="https://cricapi.com/api/cricketScore/"
        self.apikey="EfVcqRJIAAaQzQI5B0I0M5Af3rI2"
        self.unique_id=""

    def get_unique_id(self):
        uri_params={"apikey":self.apikey}
        resp=requests.get(self.url_matches,params=uri_params) 
        resp_dict=resp.json()
        uid_found=0

        for i in resp_dict['matches']:
            if(i['team-1']=="India" or i['team-2']=="India" and i['matchStarted']):
                today=datetime.today().strftime('%Y-%m-%d')
                # print(today)
                if today == i['date'].split("T")[0]:
                    self.unique_id=i['unique_id']
                    # print(self.unique_id)
                    uid_found=1
                    break
        if not uid_found:
            self.unique_id=-1
            
        send_data=self.get_scurrent(self.unique_id)
        print(send_data)   
        speak("Welcome back sir ") 
        speak(send_data)
             
               
    def get_scurrent(self,unique_id):
        data=""
        if unique_id==-1:
            data="No matches of India Today :()"
        else:
            uri_params={"apikey":self.apikey,"unique_id":unique_id}
            resp=requests.get(self.get_score,params=uri_params)    
            data_json=resp.json()
            try:
                data="Here is the score : \n"+data_json['stat']+"\n"+data_json['score']
            except KeyError as e:
                print(e)
        return data    




if __name__=="__main__":
    s=ScoreGet()
    s.get_unique_id()
