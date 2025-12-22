from quart import Quart, request, jsonify
from quart_cors import cors
from quart_schema import QuartSchema, validate_querystring, validate_response
from dataclasses import dataclass
from amadeus_api import get_flights, get_locations
from amadeus import ResponseError
import json
"""
This script sets up a Quart web server with two endpoints: /flights and /locations.
The /flights endpoint retrieves flight information based on origin, destination, and departure date parameters.
The /locations endpoint retrieves available flight locations based on a keyword parameter.
"""

app = Quart(__name__)
app = cors(app,  allow_origin="*") #http://localhost:3000

# Quart-Schema for documentation
QuartSchema(
    app,
    title="Flight Search API",
    version="1.0.0",
    description="API para buscar vuelos y ubicaciones usando Amadeus API"
)

# Models for validation and documentation 
@dataclass
class FlightsQuery:
    """Search Flight parameters"""
    origin: str
    destination: str
    departure_date: str

@dataclass
class LocationsQuery:
    """Search Locations parameters"""
    keyword: str

@dataclass
class ErrorResponse:
    """Error response"""
    Error: str


@app.route("/flights", methods=['GET'])
@validate_querystring(FlightsQuery)
async def flights(query_args: FlightsQuery) -> tuple:
    """
    Search for available flights
    
    Searches flights from an origin to a specific destination
    
    Args:
        origin: IATA code of origin airport (e.g: BKK, MEX)
        destination: IATA code of destination airport (e.g: SFO, JFK)
        departure_date: Departure date in YYYY-MM-DD format
    
    Returns:
        List of available flights with their details
    """
    try: 
        origin: str = query_args.origin
        destination: str = query_args.destination
        departure_date: str = query_args.departure_date
        
        if not origin or not destination or not departure_date:
            return jsonify({"Error": "Not all parameters provided"}), 400
        
        flights = await get_flights(origin=origin, destination=destination, departure_date=departure_date)
        
        return jsonify(flights), 200
    
    except ResponseError as error:

        data_error = json.loads(error.response.body) if isinstance(error.response.body, str) else error.response.body
        
        return jsonify({"Error":f"{data_error["errors"][0]["title"]} {data_error["errors"][0]["detail"]}"}), error.response.status_code
        
    except KeyError as error: 
        return jsonify({"Error": f"Something went wrong with your request: {error}"}), 500
    
    except Exception as e:
        return jsonify({"error": "Internal Server Error"}), 500
    
@app.route("/locations", methods=['GET'])
@validate_querystring(LocationsQuery)
async def locations(query_args: LocationsQuery) -> tuple:
    """
    Search for available locations
    
    Searches available airports and cities based on a keyword.
    
    Args:
        keyword: Keyword to search locations (minimum 1 character)
    
    Returns:
        Dictionary with IATA codes and location names
    """
    try:
        keyword: str = query_args.keyword
        
        if not keyword:
            return jsonify({"Error": "Not all parameters provided"}), 400
        
        locations = await get_locations(keyword=keyword)
        
        return jsonify(locations), 200
    
    except ResponseError as error:

        data_error = json.loads(error.response.body) if isinstance(error.response.body, str) else error.response.body
        
        return jsonify({"Error":f"{data_error["errors"][0]["title"]} {data_error["errors"][0]["detail"]}"}), error.response.status_code
        
    except KeyError as error: 
        return jsonify({"Error": f"Something went wrong with your request: {error}"}), 500
    
    except Exception as e:
        return jsonify({"error": "Internal Server Error"}), 500
    

if __name__ == "__main__":
    app.run(debug=True)