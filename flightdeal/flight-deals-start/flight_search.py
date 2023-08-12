from datetime import datetime
import requests

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self) -> None:
        self.api_key = ''


    def update(self, city): 
        self.header = {
        "apikey" : self.api_key
        }
        self.query = {
            "term": city
        }
        location_endpoint = "https://tequila-api.kiwi.com"
        response = requests.get(url = f"{location_endpoint}/locations/query", headers=self.header, params=self.query)
        
        code=(response.json()["locations"][0]['code'])
        return code
            
          

    
