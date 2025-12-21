'use client'

import SearchBar from "@/components/SearchBar";
import { useState } from "react";

export default function Home() {


  const [flights, setFlights] = useState([])

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
      <section>

      </section>

    </main>
  );
}
