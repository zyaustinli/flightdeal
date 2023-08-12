from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager
from pprint import pprint

data_manager = DataManager()
flight_search = FlightSearch()
flight_data = FlightData()
notification_manager = NotificationManager(flight_data)
sheet_data = data_manager.get_destination_data()




for row in sheet_data:
    if (row["iataCode"]) == "":
        row["iataCode"] = flight_search.update(row["city"])


#pprint(sheet_data)



for destination in sheet_data:
    price = flight_data.search(destination['iataCode'], destination['city']) 
    if price < destination['lowestPrice']:
        destination['lowestPrice'] = price
        notification_manager.call(destination['city'])

        

data_manager.destination_data = sheet_data
data_manager.update_destination_data() 
    


