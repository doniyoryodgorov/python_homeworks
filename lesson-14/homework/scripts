#Task 1: JSON Parsing
#write a Python script that reads the students.jon JSON file and prints details of each student.

import json

with open(students.json) as file:
    students_data = json.load(file)

for student in students_data['students']:
    print(f"student_ID:{student.get('student_ID')}")
    print(f"student_name:{student.get('student_name')}")
    print(f"student_age:{student.get('student_age')}")
    print(f"grade:{student.get('grade')}")
    print(f"courses:{student.get('courses')}")

# Task 2 : Weather API
#Use this url : https://openweathermap.org/
#Use the requests library to fetch weather data for a specific city(ex. your hometown: Tashkent) and print relevant information (temperature, humidity, etc.).

import requests


API_KEY = "05821e88798bfa488b21aca77e7dbbb5"  
CITY = "Tashkent"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": CITY,
    "appid": API_KEY,
    "units": "metric"  
}


response = requests.get(BASE_URL, params=params)


if response.status_code == 200:
    data = response.json()  
    
    
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather_condition = data["weather"][0]["description"]
    wind_speed = data["wind"]["speed"]

    
    print(f"Weather in {CITY}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {weather_condition.capitalize()}")
    print(f"Wind Speed: {wind_speed} m/s")

else:
    print("Failed to fetch weather data. Check your API key or city name.")

#Task 4: Movie Recommendation System
#Use this url http://www.omdbapi.com/ to fetch information about movies.
#Create a program that asks users for a movie genre and recommends a random movie from that genre.

import requests
import random


API_KEY = "f6a450c7"  

BASE_URL = "http://www.omdbapi.com/"


GENRES = ["Action", "Comedy", "Drama", "Horror", "Sci-Fi", "Romance", "Thriller", "Adventure", "Animation"]


def fetch_movies(genre):
    url = f"{BASE_URL}?apikey={API_KEY}&s={genre}&type=movie"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if "Search" in data:
            return data["Search"]  # Returns a list of movies
        else:
            print("❌ No movies found for this genre.")
            return []
    else:
        print("❌ Error fetching movie data.")
        return []


def recommend_movie():
    print("\n🎬 Available Genres:", ", ".join(GENRES))
    genre = input("Enter a genre (e.g., Action, Comedy, Drama): ").capitalize()
    
    if genre not in GENRES:
        print("❌ Invalid genre! Please enter a valid genre from the list.")
        return
    
    movies = fetch_movies(genre)
    
    if movies:
        movie = random.choice(movies)  # Select a random movie
        print("\n🎥 Recommended Movie:")
        print(f"📌 Title: {movie['Title']}")
        print(f"📅 Year: {movie['Year']}")
        print(f"🆔 IMDb ID: {movie['imdbID']}")
        print(f"🔗 More Info: https://www.imdb.com/title/{movie['imdbID']}/")

if __name__ == "__main__":
    recommend_movie()



