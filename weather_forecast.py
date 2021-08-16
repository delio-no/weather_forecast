import requests

APPID = "b4534e0524a27721f663d669f5581780" 
URL_BASE = "http://api.openweathermap.org/data/2.5/"
def current_weather(lat: float, lon: float,units: str = "metric", appid: str = APPID) -> dict:
    print(locals(), end='\n=========\n')
    res = requests.get(URL_BASE + "weather", params=locals()).json()
    return res["main"]["temp"]

if __name__ == "__main__":
    while True:
        (latitude) = input("Enter a location:").strip()
        (longitude) = input("Enter a location:").strip()
        if latitude and longitude:
            print("Прогноз погоды: ", current_weather(latitude, longitude))

        else:
            break