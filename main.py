import json
import requests
from twilio.rest import Client
import os

URL= "http://api.openweathermap.org/data/2.5/forecast"
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
apikey = os.environ.get("OPENWEATHER_API_KEY")

LAT=22.365516
LNG=114.251748


weather_parameters={"lat":LAT,"lon":LNG,"appid":OPENWEATHER_API_KEY,"cnt":4}

response= requests.get(URL, params=weather_parameters)
response.raise_for_status()
results= response.json()


will_rain = False
for i in range(4):
    weather_id = results["list"][i]["weather"][0]["id"]
    if weather_id < 700:
        will_rain = True
if will_rain:
    twilio_client = Client(account_sid, auth_token)
    message = twilio_client.messages.create(
        body="It is going to rain today. Bring an umbrella! 🌧️",
        from_ = TWILIO_VIRTUAL_NBR,
        to=TWILIO_VERIFIED_NBR
    )
    print(message.status)






