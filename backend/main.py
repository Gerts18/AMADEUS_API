from quart import Quart, request, jsonify
from quart_cors import cors
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


@app.route("/flights", methods=['GET'])
async def flights() -> list:
    try: 
        origin: str = request.args.get('origin', '')
        destination: str = request.args.get('destination', '')
        departure_date: str = request.args.get('departure_date', '')
        
        if origin == '' or destination == '' or departure_date == '':
            return jsonify({"Error": f"Not all parameters provided"}), 400
        
        flights = await get_flights(origin=origin, destination=destination, departure_date=departure_date )
        
        return jsonify(flights)
    
    except ResponseError as error:

        data_error = json.loads(error.response.body) if isinstance(error.response.body, str) else error.response.body
        
        return jsonify({"Error":f"{data_error["errors"][0]["title"]} {data_error["errors"][0]["detail"]}"}), error.response.status_code
        
    except KeyError as error: 
        return jsonify({"Error": f"Something went wrong with your request: {error}"}), 500
    
    except Exception as e:
        return jsonify({"error": "Internal Server Error"}), 500
    
@app.route("/locations", methods=['GET'])
async def locations() -> dict:
    try:
        keyword: str = request.args.get('keyword', '')
        
        if keyword == '':
            return jsonify({"Error": f"Not all parameters provided"}), 400
        
        locations = await get_locations(keyword=keyword)
        
        return jsonify(locations)
    
    except ResponseError as error:

        data_error = json.loads(error.response.body) if isinstance(error.response.body, str) else error.response.body
        
        return jsonify({"Error":f"{data_error["errors"][0]["title"]} {data_error["errors"][0]["detail"]}"}), error.response.status_code
        
    except KeyError as error: 
        return jsonify({"Error": f"Something went wrong with your request: {error}"}), 500
    
    except Exception as e:
        return jsonify({"error": "Internal Server Error"}), 500
    

if __name__ == "__main__":
    app.run(debug=True)