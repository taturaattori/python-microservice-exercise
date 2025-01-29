# Python Microservice

## Description

This project is a microservice designed to get the weather data for a given city. Written in Python using Flask. Weather data is from https://www.weatherapi.com/.
Exercise for Tampere University Sustainable software engineering course.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/taturaattori/python-microservice.git
   ```
2. Navigate to the project directory:
   ```sh
   cd python-microservice
   ```
3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Get your WeatherAPI key and create a .env file for it:
   ```
   API_KEY=
   ```

## Usage

1. Start the microservice:
   ```sh
   python app.py
   ```
2. Access the API endpoints at `http://localhost:8000`

## API Endpoints

- `GET /weather/{city}` - Fetch weather data for the given city
