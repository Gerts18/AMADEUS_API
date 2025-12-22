export interface FlightData {
    price: string;
    id: string;
    "0firstFlightDepartureAirport": string;
    "0firstFlightAirline": string;
    "0firstFlightNumber": string;
    "0firstFlightArrivalAirport": string;
    "0secondFlightDepartureAirport"?: string;
    "0secondFlightAirline"?: string;
    "0SecondFlightNumber"?: string;
    "0secondFlightArrivalAirport"?: string;
}

export interface FlightCardProps {
    flight: FlightData;
}