'use client'

import SearchBar from "@/components/SearchBar";
import { useState } from "react";

export default function Home() {

  const [locations, setLocations] = useState([
    {
      "NYC": "NEW YORK"
    },
    {
      "JFK": "JOHN F KENNEDY INTL"
    },
    {
      "EWR": "NEWARK LIBERTY INTL"
    },
    {
      "LGA": "LAGUARDIA"
    },
    {
      "SWF": "STEWART INTERNATIONAL"
    },
    {
      "NYS": "SKYPORTS SPB"
    }
  ])

  const [flights, setFlights] = useState([])

  const [form, setForm] = useState(
    {
      departure_date : "",
      destination: "",
      origin: ""
    }
  )

  return (
    <main>

      {/* Search engine for flights */}
      <section>

        <div className= "decoration-black border-4 border-solid flex flex-col items-center max-w-3xs ">
          <SearchBar/>
          <div>SearchResults</div>
        </div>

      </section>

      {/*  Map results of the flights  */}
      <section>

      </section>

    </main>
  );
}
