from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("API_KEY")
URL = "http://api.weatherapi.com/v1/current.json"

@app.route("/weather/<city>", methods=["GET"])
def get_weather(city):
    
    response = requests.get(f"{URL}?key={API_KEY}&q={city}&aqi=no")

    if response.status_code != 200:
        return jsonify({"error": "Something went wrong while fetching the weather data. Check the given parameter"}), 400
    
    data = response.json()

    return jsonify({
        "city": data["location"]["name"],
        "country": data["location"]["country"],
        "temperature": data["current"]["temp_c"],
        "condition": data["current"]["condition"]["text"]
    })

if __name__ == "__main__":
    app.run(port=8000)