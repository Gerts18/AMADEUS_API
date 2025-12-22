# Flight Search Application

A modern flight search application that allows users to search for flights and locations using the Amadeus Self-Service API. The application features a Next.js frontend with TypeScript and a Python Quart backend.

## Project Objective

This project demonstrates the integration of the Amadeus API to create a functional flight search engine. Users can:
- Search for available flights between airports
- Look up airport and city locations by keyword
- View detailed flight information including prices, routes, and itineraries

## Technologies Used

### Frontend
- **Next.js 16** - React framework for production
- **React 19** - JavaScript library for building user interfaces
- **TypeScript** - Type-safe JavaScript
- **Tailwind CSS** - Utility-first CSS framework
- **Axios** - HTTP client for API requests
- **React Datetime** - Date picker component

### Backend
- **Python 3** - Programming language
- **Quart** - Async Python web framework
- **Quart-CORS** - Cross-Origin Resource Sharing support
- **Quart-Schema** - OpenAPI/Swagger documentation
- **Amadeus Python SDK** - Official Amadeus API client
- **python-dotenv** - Environment variable management

## Prerequisites

Before you begin, ensure you have the following installed:
- **Node.js** (v18 or higher)
- **Python** (v3.8 or higher)
- **pip** (Python package manager)
- **Amadeus API credentials** (Get them from [Amadeus for Developers](https://developers.amadeus.com/))

## Setup Instructions

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
venv\Scripts\activate 
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the backend directory with your Amadeus API credentials:
```env
AMADEUS_CLIENT_ID=your_client_id_here
AMADEUS_CLIENT_SECRET=your_client_secret_here
```

5. Run the backend server:
```bash
python main.py
```

The backend will start on `http://localhost:5000`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Create a `.env.local` file in the frontend directory with the backend URL:
```env
NEXT_PUBLIC_BACK_URL=http://localhost:5000
```

4. Run the development server:
```bash
npm run dev
```

The frontend will start on `http://localhost:3000`

## API Documentation

Once the backend is running, you can access the interactive API documentation:

- **Swagger UI**: [http://localhost:5000/docs](http://localhost:5000/docs)
- **ReDoc**: [http://localhost:5000/redoc](http://localhost:5000/redoc)
- **OpenAPI JSON**: [http://localhost:5000/openapi.json](http://localhost:5000/openapi.json)

### Available Endpoints

#### GET `/flights`
Search for available flights.

**Query Parameters:**
- `origin` (string, required): IATA airport code for departure (e.g., "MEX", "BKK")
- `destination` (string, required): IATA airport code for arrival (e.g., "JFK", "SFO")
- `departure_date` (string, required): Departure date in YYYY-MM-DD format

**Example:**
```
GET /flights?origin=MEX&destination=JFK&departure_date=2025-12-25
```

#### GET `/locations`
Search for airports and cities by keyword.

**Query Parameters:**
- `keyword` (string, required): Search term for location lookup (minimum 1 character)

**Example:**
```
GET /locations?keyword=New York
```

## Project Structure

```
.
├── backend/
│   ├── amadeus_api.py      # Amadeus API integration logic
│   ├── main.py             # Quart application and endpoints
│   ├── requirements.txt    # Python dependencies
│   └── .env               # Environment variables (not tracked)
├── frontend/
│   ├── app/               # Next.js app directory
│   ├── components/        # React components
│   ├── types/            # TypeScript type definitions
│   └── package.json      # Node dependencies
└── README.md             # This file
```

## Development

### Backend
The backend uses Quart (async Flask) to handle API requests. All Amadeus API interactions are in `amadeus_api.py`, with proper error handling and data parsing.

### Frontend
The frontend is built with Next.js 16 using the App Router. Components are located in the `components/` directory, with TypeScript interfaces defined in `types/`.

## License

This project is for educational purposes as part of a technical challenge.

## Acknowledgments

- [Amadeus for Developers](https://developers.amadeus.com/) for providing the flight search API
- Built as a technical assessment project