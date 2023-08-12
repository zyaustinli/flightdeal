import requests
from datetime import datetime
from pprint import pprint

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.destination_data = {}
        self.sheet_endpoint = "https://api.sheety.co/a00a2addea32a5df568027e749c8d078/flightDeals/prices"
    def get_destination_data(self):

        response = requests.get(url= self.sheet_endpoint)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_data(self):
        for city in self.destination_data:
            sheet_inputs = {
                "price": {
                "city": city["city"],
                "iataCode": city["iataCode"],
                "lowestPrice": city["lowestPrice"]
            }
            }
            response = requests.put(url= f"{self.sheet_endpoint}/{city['id']}", json = sheet_inputs)
            #print(response.text)



