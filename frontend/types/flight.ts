export interface Segment {
    departureAirport: string;
    arrivalAirport: string;
    airline: string;
    flightNumber: string;
}

export interface Itinerary {
    segments: Segment[];
}

export interface FlightData {
    price: string;
    id: string;
    itineraries: Itinerary[];
}

export interface FlightCardProps {
    flight: FlightData;
}