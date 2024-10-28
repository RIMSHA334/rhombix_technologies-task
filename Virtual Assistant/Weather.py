'''
import requests

key2='25bf65d049ad4580e255d3e6c21942f7'
api_addresses = "http://api.openweathermap.org/data/2.5/weather?q=Lahore&appid=" + key2
json_data = requests.get(api_addresses).json()

def temp():
    temprature=round(json_data["main"]["temp"]-273,1)
    return temprature

def des():
    description=json_data["weather"][0]["description"]
    return description

print(temp())
print(des())



'''
import requests

def get_weather(city_name):
    api_key = '25bf65d049ad4580e255d3e6c21942f7'
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        
        if "main" in data and "weather" in data and "name" in data and "sys" in data:
            temperature = data["main"]["temp"]
            description = data["weather"][0]["description"]
            city = data["name"]
            country = data["sys"]["country"]
            
            return f"The current temperature in {city}, {country} is {temperature}°C with {description}."
        else:
            return "Sorry, I couldn't find the weather details for that location."
    else:
        return "Sorry, I couldn't fetch the weather data right now."
