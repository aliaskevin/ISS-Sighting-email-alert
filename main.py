import requests
import smtplib
from datetime import datetime
import time

# Enter latitude and longitude of your location
LAT = 10.16
LONG = 76.37
# Fill your email id and password to sent email
my_email = "email id"
passw = "password"
parameters = {
    "lat": LAT,
    "lng": LONG,
    "formatted":0
}

while True:
  # checking time of sunrise and sunset time
    sun_response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters, )
    sun_data = sun_response.json()
    sunrise = int(sun_data['results']['sunrise'].split("T")[1].split(":")[0])
    sunset = int(sun_data['results']['sunset'].split("T")[1].split(":")[0])
    #  checking current ISS postion
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_data = iss_response.json()
    longitude = float(iss_data["iss_position"]["longitude"])
    latitude = float(iss_data["iss_position"]["latitude"])
    
    hour = datetime.now().hour
   # checking if ISS is above your location to alert you by email
    if 5<= latitude <= 15 and 71<= longitude <=81 and sunset <= hour <= sunrise:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=passw)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="youremail@gmail.com",
                msg="Subject:LOOK UP FOR ISS\n\nHi\nYou can see ISS up in the SKY"
            )
    else:
        print("not yet")
    time.sleep(60)
print(hour)
