import os
import json
from dotenv import load_dotenv
from amadeus import Client, ResponseError

load_dotenv()

amadeus = Client(
    client_id=os.getenv('AMADEUS_CLIENT_ID'),
    client_secret=os.getenv('AMADEUS_CLIENT_SECRET'),
)


def get_flights():
    origin = "SYD"
    destination = "BKK"
    departure_date = '2025-12-20'
    
    filtered_flights = []
    
    parameters = {
        "originLocationCode": origin,
        "destinationLocationCode": destination,
        "departureDate": departure_date,
        "adults": 1,
    }
    
    try:
        search_flights = amadeus.shopping.flight_offers_search.get(**parameters)
        #print(json.dumps(search_flights.data[:1], indent= 4))
        
        for flight in search_flights.data:
            filtered_flights.append(parse_flight(flight))
        
    except ResponseError as error:
        return (error.response.body)
    
    return filtered_flights

def parse_flight(flight_data):
    flight = {}
    index = 0
    
    flight['price'] = flight_data['price']['total']
    flight['id'] = flight_data['id']
    
    for i in flight_data['itineraries']:
        
        if len(flight_data['itineraries'][index]['segments']) == 2: # both-ways
            
            flight[str(index) + "firstFlightDepartureAirport"] = flight_data['itineraries'][index]['segments'][0]['departure']['iataCode']
            
            flight[str(index) + 'firstFlightAirline'] = flight_data['itineraries'][index]['segments'][0]['carrierCode']
            
            flight[str(index) + 'firstFlightNumber'] = flight_data['itineraries'][index]['segments'][0]['number']
            
            flight[str(index) + 'firstFlightArrivalAirport'] = flight_data['itineraries'][index]['segments'][0]['arrival']['iataCode']
            
            flight[str(index) + 'secondFlightDepartureAirport'] = flight_data['itineraries'][index]['segments'][1]['departure']['iataCode']
            
            flight[str(index) + 'secondFlightAirline'] = flight_data['itineraries'][index]['segments'][1]['carrierCode']
            
            flight[str(index) + 'SecondFlightNumber'] = flight_data['itineraries'][index]['segments'][1]['number']
            
            flight[str(index) + 'secondFlightArrivalAirport'] = flight_data['itineraries'][index]['segments'][1]['arrival']['iataCode']
            
            
            
        elif len(flight_data['itineraries'][index]['segments']) == 1: # One-way
            flight[str(index) + "firstFlightDepartureAirport"] = flight_data['itineraries'][index]['segments'][0]['departure']['iataCode']
            
            flight[str(index) + 'firstFlightAirline'] = flight_data['itineraries'][index]['segments'][0]['carrierCode']
            
            flight[str(index) + 'firstFlightNumber'] = flight_data['itineraries'][index]['segments'][0]['number']
            
            flight[str(index) + 'firstFlightArrivalAirport'] = flight_data['itineraries'][index]['segments'][0]['arrival']['iataCode']
        
        index +=1
        
    return flight

if __name__ == "__main__":
  print(json.dumps(get_flights(), indent = 4))