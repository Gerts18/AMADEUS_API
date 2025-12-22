export interface LocationsData{
    [iataCode: string]: string;
}

export interface SearchBarProps {
    type: string;
    selected: (name: string, value: string) => void 
}