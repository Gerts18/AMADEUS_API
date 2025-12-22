import { useState } from "react"
import Datetime from 'react-datetime'
import "react-datetime/css/react-datetime.css"
import moment from 'moment'

interface DatePickerProps {
    value: string | Date;
    onChange: (date: string) => void;
}

const DatePicker = ({ value, onChange }: DatePickerProps) => {

    const handleDateChange = (date: string | moment.Moment) => {
        if (typeof date === 'string') {
            onChange(date);
        } else {
            onChange(date.format('YYYY-MM-DD'));
        }
    }

    const isValidDate = (current: moment.Moment) => {
        const tomorrow = moment().add(1, 'day').startOf('day');
        return current.isAfter(tomorrow) || current.isSame(tomorrow, 'day');
    }

    return (
        <div className="w-full">
            <Datetime 
                value={value}
                onChange={handleDateChange}
                dateFormat="YYYY-MM-DD"
                timeFormat={false}
                isValidDate={isValidDate}
                inputProps={{
                    className: "appearance-none shadow bg-white border-2 rounded-2xl w-full p-1.5 text-black leading-tight focus:outline-none focus:shadow-outline",
                    placeholder: "departure date"
                }}
            />
        </div>
    )
}

export default DatePicker