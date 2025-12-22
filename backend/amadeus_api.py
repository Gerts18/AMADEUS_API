import os
import json
from dotenv import load_dotenv
from amadeus import Client, ResponseError, Location
import asyncio
"""
This script is the one that handles all the requests to the Amadeus API and its logic.
"""

load_dotenv()

amadeus = Client(
    client_id=os.getenv('AMADEUS_CLIENT_ID'),
    client_secret=os.getenv('AMADEUS_CLIENT_SECRET'),
)

# Retrieve flights based on parameters send by the user
async def get_flights(origin: str = "BKK", destination:str= "SFO", departure_date:str = '2025-12-23') -> list[dict]:
    filtered_flights:list = []
    
    parameters = {
        "originLocationCode": origin,
        "destinationLocationCode": destination,
        "departureDate": departure_date,
        "adults": 1,
    }
    
    try:
        search_flights = await asyncio.to_thread(
            amadeus.shopping.flight_offers_search.get, 
            **parameters
        )
        
        #print(json.dumps(search_flights.data[:3], indent= 4))
        
        """ with open('flights_data.json', 'w', encoding='utf-8') as f:
            json.dump(search_flights.data, f, indent=4, ensure_ascii=False) """
        
        for flight in search_flights.data:
            filtered_flights.append(parse_flight(flight))
            
        return filtered_flights
        
    except ResponseError as error:
        data_error = json.loads(error.response.body) if isinstance(error.response.body, str) else error.response.body
        return {"title": data_error["errors"][0]["title"],"details": data_error["errors"][0]["detail"]}

# Parse the data of a flight
def parse_flight(flight_data: dict) -> dict:
    flight: dict = {}
    
    flight['price'] = flight_data['price']['total']
    flight['id'] = flight_data['id']
    flight['itineraries'] = []
    
    for itinerary in flight_data['itineraries']:
        segments_list = []
        
        for segment in itinerary['segments']:
            segments_list.append({
                'departureAirport': segment['departure']['iataCode'],
                'arrivalAirport': segment['arrival']['iataCode'],
                'airline': segment['carrierCode'],
                'flightNumber': segment['number']
            })
        
        flight['itineraries'].append({
            'segments': segments_list
        })
        
    return flight

# Retrieve locations availables for flights  
async def get_locations(keyword: str = 'r') -> dict:
    location_list: list = []
    
    try:
        locations = await asyncio.to_thread(
                amadeus.reference_data.locations.get,
                keyword = keyword,
                subType = Location.ANY
        )
        
        locations_list = parse_locations(locations.data)
        
        return locations_list
        
    except ResponseError as error:
        data_error = json.loads(error.response.body) if isinstance(error.response.body, str) else error.response.body
        return {"title": data_error["errors"][0]["title"],"details": data_error["errors"][0]["detail"]}

# Parses the data from an array of locations
def parse_locations(locations_data: list) -> dict:
    locations_dict: dict = {}
    
    for location in locations_data:
        iata_code = location['iataCode']
        locations_dict[iata_code] = location['name']  
    
    return locations_dict 
    

if __name__ == "__main__":
  print(asyncio.run(get_locations()))