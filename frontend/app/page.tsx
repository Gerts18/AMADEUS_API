'use client'

import FlightCard from "@/components/FlightCard";
import SearchBar from "@/components/SearchBar";
import { useState } from "react";

export default function Home() {


  const [flights, setFlights] = useState([
    {
      "price": "226.82",
      "id": "1",
      "0firstFlightDepartureAirport": "SYD",
      "0firstFlightAirline": "OD",
      "0firstFlightNumber": "172",
      "0firstFlightArrivalAirport": "DPS",
      "0secondFlightDepartureAirport": "DPS",
      "0secondFlightAirline": "ID",
      "0SecondFlightNumber": "7637",
      "0secondFlightArrivalAirport": "DMK"
    },
    {
      "price": "239.56",
      "id": "2",
      "0firstFlightDepartureAirport": "SYD",
      "0firstFlightAirline": "VJ",
      "0firstFlightNumber": "86",
      "0firstFlightArrivalAirport": "SGN",
      "0secondFlightDepartureAirport": "SGN",
      "0secondFlightAirline": "VJ",
      "0SecondFlightNumber": "801",
      "0secondFlightArrivalAirport": "BKK"
    }
  ])

  const [form, setForm] = useState(
    {
      origin: "",
      destination: "",
      departure_date : "",
    }
  )

  const handleChange = (name: string, value: string) => {
    setForm(
      {
        ...form,
        [name] : value
      }
    )
  }

  return (
    <main>

      {/* Search engine for flights */}
      <section>

          <SearchBar 
            type = "origin"  
            selected= {handleChange}
          />

          <SearchBar 
            type = "destination"  
            selected= {handleChange}
          />

      </section>

      {/*  Map results of the flights  */}
      <section className="flex flex-col items-center gap-5">

        {
          flights.map((flight) => (
            <FlightCard 
              key={flight.id} 
              flight={flight} 
            />
          ))
        }

      </section>

    </main>
  );
}
