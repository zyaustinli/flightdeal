
import requests
from data_manager import DataManager
from datetime import datetime, timedelta

#leave between tmrw to 6 months
#round trips return between 7-28 days
#currnecy of price in GBP


class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self) -> None:
        pass

    def search(self, city, city_name):
        self.api_key = '0Wdo1dGipm1WDCI401xNW8Zxq6JDyxlL'

        self.header = {
        "apikey" : self.api_key
        }

        monthslater = datetime.now() + timedelta(180)



        self.query = {
             "fly_from": "SAN",
             "fly_to": city,
             "date_from": datetime.now().strftime('%d/%m/%Y'),
             "date_to": monthslater.strftime('%d/%m/%Y'),
             "nights_in_dst_from": 7,
             "nights_in_dst_to": 28,
             "curr": "USD"
        }


        location_endpoint = "https://tequila-api.kiwi.com"
        response = requests.get(url = f"{location_endpoint}/search", headers=self.header, params=self.query)
        try:
            data = response.json()['data'][0]
        except IndexError:
            print(f'No flights found for {city}')
            return None

        index = 0

        for i in range(len(data['route'])):
            if data["route"][i]["cityTo"]==city_name:
                index = i
            


        self.flight_output = {
            'price':data["price"],
            'origin_city':data["route"][0]["cityFrom"],
            'origin_airport':data["route"][0]["flyFrom"],
            'destination_city':data["route"][index]["cityTo"],
            'destination_airport':data["route"][index]["flyTo"],
            'out_date':datetime.utcfromtimestamp(int(data["route"][0]["dTime"])).strftime('%Y-%m-%d %H:%M:%S'),
            'return_date':datetime.utcfromtimestamp(int(data["route"][-1]["aTime"])).strftime('%Y-%m-%d %H:%M:%S'),
            'link':data['deep_link']
        }

       # print(flight_output)
        print(self.flight_output["destination_city"] + " $"+ str(self.flight_output['price']))

        return self.flight_output['price']


'''x = FlightData()
x.search("PAR", "Paris")'''