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
    
    parameters = {
        "originLocationCode": origin,
        "destinationLocationCode": destination,
        "departureDate": departure_date,
        "adults": 1,
    }
    
    try:
        search_flights = amadeus.shopping.flight_offers_search.get(**parameters)
        #print(json.dumps(search_flights.data, indent= 4))
        
        for flight in search_flights.data:
            print(json.dumps(flight, indent = 4))
            print(
                f"""
                    
                """
            )
            break
        
    except ResponseError as error:
        print(error.response.body)


if __name__ == "__main__":
    get_flights()