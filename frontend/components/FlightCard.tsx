interface FlightData {
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

interface FlightCardProps {
    flight: FlightData;
}

const FlightCard = ({ flight }: FlightCardProps) => {

    const hasSecondFlight = flight["0secondFlightDepartureAirport"] && flight["0secondFlightArrivalAirport"];

    return (
        <div className="max-w-sm min-w- w-full flex flex-col items-center">
            <div className="border-2 border-gray-400 bg-white rounded-b p-4 flex flex-col justify-between leading-normal">
                <div className="mb-2">

                    <p className="text-sm text-gray-600 flex items-center">
                        <svg className="fill-current text-gray-500 w-5 h-5 mr-2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                            <path d="M10 2c-.55 0-1 .45-1 1v3L3 8.5c-.45.3-.67.85-.5 1.35l.5 1.5c.12.35.45.6.82.6l5.18-1.5v5l-2 1.5v1.5l3-1 3 1v-1.5l-2-1.5v-5l5.18 1.5c.37 0 .7-.25.82-.6l.5-1.5c.17-.5-.05-1.05-.5-1.35L11 6V3c0-.55-.45-1-1-1z" />
                        </svg>
                        Flight Available
                    </p>

                    <div className="text-gray-900 font-bold text-xl mb-2">${flight.price}</div>
                    
                    <div className="flex flex-row gap-4 min-w-100">

                        {/* First Flight Segment */}
                        <div className="text-gray-700 text-base mb-3 flex-1">
                            <p className="font-semibold">Segment 1:</p>
                            <p>{flight["0firstFlightDepartureAirport"]} → {flight["0firstFlightArrivalAirport"]}</p>
                            <p className="text-sm">Airline: {flight["0firstFlightAirline"]} | Flight: {flight["0firstFlightNumber"]}</p>
                        </div>

                        {/* Second Flight Segment - Only if exists */}
                        {hasSecondFlight && (
                            <div className="text-gray-700 text-base flex-1">
                                <p className="font-semibold">Segment 2:</p>
                                <p>{flight["0secondFlightDepartureAirport"]} → {flight["0secondFlightArrivalAirport"]}</p>
                                <p className="text-sm">Airline: {flight["0secondFlightAirline"]} | Flight: {flight["0SecondFlightNumber"]}</p>
                            </div>
                        )}
                    

                    </div>


                </div>
            </div>
        </div>
    )
}

export default FlightCard