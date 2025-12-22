'use client'

import DatePicker from "@/components/DatePicker";
import FlightCard from "@/components/FlightCard";
import SearchBar from "@/components/SearchBar";
import { useState } from "react";
import axios from "axios"

import { FlightData } from "../types/flight";

export default function Home() {

  const apiUrl = process.env.NEXT_PUBLIC_BACK_URL || ""

  const [flights, setFlights] = useState<FlightData[]>([])
  const [loading, setLoading] = useState(false)

  const [form, setForm] = useState(
    {
      origin: "",
      destination: "",
      departure_date : "",
    }
  )

  const handleChange = (name: string, value: string ) => {
    setForm(
      {
        ...form,
        [name] : value
      }
    )
    console.log(value)
  }

  const fetchData = async () => {

        try {
            setLoading(true)
            const response = await axios.get(`${apiUrl}/flights?departure_date=${form.departure_date}&destination=${form.destination}&origin=${form.origin}`)
            setFlights(response.data)
            console.log(response.data)
        }catch (error){
            console.error(`Error getting data ${error}`)
        } finally {
            setLoading(false)
        }
    }

  const handleSearch = () => {
    if (form.origin && form.destination && form.departure_date) {
      fetchData()
    } else {
      alert("Please fill all fields")
    }
  }

  return (
    <>

      <header className="flex flex-row justify-center text-lg font-semibold italic">
        <h1>Amadeus Flight Search</h1>
      </header>

      {/* Search engine for flights */}
      <section className="flex flex-col gap-4 p-6 max-w-4xl mx-auto">

          <SearchBar 
            type = "origin"  
            selected= {handleChange}
          />

          <SearchBar 
            type = "destination"  
            selected= {handleChange}
          />

          <DatePicker
            value={form.departure_date}
            onChange={(date) => handleChange("departure_date", date)}
          />

          <button 
            onClick={handleSearch}
            disabled={!form.origin || !form.destination || !form.departure_date || loading}
            className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-3 px-6 rounded-lg disabled:bg-gray-400 disabled:cursor-not-allowed transition-colors cursor-pointer"
          >
            {loading ? "Searching..." : "Search Flights"}
          </button>

      </section>

      {/*  Map results of the flights  */}
      <section className="flex flex-col items-center gap-5">

        {!loading && flights.map((flight) => (
            <FlightCard 
              key={flight.id} 
              flight={flight} 
            />
          ))
        }

      </section>

    </>
  );
}
