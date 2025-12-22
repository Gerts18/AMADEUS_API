import os
import json
from dotenv import load_dotenv
from amadeus import Client, Location
import asyncio
"""
This script is the one that handles all the requests to the Amadeus API and its logic.
"""

load_dotenv()

amadeus = Client(
    client_id=os.getenv('AMADEUS_CLIENT_ID'),
    client_secret=os.getenv('AMADEUS_CLIENT_SECRET'),
)

async def get_flights(origin: str = "BKK", destination:str= "SFO", departure_date:str = '2025-12-23') -> list[dict]:
    """
    Retrieve available flight offers from Amadeus API based on search criteria.
    """
    filtered_flights:list = []
    
    parameters = {
        "originLocationCode": origin,
        "destinationLocationCode": destination,
        "departureDate": departure_date,
        "adults": 1,
    }
    
    
    search_flights = await asyncio.to_thread(
        amadeus.shopping.flight_offers_search.get, 
        **parameters
    )
    
    #print(json.dumps(search_flights.data[:3], indent= 4))
    
    for flight in search_flights.data:
        filtered_flights.append(parse_flight(flight))
        
    return filtered_flights


def parse_flight(flight_data: dict) -> dict:
    """ 
    Parse and transform raw flight data from Amadeus API into a simplified format.
    """
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


async def get_locations(keyword: str = 'r') -> dict:
    """
    Search for airports and cities available for flight bookings using a keyword.
    """
    location_list: list = []
    
    locations = await asyncio.to_thread(
            amadeus.reference_data.locations.get,
            keyword = keyword,
            subType = Location.ANY
    )
    
    locations_list = parse_locations(locations.data)
    
    return locations_list


def parse_locations(locations_data: list) -> dict:
    """
    Transform raw location data from Amadeus API into a simplified dictionary format.
    
    """
    locations_dict: dict = {}
    
    for location in locations_data:
        iata_code = location['iataCode']
        locations_dict[iata_code] = location['name']  
    
    return locations_dict 
    

if __name__ == "__main__":
  print(asyncio.run(get_locations()))