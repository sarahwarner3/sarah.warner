#------FLIGHT DEALS TRACKER------#

#--.env--#
SHEETY_USERNAME = "sarahwaXXXX"
SHEETY_PW = "heliXXXX"

API_KEY = "5PUQsv9O29douYYGyHbj0WeGp8KdXXXX"
API_SECRET = "dF9yxNxAHZP2XXXX"

TWILIO_SID = "ACc9dbdbaca9a635ed7e91819dca50XXXX"
TWILIO_AUTH_TOKEN = "7e1a3c5d87361380d896e3bb1f5fXXXX"
TWILIO_VIRTUAL_NUMBER = "+1866775XXXX"
TWILIO_VERIFIED_NUMBER = "+715347XXXX"

EMAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
EMAIL = "swarXXXX@gmail.com"
PW = "apht ulps hfnm XXXX"

#--flight_data.py--#
class FlightData:
    def __init__(self, price, origin_airport, destination_airport, out_date, return_date, stops):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
        self.stops = stops

def find_cheapest_flight(data):
    if data is None or not data['data']:
        print("No flight data")
        return FlightData("N/A", "N/A", "N/A" ,"N/A", "N/A", "N/A")

    first_flight = data['data'][0]
    lowest_price = float(first_flight["price"]["grandTotal"])
    nr_stops = len(first_flight["itineraries"][0]["segments"])-1
    origin = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
    destination = first_flight["itineraries"][0]["segments"][nr_stops]["arrival"]["iataCode"]
    out_date = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
    return_date = first_flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]

    cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date, nr_stops)

    for flight in data["data"]:
        price = float(flight["price"]["grandTotal"])
        if price < lowest_price:
            lowest_price = price
            origin = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
            destination = flight["itineraries"][0]["segments"][nr_stops]["arrival"]["iataCode"]
            out_date = flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
            return_date = flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
            cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date, nr_stops)
            print(f"Lowest price to {destination} is £{lowest_price}")

    return cheapest_flight

#--flight_search.py--#
import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"

class FlightSearch:
    def __init__(self):
        self.api_key = os.environ["API_KEY"]
        self.api_secret = os.environ["API_SECRET"]
        self.token = self.get_new_token()

    def get_new_token(self):
        header = {'Content-Type': 'application/x-www-form-urlencoded'}
        body = {
            'grant_type': 'client_credentials',
            'client_id': self.api_key,
            'client_secret': self.api_secret
        }
        response = requests.post(url = TOKEN_ENDPOINT, headers = header, data = body)
        print(f"Your token is {response.json()['access_token']}")
        print(f"Your token expires in {response.json()['expires_in']} seconds")
        return response.json()['access_token']

    def get_destination_code(self, city_name):
        print(f"Using this token to get destination {self.token}")
        headers = {"Authorization": f"Bearer {self.token}"}
        query = {
            "keyword": city_name,
            "max": "2",
            "include": "AIRPORTS",
        }
        response = requests.get(
            url=IATA_ENDPOINT,
            headers=headers,
            params=query
        )

        print(f"Status code {response.status_code}. Airport IATA: {response.text}")
        try:
            code = response.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}.")
            return "Not Found"

        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time, is_direct = True):
        headers = {"Authorization": f"Bearer {self.token}"}
        query = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true" if is_direct else "false",
            "currencyCode": "GBP",
            "max": "10",
        }

        response = requests.get(
            url=FLIGHT_ENDPOINT,
            headers=headers,
            params=query,
        )

        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print("There was a problem with the flight search.\n"
                  "For details on status codes, check the API documentation:\n"
                  "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api"
                  "-reference")
            print("Response body:", response.text)
            return None

        return response.json()

#--data_manager.py--#
from pprint import pprint
import requests
import os
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

sheet_endpoint = "https://api.sheety.co/6de42adce96c3725bc80e1dff8e7ce40/flightDeals/prices"
sheet_users_endpoint = "https://api.sheety.co/6de42adce96c3725bc80e1dff8e7ce40/flightDeals/users"

class DataManager:
    def __init__(self):
        self.user = os.environ["SHEETY_USERNAME"]
        self.password = os.environ["SHEETY_PW"]
        self.authorization = HTTPBasicAuth(self.user, self.password)
        self.destination_data ={}
        self.customer_data = {}

    def get_destination_data(self):
        response = requests.get(url = sheet_endpoint)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url = f"{sheet_endpoint}/{city['id']}", json = new_data)
            print(response.text)

    def get_customer_emails(self):
        response = requests.get(url=sheet_users_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data

#--notification_manager.py--#
import os
import smtplib
from twilio.rest import Client

def __init__(self):
    # Retrieve environment variables only once
    self.smtp_address = os.environ["EMAIL_PROVIDER_SMTP_ADDRESS"]
    self.email = os.environ["MY_EMAIL"]
    self.email_password = os.environ["MY_EMAIL_PASSWORD"]
    self.twilio_virtual_number = os.environ["TWILIO_VIRTUAL_NUMBER"]
    self.twilio_verified_number = os.environ["TWILIO_VERIFIED_NUMBER"]
    self.client = Client(os.environ['TWILIO_SID'], os.environ["TWILIO_AUTH_TOKEN"])
    self.connection = smtplib.SMTP(os.environ["EMAIL_PROVIDER_SMTP_ADDRESS"])

def send_sms(self, message_body):
    message = self.client.messages.create(
        from_=self.twilio_virtual_number,
        body=message_body,
        to=self.twilio_verified_number
    )
    print(message.sid)

def send_emails(self, email_list, email_body):
    with self.connection:
        self.connection.starttls()
        self.connection.login(self.email, self.email_password)
        for email in email_list:
            self.connection.sendmail(
                from_addr=self.email,
                to_addrs=email,
                msg=f"Subject:New Low Price Flight!\n\n{email_body}".encode('utf-8')
            )

#--main.py--#
from data_manager import DataManager
from datetime import datetime, timedelta
import time
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager


data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "SAN"

for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        time.sleep(2)
print(f"sheet_data:\n {sheet_data}")

data_manager.destination_data = sheet_data
data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    print(f"Getting flights for {destination}")
    flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    cheapest_flight = find_cheapest_flight(flights)
    print(f"{destination['city']}: ${cheapest_flight.price}")

    if cheapest_flight.price == "N/A":
        print(f"No direct flight to {destination['city']}. Looking for indirect flights...")
        stopover_flights = flight_search.check_flights(
            ORIGIN_CITY_IATA,
            destination["iataCode"],
            from_time=tomorrow,
            to_time=six_month_from_today,
            is_direct=False
        )
        cheapest_flight = find_cheapest_flight(stopover_flights)
        print(f"Cheapest indirect flight price is: £{cheapest_flight.price}")

    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        if cheapest_flight.stops == 0:
            message = f"Low price alert! Only GBP {cheapest_flight.price} to fly direct "\
                      f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "\
                      f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        else:
            message = f"Low price alert! Only GBP {cheapest_flight.price} to fly "\
                      f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "\
                      f"with {cheapest_flight.stops} stop(s) "\
                      f"departing on {cheapest_flight.out_date} and returning on {cheapest_flight.return_date}."

        print(f"Check your email. Lower price flight found to {destination['city']}!")

        notification_manager.send_emails(email_list=customer_email_list, email_body=message)

