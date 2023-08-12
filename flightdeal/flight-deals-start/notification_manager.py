import smtplib
from flight_data import FlightData


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def __init__(self, flight_data: FlightData) -> None:
        self.data = flight_data


    def call(self,city):

        with smtplib.SMTP("smtp.gmail.com") as connection:
            my_email = "zyaustinli@gmail.com"
            connection.starttls()
            connection.login(user=my_email, password = "kvgcvndqghhxvjmw")        
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                
                msg= f"Subject:Flight to {city} price lowered!!\n\n{self.data.flight_output}"
            )