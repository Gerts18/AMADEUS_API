import { FlightCardProps } from "../types/flight";

const FlightCard = ({ flight }: FlightCardProps) => {

    return (
        <div className="max-w-2xl w-full flex flex-col items-center">
            <div className="border-2 border-gray-400 bg-white rounded-b p-4 flex flex-col justify-between leading-normal w-full">
                <div className="mb-2">

                    <p className="text-sm text-gray-600 flex items-center">
                        <svg className="fill-current text-gray-500 w-5 h-5 mr-2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                            <path d="M10 2c-.55 0-1 .45-1 1v3L3 8.5c-.45.3-.67.85-.5 1.35l.5 1.5c.12.35.45.6.82.6l5.18-1.5v5l-2 1.5v1.5l3-1 3 1v-1.5l-2-1.5v-5l5.18 1.5c.37 0 .7-.25.82-.6l.5-1.5c.17-.5-.05-1.05-.5-1.35L11 6V3c0-.55-.45-1-1-1z" />
                        </svg>
                        Flight Available
                    </p>

                    <div className="text-gray-900 font-bold text-xl mb-2">${flight.price}- ${flight.currency} </div>
                    
                    {flight.itineraries.map((itinerary, itineraryIndex) => (
                        <div key={itineraryIndex} className="mb-4">
                            <p className="font-bold text-gray-800 mb-2">Itinerary {itineraryIndex + 1}</p>
                            <div className="flex flex-row flex-wrap gap-3">
                                {itinerary.segments.map((segment, segmentIndex) => (
                                    <div key={segmentIndex} className="text-gray-700 text-base border-l-2 border-blue-500 pl-3">
                                        <p className="font-semibold">Segment {segmentIndex + 1}:</p>
                                        <p>{segment.departureAirport} → {segment.arrivalAirport}</p>
                                        <p className="text-sm">Airline: {segment.airline} | Flight: {segment.flightNumber}</p>
                                    </div>
                                ))}
                            </div>
                        </div>
                    ))}

                </div>
            </div>
        </div>
    )
}

export default FlightCard