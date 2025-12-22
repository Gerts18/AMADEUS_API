import axios from "axios"
import { useState } from "react"

interface LocationsData{
    [iataCode: string]: string;
}

interface SearchBarProps {
    type: string;
    selected: (name: string, value: string) => void 
}

const SearchBar = ({type, selected}: SearchBarProps) => {

    const apiUrl = process.env.NEXT_PUBLIC_BACK_URL || ""

    const [locations, setLocations] = useState<LocationsData>({})

    const [input, setInput] = useState("")


    const fetchData = async (value: string) => {

        if (!value) {
            setLocations({});
            return;
        }
        try {
            /* const response = await axios.get(`${apiUrl}/locations?keyword=${value}`)
            setLocations(response.data) */
            /* console.log(response.data) */
        }catch (error){
            console.error(`Error getting data ${error}`)
        }
    }

    const handleChange = (value: string) => {
        setInput(value)
        fetchData(value)
    }

    const handleClick = (value: string[]) => {
        selected(type, value[0])
        setLocations({})
        setInput(`${value[0]} - ${value[1]}`)
    }

    return (
        <div className= "flex flex-col items-center w-full max-w-3xl mx-auto ">

            <div className=" bg-white border-2 border-solid rounded-2xl p-1.5 w-full ">
                <input 
                    className="decoration-transparent border-0 h-full outline-0 w-full " 
                    placeholder= {`${type}`}
                    value={input}
                    onChange={(e) => handleChange(e.target.value)}
                />
            </div>

            <div className="w-full rounded-2xl bg-white flex flex-col items-start max-h-40 overflow-scroll overflow-x-hidden mt-2 mb-2">
                {
                    Object.entries(locations).map(([iataCode, locationName]) => {
                        return (
                            <div 
                                key={iataCode} 
                                className="p-2 hover:bg-gray-100 w-full cursor-pointer" 
                                onClick={() => handleClick([iataCode, locationName])}
                            >
                                <span className="font-bold">{iataCode}</span> - {locationName}
                            </div>
                        );
                    })
                }
            </div>

        </div>
    )
}

export default SearchBar