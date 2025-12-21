import axios from "axios"
import { useState } from "react"

interface LocationItem{
    [iataCode: string]: string;
}


const SearchBar = () => {

    const apiUrl = process.env.NEXT_PUBLIC_BACK_URL || ""

    const [locations, setLocations] = useState<LocationItem[]>([])

    const [input, setInput] = useState("")


    const fetchData = async (value: string) => {

        if (!value) {
            setLocations([]);
            return;
        }
        try {
            const response = await axios.get(`${apiUrl}/locations?keyword=${value}`)
            setLocations(response.data)
            console.log(response.data)
        }catch (error){
            console.error(`Error getting data ${error}`)
        }
    }

    const handleChange = (value: string) => {
        setInput(value)
        fetchData(value)
    }

    return (
        <div className="border-2 border-solid rounded-2xl p-1.5 w-max ">
            <input 
                className="decoration-transparent border-0 h-max outline-0 " 
                placeholder="Airport"
                value={input}
                onChange={(e) => handleChange(e.target.value)}
            />
        </div>
    )
}

export default SearchBar