from flask import Flask, request, jsonify
from amadeus_api import get_flights, get_locations

app = Flask(__name__)

@app.route("/locations", methods=['GET'])
def locations():
    try: 
        origin = request.args.get('origin', '')
        destination = request.args.get('destination', '')
        departure_date = request.args.get('departure_date', '')
        
        if origin == '' or destination == '' or departure_date == '':
            return jsonify({"Error": f"Not all parameters provided"}), 200
        
        flights = get_flights(origin=origin, destination=destination, departure_date=departure_date )
        
        return flights
    
    except KeyError as error: 
        return jsonify({"Error": f"Something went wrong with your request: {error}"}), 200

if __name__ == "__main__":
    app.run(debug=True)