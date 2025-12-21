from flask import Flask, request, jsonify
from flask_cors import CORS
from amadeus_api import get_flights, get_locations

app = Flask(__name__)
CORS(app)

@app.route("/flights", methods=['GET'])
def flights():
    try: 
        origin = request.args.get('origin', '')
        destination = request.args.get('destination', '')
        departure_date = request.args.get('departure_date', '')
        
        if origin == '' or destination == '' or departure_date == '':
            return jsonify({"Error": f"Not all parameters provided"}), 400
        
        flights = get_flights(origin=origin, destination=destination, departure_date=departure_date )
        
        return jsonify(flights)
    
    except KeyError as error: 
        return jsonify({"Error": f"Something went wrong with your request: {error}"}), 500
    
@app.route("/locations", methods=['GET'])
def locations():
    try:
        keyword = request.args.get('keyword', '')
        
        if keyword == '':
            return jsonify({"Error": f"Not all parameters provided"}), 400
        
        locations = get_locations(keyword=keyword)
        
        return jsonify(locations)
        
    except KeyError as error: 
        return jsonify({"Error": f"Something went wrong with your request: {error}"}), 500

if __name__ == "__main__":
    app.run(debug=True)