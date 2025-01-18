import requests
import streamlit as st

import os
from dotenv import load_dotenv

load_dotenv()

SERPER_API_KEY = "9f129e7be4f3385e5e1d2db817f344e7451de290"
FOURSQUARE_API_KEY = "fsq3iDsC2pCBpIsX6boS2vJzvADc1HeHmBFHRXFOE/+ujzU="
OPENWEATHER_API_KEY = "4f810fbc16783e4a18cfe46cdf064876"

def get_destination_recommendations(destination):
    """
    Fetch destination recommendations from Serper API
    
    Args:
        destination (str): Destination to search for
    
    Returns:
        list: List of travel recommendations
    """
    try:
        url = f'https://google.serper.dev/search?q={destination} travel guide&num=10'
        headers = {
            'X-API-KEY': SERPER_API_KEY,
            'Content-Type': 'application/json'
        }
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            recommendations = []
            for item in data.get('organic', []):
                if 'travel' in item.get('title', '').lower() or 'guide' in item.get('title', '').lower():
                    recommendations.append(item)
            return recommendations
        else:
            st.error(f"Error fetching recommendations: {response.status_code}")
            return []
    except Exception as e:
        st.error(f"Error in destination recommendations: {str(e)}")
        return []

def get_weather_info(destination):
    """
    Fetch weather information for a destination
    
    Args:
        destination (str): City or location name
    
    Returns:
        dict: Weather information or None if fetch fails
    """
    try:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={destination}&appid={OPENWEATHER_API_KEY}&units=metric'
        response = requests.get(url)
        
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Error fetching weather: {response.status_code}")
            return None
    except Exception as e:
        st.error(f"Error in weather fetch: {str(e)}")
        return None

def get_attractions(destination):
    """
    Fetch tourist attractions for a destination
    
    Args:
        destination (str): City or location name
    
    Returns:
        list: List of attractions
    """
    try:
        url = "https://api.foursquare.com/v3/places/search"
        headers = {
            "Accept": "application/json",
            "Authorization": FOURSQUARE_API_KEY
        }
        params = {"query": "tourist attractions", "near": destination, "limit": 10}
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            return response.json().get('results', [])
        else:
            st.error(f"Error fetching attractions: {response.status_code}")
            return []
    except Exception as e:
        st.error(f"Attractions fetch error: {e}")
        return []